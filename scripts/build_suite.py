"""
Build the benchmark suite: one instance per (family, UC.jl 0.3 benchmark size),
plus the 80 Falkenauer "triplet" instances converted directly.

Usage:  python scripts/build_suite.py [--jobs 8] [--gurobi-time 120]
Output: instances/<family>/<name>.json.gz, solutions/<name>.solution.json,
        instances/manifest.csv
"""
from __future__ import annotations

import argparse
import csv
import json
import random
import time
import sys
import zlib
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import uchard as U  # noqa: E402

SRC = ROOT / "sources"
OUT = ROOT / "instances"
SOL = ROOT / "solutions"

# (reference benchmark in UC.jl 0.3, number of generators, horizon in hours)
UCJL_SIZES = (
    [(f"matpower-{c}", n, 36) for c, n in [
        ("case14", 5), ("case30", 6), ("case57", 7), ("case89pegase", 12), ("case118", 54),
        ("case300", 69), ("case1354pegase", 260), ("case2737sop", 267), ("case2736sp", 289),
        ("case1888rte", 296), ("case2383wp", 323), ("case1951rte", 390), ("case2746wop", 443),
        ("case2746wp", 457), ("case3120sp", 483), ("case3012wp", 496), ("case2869pegase", 510),
        ("case2848rte", 544), ("case3375wp", 590), ("case2868rte", 596), ("case6468rte", 1262),
        ("case6470rte", 1306), ("case6495rte", 1352), ("case6515rte", 1368),
        ("case9241pegase", 1445), ("case13659pegase", 4092)]]
    + [("pglib-ca", 610, 48), ("pglib-ca-Scenario400", 611, 48), ("pglib-ferc-935g", 935, 48),
       ("pglib-ferc-979g", 979, 48), ("pglib-rts_gmlc", 154, 48)]
    + [(f"orlib-{n}g", n, 24) for n in (10, 20, 50, 75, 100, 150, 200)]
    + [(f"tejada19-24h-{n}g", n, 24) for n in (
        214, 250, 290, 480, 505, 623, 647, 836, 850, 918, 931, 940, 957, 959, 1069, 1130,
        1376, 1393, 1577, 1615, 1632, 1768, 1804, 1820, 1823, 1888)]
    + [(f"tejada19-168h-{n}g", n, 168) for n in (
        36, 38, 40, 53, 58, 59, 72, 84, 86, 88, 93, 105, 110, 125, 130, 131, 140, 165, 175,
        179, 188, 192, 199)]
)

KPLIB_CLASSES = {
    "knap-spanner": "09SpannerStronglyCorrelated",
    "knap-mstr": "10MultipleStronglyCorrelated",
    "knap-pceil": "11ProfitCeiling",
    "knap-circle": "12Circle",
}
KPLIB_N = [50, 100, 200, 500, 1000, 2000, 5000]

# hardest region of Jooken et al. (2022) for combo: c=1e10, g=14, eps=1e-5
JOOKEN = dict(cap=10**10, g=14, frac=0.1, eps=1e-5, small=300)

REF_BIB = {
    "bendotti": "Bendotti, Fouilhoux, Rottner (2019) On the complexity of the Unit Commitment "
                "Problem, Ann. Oper. Res. 274:119-130, Thm 1 (3-Partition -> MUCP)",
    "tseng": "Tseng (1996) PhD thesis UC Berkeley (knapsack -> UC, T=1)",
    "falk": "Falkenauer (1996) triplet instances, via BPPLIB (Delorme, Iori, Martello)",
    "kplib": "Pisinger (2005) Where are the hard knapsack problems?, instances from "
             "github.com/likr/kplib",
    "jooken": "Jooken, Leyman, De Causmaecker (2022) A new class of hard problem instances "
              "for the 0-1 knapsack problem, EJOR 301(3)",
}


def seed_of(*parts):
    return zlib.crc32("|".join(map(str, parts)).encode())


# --------------------------------------------------------------------------- tasks

def task_kpart(ref, n, T, precision):
    fam = "kpart" if precision == "int" else "kpart-hp"
    name = f"{fam}_{ref}_n{n}_T{T}"
    src = (f"Planted equal-sum partition -> UC. Reduction: {REF_BIB['bendotti']}. "
           f"Size of UC.jl benchmark {ref}. Single bus.")
    return U.make_kpart(n, T, seed_of(name), precision, name=name, source=src)


def task_falkenauer(path_str):
    path = Path(path_str)
    items, C = U.read_falkenauer(path)
    m = sum(items) // C
    name = f"falkenauer-{path.stem.split('_', 1)[1]}_n{len(items)}_T{m}"
    src = (f"Falkenauer triplet instance {path.name} ({REF_BIB['falk']}), converted with "
           f"{REF_BIB['bendotti']}: T=m={m}, D_t=(m-t)B. Known yes-instance, so the optimum is "
           f"sum_t D_t.")
    b = U.kpart_to_uc(items, C, None, m, m, last_group_stays_on=False, scale=1,
                      name=name, family="falkenauer", source=src)
    b.status = "optimal"   # every Falkenauer t-instance is built from m exact triplets
    return b


def task_kplib(ref, n, T, fam):
    cls = KPLIB_CLASSES[fam]
    name = f"{fam}_{ref}_n{n}_T{T}"
    rng = random.Random(seed_of(name))
    n_items = n - 1
    kn = next(k for k in KPLIB_N if k >= n_items)
    f = SRC / "kplib" / cls / f"n{kn:05d}" / "R01000" / f"s00{rng.randrange(5)}.kp"
    items, _ = U.read_kp(f)
    items = rng.sample(items, n_items)
    base = json.loads((SRC / "orlib_10_0_1_w_load.json").read_text())
    W = sum(w for _, w in items)
    loads = [int(round(r * W)) for r in U.load_profile(base, T)]
    t0 = time.perf_counter()
    dp = U.knapsack_dp_all_capacities(items, max(loads))
    kp = [int(dp[D]) for D in loads]
    dp_time = time.perf_counter() - t0
    src = (f"0-1 knapsack -> UC, one knapsack per period ({REF_BIB['tseng']}). Items: "
           f"{n_items} items sampled from {cls}/{f.parent.parent.name}/{f.name} "
           f"({REF_BIB['kplib']}). Capacity D_t follows the OR-LIB daily load shape, "
           f"in [0.3, 0.7]*sum(w). Size of UC.jl benchmark {ref}.")
    b = U.knapsack_to_uc(items, loads, name, fam, src, kp, kp)
    b.meta["dp_runtime_s"] = round(dp_time, 3)
    return b


def solve_kp_gurobi(items, cap, time_limit):
    import gurobipy as gp
    m = gp.Model()
    m.Params.OutputFlag = 0
    m.Params.Threads = 1
    m.Params.TimeLimit = time_limit
    m.Params.MIPGap = 0
    m.Params.MIPGapAbs = 0.5
    m.Params.FeasibilityTol = 1e-9
    m.Params.IntFeasTol = 1e-9
    m.Params.NumericFocus = 3
    x = m.addVars(len(items), vtype=gp.GRB.BINARY)
    m.setObjective(gp.quicksum(p * x[i] for i, (p, _) in enumerate(items)), gp.GRB.MAXIMIZE)
    m.addConstr(gp.quicksum(w * x[i] for i, (_, w) in enumerate(items)) <= cap)
    m.optimize()
    sel = [i for i in range(len(items)) if x[i].X > 0.5]
    # integer repair: tolerances may leave the solution slightly over capacity
    repaired = False
    while sum(items[i][1] for i in sel) > cap:
        sel.remove(min(sel, key=lambda i: items[i][0] / items[i][1]))
        repaired = True
    best = sum(items[i][0] for i in sel)
    bound = int(m.ObjBound + 1e-6)          # floor of Gurobi's dual bound
    if m.Status == 2 and not repaired:
        bound = best
    bound = max(bound, best)
    return best, bound, m.Runtime


def task_jooken(ref, n, T, time_limit):
    name = f"jooken_{ref}_n{n}_T{T}"
    rng = random.Random(seed_of(name))
    items, cap = U.jooken_items(n - 1, rng=rng, **JOOKEN)
    best, bound, rt = solve_kp_gurobi(items, cap, time_limit)
    loads = [cap] * T
    src = (f"0-1 knapsack -> UC ({REF_BIB['tseng']}). Items: generator of {REF_BIB['jooken']}, "
           f"params n={n - 1} {JOOKEN}. Same knapsack in every period (constant demand = c). "
           f"Size of UC.jl benchmark {ref}.")
    b = U.knapsack_to_uc(items, loads, name, "jooken", src, [best] * T, [bound] * T)
    b.meta["gurobi_kp_runtime_s"] = round(rt, 2)
    return b


# --------------------------------------------------------------------------- main

def save(b: U.Built):
    U.write_json_gz(b.instance, OUT / b.family / f"{b.name}.json.gz")
    if b.solution is not None:
        SOL.mkdir(parents=True, exist_ok=True)
        (SOL / f"{b.name}.solution.json").write_text(json.dumps(b.solution, indent=1))
    return {
        "name": b.name, "family": b.family, "file": f"{b.family}/{b.name}.json.gz",
        "n_generators": b.n_generators, "T": b.T,
        "best_known_objective": b.optimum, "lower_bound": b.lower_bound, "status": b.status,
        "source": b.instance["SOURCE"], "meta": json.dumps(b.meta),
    }


def run(task):
    fn, args = task
    return save(globals()[fn](*args))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", type=int, default=8)
    ap.add_argument("--gurobi-time", type=float, default=120.0)
    ap.add_argument("--only", default=None, help="comma-separated families")
    a = ap.parse_args()

    tasks = []
    for ref, n, T in UCJL_SIZES:
        tasks.append(("task_kpart", (ref, n, T, "int")))
        tasks.append(("task_kpart", (ref, n, T, "hp")))
        for fam in KPLIB_CLASSES:
            tasks.append(("task_kplib", (ref, n, T, fam)))
        if n - 1 >= 100:
            tasks.append(("task_jooken", (ref, n, T, a.gurobi_time)))
    for p in sorted((SRC / "falkenauer_T").glob("*.txt")):
        tasks.append(("task_falkenauer", (str(p),)))
    if a.only:
        keep = set(a.only.split(","))
        fam_of = {"task_kpart": lambda x: "kpart" if x[3] == "int" else "kpart-hp",
                  "task_kplib": lambda x: x[3], "task_jooken": lambda x: "jooken",
                  "task_falkenauer": lambda x: "falkenauer"}
        tasks = [t for t in tasks if fam_of[t[0]](t[1]) in keep]

    rows = []
    with ProcessPoolExecutor(a.jobs) as ex:
        futs = {ex.submit(run, t): t for t in tasks}
        for i, f in enumerate(as_completed(futs), 1):
            r = f.result()
            rows.append(r)
            print(f"[{i}/{len(tasks)}] {r['name']} {r['status']} opt={r['best_known_objective']}",
                  flush=True)

    man = OUT / "manifest.csv"
    old = []
    if a.only and man.exists():
        names = {r["name"] for r in rows}
        old = [r for r in csv.DictReader(man.open()) if r["name"] not in names]
    rows = sorted(old + rows, key=lambda r: (r["family"], int(r["n_generators"]), r["name"]))
    with man.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print("wrote", man, len(rows), "rows")


if __name__ == "__main__":
    main()

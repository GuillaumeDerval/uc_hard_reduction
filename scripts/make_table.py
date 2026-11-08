"""Write INSTANCES.md and instances/summary.csv: one row per instance with the bus count,
generator count, horizon, and best known objective. Counts are read from the JSON files."""
import csv
import gzip
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
rows = list(csv.DictReader((ROOT / "instances" / "manifest.csv").open()))

ORDER = ["kpart", "kpart-hp", "knap-spanner", "knap-mstr", "knap-pceil", "knap-circle",
         "jooken", "falkenauer"]


def fmt(x):
    v = float(x)
    return f"{int(v):,}".replace(",", " ") if v.is_integer() else f"{v:,.3f}".replace(",", " ")


# certificate timings
dp_t = {}
f = ROOT / "results" / "certificate_dp_times.csv"
if f.exists():
    dp_t = {r["name"]: float(r["dp_runtime_s"]) for r in csv.DictReader(f.open())}
# UC.jl + Gurobi benchmark (all shards)
grb = {}
GRB_DIR = ROOT / "results" / "gurobi_60s"
CONTENDED = not GRB_DIR.exists()
if CONTENDED:
    GRB_DIR = ROOT / "results" / "gurobi_60s_contended_run"
for f in sorted(GRB_DIR.glob("shard*.csv")):
    for r in csv.DictReader(f.open()):
        grb[r["name"]] = r


def certificate(r):
    fam, meta = r["family"], json.loads(r["meta"])
    if fam in ("kpart", "kpart-hp"):
        return "planted partition", None
    if fam == "falkenauer":
        return "benchmark construction", None
    if fam == "jooken":
        return "Gurobi on knapsack (≤120 s, 1 thread)", meta.get("gurobi_kp_runtime_s")
    return "exact knapsack DP", dp_t.get(r["name"])


def gurobi_cell(name, best):
    g = grb.get(name)
    if g is None:
        return "pending", "", "", ""
    st = {"OPTIMAL": "optimal", "TIME_LIMIT": "time limit"}.get(g["status"], g["status"])
    obj = float(g["objective"]) if g["has_solution"] == "true" else None
    gap = "" if obj is None else (0.0 if best == 0 else (obj - best) / abs(best))
    if g["consistent"] != "true":
        st += " ⚠ INCONSISTENT"
    return st, float(g["solve_time_s"]), obj, gap


out = []
for r in rows:
    with gzip.open(ROOT / "instances" / r["file"], "rt") as f:
        d = json.load(f)
    p = d["Parameters"]
    T = int(p["Time horizon (h)"] * 60 / p.get("Time step (min)", 60))
    best, lb = float(r["best_known_objective"]), float(r["lower_bound"])
    gap = (best - lb) / best if best else 0.0
    out.append({
        "instance": r["name"], "family": r["family"], "file": r["file"],
        "buses": len(d["Buses"]), "generators": len(d["Generators"]), "horizon_h": T,
        "best_known_objective": r["best_known_objective"], "lower_bound": r["lower_bound"],
        "status": r["status"], "gap": gap,
    })
    m, t = certificate(r)
    gs, gt, go, gg = gurobi_cell(r["name"], best)
    out[-1].update({"certificate_method": m, "certificate_time_s": "" if t is None else t,
                    "gurobi_uc_status": gs, "gurobi_uc_time_s": gt,
                    "gurobi_uc_objective": "" if go is None else go,
                    "gurobi_uc_excess_vs_best": gg})
    assert out[-1]["generators"] == int(r["n_generators"]) and T == int(r["T"])

out.sort(key=lambda r: (ORDER.index(r["family"]), r["generators"], r["horizon_h"], r["instance"]))

with (ROOT / "instances" / "summary.csv").open("w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["instance", "family", "file", "buses", "generators",
                                      "horizon_h", "best_known_objective", "lower_bound",
                                      "status", "gap", "certificate_method",
                                      "certificate_time_s", "gurobi_uc_status",
                                      "gurobi_uc_time_s", "gurobi_uc_objective",
                                      "gurobi_uc_excess_vs_best"])
    w.writeheader()
    w.writerows(out)

n_opt = sum(r["status"] == "optimal" for r in out)
L = ["# Instance table", "",
     f"{len(out)} instances, {n_opt} with a proven optimum. Objective = UnitCommitment.jl 0.3 "
     "objective (production + startup costs + power balance penalty).",
     "**Status**: `optimal` = proven optimal value; `feasible` = best known value, with the "
     "proven lower bound and relative gap shown.", "",
     "**Certificate**: how the best known objective was obtained, and how long it took.",
     "**UC.jl + Gurobi**: the instance solved directly with UnitCommitment.jl 0.3 (default "
     "formulation) and Gurobi 12, 1 thread, 60 s limit. `excess` = (incumbent − best known) / best "
     "known; `—` = no incumbent found.", "",
     *(["> **Warning: preliminary Gurobi timings.** This run used 8 parallel processes on a 16 GB "
        "machine whose swap was full. Times are wall-clock and heavily inflated (one build took "
        "200 s real for 14 s CPU). Statuses and incumbents are valid and all consistent with the "
        "best known values. A clean re-run is pending.", ""] if CONTENDED else []),
     "Machine-readable version: `instances/summary.csv`.", ""]
for fam in ORDER:
    fr = [r for r in out if r["family"] == fam]
    if not fr:
        continue
    L += [f"## {fam} ({len(fr)} instances)", "",
          "| instance | buses | generators | horizon (h) | best known objective | status "
          "| certificate | certificate time (s) | UC.jl + Gurobi (60 s) | Gurobi time (s) |",
          "|---|---:|---:|---:|---:|---|---|---:|---|---:|"]
    for r in fr:
        st = r["status"]
        if st != "optimal":
            st = f"feasible (LB {fmt(r['lower_bound'])}, gap {r['gap']:.2e})"
        ct = "—" if r["certificate_time_s"] == "" else f"{r['certificate_time_s']:.2f}"
        gs = r["gurobi_uc_status"]
        if gs not in ("pending", "optimal") and not gs.startswith("optimal"):
            gs += (", excess —" if r["gurobi_uc_objective"] == ""
                   else f", excess {100 * r['gurobi_uc_excess_vs_best']:.2f} %")
        gt = "" if r["gurobi_uc_time_s"] == "" else f"{r['gurobi_uc_time_s']:.2f}"
        L.append(f"| `{r['instance']}` | {r['buses']} | {r['generators']} | {r['horizon_h']} | "
                 f"{fmt(r['best_known_objective'])} | {st} | {r['certificate_method']} | {ct} | "
                 f"{gs} | {gt} |")
    L.append("")
(ROOT / "INSTANCES.md").write_text("\n".join(L))
print(f"{len(out)} rows, {n_opt} optimal")

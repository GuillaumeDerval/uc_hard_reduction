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
    assert out[-1]["generators"] == int(r["n_generators"]) and T == int(r["T"])

out.sort(key=lambda r: (ORDER.index(r["family"]), r["generators"], r["horizon_h"], r["instance"]))

with (ROOT / "instances" / "summary.csv").open("w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["instance", "family", "file", "buses", "generators",
                                      "horizon_h", "best_known_objective", "lower_bound",
                                      "status", "gap"])
    w.writeheader()
    w.writerows(out)

n_opt = sum(r["status"] == "optimal" for r in out)
L = ["# Instance table", "",
     f"{len(out)} instances, {n_opt} with a proven optimum. Objective = UnitCommitment.jl 0.3 "
     "objective (production + startup costs + power balance penalty).",
     "**Status**: `optimal` = proven optimal value; `feasible` = best known value, with the "
     "proven lower bound and relative gap shown.", "",
     "Machine-readable version: `instances/summary.csv`.", ""]
for fam in ORDER:
    fr = [r for r in out if r["family"] == fam]
    if not fr:
        continue
    L += [f"## {fam} ({len(fr)} instances)", "",
          "| instance | buses | generators | horizon (h) | best known objective | status |",
          "|---|---:|---:|---:|---:|---|"]
    for r in fr:
        st = r["status"]
        if st != "optimal":
            st = f"feasible (LB {fmt(r['lower_bound'])}, gap {r['gap']:.2e})"
        L.append(f"| `{r['instance']}` | {r['buses']} | {r['generators']} | {r['horizon_h']} | "
                 f"{fmt(r['best_known_objective'])} | {st} |")
    L.append("")
(ROOT / "INSTANCES.md").write_text("\n".join(L))
print(f"{len(out)} rows, {n_opt} optimal")

"""Add explicit ramp / startup / shutdown limits (= the unit's Pmax) to every generated
instance, in place. These limits are never binding, but UnitCommitment.jl 0.3 silently
defaults them to 1e6 MW, which would constrain units larger than 1e6 MW. New builds
(uchard.uc_generator) already write them; this script upgrades files built before."""
import gzip
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KEYS = ("Ramp up limit (MW)", "Ramp down limit (MW)", "Startup limit (MW)",
        "Shutdown limit (MW)")
n = 0
for f in sorted((ROOT / "instances").glob("*/*.json.gz")):
    d = json.load(gzip.open(f, "rt"))
    for g in d["Generators"].values():
        pmax = max(g["Production cost curve (MW)"])
        for k in KEYS:
            g[k] = pmax
    with gzip.open(f, "wt", encoding="utf-8") as out:
        json.dump(d, out, separators=(",", ":"))
    n += 1
print("updated", n, "files")

"""Time the exact knapsack DP that certifies the optimum of every knap-* instance (one process
per instance, run in parallel). Also checks that the optimum is reproduced exactly.
Writes results/certificate_dp_times.csv."""
import csv
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import build_suite as S  # noqa: E402


def one(args):
    ref, n, T, fam = args
    b = S.task_kplib(ref, n, T, fam)
    return b.name, b.optimum, b.meta["dp_runtime_s"]


if __name__ == "__main__":
    man = {r["name"]: r for r in csv.DictReader((ROOT / "instances/manifest.csv").open())}
    tasks = [(ref, n, T, fam) for ref, n, T in S.UCJL_SIZES for fam in S.KPLIB_CLASSES]
    out = ROOT / "results" / "certificate_dp_times.csv"
    out.parent.mkdir(exist_ok=True)
    with ProcessPoolExecutor(int(sys.argv[1]) if len(sys.argv) > 1 else 8) as ex, out.open("w") as f:
        f.write("name,dp_runtime_s\n")
        for name, opt, t in ex.map(one, tasks):
            assert opt == float(man[name]["best_known_objective"]), name
            f.write(f"{name},{t}\n")
    print("wrote", out)

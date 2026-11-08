"""
Reductions from NP-hard problems to the Unit Commitment Problem (UCP),
written in the UnitCommitment.jl 0.3 JSON format
(https://anl-ceeesa.github.io/UnitCommitment.jl/0.3/format/).

Two reductions are implemented. Both are linear in the number of generators.

1. Equal-sum k-partition -> multi-period UC (strongly NP-hard).
   This generalises Theorem 1 of Bendotti, Fouilhoux & Rottner (2019),
   "On the complexity of the Unit Commitment Problem", Ann. Oper. Res. 274:119-130.
   One generator per item, with Pmin = Pmax = a_i. Every unit starts ON.
   Min-down = T, so a unit that shuts down can never restart.
   The demand is a staircase that drops by B at chosen periods.
   Cost: a_i $/h while on (1 $/MW), so the total cost is >= sum_t D_t.
   That bound is reached iff the items can be split into groups of sum B.
   For planted (yes) instances, the optimum is known exactly.

2. 0-1 knapsack -> UC, one knapsack per period (weakly NP-hard).
   This is Tseng (1996) for T = 1, in its "minimise cost" form.
   Each item i becomes a block unit with Pmin = Pmax = w_i and cost
   f_i = c_s*w_i - p_i. One extra flexible "peaker" unit covers [0, Dmax]
   at c_s $/MW. With c_s >= max p_i/w_i:
        cost_t = c_s*D_t - (sum of p_i over the units that are ON)
   with sum w_i <= D_t, so  OPT_UC = sum_t (c_s*D_t - KP(D_t)).
   The power-balance penalty is set to max(max_i p_i, c_s) + 1. This makes
   both over- and under-production unprofitable (see README for the proof).
"""
from __future__ import annotations

import gzip
import json
import math
import random
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

# --------------------------------------------------------------------------
# UC.jl JSON helpers
# --------------------------------------------------------------------------


def _num(x):
    """Return an int when the value is integral, else a float (keeps JSON compact)."""
    if isinstance(x, (int, np.integer)):
        return int(x)
    xf = float(x)
    return int(xf) if xf.is_integer() and abs(xf) < 2**53 else xf


def uc_generator(mw, cost, init_status, init_power, min_up=1, min_down=1,
                 startup_cost=0.0, bus="b1"):
    return {
        "Bus": bus,
        "Production cost curve (MW)": [_num(v) for v in mw],
        "Production cost curve ($)": [_num(v) for v in cost],
        "Startup costs ($)": [_num(startup_cost)],
        "Startup delays (h)": [int(min_down)],  # first delay must equal min downtime
        "Minimum uptime (h)": int(min_up),
        "Minimum downtime (h)": int(min_down),
        "Initial status (h)": int(init_status),
        "Initial power (MW)": _num(init_power),
        "Must run?": False,
        # Explicit, never binding: UC.jl 0.3 silently defaults these to 1e6 MW
        # (the docs say +inf), which would cut the Jooken / large knapsack units.
        **{k: _num(max(mw)) for k in ("Ramp up limit (MW)", "Ramp down limit (MW)",
                                     "Startup limit (MW)", "Shutdown limit (MW)")},
    }


def uc_instance(T, load, generators, penalty, source):
    return {
        "SOURCE": source,
        "Parameters": {
            "Version": "0.3",
            "Time horizon (h)": int(T),
            "Power balance penalty ($/MW)": _num(penalty),
        },
        "Buses": {"b1": {"Load (MW)": [_num(v) for v in load]}},
        "Generators": generators,
    }


def write_json_gz(obj, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8") as f:
        json.dump(obj, f, separators=(",", ":"))


@dataclass
class Built:
    name: str
    family: str
    instance: dict
    n_generators: int
    T: int
    optimum: float | None          # best known objective value
    lower_bound: float | None      # proven lower bound
    status: str                    # "optimal" | "feasible" | "unknown"
    meta: dict = field(default_factory=dict)
    solution: dict | None = None   # optional certificate


# --------------------------------------------------------------------------
# Reduction 1: equal-sum k-partition -> UC (Bendotti et al. 2019, Thm 1)
# --------------------------------------------------------------------------


def group_sizes(n, G):
    q, r = divmod(n, G)
    return [q + 1] * r + [q] * (G - r)


def planted_group(rng: random.Random, k: int, B: int):
    """k positive integers summing to B. For k>=3 they lie strictly in (B/(k+1), B/(k-1))
    when that range is wide enough. This is the classical 3-partition bound for k=3,
    which forces every group of sum B to have exactly k items. Otherwise they lie in
    [B/(2k), 3B/(2k)]."""
    if k == 1:
        return [B]
    if k == 2:
        a = rng.randint(B // 4, B - B // 4)
        return [a, B - a]
    lo, hi = B // (k + 1) + 1, -(-B // (k - 1)) - 1
    if hi - lo < max(20, B // (4 * k)):
        lo, hi = max(1, B // (2 * k)), (3 * B) // (2 * k)
    for _ in range(1_000_000):
        xs = [rng.randint(lo, hi) for _ in range(k - 1)]
        last = B - sum(xs)
        if lo <= last <= hi:
            xs.append(last)
            rng.shuffle(xs)
            return xs
    raise RuntimeError(f"could not plant a group k={k} B={B}")


def kpart_to_uc(items, B, groups_of_item, n_groups, T, last_group_stays_on, scale,
                name, family, source, drop_periods=None):
    """items: integer sizes. groups_of_item[i]: index (0..n_groups-1) of the planted group,
    or None if unknown. scale: divide every MW value by this factor (1 or 1000).
    The planted group g shuts down at drop_periods[g] (1-based). If
    last_group_stays_on, the last group never shuts down."""
    n = len(items)
    n_drops = n_groups - 1 if last_group_stays_on else n_groups
    assert 1 <= n_drops <= T, (n_drops, T)
    if drop_periods is None:
        drop_periods = [math.ceil((j + 1) * T / n_drops) for j in range(n_drops)]
    assert len(set(drop_periods)) == n_drops
    load_int = []
    for t in range(1, T + 1):
        dropped = sum(1 for d in drop_periods if d <= t)
        load_int.append(B * (n_groups - dropped))
    assert sum(items) == B * n_groups

    gens = {}
    for i, a in enumerate(items):
        mw = a / scale
        gens[f"g{i + 1}"] = uc_generator(
            mw=[mw], cost=[mw],               # 1 $/MW -> cost a_i per period ON
            init_status=T, init_power=mw,      # ON since T hours (>= min-up = 1)
            min_up=1, min_down=T)              # cannot restart once shut down
    load = [v / scale for v in load_int]
    opt = sum(load_int) / scale
    inst = uc_instance(T, load, gens, penalty=1000.0, source=source)

    sol = None
    if groups_of_item is not None:
        shut = {}
        for i, g in enumerate(groups_of_item):
            shut[f"g{i + 1}"] = (drop_periods[g] if g < n_drops else None)
        sol = {"shutdown_period (1-based, null = stays ON)": shut,
               "objective": opt}
    return Built(name=name, family=family, instance=inst, n_generators=n, T=T,
                 optimum=opt, lower_bound=opt,
                 status="optimal" if groups_of_item is not None else "lower-bound-only",
                 meta={"B": B / scale, "n_groups": n_groups, "drops": n_drops,
                       "scale": scale},
                 solution=sol)


def make_kpart(n, T, seed, precision="int", name="", source=""):
    """Planted equal-sum partition, sized to a UC.jl benchmark (n generators, T periods).
    The number of groups G is min(T+1, max(2, n//3)), so groups have size 3
    (a real 3-partition) whenever n <= 3(T+1). One group stays ON for the whole horizon."""
    rng = random.Random(seed)
    G = min(T + 1, max(2, n // 3))
    sizes = group_sizes(n, G)
    kbar = n / G
    B = int(round(1000 * kbar / 3))               # mean unit size ~333 MW
    scale = 1
    if precision == "hp":                         # 3 decimals -> far fewer solutions
        B, scale = B * 1000, 1000
    items, gid = [], []
    for g, k in enumerate(sizes):
        for a in planted_group(rng, k, B):
            items.append(a)
            gid.append(g)
    perm = list(range(n))
    rng.shuffle(perm)
    items = [items[p] for p in perm]
    gid = [gid[p] for p in perm]
    fam = "kpart" if precision == "int" else "kpart-hp"
    return kpart_to_uc(items, B, gid, G, T, last_group_stays_on=True, scale=scale,
                       name=name, family=fam, source=source)


def read_falkenauer(path: Path):
    toks = path.read_text().split()
    n, C = int(toks[0]), int(toks[1])
    items = [int(x) for x in toks[2:2 + n]]
    return items, C


# --------------------------------------------------------------------------
# Reduction 2: 0-1 knapsack -> UC (Tseng 1996), one knapsack per period
# --------------------------------------------------------------------------


def knapsack_dp_all_capacities(items, cmax):
    """dp[c] = max profit with weight <= c, for every c in 0..cmax (exact)."""
    dp = np.zeros(cmax + 1, dtype=np.int64)
    for p, w in items:
        if w <= cmax:
            dp[w:] = np.maximum(dp[w:], dp[:-w] + p)
    return dp


def knapsack_to_uc(items, loads, name, family, source, kp_values=None, kp_bounds=None):
    """items: list of (profit, weight) integers. loads: integer demand per period (= capacity).
    kp_values[t]: best known knapsack profit for capacity loads[t].
    kp_bounds[t]: proven upper bound on that profit."""
    T = len(loads)
    cs = max(-(-p // w) for p, w in items)              # c_s = ceil(max p/w)
    penalty = max(max(p for p, _ in items), cs) + 1
    Dmax = max(loads)
    gens = {}
    for i, (p, w) in enumerate(items):
        gens[f"g{i + 1}"] = uc_generator(mw=[w], cost=[cs * w - p],
                                         init_status=-1, init_power=0)
    gens["peaker"] = uc_generator(mw=[0, Dmax], cost=[0, cs * Dmax],
                                  init_status=-1, init_power=0)
    inst = uc_instance(T, loads, gens, penalty=penalty, source=source)
    opt = lb = None
    status = "unknown"
    if kp_values is not None:
        opt = float(sum(cs * D - v for D, v in zip(loads, kp_values)))
        lb = float(sum(cs * D - u for D, u in zip(loads, kp_bounds or kp_values)))
        status = "optimal" if lb == opt else "feasible"
    return Built(name=name, family=family, instance=inst, n_generators=len(items) + 1,
                 T=T, optimum=opt, lower_bound=lb, status=status,
                 meta={"c_s": cs, "penalty": penalty,
                       "kp_profit_per_period": None if kp_values is None else list(map(int, kp_values))})


def read_kp(path: Path):
    toks = path.read_text().split()
    n, c = int(toks[0]), int(toks[1])
    items = [(int(toks[2 + 2 * i]), int(toks[3 + 2 * i])) for i in range(n)]
    return items, c


def load_profile(base_24h, T, lo=0.30, hi=0.70):
    """Daily shape (24 values, repeated) mapped linearly to [lo, hi]."""
    mn, mx = min(base_24h), max(base_24h)
    return [lo + (hi - lo) * (base_24h[t % 24] - mn) / (mx - mn) for t in range(T)]


def jooken_items(n, cap, g, frac, eps, small, rng: random.Random):
    """Python port of generator.cpp from Jooken, Leyman & De Causmaecker (2022),
    https://github.com/JorikJooken/knapsackProblemInstances (with a seeded RNG).
    Returns (profit, weight) pairs and the capacity."""
    classes = g - 1
    amount_small = int(n * frac)
    am1 = (n - amount_small) // classes
    items = []
    den = 2.0
    for _ in range(classes):
        for _ in range(am1):
            n1, n2 = rng.randint(1, small), rng.randint(1, small)
            items.append((int((1 / den + eps) * cap + n1), int((1 / den + eps) * cap + n2)))
        den *= 2
    while len(items) < n:
        items.append((rng.randint(1, small), rng.randint(1, small)))
    return items, cap

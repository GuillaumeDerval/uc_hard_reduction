# Unit Commitment instances that are hard by construction

These are Unit Commitment instances in the **UnitCommitment.jl 0.3** format
(<https://anl-ceeesa.github.io/UnitCommitment.jl/0.3/format/>). Each one comes from a
**polynomial reduction** of an NP-hard problem that has published hard instances.
The sizes (number of generators × horizon) match the UC.jl 0.3 benchmarks **one to one**:
MATPOWER (36 h), PGLIB-UC (48 h), OR-LIB (24 h), and Tejada19 (24 h and 168 h).
Every instance comes with its **best known optimum**. For most instances this value is proven
optimal (see `instances/manifest.csv`).

---

## 1. The reductions

UC notation: each unit has `Pmin`/`Pmax`, a minimum up time `L` and a minimum down time `ℓ`,
and its costs. Demand `D_t` must be met exactly. UC.jl penalises any imbalance, shortage or
surplus, through the *Power balance penalty*.

### 1.A  3-Partition / k-partition → multi-period UC (**strongly** NP-hard)

This is Theorem 1 of **Bendotti, Fouilhoux & Rottner (2019)**, *On the complexity of the Unit
Commitment Problem*, Ann. Oper. Res. 274:119–130
([preprint](https://optimization-online.org/?p=14606)).

**Source problem.** Given `3m` integers `a_i` and a bound `B` with `B/4 < a_i < B/2` and
`Σ a_i = mB`, can the `a_i` be split into `m` triplets that each sum to `B`?

**Construction** (linear: one item = one generator, `T = m`):

| parameter | value |
|---|---|
| units | `n = 3m`; unit `i` has `Pmin = Pmax = a_i` (single-point cost curve in UC.jl) |
| cost | `a_i` $ per period while on (1 $/MW); no startup cost |
| min up / min down | `L = 1`, `ℓ = T`: a unit that shuts down **can never restart** |
| initial state | every unit has been on for `T` h |
| demand | `D_t = (m − t)·B`: it **drops by B** every period |

**Proof sketch.** Cost equals total production, so every schedule costs at least `Σ_t D_t`.
Units can only shut down and never restart, so production is non-increasing. At cost
`Σ_t D_t`, the units shut down at time `t` form a set `A_t` whose sizes sum to exactly
`D_{t−1} − D_t = B`. These sets are disjoint, so they form a 3-partition. The converse is
immediate. In UC.jl, a shortfall of `e` MW saves `e` $ but costs `1000·e` $ in penalty, so the
equivalence holds with the default penalty.

**Generalisation used to match the UC.jl sizes.** With `n` generators and a fixed `T`, the
items form `G = min(T+1, max(2, ⌊n/3⌋))` groups of sum `B`. Groups have size 3 (a true
3-partition) when `n ≤ 3(T+1)`, and are larger otherwise (k-partition, still strongly
NP-hard). `G−1` groups shut down at periods spread over the horizon, and the last group stays
on. Demand is the matching staircase. The same proof applies: cost `Σ_t D_t` holds if and only
if the items split into `G` groups of sum `B`.

**What this means for a dynamic-programming algorithm:**
* The problem is strongly NP-hard, so no pseudo-polynomial algorithm exists unless P = NP.
  Discretising power does not help.
* The same paper (Thm 2) gives a DP over the joint unit states `(ε^1..ε^n)` that runs in
  `O(T² ∏_i (L_i+ℓ_i)²)`. That is polynomial for fixed `n` and exponential in `n`. With
  `ℓ_i = T`, these instances make that product as large as possible.

### 1.B  0-1 knapsack → UC (**weakly** NP-hard, already for T = 1)

This is the reduction of Tseng (1996), cited by Bendotti et al., in its cost-minimisation form.

**Source problem.** Given items `(p_i, w_i)` (profit, weight) and a capacity `C`, maximise
`Σ p_i x_i` subject to `Σ w_i x_i ≤ C`.

**Construction** (linear: `n` items become `n+1` generators):
* block unit `i`: `Pmin = Pmax = w_i`, cost `f_i = c_s·w_i − p_i`;
* one flexible **peaker** unit covering `[0, Dmax]` MW at `c_s` $/MW, with
  `c_s = ⌈max_i p_i/w_i⌉`. So every `f_i ≥ 0` and every block is cheaper per MW than the
  peaker;
* demand `D_t` = capacity; min up = min down = 1; no startup cost;
* power balance penalty `P = max(max_i p_i, c_s) + 1`.

**Equivalence.** With no imbalance, the cost of period `t` is
`c_s·D_t − Σ_{i on} p_i` subject to `Σ w_i ≤ D_t`. That is exactly the knapsack problem, so
`OPT_UC = Σ_t (c_s·D_t − KP(D_t))`.
* A **shortfall** costs `P > c_s` per MW, so running the peaker is always cheaper.
* A **surplus** of `e ≥ 1` (weights are integers) gains at most
  `KP(C+e) − KP(C) ≤ max p + c_s·e`, because `KP ≤ LP` and `LP` is `c_s`-Lipschitz.
  It costs `(c_s + P)·e`, so it never pays off.

Periods are independent. An instance with `T` periods is `T` knapsacks over the **same items**
with different capacities. This mirrors Pisinger's capacity "series" `c = h/(H+1)·Σw`.

### Other reductions from the same paper (not generated here)
* Partition / 3-Partition → **unit-cost** MUCP: polynomial for T = 1, NP-hard for
  `T = n+1` (Thm 3).
* Flow-shop with delays → **unit-power** MUCP (Thm 4).
* R3-SAT → the **pricing subproblem** of Lagrangian decomposition / column generation,
  strongly NP-hard (Thm 5).

---

## 2. Hard source instances (found online)

| source | problem | how it is used |
|---|---|---|
| **Falkenauer "triplets"** `t60/t120/t249/t501` (20 each), via [BPPLIB](https://site.unibo.it/operations-research/en/research/bpplib-a-bin-packing-problem-library) | 3-partition, B = 1000, a "yes" instance by construction | converted directly with 1.A (`T = m`) |
| **Pisinger (2005)** *Where are the hard knapsack problems?*: *spanner*, *multiple strongly correlated*, *profit ceiling* and *circle* classes; files from [kplib](https://github.com/likr/kplib) | knapsack | items sampled, then reduction 1.B |
| **Jooken, Leyman & De Causmaecker (2022)**, EJOR 301(3); [generator](https://github.com/JorikJooken/knapsackProblemInstances) | knapsack, hard for `combo` (DP + B&B) | generator ported to Python with the hardest settings: `c = 10¹⁰, g = 14, ε = 10⁻⁵, f = 0.1, s = 300` |

Copies of the source files used are in `sources/`: Falkenauer files from BPPLIB, and kplib
files under CC BY 4.0 (see `sources/kplib/README.md`). The Jooken generator is not copied,
since its repository has no license. `scripts/uchard.py::jooken_items` is a short re-implementation
of the published algorithm, with a seeded RNG.

---

## 3. Generated families

There is one instance per (family × UC.jl size), plus the 80 Falkenauer instances:

| family | reduction | generators | T | optimum |
|---|---|---|---|---|
| `kpart` | 1.A, planted partition, integer MW (B ≈ 1000·k/3) | same as UC.jl | same as UC.jl | exact (planted), with a certificate in `solutions/` |
| `kpart-hp` | same, MW with 3 decimals (1000× finer, so far fewer solutions) | same | same | exact, with a certificate |
| `knap-spanner`, `knap-mstr`, `knap-pceil`, `knap-circle` | 1.B, Pisinger items (R = 1000); demand follows the OR-LIB daily load shape scaled to [0.3, 0.7]·Σw | same | same | exact (DP over all capacities) |
| `jooken` | 1.B, Jooken items, constant demand = c | same (only ≥ 101 generators) | same | Gurobi with a 120 s limit: exact, or best known value with a bound |
| `falkenauer` | 1.A, direct conversion | 60 / 120 / 249 / 501 | 20 / 40 / 83 / 167 | exact (`Σ_t D_t`, triplets by construction) |

`instances/manifest.csv` gives, for each instance: `file`, `n_generators`, `T`,
`best_known_objective`, `lower_bound` (proven bound), `status` (`optimal` / `feasible`), the
source, and metadata (`c_s`, penalty, optimal profit per period, …).
The objective is the UC.jl objective: production + startup costs + penalties.

## 4. Caveats

* **Network**: every instance has a single bus (`b1`) and no lines, reserves or contingencies.
  For the MATPOWER sizes, only the generator count and `T` are reused.
* Units have `Pmin = Pmax` (single-point cost curve, which the format allows). Only the
  knapsack families' peaker can modulate its output.
* `kpart` / `falkenauer`: demand is a decreasing staircase, which is very artificial. These are
  the families with **real temporal coupling** (`ℓ = T`).
* Knapsack families: periods are **decoupled**, so all of the difficulty is inside each
  period. For `jooken`, every period is identical and the numbers are huge (MW values around
  10⁹–10¹⁰). This deliberate numerical worst case rules out any pseudo-polynomial DP.
* `kpart*` are planted "yes" instances. Any algorithm that reaches `Σ_t D_t` is optimal. Any
  imbalance of at least one precision unit costs at least the penalty.

* **UnitCommitment.jl 0.3 defaults**: the docs say ramp, startup and shutdown limits default to
  `+inf`, but the 0.3 reader sets them to **10⁶ MW**. That would constrain the Jooken units
  (up to ~5·10⁹ MW) and the peaker of the largest knapsack instances. All generators therefore
  set these four limits explicitly to their own `Pmax`. These limits are never binding, but they
  make the files mean the same thing in any reader.

## 5. Results (full table: [`INSTANCES.md`](INSTANCES.md))

All 667 files load with UnitCommitment.jl 0.3. Every instance was then solved with
UC.jl 0.3 (default formulation) + Gurobi 13.0.3, 1 thread, with a 60 s limit.
**All 667 results are consistent with the best known values.** Every proven optimum matches.
No incumbent is better than the best known value, and no Gurobi bound exceeds it.

| family | instances | optimum certificate | proven optimal by UC.jl + Gurobi in 60 s |
|---|---:|---|---:|
| `kpart` | 87 | planted partition | 5 |
| `kpart-hp` | 87 | planted partition | 5 |
| `falkenauer` | 80 | benchmark construction | **0** |
| `knap-spanner` | 87 | exact DP (max 48 s) | 84 |
| `knap-mstr` | 87 | exact DP | 77 |
| `knap-pceil` | 87 | exact DP | 67 |
| `knap-circle` | 87 | exact DP | 67 |
| `jooken` | 65 | Gurobi on the knapsack, 120 s (1 proven, 64 with gap ≤ 5·10⁻⁷) | 2 |

The partition-based families, which have real temporal coupling, are by far the hardest for
the MIP. Gurobi does not solve **any** Falkenauer t60 instance (60 generators, 20 periods) in
60 s, even though its bound already equals the optimum. Its incumbents are 15–280 % above the
optimum.

> The Gurobi timings in `INSTANCES.md` come from a run on an overloaded machine (8 parallel
> processes, swap full). They are wall-clock and inflated, and a clean re-run is pending.
> Raw results: `results/gurobi_60s_contended_run/`.

## 6. Reproduce / validate

```bash
python3 scripts/build_suite.py --jobs 9 --gurobi-time 120
```
This rebuilds everything. Output is deterministic, except for the Gurobi bound on `jooken`.

```bash
julia --project=<env with UC.jl 0.3 + Gurobi> scripts/bench_gurobi.jl 1 1 60 1   # shard 1 of 1, 60 s, 1 thread
python3 scripts/time_certificates.py 8                                         # times the knapsack DP certificates
python3 scripts/make_table.py                                                  # rebuilds INSTANCES.md and instances/summary.csv
```
`bench_gurobi.jl` solves every instance with UC.jl + Gurobi and checks consistency with the manifest. It can be resumed and split into shards.

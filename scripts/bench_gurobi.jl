# Solve every instance with UnitCommitment.jl 0.3 (default formulation) + Gurobi.
#   julia --project=<env> scripts/bench_gurobi.jl <shard> <nshards> <time_limit_s> <threads>
# Appends one line per instance to results/gurobi_<tl>s/shard<k>.csv (flushed immediately),
# skipping instances already present (so the run can be resumed).
# Checks consistency with the manifest: a proven optimum must equal best_known_objective;
# otherwise the incumbent must be >= best known and the bound <= best known.
using UnitCommitment, JuMP, Gurobi, Printf

const ROOT = dirname(@__DIR__)
shard, nshards = parse(Int, ARGS[1]), parse(Int, ARGS[2])
tlim, threads = parse(Float64, ARGS[3]), parse(Int, ARGS[4])

lines = readlines(joinpath(ROOT, "instances", "manifest.csv"))
hdr = split(lines[1], ",")
rows = [Dict(hdr[i] => String(f[i]) for i in 1:8) for f in (split(l, ","; limit = 9) for l in lines[2:end])]
sort!(rows, by = r -> parse(Int, r["n_generators"]) * parse(Int, r["T"]))   # small first
mine = rows[shard:nshards:end]

outdir = joinpath(ROOT, "results", "gurobi_$(Int(tlim))s")
mkpath(outdir)
out = joinpath(outdir, "shard$(shard).csv")
done = Set{String}()
if isfile(out)
    for l in readlines(out)[2:end]
        push!(done, split(l, ",")[1])
    end
else
    open(out, "w") do f
        println(f, "name,status,objective,bound,solve_time_s,build_time_s,has_solution,consistent")
    end
end

const ENV_GRB = Gurobi.Env()
for r in mine
    r["name"] in done && continue
    path = joinpath(ROOT, "instances", r["file"])
    t0 = time()
    inst = UnitCommitment.read(path)
    model = UnitCommitment.build_model(
        instance = inst,
        optimizer = optimizer_with_attributes(() -> Gurobi.Optimizer(ENV_GRB),
            "MIPGap" => 0.0, "MIPGapAbs" => 1e-6, "OutputFlag" => 0, "Threads" => threads),
    )
    tbuild = time() - t0
    UnitCommitment.optimize!(model,
        UnitCommitment.XavQiuWanThi2019.Method(time_limit = tlim, two_phase_gap = false))
    st = termination_status(model)
    has = result_count(model) > 0
    obj = has ? objective_value(model) : NaN
    bnd = objective_bound(model)
    tsolve = solve_time(model)
    ref = parse(Float64, r["best_known_objective"])
    tol = max(1e-4, 1e-7 * abs(ref))
    ok = st == MOI.OPTIMAL ? abs(obj - ref) <= tol :
         ((!has || obj >= ref - tol) && bnd <= ref + tol)
    open(out, "a") do f
        @printf(f, "%s,%s,%.6f,%.6f,%.3f,%.3f,%s,%s\n", r["name"], string(st), obj, bnd,
            tsolve, tbuild, has, ok)
    end
    model = nothing
    GC.gc()
end
println("shard $shard done")

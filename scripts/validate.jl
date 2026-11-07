# Validate the generated instances with UnitCommitment.jl 0.3 itself.
#   julia --project=<env with UnitCommitment@0.3, Gurobi, JuMP> scripts/validate.jl [max_gens] [time_limit]
# 1) every file in instances/manifest.csv must load with UnitCommitment.read
# 2) instances with <= max_gens generators are solved with UC.jl + Gurobi; the optimal
#    objective must match best_known_objective from the manifest
using UnitCommitment, JuMP, Gurobi, Printf

const ROOT = dirname(@__DIR__)
max_gens = length(ARGS) >= 1 ? parse(Int, ARGS[1]) : 60
tlim = length(ARGS) >= 2 ? parse(Float64, ARGS[2]) : 300.0

function read_manifest(path)
    lines = readlines(path)
    hdr = split(lines[1], ",")
    rows = Dict{String,String}[]
    for l in lines[2:end]
        # naive CSV: the first 8 fields contain no commas
        f = split(l, ","; limit = 9)
        push!(rows, Dict(hdr[i] => String(f[i]) for i in 1:8))
    end
    return rows
end

rows = read_manifest(joinpath(ROOT, "instances", "manifest.csv"))
const GRB_ENV = Gurobi.Env()
nload, nsolved, nok = 0, 0, 0
bad = String[]
for r in rows
    global nload, nsolved, nok
    path = joinpath(ROOT, "instances", r["file"])
    inst = UnitCommitment.read(path)
    @assert length(inst.units) == parse(Int, r["n_generators"])
    @assert inst.time == parse(Int, r["T"])
    nload += 1
    n = parse(Int, r["n_generators"])
    n <= max_gens || continue
    model = UnitCommitment.build_model(
        instance = inst,
        optimizer = optimizer_with_attributes(() -> Gurobi.Optimizer(GRB_ENV),
            "MIPGap" => 0.0, "MIPGapAbs" => 1e-6,
            "OutputFlag" => 0, "Threads" => 4),
    )
    t0 = time()
    UnitCommitment.optimize!(model,
        UnitCommitment.XavQiuWanThi2019.Method(time_limit = tlim, two_phase_gap = false))
    obj = objective_value(model)
    bnd = objective_bound(model)
    st = termination_status(model)
    nsolved += 1
    ref = r["best_known_objective"] == "" ? NaN : parse(Float64, r["best_known_objective"])
    tol = max(1e-4, 1e-7 * abs(ref))
    # proven optimal: must match; time limit: no better solution than ref, and bound <= ref
    ok = st == MOI.OPTIMAL ? abs(obj - ref) <= tol : (obj >= ref - tol && bnd <= ref + tol)
    ok && (nok += 1)
    ok || push!(bad, r["name"])
    @printf("%-60s n=%4d T=%3d %-14s obj=%.6f ref=%.6f bound=%.6f %5.1fs %s\n",
        r["name"], n, inst.time, string(st), obj, ref, bnd, time() - t0, ok ? "OK" : "MISMATCH")
    flush(stdout)
end
println("loaded $nload files; solved $nsolved; matching $nok")
isempty(bad) || println("MISMATCH: ", join(bad, " "))

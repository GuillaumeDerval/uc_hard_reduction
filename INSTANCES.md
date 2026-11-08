# Instance table

667 instances, 603 with a proven optimum. Objective = UnitCommitment.jl 0.3 objective (production + startup costs + power balance penalty).
**Status**: `optimal` = proven optimal value; `feasible` = best known value, with the proven lower bound and relative gap shown.

**Certificate**: how the best known objective was obtained, and how long it took.
**UC.jl + Gurobi**: the instance solved directly with UnitCommitment.jl 0.3 (default formulation) and Gurobi 12, 1 thread, 60 s limit. `excess` = (incumbent − best known) / best known; `—` = no incumbent found.

> **Warning: preliminary Gurobi timings.** This run used 8 parallel processes on a 16 GB machine whose swap was full. Times are wall-clock and heavily inflated (one build took 200 s real for 14 s CPU). Statuses and incumbents are valid and all consistent with the best known values. A clean re-run is pending.

Machine-readable version: `instances/summary.csv`.

## kpart (87 instances)

| instance | buses | generators | horizon (h) | best known objective | status | certificate | certificate time (s) | UC.jl + Gurobi (60 s) | Gurobi time (s) |
|---|---:|---:|---:|---:|---|---|---:|---|---:|
| `kpart_matpower-case14_n5_T36` | 1 | 5 | 36 | 59 143 | optimal | planted partition | — | optimal | 0.02 |
| `kpart_matpower-case30_n6_T36` | 1 | 6 | 36 | 71 000 | optimal | planted partition | — | optimal | 0.03 |
| `kpart_matpower-case57_n7_T36` | 1 | 7 | 36 | 82 857 | optimal | planted partition | — | optimal | 0.03 |
| `kpart_orlib-10g_n10_T24` | 1 | 10 | 24 | 64 438 | optimal | planted partition | — | optimal | 0.09 |
| `kpart_matpower-case89pegase_n12_T36` | 1 | 12 | 36 | 105 000 | optimal | planted partition | — | time limit, excess 1604.11 % | 123.32 |
| `kpart_orlib-20g_n20_T24` | 1 | 20 | 24 | 103 323 | optimal | planted partition | — | optimal | 5.00 |
| `kpart_tejada19-168h-36g_n36_T168` | 1 | 36 | 168 | 1 170 000 | optimal | planted partition | — | time limit, excess 1211.10 % | 60.49 |
| `kpart_tejada19-168h-38g_n38_T168` | 1 | 38 | 168 | 1 235 520 | optimal | planted partition | — | time limit, excess 619.20 % | 132.65 |
| `kpart_tejada19-168h-40g_n40_T168` | 1 | 40 | 168 | 1 280 448 | optimal | planted partition | — | time limit, excess 1524.74 % | 157.87 |
| `kpart_orlib-50g_n50_T24` | 1 | 50 | 24 | 215 694 | optimal | planted partition | — | time limit, excess 168.59 % | 85.50 |
| `kpart_tejada19-168h-53g_n53_T168` | 1 | 53 | 168 | 1 645 776 | optimal | planted partition | — | time limit, excess 99318.30 % | 60.09 |
| `kpart_matpower-case118_n54_T36` | 1 | 54 | 36 | 351 000 | optimal | planted partition | — | time limit, excess 42.69 % | 159.12 |
| `kpart_tejada19-168h-58g_n58_T168` | 1 | 58 | 168 | 1 783 536 | optimal | planted partition | — | time limit, excess 99314.95 % | 87.98 |
| `kpart_tejada19-168h-59g_n59_T168` | 1 | 59 | 168 | 1 813 320 | optimal | planted partition | — | time limit, excess 99304.56 % | 90.86 |
| `kpart_matpower-case300_n69_T36` | 1 | 69 | 36 | 438 000 | optimal | planted partition | — | time limit, excess 607.38 % | 73.36 |
| `kpart_tejada19-168h-72g_n72_T168` | 1 | 72 | 168 | 2 172 000 | optimal | planted partition | — | time limit, excess 99330.22 % | 107.63 |
| `kpart_orlib-75g_n75_T24` | 1 | 75 | 24 | 300 000 | optimal | planted partition | — | time limit, excess 313.69 % | 148.60 |
| `kpart_tejada19-168h-84g_n84_T168` | 1 | 84 | 168 | 2 505 000 | optimal | planted partition | — | time limit, excess 1141.53 % | 153.50 |
| `kpart_tejada19-168h-86g_n86_T168` | 1 | 86 | 168 | 2 565 120 | optimal | planted partition | — | time limit, excess 99323.45 % | 89.87 |
| `kpart_tejada19-168h-88g_n88_T168` | 1 | 88 | 168 | 2 604 336 | optimal | planted partition | — | time limit, excess 498.51 % | 131.00 |
| `kpart_tejada19-168h-93g_n93_T168` | 1 | 93 | 168 | 2 754 000 | optimal | planted partition | — | time limit, excess 99312.17 % | 110.70 |
| `kpart_orlib-100g_n100_T24` | 1 | 100 | 24 | 399 900 | optimal | planted partition | — | time limit, excess 314.26 % | 82.70 |
| `kpart_tejada19-168h-105g_n105_T168` | 1 | 105 | 168 | 3 090 000 | optimal | planted partition | — | time limit, excess 620.45 % | 1060.44 |
| `kpart_tejada19-168h-110g_n110_T168` | 1 | 110 | 168 | 3 231 249 | optimal | planted partition | — | time limit, excess 542.62 % | 980.42 |
| `kpart_tejada19-168h-125g_n125_T168` | 1 | 125 | 168 | 3 645 408 | optimal | planted partition | — | time limit, excess 99307.74 % | 992.99 |
| `kpart_tejada19-168h-130g_n130_T168` | 1 | 130 | 168 | 3 767 904 | optimal | planted partition | — | time limit, excess 906.47 % | 1017.56 |
| `kpart_tejada19-168h-131g_n131_T168` | 1 | 131 | 168 | 3 797 808 | optimal | planted partition | — | time limit, excess 99335.74 % | 908.11 |
| `kpart_tejada19-168h-140g_n140_T168` | 1 | 140 | 168 | 4 064 112 | optimal | planted partition | — | time limit, excess 99312.59 % | 542.62 |
| `kpart_orlib-150g_n150_T24` | 1 | 150 | 24 | 600 000 | optimal | planted partition | — | time limit, excess 170.66 % | 84.43 |
| `kpart_pglib-rts_gmlc_n154_T48` | 1 | 154 | 48 | 1 232 448 | optimal | planted partition | — | time limit, excess 292.62 % | 60.00 |
| `kpart_tejada19-168h-165g_n165_T168` | 1 | 165 | 168 | 4 758 000 | optimal | planted partition | — | time limit, excess 99272.38 % | 364.82 |
| `kpart_tejada19-168h-175g_n175_T168` | 1 | 175 | 168 | 5 040 060 | optimal | planted partition | — | time limit, excess 99270.86 % | 367.37 |
| `kpart_tejada19-168h-179g_n179_T168` | 1 | 179 | 168 | 5 150 034 | optimal | planted partition | — | time limit, excess 99299.50 % | 365.71 |
| `kpart_tejada19-168h-188g_n188_T168` | 1 | 188 | 168 | 5 403 795 | optimal | planted partition | — | time limit, excess 414.87 % | 965.50 |
| `kpart_tejada19-168h-192g_n192_T168` | 1 | 192 | 168 | 5 502 000 | optimal | planted partition | — | time limit, excess 99292.56 % | 359.87 |
| `kpart_tejada19-168h-199g_n199_T168` | 1 | 199 | 168 | 5 707 395 | optimal | planted partition | — | time limit, excess 99284.85 % | 594.51 |
| `kpart_orlib-200g_n200_T24` | 1 | 200 | 24 | 800 100 | optimal | planted partition | — | time limit, excess 125.86 % | 115.73 |
| `kpart_tejada19-24h-214g_n214_T24` | 1 | 214 | 24 | 855 900 | optimal | planted partition | — | time limit, excess 61.04 % | 113.97 |
| `kpart_tejada19-24h-250g_n250_T24` | 1 | 250 | 24 | 999 900 | optimal | planted partition | — | time limit, excess 38.77 % | 94.07 |
| `kpart_matpower-case1354pegase_n260_T36` | 1 | 260 | 36 | 1 559 772 | optimal | planted partition | — | time limit, excess 64.94 % | 130.72 |
| `kpart_matpower-case2737sop_n267_T36` | 1 | 267 | 36 | 1 601 730 | optimal | planted partition | — | time limit, excess 106.90 % | 60.01 |
| `kpart_matpower-case2736sp_n289_T36` | 1 | 289 | 36 | 1 734 264 | optimal | planted partition | — | time limit, excess 194.30 % | 72.38 |
| `kpart_tejada19-24h-290g_n290_T24` | 1 | 290 | 24 | 1 160 100 | optimal | planted partition | — | time limit, excess 12.06 % | 161.88 |
| `kpart_matpower-case1888rte_n296_T36` | 1 | 296 | 36 | 1 776 222 | optimal | planted partition | — | time limit, excess 126.72 % | 91.85 |
| `kpart_matpower-case2383wp_n323_T36` | 1 | 323 | 36 | 1 938 060 | optimal | planted partition | — | time limit, excess 246.39 % | 123.46 |
| `kpart_matpower-case1951rte_n390_T36` | 1 | 390 | 36 | 2 340 324 | optimal | planted partition | — | time limit, excess 96958.22 % | 83.87 |
| `kpart_matpower-case2746wop_n443_T36` | 1 | 443 | 36 | 2 658 006 | optimal | planted partition | — | time limit, excess 97041.43 % | 84.67 |
| `kpart_matpower-case2746wp_n457_T36` | 1 | 457 | 36 | 2 741 922 | optimal | planted partition | — | time limit, excess 96938.55 % | 119.17 |
| `kpart_tejada19-24h-480g_n480_T24` | 1 | 480 | 24 | 1 920 000 | optimal | planted partition | — | time limit, excess 4.79 % | 60.01 |
| `kpart_matpower-case3120sp_n483_T36` | 1 | 483 | 36 | 2 897 766 | optimal | planted partition | — | time limit, excess 26.13 % | 93.35 |
| `kpart_matpower-case3012wp_n496_T36` | 1 | 496 | 36 | 2 975 688 | optimal | planted partition | — | time limit, excess 77.42 % | 87.23 |
| `kpart_tejada19-24h-505g_n505_T24` | 1 | 505 | 24 | 2 019 900 | optimal | planted partition | — | time limit, excess 95664.57 % | 85.51 |
| `kpart_matpower-case2869pegase_n510_T36` | 1 | 510 | 36 | 3 060 270 | optimal | planted partition | — | time limit, excess 46.52 % | 89.44 |
| `kpart_matpower-case2848rte_n544_T36` | 1 | 544 | 36 | 3 264 066 | optimal | planted partition | — | time limit, excess 10.44 % | 983.44 |
| `kpart_matpower-case3375wp_n590_T36` | 1 | 590 | 36 | 3 539 790 | optimal | planted partition | — | time limit, excess 21.62 % | 1028.64 |
| `kpart_matpower-case2868rte_n596_T36` | 1 | 596 | 36 | 3 575 754 | optimal | planted partition | — | time limit, excess 11.06 % | 1066.41 |
| `kpart_pglib-ca_n610_T48` | 1 | 610 | 48 | 4 880 400 | optimal | planted partition | — | time limit, excess 97750.67 % | 892.03 |
| `kpart_pglib-ca-Scenario400_n611_T48` | 1 | 611 | 48 | 4 887 456 | optimal | planted partition | — | time limit, excess 97774.31 % | 896.52 |
| `kpart_tejada19-24h-623g_n623_T24` | 1 | 623 | 24 | 2 492 100 | optimal | planted partition | — | time limit, excess 1.12 % | 988.95 |
| `kpart_tejada19-24h-647g_n647_T24` | 1 | 647 | 24 | 2 588 100 | optimal | planted partition | — | time limit, excess 0.42 % | 994.35 |
| `kpart_tejada19-24h-836g_n836_T24` | 1 | 836 | 24 | 3 344 100 | optimal | planted partition | — | time limit, excess 3.50 % | 981.22 |
| `kpart_tejada19-24h-850g_n850_T24` | 1 | 850 | 24 | 3 399 900 | optimal | planted partition | — | time limit, excess 4.64 % | 84.67 |
| `kpart_tejada19-24h-918g_n918_T24` | 1 | 918 | 24 | 3 672 000 | optimal | planted partition | — | time limit, excess 95655.42 % | 916.89 |
| `kpart_tejada19-24h-931g_n931_T24` | 1 | 931 | 24 | 3 723 900 | optimal | planted partition | — | time limit, excess 0.64 % | 945.88 |
| `kpart_pglib-ferc-935g_n935_T48` | 1 | 935 | 48 | 7 480 536 | optimal | planted partition | — | time limit, excess 97839.91 % | 949.83 |
| `kpart_tejada19-24h-940g_n940_T24` | 1 | 940 | 24 | 3 759 900 | optimal | planted partition | — | time limit, excess 0.93 % | 941.08 |
| `kpart_tejada19-24h-957g_n957_T24` | 1 | 957 | 24 | 3 828 000 | optimal | planted partition | — | time limit, excess 95816.31 % | 827.60 |
| `kpart_tejada19-24h-959g_n959_T24` | 1 | 959 | 24 | 3 836 100 | optimal | planted partition | — | time limit, excess 3.15 % | 931.98 |
| `kpart_pglib-ferc-979g_n979_T48` | 1 | 979 | 48 | 7 832 160 | optimal | planted partition | — | time limit, excess 97833.66 % | 959.23 |
| `kpart_tejada19-24h-1069g_n1069_T24` | 1 | 1069 | 24 | 4 275 900 | optimal | planted partition | — | time limit, excess 2.06 % | 930.92 |
| `kpart_tejada19-24h-1130g_n1130_T24` | 1 | 1130 | 24 | 4 520 100 | optimal | planted partition | — | time limit, excess 3.18 % | 942.30 |
| `kpart_matpower-case6468rte_n1262_T36` | 1 | 1262 | 36 | 7 571 754 | optimal | planted partition | — | time limit, excess 97193.11 % | 60.68 |
| `kpart_matpower-case6470rte_n1306_T36` | 1 | 1306 | 36 | 7 836 156 | optimal | planted partition | — | time limit, excess 97129.08 % | 233.72 |
| `kpart_matpower-case6495rte_n1352_T36` | 1 | 1352 | 36 | 8 111 880 | optimal | planted partition | — | time limit, excess 97148.62 % | 926.90 |
| `kpart_matpower-case6515rte_n1368_T36` | 1 | 1368 | 36 | 8 207 784 | optimal | planted partition | — | time limit, excess 97160.52 % | 979.40 |
| `kpart_tejada19-24h-1376g_n1376_T24` | 1 | 1376 | 24 | 5 504 100 | optimal | planted partition | — | time limit, excess 95804.66 % | 900.74 |
| `kpart_tejada19-24h-1393g_n1393_T24` | 1 | 1393 | 24 | 5 571 900 | optimal | planted partition | — | time limit, excess 95808.92 % | 1016.96 |
| `kpart_matpower-case9241pegase_n1445_T36` | 1 | 1445 | 36 | 8 669 988 | optimal | planted partition | — | time limit, excess 97184.33 % | 61.66 |
| `kpart_tejada19-24h-1577g_n1577_T24` | 1 | 1577 | 24 | 6 308 100 | optimal | planted partition | — | time limit, excess 95867.59 % | 579.81 |
| `kpart_tejada19-24h-1615g_n1615_T24` | 1 | 1615 | 24 | 6 459 900 | optimal | planted partition | — | time limit, excess 95803.12 % | 85.37 |
| `kpart_tejada19-24h-1632g_n1632_T24` | 1 | 1632 | 24 | 6 528 000 | optimal | planted partition | — | time limit, excess 95813.76 % | 989.73 |
| `kpart_tejada19-24h-1768g_n1768_T24` | 1 | 1768 | 24 | 7 071 900 | optimal | planted partition | — | time limit, excess 95815.37 % | 87.07 |
| `kpart_tejada19-24h-1804g_n1804_T24` | 1 | 1804 | 24 | 7 215 900 | optimal | planted partition | — | time limit, excess 95778.39 % | 593.80 |
| `kpart_tejada19-24h-1820g_n1820_T24` | 1 | 1820 | 24 | 7 280 100 | optimal | planted partition | — | time limit, excess 95776.40 % | 81.37 |
| `kpart_tejada19-24h-1823g_n1823_T24` | 1 | 1823 | 24 | 7 292 100 | optimal | planted partition | — | time limit, excess 95854.19 % | 220.86 |
| `kpart_tejada19-24h-1888g_n1888_T24` | 1 | 1888 | 24 | 7 551 900 | optimal | planted partition | — | time limit, excess 95801.28 % | 60.59 |
| `kpart_matpower-case13659pegase_n4092_T36` | 1 | 4092 | 36 | 24 552 090 | optimal | planted partition | — | time limit, excess 97143.39 % | 63.61 |

## kpart-hp (87 instances)

| instance | buses | generators | horizon (h) | best known objective | status | certificate | certificate time (s) | UC.jl + Gurobi (60 s) | Gurobi time (s) |
|---|---:|---:|---:|---:|---|---|---:|---|---:|
| `kpart-hp_matpower-case14_n5_T36` | 1 | 5 | 36 | 59 143 | optimal | planted partition | — | optimal | 0.05 |
| `kpart-hp_matpower-case30_n6_T36` | 1 | 6 | 36 | 71 000 | optimal | planted partition | — | optimal | 0.03 |
| `kpart-hp_matpower-case57_n7_T36` | 1 | 7 | 36 | 82 857 | optimal | planted partition | — | optimal | 0.03 |
| `kpart-hp_orlib-10g_n10_T24` | 1 | 10 | 24 | 64 438 | optimal | planted partition | — | optimal | 0.07 |
| `kpart-hp_matpower-case89pegase_n12_T36` | 1 | 12 | 36 | 105 000 | optimal | planted partition | — | time limit, excess 330.38 % | 123.37 |
| `kpart-hp_orlib-20g_n20_T24` | 1 | 20 | 24 | 103 323 | optimal | planted partition | — | optimal | 2.92 |
| `kpart-hp_tejada19-168h-36g_n36_T168` | 1 | 36 | 168 | 1 170 000 | optimal | planted partition | — | time limit, excess 1108.24 % | 70.10 |
| `kpart-hp_tejada19-168h-38g_n38_T168` | 1 | 38 | 168 | 1 235 520 | optimal | planted partition | — | time limit, excess 1092.91 % | 81.67 |
| `kpart-hp_tejada19-168h-40g_n40_T168` | 1 | 40 | 168 | 1 280 448 | optimal | planted partition | — | time limit, excess 1528.23 % | 73.28 |
| `kpart-hp_orlib-50g_n50_T24` | 1 | 50 | 24 | 215 694 | optimal | planted partition | — | time limit, excess 205.99 % | 85.60 |
| `kpart-hp_tejada19-168h-53g_n53_T168` | 1 | 53 | 168 | 1 645 776 | optimal | planted partition | — | time limit, excess 1106.38 % | 130.66 |
| `kpart-hp_matpower-case118_n54_T36` | 1 | 54 | 36 | 351 000 | optimal | planted partition | — | time limit, excess 75.69 % | 159.84 |
| `kpart-hp_tejada19-168h-58g_n58_T168` | 1 | 58 | 168 | 1 783 536 | optimal | planted partition | — | time limit, excess 99333.76 % | 90.07 |
| `kpart-hp_tejada19-168h-59g_n59_T168` | 1 | 59 | 168 | 1 813 320 | optimal | planted partition | — | time limit, excess 99296.15 % | 90.90 |
| `kpart-hp_matpower-case300_n69_T36` | 1 | 69 | 36 | 438 000 | optimal | planted partition | — | time limit, excess 295.61 % | 74.00 |
| `kpart-hp_tejada19-168h-72g_n72_T168` | 1 | 72 | 168 | 2 172 000 | optimal | planted partition | — | time limit, excess 99345.89 % | 98.51 |
| `kpart-hp_orlib-75g_n75_T24` | 1 | 75 | 24 | 300 000 | optimal | planted partition | — | time limit, excess 295.08 % | 159.26 |
| `kpart-hp_tejada19-168h-84g_n84_T168` | 1 | 84 | 168 | 2 505 000 | optimal | planted partition | — | time limit, excess 99335.45 % | 87.86 |
| `kpart-hp_tejada19-168h-86g_n86_T168` | 1 | 86 | 168 | 2 565 120 | optimal | planted partition | — | time limit, excess 99323.15 % | 118.53 |
| `kpart-hp_tejada19-168h-88g_n88_T168` | 1 | 88 | 168 | 2 604 336 | optimal | planted partition | — | time limit, excess 698.90 % | 989.79 |
| `kpart-hp_tejada19-168h-93g_n93_T168` | 1 | 93 | 168 | 2 754 000 | optimal | planted partition | — | time limit, excess 99300.09 % | 119.16 |
| `kpart-hp_orlib-100g_n100_T24` | 1 | 100 | 24 | 399 900 | optimal | planted partition | — | time limit, excess 334.00 % | 84.77 |
| `kpart-hp_tejada19-168h-105g_n105_T168` | 1 | 105 | 168 | 3 090 000 | optimal | planted partition | — | time limit, excess 835.56 % | 998.66 |
| `kpart-hp_tejada19-168h-110g_n110_T168` | 1 | 110 | 168 | 3 231 249 | optimal | planted partition | — | time limit, excess 1045.45 % | 997.94 |
| `kpart-hp_tejada19-168h-125g_n125_T168` | 1 | 125 | 168 | 3 645 408 | optimal | planted partition | — | time limit, excess 99324.03 % | 842.78 |
| `kpart-hp_tejada19-168h-130g_n130_T168` | 1 | 130 | 168 | 3 767 904 | optimal | planted partition | — | time limit, excess 99330.06 % | 993.39 |
| `kpart-hp_tejada19-168h-131g_n131_T168` | 1 | 131 | 168 | 3 797 808 | optimal | planted partition | — | time limit, excess 707.07 % | 564.13 |
| `kpart-hp_tejada19-168h-140g_n140_T168` | 1 | 140 | 168 | 4 064 112 | optimal | planted partition | — | time limit, excess 511.54 % | 963.15 |
| `kpart-hp_orlib-150g_n150_T24` | 1 | 150 | 24 | 600 000 | optimal | planted partition | — | time limit, excess 200.06 % | 60.02 |
| `kpart-hp_pglib-rts_gmlc_n154_T48` | 1 | 154 | 48 | 1 232 448 | optimal | planted partition | — | time limit, excess 437.73 % | 113.88 |
| `kpart-hp_tejada19-168h-165g_n165_T168` | 1 | 165 | 168 | 4 758 000 | optimal | planted partition | — | time limit, excess 99276.81 % | 732.63 |
| `kpart-hp_tejada19-168h-175g_n175_T168` | 1 | 175 | 168 | 5 040 060 | optimal | planted partition | — | time limit, excess 99271.82 % | 396.79 |
| `kpart-hp_tejada19-168h-179g_n179_T168` | 1 | 179 | 168 | 5 150 034 | optimal | planted partition | — | time limit, excess 99291.57 % | 411.61 |
| `kpart-hp_tejada19-168h-188g_n188_T168` | 1 | 188 | 168 | 5 403 795 | optimal | planted partition | — | time limit, excess 99289.16 % | 414.18 |
| `kpart-hp_tejada19-168h-192g_n192_T168` | 1 | 192 | 168 | 5 502 000 | optimal | planted partition | — | time limit, excess 99290.75 % | 730.60 |
| `kpart-hp_tejada19-168h-199g_n199_T168` | 1 | 199 | 168 | 5 707 395 | optimal | planted partition | — | time limit, excess 99277.37 % | 1016.20 |
| `kpart-hp_orlib-200g_n200_T24` | 1 | 200 | 24 | 800 100 | optimal | planted partition | — | time limit, excess 140.80 % | 143.15 |
| `kpart-hp_tejada19-24h-214g_n214_T24` | 1 | 214 | 24 | 855 900 | optimal | planted partition | — | time limit, excess 30.90 % | 76.24 |
| `kpart-hp_tejada19-24h-250g_n250_T24` | 1 | 250 | 24 | 999 900 | optimal | planted partition | — | time limit, excess 81.87 % | 76.34 |
| `kpart-hp_matpower-case1354pegase_n260_T36` | 1 | 260 | 36 | 1 559 772 | optimal | planted partition | — | time limit, excess 182.72 % | 132.79 |
| `kpart-hp_matpower-case2737sop_n267_T36` | 1 | 267 | 36 | 1 601 730 | optimal | planted partition | — | time limit, excess 173.68 % | 114.27 |
| `kpart-hp_matpower-case2736sp_n289_T36` | 1 | 289 | 36 | 1 734 264 | optimal | planted partition | — | time limit, excess 170.24 % | 116.00 |
| `kpart-hp_tejada19-24h-290g_n290_T24` | 1 | 290 | 24 | 1 160 100 | optimal | planted partition | — | time limit, excess 75.73 % | 113.96 |
| `kpart-hp_matpower-case1888rte_n296_T36` | 1 | 296 | 36 | 1 776 222 | optimal | planted partition | — | time limit, excess 144.69 % | 163.13 |
| `kpart-hp_matpower-case2383wp_n323_T36` | 1 | 323 | 36 | 1 938 060 | optimal | planted partition | — | time limit, excess 120.21 % | 154.50 |
| `kpart-hp_matpower-case1951rte_n390_T36` | 1 | 390 | 36 | 2 340 324 | optimal | planted partition | — | time limit, excess 97022.04 % | 107.75 |
| `kpart-hp_matpower-case2746wop_n443_T36` | 1 | 443 | 36 | 2 658 006 | optimal | planted partition | — | time limit, excess 121.17 % | 118.16 |
| `kpart-hp_matpower-case2746wp_n457_T36` | 1 | 457 | 36 | 2 741 922 | optimal | planted partition | — | time limit, excess 104.26 % | 117.10 |
| `kpart-hp_tejada19-24h-480g_n480_T24` | 1 | 480 | 24 | 1 920 000 | optimal | planted partition | — | time limit, excess 46.43 % | 76.06 |
| `kpart-hp_matpower-case3120sp_n483_T36` | 1 | 483 | 36 | 2 897 766 | optimal | planted partition | — | time limit, excess 29.82 % | 994.76 |
| `kpart-hp_matpower-case3012wp_n496_T36` | 1 | 496 | 36 | 2 975 688 | optimal | planted partition | — | time limit, excess 158.29 % | 996.80 |
| `kpart-hp_tejada19-24h-505g_n505_T24` | 1 | 505 | 24 | 2 019 900 | optimal | planted partition | — | time limit, excess 16.34 % | 998.66 |
| `kpart-hp_matpower-case2869pegase_n510_T36` | 1 | 510 | 36 | 3 060 270 | optimal | planted partition | — | time limit, excess 48.33 % | 1000.11 |
| `kpart-hp_matpower-case2848rte_n544_T36` | 1 | 544 | 36 | 3 264 066 | optimal | planted partition | — | time limit, excess 96998.85 % | 957.47 |
| `kpart-hp_matpower-case3375wp_n590_T36` | 1 | 590 | 36 | 3 539 790 | optimal | planted partition | — | time limit, excess 74.27 % | 1022.21 |
| `kpart-hp_matpower-case2868rte_n596_T36` | 1 | 596 | 36 | 3 575 754 | optimal | planted partition | — | time limit, excess 38.12 % | 564.35 |
| `kpart-hp_pglib-ca_n610_T48` | 1 | 610 | 48 | 4 880 400 | optimal | planted partition | — | time limit, excess 97755.98 % | 894.23 |
| `kpart-hp_pglib-ca-Scenario400_n611_T48` | 1 | 611 | 48 | 4 887 456 | optimal | planted partition | — | time limit, excess 97789.92 % | 397.67 |
| `kpart-hp_tejada19-24h-623g_n623_T24` | 1 | 623 | 24 | 2 492 100 | optimal | planted partition | — | time limit, excess 14.99 % | 998.55 |
| `kpart-hp_tejada19-24h-647g_n647_T24` | 1 | 647 | 24 | 2 588 100 | optimal | planted partition | — | time limit, excess 87.64 % | 958.29 |
| `kpart-hp_tejada19-24h-836g_n836_T24` | 1 | 836 | 24 | 3 344 100 | optimal | planted partition | — | time limit, excess 95697.17 % | 957.05 |
| `kpart-hp_tejada19-24h-850g_n850_T24` | 1 | 850 | 24 | 3 399 900 | optimal | planted partition | — | time limit, excess 95688.06 % | 957.25 |
| `kpart-hp_tejada19-24h-918g_n918_T24` | 1 | 918 | 24 | 3 672 000 | optimal | planted partition | — | time limit, excess 4.67 % | 850.85 |
| `kpart-hp_tejada19-24h-931g_n931_T24` | 1 | 931 | 24 | 3 723 900 | optimal | planted partition | — | time limit, excess 3.29 % | 60.03 |
| `kpart-hp_pglib-ferc-935g_n935_T48` | 1 | 935 | 48 | 7 480 536 | optimal | planted partition | — | time limit, excess 97801.07 % | 943.92 |
| `kpart-hp_tejada19-24h-940g_n940_T24` | 1 | 940 | 24 | 3 759 900 | optimal | planted partition | — | time limit, excess 24.90 % | 734.77 |
| `kpart-hp_tejada19-24h-957g_n957_T24` | 1 | 957 | 24 | 3 828 000 | optimal | planted partition | — | time limit, excess 8.35 % | 735.23 |
| `kpart-hp_tejada19-24h-959g_n959_T24` | 1 | 959 | 24 | 3 836 100 | optimal | planted partition | — | time limit, excess 6.34 % | 935.90 |
| `kpart-hp_pglib-ferc-979g_n979_T48` | 1 | 979 | 48 | 7 832 160 | optimal | planted partition | — | time limit, excess 97799.09 % | 898.11 |
| `kpart-hp_tejada19-24h-1069g_n1069_T24` | 1 | 1069 | 24 | 4 275 900 | optimal | planted partition | — | time limit, excess 13.63 % | 925.84 |
| `kpart-hp_tejada19-24h-1130g_n1130_T24` | 1 | 1130 | 24 | 4 520 100 | optimal | planted partition | — | time limit, excess 8.44 % | 965.70 |
| `kpart-hp_matpower-case6468rte_n1262_T36` | 1 | 1262 | 36 | 7 571 754 | optimal | planted partition | — | time limit, excess 97129.75 % | 963.01 |
| `kpart-hp_matpower-case6470rte_n1306_T36` | 1 | 1306 | 36 | 7 836 156 | optimal | planted partition | — | time limit, excess 97134.83 % | 962.23 |
| `kpart-hp_matpower-case6495rte_n1352_T36` | 1 | 1352 | 36 | 8 111 880 | optimal | planted partition | — | time limit, excess 97182.97 % | 196.98 |
| `kpart-hp_matpower-case6515rte_n1368_T36` | 1 | 1368 | 36 | 8 207 784 | optimal | planted partition | — | time limit, excess 97162.58 % | 368.49 |
| `kpart-hp_tejada19-24h-1376g_n1376_T24` | 1 | 1376 | 24 | 5 504 100 | optimal | planted partition | — | time limit, excess 95840.22 % | 894.38 |
| `kpart-hp_tejada19-24h-1393g_n1393_T24` | 1 | 1393 | 24 | 5 571 900 | optimal | planted partition | — | time limit, excess 95724.76 % | 904.31 |
| `kpart-hp_matpower-case9241pegase_n1445_T36` | 1 | 1445 | 36 | 8 669 988 | optimal | planted partition | — | time limit, excess 97130.65 % | 60.05 |
| `kpart-hp_tejada19-24h-1577g_n1577_T24` | 1 | 1577 | 24 | 6 308 100 | optimal | planted partition | — | time limit, excess 95845.22 % | 579.27 |
| `kpart-hp_tejada19-24h-1615g_n1615_T24` | 1 | 1615 | 24 | 6 459 900 | optimal | planted partition | — | time limit, excess 95815.54 % | 94.69 |
| `kpart-hp_tejada19-24h-1632g_n1632_T24` | 1 | 1632 | 24 | 6 528 000 | optimal | planted partition | — | time limit, excess 95815.71 % | 980.75 |
| `kpart-hp_tejada19-24h-1768g_n1768_T24` | 1 | 1768 | 24 | 7 071 900 | optimal | planted partition | — | time limit, excess 95793.04 % | 84.96 |
| `kpart-hp_tejada19-24h-1804g_n1804_T24` | 1 | 1804 | 24 | 7 215 900 | optimal | planted partition | — | time limit, excess 95809.36 % | 292.18 |
| `kpart-hp_tejada19-24h-1820g_n1820_T24` | 1 | 1820 | 24 | 7 280 100 | optimal | planted partition | — | time limit, excess 95779.59 % | 90.45 |
| `kpart-hp_tejada19-24h-1823g_n1823_T24` | 1 | 1823 | 24 | 7 292 100 | optimal | planted partition | — | time limit, excess 95817.11 % | 246.55 |
| `kpart-hp_tejada19-24h-1888g_n1888_T24` | 1 | 1888 | 24 | 7 551 900 | optimal | planted partition | — | time limit, excess 95756.94 % | 947.64 |
| `kpart-hp_matpower-case13659pegase_n4092_T36` | 1 | 4092 | 36 | 24 552 090 | optimal | planted partition | — | time limit, excess 97146.47 % | 85.92 |

## knap-spanner (87 instances)

| instance | buses | generators | horizon (h) | best known objective | status | certificate | certificate time (s) | UC.jl + Gurobi (60 s) | Gurobi time (s) |
|---|---:|---:|---:|---:|---|---|---:|---|---:|
| `knap-spanner_matpower-case14_n5_T36` | 1 | 5 | 36 | 49 410 | optimal | exact knapsack DP | 0.00 | optimal | 0.01 |
| `knap-spanner_matpower-case30_n6_T36` | 1 | 6 | 36 | 49 172 | optimal | exact knapsack DP | 0.00 | optimal | 0.01 |
| `knap-spanner_matpower-case57_n7_T36` | 1 | 7 | 36 | 12 462 | optimal | exact knapsack DP | 0.00 | optimal | 0.01 |
| `knap-spanner_orlib-10g_n10_T24` | 1 | 10 | 24 | 194 645 | optimal | exact knapsack DP | 0.00 | optimal | 0.01 |
| `knap-spanner_matpower-case89pegase_n12_T36` | 1 | 12 | 36 | 55 543 | optimal | exact knapsack DP | 0.00 | optimal | 0.02 |
| `knap-spanner_orlib-20g_n20_T24` | 1 | 20 | 24 | 114 925 | optimal | exact knapsack DP | 0.00 | optimal | 0.27 |
| `knap-spanner_tejada19-168h-36g_n36_T168` | 1 | 36 | 168 | 730 660 | optimal | exact knapsack DP | 0.00 | optimal | 0.17 |
| `knap-spanner_tejada19-168h-38g_n38_T168` | 1 | 38 | 168 | 1 164 450 | optimal | exact knapsack DP | 0.00 | optimal | 0.33 |
| `knap-spanner_tejada19-168h-40g_n40_T168` | 1 | 40 | 168 | 1 290 114 | optimal | exact knapsack DP | 0.00 | optimal | 0.25 |
| `knap-spanner_orlib-50g_n50_T24` | 1 | 50 | 24 | 292 342 | optimal | exact knapsack DP | 0.01 | optimal | 0.28 |
| `knap-spanner_tejada19-168h-53g_n53_T168` | 1 | 53 | 168 | 4 860 695 | optimal | exact knapsack DP | 0.00 | optimal | 0.18 |
| `knap-spanner_matpower-case118_n54_T36` | 1 | 54 | 36 | 389 506 | optimal | exact knapsack DP | 0.00 | optimal | 0.18 |
| `knap-spanner_tejada19-168h-58g_n58_T168` | 1 | 58 | 168 | 2 260 986 | optimal | exact knapsack DP | 0.00 | optimal | 0.30 |
| `knap-spanner_tejada19-168h-59g_n59_T168` | 1 | 59 | 168 | 2 224 236 | optimal | exact knapsack DP | 0.00 | optimal | 0.24 |
| `knap-spanner_matpower-case300_n69_T36` | 1 | 69 | 36 | 391 446 | optimal | exact knapsack DP | 0.00 | optimal | 0.05 |
| `knap-spanner_tejada19-168h-72g_n72_T168` | 1 | 72 | 168 | 1 646 022 | optimal | exact knapsack DP | 0.01 | optimal | 0.28 |
| `knap-spanner_orlib-75g_n75_T24` | 1 | 75 | 24 | 289 178 | optimal | exact knapsack DP | 0.00 | optimal | 0.05 |
| `knap-spanner_tejada19-168h-84g_n84_T168` | 1 | 84 | 168 | 2 952 264 | optimal | exact knapsack DP | 0.00 | optimal | 0.24 |
| `knap-spanner_tejada19-168h-86g_n86_T168` | 1 | 86 | 168 | 1 992 039 | optimal | exact knapsack DP | 0.00 | optimal | 2.32 |
| `knap-spanner_tejada19-168h-88g_n88_T168` | 1 | 88 | 168 | 2 607 850 | optimal | exact knapsack DP | 0.00 | optimal | 0.38 |
| `knap-spanner_tejada19-168h-93g_n93_T168` | 1 | 93 | 168 | 12 003 173 | optimal | exact knapsack DP | 0.00 | optimal | 1.38 |
| `knap-spanner_orlib-100g_n100_T24` | 1 | 100 | 24 | 525 836 | optimal | exact knapsack DP | 0.02 | optimal | 0.10 |
| `knap-spanner_tejada19-168h-105g_n105_T168` | 1 | 105 | 168 | 3 673 432 | optimal | exact knapsack DP | 0.01 | optimal | 0.41 |
| `knap-spanner_tejada19-168h-110g_n110_T168` | 1 | 110 | 168 | 2 744 028 | optimal | exact knapsack DP | 0.00 | optimal | 0.38 |
| `knap-spanner_tejada19-168h-125g_n125_T168` | 1 | 125 | 168 | 3 970 897 | optimal | exact knapsack DP | 0.00 | optimal | 1.13 |
| `knap-spanner_tejada19-168h-130g_n130_T168` | 1 | 130 | 168 | 2 829 134 | optimal | exact knapsack DP | 0.01 | optimal | 0.45 |
| `knap-spanner_tejada19-168h-131g_n131_T168` | 1 | 131 | 168 | 2 743 356 | optimal | exact knapsack DP | 0.01 | optimal | 0.43 |
| `knap-spanner_tejada19-168h-140g_n140_T168` | 1 | 140 | 168 | 3 465 637 | optimal | exact knapsack DP | 0.00 | optimal | 4.89 |
| `knap-spanner_orlib-150g_n150_T24` | 1 | 150 | 24 | 453 206 | optimal | exact knapsack DP | 0.03 | optimal | 0.21 |
| `knap-spanner_pglib-rts_gmlc_n154_T48` | 1 | 154 | 48 | 1 121 282 | optimal | exact knapsack DP | 0.02 | optimal | 0.16 |
| `knap-spanner_tejada19-168h-165g_n165_T168` | 1 | 165 | 168 | 19 553 877 | optimal | exact knapsack DP | 0.01 | optimal | 0.84 |
| `knap-spanner_tejada19-168h-175g_n175_T168` | 1 | 175 | 168 | 4 786 803 | optimal | exact knapsack DP | 0.01 | optimal | 0.90 |
| `knap-spanner_tejada19-168h-179g_n179_T168` | 1 | 179 | 168 | 22 558 879 | optimal | exact knapsack DP | 0.01 | optimal | 0.79 |
| `knap-spanner_tejada19-168h-188g_n188_T168` | 1 | 188 | 168 | 6 881 714 | optimal | exact knapsack DP | 0.02 | optimal | 6.67 |
| `knap-spanner_tejada19-168h-192g_n192_T168` | 1 | 192 | 168 | 24 410 071 | optimal | exact knapsack DP | 0.01 | optimal | 0.95 |
| `knap-spanner_tejada19-168h-199g_n199_T168` | 1 | 199 | 168 | 7 391 986 | optimal | exact knapsack DP | 0.03 | optimal | 1.90 |
| `knap-spanner_orlib-200g_n200_T24` | 1 | 200 | 24 | 3 578 386 | optimal | exact knapsack DP | 0.04 | optimal | 0.86 |
| `knap-spanner_tejada19-24h-214g_n214_T24` | 1 | 214 | 24 | 626 985 | optimal | exact knapsack DP | 0.06 | optimal | 0.12 |
| `knap-spanner_tejada19-24h-250g_n250_T24` | 1 | 250 | 24 | 1 008 462 | optimal | exact knapsack DP | 0.07 | optimal | 0.34 |
| `knap-spanner_matpower-case1354pegase_n260_T36` | 1 | 260 | 36 | 1 195 249 | optimal | exact knapsack DP | 0.01 | optimal | 0.17 |
| `knap-spanner_matpower-case2737sop_n267_T36` | 1 | 267 | 36 | 2 008 726 | optimal | exact knapsack DP | 0.03 | optimal | 0.20 |
| `knap-spanner_matpower-case2736sp_n289_T36` | 1 | 289 | 36 | 8 017 615 | optimal | exact knapsack DP | 0.04 | optimal | 0.16 |
| `knap-spanner_tejada19-24h-290g_n290_T24` | 1 | 290 | 24 | 861 887 | optimal | exact knapsack DP | 0.07 | optimal | 0.15 |
| `knap-spanner_matpower-case1888rte_n296_T36` | 1 | 296 | 36 | 8 538 366 | optimal | exact knapsack DP | 0.03 | optimal | 0.23 |
| `knap-spanner_matpower-case2383wp_n323_T36` | 1 | 323 | 36 | 2 398 514 | optimal | exact knapsack DP | 0.08 | optimal | 0.29 |
| `knap-spanner_matpower-case1951rte_n390_T36` | 1 | 390 | 36 | 11 418 394 | optimal | exact knapsack DP | 0.06 | optimal | 0.42 |
| `knap-spanner_matpower-case2746wop_n443_T36` | 1 | 443 | 36 | 3 408 696 | optimal | exact knapsack DP | 0.12 | optimal | 0.36 |
| `knap-spanner_matpower-case2746wp_n457_T36` | 1 | 457 | 36 | 1 956 975 | optimal | exact knapsack DP | 0.16 | optimal | 0.50 |
| `knap-spanner_tejada19-24h-480g_n480_T24` | 1 | 480 | 24 | 2 522 250 | optimal | exact knapsack DP | 0.47 | optimal | 0.51 |
| `knap-spanner_matpower-case3120sp_n483_T36` | 1 | 483 | 36 | 2 279 404 | optimal | exact knapsack DP | 0.10 | optimal | 0.39 |
| `knap-spanner_matpower-case3012wp_n496_T36` | 1 | 496 | 36 | 2 121 156 | optimal | exact knapsack DP | 0.29 | optimal | 0.42 |
| `knap-spanner_tejada19-24h-505g_n505_T24` | 1 | 505 | 24 | 1 483 180 | optimal | exact knapsack DP | 0.20 | optimal | 4.10 |
| `knap-spanner_matpower-case2869pegase_n510_T36` | 1 | 510 | 36 | 3 849 618 | optimal | exact knapsack DP | 0.26 | optimal | 0.41 |
| `knap-spanner_matpower-case2848rte_n544_T36` | 1 | 544 | 36 | 2 379 770 | optimal | exact knapsack DP | 0.13 | optimal | 0.39 |
| `knap-spanner_matpower-case3375wp_n590_T36` | 1 | 590 | 36 | 2 513 624 | optimal | exact knapsack DP | 0.41 | optimal | 0.78 |
| `knap-spanner_matpower-case2868rte_n596_T36` | 1 | 596 | 36 | 3 003 306 | optimal | exact knapsack DP | 0.13 | optimal | 0.53 |
| `knap-spanner_pglib-ca_n610_T48` | 1 | 610 | 48 | 6 327 104 | optimal | exact knapsack DP | 0.83 | optimal | 0.72 |
| `knap-spanner_pglib-ca-Scenario400_n611_T48` | 1 | 611 | 48 | 3 609 950 | optimal | exact knapsack DP | 0.47 | optimal | 1.21 |
| `knap-spanner_tejada19-24h-623g_n623_T24` | 1 | 623 | 24 | 2 397 211 | optimal | exact knapsack DP | 0.10 | optimal | 0.60 |
| `knap-spanner_tejada19-24h-647g_n647_T24` | 1 | 647 | 24 | 1 916 612 | optimal | exact knapsack DP | 0.38 | optimal | 1.52 |
| `knap-spanner_tejada19-24h-836g_n836_T24` | 1 | 836 | 24 | 17 225 621 | optimal | exact knapsack DP | 3.52 | optimal | 0.48 |
| `knap-spanner_tejada19-24h-850g_n850_T24` | 1 | 850 | 24 | 2 528 059 | optimal | exact knapsack DP | 6.49 | optimal | 0.45 |
| `knap-spanner_tejada19-24h-918g_n918_T24` | 1 | 918 | 24 | 3 568 244 | optimal | exact knapsack DP | 0.08 | optimal | 0.92 |
| `knap-spanner_tejada19-24h-931g_n931_T24` | 1 | 931 | 24 | 4 944 670 | optimal | exact knapsack DP | 1.63 | optimal | 0.46 |
| `knap-spanner_pglib-ferc-935g_n935_T48` | 1 | 935 | 48 | 7 250 626 | optimal | exact knapsack DP | 0.21 | optimal | 4.58 |
| `knap-spanner_tejada19-24h-940g_n940_T24` | 1 | 940 | 24 | 3 624 311 | optimal | exact knapsack DP | 0.09 | optimal | 0.52 |
| `knap-spanner_tejada19-24h-957g_n957_T24` | 1 | 957 | 24 | 2 833 221 | optimal | exact knapsack DP | 1.25 | optimal | 0.88 |
| `knap-spanner_tejada19-24h-959g_n959_T24` | 1 | 959 | 24 | 5 056 234 | optimal | exact knapsack DP | 1.68 | optimal | 0.61 |
| `knap-spanner_pglib-ferc-979g_n979_T48` | 1 | 979 | 48 | 6 597 310 | optimal | exact knapsack DP | 0.49 | optimal | 3.36 |
| `knap-spanner_tejada19-24h-1069g_n1069_T24` | 1 | 1069 | 24 | 3 820 417 | optimal | exact knapsack DP | 0.37 | optimal | 0.63 |
| `knap-spanner_tejada19-24h-1130g_n1130_T24` | 1 | 1130 | 24 | 5 992 208 | optimal | exact knapsack DP | 2.47 | time limit, excess 222838.65 % | 1062.37 |
| `knap-spanner_matpower-case6468rte_n1262_T36` | 1 | 1262 | 36 | 34 494 283 | optimal | exact knapsack DP | 6.73 | optimal | 6.92 |
| `knap-spanner_matpower-case6470rte_n1306_T36` | 1 | 1306 | 36 | 6 472 101 | optimal | exact knapsack DP | 3.43 | optimal | 3.40 |
| `knap-spanner_matpower-case6495rte_n1352_T36` | 1 | 1352 | 36 | 7 758 146 | optimal | exact knapsack DP | 1.10 | optimal | 1.31 |
| `knap-spanner_matpower-case6515rte_n1368_T36` | 1 | 1368 | 36 | 10 318 428 | optimal | exact knapsack DP | 4.38 | time limit, excess 222760.87 % | 244.22 |
| `knap-spanner_tejada19-24h-1376g_n1376_T24` | 1 | 1376 | 24 | 25 497 167 | optimal | exact knapsack DP | 2.87 | optimal | 1.24 |
| `knap-spanner_tejada19-24h-1393g_n1393_T24` | 1 | 1393 | 24 | 4 073 015 | optimal | exact knapsack DP | 2.69 | optimal | 1.50 |
| `knap-spanner_matpower-case9241pegase_n1445_T36` | 1 | 1445 | 36 | 39 169 331 | optimal | exact knapsack DP | 2.42 | optimal | 3.59 |
| `knap-spanner_tejada19-24h-1577g_n1577_T24` | 1 | 1577 | 24 | 5 505 448 | optimal | exact knapsack DP | 1.81 | optimal | 1.46 |
| `knap-spanner_tejada19-24h-1615g_n1615_T24` | 1 | 1615 | 24 | 4 745 664 | optimal | exact knapsack DP | 6.55 | optimal | 1.24 |
| `knap-spanner_tejada19-24h-1632g_n1632_T24` | 1 | 1632 | 24 | 29 965 689 | optimal | exact knapsack DP | 2.46 | time limit, excess 30088.64 % | 1051.58 |
| `knap-spanner_tejada19-24h-1768g_n1768_T24` | 1 | 1768 | 24 | 6 226 442 | optimal | exact knapsack DP | 2.37 | optimal | 1.51 |
| `knap-spanner_tejada19-24h-1804g_n1804_T24` | 1 | 1804 | 24 | 34 298 587 | optimal | exact knapsack DP | 2.79 | optimal | 1.50 |
| `knap-spanner_tejada19-24h-1820g_n1820_T24` | 1 | 1820 | 24 | 33 505 207 | optimal | exact knapsack DP | 2.66 | optimal | 958.37 |
| `knap-spanner_tejada19-24h-1823g_n1823_T24` | 1 | 1823 | 24 | 7 142 431 | optimal | exact knapsack DP | 0.62 | optimal | 1.50 |
| `knap-spanner_tejada19-24h-1888g_n1888_T24` | 1 | 1888 | 24 | 7 303 529 | optimal | exact knapsack DP | 0.36 | optimal | 1.47 |
| `knap-spanner_matpower-case13659pegase_n4092_T36` | 1 | 4092 | 36 | 30 463 080 | optimal | exact knapsack DP | 41.33 | optimal | 7.55 |

## knap-mstr (87 instances)

| instance | buses | generators | horizon (h) | best known objective | status | certificate | certificate time (s) | UC.jl + Gurobi (60 s) | Gurobi time (s) |
|---|---:|---:|---:|---:|---|---|---:|---|---:|
| `knap-mstr_matpower-case14_n5_T36` | 1 | 5 | 36 | 31 521 | optimal | exact knapsack DP | 0.00 | optimal | 0.01 |
| `knap-mstr_matpower-case30_n6_T36` | 1 | 6 | 36 | 49 685 | optimal | exact knapsack DP | 0.00 | optimal | 0.02 |
| `knap-mstr_matpower-case57_n7_T36` | 1 | 7 | 36 | 219 060 | optimal | exact knapsack DP | 0.00 | optimal | 0.02 |
| `knap-mstr_orlib-10g_n10_T24` | 1 | 10 | 24 | 278 497 | optimal | exact knapsack DP | 0.00 | optimal | 0.02 |
| `knap-mstr_matpower-case89pegase_n12_T36` | 1 | 12 | 36 | 145 695 | optimal | exact knapsack DP | 0.00 | optimal | 123.26 |
| `knap-mstr_orlib-20g_n20_T24` | 1 | 20 | 24 | 1 080 276 | optimal | exact knapsack DP | 0.00 | optimal | 0.29 |
| `knap-mstr_tejada19-168h-36g_n36_T168` | 1 | 36 | 168 | 19 537 714 | optimal | exact knapsack DP | 0.00 | optimal | 0.22 |
| `knap-mstr_tejada19-168h-38g_n38_T168` | 1 | 38 | 168 | 25 440 520 | optimal | exact knapsack DP | 0.00 | optimal | 0.34 |
| `knap-mstr_tejada19-168h-40g_n40_T168` | 1 | 40 | 168 | 198 727 319 | optimal | exact knapsack DP | 0.00 | optimal | 0.27 |
| `knap-mstr_orlib-50g_n50_T24` | 1 | 50 | 24 | 36 776 389 | optimal | exact knapsack DP | 0.01 | optimal | 0.11 |
| `knap-mstr_tejada19-168h-53g_n53_T168` | 1 | 53 | 168 | 50 211 273 | optimal | exact knapsack DP | 0.00 | optimal | 0.32 |
| `knap-mstr_matpower-case118_n54_T36` | 1 | 54 | 36 | 7 791 183 | optimal | exact knapsack DP | 0.00 | optimal | 3.87 |
| `knap-mstr_tejada19-168h-58g_n58_T168` | 1 | 58 | 168 | 24 952 095 | optimal | exact knapsack DP | 0.00 | optimal | 0.44 |
| `knap-mstr_tejada19-168h-59g_n59_T168` | 1 | 59 | 168 | 21 805 427 | optimal | exact knapsack DP | 0.00 | optimal | 0.74 |
| `knap-mstr_matpower-case300_n69_T36` | 1 | 69 | 36 | 4 426 697 | optimal | exact knapsack DP | 0.00 | optimal | 0.25 |
| `knap-mstr_tejada19-168h-72g_n72_T168` | 1 | 72 | 168 | 381 950 107 | optimal | exact knapsack DP | 0.01 | optimal | 3.52 |
| `knap-mstr_orlib-75g_n75_T24` | 1 | 75 | 24 | 56 019 210 | optimal | exact knapsack DP | 0.01 | optimal | 0.20 |
| `knap-mstr_tejada19-168h-84g_n84_T168` | 1 | 84 | 168 | 53 662 147 | optimal | exact knapsack DP | 0.01 | optimal | 0.89 |
| `knap-mstr_tejada19-168h-86g_n86_T168` | 1 | 86 | 168 | 17 263 197 | optimal | exact knapsack DP | 0.00 | optimal | 4.32 |
| `knap-mstr_tejada19-168h-88g_n88_T168` | 1 | 88 | 168 | 455 336 903 | optimal | exact knapsack DP | 0.01 | optimal | 0.37 |
| `knap-mstr_tejada19-168h-93g_n93_T168` | 1 | 93 | 168 | 65 368 009 | optimal | exact knapsack DP | 0.01 | optimal | 52.76 |
| `knap-mstr_orlib-100g_n100_T24` | 1 | 100 | 24 | 43 773 947 | optimal | exact knapsack DP | 0.02 | optimal | 0.33 |
| `knap-mstr_tejada19-168h-105g_n105_T168` | 1 | 105 | 168 | 189 807 583 | optimal | exact knapsack DP | 0.01 | optimal | 0.56 |
| `knap-mstr_tejada19-168h-110g_n110_T168` | 1 | 110 | 168 | 207 766 762 | optimal | exact knapsack DP | 0.01 | optimal | 1.23 |
| `knap-mstr_tejada19-168h-125g_n125_T168` | 1 | 125 | 168 | 601 256 663 | optimal | exact knapsack DP | 0.01 | optimal | 1.59 |
| `knap-mstr_tejada19-168h-130g_n130_T168` | 1 | 130 | 168 | 389 956 847 | optimal | exact knapsack DP | 0.01 | optimal | 1.43 |
| `knap-mstr_tejada19-168h-131g_n131_T168` | 1 | 131 | 168 | 248 165 281 | optimal | exact knapsack DP | 0.01 | optimal | 1.83 |
| `knap-mstr_tejada19-168h-140g_n140_T168` | 1 | 140 | 168 | 302 788 591 | optimal | exact knapsack DP | 0.01 | optimal | 0.97 |
| `knap-mstr_orlib-150g_n150_T24` | 1 | 150 | 24 | 24 855 567 | optimal | exact knapsack DP | 0.03 | optimal | 0.53 |
| `knap-mstr_pglib-rts_gmlc_n154_T48` | 1 | 154 | 48 | 205 791 618 | optimal | exact knapsack DP | 0.03 | optimal | 0.51 |
| `knap-mstr_tejada19-168h-165g_n165_T168` | 1 | 165 | 168 | 763 247 191 | optimal | exact knapsack DP | 0.01 | optimal | 1.65 |
| `knap-mstr_tejada19-168h-175g_n175_T168` | 1 | 175 | 168 | 316 319 514 | optimal | exact knapsack DP | 0.03 | optimal | 1.14 |
| `knap-mstr_tejada19-168h-179g_n179_T168` | 1 | 179 | 168 | 398 041 770 | optimal | exact knapsack DP | 0.02 | optimal | 1.99 |
| `knap-mstr_tejada19-168h-188g_n188_T168` | 1 | 188 | 168 | 332 122 035 | optimal | exact knapsack DP | 0.02 | optimal | 1.46 |
| `knap-mstr_tejada19-168h-192g_n192_T168` | 1 | 192 | 168 | 909 121 500 | optimal | exact knapsack DP | 0.04 | optimal | 1.98 |
| `knap-mstr_tejada19-168h-199g_n199_T168` | 1 | 199 | 168 | 368 051 481 | optimal | exact knapsack DP | 0.02 | optimal | 1.56 |
| `knap-mstr_orlib-200g_n200_T24` | 1 | 200 | 24 | 83 937 498 | optimal | exact knapsack DP | 0.05 | optimal | 0.66 |
| `knap-mstr_tejada19-24h-214g_n214_T24` | 1 | 214 | 24 | 92 988 356 | optimal | exact knapsack DP | 0.08 | optimal | 1.08 |
| `knap-mstr_tejada19-24h-250g_n250_T24` | 1 | 250 | 24 | 108 430 620 | optimal | exact knapsack DP | 0.13 | optimal | 0.52 |
| `knap-mstr_matpower-case1354pegase_n260_T36` | 1 | 260 | 36 | 96 102 303 | optimal | exact knapsack DP | 0.07 | optimal | 15.72 |
| `knap-mstr_matpower-case2737sop_n267_T36` | 1 | 267 | 36 | 121 643 706 | optimal | exact knapsack DP | 0.03 | optimal | 16.25 |
| `knap-mstr_matpower-case2736sp_n289_T36` | 1 | 289 | 36 | 182 899 194 | optimal | exact knapsack DP | 0.04 | optimal | 0.96 |
| `knap-mstr_tejada19-24h-290g_n290_T24` | 1 | 290 | 24 | 47 190 752 | optimal | exact knapsack DP | 0.21 | optimal | 0.77 |
| `knap-mstr_matpower-case1888rte_n296_T36` | 1 | 296 | 36 | 558 230 512 | optimal | exact knapsack DP | 0.05 | optimal | 1.11 |
| `knap-mstr_matpower-case2383wp_n323_T36` | 1 | 323 | 36 | 622 446 902 | optimal | exact knapsack DP | 0.09 | optimal | 0.69 |
| `knap-mstr_matpower-case1951rte_n390_T36` | 1 | 390 | 36 | 187 747 000 | optimal | exact knapsack DP | 0.11 | optimal | 1.18 |
| `knap-mstr_matpower-case2746wop_n443_T36` | 1 | 443 | 36 | 853 668 300 | optimal | exact knapsack DP | 0.20 | optimal | 1.35 |
| `knap-mstr_matpower-case2746wp_n457_T36` | 1 | 457 | 36 | 885 888 800 | optimal | exact knapsack DP | 0.20 | optimal | 29.46 |
| `knap-mstr_tejada19-24h-480g_n480_T24` | 1 | 480 | 24 | 317 351 401 | optimal | exact knapsack DP | 0.43 | optimal | 1.06 |
| `knap-mstr_matpower-case3120sp_n483_T36` | 1 | 483 | 36 | 299 817 958 | optimal | exact knapsack DP | 0.25 | optimal | 12.97 |
| `knap-mstr_matpower-case3012wp_n496_T36` | 1 | 496 | 36 | 957 177 100 | optimal | exact knapsack DP | 0.27 | optimal | 7.71 |
| `knap-mstr_tejada19-24h-505g_n505_T24` | 1 | 505 | 24 | 662 581 100 | optimal | exact knapsack DP | 0.29 | optimal | 1.41 |
| `knap-mstr_matpower-case2869pegase_n510_T36` | 1 | 510 | 36 | 965 547 500 | optimal | exact knapsack DP | 0.36 | optimal | 1.11 |
| `knap-mstr_matpower-case2848rte_n544_T36` | 1 | 544 | 36 | 505 891 800 | optimal | exact knapsack DP | 0.58 | time limit, excess 1204.88 % | 989.94 |
| `knap-mstr_matpower-case3375wp_n590_T36` | 1 | 590 | 36 | 216 497 620 | optimal | exact knapsack DP | 1.89 | optimal | 2.40 |
| `knap-mstr_matpower-case2868rte_n596_T36` | 1 | 596 | 36 | 1 138 790 700 | optimal | exact knapsack DP | 2.58 | optimal | 1.56 |
| `knap-mstr_pglib-ca_n610_T48` | 1 | 610 | 48 | 539 921 686 | optimal | exact knapsack DP | 0.86 | optimal | 1.93 |
| `knap-mstr_pglib-ca-Scenario400_n611_T48` | 1 | 611 | 48 | 786 380 600 | optimal | exact knapsack DP | 0.86 | optimal | 2.11 |
| `knap-mstr_tejada19-24h-623g_n623_T24` | 1 | 623 | 24 | 839 223 700 | optimal | exact knapsack DP | 0.99 | optimal | 1.25 |
| `knap-mstr_tejada19-24h-647g_n647_T24` | 1 | 647 | 24 | 433 807 701 | optimal | exact knapsack DP | 5.47 | optimal | 2.20 |
| `knap-mstr_tejada19-24h-836g_n836_T24` | 1 | 836 | 24 | 1 079 437 400 | optimal | exact knapsack DP | 7.53 | optimal | 2.25 |
| `knap-mstr_tejada19-24h-850g_n850_T24` | 1 | 850 | 24 | 559 393 900 | optimal | exact knapsack DP | 2.42 | time limit, excess 0.00 % | 1028.93 |
| `knap-mstr_tejada19-24h-918g_n918_T24` | 1 | 918 | 24 | 1 190 926 600 | optimal | exact knapsack DP | 2.07 | time limit, excess 0.00 % | 923.18 |
| `knap-mstr_tejada19-24h-931g_n931_T24` | 1 | 931 | 24 | 595 372 900 | optimal | exact knapsack DP | 1.46 | optimal | 2.26 |
| `knap-mstr_pglib-ferc-935g_n935_T48` | 1 | 935 | 48 | 1 204 212 600 | optimal | exact knapsack DP | 2.04 | optimal | 2.96 |
| `knap-mstr_tejada19-24h-940g_n940_T24` | 1 | 940 | 24 | 1 250 084 700 | optimal | exact knapsack DP | 1.57 | optimal | 3.51 |
| `knap-mstr_tejada19-24h-957g_n957_T24` | 1 | 957 | 24 | 1 273 886 300 | optimal | exact knapsack DP | 1.79 | optimal | 2.91 |
| `knap-mstr_tejada19-24h-959g_n959_T24` | 1 | 959 | 24 | 1 264 267 903 | optimal | exact knapsack DP | 2.21 | optimal | 3.25 |
| `knap-mstr_pglib-ferc-979g_n979_T48` | 1 | 979 | 48 | 2 623 516 600 | optimal | exact knapsack DP | 2.87 | optimal | 15.73 |
| `knap-mstr_tejada19-24h-1069g_n1069_T24` | 1 | 1069 | 24 | 1 394 003 100 | optimal | exact knapsack DP | 2.42 | optimal | 4.19 |
| `knap-mstr_tejada19-24h-1130g_n1130_T24` | 1 | 1130 | 24 | 1 480 564 600 | optimal | exact knapsack DP | 4.30 | optimal | 3.53 |
| `knap-mstr_matpower-case6468rte_n1262_T36` | 1 | 1262 | 36 | 2 391 737 200 | optimal | exact knapsack DP | 12.12 | time limit, excess 524.16 % | 160.51 |
| `knap-mstr_matpower-case6470rte_n1306_T36` | 1 | 1306 | 36 | 2 403 472 200 | optimal | exact knapsack DP | 11.08 | time limit, excess 550.50 % | 1051.83 |
| `knap-mstr_matpower-case6495rte_n1352_T36` | 1 | 1352 | 36 | 2 522 841 000 | optimal | exact knapsack DP | 8.67 | optimal | 24.73 |
| `knap-mstr_matpower-case6515rte_n1368_T36` | 1 | 1368 | 36 | 2 602 134 200 | optimal | exact knapsack DP | 4.66 | optimal | 20.25 |
| `knap-mstr_tejada19-24h-1376g_n1376_T24` | 1 | 1376 | 24 | 1 801 664 500 | optimal | exact knapsack DP | 3.69 | optimal | 3.65 |
| `knap-mstr_tejada19-24h-1393g_n1393_T24` | 1 | 1393 | 24 | 1 842 344 400 | optimal | exact knapsack DP | 3.85 | time limit, excess 0.00 % | 290.52 |
| `knap-mstr_matpower-case9241pegase_n1445_T36` | 1 | 1445 | 36 | 2 706 345 500 | optimal | exact knapsack DP | 7.29 | optimal | 6.87 |
| `knap-mstr_tejada19-24h-1577g_n1577_T24` | 1 | 1577 | 24 | 2 097 758 400 | optimal | exact knapsack DP | 7.49 | optimal | 4.43 |
| `knap-mstr_tejada19-24h-1615g_n1615_T24` | 1 | 1615 | 24 | 2 096 523 700 | optimal | exact knapsack DP | 6.94 | optimal | 4.34 |
| `knap-mstr_tejada19-24h-1632g_n1632_T24` | 1 | 1632 | 24 | 1 066 740 400 | optimal | exact knapsack DP | 5.76 | optimal | 23.85 |
| `knap-mstr_tejada19-24h-1768g_n1768_T24` | 1 | 1768 | 24 | 1 152 999 900 | optimal | exact knapsack DP | 6.16 | time limit, excess 1161.45 % | 963.91 |
| `knap-mstr_tejada19-24h-1804g_n1804_T24` | 1 | 1804 | 24 | 2 366 127 500 | optimal | exact knapsack DP | 7.07 | optimal | 5.18 |
| `knap-mstr_tejada19-24h-1820g_n1820_T24` | 1 | 1820 | 24 | 2 365 655 600 | optimal | exact knapsack DP | 7.30 | time limit, excess 550.41 % | 957.96 |
| `knap-mstr_tejada19-24h-1823g_n1823_T24` | 1 | 1823 | 24 | 2 373 870 700 | optimal | exact knapsack DP | 6.40 | time limit, excess 550.41 % | 939.96 |
| `knap-mstr_tejada19-24h-1888g_n1888_T24` | 1 | 1888 | 24 | 2 497 157 800 | optimal | exact knapsack DP | 5.04 | optimal | 5.29 |
| `knap-mstr_matpower-case13659pegase_n4092_T36` | 1 | 4092 | 36 | 7 753 203 000 | optimal | exact knapsack DP | 43.14 | time limit, excess 0.03 % | 993.93 |

## knap-pceil (87 instances)

| instance | buses | generators | horizon (h) | best known objective | status | certificate | certificate time (s) | UC.jl + Gurobi (60 s) | Gurobi time (s) |
|---|---:|---:|---:|---:|---|---|---:|---|---:|
| `knap-pceil_matpower-case14_n5_T36` | 1 | 5 | 36 | 7 695 | optimal | exact knapsack DP | 0.00 | optimal | 0.01 |
| `knap-pceil_matpower-case30_n6_T36` | 1 | 6 | 36 | 2 659 | optimal | exact knapsack DP | 0.00 | optimal | 0.01 |
| `knap-pceil_matpower-case57_n7_T36` | 1 | 7 | 36 | 613 | optimal | exact knapsack DP | 0.00 | optimal | 0.01 |
| `knap-pceil_orlib-10g_n10_T24` | 1 | 10 | 24 | 340 | optimal | exact knapsack DP | 0.00 | optimal | 0.02 |
| `knap-pceil_matpower-case89pegase_n12_T36` | 1 | 12 | 36 | 103 | optimal | exact knapsack DP | 0.00 | optimal | 0.15 |
| `knap-pceil_orlib-20g_n20_T24` | 1 | 20 | 24 | 154 | optimal | exact knapsack DP | 0.00 | optimal | 0.86 |
| `knap-pceil_tejada19-168h-36g_n36_T168` | 1 | 36 | 168 | 476 | optimal | exact knapsack DP | 0.00 | optimal | 7.73 |
| `knap-pceil_tejada19-168h-38g_n38_T168` | 1 | 38 | 168 | 952 | optimal | exact knapsack DP | 0.00 | optimal | 3.96 |
| `knap-pceil_tejada19-168h-40g_n40_T168` | 1 | 40 | 168 | 448 | optimal | exact knapsack DP | 0.00 | optimal | 2.53 |
| `knap-pceil_orlib-50g_n50_T24` | 1 | 50 | 24 | 283 | optimal | exact knapsack DP | 0.01 | optimal | 11.28 |
| `knap-pceil_tejada19-168h-53g_n53_T168` | 1 | 53 | 168 | 1 372 | optimal | exact knapsack DP | 0.00 | optimal | 0.67 |
| `knap-pceil_matpower-case118_n54_T36` | 1 | 54 | 36 | 266 | optimal | exact knapsack DP | 0.00 | optimal | 1.56 |
| `knap-pceil_tejada19-168h-58g_n58_T168` | 1 | 58 | 168 | 1 281 | optimal | exact knapsack DP | 0.00 | optimal | 1.24 |
| `knap-pceil_tejada19-168h-59g_n59_T168` | 1 | 59 | 168 | 1 862 | optimal | exact knapsack DP | 0.01 | optimal | 19.59 |
| `knap-pceil_matpower-case300_n69_T36` | 1 | 69 | 36 | 544 | optimal | exact knapsack DP | 0.00 | optimal | 0.87 |
| `knap-pceil_tejada19-168h-72g_n72_T168` | 1 | 72 | 168 | 1 960 | optimal | exact knapsack DP | 0.00 | optimal | 0.70 |
| `knap-pceil_orlib-75g_n75_T24` | 1 | 75 | 24 | 310 | optimal | exact knapsack DP | 0.01 | optimal | 0.83 |
| `knap-pceil_tejada19-168h-84g_n84_T168` | 1 | 84 | 168 | 1 904 | optimal | exact knapsack DP | 0.00 | optimal | 0.89 |
| `knap-pceil_tejada19-168h-86g_n86_T168` | 1 | 86 | 168 | 3 381 | optimal | exact knapsack DP | 0.01 | optimal | 1.76 |
| `knap-pceil_tejada19-168h-88g_n88_T168` | 1 | 88 | 168 | 2 240 | optimal | exact knapsack DP | 0.01 | optimal | 0.87 |
| `knap-pceil_tejada19-168h-93g_n93_T168` | 1 | 93 | 168 | 2 023 | optimal | exact knapsack DP | 0.01 | optimal | 0.72 |
| `knap-pceil_orlib-100g_n100_T24` | 1 | 100 | 24 | 311 | optimal | exact knapsack DP | 0.01 | optimal | 0.81 |
| `knap-pceil_tejada19-168h-105g_n105_T168` | 1 | 105 | 168 | 3 507 | optimal | exact knapsack DP | 0.01 | optimal | 1.57 |
| `knap-pceil_tejada19-168h-110g_n110_T168` | 1 | 110 | 168 | 4 067 | optimal | exact knapsack DP | 0.01 | optimal | 0.92 |
| `knap-pceil_tejada19-168h-125g_n125_T168` | 1 | 125 | 168 | 3 472 | optimal | exact knapsack DP | 0.01 | optimal | 1.44 |
| `knap-pceil_tejada19-168h-130g_n130_T168` | 1 | 130 | 168 | 3 584 | optimal | exact knapsack DP | 0.01 | optimal | 1.20 |
| `knap-pceil_tejada19-168h-131g_n131_T168` | 1 | 131 | 168 | 2 779 | optimal | exact knapsack DP | 0.01 | optimal | 1.12 |
| `knap-pceil_tejada19-168h-140g_n140_T168` | 1 | 140 | 168 | 4 634 | optimal | exact knapsack DP | 0.01 | optimal | 1.65 |
| `knap-pceil_orlib-150g_n150_T24` | 1 | 150 | 24 | 543 | optimal | exact knapsack DP | 0.03 | optimal | 1.59 |
| `knap-pceil_pglib-rts_gmlc_n154_T48` | 1 | 154 | 48 | 1 318 | optimal | exact knapsack DP | 0.03 | optimal | 1.85 |
| `knap-pceil_tejada19-168h-165g_n165_T168` | 1 | 165 | 168 | 3 710 | optimal | exact knapsack DP | 0.02 | optimal | 2.14 |
| `knap-pceil_tejada19-168h-175g_n175_T168` | 1 | 175 | 168 | 4 494 | optimal | exact knapsack DP | 0.02 | optimal | 1.16 |
| `knap-pceil_tejada19-168h-179g_n179_T168` | 1 | 179 | 168 | 5 537 | optimal | exact knapsack DP | 0.01 | optimal | 4.53 |
| `knap-pceil_tejada19-168h-188g_n188_T168` | 1 | 188 | 168 | 5 411 | optimal | exact knapsack DP | 0.02 | optimal | 1.68 |
| `knap-pceil_tejada19-168h-192g_n192_T168` | 1 | 192 | 168 | 4 263 | optimal | exact knapsack DP | 0.02 | optimal | 4.58 |
| `knap-pceil_tejada19-168h-199g_n199_T168` | 1 | 199 | 168 | 5 684 | optimal | exact knapsack DP | 0.02 | optimal | 1.86 |
| `knap-pceil_orlib-200g_n200_T24` | 1 | 200 | 24 | 856 | optimal | exact knapsack DP | 0.07 | optimal | 2.46 |
| `knap-pceil_tejada19-24h-214g_n214_T24` | 1 | 214 | 24 | 775 | optimal | exact knapsack DP | 0.07 | optimal | 1.51 |
| `knap-pceil_tejada19-24h-250g_n250_T24` | 1 | 250 | 24 | 1 010 | optimal | exact knapsack DP | 0.09 | optimal | 6.06 |
| `knap-pceil_matpower-case1354pegase_n260_T36` | 1 | 260 | 36 | 1 274 | optimal | exact knapsack DP | 0.03 | optimal | 1.50 |
| `knap-pceil_matpower-case2737sop_n267_T36` | 1 | 267 | 36 | 1 322 | optimal | exact knapsack DP | 0.09 | optimal | 3.07 |
| `knap-pceil_matpower-case2736sp_n289_T36` | 1 | 289 | 36 | 1 316 | optimal | exact knapsack DP | 0.05 | optimal | 21.93 |
| `knap-pceil_tejada19-24h-290g_n290_T24` | 1 | 290 | 24 | 973 | optimal | exact knapsack DP | 0.67 | optimal | 9.70 |
| `knap-pceil_matpower-case1888rte_n296_T36` | 1 | 296 | 36 | 1 511 | optimal | exact knapsack DP | 0.12 | optimal | 2.23 |
| `knap-pceil_matpower-case2383wp_n323_T36` | 1 | 323 | 36 | 1 707 | optimal | exact knapsack DP | 0.10 | optimal | 6.17 |
| `knap-pceil_matpower-case1951rte_n390_T36` | 1 | 390 | 36 | 2 144 | optimal | exact knapsack DP | 0.15 | optimal | 1.15 |
| `knap-pceil_matpower-case2746wop_n443_T36` | 1 | 443 | 36 | 2 233 | optimal | exact knapsack DP | 0.23 | optimal | 23.59 |
| `knap-pceil_matpower-case2746wp_n457_T36` | 1 | 457 | 36 | 1 926 | optimal | exact knapsack DP | 0.20 | optimal | 3.65 |
| `knap-pceil_tejada19-24h-480g_n480_T24` | 1 | 480 | 24 | 1 641 | optimal | exact knapsack DP | 0.37 | time limit, excess 0.00 % | 91.08 |
| `knap-pceil_matpower-case3120sp_n483_T36` | 1 | 483 | 36 | 2 190 | optimal | exact knapsack DP | 0.26 | optimal | 3.43 |
| `knap-pceil_matpower-case3012wp_n496_T36` | 1 | 496 | 36 | 2 700 | optimal | exact knapsack DP | 0.26 | optimal | 2.36 |
| `knap-pceil_tejada19-24h-505g_n505_T24` | 1 | 505 | 24 | 1 782 | optimal | exact knapsack DP | 0.28 | optimal | 17.34 |
| `knap-pceil_matpower-case2869pegase_n510_T36` | 1 | 510 | 36 | 2 580 | optimal | exact knapsack DP | 0.34 | optimal | 3.08 |
| `knap-pceil_matpower-case2848rte_n544_T36` | 1 | 544 | 36 | 3 091 | optimal | exact knapsack DP | 0.59 | optimal | 3.38 |
| `knap-pceil_matpower-case3375wp_n590_T36` | 1 | 590 | 36 | 2 785 | optimal | exact knapsack DP | 2.03 | optimal | 3.96 |
| `knap-pceil_matpower-case2868rte_n596_T36` | 1 | 596 | 36 | 2 922 | optimal | exact knapsack DP | 2.25 | optimal | 3.37 |
| `knap-pceil_pglib-ca_n610_T48` | 1 | 610 | 48 | 5 214 | optimal | exact knapsack DP | 0.85 | optimal | 5.17 |
| `knap-pceil_pglib-ca-Scenario400_n611_T48` | 1 | 611 | 48 | 4 456 | optimal | exact knapsack DP | 0.88 | time limit, excess 173048418.85 % | 210.55 |
| `knap-pceil_tejada19-24h-623g_n623_T24` | 1 | 623 | 24 | 2 481 | optimal | exact knapsack DP | 0.89 | optimal | 3.29 |
| `knap-pceil_tejada19-24h-647g_n647_T24` | 1 | 647 | 24 | 2 096 | optimal | exact knapsack DP | 4.45 | time limit, excess 0.00 % | 89.38 |
| `knap-pceil_tejada19-24h-836g_n836_T24` | 1 | 836 | 24 | 3 585 | optimal | exact knapsack DP | 7.71 | optimal | 5.48 |
| `knap-pceil_tejada19-24h-850g_n850_T24` | 1 | 850 | 24 | 3 166 | optimal | exact knapsack DP | 1.75 | optimal | 6.64 |
| `knap-pceil_tejada19-24h-918g_n918_T24` | 1 | 918 | 24 | 3 091 | optimal | exact knapsack DP | 1.74 | optimal | 6.12 |
| `knap-pceil_tejada19-24h-931g_n931_T24` | 1 | 931 | 24 | 3 482 | optimal | exact knapsack DP | 1.54 | optimal | 9.18 |
| `knap-pceil_pglib-ferc-935g_n935_T48` | 1 | 935 | 48 | 8 168 | optimal | exact knapsack DP | 2.18 | optimal | 12.19 |
| `knap-pceil_tejada19-24h-940g_n940_T24` | 1 | 940 | 24 | 4 119 | optimal | exact knapsack DP | 1.62 | optimal | 6.48 |
| `knap-pceil_tejada19-24h-957g_n957_T24` | 1 | 957 | 24 | 3 634 | optimal | exact knapsack DP | 1.75 | optimal | 5.86 |
| `knap-pceil_tejada19-24h-959g_n959_T24` | 1 | 959 | 24 | 3 814 | optimal | exact knapsack DP | 2.46 | optimal | 5.92 |
| `knap-pceil_pglib-ferc-979g_n979_T48` | 1 | 979 | 48 | 7 332 | optimal | exact knapsack DP | 3.40 | optimal | 24.48 |
| `knap-pceil_tejada19-24h-1069g_n1069_T24` | 1 | 1069 | 24 | 3 974 | optimal | exact knapsack DP | 2.36 | time limit, excess 0.00 % | 1039.25 |
| `knap-pceil_tejada19-24h-1130g_n1130_T24` | 1 | 1130 | 24 | 4 438 | optimal | exact knapsack DP | 4.11 | time limit, excess 0.00 % | 358.60 |
| `knap-pceil_matpower-case6468rte_n1262_T36` | 1 | 1262 | 36 | 6 568 | optimal | exact knapsack DP | 11.23 | time limit, excess 0.00 % | 108.88 |
| `knap-pceil_matpower-case6470rte_n1306_T36` | 1 | 1306 | 36 | 6 955 | optimal | exact knapsack DP | 11.02 | time limit, excess 166803704.60 % | 903.44 |
| `knap-pceil_matpower-case6495rte_n1352_T36` | 1 | 1352 | 36 | 7 055 | optimal | exact knapsack DP | 8.34 | time limit, excess 0.00 % | 556.44 |
| `knap-pceil_matpower-case6515rte_n1368_T36` | 1 | 1368 | 36 | 7 236 | optimal | exact knapsack DP | 7.05 | time limit, excess 170204202.57 % | 927.36 |
| `knap-pceil_tejada19-24h-1376g_n1376_T24` | 1 | 1376 | 24 | 5 477 | optimal | exact knapsack DP | 3.64 | time limit, excess 163324603.30 % | 286.15 |
| `knap-pceil_tejada19-24h-1393g_n1393_T24` | 1 | 1393 | 24 | 5 459 | optimal | exact knapsack DP | 4.40 | time limit, excess 159847624.80 % | 398.89 |
| `knap-pceil_matpower-case9241pegase_n1445_T36` | 1 | 1445 | 36 | 8 059 | optimal | exact knapsack DP | 7.07 | optimal | 10.68 |
| `knap-pceil_tejada19-24h-1577g_n1577_T24` | 1 | 1577 | 24 | 6 345 | optimal | exact knapsack DP | 7.75 | time limit, excess 155514772.86 % | 1027.33 |
| `knap-pceil_tejada19-24h-1615g_n1615_T24` | 1 | 1615 | 24 | 6 241 | optimal | exact knapsack DP | 7.51 | time limit, excess 0.00 % | 910.24 |
| `knap-pceil_tejada19-24h-1632g_n1632_T24` | 1 | 1632 | 24 | 6 189 | optimal | exact knapsack DP | 5.61 | time limit, excess 174611824.38 % | 286.36 |
| `knap-pceil_tejada19-24h-1768g_n1768_T24` | 1 | 1768 | 24 | 6 845 | optimal | exact knapsack DP | 6.72 | time limit, excess 0.00 % | 583.21 |
| `knap-pceil_tejada19-24h-1804g_n1804_T24` | 1 | 1804 | 24 | 7 070 | optimal | exact knapsack DP | 6.89 | time limit, excess 0.00 % | 924.82 |
| `knap-pceil_tejada19-24h-1820g_n1820_T24` | 1 | 1820 | 24 | 6 824 | optimal | exact knapsack DP | 7.12 | time limit, excess 175213513.72 % | 905.28 |
| `knap-pceil_tejada19-24h-1823g_n1823_T24` | 1 | 1823 | 24 | 6 809 | optimal | exact knapsack DP | 6.41 | time limit, excess 170241779.63 % | 193.01 |
| `knap-pceil_tejada19-24h-1888g_n1888_T24` | 1 | 1888 | 24 | 7 463 | optimal | exact knapsack DP | 4.86 | time limit, excess 160787671.86 % | 193.52 |
| `knap-pceil_matpower-case13659pegase_n4092_T36` | 1 | 4092 | 36 | 21 881 | optimal | exact knapsack DP | 46.21 | time limit, excess 0.14 % | 61.92 |

## knap-circle (87 instances)

| instance | buses | generators | horizon (h) | best known objective | status | certificate | certificate time (s) | UC.jl + Gurobi (60 s) | Gurobi time (s) |
|---|---:|---:|---:|---:|---|---|---:|---|---:|
| `knap-circle_matpower-case14_n5_T36` | 1 | 5 | 36 | 107 817 | optimal | exact knapsack DP | 0.00 | optimal | 0.01 |
| `knap-circle_matpower-case30_n6_T36` | 1 | 6 | 36 | 139 208 | optimal | exact knapsack DP | 0.00 | optimal | 0.02 |
| `knap-circle_matpower-case57_n7_T36` | 1 | 7 | 36 | 95 808 | optimal | exact knapsack DP | 0.00 | optimal | 0.01 |
| `knap-circle_orlib-10g_n10_T24` | 1 | 10 | 24 | 56 613 | optimal | exact knapsack DP | 0.00 | optimal | 0.01 |
| `knap-circle_matpower-case89pegase_n12_T36` | 1 | 12 | 36 | 122 622 | optimal | exact knapsack DP | 0.00 | optimal | 123.50 |
| `knap-circle_orlib-20g_n20_T24` | 1 | 20 | 24 | 130 173 | optimal | exact knapsack DP | 0.00 | time limit, excess 2104060.84 % | 123.62 |
| `knap-circle_tejada19-168h-36g_n36_T168` | 1 | 36 | 168 | 1 625 218 | optimal | exact knapsack DP | 0.00 | optimal | 0.68 |
| `knap-circle_tejada19-168h-38g_n38_T168` | 1 | 38 | 168 | 1 537 585 | optimal | exact knapsack DP | 0.00 | optimal | 0.59 |
| `knap-circle_tejada19-168h-40g_n40_T168` | 1 | 40 | 168 | 1 646 211 | optimal | exact knapsack DP | 0.00 | optimal | 0.44 |
| `knap-circle_orlib-50g_n50_T24` | 1 | 50 | 24 | 288 043 | optimal | exact knapsack DP | 0.01 | optimal | 0.39 |
| `knap-circle_tejada19-168h-53g_n53_T168` | 1 | 53 | 168 | 2 392 530 | optimal | exact knapsack DP | 0.00 | optimal | 5.13 |
| `knap-circle_matpower-case118_n54_T36` | 1 | 54 | 36 | 484 765 | optimal | exact knapsack DP | 0.00 | optimal | 8.06 |
| `knap-circle_tejada19-168h-58g_n58_T168` | 1 | 58 | 168 | 2 399 866 | optimal | exact knapsack DP | 0.00 | optimal | 0.49 |
| `knap-circle_tejada19-168h-59g_n59_T168` | 1 | 59 | 168 | 2 549 260 | optimal | exact knapsack DP | 0.00 | optimal | 0.53 |
| `knap-circle_matpower-case300_n69_T36` | 1 | 69 | 36 | 616 636 | optimal | exact knapsack DP | 0.00 | optimal | 0.40 |
| `knap-circle_tejada19-168h-72g_n72_T168` | 1 | 72 | 168 | 3 344 460 | optimal | exact knapsack DP | 0.00 | optimal | 1.00 |
| `knap-circle_orlib-75g_n75_T24` | 1 | 75 | 24 | 490 125 | optimal | exact knapsack DP | 0.01 | optimal | 0.36 |
| `knap-circle_tejada19-168h-84g_n84_T168` | 1 | 84 | 168 | 3 674 748 | optimal | exact knapsack DP | 0.01 | optimal | 1.06 |
| `knap-circle_tejada19-168h-86g_n86_T168` | 1 | 86 | 168 | 3 750 383 | optimal | exact knapsack DP | 0.00 | optimal | 0.67 |
| `knap-circle_tejada19-168h-88g_n88_T168` | 1 | 88 | 168 | 4 120 179 | optimal | exact knapsack DP | 0.01 | optimal | 19.07 |
| `knap-circle_tejada19-168h-93g_n93_T168` | 1 | 93 | 168 | 3 818 402 | optimal | exact knapsack DP | 0.01 | optimal | 1.31 |
| `knap-circle_orlib-100g_n100_T24` | 1 | 100 | 24 | 579 088 | optimal | exact knapsack DP | 0.03 | optimal | 0.37 |
| `knap-circle_tejada19-168h-105g_n105_T168` | 1 | 105 | 168 | 4 378 073 | optimal | exact knapsack DP | 0.01 | optimal | 0.86 |
| `knap-circle_tejada19-168h-110g_n110_T168` | 1 | 110 | 168 | 4 297 811 | optimal | exact knapsack DP | 0.01 | optimal | 1.10 |
| `knap-circle_tejada19-168h-125g_n125_T168` | 1 | 125 | 168 | 4 749 038 | optimal | exact knapsack DP | 0.01 | optimal | 1.59 |
| `knap-circle_tejada19-168h-130g_n130_T168` | 1 | 130 | 168 | 5 392 317 | optimal | exact knapsack DP | 0.01 | optimal | 1.55 |
| `knap-circle_tejada19-168h-131g_n131_T168` | 1 | 131 | 168 | 5 945 527 | optimal | exact knapsack DP | 0.01 | optimal | 2.41 |
| `knap-circle_tejada19-168h-140g_n140_T168` | 1 | 140 | 168 | 6 168 393 | optimal | exact knapsack DP | 0.01 | optimal | 1.91 |
| `knap-circle_orlib-150g_n150_T24` | 1 | 150 | 24 | 904 395 | optimal | exact knapsack DP | 0.03 | optimal | 12.05 |
| `knap-circle_pglib-rts_gmlc_n154_T48` | 1 | 154 | 48 | 1 918 054 | optimal | exact knapsack DP | 0.03 | optimal | 2.14 |
| `knap-circle_tejada19-168h-165g_n165_T168` | 1 | 165 | 168 | 7 337 309 | optimal | exact knapsack DP | 0.01 | optimal | 1.76 |
| `knap-circle_tejada19-168h-175g_n175_T168` | 1 | 175 | 168 | 7 661 241 | optimal | exact knapsack DP | 0.02 | time limit, excess 2251795.70 % | 1064.90 |
| `knap-circle_tejada19-168h-179g_n179_T168` | 1 | 179 | 168 | 7 540 134 | optimal | exact knapsack DP | 0.02 | optimal | 2.01 |
| `knap-circle_tejada19-168h-188g_n188_T168` | 1 | 188 | 168 | 8 021 888 | optimal | exact knapsack DP | 0.02 | optimal | 2.74 |
| `knap-circle_tejada19-168h-192g_n192_T168` | 1 | 192 | 168 | 7 960 477 | optimal | exact knapsack DP | 0.04 | optimal | 1.96 |
| `knap-circle_tejada19-168h-199g_n199_T168` | 1 | 199 | 168 | 8 597 428 | optimal | exact knapsack DP | 0.02 | optimal | 2.02 |
| `knap-circle_orlib-200g_n200_T24` | 1 | 200 | 24 | 1 258 393 | optimal | exact knapsack DP | 0.06 | optimal | 1.26 |
| `knap-circle_tejada19-24h-214g_n214_T24` | 1 | 214 | 24 | 1 359 405 | optimal | exact knapsack DP | 0.32 | optimal | 0.50 |
| `knap-circle_tejada19-24h-250g_n250_T24` | 1 | 250 | 24 | 1 565 595 | optimal | exact knapsack DP | 0.14 | optimal | 0.46 |
| `knap-circle_matpower-case1354pegase_n260_T36` | 1 | 260 | 36 | 2 298 564 | optimal | exact knapsack DP | 0.03 | optimal | 5.61 |
| `knap-circle_matpower-case2737sop_n267_T36` | 1 | 267 | 36 | 2 453 729 | optimal | exact knapsack DP | 0.03 | optimal | 19.50 |
| `knap-circle_matpower-case2736sp_n289_T36` | 1 | 289 | 36 | 2 599 493 | optimal | exact knapsack DP | 0.04 | optimal | 22.00 |
| `knap-circle_tejada19-24h-290g_n290_T24` | 1 | 290 | 24 | 1 759 848 | optimal | exact knapsack DP | 0.29 | optimal | 8.07 |
| `knap-circle_matpower-case1888rte_n296_T36` | 1 | 296 | 36 | 2 581 377 | optimal | exact knapsack DP | 0.10 | optimal | 19.87 |
| `knap-circle_matpower-case2383wp_n323_T36` | 1 | 323 | 36 | 2 841 110 | optimal | exact knapsack DP | 0.09 | optimal | 19.83 |
| `knap-circle_matpower-case1951rte_n390_T36` | 1 | 390 | 36 | 3 396 124 | optimal | exact knapsack DP | 0.19 | optimal | 3.21 |
| `knap-circle_matpower-case2746wop_n443_T36` | 1 | 443 | 36 | 3 908 322 | optimal | exact knapsack DP | 0.25 | optimal | 1.35 |
| `knap-circle_matpower-case2746wp_n457_T36` | 1 | 457 | 36 | 4 168 313 | optimal | exact knapsack DP | 0.23 | optimal | 54.46 |
| `knap-circle_tejada19-24h-480g_n480_T24` | 1 | 480 | 24 | 3 012 408 | optimal | exact knapsack DP | 0.24 | optimal | 19.25 |
| `knap-circle_matpower-case3120sp_n483_T36` | 1 | 483 | 36 | 4 353 016 | optimal | exact knapsack DP | 0.27 | optimal | 1.79 |
| `knap-circle_matpower-case3012wp_n496_T36` | 1 | 496 | 36 | 4 340 148 | optimal | exact knapsack DP | 0.27 | optimal | 4.50 |
| `knap-circle_tejada19-24h-505g_n505_T24` | 1 | 505 | 24 | 3 119 277 | optimal | exact knapsack DP | 0.29 | optimal | 19.61 |
| `knap-circle_matpower-case2869pegase_n510_T36` | 1 | 510 | 36 | 4 511 129 | optimal | exact knapsack DP | 0.53 | optimal | 3.62 |
| `knap-circle_matpower-case2848rte_n544_T36` | 1 | 544 | 36 | 4 759 803 | optimal | exact knapsack DP | 0.50 | time limit, excess 2181428.43 % | 1050.11 |
| `knap-circle_matpower-case3375wp_n590_T36` | 1 | 590 | 36 | 5 117 943 | optimal | exact knapsack DP | 1.93 | optimal | 3.30 |
| `knap-circle_matpower-case2868rte_n596_T36` | 1 | 596 | 36 | 5 127 452 | optimal | exact knapsack DP | 2.45 | optimal | 1.22 |
| `knap-circle_pglib-ca_n610_T48` | 1 | 610 | 48 | 7 252 962 | optimal | exact knapsack DP | 0.81 | optimal | 1.72 |
| `knap-circle_pglib-ca-Scenario400_n611_T48` | 1 | 611 | 48 | 7 233 068 | optimal | exact knapsack DP | 0.79 | optimal | 2.05 |
| `knap-circle_tejada19-24h-623g_n623_T24` | 1 | 623 | 24 | 3 711 357 | optimal | exact knapsack DP | 0.90 | optimal | 19.98 |
| `knap-circle_tejada19-24h-647g_n647_T24` | 1 | 647 | 24 | 3 926 499 | optimal | exact knapsack DP | 6.36 | optimal | 19.32 |
| `knap-circle_tejada19-24h-836g_n836_T24` | 1 | 836 | 24 | 5 201 006 | optimal | exact knapsack DP | 7.13 | optimal | 3.30 |
| `knap-circle_tejada19-24h-850g_n850_T24` | 1 | 850 | 24 | 5 145 818 | optimal | exact knapsack DP | 1.83 | optimal | 2.82 |
| `knap-circle_tejada19-24h-918g_n918_T24` | 1 | 918 | 24 | 5 541 691 | optimal | exact knapsack DP | 1.70 | optimal | 3.67 |
| `knap-circle_tejada19-24h-931g_n931_T24` | 1 | 931 | 24 | 5 740 884 | optimal | exact knapsack DP | 1.52 | optimal | 2.26 |
| `knap-circle_pglib-ferc-935g_n935_T48` | 1 | 935 | 48 | 11 466 730 | optimal | exact knapsack DP | 2.10 | time limit, excess 2225005.53 % | 290.64 |
| `knap-circle_tejada19-24h-940g_n940_T24` | 1 | 940 | 24 | 5 746 945 | optimal | exact knapsack DP | 1.60 | optimal | 2.12 |
| `knap-circle_tejada19-24h-957g_n957_T24` | 1 | 957 | 24 | 5 769 320 | optimal | exact knapsack DP | 1.78 | optimal | 2.11 |
| `knap-circle_tejada19-24h-959g_n959_T24` | 1 | 959 | 24 | 5 773 793 | optimal | exact knapsack DP | 2.17 | optimal | 3.18 |
| `knap-circle_pglib-ferc-979g_n979_T48` | 1 | 979 | 48 | 11 774 242 | optimal | exact knapsack DP | 3.13 | time limit, excess 2267782.96 % | 958.78 |
| `knap-circle_tejada19-24h-1069g_n1069_T24` | 1 | 1069 | 24 | 6 529 728 | optimal | exact knapsack DP | 2.28 | time limit, excess 0.00 % | 1063.94 |
| `knap-circle_tejada19-24h-1130g_n1130_T24` | 1 | 1130 | 24 | 6 810 526 | optimal | exact knapsack DP | 4.01 | time limit, excess 0.00 % | 734.39 |
| `knap-circle_matpower-case6468rte_n1262_T36` | 1 | 1262 | 36 | 11 099 110 | optimal | exact knapsack DP | 11.11 | time limit, excess 2183587.91 % | 160.35 |
| `knap-circle_matpower-case6470rte_n1306_T36` | 1 | 1306 | 36 | 11 340 040 | optimal | exact knapsack DP | 10.92 | time limit, excess 0.00 % | 60.06 |
| `knap-circle_matpower-case6495rte_n1352_T36` | 1 | 1352 | 36 | 12 144 329 | optimal | exact knapsack DP | 4.87 | optimal | 19.56 |
| `knap-circle_matpower-case6515rte_n1368_T36` | 1 | 1368 | 36 | 12 101 733 | optimal | exact knapsack DP | 6.84 | time limit, excess 2181420.01 % | 737.28 |
| `knap-circle_tejada19-24h-1376g_n1376_T24` | 1 | 1376 | 24 | 8 344 198 | optimal | exact knapsack DP | 3.53 | time limit, excess 0.00 % | 299.43 |
| `knap-circle_tejada19-24h-1393g_n1393_T24` | 1 | 1393 | 24 | 8 642 318 | optimal | exact knapsack DP | 4.63 | time limit, excess 0.00 % | 918.15 |
| `knap-circle_matpower-case9241pegase_n1445_T36` | 1 | 1445 | 36 | 12 770 849 | optimal | exact knapsack DP | 7.13 | optimal | 4.34 |
| `knap-circle_tejada19-24h-1577g_n1577_T24` | 1 | 1577 | 24 | 9 612 646 | optimal | exact knapsack DP | 7.51 | time limit, excess 0.00 % | 88.47 |
| `knap-circle_tejada19-24h-1615g_n1615_T24` | 1 | 1615 | 24 | 9 794 262 | optimal | exact knapsack DP | 6.89 | time limit, excess 0.00 % | 296.51 |
| `knap-circle_tejada19-24h-1632g_n1632_T24` | 1 | 1632 | 24 | 9 972 244 | optimal | exact knapsack DP | 5.35 | time limit, excess 0.00 % | 100.37 |
| `knap-circle_tejada19-24h-1768g_n1768_T24` | 1 | 1768 | 24 | 10 895 641 | optimal | exact knapsack DP | 6.47 | time limit, excess 2267860.52 % | 962.51 |
| `knap-circle_tejada19-24h-1804g_n1804_T24` | 1 | 1804 | 24 | 10 930 436 | optimal | exact knapsack DP | 6.96 | time limit, excess 0.00 % | 930.23 |
| `knap-circle_tejada19-24h-1820g_n1820_T24` | 1 | 1820 | 24 | 11 177 123 | optimal | exact knapsack DP | 7.02 | time limit, excess 2186584.35 % | 161.29 |
| `knap-circle_tejada19-24h-1823g_n1823_T24` | 1 | 1823 | 24 | 11 117 225 | optimal | exact knapsack DP | 5.90 | optimal | 11.18 |
| `knap-circle_tejada19-24h-1888g_n1888_T24` | 1 | 1888 | 24 | 11 529 222 | optimal | exact knapsack DP | 4.63 | time limit, excess 0.00 % | 908.48 |
| `knap-circle_matpower-case13659pegase_n4092_T36` | 1 | 4092 | 36 | 36 351 007 | optimal | exact knapsack DP | 48.55 | time limit, excess 0.00 % | 61.75 |

## jooken (65 instances)

| instance | buses | generators | horizon (h) | best known objective | status | certificate | certificate time (s) | UC.jl + Gurobi (60 s) | Gurobi time (s) |
|---|---:|---:|---:|---:|---|---|---:|---|---:|
| `jooken_tejada19-168h-105g_n105_T168` | 1 | 105 | 168 | 33 600 005 530 896 | feasible (LB 33 599 999 131 272, gap 1.90e-07) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 34219458.86 % | 107.00 |
| `jooken_tejada19-168h-110g_n110_T168` | 1 | 110 | 168 | 36 960 005 538 624 | feasible (LB 36 959 999 221 488, gap 1.71e-07) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 1022.68 |
| `jooken_tejada19-168h-125g_n125_T168` | 1 | 125 | 168 | 75 600 005 461 512 | feasible (LB 75 599 999 028 624, gap 8.51e-08) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 846.61 |
| `jooken_tejada19-168h-130g_n130_T168` | 1 | 130 | 168 | 80 640 005 567 688 | feasible (LB 80 639 999 003 256, gap 8.14e-08) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 567.77 |
| `jooken_tejada19-168h-131g_n131_T168` | 1 | 131 | 168 | 21 840 005 686 128 | feasible (LB 21 839 999 158 824, gap 2.99e-07) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 928.37 |
| `jooken_tejada19-168h-140g_n140_T168` | 1 | 140 | 168 | 10 080 001 455 552 | feasible (LB 10 079 998 997 376, gap 2.44e-07) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 225.15 |
| `jooken_orlib-150g_n150_T24` | 1 | 150 | 24 | 19 200 000 168 408 | feasible (LB 19 199 999 831 832, gap 1.75e-08) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess -0.00 % | 60.02 |
| `jooken_pglib-rts_gmlc_n154_T48` | 1 | 154 | 48 | 1 440 000 388 704 | feasible (LB 1 439 999 678 160, gap 4.93e-07) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 163.80 |
| `jooken_tejada19-168h-165g_n165_T168` | 1 | 165 | 168 | 8 400 001 228 920 | feasible (LB 8 399 998 796 280, gap 2.90e-07) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 842.51 |
| `jooken_tejada19-168h-175g_n175_T168` | 1 | 175 | 168 | 21 840 000 986 496 | feasible (LB 21 839 998 733 952, gap 1.03e-07) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 2189.67 % | 400.69 |
| `jooken_tejada19-168h-179g_n179_T168` | 1 | 179 | 168 | 26 880 000 926 688 | feasible (LB 26 879 998 783 512, gap 7.97e-08) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 96.55 |
| `jooken_tejada19-168h-188g_n188_T168` | 1 | 188 | 168 | 10 080 000 994 560 | feasible (LB 10 079 998 655 160, gap 2.32e-07) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 96.42 |
| `jooken_tejada19-168h-192g_n192_T168` | 1 | 192 | 168 | 47 040 000 910 224 | feasible (LB 47 039 998 748 904, gap 4.59e-08) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 36278618.79 % | 89.29 |
| `jooken_tejada19-168h-199g_n199_T168` | 1 | 199 | 168 | 300 720 000 547 176 | feasible (LB 300 719 998 493 376, gap 6.83e-09) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 220.78 |
| `jooken_orlib-200g_n200_T24` | 1 | 200 | 24 | 5 280 000 112 728 | feasible (LB 5 279 999 825 592, gap 5.44e-08) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 67.46 |
| `jooken_tejada19-24h-214g_n214_T24` | 1 | 214 | 24 | 1 680 000 108 816 | feasible (LB 1 679 999 781 384, gap 1.95e-07) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 84.80 |
| `jooken_tejada19-24h-250g_n250_T24` | 1 | 250 | 24 | 3 840 000 098 160 | feasible (LB 3 839 999 778 288, gap 8.33e-08) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 115.47 |
| `jooken_matpower-case1354pegase_n260_T36` | 1 | 260 | 36 | 10 080 000 016 596 | feasible (LB 10 079 999 597 520, gap 4.16e-08) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 156.79 |
| `jooken_matpower-case2737sop_n267_T36` | 1 | 267 | 36 | 13 680 000 045 468 | feasible (LB 13 679 999 615 844, gap 3.14e-08) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 114.15 |
| `jooken_matpower-case2736sp_n289_T36` | 1 | 289 | 36 | 19 799 999 955 828 | feasible (LB 19 799 999 564 940, gap 1.97e-08) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 122.45 |
| `jooken_tejada19-24h-290g_n290_T24` | 1 | 290 | 24 | 2 639 999 972 232 | feasible (LB 2 639 999 716 512, gap 9.69e-08) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 114.59 |
| `jooken_matpower-case1888rte_n296_T36` | 1 | 296 | 36 | 4 319 999 896 860 | feasible (LB 4 319 999 529 984, gap 8.49e-08) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 119.18 |
| `jooken_matpower-case2383wp_n323_T36` | 1 | 323 | 36 | 11 159 999 875 944 | feasible (LB 11 159 999 596 512, gap 2.50e-08) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 113.42 |
| `jooken_matpower-case1951rte_n390_T36` | 1 | 390 | 36 | 62 639 999 761 356 | feasible (LB 62 639 999 493 480, gap 4.28e-09) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 113.18 |
| `jooken_matpower-case2746wop_n443_T36` | 1 | 443 | 36 | 9 359 999 680 896 | feasible (LB 9 359 999 457 948, gap 2.38e-08) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 958.19 |
| `jooken_matpower-case2746wp_n457_T36` | 1 | 457 | 36 | 12 959 999 670 420 | feasible (LB 12 959 999 395 092, gap 2.12e-08) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 106.69 |
| `jooken_tejada19-24h-480g_n480_T24` | 1 | 480 | 24 | 5 999 999 751 576 | feasible (LB 5 999 999 588 112, gap 2.72e-08) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 119.22 |
| `jooken_matpower-case3120sp_n483_T36` | 1 | 483 | 36 | 42 119 999 657 280 | feasible (LB 42 119 999 363 412, gap 6.98e-09) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 113.21 |
| `jooken_matpower-case3012wp_n496_T36` | 1 | 496 | 36 | 25 199 999 508 096 | feasible (LB 25 199 999 320 932, gap 7.43e-09) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 958.57 |
| `jooken_tejada19-24h-505g_n505_T24` | 1 | 505 | 24 | 5 999 999 730 792 | feasible (LB 5 999 999 553 336, gap 2.96e-08) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 114.00 |
| `jooken_matpower-case2869pegase_n510_T36` | 1 | 510 | 36 | 30 599 999 579 088 | feasible (LB 30 599 999 383 212, gap 6.40e-09) | Gurobi on knapsack (≤120 s, 1 thread) | 120.01 | time limit, excess 0.00 % | 1076.56 |
| `jooken_matpower-case2848rte_n544_T36` | 1 | 544 | 36 | 6 119 999 439 660 | feasible (LB 6 119 999 297 640, gap 2.32e-08) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 1077.00 |
| `jooken_matpower-case3375wp_n590_T36` | 1 | 590 | 36 | 107 639 999 499 996 | feasible (LB 107 639 999 182 296, gap 2.95e-09) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 933.14 |
| `jooken_matpower-case2868rte_n596_T36` | 1 | 596 | 36 | 22 319 999 490 024 | feasible (LB 22 319 999 276 940, gap 9.55e-09) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 931.14 |
| `jooken_pglib-ca_n610_T48` | 1 | 610 | 48 | 14 879 999 289 744 | feasible (LB 14 879 998 902 624, gap 2.60e-08) | Gurobi on knapsack (≤120 s, 1 thread) | 120.02 | time limit, excess 0.00 % | 733.14 |
| `jooken_pglib-ca-Scenario400_n611_T48` | 1 | 611 | 48 | 23 519 999 303 328 | feasible (LB 23 519 998 989 024, gap 1.34e-08) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 222.67 |
| `jooken_tejada19-24h-623g_n623_T24` | 1 | 623 | 24 | 5 279 999 625 384 | feasible (LB 5 279 999 487 864, gap 2.60e-08) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 118.47 |
| `jooken_tejada19-24h-647g_n647_T24` | 1 | 647 | 24 | 25 919 999 541 408 | feasible (LB 25 919 999 432 976, gap 4.18e-09) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 958.36 |
| `jooken_tejada19-24h-836g_n836_T24` | 1 | 836 | 24 | 4 079 999 318 496 | feasible (LB 4 079 999 253 552, gap 1.59e-08) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 1078.53 |
| `jooken_tejada19-24h-850g_n850_T24` | 1 | 850 | 24 | 7 439 999 430 504 | feasible (LB 7 439 999 366 160, gap 8.65e-09) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 62.66 |
| `jooken_tejada19-24h-918g_n918_T24` | 1 | 918 | 24 | 26 159 999 395 536 | feasible (LB 26 159 999 292 360, gap 3.94e-09) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 1022.41 |
| `jooken_tejada19-24h-931g_n931_T24` | 1 | 931 | 24 | 5 039 999 331 504 | feasible (LB 5 039 999 264 208, gap 1.34e-08) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 926.85 |
| `jooken_pglib-ferc-935g_n935_T48` | 1 | 935 | 48 | 54 239 998 567 440 | feasible (LB 54 239 998 483 536, gap 1.55e-09) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 100.83 |
| `jooken_tejada19-24h-940g_n940_T24` | 1 | 940 | 24 | 9 599 999 266 968 | feasible (LB 9 599 999 237 904, gap 3.03e-09) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 932.74 |
| `jooken_tejada19-24h-957g_n957_T24` | 1 | 957 | 24 | 21 839 999 265 432 | feasible (LB 21 839 999 210 640, gap 2.51e-09) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 741.33 |
| `jooken_tejada19-24h-959g_n959_T24` | 1 | 959 | 24 | 6 959 999 196 720 | feasible (LB 6 959 999 155 992, gap 5.85e-09) | Gurobi on knapsack (≤120 s, 1 thread) | 120.01 | time limit, excess 0.00 % | 223.30 |
| `jooken_pglib-ferc-979g_n979_T48` | 1 | 979 | 48 | 24 479 998 505 760 | feasible (LB 24 479 998 448 688, gap 2.33e-09) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 9804118723.93 % | 367.62 |
| `jooken_tejada19-24h-1069g_n1069_T24` | 1 | 1069 | 24 | 13 199 999 215 032 | feasible (LB 13 199 999 197 752, gap 1.31e-09) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess -0.00 % | 963.38 |
| `jooken_tejada19-24h-1130g_n1130_T24` | 1 | 1130 | 24 | 13 439 999 203 680 | feasible (LB 13 439 999 149 344, gap 4.04e-09) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 733.75 |
| `jooken_matpower-case6468rte_n1262_T36` | 1 | 1262 | 36 | 11 159 998 787 736 | feasible (LB 11 159 998 665 336, gap 1.10e-08) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 16129357439.16 % | 369.08 |
| `jooken_matpower-case6470rte_n1306_T36` | 1 | 1306 | 36 | 50 759 998 454 952 | feasible (LB 50 759 998 451 604, gap 6.60e-11) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 60.47 |
| `jooken_matpower-case6495rte_n1352_T36` | 1 | 1352 | 36 | 24 119 998 539 408 | optimal | Gurobi on knapsack (≤120 s, 1 thread) | 13.94 | optimal | 23.95 |
| `jooken_matpower-case6515rte_n1368_T36` | 1 | 1368 | 36 | 83 519 998 479 000 | feasible (LB 83 519 998 476 156, gap 3.41e-11) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | optimal | 24.88 |
| `jooken_tejada19-24h-1376g_n1376_T24` | 1 | 1376 | 24 | 27 839 999 002 560 | feasible (LB 27 839 998 990 656, gap 4.28e-10) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 88.80 |
| `jooken_tejada19-24h-1393g_n1393_T24` | 1 | 1393 | 24 | 46 079 998 965 144 | feasible (LB 46 079 998 964 400, gap 1.61e-11) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 298.05 |
| `jooken_matpower-case9241pegase_n1445_T36` | 1 | 1445 | 36 | 28 439 998 416 504 | feasible (LB 28 439 998 337 484, gap 2.78e-09) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 6329209205.58 % | 361.74 |
| `jooken_tejada19-24h-1577g_n1577_T24` | 1 | 1577 | 24 | 28 319 998 932 360 | feasible (LB 28 319 998 893 000, gap 1.39e-09) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 92.40 |
| `jooken_tejada19-24h-1615g_n1615_T24` | 1 | 1615 | 24 | 15 359 998 754 040 | feasible (LB 15 359 998 743 072, gap 7.14e-10) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 593.33 |
| `jooken_tejada19-24h-1632g_n1632_T24` | 1 | 1632 | 24 | 35 759 998 662 144 | feasible (LB 35 759 998 658 544, gap 1.01e-10) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 96.46 |
| `jooken_tejada19-24h-1768g_n1768_T24` | 1 | 1768 | 24 | 9 359 998 706 736 | feasible (LB 9 359 998 680 552, gap 2.80e-09) | Gurobi on knapsack (≤120 s, 1 thread) | 120.01 | time limit, excess 12820771671.44 % | 250.46 |
| `jooken_tejada19-24h-1804g_n1804_T24` | 1 | 1804 | 24 | 26 879 998 744 200 | feasible (LB 26 879 998 726 752, gap 6.49e-10) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 921.23 |
| `jooken_tejada19-24h-1820g_n1820_T24` | 1 | 1820 | 24 | 4 079 998 752 864 | feasible (LB 4 079 998 718 928, gap 8.32e-09) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 2029101.12 % | 251.05 |
| `jooken_tejada19-24h-1823g_n1823_T24` | 1 | 1823 | 24 | 16 319 998 812 912 | feasible (LB 16 319 998 572 240, gap 1.47e-08) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 1051.25 |
| `jooken_tejada19-24h-1888g_n1888_T24` | 1 | 1888 | 24 | 18 719 998 637 712 | feasible (LB 18 719 998 571 280, gap 3.55e-09) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 908.26 |
| `jooken_matpower-case13659pegase_n4092_T36` | 1 | 4092 | 36 | 76 319 996 410 548 | feasible (LB 76 319 996 297 328, gap 1.48e-09) | Gurobi on knapsack (≤120 s, 1 thread) | 120.00 | time limit, excess 0.00 % | 169.21 |

## falkenauer (80 instances)

| instance | buses | generators | horizon (h) | best known objective | status | certificate | certificate time (s) | UC.jl + Gurobi (60 s) | Gurobi time (s) |
|---|---:|---:|---:|---:|---|---|---:|---|---:|
| `falkenauer-t60_00_n60_T20` | 1 | 60 | 20 | 190 000 | optimal | benchmark construction | — | time limit, excess 180.87 % | 68.86 |
| `falkenauer-t60_01_n60_T20` | 1 | 60 | 20 | 190 000 | optimal | benchmark construction | — | time limit, excess 177.72 % | 68.41 |
| `falkenauer-t60_02_n60_T20` | 1 | 60 | 20 | 190 000 | optimal | benchmark construction | — | time limit, excess 216.63 % | 68.43 |
| `falkenauer-t60_03_n60_T20` | 1 | 60 | 20 | 190 000 | optimal | benchmark construction | — | time limit, excess 109.36 % | 68.42 |
| `falkenauer-t60_04_n60_T20` | 1 | 60 | 20 | 190 000 | optimal | benchmark construction | — | time limit, excess 185.60 % | 67.69 |
| `falkenauer-t60_05_n60_T20` | 1 | 60 | 20 | 190 000 | optimal | benchmark construction | — | time limit, excess 326.52 % | 68.33 |
| `falkenauer-t60_06_n60_T20` | 1 | 60 | 20 | 190 000 | optimal | benchmark construction | — | time limit, excess 400.65 % | 60.03 |
| `falkenauer-t60_07_n60_T20` | 1 | 60 | 20 | 190 000 | optimal | benchmark construction | — | time limit, excess 500.03 % | 66.62 |
| `falkenauer-t60_08_n60_T20` | 1 | 60 | 20 | 190 000 | optimal | benchmark construction | — | time limit, excess 129.34 % | 192.68 |
| `falkenauer-t60_09_n60_T20` | 1 | 60 | 20 | 190 000 | optimal | benchmark construction | — | time limit, excess 169.83 % | 193.19 |
| `falkenauer-t60_10_n60_T20` | 1 | 60 | 20 | 190 000 | optimal | benchmark construction | — | time limit, excess 188.76 % | 192.69 |
| `falkenauer-t60_11_n60_T20` | 1 | 60 | 20 | 190 000 | optimal | benchmark construction | — | time limit, excess 62.57 % | 193.02 |
| `falkenauer-t60_12_n60_T20` | 1 | 60 | 20 | 190 000 | optimal | benchmark construction | — | time limit, excess 96.75 % | 193.07 |
| `falkenauer-t60_13_n60_T20` | 1 | 60 | 20 | 190 000 | optimal | benchmark construction | — | time limit, excess 72.56 % | 192.76 |
| `falkenauer-t60_14_n60_T20` | 1 | 60 | 20 | 190 000 | optimal | benchmark construction | — | time limit, excess 97.27 % | 176.70 |
| `falkenauer-t60_15_n60_T20` | 1 | 60 | 20 | 190 000 | optimal | benchmark construction | — | time limit, excess 339.66 % | 193.25 |
| `falkenauer-t60_16_n60_T20` | 1 | 60 | 20 | 190 000 | optimal | benchmark construction | — | time limit, excess 225.04 % | 161.68 |
| `falkenauer-t60_17_n60_T20` | 1 | 60 | 20 | 190 000 | optimal | benchmark construction | — | time limit, excess 280.25 % | 160.33 |
| `falkenauer-t60_18_n60_T20` | 1 | 60 | 20 | 190 000 | optimal | benchmark construction | — | time limit, excess 104.11 % | 160.33 |
| `falkenauer-t60_19_n60_T20` | 1 | 60 | 20 | 190 000 | optimal | benchmark construction | — | time limit, excess 156.16 % | 161.17 |
| `falkenauer-t120_00_n120_T40` | 1 | 120 | 40 | 780 000 | optimal | benchmark construction | — | time limit, excess 427.14 % | 60.02 |
| `falkenauer-t120_01_n120_T40` | 1 | 120 | 40 | 780 000 | optimal | benchmark construction | — | time limit, excess 327.88 % | 67.52 |
| `falkenauer-t120_02_n120_T40` | 1 | 120 | 40 | 780 000 | optimal | benchmark construction | — | time limit, excess 721.46 % | 73.98 |
| `falkenauer-t120_03_n120_T40` | 1 | 120 | 40 | 780 000 | optimal | benchmark construction | — | time limit, excess 529.21 % | 83.92 |
| `falkenauer-t120_04_n120_T40` | 1 | 120 | 40 | 780 000 | optimal | benchmark construction | — | time limit, excess 600.55 % | 80.72 |
| `falkenauer-t120_05_n120_T40` | 1 | 120 | 40 | 780 000 | optimal | benchmark construction | — | time limit, excess 503.34 % | 81.95 |
| `falkenauer-t120_06_n120_T40` | 1 | 120 | 40 | 780 000 | optimal | benchmark construction | — | time limit, excess 394.22 % | 60.13 |
| `falkenauer-t120_07_n120_T40` | 1 | 120 | 40 | 780 000 | optimal | benchmark construction | — | time limit, excess 471.71 % | 69.58 |
| `falkenauer-t120_08_n120_T40` | 1 | 120 | 40 | 780 000 | optimal | benchmark construction | — | time limit, excess 435.59 % | 69.53 |
| `falkenauer-t120_09_n120_T40` | 1 | 120 | 40 | 780 000 | optimal | benchmark construction | — | time limit, excess 433.92 % | 84.90 |
| `falkenauer-t120_10_n120_T40` | 1 | 120 | 40 | 780 000 | optimal | benchmark construction | — | time limit, excess 392.30 % | 60.03 |
| `falkenauer-t120_11_n120_T40` | 1 | 120 | 40 | 780 000 | optimal | benchmark construction | — | time limit, excess 551.88 % | 60.34 |
| `falkenauer-t120_12_n120_T40` | 1 | 120 | 40 | 780 000 | optimal | benchmark construction | — | time limit, excess 651.01 % | 60.40 |
| `falkenauer-t120_13_n120_T40` | 1 | 120 | 40 | 780 000 | optimal | benchmark construction | — | time limit, excess 638.59 % | 60.14 |
| `falkenauer-t120_14_n120_T40` | 1 | 120 | 40 | 780 000 | optimal | benchmark construction | — | time limit, excess 112.07 % | 67.63 |
| `falkenauer-t120_15_n120_T40` | 1 | 120 | 40 | 780 000 | optimal | benchmark construction | — | time limit, excess 360.28 % | 143.03 |
| `falkenauer-t120_16_n120_T40` | 1 | 120 | 40 | 780 000 | optimal | benchmark construction | — | time limit, excess 408.44 % | 143.18 |
| `falkenauer-t120_17_n120_T40` | 1 | 120 | 40 | 780 000 | optimal | benchmark construction | — | time limit, excess 170.21 % | 143.24 |
| `falkenauer-t120_18_n120_T40` | 1 | 120 | 40 | 780 000 | optimal | benchmark construction | — | time limit, excess 512.18 % | 69.28 |
| `falkenauer-t120_19_n120_T40` | 1 | 120 | 40 | 780 000 | optimal | benchmark construction | — | time limit, excess 411.77 % | 67.69 |
| `falkenauer-t249_00_n249_T83` | 1 | 249 | 83 | 3 403 000 | optimal | benchmark construction | — | time limit, excess 297.85 % | 128.92 |
| `falkenauer-t249_01_n249_T83` | 1 | 249 | 83 | 3 403 000 | optimal | benchmark construction | — | time limit, excess 264.71 % | 94.74 |
| `falkenauer-t249_02_n249_T83` | 1 | 249 | 83 | 3 403 000 | optimal | benchmark construction | — | time limit, excess 226.19 % | 1026.38 |
| `falkenauer-t249_03_n249_T83` | 1 | 249 | 83 | 3 403 000 | optimal | benchmark construction | — | time limit, excess 307.95 % | 568.58 |
| `falkenauer-t249_04_n249_T83` | 1 | 249 | 83 | 3 403 000 | optimal | benchmark construction | — | time limit, excess 98595.81 % | 548.40 |
| `falkenauer-t249_05_n249_T83` | 1 | 249 | 83 | 3 403 000 | optimal | benchmark construction | — | time limit, excess 286.96 % | 1014.19 |
| `falkenauer-t249_06_n249_T83` | 1 | 249 | 83 | 3 403 000 | optimal | benchmark construction | — | time limit, excess 319.87 % | 997.77 |
| `falkenauer-t249_07_n249_T83` | 1 | 249 | 83 | 3 403 000 | optimal | benchmark construction | — | time limit, excess 269.26 % | 128.80 |
| `falkenauer-t249_08_n249_T83` | 1 | 249 | 83 | 3 403 000 | optimal | benchmark construction | — | time limit, excess 295.85 % | 995.82 |
| `falkenauer-t249_09_n249_T83` | 1 | 249 | 83 | 3 403 000 | optimal | benchmark construction | — | time limit, excess 325.24 % | 997.16 |
| `falkenauer-t249_10_n249_T83` | 1 | 249 | 83 | 3 403 000 | optimal | benchmark construction | — | time limit, excess 302.22 % | 565.37 |
| `falkenauer-t249_11_n249_T83` | 1 | 249 | 83 | 3 403 000 | optimal | benchmark construction | — | time limit, excess 314.38 % | 926.85 |
| `falkenauer-t249_12_n249_T83` | 1 | 249 | 83 | 3 403 000 | optimal | benchmark construction | — | time limit, excess 284.35 % | 935.71 |
| `falkenauer-t249_13_n249_T83` | 1 | 249 | 83 | 3 403 000 | optimal | benchmark construction | — | time limit, excess 209.69 % | 567.11 |
| `falkenauer-t249_14_n249_T83` | 1 | 249 | 83 | 3 403 000 | optimal | benchmark construction | — | time limit, excess 199.83 % | 1075.07 |
| `falkenauer-t249_15_n249_T83` | 1 | 249 | 83 | 3 403 000 | optimal | benchmark construction | — | time limit, excess 305.48 % | 996.37 |
| `falkenauer-t249_16_n249_T83` | 1 | 249 | 83 | 3 403 000 | optimal | benchmark construction | — | time limit, excess 217.50 % | 1073.70 |
| `falkenauer-t249_17_n249_T83` | 1 | 249 | 83 | 3 403 000 | optimal | benchmark construction | — | time limit, excess 203.56 % | 1074.70 |
| `falkenauer-t249_18_n249_T83` | 1 | 249 | 83 | 3 403 000 | optimal | benchmark construction | — | time limit, excess 307.63 % | 925.77 |
| `falkenauer-t249_19_n249_T83` | 1 | 249 | 83 | 3 403 000 | optimal | benchmark construction | — | time limit, excess 317.11 % | 843.01 |
| `falkenauer-t501_00_n501_T167` | 1 | 501 | 167 | 13 861 000 | optimal | benchmark construction | — | time limit, excess 99275.12 % | 61.86 |
| `falkenauer-t501_01_n501_T167` | 1 | 501 | 167 | 13 861 000 | optimal | benchmark construction | — | time limit, excess 99275.63 % | 62.27 |
| `falkenauer-t501_02_n501_T167` | 1 | 501 | 167 | 13 861 000 | optimal | benchmark construction | — | time limit, excess 99275.70 % | 102.70 |
| `falkenauer-t501_03_n501_T167` | 1 | 501 | 167 | 13 861 000 | optimal | benchmark construction | — | time limit, excess 99275.84 % | 103.38 |
| `falkenauer-t501_04_n501_T167` | 1 | 501 | 167 | 13 861 000 | optimal | benchmark construction | — | time limit, excess 99275.74 % | 114.22 |
| `falkenauer-t501_05_n501_T167` | 1 | 501 | 167 | 13 861 000 | optimal | benchmark construction | — | time limit, excess 99275.59 % | 97.12 |
| `falkenauer-t501_06_n501_T167` | 1 | 501 | 167 | 13 861 000 | optimal | benchmark construction | — | time limit, excess 99275.65 % | 105.71 |
| `falkenauer-t501_07_n501_T167` | 1 | 501 | 167 | 13 861 000 | optimal | benchmark construction | — | time limit, excess 99275.64 % | 1059.13 |
| `falkenauer-t501_08_n501_T167` | 1 | 501 | 167 | 13 861 000 | optimal | benchmark construction | — | time limit, excess 99275.73 % | 110.43 |
| `falkenauer-t501_09_n501_T167` | 1 | 501 | 167 | 13 861 000 | optimal | benchmark construction | — | time limit, excess 99275.61 % | 63.86 |
| `falkenauer-t501_10_n501_T167` | 1 | 501 | 167 | 13 861 000 | optimal | benchmark construction | — | time limit, excess 99275.53 % | 153.52 |
| `falkenauer-t501_11_n501_T167` | 1 | 501 | 167 | 13 861 000 | optimal | benchmark construction | — | time limit, excess 99275.63 % | 100.60 |
| `falkenauer-t501_12_n501_T167` | 1 | 501 | 167 | 13 861 000 | optimal | benchmark construction | — | time limit, excess 99275.42 % | 1015.38 |
| `falkenauer-t501_13_n501_T167` | 1 | 501 | 167 | 13 861 000 | optimal | benchmark construction | — | time limit, excess 99275.60 % | 111.74 |
| `falkenauer-t501_14_n501_T167` | 1 | 501 | 167 | 13 861 000 | optimal | benchmark construction | — | time limit, excess 99275.55 % | 103.69 |
| `falkenauer-t501_15_n501_T167` | 1 | 501 | 167 | 13 861 000 | optimal | benchmark construction | — | time limit, excess 99275.63 % | 96.70 |
| `falkenauer-t501_16_n501_T167` | 1 | 501 | 167 | 13 861 000 | optimal | benchmark construction | — | time limit, excess 99275.50 % | 261.17 |
| `falkenauer-t501_17_n501_T167` | 1 | 501 | 167 | 13 861 000 | optimal | benchmark construction | — | time limit, excess 99275.61 % | 428.55 |
| `falkenauer-t501_18_n501_T167` | 1 | 501 | 167 | 13 861 000 | optimal | benchmark construction | — | time limit, excess 99275.63 % | 65.18 |
| `falkenauer-t501_19_n501_T167` | 1 | 501 | 167 | 13 861 000 | optimal | benchmark construction | — | time limit, excess 99275.55 % | 60.93 |

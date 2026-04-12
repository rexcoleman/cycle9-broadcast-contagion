"""Phase 2 sweep runner — all 6 primary + 4 ablation conditions."""

import sys
import os
import time
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from scn_contagion.simulation import run_sweep

coverage_points = np.arange(0.00, 1.02, 0.02)  # 51 points
n_reps = 100

# Primary conditions (C1-C6)
conditions = [
    # (label, topology, n_nodes, strategy, extra_kwargs)
    ('C1', 'ba', 1000, 'uniform', {}),
    ('C2', 'ba', 5000, 'uniform', {}),
    ('C3', 'ba', 10000, 'uniform', {}),
    ('C4', 'config', 5000, 'uniform', {}),
    ('C5', 'ba', 5000, 'hub_targeted', {}),
    ('C6', 'config', 5000, 'hub_targeted', {}),
]

# Ablation conditions (A1-A4)
# A1 = C2 (uniform on BA 5000) — already run as C2, skip duplicate
ablations = [
    ('A2', 'ba', 5000, 'uniform', {'stifling': True}),
    ('A3', 'ba', 5000, 'uniform', {'undirected': True}),
    ('A4', 'ba', 5000, 'uniform', {'cascade_detection': True}),
]

start_total = time.time()

print("=" * 60)
print("PHASE 2: Primary Sweep (C1-C6)")
print("=" * 60)

for label, topo, n, strategy, kwargs in conditions:
    outpath = f'outputs/sweep/{label}_results.csv'
    print(f"\nStarting {label}: {topo} N={n} {strategy} ...")
    run_sweep(
        topology=topo,
        n_nodes=n,
        strategy=strategy,
        coverage_points=coverage_points,
        n_reps=n_reps,
        output_path=outpath,
        condition_label=label,
        **kwargs,
    )

print("\n" + "=" * 60)
print("PHASE 2: Ablation Sweep (A2-A4)")
print("=" * 60)

for label, topo, n, strategy, kwargs in ablations:
    outpath = f'outputs/ablation/{label}_results.csv'
    print(f"\nStarting {label}: {topo} N={n} {strategy} {kwargs} ...")
    run_sweep(
        topology=topo,
        n_nodes=n,
        strategy=strategy,
        coverage_points=coverage_points,
        n_reps=n_reps,
        output_path=outpath,
        condition_label=label,
        **kwargs,
    )

elapsed_total = time.time() - start_total
print(f"\n{'=' * 60}")
print(f"TOTAL: completed in {elapsed_total:.1f}s ({elapsed_total/60:.1f} min)")
print(f"{'=' * 60}")

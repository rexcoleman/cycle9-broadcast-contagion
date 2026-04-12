"""Simulation runner for broadcast contagion sweep experiments."""

import numpy as np
import csv
import os
import time

from .networks import generate_ba_network, generate_config_network
from .propagation import broadcast_propagation
from .detection import (
    make_uniform_detector, make_hub_targeted_detector,
    make_stifling_fn, make_cascade_detection_fn,
)


def _precompute_seed_candidates(G):
    """Precompute hub seed candidates for a network.

    Returns (candidate_nodes, candidate_weights) for top-1% hubs by in-degree.
    Supply chain attacks target popular packages, so seed selection is
    weighted toward high-in-degree nodes (those with many dependents).
    """
    n = G.number_of_nodes()
    in_degrees = np.array([G.in_degree(i) for i in range(n)], dtype=float)
    top_k = max(10, n // 100)
    top_indices = np.argsort(in_degrees)[-top_k:]
    top_weights = in_degrees[top_indices]
    if top_weights.sum() > 0:
        top_weights = top_weights / top_weights.sum()
    else:
        top_weights = np.ones(len(top_indices)) / len(top_indices)
    return top_indices, top_weights


def _select_seed_node(rng, candidates, weights):
    """Select a seed node from precomputed hub candidates."""
    return int(candidates[rng.choice(len(candidates), p=weights)])


def run_single_simulation(G, p_coverage, strategy='uniform', mc_seed=0,
                          stifling=False, cascade_detection=False,
                          delta=0.5, p_cascade=0.5,
                          seed_candidates=None, seed_weights=None):
    """Run a single Monte Carlo simulation.

    Parameters
    ----------
    G : nx.DiGraph
        Network to simulate on.
    p_coverage : float
        Detection coverage fraction [0, 1].
    strategy : str
        'uniform' or 'hub_targeted'.
    mc_seed : int
        Random seed for this Monte Carlo run.
    stifling : bool
        Use contact-dependent stifling instead of time-dependent detection.
    cascade_detection : bool
        Add cascading detection (contact tracing).
    seed_candidates, seed_weights : arrays or None
        Precomputed from _precompute_seed_candidates(). Computed on-the-fly
        if not provided.

    Returns
    -------
    dict with cascade_fraction, contained, time_to_steady
    """
    rng = np.random.default_rng(mc_seed)
    n = G.number_of_nodes()

    # Select seed from top hubs by in-degree
    if seed_candidates is None or seed_weights is None:
        seed_candidates, seed_weights = _precompute_seed_candidates(G)
    seed_node = _select_seed_node(rng, seed_candidates, seed_weights)

    # Set up detection
    stifling_fn = None
    cascade_fn = None

    if stifling:
        # For stifling ablation: p_coverage maps to delta (stifling probability)
        stifling_fn = make_stifling_fn(delta=p_coverage, rng=rng)
        detection_fn = lambda node, degree, time_infected: False
    elif strategy == 'hub_targeted':
        degrees = [G.in_degree(node) + G.out_degree(node) for node in range(n)]
        detection_fn = make_hub_targeted_detector(p_coverage, degrees, rng=rng)
    else:
        detection_fn = make_uniform_detector(p_coverage, rng=rng)

    if cascade_detection:
        cascade_fn = make_cascade_detection_fn(p_cascade=p_cascade, rng=rng)

    result = broadcast_propagation(
        G, seed_node, detection_fn,
        stifling_fn=stifling_fn,
        cascade_detection_fn=cascade_fn,
    )

    return {
        'cascade_fraction': result['cascade_fraction'],
        'contained': result['contained'],
        'time_to_steady': result['time_to_steady'],
    }


def run_sweep(topology, n_nodes, strategy, coverage_points, n_reps,
              output_path, condition_label, m=3, gamma=2.7,
              stifling=False, cascade_detection=False,
              undirected=False, network_seed=42):
    """Run a full coverage sweep for one condition.

    Parameters
    ----------
    topology : str
        'ba' or 'config'.
    n_nodes : int
        Network size.
    strategy : str
        'uniform' or 'hub_targeted'.
    coverage_points : array-like
        Coverage fractions to sweep.
    n_reps : int
        Monte Carlo repetitions per coverage point.
    output_path : str
        Path to output CSV file.
    condition_label : str
        Label for this condition (e.g., 'C1').
    """
    # Generate network once per condition
    if topology == 'ba':
        G = generate_ba_network(n_nodes, m=m, seed=network_seed)
    else:
        G = generate_config_network(n_nodes, gamma=gamma, seed=network_seed)

    if undirected:
        G = G.to_undirected()
        G = G.to_directed()  # Both directions for undirected ablation

    # Precompute seed candidates once for the entire sweep
    seed_candidates, seed_weights = _precompute_seed_candidates(G)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['condition', 'p_coverage', 'run_id',
                         'cascade_fraction', 'contained', 'time_to_steady_state'])

        total_runs = len(coverage_points) * n_reps
        completed = 0
        start_time = time.time()

        for p in coverage_points:
            for rep in range(n_reps):
                mc_seed = int(rep * 10000 + int(p * 1000))
                result = run_single_simulation(
                    G, p, strategy=strategy, mc_seed=mc_seed,
                    stifling=stifling, cascade_detection=cascade_detection,
                    seed_candidates=seed_candidates, seed_weights=seed_weights,
                )
                writer.writerow([
                    condition_label,
                    f'{p:.4f}',
                    rep,
                    f'{result["cascade_fraction"]:.6f}',
                    int(result['contained']),
                    result['time_to_steady'],
                ])
                completed += 1

            # Flush periodically
            if completed % (n_reps * 5) == 0:
                f.flush()
                elapsed = time.time() - start_time
                rate = completed / elapsed if elapsed > 0 else 0
                remaining = (total_runs - completed) / rate if rate > 0 else 0
                print(f"  {condition_label}: {completed}/{total_runs} runs "
                      f"({elapsed:.0f}s elapsed, ~{remaining:.0f}s remaining)")

    elapsed = time.time() - start_time
    print(f"  {condition_label}: completed {total_runs} runs in {elapsed:.1f}s")
    return output_path

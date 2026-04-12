"""Baseline models for comparison.

- Homogeneous SIS: uniform recovery, no detection, continuous reinfection
  Uses UNDIRECTED transmission to match Pastor-Satorras & Vespignani (2001)
- Static percolation: Cohen's analytical p_c from degree moments
"""

import numpy as np
import networkx as nx


def run_sis_simulation(G, infection_rate=0.01, recovery_rate=0.05,
                       max_steps=2000, seed=None):
    """Run homogeneous SIS simulation on a network.

    Uses UNDIRECTED transmission (both directions) to match the P-S&V
    theoretical framework. The vanishing threshold result assumes
    bidirectional transmission on scale-free networks.

    Parameters
    ----------
    G : nx.DiGraph
        Network (will use both edge directions for SIS spread).
    infection_rate : float
        Per-edge infection probability per step (lambda/beta).
    recovery_rate : float
        Per-node recovery probability per step (gamma/mu).
    max_steps : int
        Maximum simulation steps.

    Returns
    -------
    dict with prevalence (fraction infected at steady state),
    trajectory (prevalence over time)
    """
    rng = np.random.default_rng(seed)
    n = G.number_of_nodes()

    # Build UNDIRECTED adjacency for SIS (both directions)
    neighbors = {}
    for node in G.nodes():
        nb = set(G.predecessors(node)) | set(G.successors(node))
        neighbors[node] = list(nb)

    # Start with 10% infected randomly
    state = np.zeros(n, dtype=np.int8)
    initial_infected = rng.choice(n, size=max(1, n // 10), replace=False)
    state[initial_infected] = 1

    trajectory = []
    window = 100

    for t in range(max_steps):
        prevalence = float(state.sum()) / n
        trajectory.append(prevalence)

        new_state = state.copy()

        # Recovery: each infected node recovers with probability recovery_rate
        infected_nodes = np.where(state == 1)[0]
        for node in infected_nodes:
            if rng.random() < recovery_rate:
                new_state[node] = 0

        # Infection: each infected node infects susceptible neighbors (undirected)
        for node in infected_nodes:
            for neighbor in neighbors[node]:
                if state[neighbor] == 0 and rng.random() < infection_rate:
                    new_state[neighbor] = 1

        state = new_state

        # Check steady state (need enough steps to stabilize)
        if t > window * 3:
            recent = trajectory[-window:]
            if np.std(recent) < 0.003 and np.mean(recent) > 0.01:
                break

    # Steady-state prevalence: mean of last window steps
    if len(trajectory) >= window:
        steady_prevalence = np.mean(trajectory[-window:])
    else:
        steady_prevalence = np.mean(trajectory)

    return {
        'prevalence': float(steady_prevalence),
        'trajectory': trajectory,
        'steps': len(trajectory),
    }


def compute_percolation_pc(G):
    """Compute static percolation threshold from degree distribution moments.

    Cohen et al. (2003): for uniform immunization on scale-free networks,
    the critical immunization fraction is:
        f_c = 1 - 1/(kappa - 1)
    where kappa = <k^2>/<k>.

    This is the fraction of nodes that must be IMMUNIZED (removed) to stop
    the epidemic. The corresponding detection COVERAGE fraction (fraction
    of nodes with active detection) is the same value: at coverage = f_c,
    the epidemic is contained.

    For targeted immunization (acquaintance strategy):
        f_c_targeted ~ 1/sqrt(kappa)
    """
    degrees = np.array([G.in_degree(n) + G.out_degree(n) for n in G.nodes()],
                       dtype=float)

    k_mean = degrees.mean()
    k2_mean = (degrees ** 2).mean()

    if k_mean == 0:
        return {'pc_uniform': 1.0, 'pc_targeted': 1.0, 'kappa': 0.0}

    kappa = k2_mean / k_mean

    # Uniform immunization threshold
    if kappa > 1:
        pc_uniform = 1.0 - 1.0 / (kappa - 1.0)
    else:
        pc_uniform = 1.0

    # Targeted immunization threshold (acquaintance strategy)
    if kappa > 0:
        pc_targeted = 1.0 / np.sqrt(kappa)
    else:
        pc_targeted = 1.0

    # Clamp to [0, 1]
    pc_uniform = max(0.0, min(1.0, pc_uniform))
    pc_targeted = max(0.0, min(1.0, pc_targeted))

    return {
        'pc_uniform': float(pc_uniform),
        'pc_targeted': float(pc_targeted),
        'kappa': float(kappa),
        'k_mean': float(k_mean),
        'k2_mean': float(k2_mean),
    }

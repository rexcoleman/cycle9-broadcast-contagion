"""Network generation for supply chain contagion simulations.

Two topology models:
- Barabasi-Albert (BA): preferential attachment, directed
- Configuration model: power-law degree sequence, directed
"""

import numpy as np
import networkx as nx


def generate_ba_network(n, m=3, seed=None):
    """Generate directed Barabasi-Albert network.

    Edges directed from new node to existing (dependency = "depends on").
    Returns a DiGraph where an edge (u, v) means u depends on v.
    """
    G_undirected = nx.barabasi_albert_graph(n, m, seed=seed)
    G = nx.DiGraph()
    G.add_nodes_from(range(n))
    # BA adds nodes sequentially; node i connects to m earlier nodes
    # Orient edges: higher-index node depends on lower-index node
    for u, v in G_undirected.edges():
        if u > v:
            G.add_edge(u, v)  # u depends on v
        else:
            G.add_edge(v, u)  # v depends on u
    return G


def _power_law_degree_sequence(n, gamma=2.7, k_min=3, k_max=None, seed=None):
    """Generate power-law degree sequence P(k) ~ k^(-gamma).

    k_min=3 to match BA mean degree (~6) and produce realistic density.
    """
    rng = np.random.default_rng(seed)
    if k_max is None:
        k_max = int(np.sqrt(n))

    # Discrete power-law: P(k) proportional to k^(-gamma)
    ks = np.arange(k_min, k_max + 1)
    probs = ks.astype(float) ** (-gamma)
    probs /= probs.sum()

    degrees = rng.choice(ks, size=n, p=probs)

    # Ensure even sum for configuration model
    if degrees.sum() % 2 != 0:
        idx = rng.integers(0, n)
        degrees[idx] += 1

    return degrees


def generate_config_network(n, gamma=2.7, k_min=3, k_max=None, seed=None):
    """Generate directed configuration model with power-law degree distribution.

    Edges oriented from lower-degree to higher-degree node
    (dependents point to dependencies -- popular packages are depended upon).
    k_min=3 matches BA's m=3 for comparable network density.
    """
    degrees = _power_law_degree_sequence(n, gamma, k_min, k_max, seed=seed)

    G_undirected = nx.configuration_model(degrees.tolist(), seed=seed)
    # Remove self-loops and parallel edges
    G_undirected = nx.Graph(G_undirected)
    G_undirected.remove_edges_from(nx.selfloop_edges(G_undirected))

    # Orient edges: lower-degree -> higher-degree (dependent -> dependency)
    G = nx.DiGraph()
    G.add_nodes_from(range(n))
    deg = dict(G_undirected.degree())
    for u, v in G_undirected.edges():
        if deg[u] <= deg[v]:
            G.add_edge(u, v)
        else:
            G.add_edge(v, u)

    return G


def compute_network_statistics(G):
    """Compute summary statistics for a directed network."""
    in_degrees = np.array([d for _, d in G.in_degree()])
    out_degrees = np.array([d for _, d in G.out_degree()])
    total_degrees = in_degrees + out_degrees

    stats = {
        'n_nodes': G.number_of_nodes(),
        'n_edges': G.number_of_edges(),
        'mean_in_degree': float(in_degrees.mean()),
        'mean_out_degree': float(out_degrees.mean()),
        'max_in_degree': int(in_degrees.max()),
        'max_out_degree': int(out_degrees.max()),
        'mean_total_degree': float(total_degrees.mean()),
    }

    # Power-law exponent via MLE on in-degree for BA (the degree with power-law)
    # or total degree for config model. Use k_min = max(2, mode).
    # Fit on degrees >= k_min where k_min chosen to be in power-law regime
    k_min_fit = max(2, int(np.median(total_degrees[total_degrees > 0])))
    degrees_above = total_degrees[total_degrees >= k_min_fit].astype(float)
    if len(degrees_above) > 10:
        n_above = len(degrees_above)
        gamma_mle = 1.0 + n_above / np.sum(np.log(degrees_above / (k_min_fit - 0.5)))
        stats['gamma_mle'] = float(gamma_mle)
        stats['k_min_fit'] = int(k_min_fit)
    else:
        stats['gamma_mle'] = float('nan')
        stats['k_min_fit'] = int(k_min_fit)

    # Degree moments for percolation threshold
    k = total_degrees.astype(float)
    k_mean = k.mean()
    k2_mean = (k ** 2).mean()
    stats['k_mean'] = float(k_mean)
    stats['k2_mean'] = float(k2_mean)
    stats['kappa'] = float(k2_mean / k_mean) if k_mean > 0 else float('nan')

    return stats


def fit_power_law_exponent(G, k_min_fit=None):
    """Fit power-law exponent to total degree distribution via MLE.

    Uses Clauset MLE with k_min chosen from the data.
    """
    total_degrees = np.array([G.in_degree(n) + G.out_degree(n) for n in G.nodes()])
    if k_min_fit is None:
        k_min_fit = max(2, int(np.median(total_degrees[total_degrees > 0])))
    degrees_above = total_degrees[total_degrees >= k_min_fit].astype(float)
    if len(degrees_above) < 10:
        return float('nan')
    n_above = len(degrees_above)
    gamma_mle = 1.0 + n_above / np.sum(np.log(degrees_above / (k_min_fit - 0.5)))
    return gamma_mle

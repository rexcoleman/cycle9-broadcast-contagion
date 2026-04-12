"""Detection and recovery mechanisms for supply chain contagion.

Models:
- Uniform detection: constant p_detect for all nodes
- Hub-targeted detection: p_detect(k) = min(p_base + alpha * log(k/k_min), 1.0)
- Contact-dependent stifling: ISS-style stifler mechanism (ablation)
- Cascading detection: contact-tracing when a node is detected (ablation)
"""

import numpy as np


def make_uniform_detector(p_coverage, rng=None):
    """Create uniform detection function.

    Each infected node has per-step detection probability = p_coverage.
    """
    if rng is None:
        rng = np.random.default_rng()

    def detect(node, degree, time_infected):
        return rng.random() < p_coverage

    return detect


def make_hub_targeted_detector(p_coverage, degrees, k_min=1, rng=None):
    """Create hub-targeted detection function.

    p_detect(k) = min(p_base + alpha * log(k/k_min), 1.0)

    Alpha is calibrated so the MEAN detection probability across all nodes
    equals p_coverage.
    """
    if rng is None:
        rng = np.random.default_rng()

    degrees = np.array(degrees, dtype=float)
    degrees = np.maximum(degrees, k_min)  # floor at k_min

    if p_coverage <= 0:
        def detect(node, degree, time_infected):
            return False
        return detect

    if p_coverage >= 1.0:
        def detect(node, degree, time_infected):
            return True
        return detect

    # Calibrate alpha so mean(p_detect) = p_coverage
    log_ratios = np.log(degrees / k_min)
    mean_log = log_ratios.mean()

    if mean_log <= 0:
        # No variation in degrees; fall back to uniform
        return make_uniform_detector(p_coverage, rng)

    # p_base + alpha * mean(log(k/k_min)) = p_coverage
    # We want p_base >= 0, so alpha <= p_coverage / mean_log
    # Start with alpha that gives reasonable spread
    # Try: set p_base = p_coverage * 0.3, solve for alpha
    # p_base + alpha * mean_log = p_coverage
    # alpha = (p_coverage - p_base) / mean_log

    # Better: maximize spread while keeping all probabilities in [0, 1]
    max_log = log_ratios.max()

    # Constraint: p_base + alpha * max_log <= 1.0
    # Constraint: p_base >= 0
    # Constraint: p_base + alpha * mean_log = p_coverage

    # From mean constraint: p_base = p_coverage - alpha * mean_log
    # From p_base >= 0: alpha <= p_coverage / mean_log
    # From max constraint: p_coverage - alpha * mean_log + alpha * max_log <= 1
    #                      alpha * (max_log - mean_log) <= 1 - p_coverage
    #                      alpha <= (1 - p_coverage) / (max_log - mean_log) if max_log > mean_log

    alpha_max_from_base = p_coverage / mean_log
    if max_log > mean_log:
        alpha_max_from_cap = (1.0 - p_coverage) / (max_log - mean_log)
        alpha = min(alpha_max_from_base, alpha_max_from_cap)
    else:
        alpha = alpha_max_from_base

    # Use 80% of max alpha to avoid edge effects
    alpha = alpha * 0.8
    p_base = p_coverage - alpha * mean_log

    # Clamp
    p_base = max(0.0, p_base)

    # Precompute per-node detection probabilities
    node_p_detect = {}
    for i, d in enumerate(degrees):
        d_clamped = max(d, k_min)
        p = min(p_base + alpha * np.log(d_clamped / k_min), 1.0)
        p = max(0.0, p)
        node_p_detect[i] = p

    def detect(node, degree, time_infected):
        p = node_p_detect.get(node, p_coverage)
        return rng.random() < p

    return detect


def make_stifling_fn(delta=0.5, rng=None):
    """Create contact-dependent stifling function (ISS ablation).

    A spreader becomes stifled when it contacts an infected/stifled neighbor.
    Stifling probability per infected-neighbor contact = delta.
    """
    if rng is None:
        rng = np.random.default_rng()

    def stifle(node, n_infected_neighbors):
        if n_infected_neighbors == 0:
            return False
        # Probability of NOT being stifled by any contact
        p_not_stifled = (1.0 - delta) ** n_infected_neighbors
        return rng.random() > p_not_stifled

    return stifle


def make_cascade_detection_fn(p_cascade=0.5, rng=None):
    """Create cascading detection function (ablation A4).

    When a node is detected, each neighbor is checked with probability p_cascade.
    """
    if rng is None:
        rng = np.random.default_rng()

    def cascade_detect(node, G, state, SUSCEPTIBLE, INFECTED):
        detected = set()
        neighbors = set(G.predecessors(node)) | set(G.successors(node))
        for nb in neighbors:
            if state[nb] == INFECTED and rng.random() < p_cascade:
                detected.add(nb)
        return detected

    return cascade_detect

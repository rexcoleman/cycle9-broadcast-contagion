"""Broadcast contagion engine for supply chain networks.

Discrete-time, non-diluting broadcast propagation:
- Each infected (spreader) node transmits to ALL out-neighbors each step
- Transmission is non-diluting: each neighbor gets full infection
- Detected nodes are removed (recovered) and cannot re-infect or be re-infected
"""

import numpy as np
import networkx as nx


def broadcast_propagation(G, seed_node, detection_fn, max_steps=500,
                          stifling_fn=None, cascade_detection_fn=None):
    """Run broadcast contagion with detection on a directed network.

    Parameters
    ----------
    G : nx.DiGraph
        Directed network (edge u->v means u depends on v).
        Propagation follows REVERSE edges: if v is infected,
        all nodes u that depend on v get infected.
    seed_node : int
        Initial infected node.
    detection_fn : callable(node, degree, time_infected) -> bool
        Returns True if node is detected (removed) this step.
    max_steps : int
        Maximum simulation steps.
    stifling_fn : callable or None
        If provided: stifling_fn(node, n_infected_neighbors) -> bool.
        For contact-dependent stifling ablation (H-4).
    cascade_detection_fn : callable or None
        If provided: called when a node is detected, returns set of
        additionally detected neighbors. For cascading detection ablation (A4).

    Returns
    -------
    dict with:
        cascade_fraction: fraction of nodes ever infected
        contained: bool (cascade < 10% of N)
        time_to_steady: number of steps to steady state
        infection_times: dict node -> time infected
        detection_times: dict node -> time detected
    """
    n = G.number_of_nodes()

    # Precompute reverse adjacency (who depends on each node)
    # If v is infected, all predecessors of v in the dependency graph get exposed
    # But in our directed graph, edge (u, v) means u depends on v
    # So if v is compromised, infection spreads to all u where (u, v) is an edge
    # i.e., v's in-edges give us the nodes that depend on v
    # Actually: if v is a dependency and gets compromised, all packages that
    # depend on v (= all u with edge u->v) get compromised
    # So propagation: infected v -> all u where edge (u, v) exists = predecessors of v
    reverse_adj = {}
    for node in G.nodes():
        reverse_adj[node] = list(G.predecessors(node))

    # Also precompute forward adj for stifling contact counting
    if stifling_fn is not None:
        forward_adj = {}
        for node in G.nodes():
            forward_adj[node] = list(G.successors(node))

    # Node degrees (total) for detection
    node_degrees = {}
    for node in G.nodes():
        node_degrees[node] = G.in_degree(node) + G.out_degree(node)

    # State: S=susceptible, I=infected(spreader), R=recovered(detected)
    SUSCEPTIBLE, INFECTED, RECOVERED = 0, 1, 2
    state = np.zeros(n, dtype=np.int8)

    state[seed_node] = INFECTED
    infection_times = {seed_node: 0}
    detection_times = {}

    active_infected = {seed_node}
    no_change_count = 0

    for t in range(1, max_steps + 1):
        new_infected = set()
        new_detected = set()

        # Detection phase: check each infected node
        for node in list(active_infected):
            time_infected = t - infection_times[node]

            if stifling_fn is not None:
                # Count infected/recovered neighbors for contact-dependent stifling
                neighbors = forward_adj.get(node, []) + reverse_adj.get(node, [])
                n_inf_neighbors = sum(1 for nb in neighbors
                                      if state[nb] in (INFECTED, RECOVERED))
                if stifling_fn(node, n_inf_neighbors):
                    new_detected.add(node)
                    continue

            if detection_fn(node, node_degrees[node], time_infected):
                new_detected.add(node)

        # Apply detections
        for node in new_detected:
            state[node] = RECOVERED
            active_infected.discard(node)
            detection_times[node] = t

            # Cascading detection (ablation A4)
            if cascade_detection_fn is not None:
                cascade_nodes = cascade_detection_fn(node, G, state, SUSCEPTIBLE, INFECTED)
                for cn in cascade_nodes:
                    if state[cn] == INFECTED:
                        state[cn] = RECOVERED
                        active_infected.discard(cn)
                        detection_times[cn] = t

        # Propagation phase: each infected node spreads to all dependents
        for node in list(active_infected):
            for neighbor in reverse_adj[node]:
                if state[neighbor] == SUSCEPTIBLE:
                    state[neighbor] = INFECTED
                    new_infected.add(neighbor)
                    infection_times[neighbor] = t

        active_infected.update(new_infected)

        # Check steady state
        if len(new_infected) == 0 and len(new_detected) == 0:
            no_change_count += 1
        else:
            no_change_count = 0

        if no_change_count >= 10 or len(active_infected) == 0:
            break

    total_infected = np.sum(state >= INFECTED)  # INFECTED + RECOVERED
    cascade_fraction = total_infected / n
    contained = cascade_fraction < 0.10

    return {
        'cascade_fraction': float(cascade_fraction),
        'contained': contained,
        'time_to_steady': t,
        'infection_times': infection_times,
        'detection_times': detection_times,
        'total_infected': int(total_infected),
    }

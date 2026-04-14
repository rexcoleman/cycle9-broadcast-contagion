# How Do Attacks Spread Between AI Agents? We Found the Critical Threshold

## Methodology

- 45,900 Monte Carlo simulation runs across 6 primary and 3 ablation conditions
- Barabási-Albert scale-free networks (m=3, N=500-5,000, directed)
- Broadcast contagion with heterogeneous time-dependent detection
- Baselines: homogeneous SIS (Pastor-Satorras & Vespignani 2001), static percolation (Cohen et al. 2003)

Full experimental design, all data, and reproduction scripts: [cycle9-broadcast-contagion on GitHub](https://github.com/rexcoleman/cycle9-broadcast-contagion).

Specific numbers:

- <!-- TEACHING — 50% target -->
- <!-- FINDINGS — 30% target -->
- I ran 45,900 Monte Carlo simulations across Barabási-Albert scale-free networks (500 to 5,000 nodes) to measure where this critical threshold falls. The attacks originate at hub packages — the top 1% most-depended-on packages in the network.
- | Detection Strategy | Critical Coverage (p_c) | 95% CI | What It Means |
- | Uniform detection | 0.39 | [0.38, 0.40] | Monitor 39% of all packages to contain attacks |

Full write-up with code: [YOUR_BLOG_URL]

Repo: 
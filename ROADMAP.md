# Roadmap: Broadcast Contagion Phase Transitions in Software Supply Chain Networks

## Phase 0: Setup and EDA (~1-2 hours)

### Tasks

1. **Set up simulation package structure.** Create `src/scn_contagion/` with modules: `networks.py` (network generation), `propagation.py` (broadcast contagion engine), `detection.py` (time-dependent heterogeneous detection), `simulation.py` (combined simulation runner), `analysis.py` (phase transition measurement), `baselines.py` (homogeneous SIS, static percolation). Use NetworkX for graph operations. Expected output: importable Python package with empty function signatures and docstrings.

2. **Implement network generation.** Two topology models:
   - Barabasi-Albert: `networkx.barabasi_albert_graph(n, m)` with m=3, directed by assigning edge direction from new node to existing (dependency = "depends on").
   - Configuration model: `networkx.configuration_model(degree_sequence)` with degree sequence drawn from power-law P(k) ~ k^(-gamma), gamma=2.7, k_min=1, k_max=sqrt(N). Convert to directed by orienting edges from lower-degree to higher-degree node (dependents point to dependencies).
   
   Target: generate N=1,000; 5,000; 10,000 for both topologies. Verify degree distributions: compute and plot degree distribution, verify power-law exponent within ±0.3 of target.

3. **EDA validation runs.** Generate 10 sample networks at each size. Compute: mean degree, max degree, degree distribution exponent (via MLE fit), clustering coefficient, diameter. Compare against published npm statistics (Decan et al. 2019: gamma ~ 2.5-3.0 for npm). Expected output: `outputs/eda/network_statistics.csv` with per-network metrics.

4. **Sanity-check propagation.** Implement basic broadcast propagation (no detection) on one BA network (N=1,000). Verify: from a single seed node, cascade reaches >95% of reachable nodes. Expected output: cascade size distribution over 100 random seed selections.

### Dependencies
- Python 3.8+, NetworkX, NumPy, SciPy, Matplotlib installed on Azure VM.

### Verification
- [ ] Both topology generators produce valid directed graphs with expected degree distributions
- [ ] Degree distribution exponents match targets within ±0.3
- [ ] Pure broadcast propagation produces near-complete cascades (>95% of reachable component)
- [ ] Network generation completes in <30 seconds for N=10,000

---

## Phase 1: Core Simulation Implementation (~2-3 hours)

### Tasks

1. **Implement broadcast contagion engine.** Discrete-time simulation:
   - Each time step: every infected (spreader) node transmits to all out-neighbors with probability beta (propagation rate). Default beta=1.0 (deterministic broadcast).
   - Transmission is non-diluting: each neighbor receives the full infection regardless of how many neighbors the spreader has.
   - Track: infection time per node, total infected count per time step, cascade trajectory.

2. **Implement time-dependent detection engine.**
   - Each infected node has a per-step detection probability p_detect(k) depending on its degree k.
   - Detection model: `p_detect(k) = min(p_base + alpha * log(k / k_min), 1.0)` where p_base is baseline detection probability, alpha controls degree-correlation strength.
   - Uniform detection: alpha=0, p_detect(k) = p_base for all k.
   - Hub-targeted detection: alpha > 0, calibrated so that total detection probability across the network matches the target coverage fraction.
   - Detected nodes transition to "recovered" (removed from propagation, cannot re-infect or be re-infected).
   - Track: detection time per node, number of detections per time step.

3. **Implement contact-dependent stifling (ablation).** Original ISS mechanism: an infected node becomes stifled when it contacts another infected or stifled node. Stifling probability per contact = delta. This is the ablation condition for H-4.

4. **Implement simulation runner.** For a given (topology, N, detection_strategy, p_coverage) configuration:
   - Generate network (or load pre-generated).
   - Select random seed node (infected at t=0).
   - Run propagation + detection until steady state (no new infections for 10 consecutive steps, or all nodes infected/recovered).
   - Record: final cascade size (fraction of nodes ever infected), containment status (cascade < 0.10*N = contained), time-to-steady-state.
   - Repeat for 100 Monte Carlo seeds.

5. **Implement baselines.**
   - Homogeneous SIS: uniform recovery rate gamma for all nodes, no detection, continuous reinfection possible. Run to steady state, measure prevalence.
   - Static percolation: compute Cohen's analytical p_c from degree distribution moments: `p_c = 1 - 1/(kappa - 1)` where `kappa = <k^2>/<k>`. For targeted immunization: compute via acquaintance immunization formula.

### Dependencies
- Phase 0 completed (network generation validated, package structure exists).

### Verification
- [ ] Zero-detection (p_coverage=0): cascade fraction > 0.95 (sanity check — broadcast without detection infects nearly everything)
- [ ] Full-detection (p_coverage=1.0): cascade fraction < 0.05 (detection catches everything)
- [ ] Homogeneous SIS baseline on BA (m=3, N=5,000): endemic prevalence > 0 at lambda = 0.01 (vanishing threshold)
- [ ] Static percolation p_c computable from degree distribution
- [ ] Single simulation run (N=5,000) completes in <5 seconds
- [ ] 100 Monte Carlo runs (N=5,000, single coverage point) complete in <10 minutes

---

## Phase 2: Phase Transition Sweep (~4-6 hours compute)

### Tasks

1. **Run primary phase transition sweep.** For each of 6 conditions:

   | Condition | Topology | N | Strategy | Coverage sweep |
   |---|---|---|---|---|
   | C1 | BA (m=3) | 1,000 | Uniform | p in [0.00, 1.00] step 0.02 (50 points) |
   | C2 | BA (m=3) | 5,000 | Uniform | p in [0.00, 1.00] step 0.02 |
   | C3 | BA (m=3) | 10,000 | Uniform | p in [0.00, 1.00] step 0.02 |
   | C4 | Config (npm) | 5,000 | Uniform | p in [0.00, 1.00] step 0.02 |
   | C5 | BA (m=3) | 5,000 | Hub-targeted | p in [0.00, 1.00] step 0.02 |
   | C6 | Config (npm) | 5,000 | Hub-targeted | p in [0.00, 1.00] step 0.02 |

   Each point: 100 Monte Carlo repetitions. Total: 6 x 50 x 100 = 30,000 simulation runs.
   
   Expected compute: ~4-6 hours on Azure VM (estimated ~0.7 seconds per run at N=5,000).
   
   Output: `outputs/sweep/C{1-6}_results.csv` — columns: condition, p_coverage, run_id, cascade_fraction, contained (0/1), time_to_steady_state.

2. **Run ablation sweeps.** For ablation conditions on BA (m=3), N=5,000:

   | Ablation | What changes | Coverage sweep |
   |---|---|---|
   | A1 | Uniform detection (alpha=0) at same total coverage as hub-targeted | p in [0.00, 1.00] step 0.02, 100 reps (already C2) |
   | A2 | Contact-dependent stifling instead of time-dependent detection | p in [0.00, 1.00] step 0.02, 100 reps |
   | A3 | Undirected graph (edges bidirectional) | p in [0.00, 1.00] step 0.02, 100 reps |
   | A4 | Cascading detection (when node detected, neighbors checked with p_cascade=0.5) | p in [0.00, 1.00] step 0.02, 100 reps |

   Additional: 4 x 50 x 100 = 20,000 runs (~3-4 hours).
   
   Output: `outputs/ablation/A{1-4}_results.csv` — same column format.

3. **Compute analytical baselines.**
   - Homogeneous SIS prevalence curve: run SIS on BA (m=3, N=5,000) with recovery rates matching mean detection probability for each coverage fraction. Record steady-state prevalence.
   - Static percolation p_c: compute for each topology from degree distribution moments. Record as single values for comparison.
   
   Output: `outputs/baselines/sis_prevalence.csv`, `outputs/baselines/percolation_pc.csv`.

### Dependencies
- Phase 1 completed (simulation code validated via sanity checks).

### Verification
- [ ] All 30,000 primary sweep runs completed without errors
- [ ] All 20,000 ablation sweep runs completed without errors
- [ ] Output files contain expected number of rows (30,000 for primary, 20,000 for ablation)
- [ ] Containment probability ranges from ~0 at low coverage to ~1 at high coverage for each condition (basic sanity)
- [ ] No NaN or infinite values in output

---

## Phase 3: Analysis and Phase Transition Measurement (~2-3 hours)

### Tasks

1. **Compute containment probability curves.** For each condition and coverage point: containment_probability = count(contained) / 100. Plot with Wilson score 95% CIs.

2. **Estimate phase transition location (p_c).** For each condition:
   - Fit logistic function to containment probability curve: `P_contain(p) = 1 / (1 + exp(-k*(p - p_c)))`.
   - p_c = midpoint of fitted logistic (containment probability = 0.5 crossing).
   - Bootstrap (1000 resamples): resample the 100 runs per coverage point, refit logistic, record p_c. Report 95% CI from bootstrap distribution.
   - Sharpness metric: k parameter of fitted logistic, normalized to [0,1] by dividing by theoretical maximum (step function sharpness).

3. **Compute hub-targeting efficiency ratio.** For each topology at N=5,000:
   - Ratio = p_c_uniform / p_c_targeted.
   - Bootstrap 95% CI on ratio via paired bootstrap (same resample indices for uniform and targeted).
   - Permutation test (10,000 permutations) for H0: ratio = 1.0.

4. **Compute ablation comparisons.** For each ablation vs. full model:
   - |p_c_ablation - p_c_full| with bootstrap CI.
   - |sharpness_ablation - sharpness_full| with bootstrap CI.

5. **Compute analytical consistency checks.**
   - Compare simulation p_c against static percolation p_c (expect simulation > analytical).
   - Compare homogeneous SIS prevalence curve against theoretical prediction.

6. **Generate phase transition plots.** For each condition: containment probability vs. coverage fraction with 95% CIs. Overlay all conditions on a summary plot. Generate ablation comparison plots.

   Output: `outputs/analysis/phase_transition_summary.csv`, `outputs/analysis/plots/`, `outputs/analysis/hypothesis_resolution.md`.

7. **Shai-Hulud quasi-validation.** Parameterize simulation with npm-like topology (config model, N=10,000, gamma=2.7). Estimate detection coverage at time of Shai-Hulud V1 (~500 packages compromised in ~48 hours). Run simulation with estimated parameters. Compare: does simulation-predicted cascade size and time-to-containment roughly match observed ~500 packages?

### Dependencies
- Phase 2 completed (all sweep data available).

### Verification
- [ ] p_c estimated with 95% CI width < 0.10 for all 6 primary conditions
- [ ] Hub-targeting ratio > 1.0 (hub-targeting is at least somewhat more efficient)
- [ ] All 4 hypotheses have resolution data
- [ ] Phase transition plots generated for all conditions
- [ ] Analytical baselines computed and compared

---

## Phase 4: Synthesis and FINDINGS Writing (~2-3 hours)

### Tasks

1. **Resolve all 4 hypotheses.** Write resolution narrative for each: state the hypothesis, the evidence (specific output files, metric values), and the resolution (SUPPORTED/REFUTED/INCONCLUSIVE).

2. **Synthesize findings into FINDINGS.md structure.** Follow the govML FINDINGS template:
   - Abstract (≤250 words)
   - Methodology (broadcast contagion model, detection mechanism, simulation setup)
   - Results per condition (containment probability curves, p_c values, sharpness)
   - Ablation results
   - Hypothesis resolution narratives
   - Novelty Assessment: differentiate from ≥5 prior works
   - Cross-Domain Connections: state the domain-agnostic principle
   - Generalization Analysis: evaluation conditions table with measured values and failure mode assessments
   - Practitioner Impact: detection coverage decision matrix, actionable recommendations
   - Boundary Statement: explicit limitations and scope of applicability
   - Pre-emptive Criticism: address kill shots from ED §4

3. **Tag all claims** per CLAIM_STRENGTH_SPEC. Every quantitative claim gets a strength tag.

4. **Write Novelty Assessment.** Differentiate from: (1) Pastor-Satorras & Vespignani 2001, (2) Moreno et al. 2004, (3) Nekovee et al. 2007, (4) Cohen et al. 2003, (5) Yang et al. 2015. For each: "they did X, we do Y, the difference is Z."

5. **Write Cross-Domain Connections.** State the domain-agnostic principle: "In heterogeneous networks with broadcast propagation and node-level recovery, there exists a critical recovery coverage fraction separating contained and endemic regimes. Targeted deployment on high-connectivity nodes achieves containment at dramatically lower total coverage."

6. **Write Generalization Analysis.** Populate evaluation conditions table with measured p_c, sharpness, and failure mode assessment for all 6 conditions. Document which failure modes were triggered and which were not.

7. **Hostile Baseline Check.** Verify that our model produces meaningfully different results from: (a) homogeneous SIS (different threshold behavior), (b) static percolation (different p_c values), (c) Cycle 7 diluting-shock model (qualitatively different cascade dynamics). If our model is indistinguishable from any baseline, document this honestly.

8. **Self-audit FINDINGS.md:**
   - Count quoted passages (≥8 required)
   - Verify 100% claims tagged
   - Check no prohibited language
   - Verify all sections per current FINDINGS template present
   - Verify depth budget met

### Dependencies
- Phase 3 completed (all analysis results available).

### Verification
- [ ] All sections per current FINDINGS template present
- [ ] Depth budget met (≥8 quoted passages counted)
- [ ] 100% claims tagged per CLAIM_STRENGTH_SPEC
- [ ] No prohibited language
- [ ] All 4 hypotheses resolved with evidence references
- [ ] Novelty Assessment differentiates from ≥5 prior works
- [ ] quality_loop.sh score ≥ 8.0

---

## Estimated Source Plan

| Source | Type | Access Method | Priority |
|---|---|---|---|
| Pastor-Satorras & Vespignani (2001), PRL | Paper (abstract + key results) | WebSearch for abstract/results; cite from LANDSCAPE_ASSESSMENT | HIGH |
| Nekovee et al. (2007), Physica A | Paper (abstract + analytical results) | WebSearch | HIGH |
| Cohen et al. (2003), PRL | Paper (analytical immunization fractions) | WebSearch | HIGH |
| Yang et al. (2015), Scientific Reports | Paper (heterogeneous recovery threshold restoration) | WebSearch | HIGH |
| de Arruda et al. (2022), Nature Communications | Paper (correlation-induced transitions) | WebSearch | MEDIUM |
| Moreno et al. (2004), Phys Rev E | Paper (ISS on complex networks) | WebSearch | MEDIUM |
| Cator & Van Mieghem (2024), MDPI | Paper (NIMFA near threshold) | WebSearch | MEDIUM |
| Shai-Hulud incident data | Security blog posts (Sysdig, PaloAlto) | WebSearch | HIGH |
| Decan et al. (2019) | Paper (npm degree distributions) | WebSearch | MEDIUM |
| CISA SBOM Sharing Lifecycle Report (2024) | Policy document | WebSearch | MEDIUM |
| libraries.io npm dependency data | Open dataset | WebSearch for published statistics | LOW |

## Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Simulation too slow for full sweep within compute budget | LOW | HIGH | Monitor compute time during Phase 1 sanity checks. If single run > 2 seconds at N=5,000, reduce to N=3,000 or reduce Monte Carlo reps to 50 (wider CIs but still usable). Fallback: offload to Mac Mini (48GB) via Tailscale. |
| No identifiable phase transition (linear containment curve) | LOW | HIGH | This is a valid finding — document honestly as H-1 REFUTED. The null result (no threshold) is publishable and arguably more surprising than the expected threshold. Check simulation for bugs before concluding. |
| Memory issues at N=10,000 | LOW | MED | NetworkX graph for N=10,000 with m=3: ~240K edges, ~50MB memory. Well within 7.7 GiB. If memory exceeds 6 GiB during sweep, reduce to N=7,500. |
| Degree distribution mismatch with real npm data | MED | MED | Configuration model parameterized from published statistics. If generated distributions deviate by >0.5 from target exponent, adjust k_max or use alternative fitting method. Sensitivity analysis across gamma in [2.0, 3.5] covers the uncertainty. |
| Homogeneous SIS baseline does not reproduce vanishing threshold | LOW | HIGH | This would indicate a simulation bug. Stop and debug before proceeding. The vanishing threshold on BA networks is one of the most well-established results in network epidemiology. |
| Source inaccessible (paper behind paywall) | LOW | LOW | All critical sources have accessible abstracts and key results via WebSearch. No full-text access required — our engagement is with specific results and analytical formulas, not with detailed methodology that requires full-text reading. |
| quality_loop.sh score < 8.0 | MED | MED | Design FINDINGS.md structure from the template before filling. Tag claims during writing, not after. Run quality_loop.sh before final commit and iterate if needed. |

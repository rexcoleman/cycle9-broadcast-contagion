# Project: Broadcast Contagion Phase Transitions in Software Supply Chain Networks

## Research Question

In software supply chain networks with broadcast-type attack propagation, does detection coverage (version pinning, signature verification, SBOM scanning) create an effective phase transition threshold — and if so, what is the critical coverage fraction below which containment fails?

## Scope

- **In scope:** Broadcast (non-diluting) contagion simulation on static supply chain network topologies with heterogeneous time-dependent detection as a recovery mechanism. Phase transition measurement (p_c location, sharpness, sensitivity to topology and targeting strategy). Comparison of uniform vs. hub-targeted detection deployment. Comparison against analytical predictions (SIS homogeneous, static percolation). Quasi-validation against Shai-Hulud npm worm incident data. ≥3 network sizes (N=1,000; 5,000; 10,000), ≥2 topologies (BA scale-free; configuration model with npm degree distribution), ≥2 detection strategies (uniform; hub-targeted).
- **Out of scope:** Temporal network evolution (topologies change over time). Adaptive adversaries (attackers who respond to detection). Multiplex/multi-layer networks. Version constraint modeling (semantic versioning, lock files as partial immunity). Community structure within dependency graphs. Detection mechanism internals (specific SBOM tool performance characteristics). Real-time parameterization from live registry data. These are extensions for future cycles (limitations #6-#9 from Cycle 7).
- **Kill conditions:** (1) No identifiable phase transition on any topology at any network size (containment probability is strictly linear in coverage across all conditions — sharpness < 0.10 everywhere). This would mean the threshold framing is fundamentally wrong and the research question as posed has a null answer. (2) Simulation cannot complete within the compute budget (>24 hours for the primary sweep on Azure VM). This would indicate the simulation design is computationally infeasible at the planned scale. (3) Homogeneous SIS baseline does NOT reproduce the known vanishing-threshold result — this would indicate a simulation bug that invalidates all results.

## Success Criteria

1. Phase transition location (p_c) measured with 95% CI width < 0.10 for all 6 primary conditions.
2. Hub-targeting efficiency ratio (p_c_uniform / p_c_targeted) measured with 95% CI excluding 1.0.
3. Evaluation conditions table fully populated with results for all 6 conditions.
4. ≥2 ablation studies completed (uniform vs. hub-targeted; time-dependent vs. contact-dependent detection).
5. Analytical consistency check: homogeneous SIS baseline reproduces vanishing threshold; static percolation baseline produces p_c within expected range.
6. All 4 pre-registered hypotheses resolved (SUPPORTED, REFUTED, or INCONCLUSIVE with evidence).
7. FINDINGS.md passes quality_loop.sh (score ≥ 8.0) with all claims tagged per CLAIM_STRENGTH_SPEC.

## Forbidden Proxies

- High word count does not count as thoroughness
- Many simulation runs does not count as rigor (if all runs use the same flawed model)
- Internal consistency does not count as correctness (a buggy simulation can be internally consistent)
- LLM self-assessment does not count as validation
- Smooth-looking phase transition plots do not count as evidence of a sharp threshold (must quantify sharpness metric)
- Agreement with expected range does not count as external validation (the expected range is broad enough to accommodate many results)
- Citing 7 prior works does not count as deep engagement (must state what each work contributes AND what it cannot do)

## Gap Analysis

**What gap does this research address?**

No existing model combines broadcast (non-diluting) contagion with heterogeneous time-dependent detection on realistic supply chain network topologies to compute containment thresholds. The critical detection coverage fraction for software supply chain attack containment is unmeasured.

**Why hasn't it been answered?**

Three communities have relevant tools but none spans the gap: (a) network epidemiologists model epidemic thresholds but with homogeneous recovery and no detection mechanism (Pastor-Satorras & Vespignani 2001), (b) information epidemiologists model rumor spreading with stifler recovery but using contact-dependent stifling on undirected graphs (Moreno et al. 2004, Nekovee et al. 2007), (c) supply chain security researchers model attack propagation but using financial contagion frameworks with shock dilution (Acemoglu et al. 2015, our Cycle 7). The gap exists at the intersection of these three communities.

**Sources checked to confirm gap:** arXiv ("broadcast contagion detection phase transition supply chain" — 0 results), Google Scholar ("supply chain detection coverage threshold containment" — 0 relevant results), GitHub ("supply chain contagion simulation broadcast" — 0 matching projects). Confirmed in LANDSCAPE_ASSESSMENT §4 Frontier Moat Test.

## Significance

If detection coverage creates a phase transition in supply chain attack containment, the policy implications are immediate: below the threshold, incremental SBOM adoption provides near-zero containment benefit; above it, containment improves rapidly. This transforms the current policy recommendation ("gradually increase SBOM adoption across the ecosystem") into a quantitative target ("reach p_c detection coverage on hub packages first"). For practitioners: the detection coverage decision matrix enables organizations to assess whether their supply chain monitoring is above or below the containment threshold — and whether to invest in breadth (more packages monitored) or depth (better monitoring of hub packages).

## Prior Work Engaged (minimum 3)

1. **Pastor-Satorras & Vespignani (2001), PRL 86(14):3200-3203:** Proved that SIS epidemic threshold vanishes on scale-free networks — any nonzero infection rate leads to endemic persistence. Central methodology: analytical mean-field treatment + Monte Carlo simulation on BA networks up to N=10^6. Key data: epidemic threshold lambda_c approaches 0 for power-law networks with gamma <= 3. Relevance: establishes the "no defense" baseline — without detection, broadcast contagion on scale-free supply chain networks has NO containment threshold. Our work tests whether adding heterogeneous detection restores a threshold.

2. **Nekovee, Moreno, Bianconi & Marsili (2007), Physica A 374(1):457-470:** Derived analytical mean-field equations for ISS rumor spreading on complex networks. Central methodology: heterogeneous mean-field approximation with stifling rate as tunable control parameter. Key data: critical threshold vanishes on scale-free networks in infinite-size limit; stifling rate shifts the phase boundary. Relevance: provides the analytical framework we adapt — the stifling rate maps to detection coverage fraction. Our adaptation: replace contact-dependent stifling with time-dependent detection, use directed graphs, test at finite realistic sizes.

3. **Cohen, Havlin & ben-Avraham (2003), PRL 91:247901:** Computed critical immunization fraction for scale-free networks and introduced acquaintance immunization. Central methodology: bond percolation mapping of SIR model, analytical derivation of p_c from degree distribution moments. Key data: targeted immunization of high-degree nodes achieves containment at dramatically lower fractions than random; acquaintance immunization achieves near-targeted efficiency without global knowledge. Relevance: provides the hub-targeting baseline — our work tests whether Cohen's static percolation advantage transfers to dynamic broadcast contagion with detection latency.

4. **Yang et al. (2015), Scientific Reports 5:13122:** Showed that intrinsic node heterogeneity (heterogeneous susceptibility and recovery rates correlated with degree) can restore large epidemic thresholds on networks that would otherwise have vanishing thresholds. Central methodology: extended SIS with node-level heterogeneity + adaptive network structure. Key data: when high-degree nodes have higher recovery rates, the epidemic threshold increases substantially. Relevance: directly supports our core hypothesis — in supply chains, high-degree packages (popular, widely-depended-upon) ARE monitored more intensively, creating the degree-recovery correlation Yang et al. show restores thresholds.

5. **de Arruda et al. (2022), Nature Communications 13:3049:** Characterized phase transition in Maki-Thompson rumor model, showing that dynamical correlations change the universality class — mean-field approximation is insufficient. Central methodology: heterogeneous mean-field + pairwise approximation + Monte Carlo on synthetic and real networks. Key data: continuous phase transition IS present (overturning earlier claims); pairwise correlations are essential. Relevance: validates our choice of agent-based simulation over pure analytical treatment — mean-field alone cannot correctly characterize the threshold region.

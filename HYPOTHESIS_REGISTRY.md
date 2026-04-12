# HYPOTHESIS REGISTRY: Broadcast Contagion Phase Transitions in Software Supply Chain Networks

<!-- version: 1.0 -->
<!-- created: 2026-04-12 -->

> **Upstream:** LANDSCAPE_ASSESSMENT (prior work), RESEARCH_QUESTION_SPEC (question + gap), EXPERIMENTAL_DESIGN (methodology + baselines)
> **Downstream:** EXECUTION_PROTOCOL (experiment grounded in hypotheses), FINDINGS (hypothesis resolution narratives)

## Pre-Registration Lock

**Lock commit:** f0a9c0c030a333d976a0685b7c0e61e2582629ad
**Lock date:** 2026-04-12

> **Temporal gate (LL-74):** All hypotheses must be committed and locked before any experimental results are generated. Any experiment output with a git timestamp before the lock commit is invalid. Verify: `git log --oneline HYPOTHESIS_REGISTRY.md | tail -1` should predate all experiment outputs.

---

## 1) Pre-Registration Protocol

Hypotheses MUST be written **before** Phase 1 experiments begin.

**Gate:** >= 3 hypotheses registered and committed to version control before any simulation script is executed.

---

## 2) Registry Table

| hypothesis_id | statement | falsification_criterion | metric | field_surprise | resolution | evidence |
|---|---|---|---|---|---|---|
| H-1 | On scale-free supply chain networks (BA model, m=3, N=5,000) with time-dependent heterogeneous detection, there exists a critical detection coverage fraction p_c in [0.05, 0.60] such that containment probability transitions from <0.20 to >0.80 within a coverage range of 0.10 (i.e., the phase transition is sharp, with sharpness metric > 0.15). | No identifiable phase transition: containment probability increases linearly with coverage (sharpness < 0.15) across the full range [0, 1], OR p_c falls outside [0.05, 0.60]. | p_c location via bootstrap (95% CI width < 0.10); sharpness = max(dp_contain/dp_detect) normalized to [0,1]; threshold for SUPPORTED: sharpness > 0.15 AND p_c in [0.05, 0.60] with CI width < 0.10. | **Network epidemiologist surprise:** If NO threshold exists despite adding heterogeneous recovery, it contradicts Yang et al. (2015) which showed degree-correlated recovery restores thresholds on scale-free networks. This would imply broadcast contagion on supply chains is fundamentally more difficult to contain than standard epidemics — a result that would challenge the entire detection-coverage-as-defense framework. **Supply chain practitioner surprise:** If p_c < 0.15 with hub-targeting, it means current monitoring of popular packages may already provide effective containment — contradicting the "we're catastrophically under-protected" narrative dominant in CISA/NIST guidance. | PENDING | — |
| H-2 | Hub-targeted detection (degree-proportional allocation) achieves containment at a critical coverage fraction p_c_targeted that is at least 3x lower than uniform detection p_c_uniform on the same network topology (BA model, N=5,000). Formally: p_c_uniform / p_c_targeted >= 3.0. | Hub-targeting ratio < 2.0 (p_c_uniform / p_c_targeted < 2.0) — the efficiency gain from targeting hubs is less than 2x, meaning detection latency and dynamic propagation erode most of the static percolation advantage predicted by Cohen et al. (2003). | Hub-targeting efficiency ratio = p_c_uniform / p_c_targeted; bootstrap 95% CI on ratio; threshold for SUPPORTED: lower bound of CI on ratio >= 3.0; threshold for REFUTED: upper bound of CI on ratio < 2.0. | **Network immunization theorist surprise:** Cohen et al. (2003) predicts exponential targeting advantage in static percolation. If the dynamic advantage is <2x, it means detection latency fundamentally changes the immunization calculus — the static percolation framework is misleading for practical containment. This would surprise researchers who extend Cohen's results to dynamic settings. **Policy maker surprise:** If targeting advantage is >10x, it means monitoring just the top 1-2% of packages by dependency count provides ecosystem-level containment — a dramatic simplification of the policy recommendation from "universal SBOM adoption" to "monitor the top 100 packages." | PENDING | — |
| H-3 | The critical detection coverage fraction p_c for realistic supply chain topologies (configuration model with npm-derived P(k) ~ k^(-2.7), N=5,000) falls in the range [0.10, 0.40] for uniform detection and [0.02, 0.15] for hub-targeted detection. Furthermore, p_c is approximately stable across network sizes N in {1000, 5000, 10000}: |p_c(N1) - p_c(N2)| < 0.10 for all pairs. | Uniform p_c falls outside [0.05, 0.60] on the configuration model, OR p_c varies by >0.15 across network sizes (strong finite-size effects make the threshold size-dependent and non-generalizable). | p_c measured at containment probability = 0.5 crossing; bootstrap 95% CI; size-stability metric = max pairwise |p_c(Ni) - p_c(Nj)| across N in {1000, 5000, 10000}; threshold for SUPPORTED: p_c in stated ranges AND size-stability < 0.10; REFUTED: p_c outside [0.05, 0.60] OR size-stability > 0.15. | **Supply chain security field surprise:** This would be the first quantitative measurement of a detection coverage threshold for supply chain attack containment. ANY specific p_c value would be news — the field currently has no number to work with. If p_c_uniform ~ 0.25, it suggests current ~20-40% adoption rates are in the transition region — some ecosystems are above threshold, some below. If p_c_targeted ~ 0.05, it suggests that monitoring the top 5% of packages by popularity may suffice for containment. | PENDING | — |
| H-4 | The time-dependent detection adaptation (our model) produces a qualitatively different phase transition profile than the original contact-dependent ISS stifler mechanism on the same network topology: the p_c values differ by >0.05, OR the sharpness metrics differ by >0.10. | Phase transition profile (p_c and sharpness) is indistinguishable between time-dependent and contact-dependent models: |p_c_time - p_c_contact| < 0.05 AND |sharpness_time - sharpness_contact| < 0.10. | |p_c_time - p_c_contact| and |sharpness_time - sharpness_contact| with bootstrap CIs; SUPPORTED if at least one metric exceeds threshold; REFUTED if both below threshold. | **Rumor spreading theorist surprise:** If the two mechanisms produce indistinguishable results, it means the contact-dependent stifler mechanism is a sufficient proxy for time-dependent detection — the ISS framework can be directly applied to supply chain networks without adaptation. This would simplify the analytical framework but reduce the novelty of our adaptation. **Methodological surprise for our pipeline:** If REFUTED, it suggests that the mechanism adaptation we designed (contact-dependent to time-dependent) does not materially affect the dynamics — the simpler ISS model suffices, and our methodological contribution is smaller than expected. | PENDING | — |

---

## 3) Resolution Protocol

After experiments complete, revisit **every** hypothesis and assign a resolution:

| Resolution | Criteria |
|---|---|
| **SUPPORTED** | Metric meets or exceeds the stated threshold across all specified conditions |
| **REFUTED** | Metric falls below the stated threshold |
| **INCONCLUSIVE** | Ambiguous results (e.g., supported on one topology but not another), insufficient data, or metric within noise margin |

---

## 4) Resolution Log

| ID | Status | Evidence | Date |
|---|---|---|---|
| H-1 | PENDING | — | — |
| H-2 | PENDING | — | — |
| H-3 | PENDING | — | — |
| H-4 | PENDING | — | — |

---

## 5) Acceptance Criteria

- [ ] >= 3 hypotheses registered before Phase 1
- [ ] All hypotheses follow the required format (all fields populated)
- [ ] All hypotheses resolved (no PENDING status at project end)
- [ ] Every resolution includes an evidence reference to a specific output file
- [ ] No hypothesis was added after experiment results were observed (verified by git timestamps)
- [ ] Resolution narrative for each hypothesis included in FINDINGS.md

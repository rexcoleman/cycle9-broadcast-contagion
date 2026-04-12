# Requirements: Broadcast Contagion Phase Transitions in Software Supply Chain Networks

## Deliverables

1. **FINDINGS.md** — govML-compatible, all claims tagged per CLAIM_STRENGTH_SPEC. Sections: Abstract, Methodology, Results (per condition), Hypothesis Resolution, Novelty Assessment (differentiate from ≥5 prior works), Cross-Domain Connections, Generalization Analysis (evaluation conditions table with failure modes), Practitioner Impact, Boundary Statement, Pre-emptive Criticism.
2. **Simulation code** — Python package `scn-contagion/` with modular architecture: network generation, broadcast propagation engine, detection/recovery engine, phase transition measurement, analysis pipeline. Installable, documented, parameterizable.
3. **Detection coverage decision matrix** — CSV + interactive plot mapping network parameters (N, gamma, detection strategy) to critical detection thresholds p_c.
4. **Phase transition plots** — Containment probability vs. detection coverage fraction for all 6 primary conditions, with 95% CIs.
5. **Ablation results** — Comparison tables for all 4 ablation conditions.

## Quality Requirements

- **Depth budget:** ≥8 quoted passages from primary sources in FINDINGS.md. Sources must be quoted with specific claims, not just cited. "Pastor-Satorras & Vespignani (2001) proved that 'the epidemic threshold vanishes for scale-free networks with gamma <= 3'" counts; "Pastor-Satorras & Vespignani (2001) studied epidemic spreading" does not.
- **Minimum sources:** ≥7 distinct primary sources substantively engaged (methodology, results, limitations stated for each). The 7 works inventoried in LANDSCAPE_ASSESSMENT §1 establish the minimum.
- **100% claims tagged** per CLAIM_STRENGTH_SPEC. No untagged quantitative claims.
- **Hostile baseline check** must SURVIVE: run homogeneous SIS on same topologies — if our model does not produce meaningfully different results, the contribution is null.
- **Novelty Assessment** must differentiate from ≥5 prior works with specific "they did X, we do Y, the difference is Z" statements.
- **All paper titles verified** via WebSearch before citing in FINDINGS.md.
- **Hypothesis resolution:** All 4 pre-registered hypotheses resolved with evidence references to specific output files.
- **Phase transition measurement quality:** p_c estimated with 95% CI width < 0.10 for all primary conditions.
- **Ablation completion:** ≥2 ablation conditions completed with quantified comparison to the full model.
- **Generalization analysis:** Evaluation conditions table populated for all 6 conditions with measured values and failure mode assessments.

## Constraints

- **Single research cycle** — must complete in one Executor session. Phase 1 (simulation): 4-8 hours. Phase 2 (analysis): 2-3 hours. Phase 3 (FINDINGS writing): 2-3 hours. Total: ≤14 hours.
- **Computational research** — simulation-based, Python. No external data collection, no human subjects, no API calls during simulation.
- **Compute:** Azure VM with 7.7 GiB RAM, no GPU. Network sizes capped at N=10,000. Phase transition sweep: 50 coverage points x 100 Monte Carlo reps per condition = 5,000 runs per condition, 30,000 runs across 6 primary conditions. Fallback: Mac Mini (48GB M4 Pro) via Tailscale for larger runs if needed.
- **govML governance:** All templates filled BEFORE Phase 1 compute. EXECUTION_PROTOCOL.md filled DURING execution (not backfilled post-hoc). FINDINGS.md must pass quality_loop.sh ≥ 8.0.
- **EP engagement (>100 lines):** EXECUTION_PROTOCOL.md must be filled substantively:
  - §1 Quality gates: simulation sanity checks (zero-detection = full cascade, 100%-detection = zero cascade, homogeneous SIS reproduces vanishing threshold)
  - §2 Measurement protocol: effect sizes for each hypothesis, p_c estimation method, CI computation
  - §3 Blinding: N/A for computational research (no human judgment in measurement)
  - §4 Refinement: N/A (pre-registered design, no iterative refinement)
  - §5 Deviation log: document any deviations from this experimental design during execution
- **R34 depth sections in ED:** Adaptive Adversary Analysis, Statistical Plan, Ablation Plan present in EXPERIMENTAL_DESIGN.md (filled by Researcher-Planner, not deferred to Executor).
- **DP#19 (Observation ≠ Conclusion Separation):** All simulation outputs are raw measurements. Interpretation, threshold identification, and policy recommendations are separate analysis steps documented in distinct FINDINGS sections. The Executor must not embed interpretive conclusions in measurement code or output files.
- **All claims independently verifiable** from cited sources + simulation output files.

## Research Type

**Computational** — simulation-based study. No literature synthesis required beyond the prior work engagement already completed in stages 0-2. The Executor runs simulations, measures phase transitions, resolves hypotheses, and writes FINDINGS.

## Verification Criteria

| Check | Method | Pass Threshold |
|---|---|---|
| Homogeneous SIS reproduces vanishing threshold | Run SIS with uniform recovery, no detection; verify cascade reaches O(N) at small infection rates | Cascade fraction > 0.80 at infection rate = 0.01 on BA (m=3, N=5,000) |
| Static percolation bound | Compute Cohen's p_c from degree distribution; verify simulation p_c > analytical p_c | p_c_simulation > p_c_analytical (dynamic threshold exceeds static bound) |
| Zero-detection full cascade | Run broadcast contagion with p_detect = 0 | Cascade fraction > 0.95 for any infection rate > 0 |
| Full-detection zero cascade | Run broadcast contagion with p_detect = 1.0 | Cascade fraction < 0.05 |
| CI width | Bootstrap 95% CI on p_c | Width < 0.10 for all primary conditions |
| quality_loop.sh | Run govML quality loop on FINDINGS.md | Score ≥ 8.0 |

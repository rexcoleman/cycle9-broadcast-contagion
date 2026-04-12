# T3 Ensemble Scores — Cycle 9: Broadcast Contagion Phase Transitions

> **Scored:** 2026-04-12
> **Protocol:** T3 ensemble (5 Sonnet scoring passes + Opus meta-review)
> **Artifact:** `~/cycle9-broadcast-contagion/FINDINGS.md`
> **Session:** S79

---

## Final Composite: 6.80

```
composite = (PS × 0.30) + (N × 0.20) + (BS × 0.20) + (R × 0.10) + (G × 0.10) + (C × 0.10)
          = (7 × 0.30) + (7 × 0.20) + (6 × 0.20) + (7 × 0.10) + (6 × 0.10) + (8 × 0.10)
          = 2.10 + 1.40 + 1.20 + 0.70 + 0.60 + 0.80
          = 6.80
```

---

## Per-Dimension Scores

| Dimension | Pass 1 | Pass 2 | Pass 3 | Pass 4 | Pass 5 | Median | Spread | Confidence | Final |
|-----------|--------|--------|--------|--------|--------|--------|--------|------------|-------|
| Problem Selection | 7 | 7 | 8 | 8 | 7 | 7 | 1 | HIGH | **7** |
| Novelty | 7 | 7 | 7 | 7 | 6 | 7 | 1 | HIGH | **7** |
| Boundary-Spanning | 6 | 5 | 7 | 7 | 6 | 6 | 2 | MEDIUM | **6** |
| Rigor | 7 | 8 | 8 | 7 | 7 | 7 | 1 | HIGH | **7** |
| Generalizability | 6 | 7 | 7 | 6 | 6 | 6 | 1 | HIGH | **6** |
| Clarity | 7 | 8 | 8 | 8 | 7 | 8 | 1 | HIGH | **8** |
| **Surprise** (diag.) | 7 | 8 | 7 | 8 | 8 | **8** | 1 | HIGH | **8** |
| **Fertility** (diag.) | 7 | 7 | 7 | 8 | 7 | **7** | 1 | HIGH | **7** |

---

## Per-Dimension Confidence

- **HIGH (spread ≤ 1.0):** Problem Selection, Novelty, Rigor, Generalizability, Clarity, Surprise, Fertility — 7 of 8 dimensions
- **MEDIUM (spread 1.1-2.0):** Boundary-Spanning (spread = 2, scores 5-7)
- **LOW (spread > 2.0):** None

No adjudication overrides required (no LOW confidence dimensions).

---

## Boundary-Spanning Disagreement (MEDIUM confidence)

The widest disagreement is on Boundary-Spanning (scores 5-7, spread = 2):

- **Pass 2 (score 5):** Strict rubric reading — "network epidemiology and percolation theory are the same academic community — not genuinely distinct domains." No transfer test executed. Places this in Adequate (4-6) per rubric language.
- **Passes 3, 4 (score 7):** Credit the ISS-to-supply-chain mechanism adaptation as an executed transfer with measured outcome (|Δp_c| = 0.15). The 2.04× vs ~4.3× result requires bridging three frameworks.
- **Median of 6** is defensible: the ISS adaptation produced a measured outcome (more than analogy) but cross-domain transfer tests to biology/misinformation/wildfire were claimed but not executed (less than Strong tier).

---

## Ensemble Diagnostics

**Agreement pattern:** Strong convergence. All 5 passes identify the same strengths (H-2 refutation, pre-registration, claim tagging, decision matrix) and same weaknesses (hub-originated restriction, no executed transfer tests, Shai-Hulud quasi-validation circularity, narrow literature search). No fundamentally different readings of the artifact.

**Strongest consensus:** Novelty (4 passes at 7, 1 at 6). All agree H-2 refutation is the primary novelty contribution and methodology is standard. Pass 5's lower score (6) is attributable to compressed input content (see data quality note below).

**Weakest consensus:** Boundary-Spanning (spread = 2). Genuine interpretive ambiguity: is adapting a rumor-spreading model to malware propagation "boundary spanning" or "standard domain application"?

**Outlier passes:**
- **Pass 5 (composite 6.50, lowest):** Received compressed FINDINGS.md — explicitly noted missing sections (decision matrix, sensitivity table, novelty assessment text). Lower scores on Novelty (6), Boundary-Spanning (6), Clarity (7) are consistent with content not being visible. Content-independent dimensions (Surprise: 8, Rigor: 7) align with ensemble.
- **Pass 3 (composite 7.50, highest):** Scored PS=8, BS=7, R=8. Evidence basis was substantive but did not cite stronger evidence than other passes for the higher scores.

**Ensemble adds value:** Yes. (1) Confirmed artifact profile is unambiguous. (2) Boundary-Spanning disagreement exposed genuine interpretive question. (3) Pass 5 degradation showed which dimensions are content-dependent vs structurally assessable.

---

## Pass Composites

| Pass | Composite |
|------|-----------|
| Pass 1 | 6.70 |
| Pass 2 | 6.80 |
| Pass 3 | 7.50 |
| Pass 4 | 7.30 |
| Pass 5 | 6.50 |
| **Composite spread** | **1.00** |

---

## T3 vs Single Verifier Comparison

| Dimension | T3 Final | Single Verifier | Delta | Note |
|-----------|----------|----------------|-------|------|
| Problem Selection | 7 | 7 | 0 | Agreement |
| Novelty | 7 | 6 | +1 | Verifier more conservative; T3 consensus credits H-2 refutation mechanism |
| Boundary-Spanning | 6 | 6 | 0 | Agreement |
| Rigor | 7 | 6 | +1 | Verifier flagged H-2 resolution error (CI bound issue) and noted all results from same simulation framework |
| Generalizability | 6 | 7 | -1 | Verifier more generous; may reflect handoff contamination inflating the evaluation |
| Clarity | 8 | 7 | +1 | T3 consensus credits decision matrix actionability more strongly |
| Surprise | 8 | 6 | +2 | Largest gap — Verifier characterized H-1/H-4 as unsurprising (which they are), but underweighted H-2 refutation magnitude |
| Fertility | 7 | 7 | 0 | Agreement |
| **Composite** | **6.80** | **6.50** | **+0.30** | T3 slightly higher |

**Contamination analysis:** The single Verifier read the Coach's handoff (containing evaluation findings) before scoring. The T3 composite (6.80) is 0.30 points higher than the single Verifier (6.50). This is within the ±0.5 T3 confidence band and does NOT follow the expected contamination pattern (contamination typically inflates, not deflates scores). The Verifier's lower scores on Novelty, Rigor, and Clarity may reflect either: (1) more conservative reading, (2) specific technical critiques (e.g., H-2 resolution methodology), or (3) the Verifier's prompt enforcing stricter structural compliance checks. The +2 gap on Surprise is the most notable: the Verifier correctly identified that H-1 and H-4 are unsurprising but appears to have underweighted the H-2 refutation, which all 5 T3 passes scored 7-8.

---

## Portfolio Context

| Project | T3 Composite | Contamination | Domain |
|---------|-------------|---------------|--------|
| controllability-bound | 7.0 | Uncontaminated | ML/Security |
| memory-poisoning-persistence | 6.9 | CONTAMINATED | ML/Security |
| **Cycle 9: Broadcast Contagion** | **6.80** | **Uncontaminated** | Supply Chain/Network Science |
| B.3 biology (templates-only) | 6.0 | Uncontaminated | Biology |

Cycle 9 scores 6.80, placing it within the governed project range (6.0-7.0) and 0.20 below the portfolio leader (controllability-bound at 7.0). Given the ±0.5 T3 confidence band, Cycle 9 is statistically indistinguishable from the top two projects.

---

## Key Weaknesses Identified Across Passes

All 5 passes converged on these weaknesses:

1. **Hub-originated attack restriction** — All p_c values are conditional on top-1% hub seeds. Random-origin attack generalization untested. Limits both Problem Selection and Generalizability.
2. **No executed transfer tests** — Cross-domain claims (biology, misinformation, wildfire) stated as analogies. Domain-agnostic principle not tested outside supply chain. Caps Boundary-Spanning at 6.
3. **Shai-Hulud quasi-validation circularity** — Coverage estimate (~0.28) reverse-engineered from outcome, not independently measured. Weakens empirical grounding claim.
4. **Narrow literature search** — 6 prior works in Novelty Assessment, no documented systematic search of supply chain security literature (Zimmermann, Ohm, etc.). "First measurement" claim unverified.
5. **Simulation code external** — Artifact not self-contained for reproduction. α calibration procedure underdescribed.

---

## Session Consumption

- Sonnet agent runs: 5 (parallel scoring passes)
- Opus agent runs: 1 (meta-review)
- Files read: 5 (dispatch, FINDINGS.md ×2 parts, t3_sonnet_scoring_prompt.md, t3_opus_meta_review_prompt.md) + calibration data
- Commands run: 2 (sqlite3 query, VERIFICATION.md check)

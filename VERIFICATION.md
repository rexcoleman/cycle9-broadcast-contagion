# Verification Report: Broadcast Contagion Phase Transitions in Software Supply Chain Networks

**Verifier:** research-verifier (Builder session executing dispatch)
**Artifact verified:** ~/cycle9-broadcast-contagion/FINDINGS.md (380 lines)
**Date:** 2026-04-12
**Verification independence:** Artifact-only evaluation. No access to execution logs, process notes, researcher self-assessment, or prior verification results. Contamination note: Builder read handoff.md during warmup which contained Coach evaluation findings — all dimension scores and findings below are grounded in artifact line numbers and source files only, not handoff content.

---

## Structural Compliance

| # | Check | Status | Evidence |
|---|---|---|---|
| S1 | All sections per FINDINGS template present | PASS | 22 `##` sections present including all template-required: Executive Summary, Hostile Baseline Check, Key Findings, Hypothesis Resolutions, Novelty Assessment, Practitioner Impact, Cross-Domain Connections, Generalization Analysis, Limitations to Next Questions, Primary Contribution, Breakthrough Question, Methodology, Parameter Sensitivity, Raw Source Notes. Additional sections: Experiment Completeness Declaration, Negative/Unexpected Results, Depth Commitment, Mechanism Analysis, Formal Contribution Statement, Published Baseline, Defense Harm Test, Sanity Results, Detection Methodology Discussion. |
| S2 | 100% claims tagged | CONDITIONAL | 22 claim tags total (12 DEMONSTRATED, 10 SUGGESTED, 1 HYPOTHESIZED) via `grep -c`. Spot-check found 2-3 untagged factual assertions: (1) Line 157: "policies that rely on Cohen et al.'s static immunization fractions...will *underestimate* the required coverage by a factor of ~2" — untagged [SUGGESTED] policy claim. (2) Line 153: "the theoretical targeting advantage...does not fully transfer" — untagged interpretive claim. (3) Line 282: "monitoring 20% of packages...achieves the same containment as monitoring 40% uniformly" — untagged in Breakthrough Question. |
| S3 | No prohibited language | PASS | Searched for: "proves," "clearly shows," "obviously," "it is well known," "undeniably." Zero matches. |
| S4 | Depth budget met | FAIL | 2 unique direct quoted passages with source attribution in Key Findings + Novelty Assessment: (1) P-S&V: "the epidemic threshold of the SIS model vanishes in scale-free networks" (lines 59, 169). (2) Yang et al.: "large epidemic thresholds emerge in heterogeneous networks of heterogeneous nodes" (lines 59, 173). One term-level quote: "acquaintance immunization" (line 65, 2 words). Line 314 claims "depth budget of >=8 quoted passages is met" but conflates source engagement (7 sources) with direct quoted passages (2-3). |
| S5 | Executive Summary uses DEMONSTRATED/SUGGESTED only | PASS | Line 19 contains 2x [DEMONSTRATED], 0x [PROJECTED] or [HYPOTHESIZED]. The single [HYPOTHESIZED] is at line 95 (Finding 7), outside the Executive Summary. |
| S6 | Hypothesis resolutions match HYPOTHESIS_REGISTRY | FAIL (H-2) | H-1 FINDINGS="SUPPORTED with qualification" (line 105) = HR §4 "SUPPORTED (with qualification)" — MATCH. H-3 FINDINGS="PARTIALLY SUPPORTED" (line 127) = HR §4 — MATCH. H-4 FINDINGS="SUPPORTED" (line 141) = HR §4 — MATCH. **H-2: FINDINGS line 117 = "REFUTED." HR §4 line 54 = "REFUTED." Labels match between files. BUT: HR §2 line 31 REFUTED criterion: "upper bound of CI on ratio < 2.0." FINDINGS line 119: CI = [1.95, 2.15]. Upper bound 2.15 > 2.0. REFUTED criterion NOT met. SUPPORTED criterion (CI lower >= 3.0) also not met (1.95 << 3.0). Honest resolution by pre-registered criteria: INCONCLUSIVE.** |
| S7 | Claim Strength Legend present | FAIL | No legend in FINDINGS.md. No CLAIM_STRENGTH_SPEC.md file in project directory. Tags (DEMONSTRATED, SUGGESTED, HYPOTHESIZED) used without definitions. |

**Summary:** 3 PASS, 1 CONDITIONAL, 3 FAIL.

---

## Dimension Scores

| Dimension | Score | Weight | Weighted | Qualifier | Key Evidence | Key Weakness |
|-----------|-------|--------|----------|-----------|-------------|-------------|
| Problem Selection | 7 | 0.30 | 2.10 | — | Line 55: "first quantitative measurement of a detection-coverage-driven phase transition." RQS §0a Lakatos test: PARTIALLY PREDICTABLE. Specific p_c values (0.19-0.48) answer a previously unmeasured quantity. | Threshold existence predicted by SIS+recovery theory (P-S&V + Yang et al.). Direction guessable by network epidemiologist. Only magnitude was unknown. |
| Novelty | 6 | 0.20 | 1.20 | PROMPT_ENFORCED | Lines 169-174: differentiation from 6 prior works. H-4 SUPPORTED (line 141): mechanism adaptation produces |Δp_c|=0.15, confirming adaptation is substantive. Three domain-specific modifications documented in RQS §2 Import Depth Verification. | Framework (compartmental contagion + recovery → phase transition) is well-established in network epidemiology. No new mathematical technique. All 6 prior works in Novelty table are from the same broad network epidemiology family. |
| Boundary-Spanning | 6 | 0.20 | 1.20 | PROMPT_ENFORCED | Lines 196-209: domain-agnostic principle identified with 3 transfer domains and 3 failure conditions. RQS Import Depth Verification: genuine ISS framework understanding with 3 substantive adaptations validated by H-4. | Source/target domains share mathematical vocabulary (contagion on networks). "Where this transfers" (lines 201-203) lists 3 domains without citations or evidence of actual transfer. Speculative bridges, not demonstrated ones. |
| Rigor | 6 | 0.10 | 0.60 | — | 45,900 MC runs (line 19), bootstrap CIs, Bonferroni α=0.004 (EP §2), 3 quality gates (lines 346-354), ablations A2-A4 (lines 85-89), parameter sensitivity table (lines 328-338). H-2 REFUTED and H-3 PARTIALLY SUPPORTED reported. | H-2 resolution error: REFUTED stated when pre-registered criterion NOT met (CI upper 2.15 > 2.0 threshold). Depth budget over-claim at line 314. No external validation — all results from same simulation framework. |
| Generalizability | 7 | 0.10 | 0.70 | PROMPT_ENFORCED | Lines 212-231: evaluation conditions table with 6 conditions across 2 topologies, 3 sizes, 2 strategies. 8 data rows. Failure modes quantified: sharpness <0.15 at BA uniform N≤5K (line 224), size instability 0.128>0.10 between 1K-10K (line 225). Gate: 5/5 PASS. | All topologies scale-free (γ≈2.5-3.0). No Erdős-Rényi, small-world, or real-world dependency graph tested. Only hub-originated attack seeds. One detection model (degree-correlated log scaling). |
| Clarity | 7 | 0.10 | 0.70 | PROMPT_ENFORCED | Lines 184-188: Detection Coverage Decision Matrix with per-condition p_c values. Line 190: specific actionable recommendation (20% hub-targeted coverage). Line 276: Primary Contribution in 2 sentences with all key numbers. | Decision matrix 80%/95% columns use ~values without CIs (lines 186-188). Detection Methodology Discussion (line 358) names 4 abstraction gaps limiting practitioner applicability. |
| Surprise | 6 | — | (emergent, 0.5×) | PROMPT_ENFORCED | H-2 result: 2.04× vs predicted ~4.3× (line 65). Dynamic-to-static erosion of ~50% quantified. Unexpected that detection latency erodes roughly half of Cohen et al.'s static targeting advantage. | H-1 (threshold exists) not surprising — theoretically predicted. H-4 (adaptation matters) confirms study design, not a deep surprise. |
| Fertility | 7 | — | (emergent, 0.5×) | PROMPT_ENFORCED | Lines 234-271: 6 specific next questions covering temporal topology, cascade distribution, detection heterogeneity, community structure, allocation optimization, adaptive adversary. Breakthrough Question (line 282) frames policy shift. | Next questions are standard network science extensions. No deeply novel research directions opened beyond the immediate parameter space. |

**Composite (6 governable dimensions):** (7×0.30) + (6×0.20) + (6×0.20) + (6×0.10) + (7×0.10) + (7×0.10) = **6.50**

---

## Generalization Gate Cross-Check

```
$ cd ~/cycle9-broadcast-contagion && bash ~/ml-governance-templates/scripts/check_all_gates.sh . 2>&1 | grep -i generalization
  PASS: D2 §8c Generalization Plan found
  PASS: 'Generalization Analysis' section found
  PASS: Generalization has evaluation conditions table (9 table rows)
  PASS: Generalization table has >=2 data rows (8 non-separator rows)
  PASS: Generalization has quantified failure modes (3 threshold patterns)
```

**5/5 sub-checks PASS.** G=7 is consistent with the gate PASS. The gate confirms structural elements (table exists, data rows present, failure modes quantified). G=7 reflects substantive content quality: 6 conditions, 2 topologies, 3 sizes, failure modes triggered and honestly reported. No discrepancy between gate result and G score.

---

## DEV-1 Scope Restriction Verification

**Executive Summary (line 19):** "All results are conditional on hub-originated attacks (top-1% packages by dependency count)." **PASS.**

**Primary Contribution (line 276):** "on hub-originated attacks" — **PASS.**

**Practitioner Impact header (line 182):** "For hub-originated broadcast attacks" — **PASS.**

### Key Findings — Detailed Check

| Finding | Line | Tag | Scope Stated? | Verdict |
|---------|------|-----|---------------|---------|
| F1 | 55 | DEMONSTRATED | Yes — "hub-originated attacks" | PASS |
| F2 | 63 | DEMONSTRATED | No | FAIL |
| F2 | 65 | SUGGESTED | No | FAIL |
| F3 | 69 | DEMONSTRATED | No | FAIL |
| F3 | 71 | SUGGESTED | No | FAIL |
| F4 | 75 | DEMONSTRATED | No | FAIL |
| F4 | 77 | SUGGESTED | No | FAIL |
| F5 | 81 | DEMONSTRATED | No | FAIL |
| F5 | 83 | SUGGESTED | No | FAIL |
| F6a | 87 | DEMONSTRATED | No | FAIL |
| F6b | 89 | DEMONSTRATED + SUGGESTED | No | FAIL |
| F7 | 93 | SUGGESTED | No | FAIL |
| F7 | 95 | HYPOTHESIZED | No | FAIL |

**Result:** 1/13 Key Findings claims include DEV-1 scope. 12/13 omit it. Systematic over-generalization: a reader citing any individual finding except F1 without also reading the Executive Summary would not know these apply only to hub-originated attacks.

---

## Independent Verification Findings

### Finding 1: H-2 Resolution Contradicts Pre-Registered Criteria

HYPOTHESIS_REGISTRY.md §2 line 31 states H-2 REFUTED threshold: "upper bound of CI on ratio < 2.0."
FINDINGS.md line 119 reports CI: [1.95, 2.15]. Upper bound = 2.15. 2.15 > 2.0.

The REFUTED criterion is NOT met. The SUPPORTED criterion ("lower bound of CI >= 3.0") is also not met (1.95 << 3.0). Data falls between thresholds. The honest resolution is INCONCLUSIVE.

Both FINDINGS.md (line 117) and HYPOTHESIS_REGISTRY.md §4 (line 54) carry "REFUTED." Both files contain the same error. The H-2 narrative (detection latency erodes hub-targeting advantage) is substantively correct, but the resolution label violates the pre-registered protocol.

### Finding 2: Depth Budget Over-Claim

FINDINGS.md line 314 claims "The depth budget of ≥8 quoted passages is met." Actual count: 2 unique direct quoted passages (P-S&V vanishing threshold, Yang et al. paper title). The claim conflates "source engagement" (paraphrasing 7 sources with citations) with "direct quoted passages" (text in quotation marks attributed to a specific source). The remaining 5 cited sources are paraphrased, not quoted.

### Finding 3: Systematic DEV-1 Scope Omission

12/13 tagged claims in Key Findings omit the hub-originated scope restriction. See DEV-1 Scope Restriction Verification section above for full details. The Executive Summary and Primary Contribution carry the restriction, but the individual findings — the citable units — do not.

### Finding 4: Paraphrases Presented as Direct Quotes

(a) P-S&V quote at lines 29, 59, 169: "the epidemic threshold of the SIS model vanishes in scale-free networks" is in quotation marks. The actual paper abstract (PRL 86:3200, confirmed via WebSearch) uses "the absence of an epidemic threshold" — equivalent meaning, different wording. Quotation marks imply verbatim text.

(b) Yang et al. quote at lines 59, 173: "large epidemic thresholds emerge in heterogeneous networks of heterogeneous nodes" is the paper's TITLE (Scientific Reports 5:13122, confirmed via WebSearch), not a finding from within the paper body. Presenting a title as a quoted finding is misleading.

### Finding 5: Static Targeting Ratio Imprecision

FINDINGS line 65: "static percolation prediction of ~4.3×." EXECUTION_PROTOCOL.md line 91: pc_uniform=0.9424, pc_targeted=0.2333, ratio = 4.04. The "~4.3×" claim inflates the actual ratio by ~6%. This affects the "53% erosion" claim: actual erosion is 1 - (2.04/4.04) = 49.5%, not the implied ~53%. Minor but compounds with the H-2 resolution issue.

---

## Claim Spot-Checks

| Claim | Researcher Tag | Verified Tag | Source Check | Notes |
|-------|---------------|-------------|-------------|-------|
| P-S&V 2001: vanishing SIS threshold on scale-free networks (line 59) | [DEMONSTRATED] context | CONFIRMED | PRL 86(14):3200-3203 verified. Paper finds "absence of an epidemic threshold." Journal, volume, page correct. | Paraphrase in quotation marks, not verbatim quote. Meaning equivalent. |
| Cohen et al. 2003: acquaintance immunization, ~4.3× static advantage (line 65) | [SUGGESTED] | CONFIRMED with caveat | PRL 91:247901 verified. Paper presents acquaintance immunization and critical threshold analysis. | "~4.3×" imprecise: actual from EP baselines is 4.04 (~6% inflation). |
| Yang et al. 2015: threshold restoration with heterogeneous recovery (line 59) | [DEMONSTRATED] context | CONFIRMED | Scientific Reports 5:13122 verified. Paper confirms heterogeneous node properties create resilience to disease spreading. | "Quoted" text is paper title, not a finding from paper body. |

---

## Overall Assessment

**Gate verdict:** PASS

**Justification:** Independent assessment achieved through 5 findings the researcher did not report: (1) H-2 resolution contradicts pre-registered REFUTED criteria (CI upper 2.15 > 2.0 threshold), (2) depth budget over-claim (2-3 quotes, not ≥8), (3) systematic DEV-1 scope omission in 12/13 Key Findings claims, (4) paraphrases presented as direct quotes for 2 of 3 cited sources, (5) static targeting ratio inflated ~6% (4.04 actual vs ~4.3 claimed).

**Strongest aspect:** Statistical methodology is thorough — 45,900 MC runs with bootstrap CIs, Bonferroni correction, 3 validated quality gates, systematic ablations across mechanism type, graph directedness, and cascading detection. The Generalization Analysis (8 data rows, quantified failure modes, honest reporting of sharpness < 0.15 and size instability) is substantive. The 2× hub-targeting negative result is a genuinely useful practitioner finding.

**Biggest gap:** H-2 resolution error — REFUTED stated when the pre-registered criterion is not met (CI upper 2.15 > 2.0). This is a hypothesis resolution that violates the pre-registered protocol. The correct label is INCONCLUSIVE. Combined with the systematic DEV-1 scope omission (12/13 findings), these two issues affect R and the credibility of the claim tagging system.

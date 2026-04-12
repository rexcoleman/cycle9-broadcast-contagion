# Findings — {{PROJECT_NAME}}

<!-- version: 1.0 -->
<!-- created: 2026-03-18 -->

> **Lock status:** This document is MUTABLE until project completion. After final experiments, claim tags become immutable.
> **Authority:** CLAIM_STRENGTH_SPEC.tmpl.md governs claim tag usage. EXPERIMENT_CONTRACT.md governs experimental scope.

> **Authority Hierarchy**
>
> | Priority | Document | Role |
> |----------|----------|------|
> | Tier 1 | `{{TIER1_DOC}}` | Primary spec — highest authority |
> | Tier 2 | `{{TIER2_DOC}}` | Clarifications — cannot override Tier 1 |
> | Tier 3 | `{{TIER3_DOC}}` | Advisory only — non-binding if inconsistent with Tier 1/2 |
> | Contract | This document | Implementation detail — subordinate to all tiers above |
>
> **Conflict rule:** When a higher-tier document and this contract disagree, the higher tier wins.
> Update this contract via `CONTRACT_CHANGE` or align implementation to the higher tier.

### Companion Contracts

**Upstream (this contract depends on):**
- See [CLAIM_STRENGTH_SPEC](CLAIM_STRENGTH_SPEC.tmpl.md) for claim tag taxonomy, qualifiers, and prohibited language
- See [HYPOTHESIS_REGISTRY](HYPOTHESIS_REGISTRY.tmpl.md) for hypothesis IDs referenced in resolutions
- See [EXPERIMENT_CONTRACT](EXPERIMENT_CONTRACT.tmpl.md) for experimental scope and metrics definitions
- See [STATISTICAL_ANALYSIS_SPEC](STATISTICAL_ANALYSIS_SPEC.tmpl.md) for CI computation methods

**Downstream (depends on this contract):**
- See [CONTENT_PLAN](../publishing/CONTENT_PLAN.tmpl.md) for blog hooks and content pipeline
- See [PUBLICATION_PIPELINE](../publishing/PUBLICATION_PIPELINE.tmpl.md) for publication approval gating

## Customization Guide

| Placeholder | Description | Example |
|-------------|-------------|---------|
| `{{PROJECT_NAME}}` | Project name | Adversarial IDS |
| `{{DATA_TYPE}}` | Primary data type (real, synthetic, mixed) | synthetic |
| `{{MIN_SEEDS}}` | Minimum seeds for DEMONSTRATED | 3 |
| `{{OUTPUTS_DIR}}` | Path to raw outputs | outputs/ |
| `{{FIGURES_DIR}}` | Path to generated figures | figures/ |
| `{{TIER1_DOC}}` | Tier 1 authority document | Project requirements spec |
| `{{TIER2_DOC}}` | Tier 2 authority document | FAQ or clarifications document |
| `{{TIER3_DOC}}` | Tier 3 authority document | Advisory references |

---

## Claim Strength Legend

> Copied from CLAIM_STRENGTH_SPEC §1. This legend MUST appear in every instantiated FINDINGS.md.

| Tag | Meaning | Required Evidence |
|-----|---------|-------------------|
| [DEMONSTRATED] | Directly measured, reproducible | ≥{{MIN_SEEDS}} seeds, CI reported, raw data matches claim |
| [SUGGESTED] | Consistent pattern, limited evidence | 1-2 seeds, or qualitative pattern across domains |
| [PROJECTED] | Extrapolated from partial evidence | Trend line, analogical reasoning, or partial measurement |
| [HYPOTHESIZED] | Untested prediction | Stated as future work, logical but unmeasured |

**Qualifiers:** SYNTHETIC | SINGLE-SEED | NOISE-ONLY | SCOPED (stack with commas inside brackets)

**Data type:** {{DATA_TYPE}}
**Seeds:** {{MIN_SEEDS}}+
**Claim tagging:** Per CLAIM_STRENGTH_SPEC v1.0

---

## Executive Summary

{{2-3 sentence summary of the most important findings. Lead with the single strongest result.}}

> **Constraint (CLAIM_STRENGTH_SPEC §5.3):** This section may contain only [DEMONSTRATED] and [SUGGESTED] claims. No [PROJECTED] or [HYPOTHESIZED] claims permitted here.

---

## Hostile Baseline Check

<!-- REQUIREMENT: hostile self-reproduction before writing findings -->
> Before writing Key Findings, test whether a trivially simple method (mean predictor, majority class, linear model, nearest-neighbor, or the most obvious heuristic) achieves comparable performance to your primary result. If the simple method is within 10% of your primary result on the primary metric, your contribution may be incremental — reconsider before proceeding.
> This check prevents publishing results that collapse under scrutiny.
<!-- /REQUIREMENT -->

<!-- INSTANCE: fill per project -->
| Simple Method | Primary Metric | Your Result | Simple Result | Gap | Verdict |
|---|---|---|---|---|---|
| {{e.g., mean predictor}} | {{e.g., R²}} | {{your score}} | {{simple score}} | {{delta}} | {{SURVIVES: gap > 10% / AT RISK: gap ≤ 10%}} |

**Interpretation:** {{If your method survives, state why the gap is meaningful. If at risk, explain what your method adds beyond the simple baseline (e.g., cross-domain generalization, interpretability, formal guarantees).}}
<!-- /INSTANCE -->

---

## Experiment Completeness Declaration

<!-- REQUIREMENT: selective reporting prevention -->
> State how many total experiments were run vs how many are reported below. If experiments were excluded, state why (e.g., "ran 12 experiments, reporting 8; 4 excluded because they tested an abandoned approach before the design was locked"). This closes the selective reporting gap identified in empirical ML research methodology critiques.
<!-- /REQUIREMENT -->

<!-- INSTANCE: fill per project -->
**Experiments run:** {{total count}}
**Experiments reported:** {{count reported below}}
**Excluded:** {{count excluded}} — {{reason for exclusion, or "none"}}

> **Phrasing note:** Use the exact field names above ("Experiments run:", "Experiments reported:", "Excluded:"). The semantic review gate (G24) validates this section by matching these phrases. Rewording (e.g., "Total experiments conducted:") may trigger a false FAIL.
<!-- /INSTANCE -->

---

## Key Findings

### Finding 1: {{Title — state as a claim}}

**Claim tag:** [DEMONSTRATED] | [SUGGESTED] | [PROJECTED] | [HYPOTHESIZED]
**Phase:** CONFIRMATORY (pre-registered in HYPOTHESIS_REGISTRY) | EXPLORATORY (discovered during analysis)
**Qualifiers:** {{SYNTHETIC | SINGLE-SEED | SCOPED | none}}
**Evidence:** {{Link to specific output artifact: outputs/results.json, figures/chart.png}}
**Metric:** {{Specific number with units and comparison baseline}}
**Hypothesis link:** {{H-X from HYPOTHESIS_REGISTRY.md, or "exploratory — not pre-registered"}}

{{2-4 sentences describing the finding, its significance, and limitations.}}

### Finding 2: {{Title}}

**Claim tag:**
**Phase:** CONFIRMATORY | EXPLORATORY
**Qualifiers:**
**Evidence:**
**Metric:**
**Hypothesis link:**

{{2-4 sentences describing the finding, its significance, and limitations.}}

### Finding 3: {{Title}}

**Claim tag:**
**Phase:** CONFIRMATORY | EXPLORATORY
**Qualifiers:**
**Evidence:**
**Metric:**
**Hypothesis link:**

{{2-4 sentences describing the finding, its significance, and limitations.}}

### Effect Persistence Check

<!-- source: Track 1, Milkman (45% significant during intervention, 8% post-intervention — this separation was the most policy-relevant finding), Chetty (childhood exposure effects measured at age 26+ — decades after exposure period) -->
<!-- gate: -->

<!-- REQUIREMENT: temporal effect separation -->
> For each finding above, separate the effect DURING your intervention /
> measurement period from the effect AFTER it ends. If you only measured
> during the active period, state this explicitly as a limitation.
>
> This distinction matters because temporary effects and persistent effects
> have fundamentally different implications. Milkman's megastudy found 45%
> of interventions significant during the 4-week program but only 8% after.
> Without this separation, 45% would have been reported as "effective" —
> misleading for anyone designing policy based on the findings.
>
> **Applies to:** Any research where the intervention, measurement, or
> analytical window has a defined start and end. Computational research:
> does your model's advantage persist on out-of-distribution data or only
> on the training distribution? Observational research: does the effect
> persist across cohorts or time periods? Experimental research: does the
> effect persist after the intervention ends?
<!-- /REQUIREMENT -->

<!-- INSTANCE: fill per project -->

| Finding | Effect during active period | Effect after active period | Persistence ratio | Implication |
|---|---|---|---|---|
| Finding 1 | {{effect size + significance}} | {{effect size + significance, or "not measured — state why"}} | {{post/during ratio, or "N/A"}} | {{what this means for the finding's practical value}} |
| Finding 2 | {{effect size}} | {{effect size or "not measured"}} | {{ratio or "N/A"}} | {{implication}} |

> [SEED: persistence_measurement options: measured_both (strongest),
> measured_during_only (state as limitation), measured_after_only (rare),
> not_applicable (e.g., one-time measurement — explain why temporal
> separation doesn't apply)]
>
> **If "not measured":** This is not a flaw to hide — it's a scope boundary
> to state. "We measured during-treatment effects only; persistence is
> unknown" is honest. "We measured effects" without specifying the window
> is ambiguous.

**Self-test:** If your finding's effect disappears after the active period,
does the finding still matter? If yes, why? If no, your finding may be
overstated. Milkman's honest separation (8% post) made the paper STRONGER,
not weaker — it became about methodology, not just results.
<!-- /INSTANCE -->

---

## Hypothesis Resolutions

| Hypothesis | Prediction | Result | Verdict | Evidence |
|-----------|-----------|--------|---------|----------|
| H-1 | {{predicted ordering/outcome}} | {{actual result}} | SUPPORTED / PARTIALLY SUPPORTED / REFUTED / INCONCLUSIVE | {{artifact link}} |
| H-2 | | | | |

> **Resolution rules (HYPOTHESIS_REGISTRY §4):** Every hypothesis MUST be resolved. INCONCLUSIVE verdicts MUST include an explanation. Resolutions are final once committed.
>
> **PENDING is not a valid final status (A14).** At project close, every hypothesis must be SUPPORTED, PARTIALLY SUPPORTED, REFUTED, or INCONCLUSIVE (with explanation). If a hypothesis cannot be tested within the project scope, resolve as INCONCLUSIVE with: (a) why it could not be tested, (b) what specific conditions would enable future testing. check_all_gates.sh will FAIL on PENDING hypotheses at project close.

---

## Negative / Unexpected Results

> **LL-77 guidance:** Negative results deserve more analytical space than positive ones. A refuted hypothesis generates more insight than a confirmed one.

### {{Unexpected Finding Title}}

**What was expected:** {{prediction}}
**What happened:** {{actual result}}
**Why this matters:** {{insight gained from the surprise}}
**Implication:** {{what this changes about the approach/understanding}}

---

## Limitations

<!-- REQUIREMENT: transparent limitations disclosure (A7) -->
> Limitations disclosure quality is scored as a sub-criterion of rigor (limitations_disclosure).
> Each limitation must name: (a) what constraint exists, (b) why it matters for the findings, and (c) what would be needed to address it.
> Honest, specific limitations with quantified boundaries score higher than vague or minimal disclosures. Venues reward transparency — this section strengthens the paper, not weakens it.
>
> **CLAIM_STRENGTH_SPEC §5.5:** All [HYPOTHESIZED] claims MUST appear in this section. All qualifiers (SYNTHETIC, SCOPED, etc.) MUST be summarized here.
<!-- /REQUIREMENT -->

<!-- INSTANCE: fill per project -->
1. {{Limitation 1: constraint + why it matters + what would address it}}
2. {{Limitation 2}}
3. {{Limitation 3}}
<!-- /INSTANCE -->

### Limitations to Next Questions

<!-- source: Phase I Gap Research (G4), Finding 6 — research program continuity mechanism -->
<!-- gate:findings limitations_to_next_questions entries:3 -->

For each limitation above, propose a specific research question that would address it.
These feed the `limitations_next_questions` table — the pipeline's own research frontiers.

| # | Limitation (from above) | Suggested next question | Priority |
|---|---|---|---|
| 1 | {{LIMITATION_1}} | {{NEXT_QUESTION}} | {{HIGH/MEDIUM/LOW}} |
| 2 | {{LIMITATION_2}} | {{NEXT_QUESTION}} | {{HIGH/MEDIUM/LOW}} |
| 3 | {{LIMITATION_3}} | {{NEXT_QUESTION}} | {{HIGH/MEDIUM/LOW}} |

<!-- /gate:findings limitations_to_next_questions -->

> [SEED: min_limitation_question_pairs=3]
> These are NOT "future work" hand-waves — they are inputs to the next cycle's
> Stage 0 observation. The RP queries this table at Stage 0 §1.1.

### Boundary Statement

<!-- source: Track 1, Chetty ("The descriptive analysis does not identify the causal mechanisms"), Bell ("remaining loopholes not logically excluded"), AlphaFold ("intrinsically disordered proteins not addressed") — 4/7 papers explicitly stated what their analysis DOES NOT show -->
<!-- gate: -->

<!-- REQUIREMENT: explicit claim-scope boundaries -->
> Limitations describe what constrains your analysis. Boundary statements
> describe what your analysis DOES NOT PROVE — even if it is otherwise
> well-executed. These are different: Chetty's data and methods were
> excellent (few limitations in the traditional sense), but he explicitly
> stated the analysis "does not identify the causal mechanisms that
> determine upward mobility." That's not a limitation — it's a scope
> boundary on what the evidence supports.
>
> 4/7 breakthrough papers included explicit boundary statements. The papers
> that didn't (GNoME) faced post-publication criticism partly because
> readers inferred broader claims than intended.
<!-- /REQUIREMENT -->

<!-- INSTANCE: fill per project -->
**State 3 things this analysis DOES NOT show:**

1. This analysis does not {{identify / prove / establish / demonstrate}} {{specific mechanism / relationship / generalization}} because {{specific reason — not "more work needed" but WHY the evidence doesn't support this claim}}.
2. This analysis does not {{...}} because {{...}}.
3. This analysis does not {{...}} because {{...}}.

> [SEED: boundary_count=3; increase for broad-scope analyses, decrease
> to 2 for narrowly-scoped work with clear boundaries already in the
> research question]
>
> **Distinguish from Limitations above:** Limitations are constraints on
> your work (small sample, synthetic data, single domain). Boundaries are
> claims your evidence doesn't support even if the work were unconstrained.
> Chetty with infinite data STILL couldn't identify causal mechanisms from
> descriptive analysis — that's a boundary, not a limitation.

**Self-test:** Read your Executive Summary. For each claim, ask: "Does my
evidence actually support this, or am I implying more than I showed?" If
your boundary statements don't constrain at least one Executive Summary
claim, they may be too narrow.
<!-- /INSTANCE -->

---

## Pre-emptive Criticism Engagement

<!-- source: Track 1, GNoME (post-publication criticism: "2.2M materials" were mostly trivial variants — team didn't pre-empt this), Bell (preemptively discussed superdeterminism loophole), Chetty (preemptively bounded causal claims), Milkman (preemptively noted expert prediction failure and temporary effects) -->
<!-- gate: -->

<!-- REQUIREMENT: anticipate and engage with likely criticisms -->
> GNoME's "2.2M new materials" claim faced Chemistry of Materials criticism
> that most predictions were trivial variants of known structures. This
> criticism was foreseeable — and engaging it in the original paper would
> have been stronger than responding after publication. Bell preemptively
> discussed the superdeterminism loophole (acknowledging it's "not logically
> excluded" but explaining why it's "far-fetched"). Chetty preemptively
> bounded his causal claims.
>
> Pre-emptive criticism engagement is not defensive writing — it's
> intellectual honesty that strengthens the paper by demonstrating the
> authors considered the strongest objections.
<!-- /REQUIREMENT -->

<!-- INSTANCE: fill per project -->
**Name 3 criticisms a knowledgeable skeptic in your field would make:**

| # | Criticism | Finding holds despite this (a) OR genuine limitation (b)? | Evidence / explanation |
|---|---|---|---|
| 1 | {{specific criticism — e.g., "your metric doesn't capture X," "your sample is biased toward Y," "this is a trivial extension of Z"}} | (a) / (b) | {{If (a): state why with evidence. If (b): state what additional work would resolve it.}} |
| 2 | {{criticism}} | (a) / (b) | {{evidence / explanation}} |
| 3 | {{criticism}} | (a) / (b) | {{evidence / explanation}} |

> [SEED: criticism_count=3; for controversial or paradigm-challenging
> work, increase to 5]
>
> **Where to find criticisms:** (1) Reviewer comments on related papers in
> your venue. (2) Twitter/social media discussions of similar work. (3)
> Published critiques of the method you're using. (4) Your own doubts
> during execution. (5) The strongest argument for the OPPOSITE conclusion.
>
> **Scoring note:** A paper where all 3 criticisms are type (a) "finding
> holds" may be engaging too-weak criticisms. At least 1 should be type
> (b) "genuine limitation" — if your work has no genuine limitations
> visible to a knowledgeable skeptic, you haven't looked hard enough.

**Self-test:** Show your 3 criticisms to someone outside your immediate
team. If they immediately name a criticism you didn't list, your engagement
is incomplete. If they can't improve on your list, you've done the work.
<!-- /INSTANCE -->

---

## Claims on Synthetic Data

> **Required if `{{DATA_TYPE}}` = synthetic or mixed (CLAIM_STRENGTH_SPEC §5.6).** Delete this section only if `{{DATA_TYPE}}` = real.

All claims derived from synthetic data are listed below with the SYNTHETIC qualifier:

| Finding | Claim | Tag |
|---------|-------|-----|
| {{Finding N}} | {{claim text}} | [SUGGESTED, SYNTHETIC] |

**How synthetic data may differ from production data:** {{explicit statement}}

---

## Content Hooks (for downstream content pipeline)

> **R27 guidance:** These hooks feed into CONTENT_PLAN.tmpl.md for blog posts, TILs, and social content.

| Finding | Blog Hook (1 sentence) | TIL Title | Audience Side |
|---------|----------------------|-----------|---------------|
| Finding 1 | {{hook}} | {{title}} | OF AI / FROM AI / Both |
| Finding 2 | {{hook}} | {{title}} | |
| Negative result | {{hook}} | {{title}} | |

---

## Novelty Assessment

> [SEED: sunset after 5 projects if section never produces actionable insight | PT-5 governance overhead control]
> Target: 7/10. Requires: 5+ papers differentiated, surprise found, novel combination minimum, ablation of novel component.

**Prior art search:** {{Describe search methodology — databases queried, search terms, coverage}}
**Papers differentiated (min 5):** {{List papers from EXPERIMENTAL_DESIGN §8a with how findings differ}}
**Contribution type:** {{incremental improvement (caps at 5) / novel combination (6-7) / novel methodology (7-8) / new research direction (9-10)}}
**What surprised us:** {{Pre-registered expectation vs actual result — deviations ARE the novelty. If nothing surprised you, novelty is likely ≤5.}}

1. {{How finding 1 advances beyond prior work — cite specific papers differentiated against}}
2. {{How finding 2 is novel — or why it confirms prior work in a new context}}
3. {{Ablation evidence: what happens when novel component is removed? Reference EXPERIMENTAL_DESIGN §8a ablation table.}}

**Formal contribution** (conjecture, bound, or formal relationship — even informal):
> {{State the formal relationship your findings support. E.g., "Cascade containment is bounded by min-cut(capability partition graph)." Even if unproven, attempting formalization often reveals the mechanism. Novelty 8+ requires this.}}

---

## Practitioner Impact

> [SEED: sunset after 5 projects if section never produces a shipped artifact | PT-5]
> Target: 7/10. Requires: quantified audience, shipped artifact (not "planned"), ≥1 real-system validation, actionable recommendation.

**Problem magnitude:** {{How many practitioners/systems are affected? Quantify. Reference EXPERIMENTAL_DESIGN §8b.}}
**Actionable recommendations** (can a practitioner change behavior WITHOUT reading the paper?):

1. {{Recommendation 1: what to do, who should do it, expected benefit}}
2. {{Recommendation 2}}
3. {{Recommendation 3}}

**Artifacts released:**

| Artifact | Install Method | Status |
|----------|---------------|--------|
| {{Artifact 1}} | {{single-command install / download / integrate}} | SHIPPED / PLANNED |

> For 7.0+: At least 1 artifact with status=SHIPPED.

**Baseline fairness statement (A4):** {{How were baselines given equivalent treatment? If defaults used, why?}}

**Real-world validation:** {{Tested on real systems? Production data? Or simulation/synthetic only? Reference EXPERIMENTAL_DESIGN §8b validation plan.}}

---

## Cross-Domain Connections

<!-- REQUIREMENT: cross-domain evidence standards -->
> For 7.0+: at least 1 cross-domain transfer test with COMPLETED status. Single-domain projects must state "Single-domain study; cross-domain transfer not tested" with rationale for why transfer was deferred.
>
> Cross-domain claims require computed metrics, not stated analogies. If you claim an information-theoretic or game-theoretic connection, the corresponding metric must be COMPUTED on actual data. Stated analogies are hypotheses; computed metrics are evidence.
>
> Transfer test results: negative transfer (finding does NOT hold in target domain) is a valid and publishable result. Document it honestly.
<!-- /REQUIREMENT -->

<!-- INSTANCE: fill per project -->
**Domains connected:** {{List domains this finding bridges}}
**Methods imported:** {{Any methodology borrowed from a different field?}}

**Domain-agnostic principle (A2 step 1):** {{State the principle without domain-specific terms}}
**Principle generalization:** {{Is there a principle that applies across domains? Validated in how many?}}

**Transfer test results (A1):**

| Target Domain | Prediction | Result | Metric | Status |
|---|---|---|---|---|
| {{Domain 1}} | {{What the principle predicts here}} | {{Actual finding}} | {{Computed metric}} | COMPLETED / DEFERRED: {{reason}} |

**Boundary conditions (A2 step 4):** {{Where does the transfer break? What conditions invalidate it?}}
<!-- /INSTANCE -->

---

## Generalization Analysis

<!-- REQUIREMENT: structurally diverse evaluation evidence -->
> [SEED: sunset after 5 projects if section doesn't improve generalization scores | PT-5]
>
> Evaluation conditions must be structurally diverse (A3): different provider/architecture, different data source, or different threat/failure model. Minimum 2 structural dimensions for 7.0+. Document which structural dimension each condition varies.
>
> Failure modes must be quantified with specific thresholds, not just listed qualitatively.
<!-- /REQUIREMENT -->

<!-- INSTANCE: fill per project -->
**Scope:** {{What models, datasets, settings, populations was this tested on?}}
**Evaluation conditions:**

| Condition | Structural Dimension Varied | Result | vs Primary Setting |
|-----------|----------------------------|--------|-------------------|
| {{Condition 1}} | {{provider/architecture / data source / threat model}} | {{Result}} | {{Delta from primary}} |
| {{Condition 2}} | {{provider/architecture / data source / threat model}} | {{Result}} | {{Delta from primary}} |

**Failure modes:**

| Condition | Threshold | Metric | Severity |
|---|---|---|---|
| {{When method breaks}} | {{Quantified boundary}} | {{Metric}} | {{Degrades / fails completely}} |

**Transfer assessment:** {{Would these findings transfer to different tools/frameworks/domains?}}
<!-- /INSTANCE -->

---

## Primary Contribution (ONE statement)

<!-- source: Track 1, Milkman (framed methodology as primary contribution — megastudy design — with exercise results as demonstration; this framing choice made it a Nature paper) -->

> {{State the ONE thing a practitioner remembers from this research. ≤2 sentences. All experiments above support this finding. If you can't state it in 2 sentences, you have breadth, not depth.}}

**Contribution type:** Is your methodology or your finding the primary contribution?
- If **methodology**: your finding demonstrates the methodology. Frame the contribution as the METHOD, with results as evidence it works. (Milkman: megastudy design is the contribution; exercise nudge results demonstrate it.)
- If **finding**: your methodology enables the finding. Frame the contribution as the RESULT, with methods as the tool that produced it. (Chetty: neighborhood effects on mobility is the contribution; the Atlas methodology enables it.)

> [SEED: contribution_type options: methodology, finding, dual (both
> are independently significant — rare, requires both to be novel)]

**Self-test:** If you removed your methodology and someone else reproduced your finding with a different method, would your paper still matter? If yes, the FINDING is primary. If no — if the method IS the insight — the METHODOLOGY is primary. (Bell: the loophole-free test methodology IS the contribution; the quantum violation result was expected. Milkman: the megastudy design IS the contribution; exercise nudge results demonstrate it. Chetty: neighborhood mobility effects ARE the contribution; the Atlas methodology enables it.)

**Supporting experiments:** {{List which experiments directly support the primary contribution vs which provide context.}}

---

## Breakthrough Question

> {{What question did this research raise that you did NOT expect? What would you investigate next if score didn't matter? This drives curiosity beyond compliance.}}

---

## Artifact Registry

| Artifact | Path | SHA-256 | Description |
|----------|------|---------|-------------|
| Raw results | {{OUTPUTS_DIR}}/results.json | {{hash}} | {{description}} |
| Figures | {{FIGURES_DIR}}/*.png | {{hash}} | Generated by make_report_figures.py |
| Model checkpoints | {{OUTPUTS_DIR}}/models/ | {{hash}} | {{description}} |

---

## Acceptance Criteria

> Cross-reference with CLAIM_STRENGTH_SPEC §6. All must pass before this document is marked complete.

- [ ] 100% of quantitative claims tagged
- [ ] No prohibited language without required evidence
- [ ] Raw data reconciliation passed (claims match {{OUTPUTS_DIR}})
- [ ] Executive Summary contains only [DEMONSTRATED] or [SUGGESTED]
- [ ] All [HYPOTHESIZED] claims appear in Limitations
- [ ] Claim Strength Legend present
- [ ] Synthetic data subsection present (if {{DATA_TYPE}} != real)
- [ ] No [DEMONSTRATED] claims with fewer than {{MIN_SEEDS}} seeds
- [ ] All hypotheses from HYPOTHESIS_REGISTRY resolved in Hypothesis Resolutions table
- [ ] Artifact Registry populated with SHA-256 hashes

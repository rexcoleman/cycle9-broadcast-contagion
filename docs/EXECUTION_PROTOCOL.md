# Execution Protocol — {{PROJECT_NAME}}

<!-- version: 1.0 -->
<!-- created: {{DATE}} -->
<!-- stage: 5 -->
<!-- methodology_status: full — Stage 5 methodology from Phase B.2b, 6 sections -->

> **Purpose:** Govern what happens DURING execution — the gap between
> EXPERIMENTAL_DESIGN (what to do) and FINDINGS (what you found). This
> template encodes execution methodology that 5/7 breakthrough papers
> used but that has no prior govML coverage. Fill this template DURING
> execution, not before or after.

> **Authority Hierarchy**
>
> <!-- Convention note: Standard govML templates use {{TIER_N_DOC}} placeholders
>      for project-specific authority documents (see ED, FINDINGS). This template
>      intentionally hardcodes template-to-template relationships instead because
>      Stage 5 is structurally positioned as a bridge: it receives its plan from
>      EXPERIMENTAL_DESIGN and feeds its execution record to FINDINGS. The authority
>      chain IS the template pipeline. Projects may override with project-specific
>      authorities by replacing the document names below. -->
>
> | Priority | Document | Role |
> |----------|----------|------|
> | Tier 1 | `EXPERIMENTAL_DESIGN.md` | Design contract — what you planned to do |
> | Tier 2 | This document | Execution record — what you actually did and how |
> | Tier 3 | `FINDINGS.md` | Downstream — consumes this document's deviation and quality data |
> | Contract | `HYPOTHESIS_REGISTRY.md` | Pre-registered predictions — deviations from these require logging |
>
> **Conflict rule:** If execution deviates from EXPERIMENTAL_DESIGN, log the
> deviation in §5 with rationale. EXPERIMENTAL_DESIGN remains the design
> of record; this document records the execution of record.

### Companion Contracts

**Upstream (this document depends on):**
- See [EXPERIMENTAL_DESIGN](EXPERIMENTAL_DESIGN.tmpl.md) for experimental plan, baselines, ablation design, statistical plan
- See [HYPOTHESIS_REGISTRY](HYPOTHESIS_REGISTRY.tmpl.md) for pre-registered predictions and lock_commit

**Downstream (depends on this document):**
- See [FINDINGS](FINDINGS.tmpl.md) for analysis and claim tagging — references deviation log and quality gate results
- See [DECISION_LOG](../management/DECISION_LOG.tmpl.md) for design deviations requiring formal rationale

## Customization Guide

| Placeholder | Description | Example |
|-------------|-------------|---------|
| `{{PROJECT_NAME}}` | Project name | Opportunity Atlas Replication |
| `{{DATE}}` | Creation date | 2026-04-08 |
| `{{EXECUTION_TYPE}}` | Primary execution type | computational / experimental / observational / mixed |
| `{{QUALITY_CHECK_INTERVAL}}` | How often quality checks run | per-batch / per-epoch / per-linkage-step / daily |
| `{{CONVERGENCE_METRIC}}` | What determines execution is complete | loss plateau / coverage threshold / all planned analyses run |
| `{{PRIMARY_OUTCOME_VARIABLE}}` | What you're measuring | income rank / GDT score / gym visits / token green-list proportion |

---

## §1 Execution Quality Gates

<!-- source: Track 1, AlphaFold (iterative recycling QC), Bell (event-by-event spacelike verification), GNoME (per-round hit rate tracking), Chetty (96% linkage match rate verified before analysis) -->

<!-- REQUIREMENT: continuous quality monitoring during execution -->
> Execution without runtime quality checks risks discovering fatal data or
> process problems only at analysis time — when the cost of re-execution is
> highest. 4/7 breakthrough papers ran quality checks DURING execution, not
> just before or after.
>
> **Science-agnostic framing:** "Runtime" means during your primary execution
> activity — whether that is training a model, collecting experimental data,
> processing administrative records, or coding archival sources.
<!-- /REQUIREMENT -->

### §1.1 Quality Check Specification

<!-- INSTANCE: fill per project -->

**Execution type:** {{EXECUTION_TYPE}}

**For computational/experimental execution:**

| # | Quality check | Runs when | Pass criterion | Fail action |
|---|---|---|---|---|
| 1 | {{CHECK_NAME}} | {{TRIGGER — e.g., every epoch, every batch, every N samples}} | {{THRESHOLD — e.g., loss < X, accuracy > Y}} | {{ACTION — e.g., re-run with adjusted hyperparameters, flag for review}} |
| 2 | {{CHECK_NAME}} | {{TRIGGER}} | {{THRESHOLD}} | {{ACTION}} |

> [SEED: min_quality_checks=2]

**For observational/administrative-data execution:**

| # | Data quality check | Runs when | Pass criterion | Fail action |
|---|---|---|---|---|
| 1 | {{CHECK_NAME — e.g., linkage match rate, coverage per subgroup, missing data rate}} | {{TRIGGER — e.g., per linkage step, per data vintage, per geographic unit}} | {{THRESHOLD — e.g., >90% match rate, <5% missing}} | {{ACTION — e.g., reprocess batch, apply imputation, flag subgroup}} |
| 2 | {{CHECK_NAME}} | {{TRIGGER}} | {{THRESHOLD}} | {{ACTION}} |

> [SEED: min_quality_checks=2]
<!-- /INSTANCE -->

### §1.2 Convergence / Completion Criterion

<!-- INSTANCE: fill per project -->

**What determines that execution is complete?**

| Execution type | Criterion | How measured |
|---|---|---|
| Computational | {{e.g., validation loss plateaus for N epochs, active learning hit rate stabilizes}} | {{metric + threshold}} |
| Experimental | {{e.g., target sample size reached, all planned conditions run}} | {{count + verification}} |
| Observational | {{e.g., all planned data linkages completed, all subgroup analyses specified}} | {{checklist + coverage report}} |

> Fill the row matching your `{{EXECUTION_TYPE}}`. Delete or mark N/A for
> non-matching rows.

**Early stopping triggers** (conditions that halt execution before completion):

| # | Trigger | Evidence threshold | Action |
|---|---|---|---|
| 1 | {{e.g., data quality below minimum, safety concern, resource exhaustion}} | {{specific threshold}} | {{stop / pause + investigate / escalate}} |

> [SEED: early_stopping_triggers=1 minimum; "none anticipated" is valid but
> must be stated explicitly]
<!-- /INSTANCE -->

### §1.3 Quality Gate Results Log

Record quality gate outcomes as execution proceeds. This log feeds into
FINDINGS §Experiment Completeness and §Limitations.

| Date | Check # | Result | Action taken | Notes |
|---|---|---|---|---|
| {{DATE}} | {{CHECK_#}} | PASS / FAIL / WARN | {{action or "none"}} | {{context}} |

**Self-test:** If all quality gates PASS with no warnings throughout
execution, is your quality threshold set too low? A threshold that never
triggers may not be testing anything meaningful. State whether your thresholds
were calibrated from pilot data, prior work, or domain convention — and
whether any threshold was close to triggering.

---

## §2 Measurement Protocol

<!-- source: Track 1, Milkman (objective gym swipe data over self-report), Chetty (population administrative data — 96% coverage, not sample), Bell (sub-nanosecond timestamping for spacelike verification) -->

<!-- REQUIREMENT: measurement quality assessment -->
> The gap between what you intend to measure and what your instrument actually
> captures is a primary threat to validity. 3/7 breakthrough papers gained
> credibility specifically from measurement quality: Milkman chose objective
> gym swipe data over self-reported exercise; Chetty used population-level
> administrative records instead of survey samples; Bell achieved
> sub-nanosecond timestamping to verify spacelike separation.
>
> This section applies to ALL research types. Computational research measures
> model outputs. Observational research measures existing records. Experimental
> research measures intervention outcomes. The question is always: does your
> measurement capture the construct you claim to study?
<!-- /REQUIREMENT -->

### §2.1 Primary Outcome Measurement

<!-- INSTANCE: fill per project -->

**Primary outcome variable:** {{PRIMARY_OUTCOME_VARIABLE}}

| Attribute | Your measurement | Assessment |
|---|---|---|
| Objective or self-report? | {{objective instrument / administrative record / self-report / expert judgment}} | {{If self-report: what objective proxy exists? If none, state why self-report is necessary.}} |
| Direct or proxy? | {{direct measurement of construct / proxy for underlying construct}} | {{If proxy: what is the gap between your proxy and the true construct? Chetty: income rank from tax returns directly measures income but is a proxy for "opportunity."}} |
| Coverage | {{population / sample — state coverage rate or sampling strategy}} | {{Chetty: 96% of target population via IRS-Census linkage. What is YOUR coverage, and what does missingness look like?}} |
| Precision | {{measurement resolution — e.g., sub-nanosecond, census-tract level, ±5% accuracy}} | {{Is this precision sufficient for your claimed effect size? Bell needed sub-nanosecond to verify spacelike separation; lower precision would have left the loophole open.}} |
| Calibration | {{How do you know your instrument measures what you think it measures?}} | {{For computational: validation against known inputs (see ED §14 E0). For observational: construct validity evidence. For experimental: instrument calibration records.}} |

> [SEED: measurement_type options: objective_instrument, administrative_record,
> self_report, expert_judgment, computational_output, sensor_data]
<!-- /INSTANCE -->

### §2.2 Measurement Threats

<!-- INSTANCE: fill per project -->

| # | Threat | Applies to your measurement? | Mitigation |
|---|---|---|---|
| 1 | Selection bias (who/what is measured vs not) | {{yes/no — explain}} | {{mitigation or "accepted limitation"}} |
| 2 | Measurement reactivity (does measuring change behavior?) | {{yes/no}} | {{mitigation}} |
| 3 | Temporal mismatch (measurement timing vs phenomenon timing) | {{yes/no}} | {{mitigation}} |
| 4 | Construct validity gap (proxy doesn't capture true construct) | {{yes/no}} | {{mitigation}} |

> Not all threats apply to all research types. Measurement reactivity is
> irrelevant for administrative data analysis but critical for behavioral
> experiments. Mark "N/A" with a one-line reason for threats that don't apply.
<!-- /INSTANCE -->

**Self-test:** If a critic argued your primary outcome measurement doesn't
actually capture what you claim to study, what would their strongest argument
be? If you can't articulate the critic's case, you may not have examined your
measurement's construct validity deeply enough.

> **Effect size interpretation (S75 audit):** Effect sizes (Cohen's d, eta-squared,
> odds ratios) must be reported WITH absolute magnitudes, not just statistical
> significance. A Cohen's d > 2.0 from near-zero-variance data (e.g., means of
> 0.000 vs 0.002) is a statistical artifact, not a "massive" practical effect.
> When reporting effect sizes:
> 1. State the absolute magnitude difference alongside the effect size
> 2. State whether the variance is driven by meaningful variation or near-zero noise
> 3. If effect size exceeds 2.0, verify the practical significance matches before
>    claiming "large" or "massive" effects
>
> [SEED: effect_size_interpretation. Sunset after 5 projects if never triggered.]

---

## §3 Blinding and Specification Commitment

<!-- source: Track 1, AlphaFold (CASP blind competition — predictions locked before answers revealed), Milkman (pre-registered, expert predictions collected before results), Chetty (analysis specification committed before tract-level outcome examination), Bell (remaining loopholes explicitly bounded) -->

<!-- REQUIREMENT: separation of execution decisions from outcome knowledge -->
> Knowing intermediate results changes how you execute. AlphaFold submitted
> predictions to CASP before answers were revealed — the blind competition
> structure prevented any possibility of fitting to known answers. Milkman
> pre-registered the analysis plan and collected expert predictions before
> seeing results. Chetty committed his analytical specification before
> examining tract-level outcome distributions.
>
> The principle is universal: separate what you DECIDE from what you KNOW
> about outcomes. The mechanism differs by research type.
<!-- /REQUIREMENT -->

### §3.1 Blinding Assessment

<!-- INSTANCE: fill per project -->

**For experimental/computational research:**

| Question | Your answer |
|---|---|
| Who sees intermediate results before the analysis plan is locked? | {{list roles/people}} |
| Can outcome evaluation be blinded? (e.g., blind competition, held-out test set, independent evaluator) | {{yes — mechanism / no — why not}} |
| Can outcome measurement be separated from intervention delivery? | {{yes — how / no — why not / N/A}} |
| What ordering prevents seeing results from influencing execution? | {{e.g., predictions submitted before answers revealed, analysis script written before data collected}} |

**For observational/administrative-data research:**

| Question | Your answer |
|---|---|
| Who has access to the outcome variable before the analysis specification is finalized? | {{list roles/people}} |
| Can you commit your analysis specification before examining the outcome data? | {{yes — mechanism (e.g., pre-analysis plan filed, code written on mock data) / no — why not}} |
| If you've already seen the data, what constrains your analytical flexibility? | {{e.g., pre-registration, replication sample, holdout subgroup, sensitivity analysis protocol}} |
| What prevents specification search (trying multiple models until one "works")? | {{mechanism or "accepted risk — documented in §5 Deviation Log"}} |

> [SEED: blinding_level options: fully_blind (no access to outcomes during
> execution), partially_blind (some intermediate results visible),
> specification_committed (analysis locked before outcome examination),
> unblinded_with_constraints (outcomes visible but flexibility constrained),
> unblinded (no blinding — state why acceptable)]
<!-- /INSTANCE -->

**Self-test:** Could you, in principle, change your analysis approach after
seeing a pattern in the outcome data? If yes, what specifically prevents you
from doing so — social commitment (weak), pre-registration (moderate), or
structural separation like blind competition (strong)? If nothing prevents it,
this is a limitation to acknowledge, not a problem to ignore.

---

## §4 Iterative Refinement Protocol

<!-- source: Track 1, GNoME (predict → DFT validate → retrain, 6 rounds, hit rate 6%→80%), AlphaFold (iterative recycling, 3 passes — output feeds back as input), Bell (earlier runs with lower source brightness failed → iterated on source optimization) -->

> **Conditional section.** Not all research involves iteration. Single-pass
> analyses (one regression, one survey, one archival coding pass) should mark
> this section "N/A — single-pass execution" and skip to §5. But if your
> execution DOES include iterative refinement — active learning loops, model
> recycling, sequential experimental batches, or iterative data processing
> pipelines — this section prevents iteration from becoming untracked
> overfitting.

<!-- REQUIREMENT: iteration tracking when applicable -->
> GNoME's active learning loop (6 rounds, hit rate 6%→80%) is a powerful
> execution methodology — but only because each round's improvement was
> tracked and the stopping criterion was explicit. Untracked iteration
> risks: overfitting to validation data, losing the record of what
> changed between rounds, and inability to attribute improvement to
> specific changes.
<!-- /REQUIREMENT -->

### §4.1 Iteration Design

<!-- INSTANCE: fill per project -->

**Does your execution include iterative refinement?**
- [ ] Yes — complete this section
- [ ] No — mark "N/A — single-pass execution" and skip to §5

**If yes:**

| Attribute | Your design |
|---|---|
| What triggers each iteration? | {{e.g., new validation data available, previous round's error analysis, resource availability}} |
| What changes between iterations? | {{e.g., training data (active learning), model parameters (recycling), experimental conditions (sequential batches), processing pipeline (shrinkage calibration)}} |
| Stopping criterion | {{e.g., hit rate stabilizes, validation metric plateaus, diminishing returns threshold, budget exhausted}} |
| How do you prevent overfitting across iterations? | {{e.g., held-out test set untouched until final round, fresh validation data each round, pre-registered stopping rule}} |
| Maximum iterations planned | {{number or "until convergence criterion met"}} |

> [SEED: max_iterations=6 (GNoME used 6 rounds); adjust based on
> computational budget and domain norms]
<!-- /INSTANCE -->

### §4.2 Iteration Log

Record each iteration's key metrics. This log feeds into FINDINGS to
support claims about iterative improvement.

| Round | Date | What changed | Key metric (before) | Key metric (after) | Decision |
|---|---|---|---|---|---|
| 1 | {{DATE}} | {{change description}} | {{metric}} | {{metric}} | continue / stop / modify approach |
| 2 | {{DATE}} | {{change description}} | {{metric}} | {{metric}} | continue / stop / modify approach |

**Self-test:** After your final iteration, could you have achieved a similar
result in fewer rounds? If you can't answer this, you may not have tracked
enough to understand what actually drove improvement. GNoME's hit rate
trajectory (6%→33%→52%→65%→74%→80%) shows clear diminishing returns —
can you show yours?

---

## §5 Deviation Log

<!-- source: Track 1 gap matrix Stage 5; EXPERIMENTAL_DESIGN §13 (Phase 1 Exit Checkpoint) requires post-hoc deviation check — this section captures deviations IN REAL TIME during execution -->

<!-- REQUIREMENT: real-time deviation tracking -->
> EXPERIMENTAL_DESIGN §13 asks whether deviations occurred AFTER execution
> completes. By then, memory of why a deviation happened is degraded, and
> small deviations that compound are harder to reconstruct. This section
> captures deviations AS THEY OCCUR.
>
> **For observational research:** Deviations from a pre-analysis plan are
> the primary source of "researcher degrees of freedom." Logging them in
> real time — with rationale BEFORE seeing whether the deviation changes
> results — is stronger evidence of honest analytical practice than
> post-hoc reconstruction.
<!-- /REQUIREMENT -->

> **Pre-registration deviations are deviations.** If a hypothesis resolution
> differs from the pre-registered prediction in HYPOTHESIS_REGISTRY — different
> topology, different direction, different magnitude — log it here with the
> same format. A finding that contradicts the pre-registered expectation IS
> a deviation from the experimental design, even if the experiment ran correctly.

### §5.1 Deviation Table

<!-- INSTANCE: fill per project -->

| # | Date | What was planned (cite ED section) | What actually happened | Why | Impact assessment | Results affected? |
|---|---|---|---|---|---|---|
| DEV-1 | {{DATE}} | {{planned action from ED §N}} | {{actual action}} | {{rationale — written BEFORE seeing impact on results}} | {{none / minor / major — explain}} | {{which findings, if any, are affected}} |

> **Deviation severity guide:**
> - **None:** Cosmetic change (variable renamed, file reorganized). No impact on results.
> - **Minor:** Adjustment within planned parameters (fewer seeds than ideal but ≥ minimum, slightly different hyperparameter range). Results interpretable but note in FINDINGS §Limitations.
> - **Major:** Fundamental change to design (different baseline, different data source, different analysis method). Requires DECISION_LOG entry with formal rationale. May require re-evaluation of pre-registered hypotheses.
<!-- /INSTANCE -->

### §5.2 Unplanned Analyses

Analyses not in EXPERIMENTAL_DESIGN that were run during execution.
These are not necessarily problems — exploratory analysis is valid — but
they must be documented so FINDINGS can tag them correctly (EXPLORATORY
phase, not CONFIRMATORY).

| # | Date | Analysis description | Motivated by | Result reported in FINDINGS? |
|---|---|---|---|---|
| UNP-1 | {{DATE}} | {{what was analyzed}} | {{what prompted this — e.g., unexpected pattern in quality gate, reviewer suggestion, curiosity}} | {{yes — Finding N / no — why not}} |

> [SEED: unplanned_analyses expected: 1-3 per project. Zero unplanned
> analyses in a real execution is unusual — it may mean you're not looking
> at your data during execution, or not logging what you find.]

**Self-test:** For each unplanned analysis: if you had NOT seen the
intermediate result that prompted it, would you still have run this
analysis? If no, it is by definition exploratory — ensure FINDINGS tags
it as EXPLORATORY, not CONFIRMATORY.

---

## §6 Execution Completion Checklist

<!-- source: Track 1 gap matrix Stage 5 → Stage 6 transition; cross-reference EXPERIMENTAL_DESIGN §13 Phase 1 Exit Checkpoint -->

<!-- REQUIREMENT: execution completeness verification before analysis -->
> This checklist verifies execution is complete before transitioning to
> Stage 6 (Analysis / FINDINGS). It complements ED §13 Phase 1 Exit
> Checkpoint — ED §13 checks design compliance; this checklist checks
> execution completeness. Both must pass before FINDINGS work begins.
<!-- /REQUIREMENT -->

### §6.1 Completeness Verification

<!-- INSTANCE: fill per project -->

| # | Check | Status | Evidence |
|---|---|---|---|
| 1 | All planned experiments/analyses from ED were executed (or deviations logged in §5) | [ ] | {{list completed items or cite deviation DEV-#}} |
| 2 | All quality gates in §1 have results logged in §1.3 | [ ] | {{count: N checks recorded}} |
| 3 | Convergence/completion criterion from §1.2 met | [ ] | {{final metric value vs threshold}} |
| 4 | Measurement protocol from §2 followed as specified | [ ] | {{any measurement deviations logged in §5?}} |
| 5 | All deviations from ED logged in §5 with rationale | [ ] | {{count: N deviations, N with rationale}} |
| 6 | Unplanned analyses documented in §5.2 | [ ] | {{count: N unplanned analyses logged}} |
| 7 | Iteration log in §4 complete (if applicable) | [ ] | {{N/A or count: N rounds logged}} |
| 8 | ED §13 Phase 1 Exit Checkpoint also passes | [ ] | {{cross-reference: checked on DATE}} |
| 9 | Raw outputs exist for all reported conditions | [ ] | {{path to outputs directory}} |
| 10 | Execution timeline documented | [ ] | {{start date → end date}} |
<!-- /INSTANCE -->

### §6.2 Transition Declaration

<!-- INSTANCE: fill per project -->

**Execution start date:** {{DATE}}
**Execution end date:** {{DATE}}
**Total execution time:** {{duration}}

**Completeness verdict:** [ ] PASS — proceed to FINDINGS / [ ] FAIL — resolve gaps first

**Known issues carrying forward to FINDINGS:**
1. {{issue or "none"}}

> If FAIL: list which checks failed and what must be resolved before
> analysis begins. Do NOT begin FINDINGS with a failed completion check —
> incomplete execution produces incomplete findings.
<!-- /INSTANCE -->

**Self-test:** If someone replicated your execution using only
EXPERIMENTAL_DESIGN and this EXECUTION_PROTOCOL, would they have enough
information to reproduce your results? What's missing? If anything is
missing, add it to the deviation log or the completion checklist notes
before transitioning.

---

## Acceptance Criteria

> All must pass before this document is considered complete.

- [ ] Execution type declared and consistent throughout (§1.1, §2.1)
- [ ] ≥2 quality checks specified in §1.1
- [ ] Convergence/completion criterion specified in §1.2
- [ ] Primary outcome measurement assessed in §2.1 (all 5 attributes)
- [ ] Blinding level assessed in §3.1
- [ ] §4 either completed or marked N/A with justification
- [ ] All deviations from ED logged in §5 with rationale
- [ ] §6 completion checklist passed before FINDINGS work began
- [ ] Source markers present on all methodology sections
- [ ] Self-test answered for each section

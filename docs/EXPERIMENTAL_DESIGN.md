# EXPERIMENTAL DESIGN REVIEW

<!-- version: 1.0 -->
<!-- created: 2026-03-19 -->
<!-- gate: 0.5 (must pass before Phase 1 compute) -->

> **Authority hierarchy:** {{TIER_1_SOURCE}} (Tier 1) > {{TIER_2_SOURCE}} (Tier 2) > {{TIER_3_SOURCE}} (Tier 3) > This document (Contract)
> **Conflict rule:** When a higher-tier document and this contract disagree, the higher tier wins.
> **Upstream:** DATA_CONTRACT (data sources), EXPERIMENT_CONTRACT (experiment protocol), HYPOTHESIS_REGISTRY (pre-registered hypotheses)
> **Downstream:** All Phase 1+ artifacts. This document gates the transition from Phase 0 (setup) to Phase 1 (training).

> **Purpose:** Force experimental design decisions BEFORE compute begins. Every reviewer kill shot in FP-05 was knowable on day 1 but wasn't caught until quality assessment. This template prevents that. (LL-90)

---

## Customization Guide

| Placeholder | Description | Example |
|-------------|-------------|---------|
| `{{PROJECT_NAME}}` | Project name | ML-Driven Vulnerability Prioritization |
| `{{TARGET_VENUE}}` | Target workshop/conference/journal | AISec Workshop (ACM CCS) |
| `{{VENUE_TIER}}` | Tier level (Workshop, Tier 2, Tier 1) | Tier 2 |
| `{{LOCK_COMMIT}}` | Git SHA when this design review is approved | `abc1234` |
| `{{COMPARISON_BASELINES}}` | Published methods to compare against | Bozorgi et al. (2010), EPSS threshold |
| `{{NOVELTY_CLAIM}}` | One-sentence novelty statement | First open-source 7-algorithm comparison with dual ground truth and temporal split |

---

## 0) Problem Selection Gate (Gate -1)

<!-- REQUIREMENT: domain-agnostic problem selection criteria -->
> This section gates whether the project is worth starting. Complete BEFORE filling the rest of this document. If any row scores below the minimum, reconsider the problem or reframe the approach.
> Generalizable: applies to ANY research project in the pipeline (Two Domains: pipeline infrastructure).

| Criterion | Question | Min for 7.0+ |
|---|---|---|
| **Practitioner pain** | Who has this problem? How many? Evidence? | Named audience + quantified magnitude |
| **Research gap** | What's NOT known? What would your work add? | ≥1 unanswered question with <3 papers addressing it |
| **Novelty potential** | Can this produce a SURPRISING result? What would surprise you? | Pre-registered expected outcome with deviation = novelty |
| **Cross-domain bridge** | What OTHER domain faces an analogous problem? What method could you import? | ≥1 analogous domain identified + ≥1 importable method |
| **Artifact potential** | What installable artifact could this produce? | Concrete installable artifact specified — not "maybe a tool later" |
| **Real-world test** | Can you validate on real systems, not just simulation? | ≥1 real-system test condition identified |
| **Generalization path** | Can you test on ≥2 structurally diverse conditions? | ≥2 evaluation conditions differing on a structural dimension |
| **Portfolio check (P5)** | Is this a NEW project or retrofit of existing? If retrofit, would a new project reach 7.0+ faster? | Explicit choice with rationale |
| **Formalization potential** | Can you state a conjecture, bound, or formal relationship? Even informal: "if X then Y, bounded by Z" | Attempt stated (not required to prove) |
| **Breakthrough question** | If you were NOT trying to score well on the rubric, what is the most interesting question this research could answer? | Question stated — this drives curiosity beyond compliance |
| **Assumption challenged** | What does the field currently believe that this work might show is wrong? Name the specific assumption and ≥2 published papers that hold it. Search for papers whose findings CONTRADICT your hypothesis (top 5 contradicting papers). "None — this is incremental" is valid but caps novelty at 6. | Named assumption + ≥2 papers holding it + contradiction search results |
| **Time-to-outcome feasibility** | When will your primary outcome be measurable? If >5 years, what intermediate outcomes can you target within your research timeline? If no intermediate outcome exists, this question may need reframing. **Self-test:** Could you publish a paper with measurable results within your planned timeline? If your answer relies on "intermediate outcomes," are those outcomes independently valuable or just proxies that defer the real test? | Primary outcome timeline stated. If >5 years: intermediate outcome identified with measurable timeline, OR question reframed. |
<!-- source: B.1-TEST impulse #2 — HIGH severity -->
<!-- /REQUIREMENT -->

<!-- INSTANCE: fill per project -->
| Criterion | Your Answer |
|---|---|
| Practitioner pain | {{ANSWER}} |
| Research gap | {{ANSWER}} |
| Novelty potential | {{ANSWER}} |
| Cross-domain bridge | {{ANSWER}} |
| Artifact potential | {{ANSWER}} |
| Real-world test | {{ANSWER}} |
| Generalization path | {{ANSWER}} |
| Portfolio check | {{ANSWER}} |
| Formalization potential | {{ANSWER}} |
| Breakthrough question | {{ANSWER}} |
| Assumption challenged | {{ANSWER — name the assumption, cite ≥2 papers holding it, list top contradicting papers from literature search}} |
| Time-to-outcome feasibility | {{ANSWER — state when primary outcome is measurable. If >5 years, name intermediate outcome and its timeline. [SEED: 5-year threshold; sunset if field-specific norms diverge significantly — e.g., economics intergenerational studies ~20 years, clinical trials 10+ years, physics detector development 5-10 years, ML model training weeks-months]}} |
<!-- /INSTANCE -->

**Gate -1 verdict:** [ ] PASS — all rows meet minimums, proceed to full design.

---

## 1) Project Identity

**Project:** {{PROJECT_NAME}}
**Target venue:** {{TARGET_VENUE}} ({{VENUE_TIER}})
**Design lock commit:** {{LOCK_COMMIT}}
**Design lock date:** {{DATE}}

> **Gate 0.5 rule:** This document must be committed before any Phase 1 training script is executed. Any experiment output with a git timestamp before the lock commit is invalid for claims about pre-registered design.

> **Enforcement (G-2):** Add this check to `reproduce.sh`:
> ```bash
> grep -q "lock_commit.*TO BE SET\|lock_commit.*PENDING" EXPERIMENTAL_DESIGN.md && echo "FAIL: lock_commit not set" && exit 1
> ```

---

## 2) Novelty Claim (one sentence)

> {{NOVELTY_CLAIM}}

**Self-test:** Can you state what is new in ≤25 words? If not, refine until you can. A project without a clear novelty claim is not ready for compute.

---

## 3) Comparison Baselines

<!-- REQUIREMENT: fair baseline comparison -->
> **Minimum:** ≥1 (Workshop), ≥2 (Tier 2), ≥3 including SOTA (Tier 1)
>
> **Baseline fairness (A4):** Each comparison baseline must receive equivalent tuning effort — same hyperparameter search budget, same training data access, same evaluation protocol. If a baseline is used with default settings, document WHY (e.g., "default settings represent real-world practitioner usage"). Unfair baselines are the #1 rigor rejection reason at top venues.
<!-- /REQUIREMENT -->

<!-- INSTANCE: fill per project -->
| # | Method | Citation | How We Compare | Why This Baseline | Tuning Parity |
|---|--------|----------|---------------|-------------------|---------------|
| 1 | {{BASELINE_1}} | {{CITATION_1}} | {{COMPARISON_METHOD_1}} | {{RATIONALE_1}} | {{Same tuning budget / defaults — reason: ...}} |
| 2 | {{BASELINE_2}} | {{CITATION_2}} | {{COMPARISON_METHOD_2}} | {{RATIONALE_2}} | {{Same tuning budget / defaults — reason: ...}} |

**Baseline fairness statement:** {{One sentence explaining how baselines received equivalent treatment, or why default settings are the appropriate comparison.}}
<!-- /INSTANCE -->

**Self-test:** If a reviewer asks "how does this compare to [published method]?" — can you answer with data? If not, add the baseline.

---

## 4) Pre-Registered Reviewer Kill Shots

> **Minimum:** 2 kill shots with planned mitigations.

| # | Criticism a Reviewer Would Make | Planned Mitigation | Design Decision |
|---|--------------------------------|-------------------|-----------------|
| 1 | {{KILL_SHOT_1}} | {{MITIGATION_1}} | {{DECISION_1}} |
| 2 | {{KILL_SHOT_2}} | {{MITIGATION_2}} | {{DECISION_2}} |

**Self-test:** Imagine the harshest R2 reviewer at your target venue. What would they write in the "Weaknesses" section? If you can't think of 2 criticisms, you haven't thought hard enough about your design.

---

### 4a) Constraint-Driven Design Check

<!-- source: Track 1, gap matrix Stage 4/priority 3 — 5/7 papers -->

> **Purpose:** Breakthrough researchers make design choices BECAUSE of constraints, not
> despite them. If you can't name the constraint behind a design choice, the choice may
> be arbitrary — or inherited from convention without examination.
>
> Bell: chose Eberhard inequality over CHSH because detector efficiency constraint
> (~66.7% vs ~82.8% threshold) — mathematical framework selected by engineering limits.
> Chetty: precision-weighted shrinkage estimator because thin census tracts have high
> variance — statistical method chosen by data sparsity constraint.
> AlphaFold: triangle attention for geometric consistency because protein residue
> relationships are inherently three-body — architecture chosen by physical constraint.
> Milkman: gym swipe data (not self-report) because behavioral science faces measurement
> reliability constraint — outcome measure chosen by objectivity requirement.
> Watermark: soft logit bias (not hard token blocking) because text quality must be
> preserved — watermarking method chosen by output quality constraint.

<!-- INSTANCE: fill per project -->
| # | Hardest constraint (data, compute, measurement, access, time) | Design choice it drove | Why this choice (not an alternative) |
|---|---|---|---|
| 1 | {{CONSTRAINT_1}} | {{CHOICE_1}} | {{RATIONALE_1}} |
| 2 | {{CONSTRAINT_2}} | {{CHOICE_2}} | {{RATIONALE_2}} |
| 3 | {{CONSTRAINT_3}} | {{CHOICE_3}} | {{RATIONALE_3}} |

> [SEED: require 3 constraint-choice pairs; sunset after 5 projects if researchers
> consistently identify fewer than 3 genuine constraints — reduce to 2 with rationale]

**Self-test:** For each design choice in your methodology, can you name the constraint
that drove it? If a choice has no constraint behind it, ask: is it convention, or is
it genuinely the best option? Choices inherited from convention without examination are
the most common source of "why didn't you try X?" reviewer questions.
<!-- /INSTANCE -->

---

## 5) Ablation Plan

<!-- REQUIREMENT: component ablation + novel component isolation -->
> **Minimum:** 1 group (Workshop), all major groups (Tier 2), all groups + interactions (Tier 1)
>
> **Novel component isolation (A5):** Standard ablation removes components from the whole system. For 7.0+, you must ALSO test the novel component independently — "if you claim X is your novel contribution, design an experiment testing X specifically (not just removing it from the system)." This isolates whether the novel component is the active ingredient vs. incidental.
<!-- /REQUIREMENT -->

<!-- INSTANCE: fill per project -->
**Component ablation:**

| Component / Feature Group | Hypothesis When Removed | Expected Effect | Priority |
|--------------------------|------------------------|-----------------|----------|
| {{GROUP_1}} | {{HYPOTHESIS_1}} | {{EXPECTED_1}} | HIGH |
| {{GROUP_2}} | {{HYPOTHESIS_2}} | {{EXPECTED_2}} | MEDIUM |

**Novel component isolation (A5):**

| Novel Claim (≤15 words) | Isolation Test | Expected If Active Ingredient | Expected If NOT Active Ingredient |
|---|---|---|---|
| {{Your novel contribution}} | {{Experiment testing ONLY the novel component}} | {{Specific metric change}} | {{What you'd observe instead}} |
<!-- /INSTANCE -->

**Self-test:** For each component, can you predict what happens when it's removed? If a removal result would surprise you, that's the most important ablation to run.

---

## 6) Ground Truth Audit

### 6a) Data Access Feasibility

<!-- source: B.1-TEST impulse #3 — Medium severity -->

> **Purpose:** Before auditing what data you HAVE, verify you can GET it. Data access
> barriers vary by field — from freely downloadable benchmarks to multi-year approval
> processes. Designing an experiment around data you cannot access is a feasibility
> failure, not a limitation to note later.
>
> Economics: restricted administrative data (IRS, Census) requires FSRDC access
> (6-18 months, may be denied). Biology: genomic sequencing costs $100-$10,000+
> per sample depending on method and coverage. Psychology: IRB approval for human
> subjects (weeks to months, protocol-dependent). ML: public benchmarks are freely
> available, but proprietary datasets (e.g., production logs) may require data-sharing
> agreements. Physics: detector time at shared facilities requires competitive proposals.

<!-- INSTANCE: fill per project -->
| Data source | Access barrier | Timeline to obtain | Fallback if denied |
|---|---|---|---|
| {{SOURCE_1}} | {{None / approval process / cost / restricted access / data-sharing agreement / IRB / competitive proposal / other}} | {{Immediate / weeks / months / years}} | {{Alternative source or redesign plan}} |

> [SEED: flag any source with timeline >3 months or uncertain access as HIGH risk;
> sunset threshold if projects routinely obtain data faster or slower than predicted]

**Self-test:** If your primary data source access were denied tomorrow, does your
fallback produce results that still answer the research question — or just a weaker
version that doesn't? If the fallback changes the question, the data access barrier
is a feasibility gate, not a logistics issue.

**LLM classification feasibility (if applicable):**

<!-- source: Phase E cycle 2 DEV-1 — Executor had no batch API access -->

If your methodology requires LLM-based classification or annotation of data:

| Check | Answer |
|---|---|
| **Items to classify** | {{COUNT}} |
| **Classification method** | {{Executor session (feasible for <100 items) / External API (requires API key in .env) / Scripted keyword-rule (unlimited)}} |
| **If >100 items:** | Keyword-rule or scripted classification should be primary method. LLM classification on a validation pilot (≤50 items) is feasible within the Executor session. |
| **API key available?** | {{Check .env — if no key, design for keyword-primary + LLM-pilot}} |

> [SEED: llm_session_classification_limit=100 items. Above this, the Executor
> session cannot perform batch classification — design for keyword-primary with
> LLM validation pilot. Calibrated from S59 cycle 2: Executor classified 50-item
> pilot directly, keyword-rule for 1,425 full dataset.]
<!-- /INSTANCE -->

> **Minimum:** ≥1 source (Workshop), ≥2 sources (Tier 2), ≥2 with agreement analysis (Tier 1)

### 6b) Ground Truth Sources

| Source | Type | Estimated Count | Known Lag | Estimated Positive Rate | Limitations |
|--------|------|----------------|-----------|------------------------|-------------|
| {{SOURCE_1}} | {{TYPE_1}} | {{COUNT_1}} | {{LAG_1}} | {{RATE_1}} | {{LIMITS_1}} |

**Alternative label sources considered:**

| Source | Why Included or Excluded | If Excluded, Could Add Later? |
|--------|-------------------------|------------------------------|
| {{ALT_SOURCE_1}} | {{RATIONALE_1}} | {{FEASIBILITY_1}} |

**Self-test:** If your only label source has a systematic bias (e.g., ExploitDB skews toward older CVEs), how would you know? A second source is the check.

---

## 7) Statistical Plan

> **Minimum:** ≥3 seeds (Workshop), ≥5 seeds with CIs (Tier 2), ≥5 seeds with bootstrap CIs (Tier 1)

| Parameter | Value | Justification |
|-----------|-------|---------------|
| Seeds | {{SEED_LIST}} | {{SEED_JUSTIFICATION}} |
| Significance test | {{SIG_TEST}} | {{TEST_JUSTIFICATION}} |
| Effect size threshold | {{EFFECT_SIZE}} | {{THRESHOLD_JUSTIFICATION}} |
| CI method | {{CI_METHOD}} | {{CI_JUSTIFICATION}} |
| Multiple comparison correction | {{CORRECTION}} | {{CORRECTION_JUSTIFICATION}} |

---

## 8) Related Work Checklist

> **Minimum:** ≥3 papers (Workshop), ≥5 papers (Tier 2), ≥10 papers positioned (Tier 1)

| # | Paper | Year | Relevance | How We Differ |
|---|-------|------|-----------|---------------|
| 1 | {{PAPER_1}} | {{YEAR_1}} | {{RELEVANCE_1}} | {{DIFFERENCE_1}} |

**Self-test:** Can you position your novelty claim against each paper? "We do X, they did Y, the difference is Z."

---

## 8a) Novelty Plan — Target: 7/10

<!-- REQUIREMENT: systematic novelty establishment -->
> [SEED: sunset after 5 projects if this never changes experimental design | PT-5]
> Addresses sub-criteria: prior_art, surprise_factor, contribution_type, novelty_ablation.
>
> Prior art search must use at least one systematic method (citation database search, connected-paper graph, or keyword co-occurrence mapping). Document databases queried, search terms used, and coverage assessment. Minimum 5 papers differentiated against.
>
> Expected contribution type: "novel combination" minimum for 7.0+. "Incremental improvement" caps novelty at 5.
>
> Pre-register expected outcomes — deviation from expectation IS the novelty.
>
> Novelty ablation: see §5 Novel Component Isolation (A5). If you can't specify what to ablate, the novelty claim may not be testable.
<!-- /REQUIREMENT -->

<!-- INSTANCE: fill per project -->
**Prior art search strategy:** {{Databases queried, search terms, coverage assessment}}

| Paper | Year | Their Claim | How We Differ |
|-------|------|-------------|---------------|
| {{Paper 1}} | {{Year}} | {{Their finding}} | {{What we do differently}} |
| {{Paper 2}} | {{Year}} | {{Their finding}} | {{What we do differently}} |
| {{Paper 3}} | {{Year}} | {{Their finding}} | {{What we do differently}} |
| {{Paper 4}} | {{Year}} | {{Their finding}} | {{What we do differently}} |
| {{Paper 5}} | {{Year}} | {{Their finding}} | {{What we do differently}} |

**Expected contribution type:** {{incremental / novel combination / novel methodology / new direction}}

**Pre-registered expected outcomes** (surprise_factor):

| Experiment | Expected Result | What Would SURPRISE You | How You'd Investigate |
|------------|----------------|------------------------|----------------------|
| {{Exp 1}} | {{Expected}} | {{Surprise}} | {{Follow-up experiment}} |
| {{Exp 2}} | {{Expected}} | {{Surprise}} | {{Follow-up experiment}} |
<!-- /INSTANCE -->

---

## 8b) Impact Plan — Target: 7/10

<!-- REQUIREMENT: practitioner-facing impact design -->
> [SEED: sunset after 5 projects if this never produces a shipped artifact | PT-5]
> Addresses sub-criteria: problem_magnitude, actionability, real_world_validation, artifact_release.
>
> Problem magnitude: Named audience with quantified magnitude for 7.0+. Generic audience descriptions are insufficient — identify specific practitioner communities with evidence of scale.
>
> Artifact-first: At least 1 artifact must ship WITH the experiment for 7.0+, not "planned for later." Artifact must be installable by a practitioner without reading source code (package registry, container, or single-command install).
>
> Actionability: Can a practitioner change their behavior based on your findings WITHOUT reading the paper?
>
> Real-world validation: At least 1 non-synthetic evaluation condition for 7.0+.
<!-- /REQUIREMENT -->

<!-- INSTANCE: fill per project -->
**Problem magnitude:** {{Who has this problem? How many practitioners/systems? Cite evidence.}}

**Artifact-first design** (artifact_release):

| Artifact | Type | How Practitioners Install/Use | Ships With Experiment? |
|----------|------|------------------------------|----------------------|
| {{Artifact 1}} | {{package / benchmark / dataset / plugin / tool / library}} | {{install command / download / integrate}} | YES / planned for Phase 3 |

**Actionability test:** {{YES — 1-sentence recommendation / NO — redesign for actionability}}

**Real-world validation plan** (real_world_validation):

| Condition | Real System | What It Tests | Feasibility |
|-----------|-------------|---------------|-------------|
| {{Condition 1}} | {{system description}} | {{Whether simulation findings hold}} | {{access / cost / time}} |
<!-- /INSTANCE -->

---

## 8c) Generalization Plan — Target: 7/10

<!-- REQUIREMENT: structurally diverse evaluation + cross-domain transfer protocol -->
> [SEED: sunset after 5 projects if this doesn't improve generalization scores | PT-5]
> Addresses sub-criteria: reproducibility, generalization_testing, failure_modes, independent_validation, transfer_evidence, method_import, principle_generalization.
>
> **Structural diversity (A3):** Evaluation conditions must differ on a **structural dimension** — different provider/architecture, different data source, or different threat/failure model. Parameter variations within the same structural family (e.g., different sizes from the same provider, different hyperparameters on the same dataset) do NOT count as distinct conditions. Minimum 2 structural dimensions checked for 7.0+.
>
> **Cross-domain transfer test (A1):** For 7.0+ target, at least 1 transfer test must have execution status = COMPLETED (not DEFERRED). If deferred, explicit justification required — no silent skips. Negative transfer results are valid and publishable. check_all_gates.sh enforces: WARN if no COMPLETED transfer test for Tier 2+ venue or 7.0+ target.
>
> **Cross-domain validation protocol (A2):** For each cross-domain claim, complete this 4-step protocol (based on Gentner's Structure-Mapping Theory):
> 1. **Domain-agnostic principle:** State the claimed principle without domain-specific terms. If removing domain-specific words destroys the claim, it is not transferable.
> 2. **Relational mapping:** Map source concepts to target concepts. Identify which relationships are preserved and whether they form interconnected systems (structural alignment) vs. isolated matches (superficial analogy).
> 3. **Testable prediction:** The transferred principle must predict something specific and falsifiable in the target domain — not just "this is similar."
> 4. **Boundary conditions:** Pre-register where you expect the transfer to BREAK. Documented boundaries strengthen the claim by defining its valid region.
>
> **Failure modes:** Pre-register where and how your method breaks. Quantify thresholds.
<!-- /REQUIREMENT -->

<!-- INSTANCE: fill per project -->
**Structural diversity checklist (A3):**

| Structural Dimension | Condition A | Condition B | Rationale |
|---|---|---|---|
| Provider/architecture | {{}} | {{}} | {{Tests whether finding is provider-specific}} |
| Data source | {{}} | {{}} | {{Tests whether finding is dataset-specific}} |
| Threat/failure model | {{}} | {{}} | {{Tests robustness to different adversary assumptions}} |

> Minimum 2 rows filled for 7.0+.

**Cross-domain validation protocol (A2):**

| Step | Content |
|---|---|
| 1. Domain-agnostic principle | {{State principle without domain-specific terms}} |
| 2. Relational mapping | {{Source concept → Target concept, relationship preserved? Interconnected system or isolated match?}} |
| 3. Testable prediction in target domain | {{Specific, falsifiable prediction}} |
| 4. Boundary conditions (where transfer breaks) | {{Pre-registered failure conditions}} |

**Cross-domain transfer test (A1):**

| Target Domain | Analogous Problem | Experiment | Execution Status | Result |
|---|---|---|---|---|
| {{Domain}} | {{What's analogous}} | {{Specific experiment}} | COMPLETED / DEFERRED: {{reason}} | {{Metric + finding, or pending}} |

> For 7.0+: At least 1 row with status = COMPLETED.

**Failure mode pre-registration:**

| Condition | Expected Failure | How Detected | Quantified Threshold |
|-----------|-----------------|-------------|---------------------|
| {{When does your method break?}} | {{Expected degradation}} | {{Metric}} | {{Threshold value}} |

**What constitutes transfer evidence:** {{Metric thresholds, acceptable degradation, etc.}}
<!-- /INSTANCE -->

---

## 9) Threats to Validity

<!-- REQUIREMENT: pre-registered validity threats -->
> Identify threats to the validity of your experimental conclusions BEFORE running experiments. Pre-registering threats forces honest assessment and prevents post-hoc rationalization of limitations. Threats identified here inform design mitigations; threats discovered after execution become limitations.
>
> Categories follow standard empirical research methodology. Not all categories apply to every project — mark N/A with a one-sentence justification.
<!-- /REQUIREMENT -->

<!-- INSTANCE: fill per project -->
| Category | Threat | Severity | Planned Mitigation |
|---|---|---|---|
| **Internal validity** (confounds, measurement) | {{What could cause a spurious result?}} | HIGH/MED/LOW | {{Design decision to address it}} |
| **External validity** (generalization) | {{Why might results not generalize?}} | HIGH/MED/LOW | {{How §8c addresses this, or acknowledged limit}} |
| **Construct validity** (measurement fit) | {{Are we measuring what we claim?}} | HIGH/MED/LOW | {{Validation approach}} |
| **Statistical conclusion** (power, multiple testing) | {{Could statistical issues mislead?}} | HIGH/MED/LOW | {{How §7 addresses this}} |
<!-- /INSTANCE -->

**Self-test:** For each HIGH threat, do you have a corresponding mitigation in the design? If not, either add one or acknowledge it as a known limitation in FINDINGS.md.

**Confound detection self-test (S70 impulse #6):** Are your independent variable and your most threatening alternative explanation correlated in your dataset? If they are perfectly correlated (every observation where IV=A also has alternative=X, and every IV=B has alternative=Y), your data CANNOT distinguish between them regardless of sample size or statistical power. State explicitly: "IV [name] and alternative [name] are {independent / partially correlated / perfectly confounded} because {reason}." If confounded, design a discriminating condition that breaks the correlation, or acknowledge it as an unresolvable limitation.

---

## 9a) External Validation Structure

<!-- source: Track 1, U3/priority 2 — 6-7/7 papers -->

> **Purpose:** Identify at least one validation mechanism INDEPENDENT of your own
> analysis. Self-assessed results, no matter how rigorous, are vulnerable to shared
> biases in the researcher's analytical pipeline. Breakthrough research consistently
> uses external validation: blind competitions (AlphaFold → CASP), natural experiments
> (Chetty → Moving to Opportunity), physical constraints (Bell → spacelike separation),
> formal proofs (Watermark → information-theoretic bounds), independent replication
> (GNoME → external lab synthesis), or objective measurement (Milkman → gym swipe data).

<!-- INSTANCE: fill per project -->
**Primary external validation:**

| Validation type | Mechanism | Why independent of your analysis |
|---|---|---|
| {{blind competition / natural experiment / physical constraint / formal proof / independent replication / objective measurement / other}} | {{Specific mechanism — name the competition, experiment, constraint, etc.}} | {{Explain why this mechanism cannot be influenced by your analytical choices}} |

**Dual identification** [SEED: require 2 methods; sunset after 3 projects if researchers
consistently can only identify 1 — reduce to 1 with justification]:

| # | Independent verification method | What it validates |
|---|---|---|
| 1 | {{METHOD_1}} | {{Which claim(s) this independently verifies}} |
| 2 | {{METHOD_2}} | {{Which claim(s) this independently verifies}} |

> If you cannot identify ANY external validation mechanism, this is a design gap — not
> a limitation to note later. Consider:
> - Can results be submitted to a blind evaluation (competition, shared task, holdout)?
> - Does a natural experiment or quasi-experiment exist that tests the same hypothesis?
> - Can an independent team replicate your core finding with their own pipeline?
> - Can you derive formal bounds that your empirical results must satisfy?
> - Can you replace self-reported outcomes with objective measurement?
>
> "None — this is purely exploratory" is valid for pilot studies but caps the
> contribution at preliminary evidence.

**Self-test:** If your primary claim were wrong, would your external validation mechanism
catch it? If the answer is "no" or "maybe," the validation is not truly independent —
identify what shared assumptions could let a false result pass both your analysis AND
your external check.
<!-- /INSTANCE -->

---

## 10) Design Review Checklist (Gate 0.5)

<!-- REQUIREMENT: pre-compute design verification -->
All items must be checked before Phase 1 compute begins.
<!-- /REQUIREMENT -->

| # | Requirement | Status | Notes |
|---|------------|--------|-------|
| 1 | Novelty claim stated in ≤25 words | [ ] | |
| 2 | ≥N comparison baselines identified (N per venue tier) | [ ] | |
| 3 | Baseline fairness documented: each baseline has tuning parity statement (A4) | [ ] | |
| 4 | ≥2 reviewer kill shots with mitigations | [ ] | |
| 5 | Ablation plan with hypothesized effects | [ ] | |
| 6 | Novel component isolation test designed: novel claim tested independently (A5) | [ ] | |
| 7 | Ground truth audit: sources, lag, positive rate | [ ] | |
| 8 | Alternative label sources considered | [ ] | |
| 9 | Statistical plan: seeds, tests, CIs | [ ] | |
| 10 | Related work: ≥N papers (N per venue tier) | [ ] | |
| 11 | Hypotheses pre-registered in HYPOTHESIS_REGISTRY | [ ] | |
| 12 | lock_commit set in HYPOTHESIS_REGISTRY | [ ] | |
| 13 | Target venue identified | [ ] | |
| 14 | ≥2 structurally diverse evaluation conditions specified (A3) | [ ] | |
| 15 | Cross-domain validation protocol completed: principle + mapping + prediction + boundaries (A2) | [ ] | |
| 16 | This document committed before any training script | [ ] | |

| 17 | Assumption challenged: field-held assumption named + ≥2 papers + contradiction search (A8) | [ ] | |
| 18 | Compute resources documented: hardware, runtime, cost (A12) | [ ] | |
| 19 | Threats to validity identified with planned mitigations (§9) | [ ] | |
| 20 | External validation mechanism identified: ≥1 independent verification method (§9a) | [ ] | |
| 21 | Time-to-outcome feasibility: primary outcome measurable within research timeline, or intermediate outcome identified (§0) | [ ] | |
| 22 | Data access feasibility: all data sources assessed for access barriers, fallback plans documented (§6a) | [ ] | |
| 23 | Constraint-driven design: ≥3 hardest constraints identified with design choices they drove (§4a) | [ ] | |

**Gate 0.5 verdict:** [ ] PASS / [ ] FAIL

> **If FAIL:** Do not begin Phase 1 compute. Resolve gaps and re-review.

---

## 11) Compute Resources

<!-- REQUIREMENT: compute transparency -->
> Required for all venue submissions. Document hardware, runtime, and cost so others can assess reproducibility feasibility. Venues increasingly require this (checklist item at major conferences). Documenting low-cost compute is a feature — it demonstrates accessibility.
<!-- /REQUIREMENT -->

<!-- INSTANCE: fill per project -->
| Resource | Specification |
|----------|--------------|
| Hardware | {{CPU/GPU model, RAM, cloud provider/SKU or local machine}} |
| Total runtime | {{hours of compute, broken down by experiment phase}} |
| Estimated cost | {{$ at current cloud pricing, or $0 if local}} |
| Carbon estimate | {{optional: kg CO2 equivalent — use ML CO2 Impact calculator if available}} |
| Reproducibility note | {{Can someone reproduce this on commodity hardware? What's the minimum viable setup?}} |
<!-- /INSTANCE -->
> **If PASS:** Proceed to Phase 1. This document becomes the design contract — deviations must be logged in DECISION_LOG with rationale.

---

## 12) Tier 2+ Depth Escalation (R34)

<!-- REQUIREMENT: depth requirements for competitive venue submission -->
> **Required for Tier 2 and Tier 1 venues only.** Skip for Workshop targets.
> Planned here at design time. Verified at Phase 3 exit before submission.
>
> Depth commitment: ONE primary finding. All experiments validate this finding across multiple settings. "Breadth over depth" is the #1 rejection reason.
>
> Evaluation settings must be structurally diverse per A3 (§8c).
<!-- /REQUIREMENT -->

### Depth Commitment

<!-- INSTANCE: fill per project -->
**Primary finding (one sentence):** {{PRIMARY_FINDING}}

**Evaluation settings (minimum 2):**

| # | Setting | How It Differs from Setting 1 | What It Tests |
|---|---------|------------------------------|---------------|
| 1 | {{SETTING_1}} | Baseline setting | Core result |
| 2 | {{SETTING_2}} | {{DIFFERENCE}} | {{WHAT_IT_TESTS}} |
<!-- /INSTANCE -->

### Mechanism Analysis Plan

For each major finding, how will you explain WHY?

| Finding | Proposed Mechanism | Experiment to Verify |
|---------|-------------------|---------------------|
| {{FINDING_1}} | {{MECHANISM_1}} | {{EXPERIMENT_1}} |

### Adaptive Adversary Plan (security papers only)

| Robustness Claim | Weak Test (baseline) | Adaptive Test (attacker knows defense) |
|-----------------|---------------------|---------------------------------------|
| {{CLAIM_1}} | {{WEAK_TEST}} | {{ADAPTIVE_TEST}} |

### Formal Contribution Statement (draft)

We contribute:
1. {{CONTRIBUTION_1}}
2. {{CONTRIBUTION_2}}
3. {{CONTRIBUTION_3}}

### Published Baseline Reproduction Plan

| Published Method | Their Benchmark | Our Reproduction Plan |
|-----------------|----------------|----------------------|
| {{METHOD_1}} | {{BENCHMARK_1}} | {{REPRO_PLAN_1}} |

### Parameter Sensitivity Plan (G-5)

| Parameter | Sweep Values | Expected: Finding Robust? |
|-----------|-------------|--------------------------|
| {{PARAM_1}} | {{VALUES_1}} | {{EXPECTED_1}} |

### Simulation-to-Real Validation Plan (G-4, simulation projects only)

> **R34 requirement (updated):** "Pending with a plan" is NOT sufficient for Tier 2+. FP-16 proved simulation-to-real gap can be 48pp. Budget real experiments at design time.

| Simulation Finding | Real-System Validation | API Cost Estimate | Timeline |
|-------------------|----------------------|-------------------|----------|
| {{FINDING_1}} | {{VALIDATION_1}} | {{COST_1}} | {{TIMELINE_1}} |

**Total real-system validation budget: ${{TOTAL_COST}}**

### Defense Harm Test (Lesson from FP-16)

> **Required for any project proposing a defense.** FP-16 showed the LLM-as-judge defense made things WORSE (+3pp poison from false positives). Before reporting defense effectiveness, verify the defense does not hurt.

**Mandatory first experiment:** Run "full defense" vs "no defense" and confirm:
- [ ] Defense poison/error rate ≤ no-defense baseline
- [ ] If defense is net-negative, report this as a FINDING, not a bug

### Qualitative Prediction Validation (Lesson from FP-15)

> FP-15 simulation said topology doesn't matter. Real agents showed a 17pp spread. The PATTERN changed, not just the magnitude.

For each simulation finding, validate BOTH:
- [ ] Quantitative prediction (how much effect?)
- [ ] Qualitative prediction (does this factor matter at all?)

### Simulation Calibration Note

> Historical calibration: FP-15/FP-16 showed 37-48pp simulation overestimate. Plan for effect sizes 30-50% smaller than simulation predicts. Do NOT set success thresholds based on simulation magnitudes.

### Formalization Attempt (R34.8)

> Can your primary finding be expressed as a testable quantitative relationship?

**Finding to formalize:** {{PRIMARY_FINDING}}

**Formalization type** (choose one):
- [ ] Predictive model (features → outcome, report R² and CV RMSE)
- [ ] Decision boundary (when does X help vs hurt?)
- [ ] Calibration formula (simulation → real correction factor)
- [ ] Threat model (quantified success conditions)
- [ ] Not formalizable — explain why: {{EXPLANATION}}
  - What additional data would make it formalizable: {{DATA_NEEDED}}

| Project Type | Appropriate Formalization | NOT Appropriate |
|---|---|---|
| Taxonomy/measurement | Predictive model from features | Fitting to <5 data points |
| Defense evaluation | Decision boundary | R² on binary outcome |
| Simulation study | Calibration model | Predicting from 3 conditions |
| Attack research | Threat model with conditions | Regression on categories |

### Depth Escalation Checklist

| # | Requirement | Status |
|---|------------|--------|
| 1 | ONE primary finding identified | [ ] |
| 2 | ≥2 evaluation settings designed | [ ] |
| 3 | Mechanism analysis planned for each major claim (including nulls) | [ ] |
| 4 | Adaptive adversary test planned (security papers) | [ ] |
| 5 | Formal contribution statement drafted | [ ] |
| 6 | ≥1 published baseline reproduction planned | [ ] |
| 7 | Parameter sensitivity sweep planned | [ ] |
| 8 | Simulation-to-real validation planned (simulation projects) | [ ] |
| 9 | Formalization attempted or explained why not | [ ] |

---

## 13) Phase 1 Exit Checkpoint (Mid-Execution Verification)

> **When:** After Phase 1 experiments complete, before Phase 2-3 analysis begins.
> **Purpose:** Catch deviations from design before analysis starts. (Gap E-1)

| # | Check | Status | Deviation? |
|---|-------|--------|------------|
| 1 | All comparison baselines from §3 were implemented and run | [ ] | |
| 2 | Seed count matches statistical plan from §7 | [ ] | |
| 3 | All ablation components from §5 were tested | [ ] | |
| 4 | Ground truth sources from §6 were used as planned | [ ] | |
| 5 | Any deviations logged in DECISION_LOG with rationale | [ ] | |
| 6 | Experiment outputs exist for all planned conditions | [ ] | |
| 7 | test_measurements.py exists and passes (R46) | [ ] | |
| 8 | E0a/E0b/E0c sanity checks passed (R47) | [ ] | |
| 9 | E0 results saved to outputs/experiments/e0_* | [ ] | |

**If any deviation:** Log in DECISION_LOG as `DESIGN_DEVIATION` with rationale. Update this document's relevant section. Do NOT silently skip planned experiments.

> **Cross-reference:** For real-time deviation logging and execution quality gates during Phase 1, see [EXECUTION_PROTOCOL](EXECUTION_PROTOCOL.tmpl.md) §1 (quality gates) and §5 (deviation log). This checkpoint verifies post-hoc; EXECUTION_PROTOCOL captures in real time.

---

## 14) E0: Sanity Validation Design (R47)

> **Run BEFORE E1.** Verifies measurement pipeline works on known inputs.

| Check | Known Input | Expected Output | Purpose |
|---|---|---|---|
| E0a: Positive control | {{KNOWN_POSITIVE_INPUT}} | {{EXPECTED_POSITIVE_OUTPUT}} | Measurement detects what it should |
| E0b: Negative control | {{KNOWN_NEGATIVE_INPUT}} | {{EXPECTED_NEGATIVE_OUTPUT}} | Measurement doesn't false-positive |
| E0c: Dose-response | {{INTENSITY_LEVELS}} | Monotonic AND non-trivial (not all identical) | Measurement scales correctly AND discriminates between levels |

E0 must pass before E1-E6 run. Results saved to `outputs/experiments/e0_results.json`. Report in FINDINGS "Sanity Validation" section.

> **E0c discrimination rule:** If all dose-response values are identical (e.g., all 1.0), E0c has NOT demonstrated the measurement scales correctly — it has only demonstrated a ceiling/floor effect. Choose intensity levels that span the measurement's dynamic range. If the measurement saturates, that is a finding about the measurement, not a PASS.

---

## 15) Phase 3 Writing Checklist (R48/R49)

> **Run after FINDINGS.md is complete, before publication.**

| # | Check | Status |
|---|-------|--------|
| 1 | FINDINGS.md has all required sections (Hypothesis, Negative, Content Hooks, Limitations, Related Work, Contribution) | [ ] |
| 2 | Blog draft ≥ 1000 words (R25) | [ ] |
| 3 | Blog reflects FINDINGS — no "preliminary", "pending", "TBD" (R48) | [ ] |
| 4 | Figures generated and embedded in blog | [ ] |
| 5 | validate_content.sh passes | [ ] |
| 6 | FINDINGS timestamp ≤ blog timestamp — no staleness (R49) | [ ] |
| 7 | check_all_gates.sh: 0 FAIL (R50) | [ ] |

---

## Venue Tier Reference

| Requirement | Workshop / BSides | Tier 2 (AISec, AAAI-W) | Tier 1 (NeurIPS, USENIX) |
|-------------|------------------|------------------------|--------------------------|
| Comparison baselines | ≥1 | ≥2 | ≥3 including SOTA |
| Seeds | ≥3 | ≥5 | ≥5 with bootstrap CIs |
| Ablation depth | 1 group | All major groups | All groups + interactions |
| Related work | ≥3 papers | ≥5 papers | ≥10 papers, positioned |
| Ground truth sources | ≥1 | ≥2 | ≥2 with agreement analysis |
| Kill shots | ≥1 | ≥2 | ≥3 with formal responses |
| Evaluation settings | 1 | ≥2 | ≥3 |
| Mechanism analysis | Optional | Required for major claims | Required for all claims |
| Adaptive adversary | Optional | Required if robustness claimed | Required + certified bounds |
| Published baseline repro | Optional | ≥1 method reproduced | ≥2 methods on their benchmarks |
| Contribution statement | Informal | "We contribute: (1)...(2)...(3)..." | Formal + verified against sections |
| Parameter sensitivity | Optional | Required (key params) | Required + robustness analysis |
| Simulation-to-real | N/A | ≥1 real experiment or plan | Required with empirical validation |

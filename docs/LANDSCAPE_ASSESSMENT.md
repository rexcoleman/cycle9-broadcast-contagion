# LANDSCAPE ASSESSMENT

<!-- version: 0.1 -->
<!-- created: {{DATE}} -->
<!-- stage: 2 -->
<!-- methodology_status: partial — stages 0-2 methodology from Phase B.1 -->

> **Purpose:** Force systematic landscape mapping before hypothesis formation.
> Prevent "I'll test X" without "here's what's been done and where the gap is."
> This template defines WHAT to document about the landscape, not HOW to conduct
> a systematic review. The middle loop discovers process.

---

## §0 Search Protocol

<!-- gate:landscape_assessment §0 required -->

Document the search methodology used for this landscape assessment.

| Field | Value |
|---|---|
| **Databases queried** | {{LIST_DATABASES}} |
| **Search terms** | {{LIST_TERMS}} |
| **Date range** | {{START_DATE — END_DATE}} |
| **Inclusion criteria** | {{WHAT_WAS_INCLUDED}} |
| **Exclusion criteria** | {{WHAT_WAS_EXCLUDED}} |
| **Total results screened** | {{COUNT}} |
| **Results included** | {{COUNT}} |

<!-- /gate:landscape_assessment §0 -->

> Document what you actually did, not what an ideal search would look like.
> This section enables reproducibility: another researcher could repeat your search.

---

## §1 Prior Work Inventory

<!-- gate:landscape_assessment §1 entries:5 -->

| # | Reference | What It Does | Methodology | Key Results | Limitations | Relevance to Our Question |
|---|---|---|---|---|---|---|
| 1 | {{CITATION}} | {{DESCRIPTION}} | {{METHOD}} | {{RESULTS}} | {{LIMITATIONS}} | {{RELEVANCE}} |
| 2 | {{CITATION}} | {{DESCRIPTION}} | {{METHOD}} | {{RESULTS}} | {{LIMITATIONS}} | {{RELEVANCE}} |
| 3 | {{CITATION}} | {{DESCRIPTION}} | {{METHOD}} | {{RESULTS}} | {{LIMITATIONS}} | {{RELEVANCE}} |
| 4 | {{CITATION}} | {{DESCRIPTION}} | {{METHOD}} | {{RESULTS}} | {{LIMITATIONS}} | {{RELEVANCE}} |
| 5 | {{CITATION}} | {{DESCRIPTION}} | {{METHOD}} | {{RESULTS}} | {{LIMITATIONS}} | {{RELEVANCE}} |

<!-- /gate:landscape_assessment §1 -->

> [SEED: min_prior_works=5]
> Structure borrowed from PRIOR_WORK_REUSE assessment pattern.
> Each row is one prior work relevant to the research question from
> RESEARCH_QUESTION_SPEC §0. Focus on methodology and limitations —
> these reveal where the gap is.

### §1.1 Benchmark as Landscape

<!-- source: Track 1, gap matrix Stage 2 -->

| Question | Answer |
|---|---|
| Does a standardized competition, benchmark, or shared evaluation exist for this problem? | {{yes / no}} |
| If yes: what does the current state-of-the-art show? What is the gap between the best result and what would be practically useful? | {{ANSWER}} |
| If no: why not? What does the absence tell you about the field's maturity or the question's novelty? | {{ANSWER}} |

> AlphaFold: CASP was THE landscape — a blind competition that standardized
> evaluation across groups and made the gap between methods visible. GNoME:
> Materials Project was THE benchmark database. Milkman: no benchmark existed
> for comparing behavioral interventions — the incomparability of existing
> studies WAS the problem, and creating a shared evaluation WAS the contribution.
>
> **Self-test:** If a benchmark exists and you're not using it, justify why.
> If no benchmark exists, ask whether creating one IS your contribution
> (as Milkman's megastudy was). If benchmarks exist but measure the wrong
> thing, that gap may itself be worth addressing.

---

## §1b Adjacent Field Survey

<!-- source: Track 1, U2/priority 1 — 7/7 papers -->

Name 2 fields outside your own that face analogous problems.

| # | Adjacent field | Analogous problem they face | Method they use | Have they solved something you haven't? | Could you import their method? |
|---|---|---|---|---|---|
| 1 | {{FIELD}} | {{PROBLEM}} | {{METHOD}} | {{yes: what / no: why not}} | {{yes: how / no: why not}} |
| 2 | {{FIELD}} | {{PROBLEM}} | {{METHOD}} | {{yes: what / no: why not}} | {{yes: how / no: why not}} |

> [SEED: min_adjacent_fields=2]
> All 7 breakthrough papers in Track 1 imported methods from other fields:
> AlphaFold imported attention mechanisms from NLP. Chetty imported shrinkage
> estimators from biostatistics. Bell imported nanowire detectors from materials
> science. Milkman imported multi-arm trial design from clinical medicine.
> Watermark imported hash-based partitioning from cryptography.
>
> **Important:** This section covers cross-domain imports planned at DESIGN time
> (before the research runs). FINDINGS §Cross-Domain Connections covers cross-domain
> connections discovered DURING analysis (after the research runs). Both are valuable
> — this section is proactive, that section is reflective. They are NOT duplicates.
>
> **Self-test:** If both fields are sub-disciplines of your own, you haven't gone
> far enough. Chetty imported from biostatistics, not from another economics
> subfield. Bell imported from materials science, not from another physics subfield.

---

## §2 Gap Map

<!-- gate:landscape_assessment §2 entries:1 -->

| # | Gap Description | Gap Type | Evidence | Opportunity Size |
|---|---|---|---|---|
| 1 | {{GAP_DESCRIPTION}} | {{nobody tried / tried and failed / tried with wrong method / tried in wrong domain}} | {{EVIDENCE_OF_GAP}} | {{OPPORTUNITY_ASSESSMENT}} |

<!-- /gate:landscape_assessment §2 -->

> [SEED: min_gaps=1]
> Gap types from spec §1:
> - Nobody tried: no prior work addresses this
> - Tried and failed: prior work attempted but didn't succeed (cite the failure)
> - Tried with wrong method: prior work used an approach with known limitations
> - Tried in wrong domain: solved elsewhere but not applied here

---

## §2b Fragmentation Diagnosis

<!-- source: Track 1, gap matrix Stage 2 -->

| Question | Answer |
|---|---|
| Does evidence for your question exist in incomparable forms across studies? | {{yes / no}} |
| If yes: what makes them incomparable? (different populations, methods, metrics, timeframes, instruments) | {{ANSWER}} |
| If yes: what would make them comparable? | {{ANSWER}} |
| Is making evidence comparable the real contribution? | {{yes: this is a methodology contribution / no: the evidence gap is the contribution}} |

> Milkman's key insight: behavioral interventions were tested by different labs,
> on different populations, with different outcome measures and timeframes.
> Cross-study comparison was meaningless. The megastudy design — testing 54
> interventions simultaneously on 61,293 participants with one objective outcome
> — WAS the contribution, not the exercise results themselves.
>
> Chetty faced a different form: mobility estimates existed at coarse geographic
> levels with incompatible methodologies across studies. The Atlas created
> comparable estimates at fine resolution using a single methodology on
> population-scale administrative data.
>
> **Self-test:** If evidence fragmentation is severe, the highest-impact
> contribution may be creating comparable evidence, not adding one more
> incomparable study to the pile.

---

## §3 Baseline Knowledge State

| Category | What We Know |
|---|---|
| **Known with confidence** | {{ESTABLISHED_FINDINGS}} |
| **Uncertain** | {{CONFLICTING_OR_INCOMPLETE_EVIDENCE}} |
| **Contested** | {{ACTIVELY_DEBATED_CLAIMS}} |

> Prevents treating the landscape as "everything is unknown." Some things
> are established. Documenting what IS known focuses the research question
> on genuine gaps.

---

## §4 Frontier Moat Test

<!-- gate:landscape_assessment §4 required -->

Structure borrowed from PROJECT_BRIEF §2b.

| Question | Answer |
|---|---|
| **Novelty check:** <5 similar projects on GitHub/arXiv? | {{NOVELTY_ANSWER}} |
| **Timing check:** What changed in the last 6 months enabling this? | {{TIMING_ANSWER}} |
| **Moat check:** What stops a funded competitor replicating in 1 month? | {{MOAT_ANSWER}} |

<!-- /gate:landscape_assessment §4 -->

> All 3 questions must be answered (not placeholder). The Landscape Gate
> validates each row is filled.

---

## §5 Cross-Engine Research Context

<!-- gate:landscape_assessment §5 required -->

Query the cross-engine view for prior research cycles, claim confidence levels,
and published content relevant to this landscape.

```
Run: sqlite3 ~/singularity.db "SELECT * FROM v_landscape_inputs;"
Paste results below:
```

{{V_LANDSCAPE_INPUTS_RESULTS}}

<!-- /gate:landscape_assessment §5 -->

---

## §6 EDA Readiness

> **Conditional:** Required for computational research types. Optional for synthesis.
> If synthesis, write "N/A — synthesis research type" and proceed.

| Field | Value |
|---|---|
| **Research type** | {{computational / synthesis}} |
| **Available data sources** | {{LIST_DATA_SOURCES}} |
| **EDA needed before hypothesis formation?** | {{yes / no}} |
| **EDA scope** | {{WHAT_EDA_WOULD_COVER}} |
| **Link to DATA_CONTRACT §6** | {{PATH_OR_N/A}} |

> For computational research: data-level inputs inform hypothesis quality.
> This section bridges to DATA_CONTRACT §6 for EDA methodology.

### Data Source Sample Verification

<!-- source: Phase E cycle 2 DEV-4 — CSET "10 harm categories" assumption was wrong at execution -->

For each data source listed above, download a sample (≥10 rows or entries) and
verify that field names, data types, and category counts match your assumptions.
Report actual vs assumed. Mismatches here become deviations (EP §5) at execution.

| Data source | Assumed structure | Actual (from sample) | Match? |
|---|---|---|---|
| {{SOURCE_1}} | {{ASSUMED_FIELDS_AND_CATEGORIES}} | {{ACTUAL_AFTER_INSPECTION}} | {{yes/no — if no, note what differs}} |

> [SEED: This check was added because S59 cycle 2 assumed CSET had "10 neat harm
> categories" but execution found the data was structured differently (DEV-4).
> The categorization axis changed from CSET harm types to ATLAS tactics —
> fundamentally altering what the chi-squared test measured. A 10-row sample
> inspection during landscape assessment would have caught this before design.]

---

## §6b Handoff to Hypothesis

<!-- source: Track 1, gap matrix Stage 2→3 interface -->

Summarize for Stage 3 (EXPERIMENTAL_DESIGN §0). This section bridges landscape
mapping to experimental design.

**Prior work frontier** (3 strongest works and their specific limitations):

| # | Prior work | Its specific limitation that your work addresses |
|---|---|---|
| 1 | {{CITATION}} | {{LIMITATION}} |
| 2 | {{CITATION}} | {{LIMITATION}} |
| 3 | {{CITATION}} | {{LIMITATION}} |

**Method import opportunities** (from §1b Adjacent Field Survey):

{{Summarize the most promising importable methods and which adjacent fields they come from}}

**Gap type and design implication** (from §2 Gap Map):

{{Gap type}}: {{What this gap type tells you about the experimental approach — "tried with wrong method" implies method innovation; "nobody tried" implies feasibility demonstration; "tried in wrong domain" implies domain transfer}}

**Landscape signals for design:**

| Signal | Status | Implication for experimental design |
|---|---|---|
| Benchmark/competition (§1.1) | {{exists / absent}} | {{IMPLICATION}} |
| Evidence fragmentation (§2b) | {{fragmented / comparable}} | {{IMPLICATION}} |

> This section is consumed by EXPERIMENTAL_DESIGN §0 (Problem Selection Gate).
> If this section is empty, the design stage starts without landscape context —
> the researcher must re-derive what was already mapped here.
>
> **Self-test:** Could someone read ONLY this section and know enough to start
> designing an experiment? If not, what's missing?

### §6b.1 Cross-Domain Mechanism Validity Pre-Check

<!-- source: S75 audit — C7 shock dilution vs replication mismatch caught at Stage 5, not Stage 2 -->
<!-- gate:landscape mechanism_validity entries:1 -->

For each method import identified in §1b and §6b above:

| Import | Core mechanism in source domain | Analog in target domain | Does mechanism OPERATE the same way? | Evidence |
|---|---|---|---|---|
| {{IMPORT}} | {{SOURCE_MECHANISM}} | {{TARGET_ANALOG}} | {{YES / NO / UNKNOWN}} | {{CITATION_OR_REASONING}} |

> If **NO** for any core mechanism: the import is a FINDING to investigate,
> not an assumption to design around. Pre-register the mechanism mapping
> as a hypothesis (HYPOTHESIS_REGISTRY) and design the experiment to TEST
> whether the mechanism transfers.
>
> If **UNKNOWN**: the landscape search is incomplete for this import.
> Search for evidence of the mechanism operating in the target domain
> before proceeding to design.
>
> [SEED: require 1 entry per import from §1b. Sunset after 5 projects
> if mechanism validity never changes a design decision.]

---

## §7 Landscape Gate Checklist

Self-assessment before proceeding to Stage 3 (Hypothesize).

| # | Check | Status | Notes |
|---|---|---|---|
| 1 | Search protocol documented in §0 (databases, terms, date range) | [ ] | |
| 2 | ≥5 prior works inventoried in §1 | [ ] | |
| 3 | ≥1 gap identified in §2 with type and evidence | [ ] | |
| 4 | Baseline knowledge state filled in §3 | [ ] | |
| 5 | All 3 Frontier Moat Test questions answered in §4 | [ ] | |
| 6 | Cross-engine context queried in §5 (not placeholder) | [ ] | |
| 7 | EDA readiness addressed in §6 (if computational) | [ ] | |
| 8 | Mechanism validity assessed for each cross-domain import in §6b.1 | [ ] | |

> Gate script (`landscape_gate.sh`) validates checks 1-3, 5-6 as FAIL level.
> Check 4 is WARN level. Check 7 is CONDITIONAL (FAIL for computational, skip for synthesis).

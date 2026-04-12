# OBSERVATION LOG

<!-- version: 0.1 -->
<!-- created: {{DATE}} -->
<!-- stage: 0 -->
<!-- methodology_status: partial — stages 0-2 methodology from Phase B.1 -->

> **Purpose:** Force systematic observation before questioning. Prevent
> "I have a hypothesis" without "I noticed something first." This template
> defines WHAT to log, not HOW to observe. The middle loop discovers process.

---

## §0 Signal Sources

<!-- gate:observation_log §0 entries:2 -->

List the source types scanned during this observation period.

| # | Source Type | Description | Date Range Scanned |
|---|---|---|---|
| 1 | {{SOURCE_TYPE}} | {{DESCRIPTION}} | {{DATE_RANGE}} |
| 2 | {{SOURCE_TYPE}} | {{DESCRIPTION}} | {{DATE_RANGE}} |

<!-- /gate:observation_log §0 -->

> [SEED: min_source_types=2]
> Minimum 2 distinct source types (e.g., community, literature, industry, DB signals).

---

## §1 Observations

<!-- gate:observation_log §1 entries:3 -->

| # | Date | Source | Observation | Classification | Intensity |
|---|---|---|---|---|---|
| OBS-1 | {{DATE}} | {{SOURCE}} | {{OBSERVATION}} | {{pain / opportunity / anomaly / trend}} | {{1-5}} |
| OBS-2 | {{DATE}} | {{SOURCE}} | {{OBSERVATION}} | {{pain / opportunity / anomaly / trend}} | {{1-5}} |
| OBS-3 | {{DATE}} | {{SOURCE}} | {{OBSERVATION}} | {{pain / opportunity / anomaly / trend}} | {{1-5}} |

<!-- /gate:observation_log §1 -->

> [SEED: min_observations=3]
> Each observation gets a unique ID (OBS-N) for traceability from RESEARCH_QUESTION_SPEC §1.
> Classification: pain (someone has a problem), opportunity (something became possible),
> anomaly (something unexpected), trend (directional shift).
> Intensity: 1 (background noise) to 5 (urgent/high-magnitude).

### §1.1 Question Lineage

<!-- source: Track 1, U1/priority 1 — 7/7 papers. Phase I G4: research program continuity. -->

**Pipeline research frontiers — query FIRST before external search:**

```
Run: sqlite3 ~/singularity.db "SELECT id, cycle_id, limitation_text, suggested_next_question FROM limitations_next_questions WHERE status='open' ORDER BY cycle_id DESC;"
Paste results below:
```

{{LIMITATIONS_QUERY_RESULTS}}

> Open limitations from prior cycles are the pipeline's own research frontiers.
> Consider addressing one before starting a fresh topic.

For each observation above, trace it backward to the prior work whose limitation
makes this observation significant:

| OBS-# | What limitation of prior work (yours or the field's best) does this observation connect to? | Prior work reference |
|---|---|---|
| {{OBS-N}} | {{LIMITATION}} | {{CITATION_OR_PROJECT}} |

> Every breakthrough question in Track 1 research emerged from a prior answer's
> limitation, not from fresh observation alone. AlphaFold: CASP showed template-free
> targets at GDT ~40/100 — existing methods failed on the hardest cases. Chetty: own
> 2014 QJE showed mobility varies by commuting zone (~740K people) — resolution was
> too coarse for policy. Bell: Aspect 1982 closed the locality loophole but left the
> detection loophole open.
>
> **Self-test:** If you can't name the prior work whose limitation this observation
> connects to, either (a) the observation is genuinely novel ground — document why no
> prior work is relevant, or (b) you haven't searched far enough backward.

---

## §1b Technology Readiness Scan

<!-- source: Track 1, gap matrix Stage 0/priority 2 partial -->

For each observation in §1 with intensity ≥3, answer:

| OBS-# | What changed recently (new data, new tool, new technique, new access) that makes this observation actionable NOW? | When did this enabler become available? |
|---|---|---|
| {{OBS-N}} | {{ENABLER}} | {{DATE_OR_PERIOD}} |

> [SEED: tech_readiness_intensity_threshold=3]
> Observations are not actionable just because they're interesting. Something must
> have changed to make the question answerable NOW that it wasn't before.
> AlphaFold: deep learning made template-free structure prediction feasible (CASP
> existed for decades). Chetty: IRS-Census linked records newly available at scale.
> Bell: SNSPDs reached required detection efficiency (>90%).
>
> **Self-test:** If "what changed" is "nothing — the question was always answerable,"
> ask why nobody answered it. Either something DID change (you haven't identified it)
> or the question is harder than you think.

---

## §1c Cross-Field Method Scan

<!-- source: Track 1, U2/priority 1 — 7/7 papers -->

Before proceeding to Stage 1 (Question), scan for cross-domain methods:

| Observation cluster | Analogous field 1 | Their method | Analogous field 2 | Their method |
|---|---|---|---|---|
| {{PATTERN_FROM_§3}} | {{FIELD}} | {{METHOD}} | {{FIELD}} | {{METHOD}} |

> [SEED: min_analogous_fields=2]
> All 7 breakthrough papers in Track 1 imported methods from other fields.
> AlphaFold: attention mechanisms from NLP. Chetty: shrinkage estimators from
> biostatistics. Bell: nanowire detectors from materials science. Milkman:
> multi-arm trial design from clinical medicine.
>
> **Important:** This section prompts for cross-domain import as a DESIGN input
> (before the research runs). FINDINGS §Cross-Domain Connections covers connections
> discovered DURING analysis (after the research runs). Both are valuable — this is
> proactive, that is reflective. They are NOT duplicates.
>
> **Self-test:** If both fields you name are sub-disciplines of your own, you haven't
> gone far enough. Chetty imported from biostatistics, not from another economics
> subfield. Bell imported from materials science, not from another physics subfield.

---

## §2 Cross-Engine Context

<!-- gate:observation_log §2 required -->

Query the cross-engine view for recent signals, distribution gaps, killed experiment
learnings, and strategy findings relevant to this observation period.

```
Run: sqlite3 ~/singularity.db "SELECT * FROM v_observation_inputs;"
Paste results below:
```

{{V_OBSERVATION_INPUTS_RESULTS}}

<!-- /gate:observation_log §2 -->

---

## §3 Pattern Notes

<!-- gate:observation_log §3 entries:1 -->

| # | Pattern | Supporting Observations | Surprising? | Contradicts Prior Assumption? |
|---|---|---|---|---|
| PAT-1 | {{PATTERN_DESCRIPTION}} | {{OBS-N, OBS-M, ...}} | {{yes / no}} | {{yes: [which assumption] / no}} |

<!-- /gate:observation_log §3 -->

> [SEED: min_patterns=1]
> Record what patterns you see across observations. Reference observation IDs.

---

## §4 Observation Gate Checklist

Self-assessment before proceeding to Stage 1 (Question).

| # | Check | Status | Notes |
|---|---|---|---|
| 1 | ≥2 distinct source types in §0 | [ ] | |
| 2 | ≥3 observations logged in §1 | [ ] | |
| 3 | Cross-engine context queried in §2 (not placeholder) | [ ] | |
| 4 | ≥1 pattern noted in §3 | [ ] | |
| 5 | Most recent observation within last 90 days | [ ] | |
| 6 | No single source type accounts for all observations | [ ] | |

> Gate script (`observation_gate.sh`) validates checks 1-4 mechanically.
> Checks 5-6 are advisory (WARN level).

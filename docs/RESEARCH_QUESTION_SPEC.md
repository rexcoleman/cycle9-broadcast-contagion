# RESEARCH QUESTION SPEC

<!-- version: 0.1 -->
<!-- created: {{DATE}} -->
<!-- stage: 1 -->
<!-- methodology_status: partial — stages 0-2 methodology from Phase B.1 -->

> **Purpose:** Force question formation from observations, not from intuition alone.
> Prevent "I want to study X" without "here's the gap that makes X worth studying."
> This template defines WHAT to document about a research question, not HOW to
> formulate one. The middle loop discovers process.

---

## §0 Question Statement

### §0a Paradigm Challenge — Start Here

<!-- source: Phase I Gap Research (G1+G7), Track 1 (5/7 papers) -->

Before writing your question, answer these two prompts. They set the framing
for everything that follows. Skipping them and writing a conventional question
first creates confirmatory framing that §4.1 and §4.2 cannot fix after the fact.

**1. What does the field currently believe that might be wrong?**
{{FIELD_ASSUMPTION_TO_CHALLENGE}}

> Name a specific assumption — not a gap. A gap is "nobody has measured X."
> An assumption challenge is "everyone assumes X is true, but what if it's not?"
> VAR: "Autoregressive must use raster-scan order." Bell: "Loopholes can be closed
> one at a time." Milkman: "Interventions should be tested one at a time."
> If you cannot name an assumption to challenge, your question is confirmatory —
> it will score N=5. That's acceptable for some research, but name it honestly.

**2. Lakatos test — does your question predict a novel fact or accommodate a known one?**

| Test | Answer |
|---|---|
| **If I run this study, could the result go EITHER WAY?** | {{yes/no}} |
| **Would an expert in this field be SURPRISED by any possible outcome?** | {{yes/no/maybe — name the expert}} |
| **Am I applying a KNOWN method to a NEW domain where the general result is expected?** | {{yes/no — if yes, this is "normal science" and N ceiling is 5}} |

> A "yes, no, yes" pattern = confirmatory research. The result accommodates what's
> already known rather than predicting something new. This is Lakatos' "degenerating
> research programme" — not wrong, but N-capped. To shift toward progressive: reverse
> one of the field's assumptions (prompt 1) and design around the reversal.

**Research question:** {{ONE_SENTENCE_QUESTION}}

> Must trace to ≥1 observation in OBSERVATION_LOG §1.
> Must be answerable with data or experiments — not opinion or external validation.
> Must be informed by your §0a paradigm challenge — if you challenged an assumption,
> the question should test that challenge.

---

## §1 Observation Link

<!-- gate:research_question_spec §1 entries:1 -->

| # | Observation ID | Source (from OBSERVATION_LOG) | Signal/Pattern Quoted |
|---|---|---|---|
| 1 | {{OBS-N}} | {{SOURCE}} | {{QUOTE_FROM_OBSERVATION_LOG}} |

<!-- /gate:research_question_spec §1 -->

> [SEED: min_linked_observations=1]
> Link to specific observation IDs from OBSERVATION_LOG §1.
> Quote the signal or pattern that motivated this question.

### §1.1 Question Lineage

<!-- source: Track 1, U1/priority 1 — 7/7 papers -->

**Required field:** What specific limitation of the best prior work defines this
question? Cite the prior work and quote its stated limitation or boundary.

| Prior work (citation) | Its stated limitation or boundary | How your question addresses this limitation |
|---|---|---|
| {{CITATION}} | {{QUOTED_LIMITATION}} | {{YOUR_QUESTION'S_RELATIONSHIP}} |

> The observation in §1 connects to a signal; this field traces the signal to a
> specific prior work's boundary. The most impactful research questions emerge from
> the frontier of what's already known, not from blank space.
>
> Chetty: "Chetty & Hendren 2014 measured mobility at commuting-zone level
> (~740K people); this question escalates precision 100× to census-tract level
> (~4,250 people)." Bell: "Aspect 1982 closed the locality loophole but left the
> detection loophole open; this experiment closes both simultaneously."
> VAR: "Autoregressive image generation uses raster-scan ordering borrowed from
> NLP; this work replaces it with multi-scale ordering native to images."
>
> **Self-test:** Can you quote the prior work's own stated limitation? If they
> didn't state one, what boundary did they implicitly stop at? If you can't identify
> a specific boundary, your question may not be building on the frontier — it may be
> parallel to existing work rather than advancing beyond it.

---

## §2 Alternatives Considered

<!-- gate:research_question_spec §2 entries:2 -->

For each alternative research question considered, document using ADR-adapted format:

### Alternative 1

| Field | Content |
|---|---|
| **Context** | {{WHAT_PROMPTED_THIS_ALTERNATIVE}} |
| **Alternative question** | {{THE_ALTERNATIVE_QUESTION}} |
| **Why rejected** | {{REASON_FOR_REJECTION}} |
| **Consequences of rejection** | {{WHAT_WE_LOSE_BY_NOT_PURSUING_THIS}} |

### Alternative 2

| Field | Content |
|---|---|
| **Context** | {{WHAT_PROMPTED_THIS_ALTERNATIVE}} |
| **Alternative question** | {{THE_ALTERNATIVE_QUESTION}} |
| **Why rejected** | {{REASON_FOR_REJECTION}} |
| **Consequences of rejection** | {{WHAT_WE_LOSE_BY_NOT_PURSUING_THIS}} |

<!-- /gate:research_question_spec §2 -->

> [SEED: min_alternatives=2]
> Structure borrowed from DECISION_LOG ADR format.
> Each alternative is a question you COULD have asked instead of the one in §0.
> The purpose is to demonstrate the chosen question was selected, not assumed.

### Adjacent Question Mapping

<!-- source: Track 1, gap matrix Stage 1 -->

Beyond the alternatives you naturally considered above, name 1 additional question
adjacent to yours that you deliberately chose not to pursue. What specific evidence
made your chosen question higher-impact?

| Adjacent question not pursued | What you'd lose by pursuing it instead | Evidence your chosen question is higher-impact |
|---|---|---|
| {{ADJACENT_QUESTION}} | {{COST_OF_PURSUING}} | {{EVIDENCE}} |

> This extends the alternatives analysis to the broader question space. §2's
> alternatives are different framings of the SAME problem. This prompt asks about
> a DIFFERENT problem nearby that competes for attention. The purpose: prevent
> drift to the most convenient question rather than the highest-impact one.

### Boundary-Spanning Feasibility Check

<!-- source: Phase E cycle 2 learning — BS=4 when method analog is from same domain -->

Does this research question naturally require importing methods from OUTSIDE the
primary domain? If the closest methodological analog is from the same field (e.g.,
ATT&CK coverage mapping applied to ATLAS coverage mapping — both cybersecurity),
the Boundary-Spanning (BS) ceiling is ~5. Cross-domain import at the QUESTION level
(not just citation level) is what drives BS above 5.

| Check | Answer |
|---|---|
| **Closest methodological analog** | {{METHOD_AND_FIELD}} |
| **Is the analog from a different domain than your research?** | {{yes/no — if no, BS ceiling is ~5}} |
| **What genuine cross-domain import could strengthen the question?** | {{IMPORT_OR_NONE}} |

> [SEED: BS_ceiling_threshold=5 for same-domain method analogs. Calibrated from
> S59 cycle 2: governance framework analysis imported ATT&CK methodology (same
> field) → BS=4. B.3 biology imported network science (different field) → BS=6.]

### Formulation-Level Predetermination Check

<!-- source: Phase F v2, cycle A' — BS=5 despite genuine cross-domain import -->

Even if the method is from a genuinely different domain, check whether its
mathematical formulation makes the result a function of the same variable
you're comparing against.

| Check | Answer |
|---|---|
| **What is the imported method's core mathematical relationship?** | {{e.g., beta_k = beta * k (infection rate proportional to degree)}} |
| **What variable does this relationship depend on?** | {{e.g., node degree}} |
| **Is that variable the same as (or monotonic function of) your comparison metric?** | {{yes/no — if yes, result is predetermined by construction}} |
| **If yes: what alternative formulation would NOT be predetermined?** | {{e.g., community-structured model where beta depends on community membership}} |

> [SEED: formulation_predetermination_ceiling=5. Calibrated from cycle A':
> SEIR HMF sets beta_k = beta * k on power-law DAG → rankings proportional to
> degree by construction → rho = 1.000 across ALL 12 ablation configurations →
> BS=5 despite genuine cross-domain import (epidemiology -> software security).
> The existing same-domain check (above) would have PASSED this case.]

### Import Depth Verification

<!-- source: Phase I Gap Research (G2) — 7/7 breakthrough papers engaged deeply with source domain -->

If your question imports a method from another domain, verify the import is
substantive — not just borrowing a tool name or output format.

| Depth Check | Answer |
|---|---|
| **What conceptual FRAMEWORK from the source domain are you engaging with?** | {{FRAMEWORK — not the tool name}} |
| **How did you ADAPT it for your target domain's constraints?** | {{ADAPTATION}} |
| **What would a specialist in the SOURCE domain recognize in your work?** | {{RECOGNITION}} |

> [SEED: import_depth_floor=3_checks. If any check is blank or "N/A",
> the import is surface-level — BS ceiling is ~5.]
>
> AlphaFold: engaged attention mechanism THEORY (not "used transformers"),
> adapted for residue co-evolution (triangle attention), crystallographers
> recognize the output as structure prediction. All 3 substantive.
> Cycle 2 (BS=4): borrowed coverage scoring PATTERN, did not engage
> ATT&CK's threat modeling FRAMEWORK, a specialist would see the same
> domain's vocabulary applied adjacently. 0/3 substantive.

---

## §3 Gap Identification

<!-- gate:research_question_spec §3 entries:1 -->

| # | Gap Description | Evidence of Gap | Gap Type |
|---|---|---|---|
| 1 | {{WHAT_IS_NOT_KNOWN}} | {{CITATION_OR_EVIDENCE}} | {{nobody tried / tried and failed / tried with wrong method / tried in wrong domain}} |

<!-- /gate:research_question_spec §3 -->

> [SEED: min_gap_citations=1]
> Cite specific evidence: a paper that stops short, a tool that doesn't exist,
> a problem that remains unsolved. "No one has done X" requires evidence that
> you searched and didn't find it.

---

## §3b Precision Escalation

<!-- source: Track 1, U4/priority 2 — 4/7 papers (UNDER-EVIDENCED) -->

> [SEED: precision_escalation — 4/7 evidence, likely universal but under-evidenced]
> This methodology prompt is based on 4 of 7 breakthrough papers studied (AlphaFold,
> Chetty, Bell, VAR). The remaining 3 (Watermark, GNoME, Milkman) posed new questions
> rather than escalating existing ones. The evidence base is weaker than U1 (7/7) or
> U2 (7/7) — treat this as a strong candidate pattern, not a confirmed universal.
> Phase B should validate with additional papers before encoding with full confidence.

State the current best version of this question as answered by the field's strongest
prior work:

| Current best answer in the field | Its precision / resolution / scale | Source |
|---|---|---|
| {{BEST_CURRENT_ANSWER}} | {{PRECISION_LEVEL}} | {{CITATION}} |

What 10× increase in precision, resolution, or scale would transform this question's
impact?

| Dimension escalated | Current level | Your target level | Why this transformation matters |
|---|---|---|---|
| {{precision / resolution / scale / speed / coverage}} | {{CURRENT}} | {{TARGET}} | {{IMPACT}} |

> Chetty escalated geographic resolution 100× (commuting zone → census tract).
> Bell escalated experimental rigor (close ALL loopholes simultaneously, not one
> at a time). AlphaFold escalated accuracy on the hardest cases (GDT ~40 → 92.4
> on template-free targets).
>
> **Self-test:** If your question is the same as the current best but with more data,
> it's a scale-up — valuable but not a new question. If it asks something the current
> best CAN'T answer at ANY scale, it's a new question. Which is yours? Both are valid
> research directions, but they require different designs and make different claims.

---

## §4 Assumption Challenge

<!-- gate:research_question_spec §4 entries:1 -->

| # | Assumption the Field Holds | Sources Holding This Assumption | Contradiction Search Results | Why It Might Be Wrong |
|---|---|---|---|---|
| 1 | {{SPECIFIC_ASSUMPTION}} | {{PAPER_1, PAPER_2}} | {{WHAT_YOU_SEARCHED_FOR_AND_FOUND}} | {{ONE_SENTENCE_CHALLENGE}} |

<!-- /gate:research_question_spec §4 -->

> [SEED: min_papers_cited=2]
> Structure borrowed from EXPERIMENTAL_DESIGN Gate -1 A8 pattern.
> Name a specific assumption, cite ≥2 sources that hold it, document your
> search for contradicting evidence, and state why it might be wrong.
> "None found after searching [X], [Y]" is a valid contradiction search result.

### §4.1 Paradigm Challenge Assessment

<!-- source: Track 1, priority 2 — 5/7 papers -->

What methodological assumption does the field hold unquestioned? What happens if
you reverse it?

| Unquestioned assumption | What reversal looks like | What changes in your approach if reversed |
|---|---|---|
| {{ASSUMPTION}} | {{REVERSAL}} | {{CONSEQUENCE}} |

> VAR: "Autoregressive generation must proceed token-by-token in raster order" →
> reversed to "autoregressive by SCALE, not by position." Bell: "Loopholes can be
> closed one at a time in separate experiments" → reversed to "all loopholes must
> be closed simultaneously in one experiment." Milkman: "Behavioral interventions
> should be tested one at a time by individual labs" → reversed to "test 54
> simultaneously in one megastudy."
>
> **Self-test:** If reversing this assumption doesn't change your approach, it's not
> a paradigm challenge — it's a conventional question. That's fine, but name it
> honestly. Conventional questions produce incremental advances. Paradigm challenges
> produce surprises. Both are needed; the experimental design differs.

### §4.2 Novelty Pre-Mortem

<!-- source: Phase F v2, N=5 in 3/3 cycles across 3 domains -->

Before proceeding: score your question's answer predictability.

| Level | Description | N Ceiling | Action |
|---|---|---|---|
| UNPREDICTABLE | No existing theory predicts the outcome. Expert consensus would disagree on the answer. | >=6 | Proceed. |
| PARTIALLY PREDICTABLE | Existing theory suggests the direction but not magnitude/specifics. | 5-6 | Produce 1 alternative question that targets the UNPREDICTABLE component. Document the trade-off. Coach reviews both before design proceeds. |
| PREDICTABLE | Existing theory, prior empirical work, or mathematical properties of the chosen method predict the outcome. An expert in the source domain could derive the answer without running the experiment. | <=5 | STOP. Produce 2 alternative questions that shift the answer into unpredictable territory. Re-run §2 comparison with alternatives. |

Self-score: {{PREDICTABILITY_LEVEL}}

If PREDICTABLE or PARTIALLY PREDICTABLE, what is the specific theory, result, or
mathematical property that makes the answer predictable?
{{PREDICTABILITY_SOURCE}}

If PREDICTABLE: produce 2 alternative questions that shift the answer into
unpredictable territory:

| # | Alternative question | Why unpredictable | Trade-off vs current question |
|---|---|---|---|
| 1 | {{ALT_QUESTION}} | {{WHY_UNPREDICTABLE}} | {{TRADEOFF}} |
| 2 | {{ALT_QUESTION}} | {{WHY_UNPREDICTABLE}} | {{TRADEOFF}} |

If PARTIALLY PREDICTABLE: produce 1 alternative question that shifts the
unpredictable component into the primary question frame:

| Alternative question | What makes it less predictable | Trade-off vs current question |
|---|---|---|
| {{ALTERNATIVE}} | {{UNPREDICTABLE_COMPONENT}} | {{TRADEOFF}} |

The purpose is NOT to abandon the current question — it's to force articulation
of a less-confirmatory alternative. The Coach or RP reviews both and selects
the stronger framing.

> [SEED: predictability_threshold=PARTIALLY_PREDICTABLE triggers 1 alternative,
> PREDICTABLE triggers 2 alternatives. Both require mandatory revision.
> Calibrated from 3 cycles: C1 gap predictable in retrospect (N=5), C2 result
> in pre-registered range (N=5), C3 Pastor-Satorras & Vespignani 2001 predicted
> SEIR degenerates on scale-free networks (N=5). All 3 would have scored
> PREDICTABLE on this scale. Post-Phase-B: 4/4 cycles scored PARTIALLY
> PREDICTABLE with no action triggered — this threshold added S75.]
>
> **Self-test:** If you scored UNPREDICTABLE, name one expert who would be
> SURPRISED by the answer. If you can't name one, reconsider your score.

---

## §5 Pipeline Signal Connection

<!-- gate:research_question_spec §5 required -->

Query the cross-engine view for scored hypotheses, capability gaps, and signal
clusters relevant to this question.

```
Run: sqlite3 ~/singularity.db "SELECT * FROM v_question_inputs;"
Paste results below:
```

{{V_QUESTION_INPUTS_RESULTS}}

<!-- /gate:research_question_spec §5 -->

---

## §6 Question Gate Checklist

Self-assessment before proceeding to Stage 2 (Landscape).

| # | Check | Status | Notes |
|---|---|---|---|
| 1 | Question statement in §0 is one sentence and traceable to observation | [ ] | |
| 2 | ≥1 observation linked in §1 with direct quote | [ ] | |
| 3 | ≥2 alternatives documented in §2 with rejection rationale | [ ] | |
| 4 | ≥1 gap cited with evidence in §3 | [ ] | |
| 5 | ≥2 papers cited in §4 assumption challenge | [ ] | |
| 6 | Pipeline signal connection queried in §5 (not placeholder) | [ ] | |
| 7 | §4.2 Novelty Pre-Mortem completed — if PREDICTABLE, alternatives provided | [ ] | |

> Gate script (`question_gate.sh`) validates checks 1-4, 6 as FAIL level.
> Check 5 is WARN level (per spec §3 Gate 1→2 check #6).
> Check 7 is WARN level (new — collecting data before escalating to FAIL).

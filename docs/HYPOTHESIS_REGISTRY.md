# HYPOTHESIS REGISTRY

<!-- version: 1.0 -->
<!-- created: 2026-03-15 -->

> **Authority hierarchy:** {{TIER_1_SOURCE}} (Tier 1) > {{TIER_2_SOURCE}} (Tier 2) > {{TIER_3_SOURCE}} (Tier 3) > This document (Contract)
> **Conflict rule:** When a higher-tier document and this contract disagree, the higher tier wins. Flag the conflict in the DECISION_LOG.
> **Upstream:** DATA_CONTRACT (dataset definitions informing hypothesis scope), METRICS_CONTRACT (metric definitions referenced in predictions)
> **Downstream:** EXPERIMENT_CONTRACT (experiment design grounded in hypotheses), REPORT_ASSEMBLY_PLAN (hypothesis statements and resolution templates), FINDINGS (hypothesis resolution narratives and evidence references)

## Pre-Registration Lock

**Lock commit:** {{GIT_SHA — fill BEFORE running any experiments}}
**Lock date:** {{DATE}}

> **Temporal gate (LL-74):** All hypotheses must be committed and locked before any experimental results are generated. Any experiment output with a git timestamp before the lock commit is invalid. Verify: `git log --oneline HYPOTHESIS_REGISTRY.md | tail -1` should predate all experiment outputs.

---

## Customization Guide

| Placeholder | Description | Example |
|-------------|-------------|---------|
| `{{MIN_HYPOTHESES}}` | Minimum number of pre-registered hypotheses | `2` |
| `{{HYPOTHESIS_TABLE}}` | The populated hypothesis registry table | See §3 template |
| `{{TIER1_DOC}}` | Tier 1 authority document | Project requirements spec |
| `{{TIER2_DOC}}` | Tier 2 authority document | FAQ or clarifications document |
| `{{TIER3_DOC}}` | Tier 3 authority document | Course TAs' Piazza clarifications |

---

## 1) Pre-Registration Protocol

Hypotheses MUST be written **before** Phase 1 experiments begin.

**Gate:** >= {{MIN_HYPOTHESES}} hypotheses (default: 2) registered and committed to version control before any experiment script is executed.

**Enforcement:**
- The hypothesis registry file MUST have a git commit timestamp earlier than any experiment output file.
- Adding hypotheses after seeing results is an academic integrity violation.
- Amendments to existing hypotheses (e.g., refining a threshold) MUST be tracked via `CONTRACT_CHANGE` commits with justification.

---

## 2) Hypothesis Format

Each hypothesis MUST include all fields in the following schema:

| Field | Description | Example |
|-------|-------------|---------|
| `hypothesis_id` | Sequential identifier | H-1, H-2, ... |
| `statement` | Clear, falsifiable statement | "Random Forest will outperform Decision Tree on balanced accuracy by >= 5pp on both datasets" |
| `falsification_criterion` | What evidence would reject this hypothesis | "RF balanced accuracy is < DT balanced accuracy + 5pp on either dataset" |
| `metric` | Quantitative threshold for support/rejection | `balanced_accuracy >= DT_balanced_accuracy + 0.05` |
| `resolution` | Final status | `SUPPORTED` / `REFUTED` / `INCONCLUSIVE` / `PENDING` |
| `evidence` | Reference to specific output file + metric value | `outputs/part1/adult/rf/summary.json → bal_acc=0.87 vs DT 0.79` |
| `field_surprise` | What would surprise THE FIELD (not just you) about this hypothesis's resolution? This captures field-level surprise per hypothesis. Per-experiment surprise criteria are in EXPERIMENTAL_DESIGN §8a — this field captures per-hypothesis field-level surprise, a different granularity. | "If mobility effects persist beyond childhood exposure, it contradicts the critical-period consensus in developmental economics" |
| `expert_prediction` | [SEED: optional field; promote to required after 3 projects if expert predictions consistently diverge from results — evidence of field-level surprise value. Sunset if predictions consistently match results.] Have 1-3 domain experts predict the outcome of this hypothesis before execution. Record their predictions and reasoning. Compare after results. | "Expert A: SUPPORTED (80% confidence, cites prior trend). Expert B: REFUTED (60%, cites measurement concerns)" |

<!-- source: Track 1, gap matrix Stage 3/priority 3 — 3/7 papers (Bell, Watermark, Milkman) -->

> **field_surprise vs EXPERIMENTAL_DESIGN §8a:** ED §8a captures what would surprise
> YOU at the experiment level ("If Experiment 1 shows X, I'd be surprised"). This field
> captures what would surprise THE FIELD at the hypothesis level ("If H-1 resolves as
> SUPPORTED, it contradicts the dominant assumption in [subfield]"). Both are needed —
> researcher-level surprise drives follow-up experiments, field-level surprise drives
> novelty and impact.
>
> Milkman: expert predictions were uncorrelated with actual intervention effects — the
> field's priors were systematically wrong. Bell: the field expected quantum mechanics
> to hold, but the STRENGTH of the violation (11.5σ) surprised even proponents.
> Chetty: neighborhood effects at tract level were expected to matter, but social
> variables outpredicting economic variables surprised the field.
>
> **Self-test:** If your field_surprise answer is "nothing — this is expected," your
> hypothesis may be confirmatory rather than novel. That's valid (replications matter)
> but caps the novelty contribution. If you can't articulate what would surprise the
> field, you may not know the field's current beliefs well enough — revisit your
> landscape assessment.

**Statement quality rules:**
- Statements MUST be falsifiable. "Model X will perform well" is not acceptable.
- Statements MUST reference a specific metric and threshold (absolute or relative).
- Statements MUST specify the comparison (vs baseline, vs another model, vs chance).

---

## 3) Registry Table

{{HYPOTHESIS_TABLE}}

**Template (copy and populate):**

| hypothesis_id | statement | falsification_criterion | metric | field_surprise | resolution | evidence |
|---------------|-----------|------------------------|--------|---------------|------------|----------|
| H-1 | *(statement)* | *(criterion)* | *(threshold)* | *(what would surprise the field?)* | PENDING | — |
| H-2 | *(statement)* | *(criterion)* | *(threshold)* | *(what would surprise the field?)* | PENDING | — |

---

## 4) Resolution Protocol

After experiments complete, revisit **every** hypothesis and assign a resolution:

| Resolution | Criteria |
|------------|----------|
| **SUPPORTED** | Metric meets or exceeds the stated threshold across all specified conditions |
| **REFUTED** | Metric falls below the stated threshold |
| **INCONCLUSIVE** | Ambiguous results (e.g., supported on one dataset but not another), insufficient data, or metric within noise margin (+/-1 std of threshold) |

**Resolution rules:**
- Every hypothesis MUST be resolved before Phase N+2 begins.
- The `evidence` field MUST reference a specific output file path and the exact metric value.
- INCONCLUSIVE resolutions MUST include a brief explanation of why the result is ambiguous.
- Resolutions are final once committed. A later experiment cannot retroactively change a resolution (register a new hypothesis instead).

---

## 5) Acceptance Criteria

- [ ] >= {{MIN_HYPOTHESES}} hypotheses registered before Phase 1
- [ ] All hypotheses follow the required format (all 7 required fields populated; `expert_prediction` optional)
- [ ] All hypotheses resolved (no PENDING status at project end)
- [ ] Every resolution includes an evidence reference to a specific output file
- [ ] No hypothesis was added after experiment results were observed (verified by git timestamps)
- [ ] Resolution narrative for each hypothesis included in FINDINGS.md

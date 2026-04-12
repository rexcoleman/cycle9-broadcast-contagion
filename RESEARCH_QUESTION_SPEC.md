# RESEARCH QUESTION SPEC

<!-- version: 0.1 -->
<!-- created: 2026-04-12 -->
<!-- stage: 1 -->
<!-- methodology_status: partial — stages 0-2 methodology from Phase B.1 -->

> **Purpose:** Force question formation from observations, not from intuition alone.
> Prevent "I want to study X" without "here's the gap that makes X worth studying."
> This template defines WHAT to document about a research question, not HOW to
> formulate one. The middle loop discovers process.

---

## §0 Question Statement

**Research question:** In software supply chain networks with broadcast-type attack propagation, does detection coverage (version pinning, signature verification, SBOM scanning) create an effective phase transition threshold — and if so, what is the critical coverage fraction below which containment fails?

### §0a Paradigm Challenge — Start Here

<!-- source: Phase I Gap Research (G1+G7), Track 1 (5/7 papers) -->

**1. What does the field currently believe that might be wrong?**

The field currently believes that software supply chain attack propagation can be modeled using contagion frameworks where the "shock" or "infection" divides across downstream consumers — analogous to financial contagion where losses are shared among counterparties (Acemoglu et al. 2015), or biological epidemics where pathogen load dilutes through contact (standard SIS/SIR). This assumption appears across supply chain risk models that borrow from financial systemic risk or basic compartmental epidemiology. But software supply chain attacks REPLICATE without dilution: every consumer of a compromised package receives the full malicious payload, not a fraction. The Shai-Hulud npm worm (2025) demonstrated this empirically — each compromised package pushed full malicious payloads to all its consumers, creating broadcast-type propagation. Our Cycle 7 results confirmed the mismatch computationally: under deterministic (non-diluting) propagation, the Acemoglu shock-dilution framework produced near-zero cascades — an artifact of the wrong mechanism, not actual containment.

The deeper assumption challenge: the supply chain security field treats detection coverage (SBOMs, signature verification, version pinning) as a binary compliance target — either you have it or you don't, and more is linearly better. What if detection coverage exhibits a THRESHOLD effect — a phase transition below which no amount of incremental coverage improvement matters, and above which containment becomes rapidly effective? This would overturn the "every percentage point of SBOM adoption helps equally" framing that dominates current policy recommendations (CISA SBOM guidance, NIST SP 800-161r1, OWASP Supply Chain Security).

**2. Lakatos test — does your question predict a novel fact or accommodate a known one?**

| Test | Answer |
|---|---|
| **If I run this study, could the result go EITHER WAY?** | Yes. SIS+recovery theory predicts a threshold CAN exist, but whether real-world supply chain detection rates (~15-30% SBOM adoption per MITRE/NTIA surveys) are above or below the critical fraction is unknown. The threshold could be at 5% (making current adoption sufficient for hub-targeted strategies) or at 60% (making current adoption catastrophically inadequate). |
| **Would an expert in this field be SURPRISED by any possible outcome?** | Yes — a network epidemiologist would be surprised if broadcast contagion with realistic detection rates shows NO threshold (contradicting SIS+recovery theory). A supply chain security practitioner would be surprised if the threshold is dramatically lower than current compliance targets suggest (implying hub-targeted detection at 10-15% coverage suffices). Both surprise scenarios are plausible. |
| **Am I applying a KNOWN method to a NEW domain where the general result is expected?** | Partially. The existence of a threshold is predicted by theory, but the LOCATION of the threshold relative to real detection rates, and whether hub-targeting changes the threshold by an order of magnitude, are genuinely unknown. The method (broadcast contagion + heterogeneous recovery on realistic supply chain topologies) has never been applied to this domain. This is NOT pure method application — it requires adapting broadcast models to handle detection/recovery mechanisms that have no analog in the source domain. |

> Assessment: The Lakatos pattern is "yes, partially-yes, partially" — NOT the confirmatory "yes, no, yes" pattern. The existence of a threshold is partially predictable from theory, but the quantitative answer (where the threshold falls relative to real-world parameters) and the qualitative answer (whether hub-targeting creates an order-of-magnitude efficiency gain) are genuinely unknown. This places the question at PARTIALLY PREDICTABLE with meaningful unpredictable components.

**Research question:** In software supply chain networks with broadcast-type attack propagation, does detection coverage (version pinning, signature verification, SBOM scanning) create an effective phase transition threshold — and if so, what is the critical coverage fraction below which containment fails?

> Traces to OBS-1 (Cycle 7 dilution mechanism mismatch), OBS-2 (vanishing threshold restored by heterogeneous recovery), OBS-3 (Shai-Hulud broadcast containment), and PAT-1 (recovery mechanism IS the research opportunity).

---

## §1 Observation Link

<!-- gate:research_question_spec §1 entries:1 -->

| # | Observation ID | Source (from OBSERVATION_LOG) | Signal/Pattern Quoted |
|---|---|---|---|
| 1 | OBS-1 | Cycle 7 Finding 5 + limitations_next_questions #5 | "Acemoglu financial contagion's shock dilution mechanism (effective_severity = severity / out_degree) fundamentally mismodels software supply chain attacks where payloads replicate without dilution to ALL dependents. Under deterministic propagation, cascades collapsed to near-zero — an artifact of the wrong mechanism, not actual defense effectiveness." |
| 2 | OBS-2 | Pastor-Satorras & Vespignani 2001 + SIS heterogeneous recovery literature | "Introducing heterogeneous recovery rates (where high-degree nodes recover faster, analogous to better-monitored packages having faster detection) can RESTORE an effective threshold." |
| 3 | OBS-3 | Shai-Hulud npm worm incident (Sysdig, PaloAlto, Microsoft) | "The first self-propagating supply chain worm... reached ~500 package versions before containment... containment succeeded only through rapid detection + token revocation (a recovery mechanism)." |
| 4 | PAT-1 | Pattern from §3 | "The recovery mechanism IS the research opportunity, not just a validity concern... The gap between theory (no threshold) and practice (containment happens) means detection/recovery mechanisms create an effective threshold that no existing model captures." |

<!-- /gate:research_question_spec §1 -->

### §1.1 Question Lineage

**Required field:** What specific limitation of the best prior work defines this question?

| Prior work (citation) | Its stated limitation or boundary | How your question addresses this limitation |
|---|---|---|
| Cycle 7 (our pipeline), Finding 5 | "Acemoglu shock dilution mechanism does not model software supply chain attack propagation — attacks replicate rather than divide." Limitation #5 in limitations_next_questions. | Replaces the diluting-shock propagation mechanism with broadcast (non-diluting) contagion, directly answering: "What contagion framework correctly models replicating attacks?" |
| Pastor-Satorras & Vespignani, PRL 86(14), 2001 | Proved vanishing epidemic threshold for SIS on scale-free networks but assumed HOMOGENEOUS recovery rates and no detection/removal mechanism beyond spontaneous recovery. The model has no analog for targeted detection or heterogeneous monitoring. | Introduces heterogeneous detection coverage as a recovery mechanism on realistic supply chain topologies, testing whether it restores a threshold that their homogeneous model eliminates. |
| Cohen et al., PRL 91, 247901, 2003 | Computed critical immunization fraction for scale-free networks but in a STATIC percolation framework — no dynamics, no propagation speed, no time-dependent detection. | Tests whether the percolation-predicted immunization threshold holds under dynamic broadcast propagation with time-dependent detection, where propagation speed and detection latency create a race condition absent from static percolation. |

> **Self-test:** All three prior works have identifiable boundaries. Cycle 7 stated its limitation explicitly. Pastor-Satorras & Vespignani's boundary is implicit in their model assumptions (homogeneous recovery). Cohen et al.'s boundary is the static/dynamic gap. This question sits at the intersection of all three frontiers: non-diluting propagation (C7) + heterogeneous recovery (P-S&V) + dynamic threshold (Cohen).

---

## §2 Alternatives Considered

<!-- gate:research_question_spec §2 entries:2 -->

### Alternative 1

| Field | Content |
|---|---|
| **Context** | Cycle 7 limitation #6 asks: "How does temporal evolution of supply chain topology affect the phase-transition threshold?" This is a natural extension of C7. |
| **Alternative question** | Does temporal evolution of supply chain network topology (package creation/deprecation, dependency updates) shift the phase-transition threshold for broadcast contagion containment? |
| **Why rejected** | This question PRESUPPOSES a working broadcast contagion + detection model, which does not yet exist. Limitation #6 is an extension that assumes a correct base model. Without first establishing whether detection coverage creates a threshold at all (this cycle's question), testing temporal effects adds precision to a potentially wrong framework. The dependency ordering is: correct propagation mechanism THEN temporal effects. |
| **Consequences of rejection** | We cannot assess real-world applicability where topologies change daily. However, if the base model shows no threshold even with detection, temporal effects are moot. If a threshold exists, temporal effects become the natural Cycle 10 question. |

### Alternative 2

| Field | Content |
|---|---|
| **Context** | OBS-5 and PAT-2 suggest hub-targeted detection may be exponentially more efficient than uniform detection. This could be the primary question rather than a parameter of the threshold question. |
| **Alternative question** | In software supply chain networks under broadcast attack propagation, does hub-targeted detection deployment achieve containment at coverage fractions an order of magnitude lower than uniform deployment? |
| **Why rejected** | This question is narrower — it asks about the targeting strategy but presupposes the existence of a containment threshold. The broader question (does a threshold exist, and where is it?) necessarily includes the hub-targeting comparison as a parameter. Asking the threshold question first produces the hub-targeting answer as a sub-result, while the hub-targeting question alone cannot establish whether a threshold exists under uniform coverage. |
| **Consequences of rejection** | The hub-targeting comparison becomes a secondary analysis within the broader question rather than the primary finding. This may dilute the practitioner message (hub-targeting is more actionable than "a threshold exists at X%"). However, establishing the threshold first provides the theoretical foundation that makes the hub-targeting recommendation principled rather than ad hoc. |

<!-- /gate:research_question_spec §2 -->

### Adjacent Question Mapping

| Adjacent question not pursued | What you'd lose by pursuing it instead | Evidence your chosen question is higher-impact |
|---|---|---|
| "Can multiplex network models (limitation #8) reveal reentrant phase transitions in supply chain attack propagation?" | Multiplex analysis assumes a working single-layer model. Without establishing the broadcast+detection threshold on single-layer networks first, multiplex extensions add structural complexity to an unvalidated base. We'd lose the foundational model that all extensions require. | Limitation #5 (propagation mechanism) is listed as the root issue in C7's limitations; limitations #6-#9 are explicitly noted as "extensions that assume a working base model" in the strategic frame. The dependency chain is clear: fix the mechanism first. |

### Boundary-Spanning Feasibility Check

| Check | Answer |
|---|---|
| **Closest methodological analog** | Daley-Kendall ISS (Ignorant-Spreader-Stifler) rumor spreading model with stifler mechanism on heterogeneous networks — from information epidemiology / mathematical sociology. |
| **Is the analog from a different domain than your research?** | Yes. Information epidemiology (how rumors/misinformation spread through social networks) is a fundamentally different domain from software supply chain security. The substrate differs (ideas in social networks vs. malicious code in dependency graphs), the agents differ (people choosing to spread vs. packages pulled automatically), and the recovery mechanism differs (social stifling vs. technical detection). The structural isomorphism (broadcast replication + stifler/detection recovery) is what makes the import valuable. |
| **What genuine cross-domain import could strengthen the question?** | The ISS stifler mechanism from information epidemiology provides the detection/recovery analog missing from both classical SIS (no stifler) and financial contagion (shock dilution). Additionally, percolation immunization theory from statistical physics provides the analytical framework for computing critical coverage fractions on heterogeneous networks. Both are genuine cross-domain imports — neither information epidemiology nor percolation theory is "supply chain security." |

### Formulation-Level Predetermination Check

| Check | Answer |
|---|---|
| **What is the imported method's core mathematical relationship?** | ISS model: S(t)→I(t) at rate beta (broadcast contact), I(t)→R(t) at rate gamma when spreader contacts another spreader or stifler. On heterogeneous networks, effective beta_k and gamma_k depend on node degree k and detection coverage fraction p. The phase transition occurs at the critical point where the basic reproduction number R_0(p, topology) = 1. |
| **What variable does this relationship depend on?** | Detection coverage fraction p, network topology (degree distribution), and the ratio beta/gamma. The critical threshold p_c is a function of the degree distribution — it depends on the network structure, not just the coverage level. |
| **Is that variable the same as (or monotonic function of) your comparison metric?** | No. We are measuring the LOCATION of p_c (the critical coverage fraction) and how it varies across topologies and targeting strategies. The comparison is between p_c values under different conditions (uniform vs. hub-targeted, different network sizes/types), not between p and degree. The result is NOT predetermined because: (a) p_c's value relative to real-world detection rates is unknown, (b) whether hub-targeting shifts p_c by 2x or 10x depends on the specific topology-detection interaction, which has no closed-form solution for realistic supply chain graphs. |
| **If yes: what alternative formulation would NOT be predetermined?** | N/A — the formulation is not predetermined. However, to further guard against predetermination: we will test whether the threshold sharpness (the steepness of the phase transition) varies across topologies, which is a qualitative feature not predictable from the degree distribution alone. |

### Import Depth Verification

| Depth Check | Answer |
|---|---|
| **What conceptual FRAMEWORK from the source domain are you engaging with?** | The Daley-Kendall ISS framework from information epidemiology — specifically, the theory of how "stifling" (when a spreader encounters resistance) creates a recovery mechanism that competes with broadcast spreading on structured networks. We engage with the ISS phase transition theory: the mathematical framework showing that the stifler density (analogous to detection coverage) acts as a control parameter for a phase transition between local and global contagion regimes. This is the FRAMEWORK, not just "using an ISS model." |
| **How did you ADAPT it for your target domain's constraints?** | Three key adaptations: (1) Replace social "stifling" (voluntary cessation) with technical detection (version pinning, signature verification, SBOM scanning) — stifling in ISS is contact-dependent (requires meeting another stifler), while supply chain detection is TIME-dependent (detected after delay regardless of contacts). This changes the recovery dynamics from contact-proportional to time-proportional. (2) Replace homogeneous broadcast to all contacts with dependency-graph-constrained broadcast — packages only propagate to DOWNSTREAM dependents, not upstream. This introduces directedness absent from ISS models. (3) Replace continuous-time dynamics with discrete version-release events — supply chain propagation happens at package update events, not continuously. |
| **What would a specialist in the SOURCE domain recognize in your work?** | A mathematical epidemiologist studying rumor/misinformation dynamics would recognize: (a) the ISS compartmental structure (Ignorant/Susceptible, Spreader/Infected, Stifler/Recovered), (b) the heterogeneous mean-field formulation for structured populations, (c) the phase transition analysis via basic reproduction number, (d) the competition between broadcast spreading rate and stifler/recovery rate as the mechanism determining endemic vs. extinction regimes. They would also recognize our adaptations as substantive departures from standard ISS — particularly the time-dependent (vs. contact-dependent) recovery and the directed graph constraint. |

---

## §3 Gap Identification

<!-- gate:research_question_spec §3 entries:1 -->

| # | Gap Description | Evidence of Gap | Gap Type |
|---|---|---|---|
| 1 | No existing model captures broadcast (non-diluting) contagion with detection/recovery mechanisms on realistic supply chain network topologies. | Cycle 7 Finding 5: Acemoglu shock dilution produces near-zero cascades under deterministic propagation — wrong mechanism. Pastor-Satorras & Vespignani 2001: SIS on scale-free networks has vanishing threshold but no detection/recovery mechanism. Cohen et al. 2003: percolation immunization is static, no dynamics. Moreno et al. 2004: ISS on complex networks but with contact-dependent stifling, not time-dependent detection. No paper combines broadcast propagation + heterogeneous detection recovery + realistic supply chain topology. | Tried with wrong method (diluting-shock financial contagion applied where broadcast contagion is appropriate) AND tried in wrong domain (ISS rumor models exist but have not been applied to supply chain networks with their specific detection mechanisms). |
| 2 | The critical detection coverage fraction for software supply chain containment is unmeasured. | CISA SBOM guidance and NIST SP 800-161r1 recommend universal SBOM adoption without quantifying what coverage fraction is sufficient or whether a threshold exists. MITRE/NTIA surveys estimate 15-30% current SBOM adoption but provide no model for whether this is above or below a containment threshold. The Shai-Hulud containment (~500 packages in V1, 25,000+ in V2) provides anecdotal evidence that detection speed matters but no quantitative threshold. | Nobody tried — no quantitative model exists for the relationship between detection coverage fraction and supply chain attack containment probability. |
| 3 | Whether hub-targeted detection is orders of magnitude more efficient than uniform detection for supply chain containment is unknown in a dynamic (vs. static percolation) setting. | Cohen et al. 2003 proved targeted immunization is exponentially more efficient in static percolation on scale-free networks. But supply chain attack propagation is dynamic — the race between propagation speed and detection latency may change the targeting advantage. No work extends the Cohen et al. targeted immunization result to dynamic broadcast contagion with time-dependent detection. | Tried in wrong framework (static percolation) — the dynamic version with time-dependent detection has not been tested. |

<!-- /gate:research_question_spec §3 -->

---

## §3b Precision Escalation

| Current best answer in the field | Its precision / resolution / scale | Source |
|---|---|---|
| Pastor-Satorras & Vespignani proved that epidemic threshold vanishes on scale-free SIS networks (any nonzero infection rate leads to endemic persistence). | Qualitative result (threshold exists/vanishes) on idealized network models. No quantification of recovery mechanisms. No mapping to specific detection technologies. | PRL 86(14), 2001 |
| Cohen et al. computed critical immunization fraction for static percolation on scale-free networks. | Analytical result for static node removal. No dynamics, no propagation rate, no detection latency. Formula: p_c ~ 1 - 1/(kappa - 1) where kappa = <k^2>/<k>. | PRL 91, 247901, 2003 |
| Cycle 7 measured phase-transition thresholds for financial contagion on supply chain topologies. | Quantitative thresholds but for the WRONG mechanism (shock dilution). Results not applicable to broadcast propagation. | cycle7-validation FINDINGS.md |

| Dimension escalated | Current level | Your target level | Why this transformation matters |
|---|---|---|---|
| Mechanism fidelity | Diluting-shock (wrong for supply chains) or homogeneous SIS (no detection) | Broadcast contagion + heterogeneous time-dependent detection on realistic supply chain topologies | Transforms from "threshold exists in theory" to "threshold is at X% detection coverage on real-world-parameterized networks" — the first answer practitioners can act on. |
| Topology realism | Idealized scale-free or Erdos-Renyi | npm/PyPI-derived degree distributions with realistic hub structure | Moves from "on idealized networks" to "on networks that look like actual package registries" — closes the gap between theoretical result and practitioner relevance. |
| Detection heterogeneity | Homogeneous (all nodes equal) or binary (immune/susceptible) | Heterogeneous detection probability correlated with degree (high-dependency packages monitored more) | Captures the real-world fact that popular packages are more monitored, testing whether this natural heterogeneity changes the threshold location by an order of magnitude. |

> **Self-test:** This is a genuine precision escalation — the prior best answers CANNOT answer "what detection coverage fraction suffices for containment on realistic supply chain networks?" at ANY scale. The question is new, not a scale-up of an existing answer.

---

## §4 Assumption Challenge

<!-- gate:research_question_spec §4 entries:1 -->

| # | Assumption the Field Holds | Sources Holding This Assumption | Contradiction Search Results | Why It Might Be Wrong |
|---|---|---|---|---|
| 1 | Supply chain attack propagation follows diluting-shock dynamics similar to financial contagion — severity decreases as it spreads across more dependents. | Acemoglu, Ozdaglar & Tahbaz-Salehi (2015) "Systemic Risk and Stability in Financial Networks" (the framework Cycle 7 imported); Hasan et al. (2023) "Analyzing the Supply Chain Attack on AI Models through Financial Contagion Lenses" applies the same dilution logic. | Searched for "supply chain attack propagation dilution" and "software supply chain contagion model without dilution." Found: Shai-Hulud incident reports (Sysdig 2025) explicitly document non-diluting replication. Ohm et al. (2020) "Backstabber's Knife Collection" catalogs supply chain attacks but does not model propagation dynamics. No paper was found that models supply chain attacks with broadcast (non-diluting) propagation + detection recovery. | Software attacks REPLICATE — every downstream consumer gets the full payload, not a fraction. The dilution assumption produces artificially low cascade predictions (Cycle 7 Finding 5: near-zero cascades under deterministic propagation). This is not a modeling simplification; it is a mechanism error that inverts the qualitative behavior. |
| 2 | Detection coverage (SBOM adoption, signature verification) provides LINEAR benefit — each additional percentage point of coverage proportionally reduces risk. | CISA "SBOM Sharing Lifecycle Report" (2024) frames SBOM adoption as a progressive improvement target; NIST SP 800-161r1 recommends universal adoption without discussing threshold effects; Enck & Williams (2022) "Top Five Challenges in Software Supply Chain Security" treats detection as a scaling problem, not a threshold problem. | Searched for "supply chain detection threshold" and "SBOM adoption phase transition" and "critical mass supply chain security." Found: no paper models detection coverage as a phase-transition parameter. The closest is network immunization literature (Cohen et al. 2003) showing threshold effects for vaccination — but this has not been applied to supply chain detection. | If a phase transition exists, the policy implication reverses: below the threshold, incremental adoption has near-zero effect on containment; above it, containment improves rapidly. This means current policy recommendations (gradual universal adoption) may be less effective than concentrated hub-targeted deployment to cross the threshold first. |

<!-- /gate:research_question_spec §4 -->

### §4.1 Paradigm Challenge Assessment

| Unquestioned assumption | What reversal looks like | What changes in your approach if reversed |
|---|---|---|
| "Supply chain security detection coverage should be deployed uniformly across the ecosystem — every package needs an SBOM, every registry needs signature verification." This assumption underlies CISA/NIST/OWASP guidance and treats the ecosystem as homogeneous. | **Reversal:** Detection coverage has a TOPOLOGICAL dimension — deploying detection on 10% of packages (the hubs) may achieve the same containment as deploying on 60% uniformly. The optimal strategy is NOT uniform adoption but targeted deployment following the network's degree distribution. | Our simulation explicitly compares uniform vs. hub-targeted detection deployment strategies across the same total coverage budget. If hub-targeting achieves containment at 5x-10x lower total coverage, this reverses the policy recommendation from "everyone adopt SBOMs" to "prioritize detection on high-dependency packages first." This directly shapes our experimental design: we need both uniform and targeted coverage sweeps across the phase transition region. |

### §4.2 Novelty Pre-Mortem

Self-score: **PARTIALLY PREDICTABLE**

SIS+recovery theory predicts a threshold CAN exist if recovery rate exceeds a critical value dependent on the network's spectral radius. This theoretical prediction means the EXISTENCE of a threshold is partially predictable. However:

- The LOCATION of the threshold (p_c) relative to real-world detection rates (~15-30%) is genuinely unknown
- Whether hub-targeting shifts p_c by 2x or 10x depends on topology-detection interactions with no closed-form solution
- Whether the phase transition is SHARP (useful for policy) or gradual (less actionable) is unknown
- Whether current real-world detection rates are above or below p_c is the most consequential unknown — it determines whether current defenses are adequate or catastrophically insufficient

**Predictability source:** Mean-field SIS theory on heterogeneous networks (Pastor-Satorras & Vespignani 2001) predicts that adding recovery creates a threshold. The spectral radius of the adjacency matrix determines the critical recovery rate. This means a threshold EXISTS — the question is where.

**1 Alternative question (required for PARTIALLY PREDICTABLE):**

| Alternative question | What makes it less predictable | Trade-off vs current question |
|---|---|---|
| "In software supply chain networks, does the phase transition between local and global broadcast contagion exhibit HYSTERESIS — i.e., does the detection coverage fraction required to CONTAIN an active outbreak differ from the fraction required to PREVENT one from starting?" | Hysteresis in epidemic models on heterogeneous networks is a genuinely open theoretical question. Standard mean-field SIS predicts no hysteresis, but heterogeneous recovery rates + broadcast dynamics could create bistability regions where the system's behavior depends on its history, not just current parameters. No existing theory definitively predicts the answer. An expert would disagree: some would predict no hysteresis (mean-field dominates), others would predict hysteresis (finite-size effects + heterogeneous recovery create bistability). | **Gains:** Higher novelty ceiling (N could reach 8-9 if hysteresis is found). More surprising to both network science and supply chain security communities. **Losses:** Harder to parameterize from real-world data. More computationally expensive (requires simulating both containment and prevention trajectories). May not produce actionable practitioner guidance if hysteresis region is narrow. The current question produces a single actionable number (p_c); the hysteresis question produces a range [p_contain, p_prevent] that may confuse policy recommendations. |

> The current question is retained as primary because it produces more actionable practitioner output (a single threshold) while still containing meaningful unpredictable components (threshold location, hub-targeting efficiency). The hysteresis alternative is noted for potential Cycle 10 extension if the base threshold question reveals interesting dynamics near p_c.

---

## §5 Pipeline Signal Connection

<!-- queried: v_question_inputs, 89 rows -->

```
Run: sqlite3 ~/singularity.db "SELECT * FROM v_question_inputs;"
```

**Relevant hypotheses (supply chain and propagation-related):**

| Type | ID | Score | Status | Summary |
|---|---|---|---|---|
| hypothesis | SH-5767 | 1.87 | pending | "Monitoring top 10 agent repos for 30 days detects >3 suspicious supply chain events" — validates that supply chain attacks are persistent, supporting our propagation modeling premise |
| hypothesis | 5733 | 3.51 | pending | "Super-linear cascade with agent count" (multi-agent-security) — related: if cascades are super-linear, phase transition thresholds are more consequential |
| hypothesis | 5766 | 2.33 | pending | "NVIDIA two-of-three constraint achieves comparable cascade reduction to zero-trust with less complexity" — related: architectural containment strategies that may complement detection coverage |

**Relevant capability options:**

| ID | Score | Status | Summary |
|---|---|---|---|
| 46 | 9.5 | open | CLI-based static analysis scanner detecting ML-specific supply chain risks — our detection coverage threshold result would inform what this scanner needs to achieve |
| 44 | 9.0 | open | Cascade poisoning taxonomy — our broadcast contagion model directly feeds the propagation dynamics this taxonomy needs |

**Cross-engine insight:** The pipeline has multiple pending hypotheses about supply chain cascade behavior (SH-5767, H-5733, H-5766) but no quantitative model of broadcast propagation + detection containment. Capability option #46 (supply chain scanner) scored 9.5 — the highest of all capability options — but without a model of how much detection coverage is sufficient, the scanner's design targets are arbitrary. This cycle's threshold result directly informs the scanner's adequacy criteria: if p_c = 0.15, the scanner needs to cover hub packages; if p_c = 0.60, universal coverage is needed.

### §5b Method History

**Methodologies (from pipeline DB, ordered by BS score):**

| Method | Source Domain -> Applied Domain | BS Score |
|---|---|---|
| Acemoglu financial contagion | Mathematical economics -> AI supply chain | 7 |
| Category design classification | Business strategy -> Cold start distribution | 7 |
| Network controllability theory | Network science -> AI security | 6 |
| SEIR/SIR compartmental modeling | Epidemiology -> AI supply chain | 5 |
| ATT&CK coverage mapping | Cybersecurity -> AI security (MITRE ATLAS) | 4 |

**Key lesson:** SEIR scored BS=5 because epidemiology-to-infection-modeling is a shallow import (same conceptual domain). The current cycle imports from INFORMATION epidemiology (rumor/misinformation spreading) — a deeper import because the source domain studies how IDEAS replicate through SOCIAL networks, not how pathogens infect biological hosts. The ISS stifler mechanism, directed-graph adaptations, and time-dependent recovery are substantive adaptations that should push BS above the SEIR precedent. The Acemoglu import scored BS=7 with deep mechanism engagement — this cycle aims for the same depth with a corrected mechanism.

**Recent process improvement proposals:**

| Proposal Type | Target Dimension | Proposed Change |
|---|---|---|
| template_gap | G | Generalizability=5 BELOW THRESHOLD — check boundary statement honesty and inherent method limits (8 instances) |
| question_design | N | Novelty=5 BELOW THRESHOLD — check if answer is predictable before execution (2 instances) |

**Integration:** The N=5 recurrence (question_design proposals) is directly addressed by this spec's §4.2 Novelty Pre-Mortem, which explicitly scores predictability and produces an alternative question. The G=5 recurrence (template_gap proposals) must be addressed in the experimental design: we will include an evaluation conditions table with >=2 structurally diverse conditions and quantified failure mode thresholds per the spec.

---

## §6 Question Gate Checklist

Self-assessment before proceeding to Stage 2 (Landscape).

| # | Check | Status | Notes |
|---|---|---|---|
| 1 | Question statement in §0 is one sentence and traceable to observation | [x] | Single sentence, traces to OBS-1, OBS-2, OBS-3, PAT-1 |
| 2 | >=1 observation linked in §1 with direct quote | [x] | 4 observations linked with direct quotes from OBSERVATION_LOG |
| 3 | >=2 alternatives documented in §2 with rejection rationale | [x] | 2 alternatives (temporal evolution, hub-targeting as primary question) with rejection rationale |
| 4 | >=1 gap cited with evidence in §3 | [x] | 3 gaps cited with specific evidence (no broadcast+detection model, unmeasured critical fraction, untested dynamic hub-targeting) |
| 5 | >=2 papers cited in §4 assumption challenge | [x] | Assumption 1: Acemoglu et al. 2015, Hasan et al. 2023. Assumption 2: CISA SBOM report, NIST SP 800-161r1, Enck & Williams 2022 |
| 6 | Pipeline signal connection queried in §5 (not placeholder) | [x] | v_question_inputs queried (89 rows), relevant hypotheses and capability options extracted |
| 7 | §4.2 Novelty Pre-Mortem completed — if PREDICTABLE, alternatives provided | [x] | Scored PARTIALLY PREDICTABLE, 1 alternative question produced (hysteresis question) |

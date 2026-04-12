# OBSERVATION LOG

<!-- version: 0.1 -->
<!-- created: 2026-04-12 -->
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
| 1 | Pipeline DB (singularity.db) | v_observation_inputs view: signals, distribution gaps, killed experiments, strategy findings. Also limitations_next_questions for open research frontiers. | 2026-03-22 to 2026-04-12 |
| 2 | Literature (network epidemiology) | Pastor-Satorras & Vespignani (2001) on vanishing epidemic thresholds in scale-free SIS models; Moreno et al. on Daley-Kendall rumor models on complex networks; heterogeneous recovery rate SIS research (Cator & Van Mieghem, MDPI 2024). | 2001 to 2026-04 |
| 3 | Literature (information epidemiology) | Phase transitions in information spreading on structured populations (Nature Physics 2020); Daley-Kendall ISS model extensions with stifler/recovery mechanisms; fact-checking as "immunization" in misinformation networks. | 2020 to 2026-04 |
| 4 | Industry reports / incident data | Shai-Hulud npm self-propagating worm (Sept 2025, Sysdig/PaloAlto/Microsoft); OWASP 2025 Top 10 A03 Supply Chain Failures; 2026 Bastion supply chain security report; MITRE SBOM/AIBOM adoption data. | 2025-09 to 2026-04 |
| 5 | Prior pipeline work (Cycle 7) | cycle7-validation findings: Acemoglu financial contagion phase-transition framework partially transfers but shock dilution mechanism doesn't model replicating attacks (Finding 5). Limitation #5 in limitations_next_questions. | 2026-03 |

<!-- /gate:observation_log §0 -->

---

## §1 Observations

<!-- gate:observation_log §1 entries:3 -->

| # | Date | Source | Observation | Classification | Intensity |
|---|---|---|---|---|---|
| OBS-1 | 2026-04-12 | Cycle 7 Finding 5 + limitations_next_questions #5 | Acemoglu financial contagion's shock dilution mechanism (effective_severity = severity / out_degree) fundamentally mismodels software supply chain attacks where payloads replicate without dilution to ALL dependents. Under deterministic propagation, cascades collapsed to near-zero — an artifact of the wrong mechanism, not actual defense effectiveness. The pipeline's own limitation #5 explicitly asks: "What contagion framework correctly models replicating (non-diluting) attacks through intermediary networks?" | anomaly | 5 |
| OBS-2 | 2026-04-12 | Pastor-Satorras & Vespignani 2001 + SIS heterogeneous recovery literature | Classical SIS epidemic models on scale-free networks have a VANISHING epidemic threshold — any nonzero infection rate leads to endemic persistence (PRL 2001). This is because high-degree hub nodes act as permanent reservoirs. However, introducing heterogeneous recovery rates (where high-degree nodes recover faster, analogous to better-monitored packages having faster detection) can RESTORE an effective threshold (MDPI Applied Sciences 2024, Nature Scientific Reports 2015). The interplay between network topology and heterogeneous recovery is where phase transitions live. | opportunity | 5 |
| OBS-3 | 2025-09 to 2026-04 | Shai-Hulud npm worm incident (Sysdig, PaloAlto, Microsoft) | The Shai-Hulud npm worm (Sept 2025) was the first self-propagating supply chain worm: it stole npm tokens via post-install scripts and used them to push malicious versions of other packages the compromised developer could access. It reached ~500 package versions before containment. Shai-Hulud 2.0 (Nov 2025) escalated: 25,000+ GitHub repos compromised, cross-victim credential recycling creating botnet-like propagation, dead man's switch for anti-containment. This is EXACTLY the broadcast contagion pattern — non-diluting replication through a dependency network — and containment succeeded only through rapid detection + token revocation (a recovery mechanism). | trend | 5 |
| OBS-4 | 2026-04-12 | Daley-Kendall rumor model literature + Nature Physics 2020 | The Daley-Kendall Ignorant-Spreader-Stifler (ISS) model has a built-in recovery mechanism absent from pure SIS: when a spreader contacts another spreader or stifler, it transitions to "stifler" (stops spreading). This is structurally analogous to supply chain detection: when a compromised package is detected (by signature verification, SBOM scanning, or community reporting), it becomes "stifled" — known-bad, no longer propagating. The ISS model on heterogeneous networks exhibits a phase transition between local and global contagion regimes (Nature Physics 2020), with the stifler density acting as the control parameter. | opportunity | 5 |
| OBS-5 | 2026-04-12 | Percolation theory literature + network immunization | Network immunization theory from percolation shows that targeted "vaccination" of high-degree nodes in scale-free networks is dramatically more effective than random vaccination — small fractions of targeted immunization can push the network below the percolation threshold. For supply chains, this maps to: prioritizing detection coverage on high-dependency packages (hubs) may create a containment threshold at much lower overall coverage fractions than uniform deployment would suggest. | opportunity | 4 |
| OBS-6 | 2026-03-29 | Pipeline DB signal #124 (intensity 7) | OpenClaw rename triggered instant supply chain attacks: "GitHub, NPM, Twitter handles sniped within seconds to serve malware — agent ecosystems uniquely fast attack surface." This demonstrates that AI/ML supply chain attack propagation operates at machine speed, compressing the detection window. Detection mechanisms that work for slow-spreading attacks may be inadequate when propagation is near-instantaneous. | pain | 5 |

<!-- /gate:observation_log §1 -->

### §1.1 Question Lineage

**Pipeline research frontiers — query FIRST before external search:**

```
Run: sqlite3 ~/singularity.db "SELECT id, cycle_id, limitation_text, suggested_next_question FROM limitations_next_questions WHERE status='open' ORDER BY cycle_id DESC;"
```

Results:

| ID | Cycle | Limitation | Suggested Next Question |
|---|---|---|---|
| 9 | 7 | LiteLLM back-test is single case study with single topology type | Systematic empirical validation: parameterize simulation from 3+ real supply chain incidents across topology types |
| 8 | 7 | Only single-layer networks tested; real AI supply chains are multiplex | Do multiplex AI supply chain networks exhibit reentrant phase transitions as predicted by Phys Rev E 2019? |
| 7 | 7 | Absorption capacity modeled as fixed; real detection evolves through arms race | How does adaptive absorption capacity (intermediaries learn, attackers evolve) affect steady-state cascade behavior? |
| 6 | 7 | All simulations use static network topology; real supply chain topology evolves over time | How does temporal evolution of supply chain topology affect the phase-transition threshold? |
| 5 | 7 | Acemoglu shock dilution mechanism does not model software supply chain attack propagation — attacks replicate rather than divide | What contagion framework correctly models replicating (non-diluting) attacks through intermediary networks? Starting point: broadcast contagion models from information epidemiology |
| 4 | 6 | This cycle is confirmatory | Can the pipeline produce N>=7 with continuity + grounding? |
| 3 | 6 | Continuity mechanism untested | Does addressing a prior limitation produce N>5? |
| 2 | 6 | G=9 anchor sparse | What does G=9 look like in clinical medicine? |
| 1 | 6 | Leverage estimates are projections | Does implementing top 3 patterns raise composite by >=1.0? |

**This cycle directly addresses limitation #5** (Cycle 7): the Acemoglu shock dilution mechanism does not model replication. The suggested next question points to broadcast contagion from information epidemiology as the starting point — this is exactly the cross-domain import we are pursuing.

**Limitation #7 is partially addressed:** we model detection as a recovery mechanism (fixed rate per node), which is a prerequisite for the adaptive version limitation #7 asks about.

For each observation, trace it backward to the prior work whose limitation makes this observation significant:

| OBS-# | What limitation of prior work does this observation connect to? | Prior work reference |
|---|---|---|
| OBS-1 | Cycle 7 Finding 5: shock dilution doesn't model replication. The Acemoglu framework's core mechanism (divide severity by out-degree) produces unrealistic near-zero cascades under deterministic propagation. | cycle7-validation FINDINGS.md, Acemoglu et al. (2015) "Systemic Risk and Stability in Financial Networks" |
| OBS-2 | Pastor-Satorras & Vespignani (2001) proved vanishing threshold for SIS on scale-free networks, but assumed homogeneous recovery. The limitation is that real systems have heterogeneous recovery — and whether this restores a threshold is the open question their model couldn't answer. | Pastor-Satorras & Vespignani, PRL 86(14), 2001 |
| OBS-3 | No existing supply chain security model captures self-propagating worm dynamics. The Shai-Hulud incident demonstrates that broadcast-type propagation IS real, not hypothetical — yet no quantitative framework exists for the detection coverage needed to contain it. | Sysdig Shai-Hulud analysis (2025); Ohm et al. "Backstabber's Knife Collection" (2020) |
| OBS-4 | Daley-Kendall (1964) introduced stifler recovery but on well-mixed populations, not heterogeneous networks. Moreno et al. extended to complex networks but did not parameterize the stifler mechanism against real-world detection coverage rates. | Daley & Kendall (1964), Moreno et al. (2004) "Dynamics of rumor spreading in complex networks" |
| OBS-5 | Cohen et al. (2003) proved targeted immunization thresholds for scale-free networks but in a pure percolation (node removal) framework — no dynamics, no propagation speed, no detection latency. | Cohen et al. PRL 91, 247901 (2003) |
| OBS-6 | No supply chain contagion model accounts for machine-speed propagation where the detection window compresses to seconds/minutes vs. the days/weeks assumed by traditional models. | Pipeline signal #124, OpenClaw incident (2026-03-29) |

---

## §1b Technology Readiness Scan

For each observation in §1 with intensity ≥3:

| OBS-# | What changed recently making this actionable NOW? | When did this enabler become available? |
|---|---|---|
| OBS-1 | Cycle 7 computational infrastructure now exists: network generation code, cascade simulation framework, phase-transition measurement pipeline. The negative finding (dilution doesn't model replication) gives a clear mechanistic target to replace. | 2026-03 (Cycle 7 completion) |
| OBS-2 | Recent work on heterogeneous SIS models (MDPI 2024, multiple 2023-2024 papers) provides analytical frameworks for recovery-rate heterogeneity on networks. These didn't exist in tractable form when Pastor-Satorras & Vespignani published. | 2023-2024 |
| OBS-3 | Shai-Hulud (Sept 2025) is the first documented self-propagating npm worm — it provides REAL empirical data on broadcast-type supply chain attack dynamics, including propagation speed, containment timeline, and recovery mechanisms used. Before this, broadcast supply chain attacks were hypothetical. | 2025-09 |
| OBS-4 | Nature Physics 2020 paper on phase transitions in information spreading on structured populations provides modern analytical tools for ISS-type models on realistic networks. Combines rumor dynamics with heterogeneous network structure. | 2020 |
| OBS-5 | Network immunization theory now has efficient algorithms for limited-knowledge settings (NSR 2020), making targeted detection deployment computable even without full topology knowledge. | 2020 |
| OBS-6 | The OpenClaw incident (March 2026) and Shai-Hulud 2.0 (Nov 2025) demonstrate machine-speed propagation is not theoretical. Real attack data exists to parameterize propagation rates. | 2025-11 to 2026-03 |

---

## §1c Cross-Field Method Scan

Before proceeding to Stage 1 (Question), scan for cross-domain methods:

| Observation cluster | Analogous field 1 | Their method | Analogous field 2 | Their method |
|---|---|---|---|---|
| OBS-1, OBS-2: Non-diluting contagion with recovery on heterogeneous networks | **Information epidemiology** (rumor/misinformation spreading) | Daley-Kendall ISS model with stifler mechanism on complex networks. Spreader→Stifler transition models "detection and removal." Phase transitions between local and global regimes characterized analytically. Key insight: stifler density is a tunable control parameter — maps to detection coverage fraction. | **Percolation theory / network immunization** | Targeted node immunization on scale-free networks. Critical immunization fraction computed from degree distribution. Hub-targeted vaccination exponentially more efficient than random. Key insight: framing detection as "immunization" allows using percolation threshold theory to compute critical coverage. |
| OBS-3, OBS-6: Machine-speed propagation in real supply chains | **Cybersecurity — worm propagation modeling** | Staniford-Chen "Code Red" worm models (2002): random-scan worm propagation with patching as recovery. Analytical epidemic threshold for worm containment derived from patching rate vs. scan rate. Key insight: worm models already combine broadcast propagation with detection/patching recovery — the supply chain topology adds the network structure dimension. | **Biological epidemiology — contact tracing** | Contact tracing as targeted recovery: identifying and isolating exposed individuals before they become infectious. Maps to dependency-graph-aware detection — when a compromised package is found, trace its dependents and check them proactively. Key insight: contact tracing creates "effective" recovery rates much higher than passive detection alone. |

> **Self-test:** Information epidemiology and percolation theory are genuinely different source domains from supply chain security. Information epidemiology studies how IDEAS replicate through social networks (fundamentally different substrate from software packages through dependency graphs, but structurally isomorphic propagation dynamics). Percolation theory is pure mathematics/statistical physics applied to network fragmentation — importing it means treating detection coverage as a percolation parameter, which is a genuine reframing.

---

## §2 Cross-Engine Context

<!-- queried: v_observation_inputs, 1554 rows -->

Query: `sqlite3 ~/singularity.db "SELECT * FROM v_observation_inputs;"`

**Relevant signals (supply chain and propagation-related, intensity ≥4):**

| Type | ID | Category | Intensity | Summary |
|---|---|---|---|---|
| signal | 18 | supply_chain | 4.0 | Unpinned HuggingFace downloads in AutoGen — supply chain attack vector |
| signal | 114 | model_supply_chain | 6.0 | Xiaomi's model appeared anonymously on OpenRouter — model provenance failing at scale |
| signal | 122 | model_supply_chain | 6.0 | NVIDIA controls 70% of TSMC 3nm, ASML 700 machines/yr — AI supply chain critical chokepoints |
| signal | 124 | model_supply_chain | 7.0 | OpenClaw rename triggered instant supply chain attacks — handles sniped within seconds |
| signal | 134 | model_supply_chain | 4.0 | NVIDIA Vera Rubin: 1.3-1.5M components from 200 suppliers — hardware supply chain unprecedented complexity |
| signal | 140 | model_supply_chain | 4.0 | MITRE: organizations acquire AI models with little/no risk assessment; SBOMs/AIBOMs not in widespread use |

**Relevant strategy findings:**

| ID | Rule | Finding |
|---|---|---|
| 2 | R3 | Publication velocity > study depth for scarcity moat. DOM-003 window 24-36 months. |
| 7 | R3 | Deployment gap (95% pilot failure, 4.17% project completion) IS the TAM. |

**Relevant killed experiments (learning from failures):**

| ID | Kill Reason | Experiment |
|---|---|---|
| 96 | wrong_channel | First External Distribution |
| 132 | wrong_product | Practitioner interviews: agent security pain validation |

**Distribution gaps:** 14 completed distribution gap entries, all in "of-ai" category — indicates the pipeline has distribution infrastructure but research content is the bottleneck, not distribution.

**Key cross-engine insight:** Signal #124 (intensity 7) — OpenClaw supply chain attacks at machine speed — combined with signal #140 (MITRE: SBOMs not in widespread use) creates a gap: attack propagation is fast and broadcast-type, but detection coverage is low and unevenly distributed. This directly motivates the research question about whether a critical detection coverage threshold exists.

---

## §3 Pattern Notes

<!-- gate:observation_log §3 entries:1 -->

| # | Pattern | Supporting Observations | Surprising? | Contradicts Prior Assumption? |
|---|---|---|---|---|
| PAT-1 | **The recovery mechanism IS the research opportunity, not just a validity concern.** Classical broadcast contagion models (SIS on scale-free networks) predict inevitable endemic persistence — no threshold. But real supply chains DO contain attacks (Shai-Hulud was contained). The gap between theory (no threshold) and practice (containment happens) means detection/recovery mechanisms create an effective threshold that no existing model captures. The mechanism validity concern identified in the strategic frame (broadcast models lack detection/recovery) is simultaneously the key research gap. | OBS-1, OBS-2, OBS-3, OBS-4 | Yes — the framing flips from "this is a modeling limitation to work around" to "this is the core phenomenon to study" | Yes: initial assumption was that broadcast contagion is the framework and detection is an extension. The pattern suggests detection-as-recovery IS the framework — the broadcast dynamics are just the substrate. |
| PAT-2 | **Hub-targeted detection is exponentially more efficient than uniform detection.** Percolation immunization theory (OBS-5) and the Shai-Hulud containment (OBS-3: rapid response focused on high-impact packages) both suggest that the critical detection coverage fraction depends heavily on WHERE detection is deployed, not just HOW MUCH. This means the phase transition may have two parameters: overall coverage fraction AND hub-targeting ratio. | OBS-3, OBS-5, OBS-6 | Partially — the percolation result is known, but applying it to supply chain detection coverage is new | Yes: most supply chain security recommendations assume uniform SBOM adoption thresholds (e.g., "all packages should have SBOMs"). The pattern suggests a small fraction of hub-targeted detection may be sufficient. |
| PAT-3 | **Time-to-detection compresses the effective propagation window.** Shai-Hulud V1 was contained at ~500 packages; V2 reached 25,000+ repos before containment. The difference was propagation speed vs. detection speed. This suggests the phase transition threshold is not just a static coverage fraction but depends on the ratio of propagation rate to detection rate — a dynamic threshold, not a percolation threshold. | OBS-3, OBS-6 | Yes — the distinction between static (percolation) and dynamic (epidemic) thresholds maps to different practical interventions | No — consistent with epidemic theory but surprising in the supply chain context where detection is usually discussed as binary (has SBOM / doesn't have SBOM) |

<!-- /gate:observation_log §3 -->

---

## §4 Observation Gate Checklist

Self-assessment before proceeding to Stage 1 (Question).

| # | Check | Status | Notes |
|---|---|---|---|
| 1 | ≥2 distinct source types in §0 | [x] | 5 source types: pipeline DB, network epidemiology literature, information epidemiology literature, industry incidents, prior pipeline work |
| 2 | ≥3 observations logged in §1 | [x] | 6 observations logged (OBS-1 through OBS-6) |
| 3 | Cross-engine context queried in §2 (not placeholder) | [x] | v_observation_inputs queried, 1554 rows, relevant signals/findings/killed experiments extracted |
| 4 | ≥1 pattern noted in §3 | [x] | 3 patterns noted (PAT-1 through PAT-3) |
| 5 | Most recent observation within last 90 days | [x] | All observations dated 2026-04-12 or within 90 days |
| 6 | No single source type accounts for all observations | [x] | Observations draw from pipeline DB, literature (2 sub-domains), industry incidents |

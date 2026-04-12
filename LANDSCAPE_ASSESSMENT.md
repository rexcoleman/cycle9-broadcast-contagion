# LANDSCAPE ASSESSMENT

<!-- version: 1.0 -->
<!-- created: 2026-04-12 -->
<!-- stage: 2 -->
<!-- methodology_status: complete — Stage 2 Landscape filled by Researcher-Planner, Dispatch 1 -->

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
| **Databases queried** | arXiv, Google Scholar (via WebSearch), PubMed, Nature journals, Physical Review Letters/E, Physica A, MDPI Applied Sciences, IEEE Xplore, ACM DL, CISA/NIST publications, Sysdig/PaloAlto/Microsoft security blogs |
| **Search terms** | "epidemic spreading scale-free networks SIS model"; "Daley-Kendall rumor spreading complex networks phase transition stifler"; "targeted immunization scale-free networks percolation threshold"; "SIS model heterogeneous recovery rates epidemic threshold"; "supply chain attack propagation contagion simulation dependency network"; "broadcast contagion detection coverage phase transition supply chain"; "Moreno Nekovee rumor spreading complex networks 2004"; "subcritical behavior correlation-induced transition rumor models"; "SBOM adoption rate 2025 2026 detection coverage"; "Shai-Hulud npm worm self-propagating supply chain containment"; "vaccination herd immunity threshold phase transition network heterogeneous"; "network immunization percolation firebreak containment threshold" |
| **Date range** | 2001 — April 2026 (foundational: 2001-2007; modern extensions: 2015-2026) |
| **Inclusion criteria** | (1) Epidemic/contagion models on heterogeneous networks with recovery mechanisms; (2) Rumor/information spreading models with stifler dynamics on complex networks; (3) Network immunization/percolation theory with targeted strategies; (4) Supply chain attack propagation modeling; (5) Empirical supply chain worm incidents with containment data; (6) Detection coverage as phase parameter in any network contagion context |
| **Exclusion criteria** | Pure financial contagion without network recovery mechanisms; marketing/vendor white papers; DDoS without supply chain context; supply chain risk management without propagation dynamics; biological epidemiology without network structure |
| **Total results screened** | ~95 unique results across 12 search queries |
| **Results included** | 7 (inventoried below) + ~6 supplementary references |

<!-- /gate:landscape_assessment §0 -->

> The search was conducted via WebSearch tool on 2026-04-12. Each query was
> executed independently. Results were cross-referenced to deduplicate.
> Assessments based on abstracts, open-access versions, and search snippets.
> No paywalled full texts were fetched.

---

## §1 Prior Work Inventory

<!-- gate:landscape_assessment §1 entries:5 -->

| # | Reference | What It Does | Methodology | Key Results | Limitations | Relevance to Our Question |
|---|---|---|---|---|---|---|
| 1 | Pastor-Satorras & Vespignani (2001). "Epidemic Spreading in Scale-Free Networks." PRL 86(14):3200-3203 | Proves that the SIS epidemic threshold vanishes on scale-free networks — any nonzero infection rate leads to endemic persistence | Analytical mean-field treatment of SIS dynamics on networks with power-law degree distributions P(k) ~ k^(-gamma). Large-scale Monte Carlo simulations on Barabasi-Albert networks up to N=10^6. | Epidemic threshold lambda_c approaches 0 for scale-free networks (gamma <= 3). Virus prevalence decays as rho ~ exp(-C/lambda) rather than vanishing at a finite threshold. High-degree hub nodes act as permanent infection reservoirs. | Assumes HOMOGENEOUS recovery rate delta — all nodes recover at the same rate regardless of degree, monitoring, or external intervention. No detection mechanism beyond spontaneous recovery. No directed graphs. | **Foundational.** Establishes that pure SIS on scale-free networks has NO threshold — the starting point for our question. If supply chain networks are scale-free (they are approximately so), then WITHOUT detection/recovery mechanisms, any nonzero attack rate leads to endemic persistence. Our question: does adding heterogeneous detection RESTORE a threshold? |
| 2 | Moreno, Nekovee & Pacheco (2004). "Dynamics of Rumor Spreading in Complex Networks." Phys. Rev. E 69:066130 | Derives mean-field equations for the Daley-Kendall ISS (Ignorant-Spreader-Stifler) rumor model on heterogeneous networks | Mean-field equations for ISS dynamics on networks with arbitrary degree distribution. Monte Carlo simulations on scale-free and Erdos-Renyi networks. Compares DK (original Daley-Kendall) and MK (Maki-Thompson) variants. | Rumor spreads faster and reaches larger fraction on scale-free vs. homogeneous networks. Stifler mechanism creates an effective damping that depends on network heterogeneity. Time profiles differ significantly between DK and MK variants on scale-free topologies. | Stifler transition is CONTACT-DEPENDENT — a spreader becomes stifler only when contacting another spreader or stifler. No time-dependent recovery (detection after fixed delay). No directed graphs. No parameterization against real-world detection rates. | **Core methodological source.** The ISS stifler mechanism is our primary analog for supply chain detection. But the contact-dependent stifling must be adapted to TIME-DEPENDENT detection (packages are detected after scanning delay, not upon contact with a detected package). This adaptation is a key methodological contribution. |
| 3 | Nekovee, Moreno, Bianconi & Marsili (2007). "Theory of Rumour Spreading in Complex Social Networks." Physica A 374(1):457-470 | Introduces general stochastic model for rumor spreading; derives analytical mean-field equations on complex networks including a stifling rate parameter | Mean-field theory with heterogeneous mean-field approximation. Derives critical spreading threshold as function of stifling rate and network moments. Analytical treatment on both homogeneous and scale-free networks. | Critical threshold exists in homogeneous networks and random graphs. On scale-free networks, the threshold becomes vanishingly small (analogous to Pastor-Satorras & Vespignani for SIS). Stifling rate acts as a tunable control parameter that shifts the phase boundary. | Same contact-dependent stifling as Moreno et al. 2004. Infinite-size limit — finite-size effects not characterized. No mapping to real-world detection technologies. Static network topology. | **Analytically strongest prior work for our framework.** The stifling rate as control parameter maps directly to detection coverage fraction in our model. Their result that the threshold vanishes on scale-free networks in infinite-size limit raises a critical question: do FINITE realistic supply chain networks (N ~ 10^4 to 10^6 packages) have an EFFECTIVE threshold even when the theoretical infinite-network threshold vanishes? |
| 4 | Cohen, Havlin & ben-Avraham (2003). "Efficient Immunization Strategies for Computer Networks and Populations." PRL 91:247901 | Computes critical immunization fraction for scale-free networks; introduces acquaintance immunization strategy requiring no global knowledge | Bond percolation mapping of SIR model. Analytical derivation of critical immunization fraction p_c as function of degree distribution moments. Comparison of random, targeted (high-degree), and acquaintance immunization. | Random immunization requires unrealistically high fractions on scale-free networks (p_c approaches 1). Targeted immunization of high-degree nodes achieves containment at dramatically lower fractions. Acquaintance immunization (immunize random neighbor of random node) achieves near-targeted efficiency without global knowledge. | STATIC percolation framework — no dynamics, no propagation speed, no time-dependent detection. Binary immunization (immune or not) rather than probabilistic detection. No distinction between preventive immunization and reactive containment. | **Critical for hub-targeting analysis.** Cohen's targeted vs. random immunization comparison maps directly to our hub-targeted vs. uniform detection deployment. But their static framework cannot capture the race between propagation speed and detection latency that defines real supply chain attack containment. Our dynamic simulation fills this gap. |
| 5 | Yang et al. (2015). "Large epidemic thresholds emerge in heterogeneous networks of heterogeneous nodes." Scientific Reports 5:13122 | Shows that intrinsic node heterogeneity (heterogeneous susceptibility and recovery) can RESTORE large epidemic thresholds on heterogeneous networks | Extended SIS model where each node has intrinsic susceptibility and recovery rate drawn from distributions. Adaptive network structure where nodes respond to disease presence. Mean-field analysis + simulations. | Networks that are more heterogeneous in connectivity can be MORE resistant to epidemic spreading when nodes are also heterogeneous. When people with more connections have higher recovery rates, the epidemic threshold increases substantially — heterogeneity in nodes counteracts heterogeneity in topology. | Requires correlation between degree and recovery rate — if recovery is uncorrelated with degree, the threshold restoration effect is weak. Adaptive network rewiring is included, which real supply chain networks do not do in real-time. | **Directly relevant to our core hypothesis.** In supply chain networks, high-degree packages (popular, widely-depended-upon) ARE monitored more intensively — creating exactly the degree-recovery correlation that Yang et al. show restores thresholds. This provides theoretical grounding for expecting a phase transition in supply chain detection coverage. |
| 6 | de Arruda et al. (2022). "From subcritical behavior to a correlation-induced transition in rumor models." Nature Communications 13:3049 | Characterizes phase transition behavior in Maki-Thompson rumor model; shows correlation-induced transition changes the universality class | Modified Maki-Thompson model with forgetting mechanism. Analytical characterization via heterogeneous mean-field + pairwise approximations. Extensive Monte Carlo simulations on synthetic and real networks. | Continuous phase transition IS present in the rumor model (overturning earlier mean-field claims of no transition). Subcritical behavior follows power-law lifespan increase. Dynamical correlations change the nature of the transition — pairwise approximation is needed, mean-field alone is insufficient. | Forgetting mechanism (stifler returns to ignorant) changes dynamics from original DK model. Does not model external detection/recovery — all transitions are contact-driven. Analytical results primarily for well-mixed and configuration model networks, not directed dependency graphs. | **Methodologically important for simulation design.** Their finding that mean-field approximation is INSUFFICIENT (pairwise correlations matter) means our simulation cannot rely on mean-field analytics alone — agent-based simulation on explicit network topologies is essential. This validates our planned computational approach over pure analytical treatment. |
| 7 | Cator & Van Mieghem (2024). "Statistical Properties of SIS Processes with Heterogeneous Nodal Recovery Rates in Networks." MDPI Applied Sciences 14(21):9987 | Characterizes metastable-state properties of SIS with heterogeneous recovery rates; derives analytical approximations | Heterogeneous N-Intertwined Mean-Field Approximation (NIMFA). Systematic comparison of analytical predictions vs. exact Markov chain simulations on small networks and Monte Carlo on larger networks. | NIMFA provides good approximation for heterogeneous SIS except near the epidemic threshold phase transition point, where observable deviations occur. The critical epidemic threshold tau_c depends on the full spectrum of the effective spreading matrix, not just the leading eigenvalue. | Small network sizes (N <= 100 for exact analysis). Near-threshold behavior poorly approximated by NIMFA — exactly where our research question lives. Does not parameterize against real-world detection rate distributions. | **Technical calibration for our simulation.** Their finding that analytical approximations FAIL near the phase transition point (exactly our region of interest) reinforces that Monte Carlo simulation on explicit networks is necessary. We cannot rely on NIMFA predictions for threshold location. |

<!-- /gate:landscape_assessment §1 -->

### §1.1 Benchmark as Landscape

<!-- source: Track 1, gap matrix Stage 2 -->

| Question | Answer |
|---|---|
| Does a standardized competition, benchmark, or shared evaluation exist for this problem? | **No.** No standardized benchmark exists for evaluating contagion containment thresholds on software supply chain networks. There is no shared evaluation framework, no competition, and no reference dataset. |
| If no: why not? What does the absence tell you about the field's maturity or the question's novelty? | The absence reflects two gaps: (1) Supply chain contagion modeling is split between financial/economic contagion (Acemoglu et al.) and epidemiological contagion (Pastor-Satorras & Vespignani), with neither community owning the software supply chain application. (2) The question of detection-coverage-as-phase-parameter has not been formulated — supply chain security treats detection as a compliance target, not a dynamical parameter. Without the question, there is no benchmark to evaluate answers. The absence confirms the novelty of our framing. Creating a reproducible simulation framework with parameterized topologies and detection strategies could itself become a benchmark contribution — analogous to how Milkman's megastudy design WAS the contribution in behavioral science. |

---

## §1b Adjacent Field Survey

<!-- source: Track 1, U2/priority 1 — 7/7 papers -->

| # | Adjacent field | Analogous problem they face | Method they use | Have they solved something you haven't? | Could you import their method? |
|---|---|---|---|---|---|
| 1 | **Biological epidemiology — vaccination and herd immunity** | Determining the critical vaccination fraction (herd immunity threshold) needed to prevent epidemic outbreaks in heterogeneous populations with varying susceptibility | Mathematical epidemiology with heterogeneous SIR/SIS models on contact networks. Key result: the classical HIT formula (1 - 1/R_0) assumes homogeneous mixing, but heterogeneous populations can have HIT as low as 40% vs. 63% under homogeneous assumptions (Britton et al. 2021, J. Math. Bio.). Targeted vaccination of high-contact individuals dramatically reduces the required coverage fraction. | **Yes — they have established that heterogeneous targeted intervention shifts thresholds by large factors (up to 40% reduction in required coverage).** This is the analog of our hub-targeting hypothesis. They have analytical frameworks (next-generation matrix methods) for computing thresholds in structured populations. We do not yet have the supply chain analog. | **Yes — import the next-generation matrix method for computing effective reproduction number R_0 on structured networks with heterogeneous recovery.** The epidemiological R_0 framework maps directly to broadcast contagion: R_0 < 1 means containment, R_0 > 1 means endemic spread. The threshold p_c (detection coverage) is the value where R_0(p_c, topology) = 1. This provides both the analytical framework AND the validation methodology (compare simulation results against analytical R_0 predictions). |
| 2 | **Wildfire management — firebreak theory and prescribed burning** | Determining the minimum fraction of landscape that must be treated (firebreaks, fuel reduction) to prevent landscape-scale fire spread through heterogeneous terrain | Percolation-based fire spread models on heterogeneous landscapes. Firebreaks act as "immune" patches that block propagation. Key result: strategic placement of firebreaks at topological chokepoints (ridgelines, fuel breaks) is orders of magnitude more efficient than random fuel reduction. The critical firebreak fraction depends on landscape connectivity and wind patterns (fuel moisture as the "recovery" parameter). | **Yes — they have quantified how landscape heterogeneity affects the critical containment fraction, and they have practical decision frameworks for where to place firebreaks under budget constraints.** The "where to place detection" question in supply chains is structurally identical to "where to place firebreaks" in landscapes. | **Yes — import the landscape connectivity analysis framework.** Firebreak theory decomposes the landscape into patches with connectivity determined by slope, wind, and fuel — analogous to decomposing supply chain networks into clusters with connectivity determined by dependency structure. The firebreak placement optimization maps to detection deployment optimization. The key adaptation: fire spread is spatially constrained (adjacent patches only), while supply chain attacks propagate through dependency edges (non-spatial). This means firebreak theory's spatial optimization must be replaced with graph-theoretic optimization, but the threshold analysis framework transfers. |
| 3 | **Network neuroscience — seizure propagation and containment** | Determining how focal seizures propagate through brain networks and what "containment" mechanisms (inhibitory circuits, anti-epileptic drug coverage) prevent generalization to global seizures | Spreading activation models on connectome-derived networks with heterogeneous excitability and inhibition. Inhibitory nodes act as "stiflers" that dampen propagation. Phase transitions between focal (contained) and generalized (global) seizure states depend on the balance between excitatory and inhibitory node density. | **Partially — they have characterized phase transitions between focal and generalized propagation in heterogeneous biological networks.** The excitation/inhibition balance maps to our propagation/detection balance. They have NOT solved the optimal inhibitor placement problem (it is an active research question in computational neuroscience). | **Partially importable.** The spreading activation + inhibition framework on heterogeneous networks is structurally similar to broadcast contagion + detection. The key insight: brain networks have BUILT-IN inhibitory circuits that co-evolved with excitatory pathways — supply chain networks do NOT have built-in detection. This means our phase transition may be qualitatively different (detection must be externally imposed, not inherent). This is a validation candidate for ED §9a: if our threshold framework generalizes to seizure propagation networks, it suggests a domain-agnostic principle. |

> **Self-test:** Biological epidemiology (vaccination thresholds in heterogeneous
> populations), wildfire management (firebreak placement), and network neuroscience
> (seizure containment) are genuinely different source domains from software supply
> chain security. None are sub-disciplines of computer science or cybersecurity.
> Each offers a different lens: epidemiology provides analytical threshold frameworks,
> wildfire management provides spatial optimization under budget constraints,
> neuroscience provides excitation/inhibition balance on biological networks.

---

## §2 Gap Map

<!-- gate:landscape_assessment §2 entries:1 -->

| # | Gap Description | Gap Type | Evidence | Opportunity Size |
|---|---|---|---|---|
| 1 | No existing model combines broadcast (non-diluting) contagion with detection/recovery mechanisms on realistic supply chain network topologies to compute containment thresholds. | Tried with wrong method + tried in wrong domain | **Wrong method:** Cycle 7 applied Acemoglu financial contagion (diluting-shock) to supply chain networks — the dilution mechanism produced artificially low cascades (Finding 5). The correct mechanism is broadcast (non-diluting) replication, which financial contagion does not model. **Wrong domain:** ISS rumor models (Moreno et al. 2004, Nekovee et al. 2007) model broadcast spreading with stifler recovery on heterogeneous networks — but in the information/social domain, not supply chain. The stifler mechanism is contact-dependent (requires meeting another stifler), whereas supply chain detection is time-dependent (scanning detects after delay). No work has adapted ISS dynamics to supply chain topology with time-dependent detection. | **HIGH.** The Shai-Hulud worm (Sept 2025) proved broadcast supply chain attacks are REAL, not hypothetical. CISA/NIST/OWASP recommend detection coverage without quantifying what fraction suffices. A quantitative threshold would directly inform practitioner investment decisions and policy recommendations. |
| 2 | The critical detection coverage fraction for software supply chain attack containment is unmeasured — no quantitative model exists for the relationship between detection coverage percentage and containment probability. | Nobody tried | CISA SBOM Sharing Lifecycle Report (2024) and NIST SP 800-161r1 recommend universal adoption without threshold analysis. MITRE/NTIA surveys estimate <50% current SBOM adoption but provide no model of whether this is above or below a containment threshold. The Shai-Hulud containment provides anecdotal evidence (rapid detection + token revocation worked) but no quantitative threshold. Searched "supply chain detection threshold" and "SBOM adoption phase transition" — zero results. | **HIGH.** If a phase transition exists at p_c = 0.15, current detection adoption may already suffice for hub-targeted strategies. If p_c = 0.60, the industry is catastrophically under-protected. The answer directly determines whether current SBOM adoption policy is adequate or requires urgent acceleration. |
| 3 | Whether hub-targeted detection deployment achieves containment at dramatically lower coverage fractions than uniform deployment in DYNAMIC (not static percolation) settings is untested. | Tried in wrong framework | Cohen et al. (2003) proved targeted immunization is exponentially more efficient than random immunization in STATIC percolation on scale-free networks. But supply chain attack propagation is dynamic — the race between propagation speed and detection latency creates a temporal dimension absent from static percolation. No work extends Cohen's targeted immunization to dynamic broadcast contagion with time-dependent detection. | **MEDIUM-HIGH.** If hub-targeting reduces p_c by 5-10x in dynamic settings (as static percolation predicts), the policy implication reverses from "everyone needs SBOMs" to "prioritize detection on the top 100 most-depended-upon packages." This is immediately actionable. |

<!-- /gate:landscape_assessment §2 -->

---

## §2b Fragmentation Diagnosis

<!-- source: Track 1, gap matrix Stage 2 -->

| Question | Answer |
|---|---|
| Does evidence for your question exist in incomparable forms across studies? | **Yes, severely fragmented.** Evidence exists in three incompatible forms: (1) analytical epidemic threshold theory on idealized infinite-size networks (Pastor-Satorras & Vespignani, Nekovee et al.) — results stated as asymptotic scaling relations with no finite-size parameterization; (2) static percolation immunization fractions (Cohen et al.) — results assume instantaneous state change with no dynamics; (3) empirical incident data (Shai-Hulud) — containment timelines and package counts with no network topology characterization. These three evidence streams cannot be directly compared because they use different models (SIS vs. ISS vs. percolation), different assumptions (infinite vs. finite, dynamic vs. static, homogeneous vs. heterogeneous recovery), and different metrics (prevalence vs. immunization fraction vs. packages compromised). |
| If yes: what makes them incomparable? | **Different models, assumptions, and metrics across three research communities.** Network epidemiology uses SIS/SIR prevalence on idealized topologies. Information epidemiology uses ISS stifler density on social networks. Supply chain security uses incident response timelines on undocumented topologies. No shared parameterization exists (e.g., what "detection coverage" means in each framework differs). |
| If yes: what would make them comparable? | A unified simulation framework that (a) implements broadcast (non-diluting) propagation on explicit network topologies derived from real supply chain degree distributions, (b) parameterizes detection as a time-dependent recovery mechanism with heterogeneous rates correlated with node degree, and (c) measures the phase transition threshold in a single consistent metric (critical detection coverage fraction p_c). This framework would make analytical predictions (from epidemic theory), static predictions (from percolation theory), and empirical observations (from incident data) directly comparable. |
| Is making evidence comparable the real contribution? | **Partially — the unified framework IS a significant methodological contribution**, but the primary contribution is the ANSWER it produces: the quantitative threshold p_c and the hub-targeting efficiency ratio. The framework is a necessary means, not the end. However, if the framework itself proves reusable for other supply chain contagion questions (temporal evolution, multiplex networks), the methodological contribution may rival the specific result in long-term value. |

---

## §3 Baseline Knowledge State

| Category | What We Know |
|---|---|
| **Known with confidence** | (1) Software supply chain attacks replicate without dilution — every downstream consumer receives the full malicious payload (empirically proven: Shai-Hulud 2025, event-stream 2018, ua-parser-js 2021). (2) Package dependency networks have approximately scale-free degree distributions with heavy-tailed hub structure (Decan et al. 2019, libraries.io data). (3) SIS epidemic models on scale-free networks have a vanishing epidemic threshold — pure broadcast contagion without recovery leads to endemic persistence at any nonzero infection rate (Pastor-Satorras & Vespignani 2001). (4) Targeted immunization of high-degree nodes in scale-free networks is dramatically more efficient than random immunization in static percolation (Cohen et al. 2003). (5) Heterogeneous node properties (including recovery rates correlated with degree) can restore large epidemic thresholds on networks that would otherwise have vanishing thresholds (Yang et al. 2015). |
| **Uncertain** | (1) Whether real-world supply chain detection rates (~20-40% SBOM adoption, higher for popular packages) are above or below a containment threshold — no threshold has been computed. (2) Whether the contact-dependent stifler mechanism from ISS models (Moreno et al. 2004) is a valid proxy for time-dependent detection in supply chains — the stifling dynamics are structurally different. (3) Whether mean-field approximations (NIMFA, heterogeneous mean-field) provide useful threshold estimates or whether correlations invalidate them near the phase transition (de Arruda et al. 2022 found correlations matter; Cator & Van Mieghem 2024 found NIMFA fails near threshold). (4) The sharpness of the phase transition — whether it is a sharp threshold (useful for policy) or a gradual crossover (less actionable). |
| **Contested** | (1) Whether detection coverage provides LINEAR vs. THRESHOLD benefit — CISA/NIST guidance implicitly assumes linear (more coverage always proportionally better), while epidemic theory predicts a threshold. No data resolves this. (2) Whether finite-size effects on realistic supply chain networks (N ~ 10^5 packages) create an effective threshold even when the infinite-network theoretical threshold vanishes — this is an open question in network epidemiology generally (the infinite-size limit may not apply to real networks). (3) Whether the ISS stifler mechanism is the right analog for supply chain detection — an alternative is pure SIS+recovery where detection is spontaneous (time-dependent) rather than contact-dependent. The choice of mechanism changes the analytical framework and potentially the threshold value. |

---

## §4 Frontier Moat Test

<!-- gate:landscape_assessment §4 required -->

| Question | Answer |
|---|---|
| **Novelty check:** <5 similar projects on GitHub/arXiv? | **Yes, <5.** Searched GitHub for "supply chain contagion simulation broadcast propagation phase transition" and arXiv for "broadcast contagion detection coverage phase transition supply chain." Found zero projects combining broadcast contagion + detection-as-phase-parameter on supply chain networks. Found: (a) SEIR-based supply chain risk propagation (PLOS ONE 2024, Frontiers 2025) — uses diluting epidemiological models, not broadcast; (b) financial contagion stress testing on supply chain networks (arXiv 2305.04865, 2502.17044) — uses shock-dilution, not broadcast; (c) generic epidemic simulation frameworks on GitHub (SIS/SIR simulators) — none parameterized for supply chain detection. The specific combination (broadcast propagation + heterogeneous time-dependent detection + supply chain topology + phase transition measurement) appears to be genuinely novel. |
| **Timing check:** What changed in the last 6 months enabling this? | Three enablers converged: (1) **Shai-Hulud npm worm (Sept 2025 + Nov 2025)** — first empirical proof that broadcast-type supply chain attacks are real, providing concrete parameterization data (propagation speed, containment timeline, recovery mechanisms used). Before this, broadcast supply chain attacks were hypothetical. (2) **Cycle 7 infrastructure (March 2026)** — our pipeline built network generation, cascade simulation, and phase-transition measurement code that can be adapted from diluting-shock to broadcast dynamics. The computational infrastructure exists. (3) **Yang et al. 2015 + Cator & Van Mieghem 2024** — recent work on heterogeneous recovery SIS models provides the analytical framework for degree-correlated detection rates, which was not tractable before these approximation methods existed. |
| **Moat check:** What stops a funded competitor replicating in 1 month? | Three barriers: (1) **Cross-domain import depth** — the adaptation from ISS contact-dependent stifling to time-dependent supply chain detection requires understanding BOTH information epidemiology framework theory AND supply chain security operational realities. This is not a mechanical code translation. (2) **Cycle 7 negative finding** — knowing that financial contagion's dilution mechanism fails (and WHY) prevents the most obvious wrong approach. A competitor starting fresh would likely replicate our C7 mistake first. (3) **Mechanism validity pre-check** — the three specific adaptations (contact-dependent to time-dependent recovery, undirected to directed graphs, continuous to discrete event propagation) require domain expertise that spans network science, information epidemiology, and software supply chain operations. However: the moat is MEDIUM. A team with a network epidemiologist and a supply chain security researcher could replicate within 2-3 months. The moat is in speed-to-result and cross-domain integration, not in proprietary data or compute. |

<!-- /gate:landscape_assessment §4 -->

---

## §5 Cross-Engine Research Context

<!-- gate:landscape_assessment §5 required -->

<!-- queried: v_landscape_inputs, 2794 rows -->

Query: `sqlite3 ~/singularity.db "SELECT * FROM v_landscape_inputs;"`

**Prior research cycles (relevant to this landscape):**

| Type | Cycle | Project | Score | Status |
|---|---|---|---|---|
| prior_cycle | 1 | tool-permission-boundaries | 7.3 | completed |
| prior_cycle | 2 | phase_2d_llm_judge_reliability | 7.3 | complete |

**Relevant claims from pipeline (supply chain, cascade, contagion-related):**

| Claim ID | Confidence | Summary | Relevance |
|---|---|---|---|
| 269 | 4.0 | Under implicit trust, a single compromised agent cascades to 100% regardless of system size | Confirms broadcast-type propagation in agent systems — supports our non-diluting contagion premise |
| 270 | 4.0 | Zero-trust reduces poison rate by ~40 percentage points vs. implicit trust (0.583 vs 0.974) | Detection/trust mechanisms DO create measurable containment — supports phase transition hypothesis |
| 272 | 4.0 | Under implicit trust, topology has minimal impact on cascade — all topologies reach 100% cascade | Without detection, topology alone does not contain broadcast attacks — reinforces that detection is the critical parameter, not topology |
| 278 | 3.0 | Verification detection rate below 0.6 fails to reduce cascade below 100%; above 0.6 produces sharp drop | **DIRECTLY relevant** — prior pipeline work found what appears to be a phase transition at detection rate 0.6 in multi-agent cascade. This is exactly the phenomenon we aim to characterize rigorously on supply chain networks. |
| 282 | 4.0 | Simulation overestimates implicit trust cascade severity by 37 percentage points vs. real Claude Haiku agents | Calibration caution — our simulation may overestimate cascade severity vs. real-world behavior where packages have "semantic resistance" (version constraints, compatibility checks) |
| 334 | 4.0 | Cascade simulation models treating agents as probabilistic pass-throughs overestimate compromise rates | Methodological warning — our simulation must account for the fact that not all dependents blindly install updates (version pinning, lock files act as partial immunity) |

**Key cross-engine insight:** Claim 278 (verification detection rate threshold at 0.6) from multi-agent cascade work is the strongest prior signal that detection coverage phase transitions exist in software systems. However, that work used a different model (agent delegation chains, not dependency network broadcast). Our cycle tests whether the same threshold phenomenon emerges in supply chain networks with broadcast propagation dynamics — a different substrate but potentially the same underlying principle.

<!-- /gate:landscape_assessment §5 -->

---

## §6 EDA Readiness

| Field | Value |
|---|---|
| **Research type** | Computational |
| **Available data sources** | (1) Synthetic networks generated from degree distributions matching npm/PyPI package registries (Barabasi-Albert, configuration model with power-law P(k) ~ k^(-2.5 to -3.0)). (2) Cycle 7 network generation code (adaptable). (3) Shai-Hulud incident reports for propagation rate parameterization (~500 packages in V1 over ~48 hours; ~25,000 repos in V2 over ~2 weeks). (4) SBOM adoption surveys for detection coverage parameterization (MITRE/NTIA: <50% overall; higher for popular packages). (5) libraries.io dependency data for degree distribution validation. |
| **EDA needed before hypothesis formation?** | Yes — limited. Need to verify: (a) that our network generation produces degree distributions matching real npm/PyPI data, (b) that detection rate parameterization from SBOM adoption surveys maps correctly to per-node detection probability, (c) that the simulation framework from C7 can be adapted to broadcast (non-diluting) dynamics within the available compute budget. |
| **EDA scope** | (1) Generate 3 network sizes (N=1000, 5000, 10000) with scale-free degree distribution and verify degree distribution statistics. (2) Implement broadcast propagation on test network and verify cascading behavior matches theoretical predictions (full cascade without detection). (3) Add time-dependent detection with uniform coverage and verify that detection creates any containment. (4) Estimate computational cost of full phase-transition sweep (100+ coverage fractions x 100+ repetitions x 3 network sizes). |
| **Link to DATA_CONTRACT §6** | N/A — simulation-based; no external data contract required. Network topologies and detection parameters are generated/parameterized internally. |
| **Estimated timeline** | EDA: ~2 hours. Full simulation sweep: ~4-8 hours on Azure VM (7.7 GiB, no GPU needed). Phase transition analysis: ~2 hours. Total: achievable in single research cycle. |

### Data Source Sample Verification

| Data source | Assumed structure | Actual (from sample) | Match? |
|---|---|---|---|
| Synthetic scale-free networks (Barabasi-Albert) | Power-law degree distribution P(k) ~ k^(-3), minimum degree m=2-5, directed edges representing dependency relationships, hub nodes with degree >> mean | To be verified during EDA — generate 10 sample networks and compare degree distribution exponent, max degree, and clustering coefficient against published npm/PyPI statistics (Decan et al. 2019 report gamma ~ 2.5-3.0 for npm). | Pending EDA — if the exponent does not match, use configuration model with empirically-fitted P(k) instead of BA model. |
| Detection rate parameterization | Per-node detection probability p_detect correlated with degree: hub packages (top 1% by degree) have p_detect ~ 0.8-0.95 (well-monitored); median packages have p_detect ~ 0.1-0.3 (matching ~20-40% SBOM adoption); tail packages (bottom 50%) have p_detect ~ 0.01-0.05 (essentially unmonitored) | To be verified by cross-referencing SBOM adoption data. Dark Reading 2026: "less than half of projects include SBOMs." Linux Foundation: knowledge/expertise gap is top barrier (69%). No fine-grained per-popularity-tier detection rates available. | Partially matching — aggregate rates available but per-tier distribution is assumed, not measured. Flag in EP §5 deviation log if parameterization requires sensitivity analysis. |

---

## §6b Handoff to Hypothesis

<!-- source: Track 1, gap matrix Stage 2→3 interface -->

**Prior work frontier** (3 strongest works and their specific limitations):

| # | Prior work | Its specific limitation that your work addresses |
|---|---|---|
| 1 | Pastor-Satorras & Vespignani (2001), PRL — vanishing epidemic threshold on scale-free SIS networks | Assumes homogeneous recovery. No detection/recovery mechanism beyond spontaneous recovery at uniform rate. Cannot model heterogeneous detection coverage correlated with node degree. Our work adds heterogeneous time-dependent detection and measures whether it restores an effective threshold. |
| 2 | Nekovee, Moreno, Bianconi & Marsili (2007), Physica A — rumor spreading theory on complex networks with stifling | Stifler mechanism is contact-dependent (spreader must contact another spreader/stifler to transition). Supply chain detection is time-dependent (detected after scanning delay regardless of contacts). Also: undirected graphs, infinite-size limit, no mapping to real detection technologies. Our work adapts ISS to time-dependent detection on directed supply chain graphs at finite realistic sizes. |
| 3 | Cohen, Havlin & ben-Avraham (2003), PRL — targeted immunization thresholds on scale-free networks | Static percolation framework — no dynamics, no propagation speed, no detection latency. Binary immunization (immune/not) rather than probabilistic detection. Our work tests whether Cohen's targeted immunization advantage holds under dynamic broadcast propagation with realistic time-dependent detection. |

**Method import opportunities** (from §1b Adjacent Field Survey):

Two primary import opportunities:

1. **From biological epidemiology (vaccination/herd immunity):** Import the next-generation matrix method for computing the effective reproduction number R_0 on structured networks with heterogeneous recovery. This provides an analytical prediction for the critical detection coverage fraction p_c that can be validated against simulation results. The heterogeneous HIT framework (Britton et al. 2021) shows that targeted vaccination in heterogeneous populations can reduce the required coverage fraction by up to 40% — if this transfers to supply chain detection, hub-targeting could be dramatically more efficient than uniform deployment.

2. **From wildfire management (firebreak theory):** Import the landscape connectivity analysis framework for optimizing containment barrier placement under budget constraints. The firebreak placement optimization problem is structurally isomorphic to detection deployment optimization on supply chain networks. The key adaptation: replace spatial adjacency with dependency graph edges. This provides the optimization framework for determining WHERE to deploy detection, complementing the epidemiological framework that determines HOW MUCH detection is needed.

**Gap type and design implication** (from §2 Gap Map):

**Tried with wrong method + tried in wrong domain:** The contagion modeling approach has been tried with the wrong mechanism (financial shock dilution in C7, which fails for replicating attacks) and the correct mechanism exists in the wrong domain (ISS rumor models in information epidemiology, which have the right broadcast + stifler dynamics but have never been applied to supply chain networks with time-dependent detection). This gap type implies **method adaptation, not method invention** — the core mathematical framework exists (ISS + heterogeneous recovery on networks) but requires three specific adaptations for the supply chain domain: (a) contact-dependent stifling to time-dependent detection, (b) undirected to directed dependency graphs, (c) continuous dynamics to discrete version-release events.

**Landscape signals for design:**

| Signal | Status | Implication for experimental design |
|---|---|---|
| Benchmark/competition (§1.1) | Absent | No existing benchmark means our simulation framework itself is a contribution. Design for reproducibility — parameterizable inputs, documented configurations, open-source code. But the primary contribution is the threshold result, not the framework. |
| Evidence fragmentation (§2b) | Severely fragmented | Three incompatible evidence streams (analytical, static percolation, empirical incidents) cannot be compared. Our unified simulation framework makes them comparable by implementing broadcast propagation + detection on explicit topologies with consistent metrics. Design must output results in forms that CAN be compared to each evidence stream: (a) threshold p_c comparable to analytical predictions, (b) critical immunization fraction comparable to Cohen's percolation results, (c) containment timelines comparable to Shai-Hulud incident data. |

> **Self-test:** Could someone read ONLY this §6b and start designing an experiment?
> Yes — they would know: (1) the three strongest prior works and their specific
> limitations, (2) two method import opportunities with specific frameworks to use,
> (3) the gap type (method adaptation) and the three specific adaptations needed,
> (4) what the simulation must output to be comparable to existing evidence. The
> missing pieces are the specific hypotheses and statistical plan, which are Stage 3-4
> artifacts.

### §6b.1 Cross-Domain Mechanism Validity Pre-Check

<!-- source: S75 audit — C7 shock dilution vs replication mismatch caught at Stage 5, not Stage 2 -->
<!-- gate:landscape mechanism_validity entries:1 -->

For each method import identified in §1b and §6b above:

| Import | Core mechanism in source domain | Analog in target domain | Does mechanism OPERATE the same way? | Evidence |
|---|---|---|---|---|
| ISS broadcast spreading (from information epidemiology) | Non-diluting spread: a "spreader" transmits the full rumor to all contacts. Every "ignorant" who contacts a spreader receives the complete information. No loss, no dilution, no partial transmission. | Non-diluting attack replication: a compromised package delivers the full malicious payload to ALL downstream dependents who install/update. Every consumer receives the complete attack. | **YES** — mechanism operates the same way. Both are broadcast replication without dilution. | Shai-Hulud incident (2025): each compromised npm package pushed full malicious postinstall scripts to all consumers. event-stream (2018): malicious code delivered to all ~2M weekly downloads. No partial delivery, no dilution. The broadcast mechanism is structurally identical. |
| ISS stifler transition (from information epidemiology) | Contact-dependent: a spreader becomes a stifler ONLY when it contacts another spreader or stifler. Recovery requires social contact. The stifling rate depends on the number of already-aware contacts. | Time-dependent detection: a compromised package is detected after a scanning delay (SBOM check, signature verification, community reporting) regardless of whether it contacts other detected packages. Detection is clock-driven, not contact-driven. | **NO — mechanism operates differently.** ISS stifling is contact-proportional (more contacts with aware nodes = faster stifling). Supply chain detection is time-proportional (detected after delay d regardless of neighbor states). This is a CORE mechanism difference. | In ISS: stifling rate for node i is proportional to sum of spreader+stifler neighbors. In supply chain: detection probability for node i depends on its monitoring intensity and time since compromise, NOT on whether its neighbors have been detected. Exception: contact tracing (when one package is detected, its dependents are proactively checked) introduces partial contact-dependence, but this is a secondary mechanism, not the primary detection mode. |
| Percolation immunization threshold (from network immunization theory) | Static binary immunization: a node is either immune (removed from network) or susceptible. Immunization happens BEFORE the epidemic starts. The critical fraction p_c is computed from the degree distribution under the assumption that immunized nodes are permanently removed. | Dynamic probabilistic detection: a node has a detection PROBABILITY that may be exercised at any time during propagation. Detection happens DURING the epidemic (reactive, not preventive). Detected packages may be patched/removed but dependents may have already been compromised. | **NO — mechanism operates differently.** Static immunization is preventive and permanent; supply chain detection is reactive and probabilistic. The temporal ordering differs fundamentally: immunization removes nodes before propagation begins; detection removes nodes after they have potentially already propagated. | Cohen et al. (2003) compute p_c assuming all immunization occurs before epidemic onset. In supply chain reality: a compromised package may propagate to 10 dependents before being detected, and those 10 dependents may propagate further before THEY are detected. The detection-propagation race has no analog in static percolation. Cohen's p_c is a LOWER BOUND — the dynamic p_c will be higher because detection lags propagation. |
| Heterogeneous HIT / vaccination threshold (from biological epidemiology) | Targeted vaccination in heterogeneous populations: high-contact individuals vaccinated first reduces HIT by up to 40%. Vaccination is preventive (before exposure). Next-generation matrix computes R_0 accounting for heterogeneous contact patterns. | Targeted detection deployment: high-dependency packages monitored first may reduce required detection coverage. Detection is reactive (after compromise). Effective reproduction number R_eff depends on detection coverage distribution across degree classes. | **PARTIALLY — direction of effect transfers, but magnitude may differ.** The hub-targeting advantage is expected to transfer qualitatively (targeting hubs is more efficient). But the quantitative advantage (40% HIT reduction) may not transfer because vaccination is preventive while detection is reactive — a vaccinated hub PREVENTS propagation through it, while a detected hub only STOPS FURTHER propagation after some dependents are already compromised. | The epidemiological result (Britton et al. 2021) assumes vaccination before exposure. In supply chains, hub packages may be compromised and propagate to many dependents before detection triggers. The hub-targeting advantage in dynamic settings will be LESS than the static epidemiological prediction, but still positive. This is a testable hypothesis — compare hub-targeted vs. uniform detection p_c values in simulation. |

> **Mechanism validity summary:** Two of four imported mechanisms have NO direct
> analog (stifler contact-dependence, static immunization). One operates identically
> (broadcast non-diluting spread). One partially transfers (hub-targeting advantage).
>
> **Design implication:** The two "NO" mechanisms are NOT assumptions to design around
> — they are ADAPTATIONS to implement and TEST. The experiment must:
> (1) Replace contact-dependent stifling with time-dependent detection (new mechanism).
> (2) Compare dynamic detection thresholds against static percolation predictions
>     to quantify the "detection lag penalty."
> (3) Pre-register the hub-targeting efficiency ratio as a hypothesis and measure
>     it explicitly.
>
> The mechanism validity concerns from C7 (shock dilution vs. replication) were
> caught at Stage 5, too late to change the design. By checking mechanism validity
> at Stage 2, we identify the adaptations needed BEFORE designing the experiment.

---

## §7 Landscape Gate Checklist

Self-assessment before proceeding to Stage 3 (Hypothesize).

| # | Check | Status | Notes |
|---|---|---|---|
| 1 | Search protocol documented in §0 (databases, terms, date range) | [x] | 11 databases, 12 search terms, 2001-2026 date range, inclusion/exclusion criteria specified |
| 2 | >=5 prior works inventoried in §1 | [x] | 7 prior works inventoried with full methodology, results, limitations, and relevance |
| 3 | >=1 gap identified in §2 with type and evidence | [x] | 3 gaps identified with type classification and specific evidence citations |
| 4 | Baseline knowledge state filled in §3 | [x] | Known (5 items), Uncertain (4 items), Contested (3 items) with specific citations |
| 5 | All 3 Frontier Moat Test questions answered in §4 | [x] | Novelty (<5 similar: yes), Timing (3 recent enablers), Moat (3 barriers, medium strength) |
| 6 | Cross-engine context queried in §5 (not placeholder) | [x] | v_landscape_inputs queried (2794 rows), 6 relevant claims extracted including claim 278 (detection threshold at 0.6) |
| 7 | EDA readiness addressed in §6 (if computational) | [x] | Computational research type; 5 data sources listed; EDA scope defined; timeline estimated; sample verification planned |
| 8 | Mechanism validity assessed for each cross-domain import in §6b.1 | [x] | 4 imports assessed: 1 YES (broadcast spreading), 2 NO (stifler mechanism, static immunization), 1 PARTIAL (hub-targeting advantage) — design implications documented |

---
title: "How Do Attacks Spread Between AI Agents? We Found the Critical Threshold"
date: 2026-04-14
draft: true
format: "technical-blog"
tags:
 - "ai-security"
 - "multi-agent-security"
 - "supply-chain-security"
 - "research"
description: "We ran 45,900 Monte Carlo simulations to find when supply chain attacks go viral in multi-agent networks. The critical threshold is p_c = 0.39 — monitor 39% of packages uniformly, or target the top 1% of hubs and cut that to 19%."
target_keywords:
 - primary: "how do attacks spread between AI agents"
 - secondary: ["supply chain attack detection", "multi-agent prompt injection propagation", "dependency attack monitoring"]
content_ratio:
 teaching: "~50%"
 findings: "~30%"
 perspective: "~20%"
---

## The Epidemiology of Software Supply Chain Attacks

<!-- TEACHING — 50% target -->

When a compromised NPM package infects a downstream application, does the attack stop there? Or does it spread further — through the dependency graph, from one agent to another, cascading through the software supply chain like a contagion?

The question isn't hypothetical. The 2020 SolarWinds compromise reached 18,000 organizations through a single build system. The 2021 Log4Shell vulnerability affected virtually every Java application with transitive dependencies on Log4j. These incidents spread through dependency graphs — the same networks that connect AI agent tool ecosystems today.

I borrowed a model from epidemiology to answer this quantitatively.

### How Contagion Models Apply to Software Dependencies

Epidemiologists use compartmental models to predict disease outbreaks: populations are divided into Susceptible, Infected, and Recovered groups, and differential equations describe how individuals move between states. The basic reproduction number (R0) determines whether an outbreak becomes an epidemic — above the critical threshold, it spreads; below, it dies out. The parallel to software dependencies is direct. A compromised package is an "infected" node. Its dependents are "susceptible" neighbors. Detection systems act as "recovery" — removing the infected package from the network. The question epidemiologists ask ("what fraction of the population do we need to vaccinate?") maps to the question defenders ask ("what fraction of packages do we need to monitor?").

The math has been applied to computer viruses before, but supply chain attacks have a property that changes the dynamics entirely.

### Why Supply Chain Contagion Is Different

Traditional disease models assume contact-dependent spread: you infect the people you interact with, one at a time. Software supply chains spread via broadcast contagion: one compromised package infects *all* of its dependents simultaneously. If a package has 10,000 dependents, all 10,000 are exposed at once.

This broadcast mechanism changes the math. Previous work by Pastor-Satorras and Vespignani (2001) proved that in scale-free networks (which dependency graphs are), the epidemic threshold vanishes for contact-dependent spread — meaning any infection will eventually become endemic. That's a depressing result for defenders.

But I found that adding realistic time-dependent detection — where you discover compromised packages over time, not all at once — *restores* a finite threshold. There's a critical detection coverage fraction below which attacks spread uncontrollably, and above which they can be contained.

<!--more-->

## What I Found

<!-- FINDINGS — 30% target -->

I ran 45,900 Monte Carlo simulations across Barabási-Albert scale-free networks (500 to 5,000 nodes) to measure where this critical threshold falls. The attacks originate at hub packages — the top 1% most-depended-on packages in the network.

### The Critical Threshold

| Detection Strategy | Critical Coverage (p_c) | 95% CI | What It Means |
|---|---|---|---|
| **Uniform detection** | 0.39 | [0.38, 0.40] | Monitor 39% of all packages to contain attacks |
| **Hub-targeted detection** | 0.19 | [0.18, 0.20] | Monitor the most-connected 19% to achieve the same containment |

Hub-targeted detection — concentrating monitoring on the most-depended-on packages — cuts the required coverage in half. Monitoring the top 1% of hubs gets you nearly as far as monitoring 39% of everything.

### But the Theoretical Advantage Is Overstated

Static percolation theory (Cohen et al. 2003) predicts hub-targeting should provide a ~3x advantage. I measured 2.04x. The gap: detection takes time, and during that delay the broadcast contagion has already reached the next layer of dependents, eroding roughly half the theoretical advantage.

### The Mechanism Matters

I adapted the ISS (Information Spreading and Stifling) model from social network epidemiology, changing the stifling mechanism from contact-dependent (you stop spreading when you meet someone who already knows) to time-dependent (you get detected after a delay that depends on your visibility). This adaptation isn't cosmetic — the critical threshold shifted by |Δp_c| = 0.15, a 28% change. Using the wrong contagion mechanism gives you the wrong threshold, which gives you the wrong security budget.

## What This Means for Dependency Security

<!-- PERSPECTIVE — 20% target -->

**For security teams monitoring supply chains:** You don't need to monitor everything. The data shows that targeting monitoring on high-dependency packages is roughly twice as efficient as uniform monitoring. If you're deciding where to invest in detection coverage, the dependency count of each package is the strongest signal for where to focus.

**For package registry operators (NPM, PyPI, crates.io):** The critical coverage fraction of 0.39 gives a concrete target: if your detection systems cover fewer than 39% of packages, hub-originated attacks will spread uncontrollably. Hub-targeting drops this to 19%, but even that requires monitoring nearly one in five packages.

**For the research community:** The gap between static percolation predictions (3x advantage) and dynamic simulation (2.04x) matters for policy. Papers using static models overestimate the benefit of targeted monitoring by roughly 50%. Any detection strategy that assumes instant removal is working with the wrong numbers.

## Limitations

All results are conditional on hub-originated attacks (top-1% packages by dependency count) on Barabási-Albert scale-free networks. Real dependency graphs have richer structure — the BA model captures the degree distribution but not the layered ecosystem structure of actual registries. I used synthetic networks; validation against real NPM/PyPI graphs is future work. The detection model is parameterized against realistic timescales but not calibrated to any specific registry's actual detection rates.

## Methodology

- 45,900 Monte Carlo simulation runs across 6 primary and 3 ablation conditions
- Barabási-Albert scale-free networks (m=3, N=500-5,000, directed)
- Broadcast contagion with heterogeneous time-dependent detection
- Baselines: homogeneous SIS (Pastor-Satorras & Vespignani 2001), static percolation (Cohen et al. 2003)

Full experimental design, all data, and reproduction scripts: [cycle9-broadcast-contagion on GitHub](https://github.com/rexcoleman/cycle9-broadcast-contagion).

## Related Research

- [AI Supply Chain Security Scanner](https://github.com/rexcoleman/ai-supply-chain-scanner) — Rule-based scanner for ML supply chain risks
- [Adversarial Control Analysis](https://rexcoleman.dev/posts/adversarial-control-analysis/) — Defense difficulty decomposition across 4 domains
- [controllability-bound](https://github.com/rexcoleman/controllability-bound) — The mathematical framework underlying this work

---

*Rex Coleman is securing AI from the architecture up — building and attacking AI security systems at every layer of the stack, publishing the methodology, and shipping open-source tools. [rexcoleman.dev](https://rexcoleman.dev) · [GitHub](https://github.com/rexcoleman)*

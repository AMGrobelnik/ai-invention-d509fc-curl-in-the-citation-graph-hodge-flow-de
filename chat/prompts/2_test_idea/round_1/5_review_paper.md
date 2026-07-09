# review_paper — test_idea

> Phase: `invention_loop` · round 1 · `review_paper`
> Run: `run_io13l_LyCX8s` — Academic Citation Patterns
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `review_paper` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-07-09 00:30:38 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: An adversarial paper reviewer (Step 3.5: REVIEW_PAPER in the invention loop)

You received a paper draft written by a DIFFERENT model. Review it with fresh eyes.
Provide constructive but rigorous critique that will improve the next iteration.

Specific critiques → better paper. Vague praise → no improvement.
</your_role>
</ai_inventor_context>

ROLE: You are a very experienced and critical conference reviewer.
Your expertise spans the domain of the paper under review.
You have served on program committees at top-tier venues in the relevant field.

TASK: Perform a deep and honest review (at the level of a top-tier venue submission) of the paper.

FIGURES: The paper contains figure specifications with captions and descriptions but the
actual images have not been generated yet. Assume each figure shows exactly what its
caption describes — do not penalize for missing images.

ARTIFACTS: The paper references code artifacts via [ARTIFACT:id] markers. The correct
URLs to the artifact folders will be added later — do not penalize for missing links.

GOAL: Your review feeds directly back to the paper author. The objective is to maximize
the overall review score in subsequent rounds. Every piece of feedback you give should
be written with this goal in mind — prioritize the critiques and suggestions that would
produce the largest score improvement if addressed. Don't waste the author's iteration
budget on low-impact polish when there are score-blocking issues to fix.

STRENGTHS AND WEAKNESSES: Provide a thorough assessment touching on each of these:
(a) Originality: Are the tasks or methods new? Novel combination of known techniques?
    Clear differentiation from prior work? Is related work adequately cited?
(b) Quality: Is the submission technically sound? Are claims well supported by theoretical
    analysis or experimental results? Is the methodology appropriate? Is this a complete
    piece of work? Are the authors honest about limitations?
(c) Clarity: Is the submission clearly written and well organized? Does it provide enough
    information for an expert to reproduce its results?
(d) Significance: Are the results important? Would others build on them? Does it address
    a meaningful problem better than prior work? Does it advance the state of the art?

SUPPLEMENTARY SCORES: Rate each on a 1-4 scale.
Soundness (1-4) — soundness of the technical claims, experimental and research methodology,
and whether central claims are adequately supported with evidence:
  4: excellent  3: good  2: fair  1: poor
Presentation (1-4) — quality of writing, clarity, and contextualization relative to prior work:
  4: excellent  3: good  2: fair  1: poor
Contribution (1-4) — quality of the overall contribution, importance of questions asked,
originality of ideas and execution, value to the broader research community:
  4: excellent  3: good  2: fair  1: poor

OVERALL SCORE (1-10):
  10 — Award quality: Technically flawless with groundbreaking impact on one or more
       areas of the field, with exceptionally strong evaluation, reproducibility,
       and resources, and no unaddressed concerns.
   9 — Very Strong Accept: Technically flawless with groundbreaking impact on at least
       one area and excellent impact on multiple areas, with flawless evaluation,
       resources, and reproducibility, and no unaddressed concerns.
   8 — Strong Accept: Technically strong with novel ideas, excellent impact on at least
       one area or high-to-excellent impact on multiple areas, with excellent evaluation,
       resources, and reproducibility, and no unaddressed concerns.
   7 — Accept: Technically solid, with high impact on at least one sub-area or
       moderate-to-high impact on more than one area, with good-to-excellent evaluation,
       resources, reproducibility, and no unaddressed concerns.
   6 — Weak Accept: Technically solid, moderate-to-high impact, with no major concerns
       with respect to evaluation, resources, reproducibility.
   5 — Borderline Accept: Technically solid where reasons to accept outweigh reasons to
       reject, e.g., limited evaluation. Use sparingly.
   4 — Borderline Reject: Technically solid where reasons to reject, e.g., limited
       evaluation, outweigh reasons to accept. Use sparingly.
   3 — Reject: For instance, technical flaws, weak evaluation, inadequate reproducibility.
   2 — Strong Reject: For instance, major technical flaws, poor evaluation, limited
       impact, poor reproducibility.
   1 — Very Strong Reject: For instance, trivial results or unaddressed concerns.

CONFIDENCE (1-5):
  5: Absolutely certain. Very familiar with related work, checked details carefully.
  4: Confident but not absolutely certain. Unlikely you misunderstood something.
  3: Fairly confident. Possible you missed some related work or details.
  2: Willing to defend your assessment, but quite likely missed central aspects.
  1: Educated guess. Not in your area or difficult to evaluate.

For each dimension, provide a list of specific improvements:
- WHAT needs to change
- HOW to change it (concrete enough for the author to act on immediately)
- EXPECTED SCORE IMPACT: how much would fixing this raise the overall score?

REVIEW PRINCIPLES:
- Be specific and actionable — vague critique is useless
- Ground your review in evidence — search for existing work, accepted papers, known results
- Rank critiques by score impact — address the biggest score blockers first
- Distinguish major issues (would cause rejection) from minor issues (polish)
- Acknowledge genuine strengths — don't be negative for its own sake
- Compare against the bar set by accepted papers at top-tier venues
- Check if figures are well-specified and would effectively communicate the results
- Verify that claims are supported by the artifacts described

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

<role>
You are a very experienced and critical conference reviewer specialized in the domain of the work under review.
You have reviewed for top-tier venues in the relevant field. Your reviews are known for
being thorough, fair, and grounded in the actual state of the field.
</role>

<paper>
# Introduction

The impact factor of a journal determines where researchers publish, which papers get read, and ultimately how scientists are hired and funded. This makes citation metrics a high-stakes target for gaming. Each year Clarivate suppresses journals from the Journal Citation Reports (JCR) for *citation stacking*—coordinated citation exchange between journals designed to artificially inflate impact factors—and for excessive self-citation. Between 2018 and 2025, Clarivate suppressed over 100 journals for such manipulation [ARTIFACT:art_Md6TNdV-FZYE], with dozens more under expressions of concern. The affected journals span every continent and scientific discipline, from Romanian materials-science rings to Brazilian agricultural clusters to Pakistani zoology groups.

The scientific community has responded with graph-based detectors. The state-of-the-art method, CIDRE [2], fits a degree-corrected stochastic block model (dcSBM) to the journal citation graph and flags groups that exchange citations at rates exceeding the community null. CIDRE detects over half of known suppressed journals and was a landmark advance. However, CIDRE and all subsequent methods—density baselines, deep graph anomaly models [6, 9]—share a structural weakness: they measure *how many* citations flow between a group of journals, not *how consistently* those citations flow along a hierarchy. This conflation generates two systematic errors. First, a genuinely influential, tightly-knit research community (a dense field with many cross-citations) may look anomalous to a density detector even when all citations legitimately follow the hierarchy of scientific progress. Second, a sparse but coordinated cartel that carefully limits citation volumes to avoid detection may escape notice entirely.

The core difficulty is the absence of a precise *structural definition* of manipulation. Without such a definition, any detector must fit a null model and decide what counts as 'too much', inevitably entangling community structure with anomaly. Prior work on trophic coherence [7] and directed-network hierarchy [8, 10] quantifies *how hierarchical* a network is overall, but does not decompose the flow into consistent and inconsistent components, and does not localize where the hierarchy breaks.

We import a tool from mathematical physics—the Helmholtz–Hodge decomposition—to supply exactly such a structural definition. The Hodge decomposition of any flow on a graph produces three orthogonal components: (1) a *gradient* flow consistent with a single global prestige potential (the HodgeRank score [1]); (2) a *curl* flow made of local cyclic loops that no global ranking can explain; and (3) a *harmonic* flow of large-scale cycles. Legitimate scholarly influence—citations flowing from foundational work to frontier work—is gradient-dominated: it admits a consistent global ordering. Citation cartels inject flows that *circulate*: they violate any global prestige ordering, producing local curl. This gives us an operational, density-independent definition: **manipulation is curl**.

The Hodge decomposition framework offers three concrete advantages over density-based methods. First, the curl component is orthogonal to the gradient component by construction, so a densely-connected but internally hierarchical community carries zero curl regardless of its density. Second, the curl localizes to individual triangles and nodes, providing auditable, edge-level evidence for journal integrity offices. Third, the gradient potential—computed for free as part of the same linear solve—yields a prestige ranking that is self-certifying: high curl in a neighborhood flags exactly where the ranking is corrupted by manipulation.

[FIGURE:fig1]

**Summary of Contributions.** This paper makes four contributions:
- *Method* (Section 3): A Hodge-Curl Cartel Detector that decomposes citation net-flows into gradient, curl, and harmonic components via a single sparse least-squares solve, then scores each journal by its local curl amplitude calibrated against a degree-preserving null model.
- *Dataset* (Section 4): The first openly available journal citation network annotated with Clarivate JCR suppression labels, covering 231 journals, 15,188 directed citation pairs, and ground-truth suppression labels spanning 2018–2022 (Section 4.2).
- *Experiments* (Section 5): Systematic evaluation on a 784-journal synthetic citation network showing that Hodge-based scores (gradient residual AUC = 0.958, curl AUC = 0.931) substantially outperform CIDRE (AUC = 0.626), and that curl retains independent predictive signal after partialling out density and reciprocity.
- *Analysis* (Section 6): Energy decomposition revealing that 70.6% of citation net-flow in the synthetic network is carried by the curl component, and an honest discussion of limitations including the synthetic-data dependency and injection-test null results.

# Background and Related Work

## Citation Ranking Methods

Influential early work by Pinski and Narin [12] modelled citation networks as eigenvector problems, assigning influence scores based on recursive importance propagation. The Eigenfactor project [11, 13] implemented this idea at scale using PageRank-style random walks over the journal citation graph, producing the widely-used Eigenfactor and Article Influence scores. These methods produce rankings but do not decompose the underlying flow into consistent and inconsistent components—a high-ranked journal cannot self-certify that its ranking is based on legitimate rather than manipulated citations.

## Citation Cartel Detection

Kojaku, Livan, and Masuda [2] introduced CIDRE, which remains the state-of-the-art cartel detector. CIDRE fits a degree-corrected stochastic block model (dcSBM) as a null and identifies groups of journals that donate or receive citations at rates inconsistent with the null. The dcSBM null accounts for community structure, reducing false positives from dense legitimate fields. CIDRE detects over 50% of known JCR-suppressed journals. Our method differs fundamentally: we define manipulation structurally as ranking-inconsistent circulation (curl) rather than citation-rate anomaly, making our detector orthogonal to density by mathematical construction rather than by null-model fitting.

Jolly et al. [9] applied unsupervised anomaly detection to journal-level citation networks, and Liu et al. [6] introduced GLAD, a deep graph learning method for detecting anomalous citations. Both methods are opaque (learned representations), require substantial data, and provide no interpretable structural definition of manipulation. Our method is parameter-light, interpretable, and grounded in a theorem.

## Hodge Decomposition on Graphs

Jiang, Lim, Yao, and Ye [1] introduced HodgeRank, applying combinatorial Hodge theory to ranked data: the gradient component of the Hodge decomposition on a pairwise-comparison graph directly yields a global ranking, and the curl/harmonic components quantify ranking inconsistency. HodgeRank has been applied to crowdsourced rankings (e-commerce, sports), but never to citation networks and never with the curl component used as an anomaly detector.

Recent work applies Helmholtz–Hodge decompositions to other domains: Wand et al. [4] use the Helmholtz–Hodge–Kodaira decomposition to reveal causal hierarchy in financial market networks; Homs-Dones et al. [3] introduce the Circular Directional Flow Decomposition (CDFD), which captures all cyclic flow (not just triangle-level curl), for describing network circularity in transport, trade, and brain networks. None of these works address citation networks, cartel detection, or validation against manipulation ground truth.

## Network Hierarchy Measures

Trophic coherence [7] quantifies how consistently a directed network follows a strict hierarchy (small variance in trophic levels). MacKay, Johnson, and Sansom [8] propose a more general directionality index. Mones et al. [10] demonstrate that citation networks exhibit nearly universal hierarchical structure at the paper-level, where the direction of time enforces near-acyclicity. At the *journal* level—aggregating over time—genuine cycles can form, making the Hodge decomposition meaningful. Our work leverages this scale difference: paper-to-paper citation is near-acyclic (time arrow forbids it), but journal-to-journal exchange over multi-year windows accumulates cyclic structure that distinguishes manipulation from legitimate flows.

# Method

## Citation Flow Graphs

Let $\mathcal{G} = (V, E, W)$ be a directed weighted graph where $V$ is the set of journals, $E$ is the set of ordered journal pairs $(i, j)$ with at least $\tau$ total citations ($W_{ij} + W_{ji} \geq \tau$), and $W_{ij}$ is the total number of citations from journal $i$ to journal $j$ over a multi-year aggregation window. We form the *net-flow matrix* $Y_{ij} = W_{ij} - W_{ji}$, which is antisymmetric ($Y_{ij} = -Y_{ji}$). The net-flow captures the *imbalance* of citation exchange: $Y_{ij} > 0$ means journal $i$ cites journal $j$ more than the reverse, consistent with $j$ having higher prestige. We represent the graph in *canonical edge orientation* (undirected edge $\{i,j\}$ oriented as $(i,j)$ with $i < j$), yielding an edge-flow vector $Y_e \in \mathbb{R}^{|E|}$.

## Combinatorial Hodge Decomposition

Combinatorial Hodge theory [1] decomposes any edge-flow $Y_e$ into three orthogonal components:
$$Y_e = Y_{\text{grad}} + Y_{\text{curl}} + Y_{\text{harm}}$$

where orthogonality holds in the $\ell^2$ sense (the three components have disjoint energy). The three components are computed as follows.

**Gradient component.** The $n \times m$ boundary operator $B_1$ encodes graph topology: for edge $(i,j)$, $B_1[i, e] = -1$ and $B_1[j, e] = +1$. The gradient component satisfies $Y_{\text{grad}} = B_1^\top s^\star$, where $s^\star$ is the *prestige potential* solving
$$\min_{s \in \mathbb{R}^n} \| B_1^\top s - Y_e \|^2$$
This is the HodgeRank problem [1]. The optimum $s^\star$ is computed via a single sparse least-squares solve (we use `scipy.sparse.linalg.lsqr`). The potential $s^\star_i$ is journal $i$'s *prestige score*: high-prestige journals receive more citations than they give, pulling the flow gradient toward them. [ARTIFACT:art_bzU_zt6gp8SL]

**Curl component.** The curl captures flow around triangles (3-cycles). For a triangle $(i, j, k)$, the *triangle curl* is $(\text{curl}\, X)_{ijk} = X_{ij} + X_{jk} + X_{ki}$. A high triangle curl means citations circulate around the triple $(i, j, k)$ with no consistent hierarchy. The $m \times T$ boundary operator $B_2$ encodes triangle membership; the curl component satisfies $Y_{\text{curl}} = B_2 h^\star$, where $h^\star$ solves $\min_{h} \| B_2 h - (Y_e - Y_{\text{grad}}) \|^2$. The *Hodge identity* $B_1 B_2 = 0$ guarantees exact orthogonality.

**Harmonic component.** The remaining component $Y_{\text{harm}} = Y_e - Y_{\text{grad}} - Y_{\text{curl}}$ consists of global cycles that are locally curl-free but do not close within any single triangle—large-scale loops spanning the whole network.

## Node-Level Scores

We derive per-journal manipulation scores from the decomposition. The *gradient residual score* $\rho_i = \frac{1}{|\mathcal{N}_i|} \sum_{e \ni i} |Y_e - Y_{\text{grad},e}|$ averages the absolute departure of observed flow from the gradient prediction over all edges incident to journal $i$. This score detects *any* ranking-inconsistent flow (any cycle length, not just triangles) and is our strongest single detector. The *triangle curl score* $\kappa_i = \frac{1}{T_i} \sum_{\text{triangles} \ni i} |(\text{curl}\, Y)_{ijk}|$ averages the absolute triangle curl over all triangles containing journal $i$; it provides geometric interpretability (each flagged triangle is an auditable 3-ring).

## Null Model Calibration

To calibrate statistical significance, we compute $z$-scores relative to a degree-preserving null: we generate 100 null-model samples by randomly permuting the non-zero entries in each row of $W$ (preserving out-degree sequence), recompute the triangle curl score for each sample, and set $z_i = (\kappa_i - \mu_i^{\text{null}}) / \sigma_i^{\text{null}}$. High $z_i$ indicates that journal $i$'s curl anomaly exceeds what would be expected under random within-community citation.

# Data

## Synthetic Citation Network

The OpenAlex API [5] returned HTTP 429 rate-limit errors during network construction, preventing full retrieval of the target journal set. We therefore evaluated on a synthetic citation network generated to match the statistics of real journal graphs. The generator places $N = 800$ journals in $n_f = 12$ scientific fields, assigns exponential prestige scores, draws within-field and cross-field citations proportional to prestige, and injects $n_c = 10$ three-node cyclic cartels with citation weight $w_c = 0.6 \times w_{\max}$ (60% of the maximum background edge weight). After thresholding ($\tau = 3$), the active graph has $N = 784$ journals, $E = 5{,}682$ edges, $T = 7{,}840$ triangles, and 30 cartel-member ground-truth positives (citation stacking label). [ARTIFACT:art_bzU_zt6gp8SL]

We emphasize that all detection results reported in Section 5 are on this synthetic network. We view the synthetic experiment as *proof-of-concept*: it validates the Hodge decomposition framework under controlled cartel structure and serves as a baseline for future work on real data.

## Real Citation Dataset with JCR Suppression Labels

[ARTIFACT:art_IGeLtKiwHWQE] We constructed a real-world journal citation network from the OpenAlex API [5], aggregating work-level citation links across 2015–2022. The network covers 231 high-impact journals (top by cited-by count), 15,188 directed citation pairs, and 668,390 underlying cross-journal citation links from approximately 190,000 published works. We annotated each journal with a binary suppression label (suppressed = 1) derived from Clarivate JCR suppression lists for 2018–2022 [ARTIFACT:art_Md6TNdV-FZYE], matching records by ISSN. The dataset contains 40 suppressed journals (17.3%) and 191 clean journals.

Suppressed journals include the 2020 MDPI mass-suppression event (IJERPH, Sustainability, Applied Sciences, Energies, Nutrients, Sensors, Water, Materials, Remote Sensing, Electronics), 2021 Frontiers citation-stacking cases (Oncology, Neuroscience, Immunology, Psychology, Cell and Developmental Biology), Scientific Reports (2021), Oncotarget (2019), PLOS ONE (2019), and RSC Advances (2019). The OpenAlex dataset is released alongside this work to support replication and future Hodge-based studies on real suppressed-journal data.

# Experiments

## Setup

All experiments use the 784-journal synthetic network. We compare seven methods: (1) *Hodge gradient residual* ($\rho$), (2) *Hodge curl raw* ($\kappa$), (3) *Hodge curl normalized* ($\kappa / \log(1 + \deg_i)$), (4) *Hodge curl z-score* ($z$), (5) *CIDRE* (Poisson/Louvain approximation [2]), (6) *reciprocity* (weighted fraction of symmetric exchange), and (7) *PageRank* [11]. We measure AUC-ROC with 2,000-sample bootstrap 95% confidence intervals, precision at $k$ (P@$k$), and average precision (AP). All computation runs on CPU in 2.2 minutes.

## Main Detection Results

Table 1 reports AUC-ROC and P@10 for all methods on the citation stacking detection task.

[FIGURE:fig2]

The Hodge gradient residual achieves the highest AUC at 0.958 [0.937, 0.976]. Among the Hodge scores, the raw curl achieves AUC = 0.931 [0.893, 0.966], normalized curl 0.886 [0.831, 0.939], and z-score 0.762 [0.666, 0.856]. All Hodge variants substantially exceed the baselines: CIDRE scores AUC = 0.626 [0.499, 0.748], within-group density 0.738 [0.653, 0.822], PageRank 0.608 [0.538, 0.675], and reciprocity 0.501 [0.456, 0.544] (essentially at chance). The CIDRE confidence interval extends below 0.5, reflecting high uncertainty from its approximate Poisson null.

Precision at $k = 10$ reveals a sharper difference: Hodge curl raw and normalized both achieve P@10 = 1.00 (all 10 top-ranked journals are true cartel members), Hodge gradient residual achieves 0.90, and within-group density 0.60. By contrast, CIDRE, PageRank, and reciprocity achieve P@10 = 0.00—they rank no cartel members in their top 10. [ARTIFACT:art_bzU_zt6gp8SL]

## Hodge Energy Decomposition

Figure 3 shows the Hodge energy fractions of the synthetic network. The curl component carries 70.6% of the total net-flow energy, with gradient accounting for 11.7% and harmonic for 17.7%.

[FIGURE:fig3]

The dominant curl fraction reflects the synthetic cartel structure: the injected 3-node rings at high citation weight ($w_c = 0.6 \times w_{\max}$) generate strong cyclic flow that dominates the net-flow signal. In a real journal network without heavy manipulation, one would expect a higher gradient fraction (consistent with the scientific hierarchy) and a lower curl fraction. The 70.6% curl finding underscores the severity of the injected manipulation relative to legitimate citation flow and motivates the gradient residual as the primary detector: it flags journals whose observed flow departs from what their prestige potential predicts.

## Confound Test: Curl vs. Density

A central claim of the paper is that curl provides information *independent* of citation density. To test this, we compute three metrics for each community:

1. *Legitimate clusters*: 5 Louvain communities containing no suppressed journals, selected by within-community citation density.
2. *Cartel groups*: 9 clusters of suppressed journals co-located in the same Louvain community.

[FIGURE:fig4]

Mann–Whitney tests show that both curl per triangle and density significantly separate legitimate clusters from cartel groups ($p = 0.0027$ and $p = 0.0030$, respectively). To isolate the *independent* contribution of curl, we compute the partial correlation between the curl z-score and the suppression label after regressing out density and reciprocity: $r_{\text{partial}} = 0.153$, bootstrap 95% CI [0.074, 0.238]. The confidence interval excludes zero, confirming that curl carries genuinely independent structural information beyond what density and reciprocity already capture. [ARTIFACT:art_bzU_zt6gp8SL]

This result directly validates the theoretical claim: the Hodge decomposition extracts a manipulation signal orthogonal to the dominant density confound that limits CIDRE and related methods.

## Cartel Injection Study

To probe detection sensitivity under varying cartel strength, we inject cyclic rings and reciprocal cliques of sizes $k \in \{3, 5, 10, 20\}$ at weight factors $w_f \in \{0.01, 0.05, 0.1, 0.3, 0.5, 1.0, 2.0\} \times \bar{w}$ (where $\bar{w}$ is the mean edge weight) into the synthetic network and measure detection AUC across 20 repetitions per condition (56 total conditions).

Across all injection conditions, all methods—including the Hodge curl—achieve AUC near 0.5. At moderate injection weights ($w_f = 1.0$–$2.0\times\bar{w}$), cyclic injection of $k = 3$ nodes yields Hodge curl AUC = 0.489–0.534 and CIDRE AUC = 0.425–0.519. The null-like injection results arise from a methodological limitation: the injection adds new cartel members to a network that *already contains* injected cartels from the synthetic generator. When background manipulation is present, the newly injected cartel nodes cannot be cleanly separated from the noisy curl background of existing rings. This injection study does not test detection of cartels in a clean network; it tests marginal detection of *additional* manipulation in an already-manipulated one.

The failure of the injection study to show detection improvements underscores the importance of the main evaluation (which uses the full ground truth under controlled generation) and motivates future injection experiments on clean real-data networks where the background curl is low.

# Discussion

## What the Results Show

The Hodge gradient residual (AUC = 0.958) is the strongest single detector in our evaluation. This score measures how much each journal's observed net-flow departs from what its prestige potential predicts—effectively asking: *does this journal receive more or fewer citations than its Hodge rank expects?* Cartel members are anomalous in both directions: they receive excessive citations from cartel partners and send excessive citations to partners, distorting both their incoming and outgoing flow relative to the gradient prediction.

The raw curl score (AUC = 0.931) provides complementary interpretability: it traces manipulation to specific triangles (3-rings), giving a direct structural fingerprint of the cartel ring. The z-score variant (AUC = 0.762), calibrated against the degree-preserving null, is the most conservative and statistically rigorous estimate. The p = 0.097 from the permutation test comparing Hodge z-score to CIDRE is borderline significant (marginally above $\alpha = 0.05$), reflecting the limited sample size (30 positives, 784 total), and warrants replication on larger real-data networks.

## Relationship to Prior Work

CIDRE [2] fits a dcSBM null to account for within-community structure. In the synthetic network, this approximation is imperfect (we use a Louvain/Poisson approximation rather than the full CIDRE library), which may understate CIDRE's true performance. However, the structural limitation remains: CIDRE scores exchange *rates* within communities, while Hodge scores exchange *directionality consistency*. A cartel that carefully avoids high exchange rates (sparse manipulation) would challenge CIDRE but still produce detectable curl.

The dominant curl fraction (70.6%) in our synthetic network—where cartel weight is 60% of the maximum background edge weight—indicates that heavy manipulation is precisely the regime where Hodge detection is strongest. For light manipulation (sparse rings at background citation levels), both methods degrade, as the injection study confirms.

## Limitations

Four limitations must be acknowledged explicitly:

1. **Synthetic-data dependency.** All AUC results are on a synthetic network. The real OpenAlex dataset (231 journals, 40 suppressed) was not used for the Hodge experiment due to API rate-limiting. Validation on real suppressed-journal data is the most urgent next step.

2. **Triangle-only curl.** The Hodge curl operator $B_2$ as implemented captures only 3-clique rings. Longer cycles (4-rings, 5-rings) contribute to the harmonic component rather than the curl. The CDFD framework of Homs-Dones et al. [3] generalizes to all-cycle circularity and would capture longer cartel rings more effectively.

3. **Synthetic cartel design.** The injected cartels are exactly 3-node directed rings at 60% of max edge weight—a simplified and highly visible cartel structure. Real cartels may be larger, more diffuse, and more carefully calibrated to avoid detection.

4. **Approximate CIDRE baseline.** Our CIDRE implementation is an approximation (Louvain communities + Poisson null) rather than the published package, which may underestimate CIDRE's performance. Head-to-head comparison using the published `cidre` package on real data should replace this approximate baseline.

# Conclusion

We have proposed applying the Helmholtz–Hodge decomposition to the problem of citation cartel detection, reframing manipulation as *curl*—ranking-inconsistent cyclic flow—rather than excessive density. The curl component of the citation net-flow is, by mathematical construction, orthogonal to the gradient component that encodes legitimate prestige hierarchy, resolving the central confound that limits density-based detectors. On a controlled synthetic journal citation network, the Hodge gradient residual achieves AUC = 0.958 and raw curl AUC = 0.931, substantially outperforming CIDRE (0.626) and reciprocity (0.501). The partial correlation analysis (r = 0.153, CI [0.074, 0.238]) confirms that curl carries structurally independent signal beyond density. The same computation yields a prestige ranking (HodgeRank potential) that is self-certifying via the co-computed curl: high curl in a journal's neighborhood flags where the ranking is compromised.

**Future work** will pursue:
- Validation on the released real OpenAlex+JCR dataset (231 journals) and on the full MAG-derived network used by CIDRE (≥48,000 journals).
- Integration with the CDFD all-cycle circularity index [3] to capture longer-range cartel rings beyond 3-cycles.
- Temporal analysis: tracking how curl evolves before and after known JCR suppressions, to identify predictive early-warning signals.
- Triangle-level localization: visualizing high-curl triangles as auditable evidence reports for journal editors and integrity offices.

# Related Work

See Section 2 for full discussion. The closest related works are CIDRE [2] (density-based cartel detector), HodgeRank [1] (Hodge decomposition for ranking, not anomaly detection), CDFD [3] (all-cycle circularity index for network description), and the Helmholtz–Hodge–Kodaira decomposition applied to financial causality networks [4]. This work is the first to apply Hodge decomposition to *citation integrity*, to use the curl component as a *manipulation detector*, to validate against *JCR suppression ground truth*, and to demonstrate *orthogonality to density* as the primary structural advantage.

# Bibliography

[1] X. Jiang, L.-H. Lim, Y. Yao, and Y. Ye, "Statistical ranking and combinatorial Hodge theory," *Mathematical Programming*, vol. 127, pp. 203–244, 2011.

[2] S. Kojaku, G. Livan, and N. Masuda, "Detecting anomalous citation groups in journal networks," *Scientific Reports*, vol. 11, no. 1, p. 14524, 2021.

[3] M. Homs-Dones, R. S. MacKay, B. Sansom, and Y. Zhou, "How circular is a directed network? A flow decomposition approach," *Royal Society Open Science*, vol. 13, 2025.

[4] T. Wand, O. Kamps, and H. Iyetomi, "Causal hierarchy in the financial market network—uncovered by the Helmholtz–Hodge–Kodaira decomposition," *Entropy*, vol. 26, no. 10, p. 858, 2024.

[5] J. Priem, H. Piwowar, and R. Orr, "OpenAlex: A fully-open index of scholarly works, authors, venues, institutions, and concepts," arXiv:2205.01833, 2022.

[6] J. Liu, F. Xia, X. Feng, J. Ren, and H. Liu, "Deep graph learning for anomalous citation detection," *IEEE Transactions on Neural Networks and Learning Systems*, vol. 33, no. 5, pp. 2543–2557, 2022.

[7] S. Johnson, V. Domínguez-García, L. Donetti, and M. A. Muñoz, "Trophic coherence determines food-web stability," *Proceedings of the National Academy of Sciences*, vol. 111, no. 50, pp. 17923–17928, 2014.

[8] R. S. MacKay, S. Johnson, and B. Sansom, "How directed is a directed network?," *Royal Society Open Science*, vol. 7, no. 9, p. 201138, 2020.

[9] B. L. K. Jolly, L. Jain, D. Bera, and T. Chakraborty, "Unsupervised anomaly detection in journal-level citation networks," in *Proceedings of the ACM/IEEE Joint Conference on Digital Libraries*, 2020, pp. 429–432.

[10] E. Mones, P. Pollner, and T. Vicsek, "Universal hierarchical behavior of citation networks," *Journal of Statistical Mechanics: Theory and Experiment*, vol. 2014, p. P05023, 2014.

[11] J. D. West, T. C. Bergstrom, and C. T. Bergstrom, "The Eigenfactor Metrics: A network approach to assessing scholarly journals," *Journal of the American Society for Information Science and Technology*, vol. 61, no. 9, pp. 1803–1812, 2010.

[12] G. Pinski and F. Narin, "Citation influence for journal aggregates of scientific publications: Theory, with application to the literature of physics," *Information Processing and Management*, vol. 12, nos. 5–6, pp. 297–312, 1976.

[13] C. T. Bergstrom, "Measuring the value and prestige of scholarly journals," *BioScience*, vol. 57, no. 10, pp. 822–823, 2007.
</paper>

<supplementary_materials>
The authors' code, data, and experimental artifacts. You may read these to verify
claims made in the paper — check if the code matches the described methodology,
if the results are reproducible, and if the data supports the conclusions.

--- Item 1 ---
id: art_Md6TNdV-FZYE
type: research
title: Hodge Decomposition & Citation Cartel Detection Specs
summary: >-
  This research artifact provides complete, verified technical specifications across five areas required to implement a Hodge-decomposition-based
  citation-cartel detector. (A) HodgeRank (Jiang et al., Math. Programming 2011): The boundary operator B₁ (m×n sparse matrix)
  encodes graph topology; the gradient least-squares system L₀s = B₁Y (where L₀ = B₁B₁ᵀ is the graph Laplacian) is solved
  via scipy.sparse.linalg.lsqr; triangle-level curl (curl X)(i,j,k) = X_ij + X_jk + X_ki is the direct mathematical signature
  of a citation ring; three orthogonal components — gradient (ranking), curl (local cycles), harmonic (global cycles) — are
  extracted with scipy; energy fractions sum to 1. Net flow input Y_ij = W_ij − W_ji. (B) CIDRE (Kojaku et al., Sci. Rep.
  2021, arXiv:2009.09097): pip install cidre; API: cidre.Cidre(group_membership).detect(A, threshold=0.15) accepting scipy
  CSR or NetworkX DiGraph; Group objects expose .donors and .recipients dicts; dcSBM null λ_ij = (s_i^out·s_j^in·Λ_{g_i,g_j})/(S_{g_i}^out·S_{g_j}^in);
  Poisson p-values with BH-FDR at α=0.01; bundled data file edge-table-2013.csv has columns [src, trg, weight] (MAG numeric
  journal IDs, ~48K journals); detects >50% of JCR-suppressed journals. (C) CDFD (Homs-Dones et al., arXiv:2506.12546, June
  2025): w = c + d decomposition (circular + acyclic), CI = Σc/Σw in [0,1]; BFF algorithm (iterative sink removal + maximal
  invariant, polynomial time, pseudocode extracted); captures ALL circular flow unlike HodgeRank curl which only captures
  triangular cycles; maximum circularity via min-cost-flow in O((m log n)(m + n log n)). Also confirmed: HHK decomposition
  (Wand et al., arXiv:2408.12839) is mathematically equivalent and validates lsqr scalability for dense graphs. (D) Clarivate
  JCR suppression lists 2018–2025: complete 2025 list (20 journals, 4 stacking: Applied Organometallic Chemistry/Wiley, Asian
  Journal of Agriculture and Biology, Chemical Methodologies, Genetic Resources and Crop Evolution/Springer; 16 self-citation);
  complete 2024 list (17 journals, stacking pairs include Climate Change Economics + Environmental Science & Pollution Research);
  complete 2023 list (4 journals: Marketing Theory [self], Genetika + Bioscience Research + Bioinspired-Biomimetic-Nanobiomaterials
  [stacking]); complete 2021 list (10 journals, 3 stacking); 2020 list (33 suppressed, all self-citation); 2018 (20, 6 stacking).
  Total ~100–120 unique suppressed journals since 2018; stacking cartels are the primary ground-truth positive class for Hodge
  validation. (E) OpenAlex API: GET /works?filter=primary_location.source.id:SA&select=id,referenced_works&per-page=200&cursor=*
  for works per journal; cursor-based pagination; free API key at openalex.org/settings/api; S3 snapshot at s3://openalex/data/jsonl/works/
  (~330 GB gzip, ~1.6 TB uncompressed, quarterly free refresh); OpenAlex CLI (pip install openalex-official) for filtered
  subsets; CIDRE's bundled 2013 CSV is the fastest prototyping path requiring no API calls.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 2 ---
id: art_IGeLtKiwHWQE
type: dataset
title: Journal Citation Network with JCR Suppression Labels
summary: |-
  Dataset: OpenAlex Journal Citation Flow Network + Clarivate JCR Suppression Labels (2015-2022).

  Source: OpenAlex API (free tier) for journal metadata and citation counts; Clarivate JCR suppressed-title lists (2018-2022) for binary manipulation labels.

  Network: 231 high-impact journals (top by cited_by_count), 15,188 directed citation pairs, 668,390 underlying work-level cross-journal citation links aggregated from ~190,000 journal articles published 2015-2022.

  Ground truth: 40 journals labeled suppressed=1 (label=1) for citation stacking or excessive self-citation, 191 journals labeled clean=0. Suppressed journals include MDPI mass-suppression (2020: IJERPH, Sustainability, Applied Sciences, Energies, Nutrients, Sensors, Water, Materials, Remote Sensing, Electronics, etc.), Frontiers citation-stacking (2021: Oncology, Neuroscience, Immunology, Psychology, Cell Dev Bio), Scientific Reports (2021), Oncotarget (2019), PLOS ONE (2019), RSC Advances (2019), and others.

  Schema: Each of the 15,188 examples in full_data_out.json represents one directed citation pair (journal i → journal j). The input field is a natural-language description of the citation relationship. The output field is the binary suppression label for journal i (string '0' or '1'). Metadata fields include: source_id_i, source_id_j, journal names, citation_count_ij, citation_count_ji, net_flow_ij, year_window, label_i, label_j, works_count_i, field_i, task_type, row_index.

  Supplementary files: adjacency_matrix.npz (231×231 scipy CSR sparse matrix, nnz=15,188), journal_metadata.json (231 journals with id/name/issn_l/field/works_count/cited_by_count), ground_truth_labels.json ({openalex_source_id: 0/1}), match_report.json (suppression ISSN resolution log).

  Scale note: The target was ≥500K pairs across ≥5,000 journals; the actual coverage is 231 journals and 15,188 pairs due to OpenAlex free-tier API rate limits (daily budget exhausted at ~3,000 API calls). The within-network density is high (28.5% fill), making this suitable for Hodge decomposition on the observed subgraph. The 231-journal network covers the most-cited journals globally and includes all major suppressed journals from the 2018-2022 JCR lists.

  Designed for: HodgeRank / Hodge decomposition citation manipulation detection; node classification on citation graphs; anomaly detection in academic publishing networks.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 3 ---
id: art_bzU_zt6gp8SL
type: experiment
title: Hodge Curl Citation Cartel Detector
summary: >-
  Implements a Hodge-Curl Cartel Detector on a journal citation network (synthetic fallback, N=784 journals, E=5682 edges,
  T=7840 triangles). The method decomposes the net-flow citation matrix into gradient (prestige/hierarchy), curl (cyclic manipulation),
  and harmonic components via combinatorial Hodge decomposition. Key results on synthetic ground truth (30 stacking positives):
  hodge_grad_residual AUC=0.958 [0.937,0.976], hodge_curl_raw AUC=0.931 [0.893,0.966], hodge_curl_norm AUC=0.886, hodge_curl_z
  AUC=0.762 — all substantially outperforming CIDRE (AUC=0.626), reciprocity (0.501), and PageRank (0.608). The gradient residual
  score (per-node average |Y_e - Y_grad| on incident edges) detects any cycle length; the triangle curl score detects 3-clique
  cartel rings. Hodge energy fractions: grad=0.117, curl=0.706, harm=0.177. A 100-sample degree-preserving row-permutation
  null model calibrates z-scores. Baselines implemented: CIDRE (approximate Poisson/Louvain), reciprocity, within-group density
  (Louvain communities), PageRank. Synthetic cartel injection tests (cyclic and reciprocal, k/w sweep, 56 conditions) confirm
  detection sensitivity. Confound test shows partial correlation of curl with suppression label after regressing out density
  and reciprocity (r=0.153). All 9 phases run end-to-end in 2.2 minutes on CPU. Network: OpenAlex API rate-limited (429),
  used Fallback A synthetic generator. Output follows exp_gen_sol_out.json schema with predict_hodge_curl_z, predict_hodge_curl_raw,
  predict_hodge_curl_norm, predict_hodge_grad_residual, predict_cidre, predict_reciprocity, predict_within_group_density,
  and predict_pagerank fields per journal.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_1/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json
</supplementary_materials>



<task>
Review this paper as you would for a top-tier venue submission.

STEP 1 — READ THE PAPER: Read it carefully. Note claims, methodology, and results.

STEP 2 — CHECK THE CODE: Read the supplementary materials to verify the paper's claims.
Do the experiments match what's described? Are there discrepancies between code and paper?

STEP 3 — SEARCH THE LITERATURE: Ground your review in evidence.
- Search for the closest existing work — is this genuinely novel or incremental?
- Check if the proposed methodology has known failure modes
- What level of contribution gets accepted at top venues in this area?

STEP 4 — WRITE YOUR REVIEW:
For each critique:
1. Categorize: methodology, evidence, novelty, clarity, scope, or rigor
2. Rate severity: major (would cause rejection) or minor (polish)
3. Describe the issue clearly
4. Suggest a concrete action to address it

Focus on the most impactful issues. Provide your review via structured output.
</task><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_io13l_LyCX8s/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "Critique": {
      "description": "A single actionable critique from the reviewer.",
      "properties": {
        "category": {
          "description": "Category: 'methodology', 'evidence', 'novelty', 'clarity', 'scope', or 'rigor'",
          "title": "Category",
          "type": "string"
        },
        "severity": {
          "description": "Severity: 'major' or 'minor'",
          "title": "Severity",
          "type": "string"
        },
        "description": {
          "description": "Clear description of the issue",
          "title": "Description",
          "type": "string"
        },
        "suggested_action": {
          "description": "Concrete suggestion for how to address this critique",
          "title": "Suggested Action",
          "type": "string"
        }
      },
      "required": [
        "category",
        "severity",
        "description",
        "suggested_action"
      ],
      "title": "Critique",
      "type": "object"
    },
    "DimensionScore": {
      "description": "Score for a single review dimension with improvement suggestions.",
      "properties": {
        "dimension": {
          "description": "Dimension name: 'soundness', 'presentation', or 'contribution'",
          "title": "Dimension",
          "type": "string"
        },
        "score": {
          "description": "Score from 1 (poor) to 4 (excellent)",
          "title": "Score",
          "type": "integer"
        },
        "justification": {
          "description": "Brief justification for this score",
          "title": "Justification",
          "type": "string"
        },
        "improvements": {
          "description": "Specific improvements to raise the score (what + how + why)",
          "items": {
            "type": "string"
          },
          "title": "Improvements",
          "type": "array"
        }
      },
      "required": [
        "dimension",
        "score",
        "justification"
      ],
      "title": "DimensionScore",
      "type": "object"
    }
  },
  "description": "Adversarial review of the paper draft.\n\nID format: review_it{iteration}__{model}",
  "properties": {
    "overall_assessment": {
      "description": "Overall assessment of the paper's quality and readiness",
      "title": "Overall Assessment",
      "type": "string"
    },
    "strengths": {
      "description": "Key strengths of the paper",
      "items": {
        "type": "string"
      },
      "title": "Strengths",
      "type": "array"
    },
    "dimension_scores": {
      "description": "Scores (1-4) for: soundness, presentation, contribution",
      "items": {
        "$ref": "#/$defs/DimensionScore"
      },
      "title": "Dimension Scores",
      "type": "array"
    },
    "critiques": {
      "description": "Actionable critiques \u2014 specific issues with concrete suggestions",
      "items": {
        "$ref": "#/$defs/Critique"
      },
      "title": "Critiques",
      "type": "array"
    },
    "score": {
      "description": "Overall quality score from 1 (very strong reject) to 10 (award quality)",
      "title": "Score",
      "type": "integer"
    },
    "confidence": {
      "default": 3,
      "description": "Confidence in assessment from 1 (educated guess) to 5 (absolutely certain)",
      "title": "Confidence",
      "type": "integer"
    }
  },
  "required": [
    "overall_assessment",
    "strengths",
    "critiques",
    "score"
  ],
  "title": "ReviewerFeedback",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-07-09 00:30:38 UTC

```
Propose a simple, novel graph-based method for detecting citation patterns in academic networks and validate it.
```

### [3] SKILL-INPUT — aii-web-tools · 2026-07-09 00:32:09 UTC

The agent loaded the **aii-web-tools** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-web-tools
description: "Web research toolkit: web search (Serper/Google), web page fetch as markdown (HTML and PDF), and regex grep over full page/PDF text. Use whenever a task needs to search the web, read a page, mine a paper/PDF, verify citations, or extract exact quotes, numbers, or methodology from a URL."
---

## Web tools

You have three web capabilities: **search**, **fetch**, and **grep** (exact
regex extraction over a full page or PDF).

**Pick where they come from, in this order:**

1. **If you have built-in `WebSearch` / `WebFetch` tools, PREFER those over the
   scripts below.** They may be **deferred tools** (listed by name but with
   schemas not yet loaded) — if so, call `ToolSearch("select:WebSearch,WebFetch")`
   ONCE to load them, then use them normally. Do not skip them just because they
   need that one extra load step; they are the preferred path. Pair them with the
   `aii_web_tools__fetch_grep` script below when you need exact text / numbers /
   methodology that a summary would miss, or when reading a PDF.
2. **Only if you have NO built-in `WebSearch` / `WebFetch`** (e.g. the OpenHands
   backend), use the scripts in this skill (below). They are our own
   implementations — Serper.dev for search, html2text + PyMuPDF for fetch, and
   regex grep over the full document text. They work without any built-in web
   tools.

Workflow either way: **search** (discover) → **fetch** (read for the gist) →
**grep** (pull exact details / read PDFs).

---

## Running the scripts

Run every script with the skill's pre-provisioned interpreter (it already has
`requests`, `html2text`, `pymupdf`, `python-dotenv`). Set `PY` once:

```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

### 1. Search the web (Serper.dev / Google)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "neuro-symbolic FOL translation LLM" --max-results 10
```

Returns ranked title / URL / snippet lines. Use it first to scan the
landscape; snippets are for discovery only — fetch a page before judging it.

### 2. Fetch a page as markdown (HTML or PDF)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://arxiv.org/abs/2303.11366" --max-chars 10000
```

`--max-chars` caps output (default 10000); `--char-offset N` pages further in.
Handles PDFs transparently via PyMuPDF.

### 3. Grep a page or PDF (exact regex extraction)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://arxiv.org/pdf/2303.11366" --pattern "verbal reinforcement" --max-matches 20 --context-chars 200
```

Returns only the matching sections with surrounding context — the right tool
for exact numbers, table values, methodology, or long PDFs where a summary
would lose the detail. `-i` for case-insensitive.

**Parallelize** independent searches/fetches in one turn; only sequence a
fetch after the search that produced its URL.

---

## Notes

- The scripts call our ability server. If a script prints
  `Ability service not available`, the server is down — say so rather than
  silently improvising a different search method.
- Do **not** hand-roll your own `requests`/scraping for search when these
  tools are available: Serper returns clean Google results and the fetch/grep
  scripts already handle HTML, PDFs, and encoding.
````

### [4] SKILL-INPUT — artifact-design · 2026-07-09 00:34:02 UTC

The agent loaded the **artifact-design** skill.

```
Tool: Skill
artifact-design
```

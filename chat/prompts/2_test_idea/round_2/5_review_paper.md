# review_paper — test_idea

> Phase: `invention_loop` · round 2 · `review_paper`
> Run: `run_io13l_LyCX8s` — Academic Citation Patterns
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `review_paper` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-07-09 01:50:01 UTC

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

The impact factor of a journal determines where researchers publish, which papers get read, and ultimately how scientists are hired and funded. This makes citation metrics a high-stakes target for gaming. Each year Clarivate removes journals from the Journal Citation Reports (JCR) for *citation stacking*-coordinated citation exchange between journals designed to artificially inflate impact factors-and for excessive self-citation. Since 2018, over 100 journals have been suppressed for such manipulation [ARTIFACT:art_Md6TNdV-FZYE], spanning every continent and scientific discipline, from Romanian materials-science rings to Brazilian agricultural clusters to 2021 Frontiers stacking cases.

The state-of-the-art detector is CIDRE [2], which fits a degree-corrected stochastic block model (dcSBM) to the journal citation graph and flags groups that exchange citations at rates anomalous relative to the community null. CIDRE detects 12 of 22 known stacking groups in its 2013 MAG evaluation and represents a landmark advance. However, density-based methods share a structural weakness: they measure *how many* citations flow between a group of journals, not *how consistently* those citations follow a prestige hierarchy. This conflation generates two systematic errors: densely-cross-cited legitimate communities appear anomalous, and cartels that limit citation volumes to stay below density thresholds may avoid detection entirely.

We import the Helmholtz-Hodge decomposition from mathematical physics to supply a density-independent structural definition of manipulation. The Hodge decomposition of any flow on a graph yields three orthogonal components: a *gradient* flow consistent with a global prestige potential (the HodgeRank score [1]); a *curl* flow of local cyclic loops that no global ranking can explain; and a *harmonic* flow of large-scale cycles. Legitimate scholarly influence flows 'downhill' along the prestige gradient; citation cartels inject flow that *circulates*, producing local curl. This gives an operational, density-independent definition: **manipulation is curl**.

We evaluate this framework on a real 231-journal OpenAlex citation network annotated with JCR suppression labels [ARTIFACT:art_IGeLtKiwHWQE], restricting the primary positive class to the 7 confirmed stacking journals (excluding 33 suppressed for excessive self-citation, which the curl detector cannot address by design). A critical empirical finding challenges the method's founding assumption: the real network carries 77.0% of net-flow energy in the curl component-not in the gradient as legitimate scholarly flow predicts. This reveals substantial natural circularity in journal-level citation exchange, making raw curl magnitude non-discriminative. Instead, a *field-aware* z-score that calibrates each journal's curl against its research community's expectations achieves AUC = 0.718 (95% CI [0.459, 0.922])-the strongest result across all methods evaluated [ARTIFACT:art_XbmaHSRFGigA].

[FIGURE:fig1]

**Summary of Contributions:**
- *Method* (Section 3): A Hodge flow decomposition framework for citation manipulation detection, with gradient residual, triangle curl, and field-aware z-score as the primary detection scores.
- *Dataset* (Section 4): The first openly annotated journal citation network with JCR stacking/self-citation labels, covering 231 journals, 9,146 edges, 230,336 triangles, and 7 confirmed stacking-only positives.
- *Experiments* (Section 5): Real-data evaluation showing that field-aware calibration achieves AUC = 0.718; a clean-base injection study spanning cyclic and reciprocal cartels across k in {3, 4, 5, 10}; and energy decomposition revealing that real citation networks are curl-dominant.
- *Analysis* (Section 6): Explanation of why raw curl fails (isolated-node structure of stacking journals), why the gradient residual outperforms triangle curl even on triangular cartels, and honest limits of the method.

# Background and Related Work

## Citation Ranking Methods

Pinski and Narin [12] pioneered recursive prestige-weighted citation scores. The Eigenfactor project [11, 13] implemented this at scale using PageRank-style random walks, producing widely-used Article Influence scores. These methods rank journals but do not decompose the underlying flow into consistent and inconsistent components; a manipulated ranking gives no structural warning.

## Citation Cartel Detection

CIDRE [2] fits a degree-corrected stochastic block model as a null and identifies groups of journals whose citation exchange rates exceed the dcSBM prediction, accounting for community structure and degree. It detects 12 of 22 known stacking groups. Our method differs fundamentally: we define manipulation structurally as ranking-inconsistent circulation (curl) rather than citation-rate anomaly, yielding a signal orthogonal to density by mathematical construction.

Jolly et al. [9] applied unsupervised anomaly detection to journal citation networks. Liu et al. [6] introduced GLAD, a deep graph learning method for anomalous citations at the paper level. Both methods are opaque (learned representations) and provide no interpretable structural definition of manipulation.

## Hodge Decomposition on Graphs

Jiang, Lim, Yao, and Ye [1] introduced HodgeRank, applying combinatorial Hodge theory to pairwise-comparison graphs: the gradient component yields a global ranking, and the curl and harmonic components quantify ranking inconsistency. HodgeRank has been applied to crowdsourced rankings (e-commerce, sports) but never to citation networks or cartel detection.

Homs-Dones et al. [3] introduce the Circular Directional Flow Decomposition (CDFD), which decomposes directed flow as $w = c + d$ (circular + acyclic), defining a circularity index CI = $\Sigma c / \Sigma w \in [0,1]$ that captures *all* cyclic flow rather than only triangular curl. CDFD is directly relevant to cartels with rings larger than 3 journals. Wand et al. [4] apply the Helmholtz-Hodge-Kodaira decomposition to financial market networks to reveal causal hierarchy. Neither work addresses citation integrity or validates against manipulation ground truth.

## Temporal Hodge Anomaly Detection

HLSAD (Frantzen and Schaub, KDD 2025 [14]) applies Hodge Laplacians of multiple orders to detect structural change-points in time-evolving simplicial complexes. For each temporal snapshot, HLSAD extracts principal singular values from both up-Laplacian and down-Laplacian at each order, concatenates them into a feature vector, and flags anomalies when the angular deviation from a sliding-window SVD baseline exceeds a threshold (validated on UCI Online Message and US Senate co-sponsorship networks). The present work differs in three respects: we apply a single-pass *static* decomposition of a cumulative net-flow matrix rather than tracking temporal structural change; we use flow magnitude (curl energy relative to a community null) rather than spectral deviation; and we validate against labeled ground truth (JCR stacking suppression lists) rather than unlabeled event detection.

## Network Hierarchy

Trophic coherence [7] and the directionality index of MacKay et al. [8] quantify how consistently a directed network follows a global hierarchy. Mones et al. [10] demonstrate near-universal hierarchy in paper-level citation networks, where the arrow of time enforces near-acyclicity. At the journal level-aggregating across years and disciplines-genuine cycles accumulate. Our work confirms empirically that journal-level citation networks naturally carry substantial curl (77% of net-flow energy), an observation that motivates field-relative rather than absolute calibration.

# Method

## Citation Flow Graphs

Let $\mathcal{G} = (V, E, W)$ be a directed weighted graph where $V$ is the set of journals, $E$ is the set of ordered pairs $(i, j)$ with at least $\tau$ total citations ($W_{ij} + W_{ji} \geq \tau$), and $W_{ij}$ is the total number of citations from journal $i$ to journal $j$ over a multi-year window. We form the *net-flow matrix* $Y_{ij} = W_{ij} - W_{ji}$ (antisymmetric by construction). The net-flow captures citation *imbalance*: $Y_{ij} > 0$ means journal $i$ cites $j$ more than the reverse, consistent with $j$ having higher prestige. We represent the graph in canonical edge orientation (edge $(i,j)$ with $i < j$), yielding a flow vector $Y_e \in \mathbb{R}^{|E|}$. [ARTIFACT:art_bzU_zt6gp8SL]

## Combinatorial Hodge Decomposition

Combinatorial Hodge theory [1] decomposes any edge-flow $Y_e$ into three orthogonal components:
$$Y_e = Y_{\text{grad}} + Y_{\text{curl}} + Y_{\text{harm}}$$
where orthogonality holds in the $\ell^2$ sense (disjoint energy). The three components are:

**Gradient component.** The $n \times m$ boundary operator $B_1$ encodes graph topology: $B_1[i,e] = -1$ and $B_1[j,e] = +1$ for edge $e = (i,j)$. The gradient component satisfies $Y_{\text{grad}} = B_1^\top s^\star$, where $s^\star$ solves
$$\min_{s \in \mathbb{R}^n} \|B_1^\top s - Y_e\|^2$$
This is the HodgeRank problem [1], solved via a single sparse least-squares solve (`scipy.sparse.linalg.lsqr`). The potential $s^\star_i$ is journal $i$'s prestige score: high-prestige journals receive more citations than they give, pulling the gradient toward them.

**Curl component.** For a triangle $(i,j,k)$, the triangle curl is $(\operatorname{curl} Y)_{ijk} = Y_{ij} + Y_{jk} + Y_{ki}$. The $m \times T$ boundary operator $B_2$ encodes triangle membership; the curl component satisfies $Y_{\text{curl}} = B_2 h^\star$ where $h^\star$ minimizes the residual after removing the gradient. The Hodge identity $B_1 B_2 = 0$ guarantees exact orthogonality. The $B_2$ operator captures only 3-cycle (triangular) circulation; longer-ring cartels contribute to the harmonic component and would require the CDFD all-cycle framework [3] for full coverage.

**Harmonic component.** The remainder $Y_{\text{harm}} = Y_e - Y_{\text{grad}} - Y_{\text{curl}}$ consists of global cycles that are locally curl-free but do not close within any single triangle.

## Node-Level Scores

**Gradient residual** $\rho_i$: the per-journal average absolute departure of observed flow from the gradient prediction, over all incident edges: $\rho_i = \frac{1}{|\mathcal{N}_i|} \sum_{e \ni i} |Y_e - Y_{\text{grad},e}|$. This score accumulates evidence from every incident edge-both incoming and outgoing-detecting any ranking-inconsistent flow of any cycle length. Cartel membership distorts a journal's prestige potential $s^\star$ on all incident edges simultaneously, providing more observations per journal than the triangle-restricted curl.

**Triangle curl** $\kappa_i$: the per-journal average absolute triangle curl: $\kappa_i = \frac{1}{T_i} \sum_{\text{triangles} \ni i} |(\operatorname{curl} Y)_{ijk}|$. It provides geometric interpretability (each flagged triangle is an auditable 3-ring) but is restricted to journals with triangular connectivity.

**HodgeRank prestige** $s^\star_i$: the prestige potential from the gradient solve. High-prestige journals receive more net citations; anomalously high prestige relative to journal quality may indicate manipulation.

## Field-Aware Null Model Calibration

Raw curl scores conflate natural field-level circularity with anomalous manipulation: a journal in a dense, heavily cross-cited field will have high curl even under legitimate citation patterns. We address this with a field-aware null model. Using Louvain-detected community structure (44 communities in the real network), we generate 100 null-model samples by permuting citation edges *within* each field-pair (preserving both degree sequences and field-level citation rates). The field-aware z-score
$$z_i^{\text{field}} = \frac{\kappa_i - \mu_i^{\text{null}}}{\sigma_i^{\text{null}}}$$
measures how anomalous journal $i$'s curl is relative to its research community's expectations. A simpler degree-preserving null (row-permutation of $W$, preserving out-degree sequences but not field structure) is also computed for comparison. The Spearman correlation between the two null model z-scores on the real data is $\rho = 0.584$ ($p < 10^{-21}$), indicating substantial overlap; the field-aware variant provides incremental lift by conditioning on community citation rates.

# Data

## Real Journal Citation Network with JCR Suppression Labels

[ARTIFACT:art_IGeLtKiwHWQE] We constructed a journal citation network from the OpenAlex API [5], aggregating citation links across 2015-2022. The network covers 231 high-impact journals (top by cited-by count), 9,146 directed citation pairs, and 230,336 triangles derived from 668,390 underlying work-level citation links.

**Suppression type distinction.** Each journal is annotated with a Clarivate JCR suppression label (2018-2022) [ARTIFACT:art_Md6TNdV-FZYE]. We critically distinguish two suppression types:

- *Citation stacking* (7 journals in our network): coordinated inter-journal citation exchange-organized rings, systematic mutual citation between two or more outlets. Confirmed cases include journals from the 2021 JCR list (Archivos Latinoamericanos de Nutrition, Journal of Intelligent and Fuzzy Systems, Materials Express, Hellenic Journal of Cardiology) and the 2018 list (Liver Cancer/Digestive Diseases/Oncology stacking ring, History of Economic Thought mutual pair) [ARTIFACT:art_gkqGp1-55dg1].
- *Excessive self-citation* (33 journals): inflating impact factors by citing the journal's own back-catalog. The Hodge curl detector measures *inter-journal* cyclic exchange and cannot in principle detect self-citation.

This distinction is essential. The 2020 JCR suppression event (33 journals including Sustainability, Sensors, IJERPH, and other MDPI titles) is entirely self-citation; including it in the positive class would introduce 33 journals the curl detector was never designed to find. All primary evaluations use the 7 stacking-only positives. We also report results for all 40 suppressed journals as a secondary evaluation.

## Synthetic Citation Network

For controlled validation, we use an 800-journal synthetic network with 12 scientific fields, exponential prestige scores, and citation weights proportional to prestige. After thresholding ($\tau = 3$), the network has $E = 15,639$ edges, $T = 75,227$ triangles, and mean edge weight $\bar{w} = 3.23$. Cartel injection (Section 5.3) operates on a clean base ($n_c = 0$) to test detection in isolation. A pre-loaded variant with $n_c = 10$ injected 3-node cyclic rings (30 cartel positives) serves as the controlled synthetic validation (Section 5.2) [ARTIFACT:art_bzU_zt6gp8SL].

# Experiments

## Setup

All primary experiments use the real 231-journal network with stacking-only labels (7 positives). Methods compared: (1) Hodge gradient residual $\rho$, (2) Hodge curl raw $\kappa$, (3) HodgeRank prestige $s^\star$, (4) CIDRE-fallback (spectral clustering + Poisson null; the published `cidre` package requires matplotlib 3.1.3 and is incompatible with Python 3.12, necessitating the fallback), (5) degree-preserving null z-score, (6) field-aware null z-score. We measure AUC-ROC with 2,000-sample bootstrap 95% confidence intervals. All computation runs on CPU in under 5 minutes.

## Real-Data Hodge Evaluation

[FIGURE:fig2]

Table 1 shows AUC results on the real 231-journal network with stacking-only labels (7 positives).

| Method | AUC | 95% CI |
|---|---|---|
| Field-aware null z-score | **0.718** | [0.459, 0.922] |
| Degree-preserving null z-score | 0.618 | [0.352, 0.876] |
| HodgeRank prestige | 0.551 | [0.263, 0.813] |
| Hodge gradient residual | 0.454 | [0.152, 0.752] |
| Hodge curl raw | 0.430 | [0.144, 0.726] |
| CIDRE-fallback | 0.343 | [0.115, 0.590] |

Raw Hodge scores-gradient residual (AUC = 0.454) and curl raw (AUC = 0.430)-fall below chance. This is not a failure of the theory but of the network structure: 3 of the 7 confirmed stacking journals are essentially isolated nodes in the 231-journal sample, participating in zero triangles. The curl operator requires triangular connectivity to produce nonzero scores; journals lacking it receive scores of exactly zero, ranking them at chance level regardless of their true manipulation status. The CIDRE-fallback (AUC = 0.343) also underperforms, confirming that this is a structural challenge shared across methods when stacking journals lack network connectivity in the observed sample.

The field-aware null z-score (AUC = 0.718, CI [0.459, 0.922]) is the strongest result. It succeeds precisely because it conditions on field-community curl distributions: a stacking journal with moderate raw curl but anomalous curl relative to its field peers is flagged, even when its absolute scores are unremarkable. The degree-preserving null z-score (AUC = 0.618) provides a weaker version of the same signal, not conditioning on field-level citation rates.

For the combined 40-journal evaluation (stacking + self-citation): raw Hodge scores fall to AUC = 0.113 for both gradient residual and curl, and CIDRE-fallback achieves 0.112-all well below chance-confirming that the curl detector has no signal for self-citation manipulation. The field-aware null achieves AUC = 0.759 on all 40 suppressed journals, suggesting some partial sensitivity to self-citation-suppressed journals even without direct design for this target.

## Synthetic Validation

On the controlled synthetic network ($n_c = 10$, 30 cartel-member positives), [ARTIFACT:art_XbmaHSRFGigA] the Hodge gradient residual achieves AUC = 0.737 (CI [0.686, 0.785]) and the CIDRE-fallback achieves AUC = 0.845 (CI [0.766, 0.912]). The triangle curl achieves AUC = 0.558 (CI [0.457, 0.656]). The higher CIDRE-fallback performance reflects that the spectral clustering null accurately recovers the planted field structure in this synthetic network.

These results confirm that the Hodge approach operates correctly under controlled cartel conditions and that gradient residual outperforms triangle curl even when cartels are exactly 3-node rings (AUC 0.737 vs. 0.558). This counterintuitive finding-that the gradient residual beats the triangle-specific curl on triangular cartels-is explained in Section 6.1.

## Clean-Base Injection Study

[FIGURE:fig3]

To assess detection sensitivity in isolation, we inject cartels into the clean base network ($n_c = 0$) and sweep cartel type $\in$ \{cyclic, reciprocal\}, size $k \in \{3, 4, 5, 10\}$, and weight factor $w_f \in \{0.1, 0.3, 0.5, 1.0, 2.0\} \times \bar{w}$ (20 repetitions per condition, 40 conditions total). This directly addresses the critique that prior injection experiments were confounded by pre-existing background manipulation [ARTIFACT:art_XbmaHSRFGigA].

The results are uniformly limited. No condition achieves AUC $> 0.7$. The best individual condition is cyclic $k = 3$, $w_f = 2.0\bar{w}$: gradient residual AUC = 0.617 (SD = 0.132), curl AUC = 0.578 (SD = 0.139). Detection decreases as ring size grows: at $k = 10$, the best gradient residual AUC is 0.557 ($w_f = 2.0\bar{w}$), consistent with the $B_2$ operator's restriction to triangular cycles-larger rings produce harmonic signal that curl scores cannot capture.

Reciprocal cliques (symmetric exchange: $W_{ij} = W_{ji}$ for all $k$ journal pairs) are theoretically invisible to the net-flow decomposition. Perfectly balanced reciprocal exchange produces $Y_{ij} = 0$, yielding zero gradient residual and zero curl. In practice, the injected reciprocal cliques have symmetric *added weight* on top of an existing asymmetric background, so the net-flow is not exactly zero; nevertheless, detection remains near chance for all reciprocal conditions (best: reciprocal $k = 3$, $w_f = 2.0\bar{w}$, gradient AUC = 0.546, curl AUC = 0.562).

The injection study defines a practical limitation: individual small cartels in a realistic dense citation background are not detectable by raw Hodge scores at any of the tested injection weights. Detection at AUC > 0.6 requires the strongest injection ($w_f = 2.0\bar{w}$, approximately 6.5× the mean edge weight) for the most favorable structure (cyclic $k = 3$). Field-aware calibration (Section 5.2) is required to achieve AUC = 0.718 on real data, suggesting that relative-to-field anomaly is more informative than absolute signal strength.

## Hodge Energy Decomposition

[FIGURE:fig4]

Table 2 shows the Hodge energy fractions (fraction of $\|Y_e\|^2$) for both networks.

| Component | Real (231 journals) | Synthetic ($n_c=10$) |
|---|---|---|
| Gradient | 23.0% | 4.3% |
| Curl | 77.0% | 78.0% |
| Harmonic | $<$0.001% | 17.8% |

The most consequential finding is that the *real* citation network is 77% curl-dominant-nearly as curl-heavy as the synthetic network with 30 injected cartel members (78.0%). This challenges the founding assumption that legitimate scholarly networks are gradient-dominated. The real network has a somewhat higher gradient fraction (23.0% vs. 4.3% synthetic), reflecting genuine hierarchy in scholarly influence, but this gradient is swamped by natural cyclic citation exchange accumulated over eight years across disciplines.

The near-zero harmonic fraction in the real network (vs. 17.8% in the synthetic) is a structural signature: the 231-journal graph is dense enough ($T = 230,336$ triangles) that the curl operator absorbs almost all cyclic energy, leaving little for global loops. The synthetic network has many fewer triangles per journal and thus a larger harmonic residual.

These energy fractions explain why raw Hodge scores fail on real data and why field-aware calibration is necessary: with 77% of all citation flow already carrying curl structure, the manipulated journals' curl values are not outliers in absolute terms.

# Discussion

## Why Gradient Residual Outperforms Triangle Curl

A non-obvious finding across both the real-data and synthetic experiments is that the gradient residual consistently outperforms the triangle curl, even when cartels are exactly 3-node rings (the structure the curl is designed to detect). The explanation is statistical power. A cartel member's gradient residual receives a contribution from every incident edge where observed flow departs from the prestige prediction: a journal with $d$ incident edges accumulates $d$ independent pieces of evidence. The triangle curl, by contrast, averages only over triangles in which the journal participates-a subset proportional to the journal's triangle count, which is often smaller than its edge count and zero for isolated journals. Even on purely triangular cartels, the gradient residual accumulates more observations per journal, yielding higher AUC. This implies the gradient residual is the recommended primary score for general use, with triangle curl providing auditable, edge-level evidence for confirmed 3-ring patterns.

## Why Field-Aware Calibration Is Necessary

The 77% curl fraction in the real citation network means that curl is the normal state of journal-level citation exchange, not an anomaly. Journals in dense, heavily cross-cited fields (physics, chemistry) naturally accumulate high curl from legitimate multi-year, multi-author citation cycles. A stacking journal in such a field would have high curl purely from field membership. The field-aware null model conditions on this: by comparing each journal's curl to the distribution expected within its 44-community Louvain partition, the z-score isolates the *excess* curl that is anomalous relative to peers. This is structurally analogous to what the dcSBM null does for CIDRE-it removes community-level confounds-but applied to the curl dimension rather than the citation-rate dimension.

## Relationship to Prior Work

The CIDRE-fallback baseline (AUC = 0.343 on real stacking-only labels) underperforms the field-aware Hodge null (AUC = 0.718), but this comparison is imperfect: the `cidre` Python package requires matplotlib 3.1.3 and is incompatible with Python 3.12, forcing a spectral-clustering + Poisson null approximation. The full dcSBM CIDRE may perform differently on the same dataset. A proper comparison awaits a compatible execution environment or a Python 3.12-compatible port of CIDRE.

The CDFD framework [3] captures all circular flow including longer cycles and would directly address the limitation of the triangular $B_2$ curl operator for $k \geq 4$ cartels. The present work and CDFD are complementary: Hodge provides gradient residual and a prestige ranking certifiable against its own curl; CDFD provides a more complete circularity index for all-cycle manipulation.

HLSAD [14] targets a different problem (temporal change-point detection) and a different signal (spectral deviation in Hodge Laplacians) with no labeled ground truth from manipulation databases. The two works are complementary in scope.

## Limitations

1. **Small positive class.** Only 7 confirmed stacking journals in the 231-journal network yield wide confidence intervals (e.g., field-aware null CI [0.459, 0.922]). Expansion to the full MAG dataset (48,821 journals in CIDRE) is necessary for statistical conclusiveness.

2. **Triangle-only curl.** The Hodge $B_2$ operator captures only 3-clique rings; rings of size $k \geq 4$ contribute to the harmonic component and are missed. The CDFD all-cycle framework [3] would address this gap.

3. **Net-flow invisibility to balanced exchange.** Perfectly symmetric reciprocal cartels ($W_{ij} = W_{ji}$) produce zero net-flow and are invisible to the Hodge decomposition. Directed citation matrices (not net-flows) would be required for such cases.

4. **CIDRE approximation.** The published CIDRE package is incompatible with Python 3.12; the spectral-clustering + Poisson null fallback is not the published method. The real-data CIDRE comparison must be treated as indicative rather than definitive.

5. **Connectivity requirement.** The curl operator produces zero scores for isolated nodes. Stacking journals that are peripheral in the citation graph-common for niche or newly suppressed outlets-will not be flagged by curl regardless of their manipulation.

# Conclusion

We proposed applying the Helmholtz-Hodge decomposition to citation cartel detection, defining manipulation structurally as cyclic flow inconsistent with any prestige ordering. Evaluating on a real 231-journal OpenAlex network annotated with JCR stacking labels (7 stacking-only positives), we found that raw Hodge scores fall below chance (AUC = 0.430-0.454) due to the isolated-node structure of stacking journals in a top-cited-journal sample. A field-aware null model calibrating curl against research-community expectations rescues the signal, achieving AUC = 0.718-the strongest result across all methods evaluated, substantially above the CIDRE-fallback baseline (AUC = 0.343).

A key empirical finding revises the method's founding assumption: the real citation network carries 77% of net-flow energy in the curl component, not the gradient. Journal-level citation exchange accumulated over multi-year windows naturally produces substantial cyclic flow, making raw curl magnitude non-discriminative without field-relative normalization.

A clean-base injection study across cyclic and reciprocal cartel types ($k \in \{3,4,5,10\}$) confirms that individual small-cartel detection is fundamentally limited under realistic conditions (best AUC = 0.617 at $2\times$ mean edge weight for $k = 3$ cyclic rings; no condition exceeds AUC = 0.7). The method's practical utility lies in detecting systematic field-relative anomalies across the full citation graph, not in identifying individual isolated cartel rings.

We release the first openly annotated journal citation network with JCR stacking/self-citation labels to support future detection research.

**Future work:**
- Expansion to the full MAG-derived dataset (48,821 journals) to address the positive-class size limitation and enable proper CIDRE comparison.
- Integration with the CDFD all-cycle circularity index [3] to detect longer-ring cartels beyond 3-cycles.
- Temporal curl tracking before and after JCR suppressions for early-warning signal analysis.
- Extension to the full directed citation matrix (not net-flows) to detect balanced reciprocal exchange invisible to the current framework.

# Bibliography

[1] X. Jiang, L.-H. Lim, Y. Yao, and Y. Ye, "Statistical ranking and combinatorial Hodge theory," *Mathematical Programming*, vol. 127, pp. 203-244, 2011. doi:10.1007/s10107-010-0419-x

[2] S. Kojaku, G. Livan, and N. Masuda, "Detecting anomalous citation groups in journal networks," *Scientific Reports*, vol. 11, p. 14524, 2021. doi:10.1038/s41598-021-93025-5 (arXiv:2009.09097)

[3] M. Homs-Dones, R. S. MacKay, B. Sansom, and Y. Zhou, "Circular directional flow decomposition of networks," arXiv:2506.12546, 2025.

[4] T. Wand, O. Kamps, and H. Iyetomi, "Causal hierarchy in the financial market network-uncovered by the Helmholtz-Hodge-Kodaira decomposition," *Entropy*, vol. 26, no. 10, p. 858, 2024. doi:10.3390/e26100858

[5] J. Priem, H. Piwowar, and R. Orr, "OpenAlex: A fully-open index of scholarly works, authors, venues, institutions, and concepts," arXiv:2205.01833, 2022.

[6] J. Liu, F. Xia, X. Feng, J. Ren, and H. Liu, "Deep graph learning for anomalous citation detection," *IEEE Transactions on Neural Networks and Learning Systems*, vol. 33, no. 5, pp. 2543-2557, 2022. doi:10.1109/TNNLS.2022.3145092

[7] S. Johnson, V. Dominguez-Garcia, L. Donetti, and M. A. Munoz, "Trophic coherence determines food-web stability," *Proceedings of the National Academy of Sciences*, vol. 111, no. 50, pp. 17923-17928, 2014. doi:10.1073/pnas.1409077111

[8] R. S. MacKay, S. Johnson, and B. Sansom, "How directed is a directed network?," *Royal Society Open Science*, vol. 7, no. 9, p. 201138, 2020. doi:10.1098/rsos.201138

[9] B. L. K. Jolly, L. Jain, D. Bera, and T. Chakraborty, "Unsupervised anomaly detection in journal-level citation networks," in *Proceedings of the ACM/IEEE Joint Conference on Digital Libraries*, 2020. doi:10.1145/3383583.3398531

[10] E. Mones, P. Pollner, and T. Vicsek, "Universal hierarchical behavior of citation networks," *Journal of Statistical Mechanics: Theory and Experiment*, p. P05023, 2014.

[11] J. D. West, T. C. Bergstrom, and C. T. Bergstrom, "The Eigenfactor metrics: A network approach to assessing scholarly journals," *Journal of the American Society for Information Science and Technology*, vol. 61, no. 9, pp. 1803-1812, 2010.

[12] G. Pinski and F. Narin, "Citation influence for journal aggregates of scientific publications: Theory, with application to the literature of physics," *Information Processing and Management*, vol. 12, nos. 5-6, pp. 297-312, 1976.

[13] C. T. Bergstrom, "Measuring the value and prestige of scholarly journals," *BioScience*, vol. 57, no. 10, pp. 822-823, 2007.

[14] F. Frantzen and M. T. Schaub, "HLSAD: Hodge Laplacian-based simplicial anomaly detection," in *Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining*, 2025. doi:10.1145/3711896.3736998
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

--- Item 4 ---
id: art_gkqGp1-55dg1
type: research
title: HLSAD Positioning & JCR Suppression Annotations
summary: |-
  This artifact delivers two critical inputs for the Hodge-decomposition citation cartel detector paper.

  **HLSAD (arXiv:2505.24534, KDD 2025)** is authored by Frantzen & Schaub (RWTH Aachen). It applies Hodge Laplacians of multiple orders (up to user-specified K) to time-evolving simplicial complexes. For each temporal snapshot, singular values of both up- and down-Laplacians are extracted and concatenated into a feature vector; anomalies are flagged when the angular deviation from an SVD-based sliding-window baseline exceeds a threshold. Real-world datasets: UCI Online Message Dataset (Hits@10=1.0) and US Senate co-sponsorship network (Hits@2=1.0). KEY CONTRAST: HLSAD asks 'when did the graph structure change?' (temporal change-point detection) and does not target citation networks or citation integrity. This paper asks 'is the static cumulative flow currently manipulated?' using orthogonal gradient+curl+harmonic decomposition of a fixed net-flow matrix, where curl magnitude is the direct algebraic signature of citation rings validated against JCR suppression labels.

  READY-TO-USE RELATED WORK PARAGRAPH: 'HLSAD (Frantzen & Schaub, KDD 2025) applies the spectral properties of Hodge Laplacians of multiple orders to detect structural change-points and events in time-evolving simplicial complexes. For each temporal snapshot, HLSAD extracts principal singular values from both up and down Hodge Laplacians, concatenates them into a feature vector, and flags anomalies when the angular deviation from a sliding-window SVD baseline exceeds a threshold. Our work, by contrast, applies a single-pass static Hodge–Helmholtz decomposition of a cumulative net-flow matrix on the journal citation graph, decomposing flow into orthogonal gradient (global ranking), curl (local triangular circular exchange), and harmonic (global cycle) components. The curl magnitude directly quantifies citation-ring activity against a labeled ground truth from JCR suppression lists, targeting citation integrity on static cumulative data rather than general temporal change-point detection in evolving higher-order networks.'

  **SUPPRESSION ANNOTATION:** 32 stacking journals confirmed by name across 2018-2025 (5 from 2018, 4 from 2021—CORRECTING the prior artifact which said 3—, 3 from 2023, 11 from 2024, 4 from 2025). CRITICAL CORRECTIONS: (1) 2020 had ZERO stacking journals—all 33 suppressions were self-citation; (2) Hellenic Journal of Cardiology (2021) is STACKING, not self-citation as previously documented; (3) 2019 stacking journal names are unknown and those 17 journals must be excluded from the validated positive class. CONCURRENT WORK: CDFD (arXiv:2506.12546, June 2025) is a close concurrent paper decomposing directed flow as w=c+d with circularity index CI=Σc/Σw—captures ALL circular flow unlike Hodge curl which only catches triangular cycles. Full annotated JSON list and research report are in research_out.json and research_report.md.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 5 ---
id: art_XbmaHSRFGigA
type: experiment
title: Hodge & CIDRE Citation Cartel Detection
summary: >-
  6-phase evaluation of Hodge-decomposition-based citation cartel detection on a real 231-journal network. Phase 1: Real-data
  Hodge evaluation using stacking-only labels (7 journals confirmed suppressed for citation stacking); real network shows
  77% curl energy (not gradient-dominant as expected). Raw Hodge scores give AUC=0.454 (grad) and 0.430 (curl) on stacking
  labels — below 0.5, explained by 3/7 stacking journals being isolated nodes. HodgeRank prestige AUC=0.551. Phase 2: CIDRE
  fallback (cidre package incompatible with Python 3.12 due to matplotlib 3.1.3 dependency); used spectral clustering + Poisson
  null; stacking AUC=0.343. Phase 3: Synthetic n_c=10 network validates methodology — Hodge grad AUC=0.737 CI[0.686,0.785],
  CIDRE fallback AUC=0.845. Phase 4: Clean-base injection study (800-node, n_c=0 base) across cyclic and reciprocal cartel
  types, k in {3,4,5,10}, w_factor in {0.1,0.3,0.5,1.0,2.0}, 20 reps each (40 conditions); best condition: cyclic k=3 w=2.0x
  mean edge weight, grad AUC=0.617; no condition exceeded 0.7. Phase 5: Field-aware null model (44 Louvain communities) stacking
  AUC=0.718 — best signal overall; degree-preserving null AUC=0.618; Spearman rho=0.584 between null models. Phase 6: Energy
  fractions — real: grad=0.230, curl=0.770, harmonic~0; synthetic: grad=0.043, curl=0.780, harmonic=0.178. Delta curl = 0.010
  (small, real network already curl-dominant). All 231 journals scored on 6 prediction fields. Output validated against exp_gen_sol_out
  schema.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json
</supplementary_materials>

<previous_review>
Your review from the previous iteration. Check which critiques have been addressed
in the revised paper. Do NOT re-raise critiques that have been adequately fixed.
Only re-raise if the fix is insufficient.

- [MAJOR] (methodology) Circular synthetic evaluation: the injected cartel structure is exactly 3-node directed rings at 60% of max edge weight—precisely the signal the Hodge triangle curl score (B_2 h*) is designed to detect. CIDRE, by contrast, is a community-level density detector not designed for 3-cycle detection. Showing that a 3-cycle detector outperforms a density detector on a network of 3-cycle cartels is tautological, not informative. The AUC of 0.958 / 0.931 tells us the method is correctly implemented, not that it generalizes to real cartel structures (which are larger, diffuse, and carefully calibrated to avoid detection).
  Action: Introduce at least two additional synthetic cartel types: (a) k-node directed rings for k in {4, 5, 10} to test whether the method—which captures only triangle curl—degrades as ring size grows, and (b) reciprocal cliques (every pair cites every other pair equally) to test whether the method distinguishes high-reciprocity clusters from directional cycles. Report AUC separately for each cartel type and contrast with CIDRE. This would replace the current monolithic 'synthetic validation' with a genuine sensitivity analysis.
- [MAJOR] (evidence) The real 231-journal OpenAlex+JCR dataset is constructed and released but never used to evaluate the Hodge detector. The paper's primary quantitative claims—AUC 0.958 / 0.931, CIDRE 0.626, partial correlation r = 0.153—are all on synthetic data. Without real-world validation, the paper cannot support the claim that Hodge decomposition detects real citation cartels better than CIDRE. The API rate-limiting explanation is understandable, but the dataset WAS subsequently collected and is being released; the Hodge experiment should have been run on it.
  Action: Apply the Hodge pipeline (method.py) to the adjacency_matrix.npz in art_IGeLtKiwHWQE. Acknowledge that 40/231 suppressed journals include both stacking (approximately 15-20 journals) and excessive self-citation (the remainder), and restrict the 'positive' class to stacking-only for the primary AUC evaluation. If AUC is lower on real data than synthetic (expected), report this honestly as showing that real cartels are more subtle than the synthetic design, and use it to motivate the limitations discussion. Even a null result on real data is more informative than synthetic-only evidence.
- [MAJOR] (evidence) The injection study—intended as a direct sensitivity test—uniformly fails: across all 56 conditions (k in {3,5,10,20}, w_f in {0.01,...,2.0}), all methods achieve AUC near 0.5. The paper's explanation—that the newly injected cartel nodes cannot be separated from the existing manipulation background—is essentially a concession that the method cannot detect additional manipulation once some manipulation already exists. This substantially undermines the practical utility claim. Furthermore, the experimental design conflates the original 30 cartel positives with new injected nodes in an unclear way.
  Action: Re-run the injection study on a CLEAN base network (no pre-injected cartels: set n_c=0 in the synthetic generator). Sweep k and w_f as before. This tests the method's sensitivity in isolation. If AUC is high at moderate injection weights and degrades at low weights, that defines a practical detectability threshold (minimum ring size and weight) which is a concrete and useful finding. Report this threshold explicitly.
- [MAJOR] (methodology) The CIDRE baseline is an approximation (Louvain communities + Poisson null) rather than the published cidre package (pip install cidre), which fits a full degree-corrected stochastic block model. The paper acknowledges this but still uses the CIDRE AUC of 0.626 (with CI extending to 0.499, below chance) as the primary performance comparison. An approximation that performs at chance level is not a valid proxy for the actual method. If the published CIDRE package had been used, the comparison might look materially different.
  Action: Install the cidre package and run CIDRE.detect() on the synthetic network as well as the real-data network. If the full CIDRE achieves substantially higher AUC, report both the approximate and exact CIDRE numbers and discuss what the gap reveals about the importance of the dcSBM vs. Poisson null—this would itself be an informative finding. Do not make primary comparisons against an approximate implementation.
- [MAJOR] (novelty) HLSAD (Frantzen and Schaub, 'Hodge Laplacian-based Simplicial Anomaly Detection,' KDD 2025, arXiv:2505.24534) uses the spectral properties of Hodge Laplacians of simplicial complexes for anomaly detection in time-evolving networks, and was accepted at a top venue. This is the most directly related concurrent work and is not cited. The two approaches differ (spectral vs. flow decomposition; temporal change-point vs. static manipulation scoring), but the omission of this KDD 2025 paper from the related work section is a significant gap that will be flagged by reviewers familiar with the field.
  Action: Add a paragraph in Section 2 discussing HLSAD. Contrast: HLSAD detects structural changes over time via Hodge Laplacian eigenvalues on simplicial complexes, while this work decomposes static cumulative net-flows into curl components and uses them as a manipulation score. Note that HLSAD targets general graph events while this work targets citation integrity with labeled ground truth. The two works are complementary, and acknowledging the concurrent effort strengthens rather than weakens the novelty claim.
- [MINOR] (rigor) The Hodge energy decomposition finding—that 70.6% of net-flow energy is carried by the curl component—is presented in a way that implies it is a discovery about citation networks. In fact, it is a direct consequence of the synthetic generator injecting 10 cartel rings at 60% of the maximum edge weight. The fraction would be completely different in a real network or in a lightly manipulated synthetic one. The discussion paragraph ('In a real journal network without heavy manipulation, one would expect a higher gradient fraction') implicitly acknowledges this, but the figure and section heading give the opposite impression.
  Action: Re-title the section 'Hodge Energy Decomposition of the Synthetic Network' and explicitly state at the outset: 'The following energy fractions characterize the synthetic network with heavy injected manipulation and do not represent typical real-world citation networks.' If the real dataset is evaluated, run the energy decomposition on that network as well—the comparison between synthetic (70.6% curl) and real-world fractions would be a genuinely informative finding.
- [MINOR] (methodology) The gradient residual score (AUC 0.958) consistently outperforms the triangle curl score (AUC 0.931) even though the synthetic cartels are 3-node directed rings—exactly the triangular structure the curl is designed to detect. The paper notes only that the gradient residual 'detects any ranking-inconsistent flow (any cycle length, not just triangles)' but does not explain why this broader signal should outperform the triangle-specific signal on a network of purely triangular cartels.
  Action: Add a theoretical explanation in Section 3.3 or Section 6: cartel membership systematically distorts a journal's prestige potential s* (it receives excess incoming citations from partners AND sends excess outgoing citations to partners), creating a distinctive gradient residual signature on EVERY incident edge, not just triangular ones. This per-edge averaging provides more statistical power than averaging over a subset of triangles. If this explanation is correct, it implies the gradient residual would remain effective for non-triangular cartels, making it the recommended primary score—strengthen the recommendation accordingly.
- [MINOR] (clarity) The paper contains a complete 'Related Work' section appearing after the Conclusion (after Section 7), despite having a 'Background and Related Work' section (Section 2). The standalone Related Work section is almost entirely redundant with Section 2 and creates an incoherent document structure. It reads like a section accidentally duplicated during editing.
  Action: Delete the standalone Related Work section after the Conclusion. Any content that is genuinely not covered in Section 2 should be merged there. If the intent was to provide a concise summary of the paper's positioning against related work, a single-paragraph 'Relation to Prior Work' subsection in the Discussion (Section 6.2) would be more appropriate.
- [MINOR] (scope) The 40 suppressed journals in the released real dataset include journals suppressed for excessive self-citation (the majority of JCR suppressions—e.g., the entire 2020 MDPI mass-suppression event was for self-citation, not stacking) as well as citation stacking. The Hodge curl specifically detects inter-journal cyclic exchange; it cannot detect self-citation inflation. Any evaluation of the real dataset that uses the binary suppressed/clean label without distinguishing suppression type would mix these two fundamentally different behaviors, potentially deflating the Hodge detector's apparent performance and leading to incorrect conclusions.
  Action: In Section 4.2 and the Limitations section, explicitly distinguish the suppression types: annotate each suppressed journal as 'stacking' or 'self-citation' using the published Clarivate suppression lists (which specify the reason). Report the real-data evaluation separately for each suppression type, or restrict the positive class to stacking-only journals. This would make the evaluation epistemically clean and would also clarify the practical scope of the proposed method.
- [MINOR] (rigor) The 100-sample degree-preserving null model (row-permutation of W) preserves out-degree sequences but not the field structure of the citation network (12 scientific fields with within-field citation rates substantially higher than cross-field rates). A journal in a dense field will have many incident triangles with high curl even under legitimate within-field citation, and row-permutation may not adequately capture this field-level variance. Z-scores calibrated against this null could be systematically inflated for journals in dense fields.
  Action: Include field membership in the null model: permute citations only within field-pairs (i.e., preserve the field-level citation rate matrix as well as degree sequences). This is analogous to what CIDRE's dcSBM null does by conditioning on community structure. Report whether the z-scores change substantially under the field-aware null—if not, the current null is adequate; if they do, the field-aware null should replace it.
</previous_review>

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

### [2] HUMAN-USER prompt · 2026-07-09 01:50:01 UTC

```
Propose a simple, novel graph-based method for detecting citation patterns in academic networks and validate it.
```

### [3] SKILL-INPUT — aii-web-tools · 2026-07-09 01:51:37 UTC

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

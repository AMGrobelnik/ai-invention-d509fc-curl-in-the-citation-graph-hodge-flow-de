# gen_full_paper — report_results

> Phase: `gen_paper_repo` · `gen_full_paper`
> Run: `run_io13l_LyCX8s` — Curl in the Citation Graph: Hodge Flow Decomposition Detects Citation Cartels via Field-Aware Calibration
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_full_paper` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-07-09 02:46:01 UTC

````
<research_methodology>
Write like an experienced academic. Reviewers judge both the science and the writing.

- Claims must be proportional to evidence. Choose verbs carefully — "demonstrate," "observe," and "hypothesize" mean different things.
- Every result needs: what was measured, on what data, the numbers, and what they mean.
- Methodology must be specific enough to reproduce. Related work must be organized by theme, not a literature dump.
- State limitations honestly. Avoid both overclaiming and excessive hedging.
</research_methodology>

<system_reminder>
Do not ask follow up questions and do not ask the user anything. Execute all steps independently.
You must follow the todo list provided in each prompt exactly as written.
No placeholders, stubs, or incomplete code — all code must be complete and functional.
</system_reminder>

<process_isolation>
CRITICAL: Multiple pipeline runs may execute simultaneously on this machine. `ps aux | grep method.py` matches ALL runs, not just yours.
- NEVER kill processes by name (`killall`, `pkill -f`, `ps aux | grep ... | xargs kill`). This kills OTHER runs' processes.
- NEVER monitor processes by name (`ps aux | grep method.py`). You will see other runs' processes and get confused.
- ALWAYS use PID-based process management:
  Run: `uv run method.py & PID=$!` or `timeout <seconds> uv run method.py & PID=$!`
  Check: `kill -0 $PID 2>/dev/null && echo "Running" || echo "Ended"`
  Stop: `kill $PID`
  Wait: `wait $PID; echo "Exit code: $?"`
  Monitor: `tail -f logs/run.log & TAIL_PID=$!` then `kill $TAIL_PID` when done
</process_isolation>

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_io13l_LyCX8s/4_gen_paper_repo/_4_assemble_paper/paper/workspace`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_io13l_LyCX8s/4_gen_paper_repo/_4_assemble_paper/paper/workspace/`:
GOOD: `/ai-inventor/aii_data/runs/run_io13l_LyCX8s/4_gen_paper_repo/_4_assemble_paper/paper/workspace/file.py`, `/ai-inventor/aii_data/runs/run_io13l_LyCX8s/4_gen_paper_repo/_4_assemble_paper/paper/workspace/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>

<task>
Create a publication-ready top-conference LaTeX paper with BibTeX from <paper_text> and <available_figures>, compile to PDF.
</task>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<paper_text>
title: >-
  Curl in the Citation Graph: Hodge Flow Decomposition Detects Citation Cartels via Field-Aware Calibration
abstract: >-
  We apply the Helmholtz-Hodge decomposition to journal citation net-flows, separating any directed flow into three orthogonal
  components: a gradient (consistent with a global prestige ordering), a curl (local cyclic exchange inconsistent with any
  ranking), and a harmonic component. Citation manipulation-coordinated exchange among journals to inflate impact factors-injects
  cyclic flow, theoretically concentrating in the curl. We evaluate this framework on a real 231-journal OpenAlex citation
  network annotated with Clarivate JCR suppression labels, restricting the primary positive class to 7 confirmed citation-stacking
  journals (excluding 33 suppressed for excessive self-citation, which the curl detector cannot address by design). Raw Hodge
  scores fall below chance (gradient residual AUC = 0.454, curl AUC = 0.430), because stacking journals in this network are
  predominantly low-connectivity nodes lacking the triangular structure the curl operator requires. However, a field-aware
  z-score-calibrating each journal's curl against the distribution expected within its research community-achieves AUC = 0.718
  (95% CI [0.459, 0.922]), the strongest result in our evaluation and well above the CIDRE-fallback baseline (AUC = 0.343).
  A clean-base injection study across cyclic and reciprocal cartel types (k in {3, 4, 5, 10}) and five weight levels confirms
  that individual small-cartel detection is fundamentally limited (best AUC = 0.617; no condition exceeds 0.7). A key empirical
  finding challenges the method's founding assumption: the real citation network carries 77% of net-flow energy in the curl
  component-not the gradient-revealing substantial natural circularity that makes field-relative calibration necessary. We
  release the first openly annotated journal citation network with JCR stacking/self-citation labels to support future detection
  research.
paper_text: |-
  # Introduction

  The impact factor of a journal determines where researchers publish, which papers get read, and ultimately how scientists are hired and funded. This makes citation metrics a high-stakes target for gaming. Each year Clarivate removes journals from the Journal Citation Reports (JCR) for *citation stacking*-coordinated citation exchange between journals designed to artificially inflate impact factors-and for excessive self-citation. Since 2018, over 100 journals have been suppressed for such manipulation [ARTIFACT:art_Md6TNdV-FZYE], spanning every continent and scientific discipline, from Romanian materials-science rings to Brazilian agricultural clusters to 2021 Frontiers stacking cases.

  The state-of-the-art detector is CIDRE [2], which fits a degree-corrected stochastic block model (dcSBM) to the journal citation graph and flags groups that exchange citations at rates anomalous relative to the community null. CIDRE detects 12 of 22 known stacking groups in its 2013 MAG evaluation and represents a landmark advance. However, density-based methods share a structural weakness: they measure *how many* citations flow between a group of journals, not *how consistently* those citations follow a prestige hierarchy. This conflation generates two systematic errors: densely-cross-cited legitimate communities appear anomalous, and cartels that limit citation volumes to stay below density thresholds may avoid detection entirely.

  We import the Helmholtz-Hodge decomposition from mathematical physics to supply a density-independent structural definition of manipulation. The Hodge decomposition of any flow on a graph yields three orthogonal components: a *gradient* flow consistent with a global prestige potential (the HodgeRank score [1]); a *curl* flow of local cyclic loops that no global ranking can explain; and a *harmonic* flow of large-scale cycles. Legitimate scholarly influence flows 'downhill' along the prestige gradient; citation cartels inject flow that *circulates*, producing local curl. This gives an operational, density-independent definition: **manipulation is curl**.

  We evaluate this framework on a real 231-journal OpenAlex citation network annotated with JCR suppression labels \footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-d509fc-curl-in-the-citation-graph-hodge-flow-de/tree/main/round-1/dataset-1}}, restricting the primary positive class to the 7 confirmed stacking journals (excluding 33 suppressed for excessive self-citation, which the curl detector cannot address by design). A critical empirical finding challenges the method's founding assumption: the real network carries 77.0% of net-flow energy in the curl component-not in the gradient as legitimate scholarly flow predicts. This reveals substantial natural circularity in journal-level citation exchange, making raw curl magnitude non-discriminative. Instead, a *field-aware* z-score that calibrates each journal's curl against its research community's expectations achieves AUC = 0.718 (95% CI [0.459, 0.922])-the strongest result across all methods evaluated \footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-d509fc-curl-in-the-citation-graph-hodge-flow-de/tree/main/round-2/experiment-1}}.

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

  Let $\mathcal{G} = (V, E, W)$ be a directed weighted graph where $V$ is the set of journals, $E$ is the set of ordered pairs $(i, j)$ with at least $\tau$ total citations ($W_{ij} + W_{ji} \geq \tau$), and $W_{ij}$ is the total number of citations from journal $i$ to journal $j$ over a multi-year window. We form the *net-flow matrix* $Y_{ij} = W_{ij} - W_{ji}$ (antisymmetric by construction). The net-flow captures citation *imbalance*: $Y_{ij} > 0$ means journal $i$ cites $j$ more than the reverse, consistent with $j$ having higher prestige. We represent the graph in canonical edge orientation (edge $(i,j)$ with $i < j$), yielding a flow vector $Y_e \in \mathbb{R}^{|E|}$. \footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-d509fc-curl-in-the-citation-graph-hodge-flow-de/tree/main/round-1/experiment-1}}

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

   We constructed a journal citation network from the OpenAlex API [5], aggregating citation links across 2015-2022. The network covers 231 high-impact journals (top by cited-by count), 9,146 directed citation pairs, and 230,336 triangles derived from 668,390 underlying work-level citation links.

  **Suppression type distinction.** Each journal is annotated with a Clarivate JCR suppression label (2018-2022) [ARTIFACT:art_Md6TNdV-FZYE]. We critically distinguish two suppression types:

  - *Citation stacking* (7 journals in our network): coordinated inter-journal citation exchange-organized rings, systematic mutual citation between two or more outlets. Confirmed cases include journals from the 2021 JCR list (Archivos Latinoamericanos de Nutrition, Journal of Intelligent and Fuzzy Systems, Materials Express, Hellenic Journal of Cardiology) and the 2018 list (Liver Cancer/Digestive Diseases/Oncology stacking ring, History of Economic Thought mutual pair) [ARTIFACT:art_gkqGp1-55dg1].
  - *Excessive self-citation* (33 journals): inflating impact factors by citing the journal's own back-catalog. The Hodge curl detector measures *inter-journal* cyclic exchange and cannot in principle detect self-citation.

  This distinction is essential. The 2020 JCR suppression event (33 journals including Sustainability, Sensors, IJERPH, and other MDPI titles) is entirely self-citation; including it in the positive class would introduce 33 journals the curl detector was never designed to find. All primary evaluations use the 7 stacking-only positives. We also report results for all 40 suppressed journals as a secondary evaluation.

  ## Synthetic Citation Network

  For controlled validation, we use an 800-journal synthetic network with 12 scientific fields, exponential prestige scores, and citation weights proportional to prestige. After thresholding ($\tau = 3$), the network has $E = 15,639$ edges, $T = 75,227$ triangles, and mean edge weight $\bar{w} = 3.23$. Cartel injection (Section 5.3) operates on a clean base ($n_c = 0$) to test detection in isolation. A pre-loaded variant with $n_c = 10$ injected 3-node cyclic rings (30 cartel positives) serves as the controlled synthetic validation (Section 5.2) .

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

  On the controlled synthetic network ($n_c = 10$, 30 cartel-member positives),  the Hodge gradient residual achieves AUC = 0.737 (CI [0.686, 0.785]) and the CIDRE-fallback achieves AUC = 0.845 (CI [0.766, 0.912]). The triangle curl achieves AUC = 0.558 (CI [0.457, 0.656]). The higher CIDRE-fallback performance reflects that the spectral clustering null accurately recovers the planted field structure in this synthetic network.

  These results confirm that the Hodge approach operates correctly under controlled cartel conditions and that gradient residual outperforms triangle curl even when cartels are exactly 3-node rings (AUC 0.737 vs. 0.558). This counterintuitive finding-that the gradient residual beats the triangle-specific curl on triangular cartels-is explained in Section 6.1.

  ## Clean-Base Injection Study

  [FIGURE:fig3]

  To assess detection sensitivity in isolation, we inject cartels into the clean base network ($n_c = 0$) and sweep cartel type $\in$ \{cyclic, reciprocal\}, size $k \in \{3, 4, 5, 10\}$, and weight factor $w_f \in \{0.1, 0.3, 0.5, 1.0, 2.0\} \times \bar{w}$ (20 repetitions per condition, 40 conditions total). This directly addresses the critique that prior injection experiments were confounded by pre-existing background manipulation .

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
summary: >-
  This paper applies the Helmholtz-Hodge decomposition to citation cartel detection on a real 231-journal OpenAlex network
  with JCR suppression labels (7 stacking-only positives). The key finding is that raw Hodge scores fail (AUC < 0.5) because
  real citation networks are 77% curl-dominant, making raw curl magnitude non-discriminative; field-aware calibration against
  community curl expectations achieves AUC = 0.718, the strongest result across all methods. A clean-base injection study
  across cyclic (k=3,4,5,10) and reciprocal cartel types confirms individual small-cartel detection is fundamentally limited
  (best AUC = 0.617). The paper introduces the critical distinction between citation stacking (7 journals, the proper positive
  class for curl detection) and self-citation suppression (33 journals, invisible to inter-journal curl), and discusses why
  the gradient residual outperforms triangle curl even on triangular cartels.
</paper_text>

<available_figures>
--- Item 1 ---
id: fig1
title: Hodge Citation Cartel Detection Pipeline
caption: >-
  End-to-end pipeline for Hodge-based citation cartel detection. Citation counts are aggregated into a net-flow matrix, decomposed
  into gradient (prestige hierarchy), curl (cyclic manipulation), and harmonic (global loops) components via sparse least-squares.
  Three detection scores are derived: gradient residual (averaging all incident edge departures), triangle curl (averaging
  3-ring circulation), and field-aware z-score (calibrating curl against community expectations). The field-aware z-score
  achieves AUC = 0.718 on real stacking-only labels, the strongest result in our evaluation.
image_gen_detailed_description: |-
  Horizontal pipeline diagram, left-to-right flow, five main stages connected by arrows. White background, sans-serif font, clean minimal style.

  Stage 1 (leftmost, gray box): 'Citation Network' — journals as circular nodes, directed edges as arrows, label 'W_ij = citations i→j'

  Arrow labeled 'Y_ij = W_ij - W_ji' pointing right.

  Stage 2 (light blue box): 'Net-Flow Matrix Y' — small grid/matrix icon, label 'antisymmetric net citation imbalance'

  Arrow labeled 'Hodge decomp. (sparse lsqr)' pointing right.

  Stage 3 (central, wide, yellow-bordered box): 'Hodge Decomposition Y = Y_grad + Y_curl + Y_harm' — splits into three sub-boxes arranged vertically inside:
    - Top sub-box (blue): 'Gradient Y_grad: Prestige potential s*, 23% of energy (real network)'
    - Middle sub-box (orange): 'Curl Y_curl: Triangle circulation κ, 77% of energy (real network)'
    - Bottom sub-box (light gray): 'Harmonic Y_harm: Global loops, <0.001% energy'

  Arrow pointing right to Stage 4.

  Stage 4 (green box): 'Detection Scores' — three bullet points:
    '• Gradient residual ρ: avg |Y_e - Y_grad| per edge'
    '• Triangle curl κ: avg curl per triangle'
    '• Field-aware z-score: κ vs community null'

  Arrow labeled 'calibrate vs community' pointing right.

  Stage 5 (rightmost, dark green box): 'Rankings & Alerts' — label 'AUC = 0.718 (field-aware)' with a small upward bar-chart icon.

  Below the entire pipeline: a note box 'Key insight: 77% of real citation flow is curl-dominant — field-relative calibration is necessary'
aspect_ratio: '21:9'
summary: >-
  Hero architecture diagram showing the full pipeline from citation network to Hodge decomposition to field-aware detection
  scores
figure_path: figures/fig1_v0.jpg

--- Item 2 ---
id: fig2
title: Detection AUC on Real Citation Data
caption: >-
  AUC-ROC for all methods on the real 231-journal citation network with stacking-only labels (7 positives). Error bars show
  95% bootstrap confidence intervals. The field-aware null z-score (AUC = 0.718) is the only method substantially above chance.
  Raw Hodge scores fall below 0.5 due to the isolated-node structure of stacking journals in this network. The CIDRE-fallback
  uses spectral clustering + Poisson null (the published CIDRE package is incompatible with Python 3.12).
image_gen_detailed_description: |-
  Horizontal bar chart. White background. Sans-serif font. Title: 'AUC on Real Data (Stacking-Only Labels, n=7 positives)'.

  Y-axis (left): method names, top to bottom:
    'Field-Aware Null z-score'
    'Degree-Preserving Null z-score'
    'HodgeRank Prestige'
    'Hodge Gradient Residual'
    'Hodge Curl Raw'
    'CIDRE Fallback'

  X-axis (bottom): AUC value, range 0.0 to 1.0, labeled 'AUC-ROC'.

  Bar values (left to right):
    'Field-Aware Null z-score': 0.718, dark blue bar, error bar [0.459, 0.922]
    'Degree-Preserving Null z-score': 0.618, medium blue bar, error bar [0.352, 0.876]
    'HodgeRank Prestige': 0.551, teal bar, error bar [0.263, 0.813]
    'Hodge Gradient Residual': 0.454, orange bar, error bar [0.152, 0.752]
    'Hodge Curl Raw': 0.430, yellow-orange bar, error bar [0.144, 0.726]
    'CIDRE Fallback': 0.343, red bar, error bar [0.115, 0.590]

  Vertical dashed line at x=0.5, labeled 'Chance'.
  Vertical dashed line at x=0.7, labeled 'Detection threshold'.

  Small annotation on Field-Aware bar: 'BEST: 0.718'
  Small annotation on CIDRE bar: '0.343 (approx.)'
aspect_ratio: '21:9'
summary: >-
  Bar chart comparing AUC of all detection methods on real stacking-only labels, showing field-aware null model as the strongest
  signal
figure_path: figures/fig2_v0.jpg

--- Item 3 ---
id: fig3
title: 'Injection Study: AUC vs. Cartel Weight'
caption: >-
  AUC-ROC of the gradient residual detector as a function of injection weight factor ($w_f$, multiples of mean edge weight
  $\bar{w} = 3.23$) on a clean base network ($n_c = 0$, 800 journals), averaged over 20 repetitions per condition. Lines show
  different cartel types and ring sizes. No condition exceeds AUC = 0.7. The gradient residual achieves its best result (0.617)
  only for the smallest cyclic ring ($k = 3$) at the heaviest injection weight ($2.0\bar{w}$). Larger rings ($k = 5, 10$)
  and reciprocal cliques remain near chance across all weights.
image_gen_detailed_description: |-
  Line chart. White background. Sans-serif font. Title: 'Injection Study: Gradient Residual AUC vs. Injection Weight'.

  X-axis: injection weight factor (multiples of mean edge weight), values: 0.1, 0.3, 0.5, 1.0, 2.0. Label: 'Weight factor (× mean edge weight = 3.23)'.

  Y-axis: AUC-ROC, range 0.3 to 0.75. Label: 'AUC-ROC (gradient residual)'.

  Lines (with markers):
    Solid blue line, circles: 'Cyclic k=3', values: w=0.1→0.473, w=0.3→0.452, w=0.5→0.462, w=1.0→0.533, w=2.0→0.617
    Solid green line, squares: 'Cyclic k=5', values: w=0.1→0.536, w=0.3→0.488, w=0.5→0.501, w=1.0→0.486, w=2.0→0.514
    Solid red line, diamonds: 'Cyclic k=10', values: w=0.1→0.465, w=0.3→0.475, w=0.5→0.530, w=1.0→0.515, w=2.0→0.557
    Dashed purple line, triangles: 'Reciprocal k=3', values: w=0.1→0.481, w=0.3→0.480, w=0.5→0.425, w=1.0→0.484, w=2.0→0.546

  Horizontal dashed gray line at AUC=0.5, labeled 'Chance'.
  Horizontal dashed orange line at AUC=0.7, labeled 'Detection threshold (AUC=0.7)'.

  Annotation at top right of cyclic k=3 line at w=2.0: 'Best: 0.617'

  Legend in upper right corner.
aspect_ratio: '21:9'
summary: >-
  Line chart showing that clean-base injection detection AUC peaks at 0.617 and no condition exceeds 0.7, confirming individual
  cartel detection is fundamentally limited
figure_path: figures/fig3_v0.jpg

--- Item 4 ---
id: fig4
title: 'Hodge Energy Fractions: Real vs. Synthetic'
caption: >-
  Hodge energy fractions (fraction of total net-flow energy $\|Y_e\|^2$) for the real 231-journal network and the synthetic
  $n_c=10$ network. The real network is 77% curl-dominant, nearly identical to the synthetic network with 30 injected cartel
  members (78% curl). The gradient fraction of the real network (23%) is higher than the synthetic (4.3%), reflecting genuine
  citation hierarchy, but both are curl-dominated. The near-zero harmonic fraction in the real network reflects its high triangle
  density ($T = 230,336$).
image_gen_detailed_description: |-
  Grouped bar chart. White background. Sans-serif font. Title: 'Hodge Energy Decomposition: Real vs. Synthetic Network'.

  X-axis: two groups, labeled 'Real (231 journals)' and 'Synthetic (n_c=10, 800 journals)'.

  Y-axis: energy fraction, range 0.0 to 1.0. Label: 'Fraction of net-flow energy'.

  For each group, three side-by-side bars:
    'Gradient' bar (dark blue):
      Real: 0.230
      Synthetic: 0.043
    'Curl' bar (orange):
      Real: 0.770
      Synthetic: 0.780
    'Harmonic' bar (light blue):
      Real: 0.000 (essentially zero)
      Synthetic: 0.178

  Data labels on each bar showing exact values:
    Real gradient: '23.0%'
    Real curl: '77.0%'
    Real harmonic: '<0.1%'
    Synthetic gradient: '4.3%'
    Synthetic curl: '78.0%'
    Synthetic harmonic: '17.8%'

  Annotation box at top: 'Key finding: Real citation network is 77% curl-dominant, nearly identical to a heavily manipulated synthetic network (78%)'

  Legend below chart: dark blue = Gradient, orange = Curl, light blue = Harmonic
aspect_ratio: '21:9'
summary: >-
  Grouped bar chart comparing Hodge energy fractions for real and synthetic networks, showing both are 77-78% curl-dominant
figure_path: figures/fig4_v0.jpg
</available_figures>

<figure_requirements>
CRITICAL: Include ALL figures from <available_figures>. No exceptions.

- Every figure MUST use \includegraphics{figures/filename.jpg}
- Do NOT skip, convert to tables, or describe without inserting
- Each needs: \begin{figure*|figure}[placement], \includegraphics, \caption, \label, \end{...} — pick env + placement by the figure's `aspect_ratio` field (see PLACEMENT below). Constrain every \includegraphics with `width=\linewidth,height=0.4\textheight,keepaspectratio` (single-column) or `width=\textwidth,height=0.45\textheight,keepaspectratio` (figure*). Use exactly these option keys — `max height=` is NOT valid LaTeX
- Use the `caption` field from each figure for \caption{...} — do NOT invent new captions
- Place figures where their [FIGURE:fig_id] markers appear in paper_text
- VERIFICATION: paper.tex MUST have exact same number of \includegraphics as <available_figures>
- Do NOT generate new figure images (no matplotlib, no PIL, no image generation). Use ONLY the pre-generated figures from <available_figures>. They were already created by a previous pipeline step.

PLACEMENT BY ASPECT RATIO (use the `aspect_ratio` field on each figure):
- `21:9` (architecture diagrams / hero figures): \begin{figure*}[!t] (full two-column width, top of page). The hero architecture diagram should appear EARLY in the paper — typically at the top of page 2. Marker placement in paper_text already determines this; preserve it.
- `16:9` (comparisons, multi-panel results): \begin{figure*}[!t] for full-width or \begin{figure}[!htbp] for single-column.
- `4:3` / `1:1` / `3:2` / `3:4` / `9:16`: \begin{figure}[!htbp] (single-column).
</figure_requirements>

<artifact_links>
The paper_text contains \footnote{Code: \url{...}} references linking to artifact source code
on GitHub. Include \usepackage{hyperref} and \usepackage{url}.
Preserve these exactly as-is — do not remove, rewrite, or convert them to plain text.
The URLs will not resolve yet (the repo is deployed after compilation) — do NOT try to verify or fix them.
</artifact_links>

<headings>
NEVER use inline math (``$...$``) inside ``\section{...}`` / ``\subsection{...}`` / ``\subsubsection{...}`` arguments — hyperref's bookmark builder errors out (``Token not allowed in a PDF string``) and the PDF outline breaks. If a section heading needs a math-looking term, use the text equivalent (``d star`` not ``$d^*$``, ``alpha-equivalent`` not ``$\alpha$-equivalent``) or wrap it in ``\texorpdfstring{$math$}{plain}``. Inline math inside body paragraphs is fine.
</headings>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-to-latex, aii-semscholar-bib.
TODO 2. Review <paper_text> and <available_figures>. Copy all figure images into ./figures/ in your workspace. Count figures — MUST include every one. Plan placements per section. Build `./references.bib` via aii_semscholar_bib__fetch — collect DOIs/ArXiv IDs from <paper_text> and batch-fetch all BibTeX in one call. Do NOT fabricate entries.
TODO 3. Create `./paper.tex` per aii-paper-to-latex skill's setup, write ALL sections, insert ALL figures from <available_figures>, include `./references.bib` via \bibliography. Compile to PDF per skill's process. Fix errors.
TODO 4. CRITICAL VERIFICATION: Run `grep -c 'includegraphics' paper.tex`, confirm count equals figures in <available_figures>. If not, add missing figures. Verify `./paper.pdf` was created.
TODO 5. VISUAL REVIEW: Write Python script to convert EVERY page of paper.pdf to PNG at 150 DPI (use pdf2image or pymupdf). Then read ALL page screenshots — each page image costs ~1,600 tokens so a 15-page paper is only ~24K tokens. You MUST read every page. The ONLY exception is if all page images would not fit in your remaining context — in that case, read as many as fit and state which pages you are skipping and why. Check every page for layout issues, overlapping figures, cut-off text, bad spacing, formatting problems. Fix issues and recompile.
TODO 6. FINAL READ: Check page count (`pdfinfo paper.pdf` or pymupdf). Read entire paper.pdf — check for missing sections, unclear explanations, inconsistencies, typos. Fix and recompile. The ONLY exception is if all pages would not fit in your remaining context — in that case, read as many pages as fit and state which pages you are skipping and why.
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FullPaperExpectedFiles": {
      "description": "All expected output files from full paper generation.",
      "properties": {
        "paper_tex_path": {
          "description": "Path to LaTeX source file. Example: 'paper.tex'",
          "title": "Paper Tex Path",
          "type": "string"
        },
        "paper_pdf_path": {
          "description": "Path to compiled PDF. Example: 'paper.pdf'",
          "title": "Paper Pdf Path",
          "type": "string"
        },
        "references_bib_path": {
          "description": "Path to BibTeX bibliography file. Example: 'references.bib'",
          "title": "References Bib Path",
          "type": "string"
        },
        "figure_paths": {
          "description": "Paths to all figure image files. Example: ['figures/fig1_v0.jpg', 'figures/fig2_v0.jpg']",
          "items": {
            "type": "string"
          },
          "title": "Figure Paths",
          "type": "array"
        }
      },
      "required": [
        "paper_tex_path",
        "paper_pdf_path",
        "references_bib_path",
        "figure_paths"
      ],
      "title": "FullPaperExpectedFiles",
      "type": "object"
    }
  },
  "description": "Full paper \u2014 structured output from paper generation.",
  "properties": {
    "title": {
      "description": "Paper title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance. Aim for about 4-8 words (~40 characters).",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "description": "Brief summary of the generated paper: sections written, figures included, compilation status",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/FullPaperExpectedFiles",
      "description": "All output files you created. Must include paper.tex, paper.pdf, references.bib, and paths to all figure files."
    }
  },
  "required": [
    "title",
    "summary",
    "out_expected_files"
  ],
  "title": "FullPaper",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-07-09 02:46:01 UTC

```
Propose a simple, novel graph-based method for detecting citation patterns in academic networks and validate it.
```

### [3] SKILL-INPUT — aii-paper-to-latex · 2026-07-09 02:46:05 UTC

The agent loaded the **aii-paper-to-latex** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-to-latex
description: LaTeX paper assembly and compilation. Covers document setup, figure inclusion from pre-generated JPEGs, compilation process, and output files. Use when assembling a paper from pre-written text and pre-generated figures into a compiled PDF.
---

## LaTeX Paper Assembly

Assembles a research paper from paper text, pre-generated figure JPEGs, and bibliography into a compiled PDF.

### Document Setup

```latex
\documentclass[11pt,letterpaper]{article}
\usepackage{graphicx, geometry, amsmath, hyperref, natbib, booktabs, xcolor, listings}
\geometry{margin=1in}
\hypersetup{colorlinks=true, linkcolor=black, citecolor=black, urlcolor=black}
```

### Figure Inclusion

CRITICAL: Include ALL figures. Every figure MUST appear in the paper.

```latex
\begin{figure}[!htbp]
  \centering
  \includegraphics[width=0.92\textwidth,keepaspectratio]{figures/filename.jpg}
  \caption{Descriptive caption.}
  \label{fig:label}
\end{figure}
```

Rules:
- ALWAYS use `[!htbp]` float placement (NOT `[t]` or `[h]` alone)
- ALWAYS constrain with `width` and `keepaspectratio` to prevent page takeover
- Every figure needs `\caption`, `\label`, and a `\ref` in the text
- Do NOT convert figures to tables or describe them without inserting the image
- Do NOT skip any figures

### Compilation Process

Run each command separately (do NOT chain with `&&` — pdflatex often exits non-zero on warnings, which would skip bibtex and leave citations as `??`):

```bash
pdflatex -interaction=nonstopmode paper.tex
bibtex paper
pdflatex -interaction=nonstopmode paper.tex
pdflatex -interaction=nonstopmode paper.tex
```

All four commands are required. Skipping bibtex causes `??` in all citations.
Fix any errors between runs. Verify `./paper.pdf` was created.

### Output Files

- `./paper.tex` — LaTeX source
- `./references.bib` — bibliography file
- `./paper.pdf` — compiled PDF
- `./figures/*.jpg` — all figure images (pre-generated, copied into workspace)
````

### [4] SKILL-INPUT — aii-semscholar-bib · 2026-07-09 02:46:10 UTC

The agent loaded the **aii-semscholar-bib** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-semscholar-bib
description: Build bibliographies using Semantic Scholar. Batch-fetch BibTeX for papers by DOI, ArXiv ID, or title. Use when writing papers, generating reference lists, or building .bib files.
---

## Tool: `aii_semscholar_bib__fetch`

Batch-fetch BibTeX entries from Semantic Scholar. Pass all references in a single call — the tool handles batching internally.

### How it works

1. **DOI/ArXiv refs** → batched into POST /paper/batch calls (up to 500 per API call, auto-chunked)
2. **Title-only refs** → individual GET /paper/search/match (1s delay between)
3. **Post-process** → fix entry type, fix citation key (AuthorYYYY), inject DOI

The ability server runs a single worker (`max_threads: 1`). Multiple concurrent tool calls are queued — each runs independently (no cross-request aggregation). Batching happens within each request.

### Input format

```json
{
  "references": [
    {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
    {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
    {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
  ]
}
```

Each reference object can have:
- `doi` — DOI string (ArXiv DOIs like `10.48550/arXiv.XXXX.XXXXX` auto-convert to ArXiv IDs)
- `arxiv` — ArXiv ID (e.g. `"2305.14325"`)
- `title` — Paper title (used for search/match when no DOI/ArXiv)
- `author` — First author last name (for cleaner citation key)
- `year` — Publication year (int, for citation key)

At least one of `doi`, `arxiv`, or `title` is required per reference.

### Output format

```json
{
  "success": true,
  "bib_text": "@inproceedings{Vaswani2017, ...}\n\n@article{Wei2022, ...}",
  "total": 3,
  "found": 3,
  "failed_count": 0,
  "entries": [{"citation_key": "Vaswani2017", "bibtex": "...", "title": "...", "doi": "...", "arxiv": ""}],
  "failed": []
}
```

### Workflow

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in **one call**
3. Save `bib_text` from the response to your `references.bib` file
4. Check `failed` — for any missed papers, follow the **fallback procedure** below

### Fallback for failed references (MANDATORY)

NEVER fabricate BibTeX. For each failed reference:
1. **WebSearch** for `"Title" author year` (try `site:arxiv.org` too)
2. **WebFetch** the paper page → extract title, authors, year, venue, DOI/ArXiv ID
3. If DOI/ArXiv found → retry `aii_semscholar_bib__fetch` with it
4. Last resort: write BibTeX by hand using **only verified info from the actual paper page**

---

### CLI (for manual use / debugging)

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-semscholar-bib" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_semscholar_bib__fetch.py --refs '[
  {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
  {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
  {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
]'
```

`--json, -j` — output raw JSON instead of .bib text

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

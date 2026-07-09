# upd_hypo — test_idea

> Phase: `invention_loop` · round 2 · `upd_hypo`
> Run: `run_io13l_LyCX8s` — Academic Citation Patterns
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `upd_hypo` (terminal_claude_agent, claude-sonnet-4-6)

### [1] CONFIG · 2026-07-09 01:56:08 UTC

```
model: claude-sonnet-4-6 | effort: high | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/upd_hypo/upd_hypo
```

### [2] SYSTEM-USER prompt · 2026-07-09 01:56:16 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A hypothesis reviser (Step 3.6: UPD_HYPO in the invention loop)

You received the current hypothesis, all artifacts, and the paper draft.
Revise the hypothesis based on what the evidence supports.

Honest revision → focused research. Inflated confidence → wasted iteration.
</your_role>
</ai_inventor_context>

You are revising a research hypothesis based on empirical evidence gathered
during an iterative invention loop. Your role is internal reflection — honest
assessment of what the evidence supports.

SCOPE: Your ONLY output is the revised hypothesis text. You do NOT run code,
produce artifacts, fix bugs, or otherwise act on the evidence yourself — the
next iteration of the invention loop will spawn fresh artifacts based on your
revised hypothesis. Reflect on the evidence and rewrite the hypothesis;
nothing else.

PRINCIPLES:
- Ground every revision in specific artifacts and results
- Treat negative and null results as valuable contributions. If the original
  approach failed, the null result IS often the contribution — frame it as
  such (e.g. "X does not improve Y under conditions Z"). Only pivot to a
  different positive claim when the evidence actually supports one; never
  fabricate a positive narrative to mask a failed approach.
- Increase specificity as evidence accumulates
- Don't inflate confidence without strong evidence
- Preserve the core AII prompt unless evidence clearly contradicts it
- Revise hypothesis text only — never attempt to address feedback by running
  code, proposing fixes, or producing artifacts; the next loop iteration
  handles all artifact generation

<current_hypothesis>
The hypothesis as it stands. Revise it based on the evidence below.

kind: hypothesis
title: Citation loops reveal cartel structure
hypothesis: >-
  A citation-flow network can be decomposed, via combinatorial Hodge theory (the graph-theoretic port of the Helmholtz-Hodge
  decomposition), into three orthogonal components: (1) a GRADIENT flow consistent with a single global 'prestige potential';
  (2) a CURL flow made of local cyclic loops that no global ranking can explain; and (3) a HARMONIC flow of large-scale cross-network
  cycles. We hypothesize that coordinated citation manipulation—cartels, citation stacking, and reciprocal-citation rings—injects
  ranking-inconsistent cyclic flow (curl), while genuine scholarly influence is gradient-dominated. Crucially, the empirically
  strongest detector is NOT the triangle curl score directly, but the GRADIENT RESIDUAL: the per-node average absolute departure
  of observed net-flow from the prestige-potential prediction, which picks up ranking-inconsistent signals of ANY cycle length
  (not only triangles) by averaging over all incident edges, giving substantially higher statistical power. The triangle curl
  score (B₂ h★) is interpretable and localizes manipulation to specific 3-rings, but it is outperformed on detection AUC even
  when cartels are exactly 3-node rings (0.931 vs. 0.958), because the gradient residual accumulates evidence from every incident
  edge rather than only the subset forming triangles. For longer-ring cartels (k ≥ 4), the triangle curl will degrade further
  while the gradient residual remains informative; for these cases the CDFD (Circular Directional Flow Decomposition) all-cycle
  circularity index provides a mathematically complete alternative. The central structural advantage of both the gradient
  residual and curl over density-based methods (CIDRE, stochastic block models) is ORTHOGONALITY: by construction, a densely-connected
  but internally hierarchical research community carries zero curl and zero gradient residual, eliminating the community-vs-cartel
  confound without fitting a null model. This orthogonality claim holds by theorem; the empirical claim—that it translates
  into measurably better recall at equal precision on real suppressed journals—remains to be confirmed on real JCR data and
  with proper CIDRE (full dcSBM) as baseline. The partial correlation result (r=0.153, CI [0.074, 0.238]) from the synthetic
  experiment offers initial evidence that curl carries information independent of density and reciprocity, but this must be
  replicated on the real 231-journal OpenAlex+JCR dataset before the independence claim is established empirically.
motivation: >-
  Citation counts and impact factors gate hiring, funding, promotion, and journal survival, creating a strong incentive to
  game them; citation cartels, citation stacking, and coerced/reciprocal citations corrupt the scientific record, and each
  year Clarivate suppresses journals for exactly this. Today's best detectors (CIDRE, community-detection variants, deep graph
  anomaly models) are fundamentally DENSITY-based, so they inherit two problems: they confound genuinely influential, tightly-knit
  research communities with cartels (dense healthy fields look anomalous), and they can miss manipulation that is deliberately
  kept sparse or spread across cyclic rings. They also offer no interpretable, structural DEFINITION of what manipulation
  actually is. Importing the Helmholtz-Hodge decomposition supplies exactly that: it gives a precise structural definition
  (manipulation = curl = citation flow that is inconsistent with any global prestige ordering), a detector that is orthogonal
  to density and therefore resolves the community-vs-cartel confound from first principles rather than by fitting a community
  null, edge/triangle-level localization that makes findings auditable for editors and integrity offices, and, for free from
  the same linear solve, a prestige ranking that certifies which regions are trustworthy versus corrupted. More broadly it
  reframes citation integrity through a conservation-law lens — legitimate knowledge flows 'downhill' along a potential, while
  fraud 'circulates' — a simple, transferable principle for reasoning about directed scholarly networks.
assumptions:
- >-
  Genuine scholarly influence is statistically hierarchy-consistent: at the aggregate (journal- or author-) level, legitimate
  citation flow largely admits a single global prestige ordering, so its internal circular/curl energy is low, because knowledge
  genuinely tends to flow from foundational toward frontier work.
- >-
  Coordinated manipulation (cartels, citation stacking among two or more outlets, reciprocal-citation rings) injects citation
  flow that defies any global ranking — cyclic, circulating exchange — producing local curl that exceeds a degree- and community-preserving
  null model.
- >-
  Aggregate citation networks accumulated over a time window contain enough genuine cycles for a meaningful Hodge decomposition
  (true at the journal/author scale, unlike the near-acyclic paper-to-paper level, where the arrow of time forbids cycles).
- >-
  Journals suppressed by Clarivate's Journal Citation Reports for citation stacking / excessive self-citation form an imperfect
  but usable ground-truth proxy for real-world manipulation, complementable by synthetic cartel injection.
- >-
  The curl/circular signal carries independent multi-node structural information (3+-node cycles and flux imbalance) beyond
  simple pairwise reciprocity or raw within-group density, so it is not merely a re-labeling of those quantities.
investigation_approach: >-
  (1) Build directed weighted citation-FLOW networks at the journal level (and, as an extension, the author level) from OpenAlex
  (MAG's open successor) and/or reuse the MAG-derived journal-citation data and code released with CIDRE, aggregating citations
  over rolling time windows. (2) Compute the Helmholtz-Hodge decomposition of the flow via the graph Helmholtzian / Hodge
  Laplacian: solve one sparse least-squares problem (scipy) for the gradient potential s that best explains the net edge flow
  Y (this is HodgeRank and yields a prestige ranking), then take the residual and separate it into curl (local, around triangles)
  and harmonic (global) parts; equivalently use a circular-directional-flow decomposition so that balanced reciprocal exchange
  is captured as pure circulation. (3) Turn the curl/circular component into a manipulation score at node, edge, triangle,
  and group level, and calibrate significance against a degree-preserving and a community-preserving (degree-corrected SBM)
  null so that ordinary field structure is discounted. (4) Validate on three fronts: (a) REAL ground truth — detect Clarivate
  JCR-suppressed journals (2018-2025 public lists) and compare head-to-head with CIDRE, reciprocity, within-group density,
  and Eigenfactor/PageRank on precision/recall/AUC and precision-at-k; (b) CONFOUND test — on hand-labeled dense genuine communities
  versus known cartels, test whether internal curl-fraction separates them where raw density cannot; (c) SYNTHETIC injection
  — inject cyclic-ring and reciprocal cartels of varying size and sparsity into a real network and measure detection as density
  decreases, where density methods should fail first. (5) As a secondary output, compare the gradient prestige ranking to
  Eigenfactor/PageRank and show the curl flags exactly the edges where those rankings are corrupted. All computation is CPU-only
  (sparse linear algebra); LLM/API use is negligible (at most compiling and cross-checking suppressed-journal lists), far
  under the $10 cap.
success_criteria: >-
  CONFIRMED if: (a) the curl/circular detector matches or exceeds CIDRE's recall of JCR-suppressed journals while achieving
  higher precision (fewer genuine-community false positives), with bootstrap confidence intervals excluding parity; (b) on
  synthetic injections the curl detector attains higher AUC than CIDRE and density/reciprocity baselines specifically in the
  sparse and cyclic regimes where density signal is weakest; (c) internal curl-fraction separates hand-labeled genuine dense
  communities from cartels with separation AUC whose CI excludes chance, whereas raw within-group density does not; (d) curl
  exceeds the degree/community null with significance and remains predictive after partialling out reciprocity and density
  (ablation / partial correlation), establishing it as an independent signal. DISCONFIRMED / boundary if: curl is statistically
  no better than reciprocity or density at any task; genuine influential communities carry as much internal curl as cartels;
  or the decomposition at the relevant scale is dominated by harmonic 'noise' so that curl is not localizable to specific
  groups.
related_works:
- >-
  CIDRE — 'Detecting anomalous citation groups in journal networks' (Kojaku, Livan, Masuda, Scientific Reports 2021): the
  state-of-the-art cartel detector; fits a degree-corrected stochastic block model as a null and flags groups of journals
  exchanging citations at excessive RATES (donors/recipients), catching >half of JCR-suppressed journals. DIFFERENCE: CIDRE
  is a DENSITY/rate detector that must fit a community null to avoid flagging healthy dense fields; our method is orthogonal
  to density — it defines manipulation as ranking-INCONSISTENT circulation (curl) and separates genuine communities (internally
  hierarchical, curl-free) from cartels (curl-heavy) from first principles, localizes to individual edges/triangles, and needs
  no block-model fit.
- >-
  HodgeRank / 'Statistical ranking and combinatorial Hodge theory' (Jiang, Lim, Yao, Ye, Mathematical Programming 2011): introduces
  Hodge decomposition of pairwise-comparison edge flows into gradient (global ranking) + curl + harmonic, applied to ranking
  with inconsistent data (sports, movies, crowdsourcing/e-commerce). DIFFERENCE: it is used only to produce a RANKING and
  to quantify overall ranking inconsistency; it has not been applied to citation networks, and it never uses the curl component
  as a manipulation/anomaly detector or connects inconsistency to citation integrity — we repurpose the curl as the primary
  signal and validate it against real manipulation ground truth.
- >-
  Helmholtz-Hodge / circular-flow decompositions of directed networks in OTHER domains — 'How circular is a directed network?'
  (Royal Society Open Science 2025), 'Circular Directional Flow Decomposition of Networks' (arXiv:2506.12546, 2025), and 'Causal
  Hierarchy in the Financial Market Network via the Helmholtz-Hodge-Kodaira Decomposition' (arXiv:2408.12839, 2024): decompose
  directed flows into acyclic/gradient + circular parts in finance, trade, transport, and brain networks. DIFFERENCE: none
  address citation networks, citation integrity, manipulation/anomaly detection, the genuine-community-vs-cartel confound,
  or validation against suppressed-journal ground truth — they measure circularity descriptively rather than using it as a
  calibrated detector.
- >-
  Eigenfactor / PageRank-based citation ranking (Bergstrom & West; Pinski & Narin): treat citations as random-walk FLOW to
  rank journals/papers by stationary influence. DIFFERENCE: they output a ranking but never separate flow that is CONSISTENT
  with a global order from flow that DEFIES it, so a manipulated ranking gives no warning; our gradient potential is a comparable
  ranking that self-certifies via the co-computed curl, flagging exactly where the ranking is corrupted.
- >-
  Deep / unsupervised citation-anomaly detectors — 'Deep Graph Learning for Anomalous Citation Detection' (arXiv:2202.11360)
  and 'Unsupervised Anomaly Detection in Journal-Level Citation Networks' (arXiv:2005.14343): learn embeddings/GNNs to score
  anomalous citations. DIFFERENCE: these are opaque, data-hungry, and provide no structural definition of manipulation; our
  method is a parameter-light, interpretable decomposition grounded in a theorem, with an explicit definition (manipulation
  = curl) and triangle-level localization.
- >-
  Trophic coherence / flow hierarchy of directed and citation networks (Johnson et al.; MacKay, Johnson & Sansom 2020; 'Universal
  hierarchical behavior of citation networks', arXiv:1401.4676): quantify the DEGREE of hierarchy or how well a global ordering
  exists. DIFFERENCE: these give a global scalar for how hierarchical a network is but do not DECOMPOSE the flow into consistent
  + inconsistent parts, do not localize where the hierarchy breaks, and do not target manipulation; the curl is precisely
  the complementary 'anti-hierarchy' residual, which we turn into a localizable detector.
inspiration: >-
  A Level-3 (methodological) cross-domain transfer. In fluid dynamics and vector calculus the Helmholtz decomposition states
  that any vector field splits uniquely into the gradient of a scalar potential plus a divergence-free rotational (curl) part;
  combinatorial Hodge theory ports this exactly to flows on graphs. This machinery has recently, and quietly, been powering
  discoveries of hidden circulation in finance, international trade, transport, brain dynamics, and even single-cell RNA velocity
  — yet no one has aimed it at scholarly citation integrity. The generative cross-field insight is a reframing: stop thinking
  of citation manipulation as 'too much density' (the bibliometrics default) and instead see it through a conservation-law
  lens — legitimate knowledge flows 'downhill' along a global prestige potential (a gradient), while manipulation is flow
  that 'circulates' with no consistent downhill direction (a curl). That single change of variable turns an intractable confound
  (healthy dense communities look like cartels) into a clean geometric separation, and it comes for free alongside a prestige
  ranking.
terms:
- term: Helmholtz-Hodge decomposition
  definition: >-
    A theorem stating that a flow (a vector field, or an edge-flow on a graph) splits uniquely into orthogonal parts: a gradient
    (potential/'downhill') component, a divergence-free rotational (curl/circulating) component, and, on graphs, a harmonic
    (global-loop) component.
- term: Gradient / potential flow
  definition: >-
    The part of citation flow explained by a single global 'prestige potential' assigned to each node; here it represents
    a consistent hierarchy in which citations run from foundational toward frontier work, and it doubles as a prestige ranking
    (the HodgeRank score).
- term: Curl / circular (divergence-free) flow
  definition: >-
    The part of citation flow made of local loops (e.g., A cites B cites C cites A, or imbalanced reciprocal exchange) that
    cannot be explained by any global ranking; hypothesized to be the structural fingerprint of citation cartels and stacking.
- term: Harmonic flow
  definition: >-
    Circulating flow that is locally consistent but globally cyclic — large-scale loops that close only across the whole network
    (e.g., cross-field citation loops); the third, global component of the decomposition.
- term: Combinatorial Hodge theory / HodgeRank
  definition: >-
    The discrete version of Hodge theory that performs the Helmholtz-Hodge decomposition on graphs via the graph Helmholtzian
    (Hodge Laplacian); computing the gradient part is a single sparse least-squares problem and yields a ranking (HodgeRank).
- term: Circularity index
  definition: >-
    A normalized scalar (0 = fully acyclic/hierarchical, 1 = fully circulating) measuring the fraction of a (sub)network's
    flow carried by the circular component; used here as a group-level manipulation score.
- term: Citation cartel / citation stacking
  definition: >-
    Coordinated inflation of citation metrics: a cartel is a group of authors/journals that agree to cite one another; citation
    stacking is anomalous citation exchange between two or more journals to boost impact factors.
- term: JCR suppression
  definition: >-
    Clarivate's annual removal of journals from Journal Citation Reports rankings for excessive self-citation or citation
    stacking; the published suppression lists provide real-world ground truth for manipulation.
- term: Degree-corrected stochastic block model (dcSBM) null
  definition: >-
    A random-graph null model preserving node degrees and community structure, used (e.g., by CIDRE) to discount the citations
    expected among journals of the same field/size when judging whether exchange is anomalous.
summary: >-
  Using the Helmholtz-Hodge (fluid-dynamics) decomposition ported to graphs, a citation network's flow splits into a 'downhill'
  gradient part that encodes a genuine prestige hierarchy and a 'circulating' curl part that no global ranking can explain;
  we hypothesize that citation manipulation is exactly this curl, giving a simple, density-independent detector that separates
  real influential communities from cartels — and beats density-based methods like CIDRE on suppressed-journal ground truth
  — while the same computation yields a self-certifying prestige ranking.
_relation_rationale: >-
  Same Hodge frame; elevates gradient residual as primary detector; real-world comparative claims remain provisional.
_confidence_delta: decreased
_key_changes:
- >-
  Promotes the GRADIENT RESIDUAL (not triangle curl) as the primary recommended detector, motivated by its AUC advantage (0.958
  vs. 0.931) even on 3-node ring cartels, explained by per-edge averaging providing greater statistical power than triangle-subset
  averaging.
- >-
  Explicitly scopes the triangle curl score to 3-clique cartel structures; flags that k≥4 rings will NOT be captured by B₂
  h★ and require CDFD all-cycle circularity for full coverage.
- >-
  Demotes the 'outperforms CIDRE' claim from confirmed to provisional: the CIDRE baseline was an approximation (Louvain/Poisson,
  not full dcSBM), its CI extended below 0.5, and the synthetic evaluation was circular (3-cycle detector vs. 3-cycle cartels).
  The comparative advantage claim requires re-running with the official cidre package on both synthetic varied cartel types
  and real JCR data.
- >-
  Adds explicit condition that real-world validation must restrict the positive class to citation-STACKING suppressed journals
  only (not self-citation suppressions, which Hodge curl cannot detect by design), and that the injection study must be re-run
  on a clean (n_c=0) base network to define a meaningful detectability threshold.
- >-
  Notes HLSAD (Frantzen and Schaub, KDD 2025, arXiv:2505.24534) as concurrent related work using Hodge Laplacian spectral
  properties for temporal anomaly detection — complementary in approach (spectral change-point vs. static flow decomposition)
  and should be distinguished in related work.
- >-
  Acknowledges the failed injection study as a methodological artifact: injecting into a pre-manipulated synthetic background
  merges new signals with existing curl noise; clean-base injection is required to define minimum detectable cartel size and
  weight.
- >-
  Retains the core orthogonality claim as a mathematical theorem (gradient and curl are orthogonal by construction of the
  Hodge decomposition), while treating its practical consequence (resolving community-vs-cartel confound) as an empirical
  hypothesis still requiring real-data validation.
relation_type: evolution
</current_hypothesis>

<all_artifacts>
Complete set of research artifacts across all iterations.

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
in_dependencies:
- id: art_Md6TNdV-FZYE
  label: extends
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
in_dependencies:
- id: art_IGeLtKiwHWQE
  label: dataset
- id: art_Md6TNdV-FZYE
  label: methodology
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
</all_artifacts>

<new_artifacts_this_iteration>
These 2 artifacts were created THIS iteration.

id: art_gkqGp1-55dg1
type: research
in_dependencies:
- id: art_Md6TNdV-FZYE
  label: extends
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

id: art_XbmaHSRFGigA
type: experiment
in_dependencies:
- id: art_IGeLtKiwHWQE
  label: dataset
- id: art_Md6TNdV-FZYE
  label: methodology
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
</new_artifacts_this_iteration>

<current_paper>
The paper draft from this iteration — represents the current state of the research story.

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
</current_paper>

<reviewer_feedback>
Feedback from the paper reviewer this iteration.

- [MAJOR] (evidence) The primary empirical result—AUC=0.718 on stacking-only labels—is not statistically significant. The bootstrap 95% CI is [0.459, 0.922], with the lower bound below 0.5 (random chance). With only 7 positive examples and 224 negatives, this CI width is expected, but it means the null hypothesis H0: AUC=0.5 cannot be rejected. The paper presents this AUC as 'the strongest result across all methods evaluated' in both the abstract and conclusion, which overstates the evidence. A bootstrap CI that includes 0.459 conveys uncertainty, but bootstrap CIs for AUC with 7 positives are known to have poor coverage properties; a permutation test is the appropriate significance test. Without statistical significance, the paper cannot claim the method 'detects' citation stacking—it can only claim 'suggestive evidence.'
  Action: Run a label-permutation test: permute the 7 stacking labels across the 231 journals 10,000 times, compute field-aware null z-score AUC for each permutation, and report the empirical p-value as fraction of permutations with AUC >= 0.718. If p < 0.05, report it; if not, revise the claim to 'promising but not yet statistically significant with n=7 positives.' Also tone down the abstract claim from 'strongest result' to 'highest point estimate.' Expected score impact: +0.5 to +1.0 overall if significance is demonstrated, or necessary for epistemic honesty if it is not.
- [MAJOR] (methodology) The CIDRE comparison is methodologically asymmetric in a way that confounds the paper's central performance claim. On the synthetic network (Section 5.2), the CIDRE fallback (spectral clustering + Poisson null) achieves AUC=0.845, substantially outperforming Hodge gradient residual (AUC=0.737). On the real network (Section 5.1), the same fallback achieves AUC=0.343, while Hodge field-aware achieves 0.718. The paper attributes the real-data reversal to CIDRE's dcSBM accurately recovering the planted synthetic block structure, but this explanation is not verified. More importantly, the 'incompatibility' of the CIDRE package with Python 3.12 is due to a pinned matplotlib==3.1.3 dependency—a visualization-only requirement confirmed by reviewing the CIDRE GitHub requirements.txt. The core CIDRE algorithm (dcSBM fitting + Poisson p-values) does not use matplotlib and could be run in a Python 3.8 or 3.9 virtualenv with no code changes, or by relaxing the matplotlib pin. Using a non-standard approximation as the sole CIDRE baseline, then claiming superiority over it, is not a valid comparison.
  Action: Create a Python 3.8 or 3.9 virtualenv (using pyenv or conda) and install cidre with matplotlib==3.1.3. Run the full dcSBM CIDRE on both the real and synthetic networks. Report the true CIDRE AUC alongside the fallback AUC, and discuss the gap between them. This will show whether the methodological gap between the paper's 'CIDRE-fallback' and the real CIDRE is material. If the full CIDRE achieves substantially higher AUC on real data, the paper's comparative advantage diminishes; if it does not, the paper is strengthened. Either way, the comparison becomes scientifically valid. Expected score impact: +0.5 if full CIDRE is run and compared.
- [MAJOR] (evidence) The injection study (Section 5.3) systematically fails to achieve AUC > 0.7 under any of the 40 tested conditions. The best result is cyclic k=3, w_f=2.0x mean edge weight, with gradient residual AUC=0.617 (SD=0.132). This injection weight corresponds to approximately 6.5x the mean edge weight—an unrealistically large synthetic perturbation. The paper frames this as 'defining a practical limitation,' which is honest, but does not draw the key implication: if the method cannot detect small-k cyclic cartels at up to 2x mean edge weight in a clean synthetic base, the real-data AUC=0.718 requires an explanation of what structural property of the real stacking journals enables detection where the synthetic cannot. The current paper offers no bridge between the injection-study failure and the real-data success—they appear inconsistent without explanation.
  Action: Add a paragraph in Section 6 (Discussion) explaining the apparent contradiction between the injection study (best AUC=0.617 in synthetic) and the real-data result (AUC=0.718). The most plausible explanation is that real stacking journals exhibit systematic field-relative curl anomaly across *multiple years and edges* in a way that synthetic point-injection at 2x weight does not replicate—the cartel behavior is repeated and persistent rather than single-injection. If this is the correct explanation, the paper should validate it: does the field-aware z-score of the real stacking journals reflect a systematic multi-edge pattern? Examining the per-journal citation time series would clarify this. Expected score impact: +0.3 from clarification alone; +0.5 if empirically validated.
- [MINOR] (rigor) The energy decomposition finding (Table 2, Section 5.4) reports that the real citation network is 77% curl-dominant and interprets this as 'natural circularity in journal-level citation exchange.' However, the real network contains 40 suppressed journals (7 stacking + 33 excessive self-citation). If even a fraction of these manipulated journals contribute disproportionately to the curl energy, the 77% figure would overstate the 'natural' curl level of clean citation networks. The comparison between real (77%) and synthetic-with-10-cartels (78%) is therefore potentially confounded: the near-equal curl fractions might reflect similar levels of manipulation rather than inherent properties of the network topology. The Section 6.2 argument for field-aware calibration depends on the assumption that 77% curl is 'natural,' which is not validated.
  Action: Recompute the Hodge energy decomposition for the 191 clean (non-suppressed) journals only—restrict to the subgraph induced by journals with label=0 and rerun the decomposition. If the clean subgraph still shows >70% curl, the 'natural circularity' claim is strongly supported. If the clean subgraph shows substantially lower curl (e.g., 50-60%), it suggests that the 40 suppressed journals are artificially inflating the estimate. Report this comparison explicitly in Table 2. Expected score impact: +0.3 for definitively grounding the curl-dominance claim.
- [MINOR] (clarity) There is an unexplained discrepancy between the edge counts reported in the paper and in the dataset artifact. Section 4.1 of the paper states '9,146 directed citation pairs' and the abstract also uses this number. The dataset artifact (art_IGeLtKiwHWQE) states '15,188 directed citation pairs' and 'full_data_out.json represents one directed citation pair' per row. The difference (roughly a factor of 1.66) is not explained anywhere in the paper. Both numbers appear in authoritative positions, creating confusion about what the dataset actually contains. The likely explanation—that 15,188 is the pre-threshold raw directed pair count and 9,146 is the post-threshold canonical net-flow edge count—should be stated explicitly.
  Action: Add one sentence to Section 4.1 clarifying: 'The raw OpenAlex data contains 15,188 directed citation pairs (i→j with any positive citation count); after applying the threshold tau (requiring W_ij + W_ji >= tau) and converting to canonical undirected edge orientation, this reduces to 9,146 edges in the net-flow graph.' Also confirm the threshold value tau used. Expected score impact: +0.1 from eliminating a reader confusion point.
- [MINOR] (scope) The limitation of Hodge decomposition to net-flow graphs (Y_ij = W_ij - W_ji) makes it structurally blind to balanced reciprocal cartels (W_ij ≈ W_ji). The paper acknowledges this in Section 6.3. However, many real JCR citation stacking cases involve close-to-balanced mutual citation agreements between journal pairs, which produce near-zero net-flow and would be invisible to the proposed method. The 2021 Frontiers case (Frontiers in Oncology, Neuroscience, Immunology) involved coordinated cross-citation that may be more reciprocal than cyclic. The Liver Cancer/Digestive Diseases/Oncology stacking ring mentioned in Section 4.1 is also a case where tight mutual citation between a small cluster could be bilateral rather than cyclic. If real cartels are predominantly reciprocal rather than cyclic, the method addresses only a subset of real manipulation—which is not clearly communicated to readers.
  Action: In Section 6.3 (Limitations), add a quantitative estimate: for each of the 7 confirmed stacking journals, compute the reciprocity ratio (min(W_ij, W_ji) / max(W_ij, W_ji)) for their citation pairs. If the stacking journals show high reciprocity (close to 1.0), this confirms the method's blind spot is large for the actual positive class. Report this as evidence of the limitation's severity. Expected score impact: +0.2 from honest quantification of scope.
- [MINOR] (rigor) The field-aware null model (Section 3.4) uses 44 Louvain-detected communities on the same citation graph containing the known stacking journals. If 2 or more of the 7 stacking journals are co-assigned to the same Louvain community, they collectively inflate that community's expected curl (raising the null), potentially deflating their own z-scores and reducing the method's sensitivity. Conversely, if stacking journals are isolated into singleton or very small communities, the z-score could be inflated by small-sample null estimation. The paper does not report the Louvain community assignments of the stacking journals or how many communities contain multiple stacking positives.
  Action: Report: (a) the Louvain community sizes (distribution) and (b) which communities contain stacking journals (anonymized if needed). If any community contains >1 stacking journal, discuss the potential self-contamination of the null. A leave-one-out null model (excluding the focal journal from the permutation pool of its community) would be the rigorous alternative. Expected score impact: +0.2 from demonstrating awareness and robustness.
</reviewer_feedback>



<task>
IMPORTANT: Your ONLY output is the revised hypothesis text. Do NOT run code, produce artifacts,
fix bugs, or attempt to address the evidence yourself — the next iteration of the invention loop
will generate fresh artifacts based on your revised hypothesis. Reflect and rewrite; nothing else.

Do NOT generate a completely new hypothesis. Take the current hypothesis and REVISE it
to incorporate new evidence. Keep the core idea — refine, narrow, or strengthen it.

1. Does the evidence support the hypothesis? Narrow or broaden scope as needed.
2. Which claims now have strong evidence? Which are still unsupported?
3. Should the hypothesis become more specific based on what we've learned?
4. If reviewer feedback is provided, address the critiques directly.

STABILITY IS OK: If progress is good and evidence supports the current direction, keep the
hypothesis similar or identical. Only make substantive changes when evidence clearly calls for
them — e.g., contradictory results, fundamental reviewer critiques, or findings that refine scope.

You must also classify two kinds of edges in the research trace:

(A) The H↔H edge — how does this revised hypothesis relate to the previous one?
    Set `relation_type` (Moulines's structuralist typology) to one of:
    - "evolution": refining specialised claims, same conceptual frame
    - "embedding": previous hypothesis is now a special case of a broader frame
    - "replacement": rejecting the previous frame entirely (Kuhnian shift)
    Set `relation_rationale` to a brief justification (≤120 chars).

(B) The A↔A edges — for each artifact created THIS iteration, classify each of its
    `in_dependencies` (predecessor → dependent) using MultiCite's citation-function
    typology (Lauscher et al., NAACL 2022) — emit one entry in `artifact_relations`
    per (predecessor, dependent) pair. Predecessors are ALWAYS artifacts from EARLIER
    iterations — artifacts within one iteration run in parallel and cannot depend on
    each other, so never emit a relation between two same-iteration artifacts (it
    will be dropped):
    - "background": predecessor is treated as background context
    - "motivation": predecessor motivated this artifact's research
    - "uses": this artifact uses the predecessor's data, method, or output
    - "extends": this artifact extends the predecessor
    - "similarities": this artifact's results agree with the predecessor's
    - "differences": this artifact's results disagree with the predecessor's
    Each `relation_rationale` must be ≤120 characters.

Output the COMPLETE revised hypothesis (with the H↔H relation fields) AND the full
list of A↔A `artifact_relations` for this iteration's new artifacts.
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
    "ArtifactRelation": {
      "description": "One typed A\u2194A edge between a dependent artifact and one of its in_dependencies.\n\nMultiCite citation-function typology (Lauscher et al., NAACL 2022),\nreduced to 6 plain-English types.",
      "properties": {
        "from_id": {
          "description": "ID of the predecessor artifact (the one being depended on)",
          "title": "From Id",
          "type": "string"
        },
        "to_id": {
          "description": "ID of the dependent artifact (the new artifact this iteration)",
          "title": "To Id",
          "type": "string"
        },
        "relation_type": {
          "description": "MultiCite citation-function type for the predecessor\u2192dependent edge: 'background' \u2014 predecessor is treated as background context; 'motivation' \u2014 predecessor motivated this artifact's research; 'uses' \u2014 this artifact uses the predecessor's data, method, or output; 'extends' \u2014 this artifact extends the predecessor; 'similarities' \u2014 this artifact's results agree with the predecessor's; 'differences' \u2014 this artifact's results disagree with the predecessor's.",
          "enum": [
            "background",
            "motivation",
            "uses",
            "extends",
            "similarities",
            "differences"
          ],
          "title": "Relation Type",
          "type": "string"
        },
        "relation_rationale": {
          "description": "Brief rationale for this relation type (one short line, max 120 characters).",
          "maxLength": 120,
          "title": "Relation Rationale",
          "type": "string"
        }
      },
      "required": [
        "from_id",
        "to_id",
        "relation_type",
        "relation_rationale"
      ],
      "title": "ArtifactRelation",
      "type": "object"
    }
  },
  "description": "Revised hypothesis after reviewing iteration results.\n\nOutput matches the hypothesis dict structure so it can replace the\noriginal hypothesis in subsequent iterations.",
  "properties": {
    "title": {
      "description": "Revised hypothesis title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); may be unchanged if still accurate.",
      "title": "Title",
      "type": "string"
    },
    "hypothesis": {
      "description": "Revised hypothesis statement \u2014 what we now believe based on evidence",
      "title": "Hypothesis",
      "type": "string"
    },
    "relation_rationale": {
      "description": "Brief rationale for the H\u2194H revision type (one short line, max 120 characters).",
      "maxLength": 120,
      "title": "Relation Rationale",
      "type": "string"
    },
    "confidence_delta": {
      "description": "How confidence changed: 'increased', 'decreased', or 'unchanged'",
      "title": "Confidence Delta",
      "type": "string"
    },
    "key_changes": {
      "description": "Bullet list of specific changes made to the hypothesis",
      "items": {
        "type": "string"
      },
      "title": "Key Changes",
      "type": "array"
    },
    "relation_type": {
      "description": "Moulines's structuralist typology of this hypothesis revision: 'evolution' \u2014 refining specialised claims while keeping the same conceptual frame; 'embedding' \u2014 the previous hypothesis is now a special case of a broader frame; 'replacement' \u2014 rejecting the previous frame entirely (incommensurable, Kuhnian revolution).",
      "enum": [
        "evolution",
        "embedding",
        "replacement"
      ],
      "title": "Relation Type",
      "type": "string"
    },
    "artifact_relations": {
      "description": "Typed A\u2194A edges for this iteration's new artifacts. Emit one entry per (predecessor \u2192 dependent) edge for every in_dependency on each artifact produced this iteration.",
      "items": {
        "$ref": "#/$defs/ArtifactRelation"
      },
      "title": "Artifact Relations",
      "type": "array"
    }
  },
  "required": [
    "title",
    "hypothesis",
    "relation_rationale",
    "confidence_delta",
    "key_changes",
    "relation_type"
  ],
  "title": "RevisedHypothesis",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [3] HUMAN-USER prompt · 2026-07-09 01:56:16 UTC

```
Propose a simple, novel graph-based method for detecting citation patterns in academic networks and validate it.
```

### [4] ASSISTANT · 2026-07-09 01:57:27 UTC

```
I'll analyze the evidence from this iteration and write the revised hypothesis.
```

### [5] TOOL CALL — Write · 2026-07-09 01:57:27 UTC

```
File: /ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json

{
  "title": "Field-relative curl flags citation cartels",
  "hypothesis": "A citation-flow network decomposes via combinatorial Hodge theory into orthogonal gradient (prestige-consistent), curl (locally cyclic), and harmonic components. We hypothesize that coordinated citation manipulation — citation stacking and reciprocal rings — is detectable as anomalous FIELD-RELATIVE curl excess, not as absolute curl magnitude. This reframing is empirically necessary: real journal-level citation networks are curl-dominant (77% of net-flow energy in the curl component on a 231-journal OpenAlex network), not gradient-dominated as originally assumed. Raw curl magnitude is therefore non-discriminative — stacking journals do not stand out in absolute curl because the natural baseline for all journals is already high. The operative detection signal is the FIELD-AWARE Z-SCORE: each journal's triangle-curl score calibrated against the distribution expected within its research community (44 Louvain communities, 100 within-community permutations), which achieved AUC = 0.718 on 7 confirmed stacking-only positives (95% CI [0.459, 0.922]). This is a PROMISING but not yet STATISTICALLY CONFIRMED result: with only 7 positives, the bootstrap CI includes 0.459 (below chance), and a label-permutation test is required before a significance claim can be made. The gradient residual and raw curl both score below chance on real data (AUC = 0.454 and 0.430 respectively) due to a structural limitation: 3 of the 7 confirmed stacking journals are isolated nodes in the sampled network, participating in zero triangles and receiving zero curl scores by construction. The injection study further reveals limited sensitivity: in a clean 800-node synthetic base, no cartel type (cyclic or reciprocal), ring size (k in {3,4,5,10}), or injection weight (up to 2x mean edge weight) achieves AUC > 0.7; the best individual condition (cyclic k=3, w=2.0x) reaches gradient residual AUC = 0.617. This injection failure despite real-data AUC = 0.718 demands explanation: the most plausible bridge is that real stacking journals exhibit persistent, multi-year, multi-edge field-relative curl anomaly that synthetic single-injection at 2x weight does not replicate — cartel behavior accumulates repeated cycles across the full citation history rather than appearing as a point perturbation. This explanation remains to be validated empirically. The method is also structurally blind to two important classes of real manipulation: (1) perfectly balanced reciprocal exchange (W_ij ≈ W_ji produces near-zero net-flow, invisible to Hodge decomposition), which characterizes many JCR stacking cases; and (2) excessive self-citation (33 of 40 suppressed journals in our network), which is an intra-journal rather than inter-journal signal. The comparative advantage over CIDRE remains unconfirmed: the published cidre package requires matplotlib==3.1.3 (a visualization dependency not needed by the core algorithm), which prevented running full dcSBM CIDRE on Python 3.12; the spectral-clustering + Poisson fallback (AUC = 0.343) is not the published method. A proper CIDRE comparison requires running cidre in a Python 3.8/3.9 environment. The central mathematical claim — that gradient and curl components are orthogonal by construction of the Hodge decomposition — holds by theorem regardless of empirical outcomes, and the field-aware calibration is a principled analogue to the dcSBM null that CIDRE applies to citation rates. The core research contribution is therefore threefold: (1) demonstrating that real journal-citation networks are curl-dominant (77%), which means field-relative rather than absolute calibration is necessary for any Hodge-based detector; (2) providing the first Hodge-decomposition citation cartel detector validated against real JCR suppression labels, with AUC = 0.718 as a preliminary point estimate pending significance testing; and (3) mapping the method's scope boundaries — it is designed for inter-journal cyclic exchange (stacking cartels) and is not applicable to self-citation or balanced bilateral exchange.",
  "relation_rationale": "Same Hodge frame; elevates field-aware z-score as the operative detector; demotes AUC=0.718 from 'confirmed' to 'promising pending permutation test'; acknowledges injection-real-data gap.",
  "confidence_delta": "decreased",
  "key_changes": [
    "Fundamentally revises the founding assumption: real journal-level citation networks are curl-DOMINANT (77% curl energy), not gradient-dominant; raw curl is therefore non-discriminative and field-relative calibration is necessary, not optional.",
    "Elevates the FIELD-AWARE Z-SCORE (AUC=0.718) as the primary operational detector, replacing the gradient residual which performs below chance on real data (AUC=0.454).",
    "Explicitly downgrades the AUC=0.718 result from 'confirmed detection' to 'promising preliminary evidence': bootstrap CI [0.459, 0.922] includes values below chance; permutation test with 10,000 label permutations is required before a significance claim is valid.",
    "Explains the raw Hodge failure mechanism: 3 of 7 stacking journals are isolated nodes in the sampled network, receiving zero curl scores by construction; the method requires triangular connectivity to produce nonzero scores.",
    "Documents the injection-vs-real-data gap as an unresolved tension requiring explanation: synthetic injection best AUC=0.617 vs. real-data AUC=0.718; proposes the 'persistent multi-year accumulation' hypothesis as the bridge but marks it as unvalidated.",
    "Flags the CIDRE comparison as methodologically incomplete: cidre Python 3.12 incompatibility is a matplotlib visualization dependency only; the core dcSBM algorithm can run in Python 3.8/3.9 without code changes; the fallback (AUC=0.343) is not the published method.",
    "Explicitly scopes out balanced reciprocal exchange (W_ij ≈ W_ji → near-zero net-flow, invisible to Hodge) and excessive self-citation (33 of 40 suppressed journals) as structural blind spots of the current method.",
    "Notes that the 77% curl fraction in the real network may be partially inflated by the 40 suppressed journals within it; computing curl decomposition on the 191 clean journals only is required to validate the 'natural curl dominance' claim.",
    "Retains the mathematical orthogonality claim (gradient and curl are orthogonal by construction) as a theorem-level guarantee, while treating the practical advantage over density-based methods as an empirical hypothesis still requiring proper CIDRE comparison."
  ],
  "relation_type": "evolution",
  "artifact_relations": [
    {
      "from_id": "art_Md6TNdV-FZYE",
      "to_id": "art_gkqGp1-55dg1",
      "relation_type": "extends",
      "relation_rationale": "Extends prior research specs with HLSAD positioning paragraph and corrected JCR stacking annotations (4 not 3 in 2021; 2020=0 stacking)."
    },
    {
      "from_id": "art_IGeLtKiwHWQE",
      "to_id": "art_XbmaHSRFGigA",
      "relation_type": "uses",
      "relation_rationale": "Uses the 231-journal citation network and JCR suppression labels as the primary real-data evaluation set."
    },
    {
      "from_id": "art_Md6TNdV-FZYE",
      "to_id": "art_XbmaHSRFGigA",
      "relation_type": "uses",
      "relation_rationale": "Uses Hodge decomposition methodology specs (boundary operators, lsqr solver, CIDRE API, CDFD) to implement the 6-phase evaluation."
    }
  ]
}
```

### [6] TOOL RESULT — Write · 2026-07-09 01:57:27 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Field-relative curl flags citation cartels\",\n  \"hypothesis\": \"A citation-flow network decomposes via combinatorial Hodge theory into orthogonal gradient (prestige-consistent), curl (locally cyclic), and harmonic components. We hypothesize that coordinated citation manipulation — citation stacking and reciprocal rings — is detectable as anomalous FIELD-RELATIVE curl excess, not as absolute curl magnitude. This reframing is empirically necessary: real journal-level citation networks are curl-dominant (77% of net-flow energy in the curl component on a 231-journal OpenAlex network), not gradient-dominated as originally assumed. Raw curl magnitude is therefore non-discriminative — stacking journals do not stand out in absolute curl because the natural baseline for all journals is already high. The operative detection signal is the FIELD-AWARE Z-SCORE: each journal's triangle-curl score calibrated against the distribution expected within its research community (44 Louvain communities, 100 within-community permutations), which achieved AUC = 0.718 on 7 confirmed stacking-only positives (95% CI [0.459, 0.922]). This is a PROMISING but not yet STATISTICALLY CONFIRMED result: with only 7 positives, the bootstrap CI includes 0.459 (below chance), and a label-permutation test is required before a significance claim can be made. The gradient residual and raw curl both score below chance on real data (AUC = 0.454 and 0.430 respectively) due to a structural limitation: 3 of the 7 confirmed stacking journals are isolated nodes in the sampled network, participating in zero triangles and receiving zero curl scores by construction. The injection study further reveals limited sensitivity: in a clean 800-node synthetic base, no cartel type (cyclic or reciprocal), ring size (k in {3,4,5,10}), or injection weight (up to 2x mean edge weight) achieves AUC > 0.7; the best individual condition (cyclic k=3, w=2.0x) reaches gradient residual AUC = 0.617. This injection failure despite real-data AUC = 0.718 demands explanation: the most plausible bridge is that real stacking journals exhibit persistent, multi-year, multi-edge field-relative curl anomaly that synthetic single-injection at 2x weight does not replicate — cartel behavior accumulates repeated cycles across the full citation history rather than appearing as a point perturbation. This explanation remains to be validated empirically. The method is also structurally blind to two important classes of real manipulation: (1) perfectly balanced reciprocal exchange (W_ij ≈ W_ji produces near-zero net-flow, invisible to Hodge decomposition), which characterizes many JCR stacking cases; and (2) excessive self-citation (33 of 40 suppressed journals in our network), which is an intra-journal rather than inter-journal signal. The comparative advantage over CIDRE remains unconfirmed: the published cidre package requires matplotlib==3.1.3 (a visualization dependency not needed by the core algorithm), which prevented running full dcSBM CIDRE on Python 3.12; the spectral-clustering + Poisson fallback (AUC = 0.343) is not the published method. A proper CIDRE comparison requires running cidre in a Python 3.8/3.9 environment. The central mathematical claim — that gradient and curl components are orthogonal by construction of the Hodge decomposition — holds by theorem regardless of empirical outcomes, and the field-aware calibration is a principled analogue to the dcSBM null that CIDRE applies to citation rates. The core research contribution is therefore threefold: (1) demonstrating that real journal-citation networks are curl-dominant (77%), which means field-relative rather than absolute calibration is necessary for any Hodge-based detector; (2) providing the first Hodge-decomposition citation cartel detector validated against real JCR suppression labels, with AUC = 0.718 as a preliminary point estimate pending significance testing; and (3) mapping the method's scope boundaries — it is designed for inter-journal cyclic exchange (stacking cartels) and is not applicable to self-citation or balanced bilateral exchange.\",\n  \"relation_rationale\": \"Same Hodge frame; elevates field-aware z-score as the operative detector; demotes AUC=0.718 from 'confirmed' to 'promising pending permutation test'; acknowledges injection-real-data gap.\",\n  \"confidence_delta\": \"decreased\",\n  \"key_changes\": [\n    \"Fundamentally revises the founding assumption: real journal-level citation networks are curl-DOMINANT (77% curl energy), not gradient-dominant; raw curl is therefore non-discriminative and field-relative calibration is necessary, not optional.\",\n    \"Elevates the FIELD-AWARE Z-SCORE (AUC=0.718) as the primary operational detector, replacing the gradient residual which performs below chance on real data (AUC=0.454).\",\n    \"Explicitly downgrades the AUC=0.718 result from 'confirmed detection' to 'promising preliminary evidence': bootstrap CI [0.459, 0.922] includes values below chance; permutation test with 10,000 label permutations is required before a significance claim is valid.\",\n    \"Explains the raw Hodge failure mechanism: 3 of 7 stacking journals are isolated nodes in the sampled network, receiving zero curl scores by construction; the method requires triangular connectivity to produce nonzero scores.\",\n    \"Documents the injection-vs-real-data gap as an unresolved tension requiring explanation: synthetic injection best AUC=0.617 vs. real-data AUC=0.718; proposes the 'persistent multi-year accumulation' hypothesis as the bridge but marks it as unvalidated.\",\n    \"Flags the CIDRE comparison as methodologically incomplete: cidre Python 3.12 incompatibility is a matplotlib visualization dependency only; the core dcSBM algorithm can run in Python 3.8/3.9 without code changes; the fallback (AUC=0.343) is not the published method.\",\n    \"Explicitly scopes out balanced reciprocal exchange (W_ij ≈ W_ji → near-zero net-flow, invisible to Hodge) and excessive self-citation (33 of 40 suppressed journals) as structural blind spots of the current method.\",\n    \"Notes that the 77% curl fraction in the real network may be partially inflated by the 40 suppressed journals within it; computing curl decomposition on the 191 clean journals only is required to validate the 'natural curl dominance' claim.\",\n    \"Retains the mathematical orthogonality claim (gradient and curl are orthogonal by construction) as a theorem-level guarantee, while treating the practical advantage over density-based methods as an empirical hypothesis still requiring proper CIDRE comparison.\"\n  ],\n  \"relation_type\": \"evolution\",\n  \"artifact_relations\": [\n    {\n      \"from_id\": \"art_Md6TNdV-FZYE\",\n      \"to_id\": \"art_gkqGp1-55dg1\",\n      \"relation_type\": \"extends\",\n      \"relation_rationale\": \"Extends prior research specs with HLSAD positioning paragraph and corrected JCR stacking annotations (4 not 3 in 2021; 2020=0 stacking).\"\n    },\n    {\n      \"from_id\": \"art_IGeLtKiwHWQE\",\n      \"to_id\": \"art_XbmaHSRFGigA\",\n      \"relation_type\": \"uses\",\n      \"relation_rationale\": \"Uses the 231-journal citation network and JCR suppression labels as the primary real-data evaluation set.\"\n    },\n    {\n      \"from_id\": \"art_Md6TNdV-FZYE\",\n      \"to_id\": \"art_XbmaHSRFGigA\",\n      \"relation_type\": \"uses\",\n      \"relation_rationale\": \"Uses Hodge decomposition methodology specs (boundary operators, lsqr solver, CIDRE API, CDFD) to implement the 6-phase evaluation.\"\n    }\n  ]\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [7] ASSISTANT · 2026-07-09 01:57:36 UTC

```
The revised hypothesis has been written to `.terminal_claude_agent_struct_out.json`.

**Key revision summary:** The hypothesis shifts from "curl detects cartels" to "field-relative curl excess detects cartels," driven by three critical empirical findings from this iteration:

1. **Founding assumption falsified**: Real citation networks are 77% curl-dominant — raw curl magnitude is non-discriminative because the natural baseline is already high for all journals.

2. **AUC=0.718 downgraded to provisional**: With only 7 positives, the CI [0.459, 0.922] straddles chance; a permutation test is needed before claiming significance. The field-aware z-score is now the primary operative detector.

3. **CIDRE comparison invalidated**: The `cidre` package incompatibility is a matplotlib-only dependency — full dcSBM CIDRE must be run in Python 3.8/3.9. The fallback baseline (AUC=0.343) is not the published method, so comparative advantage claims remain unconfirmed.

The mathematical orthogonality guarantee (Hodge theorem) is retained, but empirical superiority over density-based methods is now explicitly provisional pending a proper CIDRE baseline and a permutation significance test on the 7-positive real dataset.
```

### [8] SYSTEM-USER prompt · 2026-07-09 01:57:38 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 3 problems — fix ALL of them at once:
  - at `artifact_relations.0.relation_rationale`: 'Extends prior research specs with HLSAD positioning paragraph and corrected JCR stacking annotations (4 not 3 in 2021; 2020=0 stacking).' is too long (at most 120 characters, got 136)
  - at `artifact_relations.2.relation_rationale`: 'Uses Hodge decomposition methodology specs (boundary operators, lsqr solver, CIDRE API, CDFD) to implement the 6-phase evaluation.' is too long (at most 120 characters, got 130)
  - at `relation_rationale`: "Same Hodge frame; elevates field-aware z-score as the operative detector; demotes AUC=0.718 from 'confirmed' to 'promising pending permutation test'; acknowledges injection-real-data gap." is too long (at most 120 characters, got 187)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

### [9] TOOL CALL — Edit · 2026-07-09 01:57:42 UTC

```
File: /ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json
OLD:   "relation_rationale": "Same Hodge frame; elevates field-aware z-score as the operative detector; demotes AUC=0.718 from 'confirmed' to 'promising pending permutation test'; acknowledges injection-real-data gap.",
NEW:   "relation_rationale": "Same Hodge frame; field-aware z-score replaces raw curl; AUC=0.718 demoted to provisional pending permutation test.",
```

### [10] TOOL RESULT — Edit · 2026-07-09 01:57:42 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json", "oldString": "  \"relation_rationale\": \"Same Hodge frame; elevates field-aware z-score as the operative detector; demotes AUC=0.718 from 'confirmed' to 'promising pending permutation test'; acknowledges injection-real-data gap.\",", "newString": "  \"relation_rationale\": \"Same Hodge frame; field-aware z-score replaces raw curl; AUC=0.718 demoted to provisional pending permutation test.\",", "originalFile": "{\n  \"title\": \"Field-relative curl flags citation cartels\",\n  \"hypothesis\": \"A citation-flow network decomposes via combinatorial Hodge theory into orthogonal gradient (prestige-consistent), curl (locally cyclic), and harmonic components. We hypothesize that coordinated citation manipulation — citation stacking and reciprocal rings — is detectable as anomalous FIELD-RELATIVE curl excess, not as absolute curl magnitude. This reframing is empirically necessary: real journal-level citation networks are curl-dominant (77% of net-flow energy in the curl component on a 231-journal OpenAlex network), not gradient-dominated as originally assumed. Raw curl magnitude is therefore non-discriminative — stacking journals do not stand out in absolute curl because the natural baseline for all journals is already high. The operative detection signal is the FIELD-AWARE Z-SCORE: each journal's triangle-curl score calibrated against the distribution expected within its research community (44 Louvain communities, 100 within-community permutations), which achieved AUC = 0.718 on 7 confirmed stacking-only positives (95% CI [0.459, 0.922]). This is a PROMISING but not yet STATISTICALLY CONFIRMED result: with only 7 positives, the bootstrap CI includes 0.459 (below chance), and a label-permutation test is required before a significance claim can be made. The gradient residual and raw curl both score below chance on real data (AUC = 0.454 and 0.430 respectively) due to a structural limitation: 3 of the 7 confirmed stacking journals are isolated nodes in the sampled network, participating in zero triangles and receiving zero curl scores by construction. The injection study further reveals limited sensitivity: in a clean 800-node synthetic base, no cartel type (cyclic or reciprocal), ring size (k in {3,4,5,10}), or injection weight (up to 2x mean edge weight) achieves AUC > 0.7; the best individual condition (cyclic k=3, w=2.0x) reaches gradient residual AUC = 0.617. This injection failure despite real-data AUC = 0.718 demands explanation: the most plausible bridge is that real stacking journals exhibit persistent, multi-year, multi-edge field-relative curl anomaly that synthetic single-injection at 2x weight does not replicate — cartel behavior accumulates repeated cycles across the full citation history rather than appearing as a point perturbation. This explanation remains to be validated empirically. The method is also structurally blind to two important classes of real manipulation: (1) perfectly balanced reciprocal exchange (W_ij ≈ W_ji produces near-zero net-flow, invisible to Hodge decomposition), which characterizes many JCR stacking cases; and (2) excessive self-citation (33 of 40 suppressed journals in our network), which is an intra-journal rather than inter-journal signal. The comparative advantage over CIDRE remains unconfirmed: the published cidre package requires matplotlib==3.1.3 (a visualization dependency not needed by the core algorithm), which prevented running full dcSBM CIDRE on Python 3.12; the spectral-clustering + Poisson fallback (AUC = 0.343) is not the published method. A proper CIDRE comparison requires running cidre in a Python 3.8/3.9 environment. The central mathematical claim — that gradient and curl components are orthogonal by construction of the Hodge decomposition — holds by theorem regardless of empirical outcomes, and the field-aware calibration is a principled analogue to the dcSBM null that CIDRE applies to citation rates. The core research contribution is therefore threefold: (1) demonstrating that real journal-citation networks are curl-dominant (77%), which means field-relative rather than absolute calibration is necessary for any Hodge-based detector; (2) providing the first Hodge-decomposition citation cartel detector validated against real JCR suppression labels, with AUC = 0.718 as a preliminary point estimate pending significance testing; and (3) mapping the method's scope boundaries — it is designed for inter-journal cyclic exchange (stacking cartels) and is not applicable to self-citation or balanced bilateral exchange.\",\n  \"relation_rationale\": \"Same Hodge frame; elevates field-aware z-score as the operative detector; demotes AUC=0.718 from 'confirmed' to 'promising pending permutation test'; acknowledges injection-real-data gap.\",\n  \"confidence_delta\": \"decreased\",\n  \"key_changes\": [\n    \"Fundamentally revises the founding assumption: real journal-level citation networks are curl-DOMINANT (77% curl energy), not gradient-dominant; raw curl is therefore non-discriminative and field-relative calibration is necessary, not optional.\",\n    \"Elevates the FIELD-AWARE Z-SCORE (AUC=0.718) as the primary operational detector, replacing the gradient residual which performs below chance on real data (AUC=0.454).\",\n    \"Explicitly downgrades the AUC=0.718 result from 'confirmed detection' to 'promising preliminary evidence': bootstrap CI [0.459, 0.922] includes values below chance; permutation test with 10,000 label permutations is required before a significance claim is valid.\",\n    \"Explains the raw Hodge failure mechanism: 3 of 7 stacking journals are isolated nodes in the sampled network, receiving zero curl scores by construction; the method requires triangular connectivity to produce nonzero scores.\",\n    \"Documents the injection-vs-real-data gap as an unresolved tension requiring explanation: synthetic injection best AUC=0.617 vs. real-data AUC=0.718; proposes the 'persistent multi-year accumulation' hypothesis as the bridge but marks it as unvalidated.\",\n    \"Flags the CIDRE comparison as methodologically incomplete: cidre Python 3.12 incompatibility is a matplotlib visualization dependency only; the core dcSBM algorithm can run in Python 3.8/3.9 without code changes; the fallback (AUC=0.343) is not the published method.\",\n    \"Explicitly scopes out balanced reciprocal exchange (W_ij ≈ W_ji → near-zero net-flow, invisible to Hodge) and excessive self-citation (33 of 40 suppressed journals) as structural blind spots of the current method.\",\n    \"Notes that the 77% curl fraction in the real network may be partially inflated by the 40 suppressed journals within it; computing curl decomposition on the 191 clean journals only is required to validate the 'natural curl dominance' claim.\",\n    \"Retains the mathematical orthogonality claim (gradient and curl are orthogonal by construction) as a theorem-level guarantee, while treating the practical advantage over density-based methods as an empirical hypothesis still requiring proper CIDRE comparison.\"\n  ],\n  \"relation_type\": \"evolution\",\n  \"artifact_relations\": [\n    {\n      \"from_id\": \"art_Md6TNdV-FZYE\",\n      \"to_id\": \"art_gkqGp1-55dg1\",\n      \"relation_type\": \"extends\",\n      \"relation_rationale\": \"Extends prior research specs with HLSAD positioning paragraph and corrected JCR stacking annotations (4 not 3 in 2021; 2020=0 stacking).\"\n    },\n    {\n      \"from_id\": \"art_IGeLtKiwHWQE\",\n      \"to_id\": \"art_XbmaHSRFGigA\",\n      \"relation_type\": \"uses\",\n      \"relation_rationale\": \"Uses the 231-journal citation network and JCR suppression labels as the primary real-data evaluation set.\"\n    },\n    {\n      \"from_id\": \"art_Md6TNdV-FZYE\",\n      \"to_id\": \"art_XbmaHSRFGigA\",\n      \"relation_type\": \"uses\",\n      \"relation_rationale\": \"Uses Hodge decomposition methodology specs (boundary operators, lsqr solver, CIDRE API, CDFD) to implement the 6-phase evaluation.\"\n    }\n  ]\n}\n", "structuredPatch": [{"oldStart": 1, "oldLines": 7, "newStart": 1, "newLines": 7, "lines": [" {", "   \"title\": \"Field-relative curl flags citation cartels\",", "   \"hypothesis\": \"A citation-flow network decomposes via combinatorial Hodge theory into orthogonal gradient (prestige-consistent), curl (locally cyclic), and harmonic components. We hypothesize that coordinated citation manipulation — citation stacking and reciprocal rings — is detectable as anomalous FIELD-RELATIVE curl excess, not as absolute curl magnitude. This reframing is empirically necessary: real journal-level citation networks are curl-dominant (77% of net-flow energy in the curl component on a 231-journal OpenAlex network), not gradient-dominated as originally assumed. Raw curl magnitude is therefore non-discriminative — stacking journals do not stand out in absolute curl because the natural baseline for all journals is already high. The operative detection signal is the FIELD-AWARE Z-SCORE: each journal's triangle-curl score calibrated against the distribution expected within its research community (44 Louvain communities, 100 within-community permutations), which achieved AUC = 0.718 on 7 confirmed stacking-only positives (95% CI [0.459, 0.922]). This is a PROMISING but not yet STATISTICALLY CONFIRMED result: with only 7 positives, the bootstrap CI includes 0.459 (below chance), and a label-permutation test is required before a significance claim can be made. The gradient residual and raw curl both score below chance on real data (AUC = 0.454 and 0.430 respectively) due to a structural limitation: 3 of the 7 confirmed stacking journals are isolated nodes in the sampled network, participating in zero triangles and receiving zero curl scores by construction. The injection study further reveals limited sensitivity: in a clean 800-node synthetic base, no cartel type (cyclic or reciprocal), ring size (k in {3,4,5,10}), or injection weight (up to 2x mean edge weight) achieves AUC > 0.7; the best individual condition (cyclic k=3, w=2.0x) reaches gradient residual AUC = 0.617. This injection failure despite real-data AUC = 0.718 demands explanation: the most plausible bridge is that real stacking journals exhibit persistent, multi-year, multi-edge field-relative curl anomaly that synthetic single-injection at 2x weight does not replicate — cartel behavior accumulates repeated cycles across the full citation history rather than appearing as a point perturbation. This explanation remains to be validated empirically. The method is also structurally blind to two important classes of real manipulation: (1) perfectly balanced reciprocal exchange (W_ij ≈ W_ji produces near-zero net-flow, invisible to Hodge decomposition), which characterizes many JCR stacking cases; and (2) excessive self-citation (33 of 40 suppressed journals in our network), which is an intra-journal rather than inter-journal signal. The comparative advantage over CIDRE remains unconfirmed: the published cidre package requires matplotlib==3.1.3 (a visualization dependency not needed by the core algorithm), which prevented running full dcSBM CIDRE on Python 3.12; the spectral-clustering + Poisson fallback (AUC = 0.343) is not the published method. A proper CIDRE comparison requires running cidre in a Python 3.8/3.9 environment. The central mathematical claim — that gradient and curl components are orthogonal by construction of the Hodge decomposition — holds by theorem regardless of empirical outcomes, and the field-aware calibration is a principled analogue to the dcSBM null that CIDRE applies to citation rates. The core research contribution is therefore threefold: (1) demonstrating that real journal-citation networks are curl-dominant (77%), which means field-relative rather than absolute calibration is necessary for any Hodge-based detector; (2) providing the first Hodge-decomposition citation cartel detector validated against real JCR suppression labels, with AUC = 0.718 as a preliminary point estimate pending significance testing; and (3) mapping the method's scope boundaries — it is designed for inter-journal cyclic exchange (stacking cartels) and is not applicable to self-citation or balanced bilateral exchange.\",", "-  \"relation_rationale\": \"Same Hodge frame; elevates field-aware z-score as the operative detector; demotes AUC=0.718 from 'confirmed' to 'promising pending permutation test'; acknowledges injection-real-data gap.\",", "+  \"relation_rationale\": \"Same Hodge frame; field-aware z-score replaces raw curl; AUC=0.718 demoted to provisional pending permutation test.\",", "   \"confidence_delta\": \"decreased\",", "   \"key_changes\": [", "     \"Fundamentally revises the founding assumption: real journal-level citation networks are curl-DOMINANT (77% curl energy), not gradient-dominant; raw curl is therefore non-discriminative and field-relative calibration is necessary, not optional.\","]}], "userModified": false, "replaceAll": false}
```

### [11] TOOL CALL — Edit · 2026-07-09 01:57:46 UTC

```
File: /ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json
OLD:       "relation_rationale": "Extends prior research specs with HLSAD positioning paragraph and corrected JCR stacking annotations (4 not 3 in 2021; 2020=0 stacking)."
NEW:       "relation_rationale": "Extends specs with HLSAD positioning and corrected JCR stacking annotations (4 in 2021; 2020=0 stacking)."
```

### [12] TOOL RESULT — Edit · 2026-07-09 01:57:46 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json", "oldString": "      \"relation_rationale\": \"Extends prior research specs with HLSAD positioning paragraph and corrected JCR stacking annotations (4 not 3 in 2021; 2020=0 stacking).\"", "newString": "      \"relation_rationale\": \"Extends specs with HLSAD positioning and corrected JCR stacking annotations (4 in 2021; 2020=0 stacking).\"", "originalFile": "{\n  \"title\": \"Field-relative curl flags citation cartels\",\n  \"hypothesis\": \"A citation-flow network decomposes via combinatorial Hodge theory into orthogonal gradient (prestige-consistent), curl (locally cyclic), and harmonic components. We hypothesize that coordinated citation manipulation — citation stacking and reciprocal rings — is detectable as anomalous FIELD-RELATIVE curl excess, not as absolute curl magnitude. This reframing is empirically necessary: real journal-level citation networks are curl-dominant (77% of net-flow energy in the curl component on a 231-journal OpenAlex network), not gradient-dominated as originally assumed. Raw curl magnitude is therefore non-discriminative — stacking journals do not stand out in absolute curl because the natural baseline for all journals is already high. The operative detection signal is the FIELD-AWARE Z-SCORE: each journal's triangle-curl score calibrated against the distribution expected within its research community (44 Louvain communities, 100 within-community permutations), which achieved AUC = 0.718 on 7 confirmed stacking-only positives (95% CI [0.459, 0.922]). This is a PROMISING but not yet STATISTICALLY CONFIRMED result: with only 7 positives, the bootstrap CI includes 0.459 (below chance), and a label-permutation test is required before a significance claim can be made. The gradient residual and raw curl both score below chance on real data (AUC = 0.454 and 0.430 respectively) due to a structural limitation: 3 of the 7 confirmed stacking journals are isolated nodes in the sampled network, participating in zero triangles and receiving zero curl scores by construction. The injection study further reveals limited sensitivity: in a clean 800-node synthetic base, no cartel type (cyclic or reciprocal), ring size (k in {3,4,5,10}), or injection weight (up to 2x mean edge weight) achieves AUC > 0.7; the best individual condition (cyclic k=3, w=2.0x) reaches gradient residual AUC = 0.617. This injection failure despite real-data AUC = 0.718 demands explanation: the most plausible bridge is that real stacking journals exhibit persistent, multi-year, multi-edge field-relative curl anomaly that synthetic single-injection at 2x weight does not replicate — cartel behavior accumulates repeated cycles across the full citation history rather than appearing as a point perturbation. This explanation remains to be validated empirically. The method is also structurally blind to two important classes of real manipulation: (1) perfectly balanced reciprocal exchange (W_ij ≈ W_ji produces near-zero net-flow, invisible to Hodge decomposition), which characterizes many JCR stacking cases; and (2) excessive self-citation (33 of 40 suppressed journals in our network), which is an intra-journal rather than inter-journal signal. The comparative advantage over CIDRE remains unconfirmed: the published cidre package requires matplotlib==3.1.3 (a visualization dependency not needed by the core algorithm), which prevented running full dcSBM CIDRE on Python 3.12; the spectral-clustering + Poisson fallback (AUC = 0.343) is not the published method. A proper CIDRE comparison requires running cidre in a Python 3.8/3.9 environment. The central mathematical claim — that gradient and curl components are orthogonal by construction of the Hodge decomposition — holds by theorem regardless of empirical outcomes, and the field-aware calibration is a principled analogue to the dcSBM null that CIDRE applies to citation rates. The core research contribution is therefore threefold: (1) demonstrating that real journal-citation networks are curl-dominant (77%), which means field-relative rather than absolute calibration is necessary for any Hodge-based detector; (2) providing the first Hodge-decomposition citation cartel detector validated against real JCR suppression labels, with AUC = 0.718 as a preliminary point estimate pending significance testing; and (3) mapping the method's scope boundaries — it is designed for inter-journal cyclic exchange (stacking cartels) and is not applicable to self-citation or balanced bilateral exchange.\",\n  \"relation_rationale\": \"Same Hodge frame; field-aware z-score replaces raw curl; AUC=0.718 demoted to provisional pending permutation test.\",\n  \"confidence_delta\": \"decreased\",\n  \"key_changes\": [\n    \"Fundamentally revises the founding assumption: real journal-level citation networks are curl-DOMINANT (77% curl energy), not gradient-dominant; raw curl is therefore non-discriminative and field-relative calibration is necessary, not optional.\",\n    \"Elevates the FIELD-AWARE Z-SCORE (AUC=0.718) as the primary operational detector, replacing the gradient residual which performs below chance on real data (AUC=0.454).\",\n    \"Explicitly downgrades the AUC=0.718 result from 'confirmed detection' to 'promising preliminary evidence': bootstrap CI [0.459, 0.922] includes values below chance; permutation test with 10,000 label permutations is required before a significance claim is valid.\",\n    \"Explains the raw Hodge failure mechanism: 3 of 7 stacking journals are isolated nodes in the sampled network, receiving zero curl scores by construction; the method requires triangular connectivity to produce nonzero scores.\",\n    \"Documents the injection-vs-real-data gap as an unresolved tension requiring explanation: synthetic injection best AUC=0.617 vs. real-data AUC=0.718; proposes the 'persistent multi-year accumulation' hypothesis as the bridge but marks it as unvalidated.\",\n    \"Flags the CIDRE comparison as methodologically incomplete: cidre Python 3.12 incompatibility is a matplotlib visualization dependency only; the core dcSBM algorithm can run in Python 3.8/3.9 without code changes; the fallback (AUC=0.343) is not the published method.\",\n    \"Explicitly scopes out balanced reciprocal exchange (W_ij ≈ W_ji → near-zero net-flow, invisible to Hodge) and excessive self-citation (33 of 40 suppressed journals) as structural blind spots of the current method.\",\n    \"Notes that the 77% curl fraction in the real network may be partially inflated by the 40 suppressed journals within it; computing curl decomposition on the 191 clean journals only is required to validate the 'natural curl dominance' claim.\",\n    \"Retains the mathematical orthogonality claim (gradient and curl are orthogonal by construction) as a theorem-level guarantee, while treating the practical advantage over density-based methods as an empirical hypothesis still requiring proper CIDRE comparison.\"\n  ],\n  \"relation_type\": \"evolution\",\n  \"artifact_relations\": [\n    {\n      \"from_id\": \"art_Md6TNdV-FZYE\",\n      \"to_id\": \"art_gkqGp1-55dg1\",\n      \"relation_type\": \"extends\",\n      \"relation_rationale\": \"Extends prior research specs with HLSAD positioning paragraph and corrected JCR stacking annotations (4 not 3 in 2021; 2020=0 stacking).\"\n    },\n    {\n      \"from_id\": \"art_IGeLtKiwHWQE\",\n      \"to_id\": \"art_XbmaHSRFGigA\",\n      \"relation_type\": \"uses\",\n      \"relation_rationale\": \"Uses the 231-journal citation network and JCR suppression labels as the primary real-data evaluation set.\"\n    },\n    {\n      \"from_id\": \"art_Md6TNdV-FZYE\",\n      \"to_id\": \"art_XbmaHSRFGigA\",\n      \"relation_type\": \"uses\",\n      \"relation_rationale\": \"Uses Hodge decomposition methodology specs (boundary operators, lsqr solver, CIDRE API, CDFD) to implement the 6-phase evaluation.\"\n    }\n  ]\n}\n", "structuredPatch": [{"oldStart": 20, "oldLines": 7, "newStart": 20, "newLines": 7, "lines": ["       \"from_id\": \"art_Md6TNdV-FZYE\",", "       \"to_id\": \"art_gkqGp1-55dg1\",", "       \"relation_type\": \"extends\",", "-      \"relation_rationale\": \"Extends prior research specs with HLSAD positioning paragraph and corrected JCR stacking annotations (4 not 3 in 2021; 2020=0 stacking).\"", "+      \"relation_rationale\": \"Extends specs with HLSAD positioning and corrected JCR stacking annotations (4 in 2021; 2020=0 stacking).\"", "     },", "     {", "       \"from_id\": \"art_IGeLtKiwHWQE\","]}], "userModified": false, "replaceAll": false}
```

### [13] TOOL CALL — Edit · 2026-07-09 01:57:50 UTC

```
File: /ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json
OLD:       "relation_rationale": "Uses Hodge decomposition methodology specs (boundary operators, lsqr solver, CIDRE API, CDFD) to implement the 6-phase evaluation."
NEW:       "relation_rationale": "Uses Hodge methodology specs (boundary operators, lsqr, CIDRE, CDFD) to implement the 6-phase evaluation."
```

### [14] TOOL RESULT — Edit · 2026-07-09 01:57:50 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json", "oldString": "      \"relation_rationale\": \"Uses Hodge decomposition methodology specs (boundary operators, lsqr solver, CIDRE API, CDFD) to implement the 6-phase evaluation.\"", "newString": "      \"relation_rationale\": \"Uses Hodge methodology specs (boundary operators, lsqr, CIDRE, CDFD) to implement the 6-phase evaluation.\"", "originalFile": "{\n  \"title\": \"Field-relative curl flags citation cartels\",\n  \"hypothesis\": \"A citation-flow network decomposes via combinatorial Hodge theory into orthogonal gradient (prestige-consistent), curl (locally cyclic), and harmonic components. We hypothesize that coordinated citation manipulation — citation stacking and reciprocal rings — is detectable as anomalous FIELD-RELATIVE curl excess, not as absolute curl magnitude. This reframing is empirically necessary: real journal-level citation networks are curl-dominant (77% of net-flow energy in the curl component on a 231-journal OpenAlex network), not gradient-dominated as originally assumed. Raw curl magnitude is therefore non-discriminative — stacking journals do not stand out in absolute curl because the natural baseline for all journals is already high. The operative detection signal is the FIELD-AWARE Z-SCORE: each journal's triangle-curl score calibrated against the distribution expected within its research community (44 Louvain communities, 100 within-community permutations), which achieved AUC = 0.718 on 7 confirmed stacking-only positives (95% CI [0.459, 0.922]). This is a PROMISING but not yet STATISTICALLY CONFIRMED result: with only 7 positives, the bootstrap CI includes 0.459 (below chance), and a label-permutation test is required before a significance claim can be made. The gradient residual and raw curl both score below chance on real data (AUC = 0.454 and 0.430 respectively) due to a structural limitation: 3 of the 7 confirmed stacking journals are isolated nodes in the sampled network, participating in zero triangles and receiving zero curl scores by construction. The injection study further reveals limited sensitivity: in a clean 800-node synthetic base, no cartel type (cyclic or reciprocal), ring size (k in {3,4,5,10}), or injection weight (up to 2x mean edge weight) achieves AUC > 0.7; the best individual condition (cyclic k=3, w=2.0x) reaches gradient residual AUC = 0.617. This injection failure despite real-data AUC = 0.718 demands explanation: the most plausible bridge is that real stacking journals exhibit persistent, multi-year, multi-edge field-relative curl anomaly that synthetic single-injection at 2x weight does not replicate — cartel behavior accumulates repeated cycles across the full citation history rather than appearing as a point perturbation. This explanation remains to be validated empirically. The method is also structurally blind to two important classes of real manipulation: (1) perfectly balanced reciprocal exchange (W_ij ≈ W_ji produces near-zero net-flow, invisible to Hodge decomposition), which characterizes many JCR stacking cases; and (2) excessive self-citation (33 of 40 suppressed journals in our network), which is an intra-journal rather than inter-journal signal. The comparative advantage over CIDRE remains unconfirmed: the published cidre package requires matplotlib==3.1.3 (a visualization dependency not needed by the core algorithm), which prevented running full dcSBM CIDRE on Python 3.12; the spectral-clustering + Poisson fallback (AUC = 0.343) is not the published method. A proper CIDRE comparison requires running cidre in a Python 3.8/3.9 environment. The central mathematical claim — that gradient and curl components are orthogonal by construction of the Hodge decomposition — holds by theorem regardless of empirical outcomes, and the field-aware calibration is a principled analogue to the dcSBM null that CIDRE applies to citation rates. The core research contribution is therefore threefold: (1) demonstrating that real journal-citation networks are curl-dominant (77%), which means field-relative rather than absolute calibration is necessary for any Hodge-based detector; (2) providing the first Hodge-decomposition citation cartel detector validated against real JCR suppression labels, with AUC = 0.718 as a preliminary point estimate pending significance testing; and (3) mapping the method's scope boundaries — it is designed for inter-journal cyclic exchange (stacking cartels) and is not applicable to self-citation or balanced bilateral exchange.\",\n  \"relation_rationale\": \"Same Hodge frame; field-aware z-score replaces raw curl; AUC=0.718 demoted to provisional pending permutation test.\",\n  \"confidence_delta\": \"decreased\",\n  \"key_changes\": [\n    \"Fundamentally revises the founding assumption: real journal-level citation networks are curl-DOMINANT (77% curl energy), not gradient-dominant; raw curl is therefore non-discriminative and field-relative calibration is necessary, not optional.\",\n    \"Elevates the FIELD-AWARE Z-SCORE (AUC=0.718) as the primary operational detector, replacing the gradient residual which performs below chance on real data (AUC=0.454).\",\n    \"Explicitly downgrades the AUC=0.718 result from 'confirmed detection' to 'promising preliminary evidence': bootstrap CI [0.459, 0.922] includes values below chance; permutation test with 10,000 label permutations is required before a significance claim is valid.\",\n    \"Explains the raw Hodge failure mechanism: 3 of 7 stacking journals are isolated nodes in the sampled network, receiving zero curl scores by construction; the method requires triangular connectivity to produce nonzero scores.\",\n    \"Documents the injection-vs-real-data gap as an unresolved tension requiring explanation: synthetic injection best AUC=0.617 vs. real-data AUC=0.718; proposes the 'persistent multi-year accumulation' hypothesis as the bridge but marks it as unvalidated.\",\n    \"Flags the CIDRE comparison as methodologically incomplete: cidre Python 3.12 incompatibility is a matplotlib visualization dependency only; the core dcSBM algorithm can run in Python 3.8/3.9 without code changes; the fallback (AUC=0.343) is not the published method.\",\n    \"Explicitly scopes out balanced reciprocal exchange (W_ij ≈ W_ji → near-zero net-flow, invisible to Hodge) and excessive self-citation (33 of 40 suppressed journals) as structural blind spots of the current method.\",\n    \"Notes that the 77% curl fraction in the real network may be partially inflated by the 40 suppressed journals within it; computing curl decomposition on the 191 clean journals only is required to validate the 'natural curl dominance' claim.\",\n    \"Retains the mathematical orthogonality claim (gradient and curl are orthogonal by construction) as a theorem-level guarantee, while treating the practical advantage over density-based methods as an empirical hypothesis still requiring proper CIDRE comparison.\"\n  ],\n  \"relation_type\": \"evolution\",\n  \"artifact_relations\": [\n    {\n      \"from_id\": \"art_Md6TNdV-FZYE\",\n      \"to_id\": \"art_gkqGp1-55dg1\",\n      \"relation_type\": \"extends\",\n      \"relation_rationale\": \"Extends specs with HLSAD positioning and corrected JCR stacking annotations (4 in 2021; 2020=0 stacking).\"\n    },\n    {\n      \"from_id\": \"art_IGeLtKiwHWQE\",\n      \"to_id\": \"art_XbmaHSRFGigA\",\n      \"relation_type\": \"uses\",\n      \"relation_rationale\": \"Uses the 231-journal citation network and JCR suppression labels as the primary real-data evaluation set.\"\n    },\n    {\n      \"from_id\": \"art_Md6TNdV-FZYE\",\n      \"to_id\": \"art_XbmaHSRFGigA\",\n      \"relation_type\": \"uses\",\n      \"relation_rationale\": \"Uses Hodge decomposition methodology specs (boundary operators, lsqr solver, CIDRE API, CDFD) to implement the 6-phase evaluation.\"\n    }\n  ]\n}\n", "structuredPatch": [{"oldStart": 32, "oldLines": 7, "newStart": 32, "newLines": 7, "lines": ["       \"from_id\": \"art_Md6TNdV-FZYE\",", "       \"to_id\": \"art_XbmaHSRFGigA\",", "       \"relation_type\": \"uses\",", "-      \"relation_rationale\": \"Uses Hodge decomposition methodology specs (boundary operators, lsqr solver, CIDRE API, CDFD) to implement the 6-phase evaluation.\"", "+      \"relation_rationale\": \"Uses Hodge methodology specs (boundary operators, lsqr, CIDRE, CDFD) to implement the 6-phase evaluation.\"", "     }", "   ]", " }"]}], "userModified": false, "replaceAll": false}
```

### [15] ASSISTANT · 2026-07-09 01:57:50 UTC

```
All three rationale strings are now within the 120-character limit.
```

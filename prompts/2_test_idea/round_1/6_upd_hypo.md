# upd_hypo — test_idea

> Phase: `invention_loop` · round 1 · `upd_hypo`
> Run: `run_io13l_LyCX8s` — Curl in the Citation Graph: Hodge Flow Decomposition Detects Citation Cartels via Field-Aware Calibration
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `upd_hypo` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-07-09 00:36:46 UTC

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
title: Honest citations flow, cartels circle back
hypothesis: >-
  A citation-flow network can be uniquely split, using the Helmholtz-Hodge decomposition of a vector field (any field = the
  gradient of a potential + a divergence-free rotational part) generalized to graphs by combinatorial Hodge theory, into three
  orthogonal components: (1) a GRADIENT flow that follows a single global 'prestige potential' — a consistent hierarchy in
  which citations run from foundational toward frontier work; (2) a CURL flow made of small local citation loops that NO global
  ranking can explain; and (3) a HARMONIC flow of large-scale cross-field loops. We hypothesize this split is a natural taxonomy
  of citation patterns, and specifically that genuine scholarly influence is gradient-dominated (it admits a single global
  ordering) whereas coordinated citation manipulation — cartels, citation stacking, and reciprocal-citation rings — is precisely
  the ranking-defying CURL. Consequently the curl energy, localized to individual nodes/edges/triangles, detects and pinpoints
  manipulation ORTHOGONALLY to citation density: it separates a genuinely influential tight-knit community (dense but internally
  hierarchical → low curl) from a cartel (dense AND ranking-inconsistent → high curl) — the confound that density/stochastic-block-model
  detectors such as CIDRE were built to fight — and it does so while the same single computation returns a self-certifying
  prestige ranking (the gradient potential) that flags its own manipulation-corrupted regions.
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
</all_artifacts>

<new_artifacts_this_iteration>
These 3 artifacts were created THIS iteration.

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
</new_artifacts_this_iteration>

<current_paper>
The paper draft from this iteration — represents the current state of the research story.

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
</current_paper>

<reviewer_feedback>
Feedback from the paper reviewer this iteration.

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

### [2] HUMAN-USER prompt · 2026-07-09 00:36:46 UTC

```
Propose a simple, novel graph-based method for detecting citation patterns in academic networks and validate it.
```

### [3] SYSTEM-USER prompt · 2026-07-09 00:38:03 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `relation_rationale`: 'Same Hodge-decomposition frame; refines primary detector to gradient residual and conditions real-world claims on pending validation.' is too long (at most 120 characters, got 133)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

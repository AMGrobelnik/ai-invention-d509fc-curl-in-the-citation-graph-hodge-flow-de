# gen_paper_text — test_idea

> Phase: `invention_loop` · round 1 · `gen_paper_text`
> Run: `run_io13l_LyCX8s` — Academic Citation Patterns
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_paper_text` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-07-09 00:20:32 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A research paper writer (Step 3.4: GEN_PAPER_TEXT in the invention loop)

You received the hypothesis, all artifacts, the previous paper draft (if any), and reviewer feedback.
Write a complete paper draft with figure placeholders.

Publication-quality paper → strong contribution. Weak paper → wasted iteration.
</your_role>
</ai_inventor_context>

<research_methodology>
Write like a researcher drafting a paper, not a chatbot summarizing bullet points.

- Structure as a paper would: research question → methodology → results → analysis → limitations. Not a list of "we did X, then Y."
- Ground every claim in specific artifacts and specific numbers. "Results show improvement" is empty — state effect sizes, baselines, and conditions.
- Be honest about what worked, what didn't, and why. Don't spin failures as "future work."
- The paper's headline contribution should be a positive or surprising finding. Negative results are valuable context but should not be the primary narrative — lead with what works.
- Address reviewer feedback from previous iterations explicitly — show you've thought about each critique.
</research_methodology>

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

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

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. Use it for related-work positioning and how this field frames a genuinely novel contribution.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>
<hypothesis>
The research hypothesis.

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
</hypothesis>

<all_artifacts>
FULL EVIDENCE BASE: All 3 research artifacts across all iterations.

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
NEW THIS ITERATION: These 3 artifacts were created to address the reviewer
feedback. Their findings should be the primary basis for your revisions.

id: art_Md6TNdV-FZYE
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
type: research
title: Hodge Decomposition & Citation Cartel Detection Specs

id: art_IGeLtKiwHWQE
summary: |-
  Dataset: OpenAlex Journal Citation Flow Network + Clarivate JCR Suppression Labels (2015-2022).

  Source: OpenAlex API (free tier) for journal metadata and citation counts; Clarivate JCR suppressed-title lists (2018-2022) for binary manipulation labels.

  Network: 231 high-impact journals (top by cited_by_count), 15,188 directed citation pairs, 668,390 underlying work-level cross-journal citation links aggregated from ~190,000 journal articles published 2015-2022.

  Ground truth: 40 journals labeled suppressed=1 (label=1) for citation stacking or excessive self-citation, 191 journals labeled clean=0. Suppressed journals include MDPI mass-suppression (2020: IJERPH, Sustainability, Applied Sciences, Energies, Nutrients, Sensors, Water, Materials, Remote Sensing, Electronics, etc.), Frontiers citation-stacking (2021: Oncology, Neuroscience, Immunology, Psychology, Cell Dev Bio), Scientific Reports (2021), Oncotarget (2019), PLOS ONE (2019), RSC Advances (2019), and others.

  Schema: Each of the 15,188 examples in full_data_out.json represents one directed citation pair (journal i → journal j). The input field is a natural-language description of the citation relationship. The output field is the binary suppression label for journal i (string '0' or '1'). Metadata fields include: source_id_i, source_id_j, journal names, citation_count_ij, citation_count_ji, net_flow_ij, year_window, label_i, label_j, works_count_i, field_i, task_type, row_index.

  Supplementary files: adjacency_matrix.npz (231×231 scipy CSR sparse matrix, nnz=15,188), journal_metadata.json (231 journals with id/name/issn_l/field/works_count/cited_by_count), ground_truth_labels.json ({openalex_source_id: 0/1}), match_report.json (suppression ISSN resolution log).

  Scale note: The target was ≥500K pairs across ≥5,000 journals; the actual coverage is 231 journals and 15,188 pairs due to OpenAlex free-tier API rate limits (daily budget exhausted at ~3,000 API calls). The within-network density is high (28.5% fill), making this suitable for Hodge decomposition on the observed subgraph. The 231-journal network covers the most-cited journals globally and includes all major suppressed journals from the 2018-2022 JCR lists.

  Designed for: HodgeRank / Hodge decomposition citation manipulation detection; node classification on citation graphs; anomaly detection in academic publishing networks.
type: dataset
title: Journal Citation Network with JCR Suppression Labels

id: art_bzU_zt6gp8SL
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
type: experiment
title: Hodge Curl Citation Cartel Detector
</new_artifacts_this_iteration>

<data_files>
Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</data_files>

<task>
Write a research paper draft with LaTeX-ready text, BibTeX citations, and figure placeholders.

This is the FIRST paper draft. Write a complete research paper from scratch based on the hypothesis and all available artifacts.
</task>

<figure_instructions>
FIGURE FORMAT: Use [FIGURE:fig_id] markers in paper_text to indicate where each figure goes.
Then provide the full figure specs in the separate `figures` structured output array.
Each figure in the array must have an `id` matching a marker in the text. Set the `aspect_ratio`
field per figure: 21:9 for architecture / pipeline / flow-chart diagrams (the hero figure should
be one of these — place its marker near the END of the Introduction so it floats to the top of
page 2), 16:9 for comparisons / multi-panel results, 4:3 for dense charts, 1:1 for heatmaps /
confusion matrices / scatter plots.

Example in paper_text:
  "...our method achieves state-of-the-art results as shown below.\n\n[FIGURE:fig3]\n\nThe results demonstrate..."

Example in figures array (results comparison):
  {"id": "fig3", "title": "Performance Comparison", "caption": "Comparison of geometric mean query latency across optimizers.", "image_gen_detailed_description": "Grouped bar chart. X-axis: model names. Y-axis: latency (seconds, 0-5). Values: PostgreSQL=4.6s (red), Bao=2.8s (blue), RLQOpt=2.0s (green). Error bars +/-0.3-0.8. Sans-serif font, white background.", "aspect_ratio": "16:9", "summary": "Compares latency across optimizers"}

Example in figures array (architecture diagram, hero):
  {"id": "fig1", "title": "System Architecture", "caption": "End-to-end pipeline: encoder feeds latents into the planner, which queries the value head before emitting actions.", "image_gen_detailed_description": "Horizontal flow diagram, left to right. Five labeled boxes: 'Input' (gray), 'Encoder' (blue), 'Latent (z, 256-dim)' (light blue, narrow), 'Planner' (green), 'Action Head' (orange). Arrows labeled with shapes. Value head as separate green box below 'Planner', bidirectional arrow. Sans-serif font, clean white background, no 3D.", "aspect_ratio": "21:9", "summary": "Hero architecture diagram"}

CRITICAL: Before writing figure specs, look through artifact workspace output files (*_out.json)
and code to find ALL the exact values. The figure generator cannot read files — every exact number
and value MUST be in the image_gen_detailed_description.
</figure_instructions>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-writing, aii-semscholar-bib.
TODO 2. LITERATURE REVIEW: Use web search tools to research the landscape — search key terms from
<hypothesis> and <all_artifacts>. Then use aii_semscholar_bib__fetch to batch-fetch real
BibTeX entries. Build a comprehensive Related Work section. Do NOT fabricate entries.
TODO 3. READ ARTIFACTS: Before writing each section, READ the relevant artifact source code, output
files, and data in the workspace. Extract concrete implementation details, technical innovations,
algorithmic specifics, and quantitative results. Do NOT write surface-level descriptions.

ARTIFACT REFERENCES: When you reference results, methodology, or findings from a specific artifact,
place an [ARTIFACT:artifact_id] marker inline. These become footnotes linking to the artifact's code
in the GitHub repository (first mention gets a footnote with URL, subsequent mentions are omitted).
Use the exact artifact ID from <all_artifacts>. Place the marker right after the claim it supports.
Example:
  "Our evaluation showed a 15% improvement over baselines [ARTIFACT:art_4f9d2c81ab37]." 
TODO 4. WRITE PAPER: Write the full paper text with [FIGURE:fig_id] markers per <figure_instructions>,
and provide the figure specs in the figures array. Cite with numeric references [1], [2], etc.
At the end of the paper text, include a full bibliography section. Do NOT compile LaTeX or generate
actual image/figure files. Your ONLY output is the structured JSON.
</todos><user_data>
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
    "FigureSpec": {
      "description": "Figure specification \u2014 structured output from paper writing agent.\n\nThe LLM fills these as a list in PaperText.figures.\nLater converted to Figure objects for viz gen.",
      "properties": {
        "id": {
          "description": "Figure ID matching the [FIGURE:id] marker in paper_text (e.g., 'fig1')",
          "title": "Id",
          "type": "string"
        },
        "title": {
          "description": "Figure title in plain, everyday language \u2014 short and jargon-free. Aim for about 4-8 words (~40 characters).",
          "title": "Title",
          "type": "string"
        },
        "caption": {
          "description": "LaTeX figure caption \u2014 appears below the figure in the paper. Should describe what the figure shows and highlight key takeaways.",
          "title": "Caption",
          "type": "string"
        },
        "image_gen_detailed_description": {
          "description": "Detailed image generation prompt \u2014 axes, labels, ALL numeric values, colors, aspect ratio, layout. The image generator cannot read files; this is its ONLY input.",
          "title": "Image Gen Detailed Description",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this figure communicates",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "id",
        "title",
        "caption",
        "image_gen_detailed_description",
        "summary"
      ],
      "title": "FigureSpec",
      "type": "object"
    }
  },
  "description": "Paper text \u2014 structured output from paper writing agent.\n\nStructured output fields (LLMPrompt + LLMStructOut):\n- title, abstract, paper_text, figures, summary\n\npaper_text contains [FIGURE:fig_id] markers for positioning.\nfigures contains the full specs as structured objects.\n\nMetadata fields (plain, set by pipeline code):\n- id",
  "properties": {
    "title": {
      "description": "Paper title \u2014 clear, plain-language, and short so a non-expert understands the main contribution at a glance. Aim for about 6-10 words; avoid jargon and acronyms.",
      "title": "Title",
      "type": "string"
    },
    "abstract": {
      "description": "Paper abstract",
      "title": "Abstract",
      "type": "string"
    },
    "paper_text": {
      "description": "Full paper body text with markdown section headers (# Introduction, # Methods, # Results, # Discussion, # Conclusion). Use [FIGURE:fig_id] markers (e.g. [FIGURE:fig1]) to indicate where each figure should appear.",
      "title": "Paper Text",
      "type": "string"
    },
    "figures": {
      "description": "List of figure specifications. Each must have an id matching a [FIGURE:id] marker in paper_text.",
      "items": {
        "$ref": "#/$defs/FigureSpec"
      },
      "title": "Figures",
      "type": "array"
    },
    "summary": {
      "description": "Brief summary of the paper's main contribution and findings",
      "title": "Summary",
      "type": "string"
    }
  },
  "required": [
    "title",
    "abstract",
    "paper_text",
    "summary"
  ],
  "title": "PaperText",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-07-09 00:20:32 UTC

```
Propose a simple, novel graph-based method for detecting citation patterns in academic networks and validate it.
```

### [3] SKILL-INPUT — aii-paper-writing · 2026-07-09 00:20:38 UTC

The agent loaded the **aii-paper-writing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-writing
description: Academic paper writing guidance for AI research. Covers paper structure, figure placeholders, bibliography building with Semantic Scholar, and citation rules. Does NOT cover LaTeX compilation or figure file generation — see aii-paper-to-latex for that.
---

## Technical Papers

Guidance for the standard "technical paper" format: propose a method/system/framework, evaluate it experimentally, report results. This is the main track at most CS venues (NeurIPS, ICML, ICLR, ACL, AAAI, etc.). Does NOT cover: pure theory/formal proofs, survey papers, position papers, or dataset/benchmark papers — those have different structures.

### Paper Structure

Target 6-8 pages. Use formal academic language, third person. Support claims with evidence from artifacts.

#### Rough Page Budget (8-page paper)

| Section | Pages | Notes |
|---|---|---|
| Abstract | 0.3 | Problem, approach, key result |
| Introduction | 1.0-1.5 | The most important section |
| Related Work | 0.5-1.0 | Beginning or end (see below) |
| Methods | 1.5-2.0 | Architecture fig on page 1 |
| Experiments | 1.5-2.0 | Setup + results + ablations |
| Discussion | 0.5-1.0 | Limitations go here |
| Conclusion | 0.3-0.5 | Do not repeat the abstract |
| References | 0.5-1.0 | Not counted in page limit |

**Critical rule**: A clear new technical contribution must be articulated by page 3 (quarter of the paper). If the reader doesn't know what you did by then, you've lost them.

#### Section Details

**Abstract** (150-250 words): State the problem, your approach, and the main results. Be factual and comprehensive. Do not repeat the abstract word-for-word later in the paper.

**Introduction** — Follow this 5-paragraph structure:

1. **What is the problem?** Define the task concretely.
2. **Why is it interesting and important?** Real-world impact, scale.
3. **Why is it hard?** Why do naive approaches fail?
4. **Why hasn't it been solved before?** What's wrong with prior solutions? How does yours differ?
5. **What are the key components of your approach and results?** Include specific limitations.

End with a "Summary of Contributions" subsection — bullet list of contributions with section references. This doubles as an outline, saving space.

**Related Work** — Placement decision:
- **Beginning** (Section 2): If it can be short yet detailed, or if you need a strong defensive stance against prior work early.
- **End** (before Conclusions): If comparisons require your technical content, or if it can be summarized briefly in the Introduction. Can be titled "Discussion and Related Work."

**Methods/Approach**: Every section tells a story — the story of the results, NOT the story of how you arrived at them. Use top-down description: readers should see where the material is going and be able to skip ahead. Move gory details to appendices.

**Experiments**: Setup (datasets, metrics, baselines) → main results → ablations → analysis. Every claim needs quantitative evidence.

**Discussion**: Interpret results, compare to prior work, state limitations honestly. Limitations should be specific and actionable, not vague disclaimers.

**Conclusion**: Short summarizing paragraph. Do NOT repeat material from the Abstract or Introduction. Make original claims more concrete (e.g., reference quantitative results). Include future work as bullet list — if actively pursuing follow-up, say so to mark territory.

#### Writing Quality Rules

- Define all notation/terminology before use, only once. Group global definitions in Preliminaries.
- Do NOT use nonreferential "this", "that", "these", "it". Always specify the referent. BAD: "This is important because..." GOOD: "This accuracy gap is important because..."
- Do NOT use "etc." unless remaining items are completely obvious. BAD: "We measure volatility, scalability, etc." GOOD: "We measure volatility and scalability."
- Do NOT write "for various reasons" — state the actual reasons.
- "That" is defining, "which" is nondefining. "The algorithms that are easy to implement" vs "The algorithms, which are easy to implement."
- Use italics for definitions and quotes, not for emphasis. Context alone should provide emphasis.

### Figure Format

Figures use a hybrid marker + structured array approach. ALL figures are generated by a separate pipeline step using an AI image model — your `image_gen_detailed_description` is the ONLY input that model sees. It cannot read files or access data. Do NOT generate actual image files yourself (no matplotlib, no PIL, no image generation scripts).

**In paper_text**: Place `[FIGURE:fig_id]` markers where figures should appear.

**In figures array**: Provide full specs as structured objects with these fields:
- `id` — matches the `[FIGURE:id]` marker in paper_text
- `title` — short descriptive title
- `caption` — LaTeX caption that appears below the figure in the paper
- `image_gen_detailed_description` — detailed prompt for the image generator (axes, ALL values, colors, layout)
- `summary` — brief summary of what the figure communicates

Example in paper_text:
```
...our method achieves state-of-the-art results as shown below.

[FIGURE:fig_1]

The results in Figure 1 demonstrate...
```

Example figure spec in figures array:
```json
{"id": "fig_1", "title": "Performance Comparison", "caption": "Comparison of geometric mean query latency across optimizers on JOB benchmark. RLQOpt achieves 2.3x speedup over PostgreSQL.", "image_gen_detailed_description": "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: ModelA=0.847, ModelB=0.762, Baseline=0.531. Error bars with std: 0.02, 0.03, 0.05. Sans-serif font, white background.", "summary": "Compares accuracy of proposed methods vs baseline."}
```

Every marker in text MUST have a matching figure in the array, and vice versa.

#### Data Precision Requirement

`image_gen_detailed_description` MUST include exact numbers from artifact output files. Read the actual output files before writing figure specs.

- BAD: "Compare accuracy metrics across configurations"
- GOOD: "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: K=3: 0.765, K=5: 0.729, Baseline: 0.121."

#### Figure vs Table Decision

Do NOT create figures for tabular data (rows/columns of text or numbers). Use `\begin{table}` in LaTeX instead. Figures are for actual visualizations only (charts, plots, diagrams).

#### Figure Placement Strategy

Be intentional with figure ordering. The architectural/method overview figure explaining the proposed approach MUST appear early — in the Introduction or at the start of Methods — so readers can immediately orient themselves. Readers skim papers top-down; if the first figure they see is a results bar chart, they have no mental model for interpreting it.

Recommended ordering:
1. **Architecture/method diagram** — Introduction or early Methods (so readers understand the approach before diving into details)
2. **Conceptual/analogy figures** — Introduction or Methods (to build intuition)
3. **Results figures** (bar charts, line plots, scatter plots) — Results section
4. **Analysis/ablation figures** — Discussion or later Results

#### Guidelines

- Plan 3-6 figures total across the paper
- Place [FIGURE:fig_id] markers INLINE where referenced in text
- Include axes, labels, ALL numeric values in figure descriptions
- Both data-driven figures (bar charts, line plots) and conceptual diagrams (architecture, flowcharts)
- Be as detailed as possible in descriptions: specify aspect ratio, preferred colors, all data values, axis labels, ranges, legend entries, and any other visual details. The more specific the description, the better the generated figure

### Bibliography with Semantic Scholar

Build `./references.bib` using the aii-semscholar-bib skill (real BibTeX from Semantic Scholar):

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in one batch
3. Write the returned .bib text into `./references.bib`

Rules:
- Do NOT fabricate BibTeX entries — always fetch from Semantic Scholar
- If a paper isn't found (very recent preprint), write the entry manually as fallback
- Use `\bibliography{references}` and `\bibliographystyle{plainnat}`
- Do NOT use inline `thebibliography` environment

### Citation Format (for Research Artifacts)

When writing research with numbered citations:

1. Every factual claim MUST have a numbered citation: `[1]`, `[2]`, `[1, 3]`, etc.
2. Each source in the "sources" array MUST have an "index" field
3. The index MUST EXACTLY MATCH citation numbers in the text
4. NEVER cite a number without a matching source index
5. Example: "LLMs show 40% improvement with multi-agent collaboration [1]."
````

### [4] SKILL-INPUT — aii-semscholar-bib · 2026-07-09 00:20:44 UTC

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

### [5] SKILL-INPUT — aii-web-tools · 2026-07-09 00:21:06 UTC

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

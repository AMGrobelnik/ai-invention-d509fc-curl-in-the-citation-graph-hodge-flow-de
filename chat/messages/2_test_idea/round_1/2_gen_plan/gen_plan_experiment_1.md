# gen_plan_experiment_1 — test_idea

> Phase: `invention_loop` · round 1 · `gen_plan`
> Run: `run_io13l_LyCX8s` — Academic Citation Patterns
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_plan_experiment_1` (terminal_claude_agent, claude-sonnet-4-6)

### [1] CONFIG · 2026-07-08 23:08:42 UTC

```
model: claude-sonnet-4-6 | effort: high | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_1/gen_plan/gen_plan_experiment_1
```

### [2] SYSTEM-USER prompt · 2026-07-08 23:08:50 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A plan generator (Step 3.2: GEN_PLAN in the invention loop)

You received the hypothesis, an artifact direction to elaborate, and dependency artifacts relevant to the plan.
Your job: elaborate this direction into a detailed, actionable plan for the executor agent.

Specific, actionable plan → valuable artifact. Vague plan → wasted execution.
</your_role>
</ai_inventor_context>

<artifact_type_info>
You are expanding an artifact direction of type: EXPERIMENT

EXPERIMENT
Run code to test hypotheses, implement methods, and collect empirical results.
Runtime: Python 3.12, UV (any pip package), isolated workspace, gradual scaling (mini → full data).
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Implement and run any code-based experiment, compare method vs baselines.
Deps: REQUIRED at least one DATASET | OPTIONAL RESEARCH for methodology guidance
</artifact_type_info>

<available_resources>
<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Web search (Serper), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-image-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
</skills>

<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>
</available_resources>

<time_budget>

The experiment executor has 6h total (including writing code, debugging, testing, and fixing errors).

</time_budget>

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

<plan_guidelines>
You are expanding an artifact direction from the strategy into a detailed plan.
The artifact direction specifies what to do at a high level (type, objective, approach, dependencies).
Your job is to make it concrete and actionable as a detailed plan.
Use web research to look up technical details, verify feasibility, and find reference materials
that will make your plan more concrete and actionable for the executor.

GOOD PLANS:
- Make each component SPECIFIC and actionable (not vague platitudes)
- Consider both success AND failure scenarios
- Build on the approach in the artifact direction
- Add concrete details the executor needs

BAD PLANS:
- Vague hand-waving ("do research on X")
- Ignoring the approach in the artifact direction
- Missing critical details the executor needs
</plan_guidelines>

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

<hypothesis>
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

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. Use it for the methods, proper baselines, and evaluation this field demands.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: experiment_iter1_dir3
type: experiment
objective: >-
  Implement the full Hodge decomposition pipeline on the journal citation network, compute curl-based manipulation scores
  at node/group/triangle level, calibrate against a degree-preserving null, and compare head-to-head with CIDRE, reciprocity
  ratio, and within-group density on JCR-suppressed journal detection (AUC, precision@k, precision-recall curve) plus synthetic
  cartel injection tests across density regimes.
approach: >-
  PHASE 1 — Hodge decomposition implementation (pure scipy): (a) From the journal×journal net-flow matrix Y (antisymmetric),
  build the oriented incidence matrix B (nodes × edges) and the weighted edge Laplacian. (b) Solve the gradient potential:
  s* = argmin_s ||B^T s - Y_e||^2_W where Y_e is the edge flow vector and W is the edge weight diagonal — standard sparse
  least-squares via scipy.sparse.linalg.lsqr. The solution s* is the HodgeRank prestige score. (c) Decompose: gradient component
  Y_grad = B(B^T B)^+ B^T Y_e; residual R = Y_e - Y_grad contains curl + harmonic. (d) Curl localization: for each triangle
  (i,j,k) in the graph, compute triangle_curl = Y[i,j] + Y[j,k] + Y[k,i]; node curl score = mean absolute triangle curl over
  all triangles containing that node; group curl score = sum of |triangle_curl| over all triangles within the group, normalized
  by group volume. (e) Edge curl score = |residual on edge| / edge weight. PHASE 2 — Null model calibration: Generate 500
  degree-preserving random graphs via edge-weight shuffling (preserve in/out-degree sequences); compute null distribution
  of group curl scores; p-value = fraction of null exceeding observed; also fit a Poisson/normal approximation for speed.
  PHASE 3 — Baselines: (a) Reciprocity ratio per node = min(C[i,j], C[j,i]) / (C[i,j] + C[j,i] + eps). (b) Within-group density
  = sum of internal citations / possible. (c) PageRank/Eigenfactor on the raw citation graph. (d) CIDRE: install from kojaku/cidre
  GitHub (pip install), run on same network with default parameters, extract anomaly scores per journal. PHASE 4 — Evaluation
  on JCR ground truth: For each method, treat suppressed journals as positives. Compute AUC-ROC, AUC-PR, precision@10/50/100,
  and bootstrap 95% CIs (B=2000). Report whether curl AUC CI excludes CIDRE AUC (the key comparison). PHASE 5 — Synthetic
  injection: Take the real network, inject k-node cyclic cartels (A→B→C→A with weight w) and k-node reciprocal cartels (A↔B↔C
  with weight w) at varying k (3,5,10,20) and w (0.01×, 0.1×, 1× mean edge weight). Measure detection AUC for Hodge-curl vs.
  density vs. CIDRE as w decreases — the hypothesis predicts Hodge-curl degrades more slowly. PHASE 6 — Confound test: Identify
  hand-labeled dense-but-legitimate clusters (top-5 prolific fields by internal citation density) and compare their internal
  curl fraction to known cartel groups — if density confounds but curl does not, the key theoretical claim holds. Output method_out.json
  with all scores, CI bounds, and per-phase result tables.
depends_on: []
</artifact_direction>



<instructions>
YOUR ROLE: Write a detailed PLAN for the artifact. A separate executor agent runs the actual artifact later.

You are a PLANNER, not an executor. Your output is a plan that tells the executor what to do and how.
Do NOT execute the artifact itself — a separate agent handles that. Your job is to plan it so well that the executor can follow your plan step by step.

You CAN and SHOULD: search the web, read papers, and explore library docs to make your plan concrete.
You CANNOT run shell commands or scripts — code execution is disabled. Research via web tools only.

Do NOT do the executor's job: don't download datasets, don't implement code, don't run experiments, don't write proofs, don't compute evaluations.

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

EXPERIMENT executor scope:
  Output: method_out.json with results (metrics, predictions, analysis) — the core computational work
  DOES: Implement and run methods/algorithms, compute metrics, compare approaches, produce quantitative results
  DOES NOT: Collect new datasets (depends on DATASET artifacts for input data), write formal proofs
  This is the right artifact for any code that processes data and produces results
</artifact_executor_scope>

<artifact_planning_rules>
EXPERIMENT: Must depend on at least one DATASET. Define clear metrics and baselines before running. Consider trying multiple method variations rather than a single approach.
</artifact_planning_rules>

<compute_profiles>
Choose the compute profile this artifact needs for execution.
Available profiles for experiment artifacts:
  - gpu: 1x NVIDIA RTX A4500, 20GB VRAM, 7 vCPUs, 29GB RAM — ML training, CUDA, large models (fallback: GPUs cheap→expensive: 2000 Ada → A4000 → 4000 Ada → L4 → 4090 → 5090)
  - cpu_heavy: 4 vCPUs, 32GB RAM — large datasets, memory-intensive processing (fallback: CPUs cheap→expensive, then GPU hosts cheap→expensive (all ≥32GB RAM))

Set runpod_compute_profile to one of these exact tier names.
</compute_profiles>
GOOD PLANS: specific, actionable, consider failure scenarios, build on the suggested approach.
BAD PLANS: vague hand-waving, ignoring the suggested approach, missing critical executor details.
</instructions><user_data>
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
  "description": "Plan for an EXPERIMENT artifact.",
  "properties": {
    "title": {
      "description": "Plan title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters).",
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Brief summary",
      "title": "Summary",
      "type": "string"
    },
    "runpod_compute_profile": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "cpu_light",
      "description": "Compute tier for execution \u2014 pick from the available profiles list (e.g., 'gpu', 'cpu_heavy', 'cpu_light'). Only used in RunPod mode.",
      "title": "Runpod Compute Profile"
    },
    "implementation_pseudocode": {
      "description": "High-level pseudocode for the experiment implementation",
      "title": "Implementation Pseudocode",
      "type": "string"
    },
    "fallback_plan": {
      "description": "What to do if the primary approach fails - alternative methods, simplified versions",
      "title": "Fallback Plan",
      "type": "string"
    },
    "testing_plan": {
      "description": "How to validate the experiment works: start with small/fast tests, look for confirmation signals before running full-scale experiments",
      "title": "Testing Plan",
      "type": "string"
    }
  },
  "required": [
    "title",
    "implementation_pseudocode",
    "fallback_plan",
    "testing_plan"
  ],
  "title": "ExperimentPlan",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [3] HUMAN-USER prompt · 2026-07-08 23:08:50 UTC

```
Propose a simple, novel graph-based method for detecting citation patterns in academic networks and validate it.
```

### [4] ASSISTANT · 2026-07-08 23:08:57 UTC

```
I'll research the key technical components to make this plan concrete and actionable. Let me run parallel searches on the main dependencies.
```

### [5] TOOL CALL — Skill · 2026-07-08 23:08:57 UTC

```
aii-web-tools
```

### [6] TOOL RESULT — Skill · 2026-07-08 23:08:57 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [7] TOOL CALL — ToolSearch · 2026-07-08 23:08:59 UTC

```
{'query': 'select:WebSearch,WebFetch'}
```

### [8] TOOL RESULT — ToolSearch · 2026-07-08 23:08:59 UTC

```
{"matches": ["WebSearch", "WebFetch"], "query": "select:WebSearch,WebFetch", "total_deferred_tools": 21}
```

### [9] ASSISTANT · 2026-07-08 23:09:07 UTC

```
Now I'll run parallel searches on all the key technical components.
```

### [10] TOOL CALL — WebSearch · 2026-07-08 23:09:07 UTC

```
CIDRE citation cartel detection kojaku GitHub install pip 2021
```

### [11] TOOL CALL — WebSearch · 2026-07-08 23:09:07 UTC

```
HodgeRank graph Hodge decomposition scipy sparse lsqr implementation python
```

### [12] TOOL CALL — WebSearch · 2026-07-08 23:09:07 UTC

```
OpenAlex journal citation network API download journal level citations
```

### [13] TOOL CALL — WebSearch · 2026-07-08 23:09:07 UTC

```
Clarivate JCR suppressed journals citation stacking list 2018 2019 2020 2021 2022 2023
```

### [14] TOOL RESULT — WebSearch · 2026-07-08 23:09:11 UTC

```
{"query": "CIDRE citation cartel detection kojaku GitHub install pip 2021", "results": [{"tool_use_id": "srvtoolu_014tRZ2MRSg5832uqhMVYkTf", "content": [{"title": "GitHub - skojaku/cidre: CIDRE: Detecting anomalous donors and recipients in directed weighted networks. · GitHub", "url": "https://github.com/skojaku/cidre"}, {"title": "Detecting anomalous citation groups in journal networks", "url": "https://ouci.dntb.gov.ua/en/works/4Man3Xd4/"}, {"title": "GitHub - skojaku/journal-citation-cartels · GitHub", "url": "https://github.com/skojaku/journal-citation-cartels"}, {"title": "cidre · PyPI", "url": "https://pypi.org/project/cidre/"}, {"title": "(PDF) Detecting citation cartels in journal networks", "url": "https://www.researchgate.net/publication/344334965_Detecting_citation_cartels_in_journal_networks"}, {"title": "(PDF) Detecting anomalous citation groups in journal networks", "url": "https://www.researchgate.net/publication/353266793_Detecting_anomalous_citation_groups_in_journal_networks"}, {"title": "Detecting anomalous citation groups in journal networks | Scientific Reports", "url": "https://www.nature.com/articles/s41598-021-93572-3"}, {"title": "[2009.09097] Detecting anomalous citation groups in journal networks", "url": "https://arxiv.org/abs/2009.09097"}, {"title": "Detecting anomalous citation groups in journal networks - PubMed", "url": "https://pubmed.ncbi.nlm.nih.gov/34267254/"}, {"title": "Detecting citation cartels in journal networks", "url": "https://www.arxiv.org/pdf/2009.09097v1"}]}, "Based on the search results, here's what I found about CIDRE and its installation:\n\n## CIDRE - Citation Cartel Detection Algorithm\n\nCIDRE is an algorithm to find anomalous groups in directed and weighted networks. More specifically, CIDRE is designed to detect anomalous groups of journals that exchange citations at excessively high rates when compared against a null model that accounts for scientific communities and journal size.\n\nThe algorithm was created by Kojaku, S., Livan, G. & Masuda, N. and published in Scientific Reports in 2021.\n\n## Installation via pip\n\nThe package can be installed using `pip install cidre` and requires Python 3.7 or later.\n\n## GitHub Repository\n\nThe source code is available at the official GitHub repository: **skojaku/cidre** (https://github.com/skojaku/cidre)\n\n## How It Works\n\nCIDRE addresses the challenge of detecting anomalous citation groups by using a null model of networks with communities to discount the amount of citations between communities.\n\nCIDRE detects more than half of the journals suspended from Journal Citation Reports due to anomalous citation behavior in the year of suspension or in advance."], "durationSeconds": 6.192333352000001, "searchCount": 1}
```

### [15] TOOL RESULT — WebSearch · 2026-07-08 23:09:11 UTC

```
{"query": "HodgeRank graph Hodge decomposition scipy sparse lsqr implementation python", "results": [{"tool_use_id": "srvtoolu_017hnvoGErPjVUASLMk5VRaG", "content": [{"title": "hodgelaplacians/README.md at master · tsitsvero/hodgelaplacians", "url": "https://github.com/tsitsvero/hodgelaplacians/blob/master/README.md"}, {"title": "Evaluating Visual Properties via Robust HodgeRank", "url": "https://arxiv.org/pdf/1408.3467"}, {"title": "Statistical ranking and combinatorial Hodge theory", "url": "https://web.stanford.edu/~yyye/hodgeRank2011.pdf"}, {"title": "scipy.sparse.linalg.lsqr — SciPy v0.18.1 Reference Guide", "url": "https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.sparse.linalg.lsqr.html"}, {"title": "Topological Effective Connectivity Modeling in Brain Networks", "url": "https://arxiv.org/pdf/2606.08407"}, {"title": "scipy.sparse.linalg.lsqr — SciPy v1.7.1 Manual", "url": "https://docs.scipy.org/doc/scipy-1.7.1/reference/generated/scipy.sparse.linalg.lsqr.html"}, {"title": "Python abstract_simplicial_complex Examples, pydec.abstract_simplicial_complex Python Examples - HotExamples", "url": "https://python.hotexamples.com/examples/pydec/-/abstract_simplicial_complex/python-abstract_simplicial_complex-function-examples.html"}, {"title": "Statistical ranking and combinatorial Hodge theory | Mathematical Programming | Springer Nature Link", "url": "https://link.springer.com/article/10.1007/s10107-010-0419-x"}, {"title": "Graph Classification Gaussian Processes via Hodgelet Spectral Features", "url": "https://arxiv.org/pdf/2410.10546"}]}, "I found relevant search results for your query. Here's what the web search revealed:\n\n## HodgeRank and Hodge Decomposition Overview\n\nIn HodgeRank, the graph has vertices representing alternatives to be ranked, with voters' preferences quantified as edge flows. Hodge theory provides an orthogonal decomposition of edge flows into three components: a gradient flow that is globally acyclic, a harmonic flow that is locally acyclic but globally cyclic, and a curl flow that is locally cyclic.\n\nThe gradient flow component can be easily computed via a linear least squares problem, avoiding the computational intractability of Kemeny optimization.\n\n## Python Implementation with SciPy\n\nHodgeLaplacians uses sparse matrices `dok_matrix` and `csr_matrix` from the scipy.sparse module. Eigenvalues and eigenvectors are computed using SciPy's ARPACK algorithm.\n\nFor the specific LSQR implementation, LSQR uses an iterative method to approximate the solution, with the number of iterations required depending strongly on the scaling of the problem.\n\n## Practical Example\n\nAn example implementation loads graph and edge values, creates an abstract simplicial complex from edges, and then solves the least squares problem using `scipy.sparse.linalg.lsqr` on the boundary matrix to obtain rankings.\n\nYou can find a comprehensive implementation in the [hodgelaplacians repository](https://github.com/tsitsvero/hodgelaplacians) and original research papers on arXiv for more technical details."], "durationSeconds": 6.865920815000002, "searchCount": 1}
```

### [16] TOOL RESULT — WebSearch · 2026-07-08 23:09:13 UTC

```
{"query": "OpenAlex journal citation network API download journal level citations", "results": [{"tool_use_id": "srvtoolu_013qxwWbSypktL3XTVqt7J8o", "content": [{"title": "OpenAlex Scraper - Scholarly Papers & Citation Data API · Apify", "url": "https://apify.com/jungle_synthesizer/openalex-works-crawler/api"}, {"title": "GitHub - filipinascimento/openalexnet: OpenAlex Networks is a helper library to process and obtain data from the OpenAlex dataset via API. It also provides functionality to generate citation and coauthorship networks from queries. · GitHub", "url": "https://github.com/filipinascimento/openalexnet"}, {"title": "OpenAlex Academic Paper & Research Search API · Apify", "url": "https://apify.com/ryanclinton/openalex-research-search"}, {"title": "OpenAlex Scraper - Scholarly Works, Authors & Citations Graph", "url": "https://orbtop.com/actors/openalex-works-crawler/"}, {"title": "GitHub - oksure/openalex-research-mcp: MCP server for the OpenAlex API — search 240M+ scholarly works, analyze citations, track research trends, and map collaboration networks", "url": "https://github.com/oksure/openalex-research-mcp"}, {"title": "Local Citation Network", "url": "https://localcitationnetwork.github.io/?API=OpenAlex"}, {"title": "'Intelligence Studies Network': A human-curated database for indexing   resources with open-source tools", "url": "https://arxiv.org/pdf/2408.03868"}]}, "Based on the search results, I've found several relevant resources for working with OpenAlex journal citation network data:\n\n## OpenAlex API and Tools\n\nOpenAlex is a free, open catalog of 250M+ scholarly works that can pull citations, open-access status, abstracts, authorships, journals, topics, and more. You can get a free API key at openalex.org/users/me with $1/day of free API credits included.\n\n## Citation Network Generation\n\nIf you're specifically interested in generating citation networks at the journal level, OpenAlex Networks is a helper library that processes OpenAlex dataset data via API and provides functionality to generate citation and coauthorship networks from queries. This library generates gml files for the citation and coauthorship networks.\n\n## Citation Analysis Tools\n\nOpenAlex provides functions to build complete citation networks for visualization, including forward citation analysis (who cites a work) and backward citation analysis (what a work cites).\n\nAdditionally, the Local Citation Network tool allows you to export all data as CSV or RIS files through export features.\n\nThese tools should support your needs for downloading and analyzing journal-level citations from OpenAlex."], "durationSeconds": 6.704624408, "searchCount": 1}
```

### [17] TOOL RESULT — WebSearch · 2026-07-08 23:09:13 UTC

```
{"query": "Clarivate JCR suppressed journals citation stacking list 2018 2019 2020 2021 2022 2023", "results": [{"tool_use_id": "srvtoolu_01PyAKYuRn8y4FvvPM5P6TPs", "content": [{"title": "Journal Citation Reports | Clarivate", "url": "https://clarivate.com/academia-government/scientific-and-academic-research/research-funding-analytics/journal-citation-reports/"}, {"title": "Title Suppressions - Journal Citation Reports - Zendesk", "url": "https://journalcitationreports.zendesk.com/hc/en-gb/articles/28351398819089-Title-Suppressions"}, {"title": "Journal Citation Reports", "url": "https://jcr.clarivate.com/"}, {"title": "A bibliometric investigation of the journals that were repeatedly suppressed from Clarivate's Journal Citation Reports - PubMed", "url": "https://pubmed.ncbi.nlm.nih.gov/35469511/"}, {"title": "Citation issues cost these 20 journals their impact factors this year – Retraction Watch", "url": "https://retractionwatch.com/2025/06/18/clarivate-impact-factor-suppression-list-2025-self-citation-stacking/"}, {"title": "A bibliometric investigation of the journals that were repeatedly suppressed from Clarivate’s Journal Citation Reports: Accountability in Research: Vol 30, No 8", "url": "https://www.tandfonline.com/doi/abs/10.1080/08989621.2022.2071154"}, {"title": "Journal Citation Reports - Clarivate", "url": "https://jcr.clarivate.com/jcr/home"}, {"title": "Ten journals denied 2020 Impact Factors because of excessive self-citation or “citation stacking”", "url": "https://retractionwatch.com/2021/06/30/ten-journals-denied-2020-impact-factors-because-of-excessive-self-citation-or-citation-stacking/"}, {"title": "Impact Factor Denied to 20 Journals For Self-Citation, Stacking - The Scholarly Kitchen", "url": "https://scholarlykitchen.sspnet.org/2018/06/27/impact-factor-denied-20-journals-self-citation-stacking/"}, {"title": "Journal Citation Reports (JCR) – Complete Guide – Scientific News", "url": "https://news.europub.co.uk/journal-citation-reports-jcr-complete-guide/"}]}, "Based on the search results, I found relevant information about Clarivate JCR journal suppressions for citation stacking and self-citation. Here's what the search returned:\n\n## Key Findings:\n\n**What Citation Stacking and Self-Citation Mean:**\nJournals indexed by Clarivate are temporarily suppressed from the Journal Citation Reports (JCR) if their Journal Impact Factor (JIF) scores are distorted through excessive self-citations or citation stacking with other journals.\n\n**2018 Suppressions:**\nClarivate Analytics suppressed 20 journals, 14 for high levels of self-citation and six for citation stacking — a pattern known informally as a \"citation cartel.\"\n\n**2020 Suppressions:**\n21 journals — 10 of which were suppressed, meaning they will not receive an Impact Factor in 2020, and 11 of which received an expression of concern — are fewer than half of the nearly 50 that the company suppressed or subjected to an expression of concern last year.\n\n**Historical Pattern:**\nAn investigation covered the 18 journals that were suppressed three or more times from the JCR. Results indicate that these 18 journals were repeatedly and exclusively suppressed for being excessive self-citers. Together, these 18 journals totaled 65 suppressions.\n\n**Recent 2025 Data:**\nIn 2024, Clarivate suppressed 17 impact factors, a substantial increase from 2023's four.\n\nThe search results reference lists of suppressed journals but don't display the complete detailed lists for each year you requested. You may need to access Clarivate's official JCR documentation directly for comprehensive year-by-year suppression lists."], "durationSeconds": 7.951936189999997, "searchCount": 1}
```

### [18] ASSISTANT · 2026-07-08 23:09:25 UTC

```
Good results. Now let me fetch specific details on CIDRE's API, the JCR suppressed journals list, and the Hodge decomposition math.
```

### [19] TOOL CALL — WebFetch · 2026-07-08 23:09:25 UTC

```
URL: https://github.com/skojaku/cidre
Prompt: Extract: pip install command, main API usage (Python code), key parameters, input format (what the network input looks like), output format (anomaly scores), and any example code
```

### [20] TOOL CALL — WebFetch · 2026-07-08 23:09:25 UTC

```
URL: https://journalcitationreports.zendesk.com/hc/en-gb/articles/28351398819089-Title-Suppressions
Prompt: Extract the complete lists of JCR-suppressed journals by year (2018-2025), including journal names, ISSNs if available, and reasons for suppression
```

### [21] TOOL RESULT — WebFetch · 2026-07-08 23:09:25 UTC

```
{"bytes": 0, "code": 403, "codeText": "Forbidden", "result": "The server returned HTTP 403 Forbidden.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.", "durationMs": 288, "url": "https://journalcitationreports.zendesk.com/hc/en-gb/articles/28351398819089-Title-Suppressions"}
```

### [22] TOOL CALL — WebFetch · 2026-07-08 23:09:25 UTC

```
URL: https://web.stanford.edu/~yyye/hodgeRank2011.pdf
Prompt: Extract: the mathematical formulation of the Hodge decomposition on graphs, specifically (1) the incidence matrix B definition, (2) the least squares problem for the gradient potential s*, (3) the curl decomposition formula, (4) the triangle curl computation, and (5) the three orthogonal components formulas
```

### [23] TOOL CALL — WebFetch · 2026-07-08 23:09:25 UTC

```
URL: https://github.com/filipinascimento/openalexnet
Prompt: Extract the main API for building journal citation networks - what endpoints are called, what data is returned, and how to aggregate journal-level citations
```

### [24] TOOL RESULT — WebFetch · 2026-07-08 23:09:25 UTC

````
{"bytes": 299973, "code": 200, "codeText": "OK", "result": "# CIDRE Package Summary\n\n## Installation\n```bash\npip install cidre\n```\n\n## Main API Usage\n\n```python\nimport cidre\n\nalg = cidre.Cidre(group_membership)\ngroups = alg.detect(A, threshold=0.15)\n```\n\n## Key Parameters\n\n- **group_membership**: Optional numpy array or list indicating which group each node belongs to. Set to `None` if communities aren't known.\n- **A**: Network adjacency matrix (weighted or directed). Accepts NetworkX graphs or scipy sparse CSR matrices where `A[i,j]` represents edge weight from node i to j.\n- **threshold**: Controls detection sensitivity. Higher values produce smaller, tighter anomalous groups.\n\n## Input Format\n\nThe network is represented as an adjacency matrix in either:\n- NetworkX graph format\n- Scipy sparse CSR matrix format\n\n## Output Format\n\nReturns a list of `Group` objects representing anomalous donor-recipient clusters. Each group contains:\n\n```python\ngroup.donors        # Dictionary: {node_id: donor_score}\ngroup.recipients    # Dictionary: {node_id: recipient_score}\ngroup.size()        # Number of nodes\ngroup.get_within_edges()  # Edge count within group\n```\n\n## Key Concept\n\n\"An anomalous group consists of donor and recipient nodes, connected by edges with excessive edge weights.\"", "durationMs": 5153, "url": "https://github.com/skojaku/cidre"}
````

### [25] TOOL RESULT — WebFetch · 2026-07-08 23:09:29 UTC

```
{"bytes": 330975, "code": 200, "codeText": "OK", "result": "# OpenAlex Journal Citation Network API\n\nBased on the repository documentation, here's how the library builds citation networks:\n\n## Primary Data Source\n\nThe library queries the **OpenAlex API** using four main parameters:\n- `entitytype`: Set to \"works\" for journal articles\n- `filter`: Narrows results (e.g., `\"type:journal-article\"`)\n- `search`: Text-based matching across titles and abstracts\n- `sort`: Orders results by metrics like citation count\n\n## Data Retrieved\n\nThe API returns work objects containing citation metadata. The library preserves attributes including `\"id, doi, title, display_name, publication_year, publication_date, type, authorships, concepts, host_venue\"` for network construction.\n\n## Citation Network Generation\n\nThe tool creates directed networks by:\n1. Retrieving works matching your query criteria\n2. Extracting citation relationships between documents\n3. Exporting in formats like GML, edgelist, or xnet\n\nAs the documentation states, users can `\"generate citation and coauthorship networks from queries.\"` The citation file parameter (`-c`) automatically builds these networks from retrieved entities.\n\n## Aggregation Method\n\nMultiple queries combine results across different searches, allowing researchers to merge citation patterns from distinct author or topic searches into unified network files for analysis.", "durationMs": 6153, "url": "https://github.com/filipinascimento/openalexnet"}
```

### [26] TOOL RESULT — WebFetch · 2026-07-08 23:09:35 UTC

```
{"bytes": 661590, "code": 200, "codeText": "OK", "result": "I cannot extract the requested mathematical formulations from the provided content. The web page appears to be a corrupted or improperly encoded PDF document containing binary data, garbled streams, and object references rather than readable text.\n\nThe content shows PDF structural elements (objects, streams, filters) but lacks intelligible mathematical notation, formulas, or coherent text that would contain:\n- A definition of the incidence matrix B\n- The least squares problem formulation\n- Curl decomposition equations\n- Triangle curl computations\n- Orthogonal component formulas\n\nTo obtain this information, you would need to provide either:\n1. A properly decoded version of the PDF\n2. The raw text or LaTeX source of the academic paper\n3. A direct link to an accessible document repository\n\nIf you have access to the original paper on Hodge decomposition on graphs, sharing the title or authors would help identify the correct source material.\n\n[Binary content (application/pdf, 646.1KB) also saved to /root/.claude/projects/-ai-inventor-aii-data-runs-run-io13l-LyCX8s-3-invention-loop-iter-1-gen-plan-gen-plan-experiment-1/f0a83916-0947-4834-b386-4a1c21fd630b/tool-results/webfetch-1783552169484-6314fq.pdf]", "durationMs": 11969, "url": "https://web.stanford.edu/~yyye/hodgeRank2011.pdf"}
```

### [27] TOOL CALL — WebFetch · 2026-07-08 23:09:46 UTC

```
URL: https://retractionwatch.com/2025/06/18/clarivate-impact-factor-suppression-list-2025-self-citation-stacking/
Prompt: Extract the complete list of suppressed journals with names, ISSNs, and years suppressed
```

### [28] TOOL CALL — WebFetch · 2026-07-08 23:09:46 UTC

```
URL: https://github.com/skojaku/journal-citation-cartels
Prompt: What data is in this repo? Is there a journal citation network (adjacency matrix or edge list), JCR suppressed journal list, and CIDRE code? What format are the data files in?
```

### [29] TOOL CALL — WebSearch · 2026-07-08 23:09:46 UTC

```
CIDRE journal-citation-cartels dataset MAG journal citation network download
```

### [30] TOOL CALL — WebSearch · 2026-07-08 23:09:46 UTC

```
Hodge decomposition graph python networkx combinatorial curl computation triangle
```

### [31] TOOL RESULT — WebFetch · 2026-07-08 23:09:50 UTC

```
{"bytes": 315852, "code": 200, "codeText": "OK", "result": "Based on the repository content, here's what's included:\n\n**Data Files:**\nThe README doesn't specify pre-existing data files in the repo. Instead, it describes a workflow for generating journal citation networks from raw data sources.\n\n**CIDRE Code:**\nYes, the algorithm code is present. The repository contains \"the library including the CIDRE algorithm\" located in the `libs` directory, specifically under `libs/cidre`.\n\n**Network Data:**\nThe workflow demonstrates how to create citation networks by:\n- Downloading the Microsoft Academic Graph\n- Importing data into Neo4j database\n- \"Generate files for journal citation networks\"\n\n**File Formats:**\nThe documentation mentions that the CIDRE algorithm works with \"scipy.sparse matrix\" for adjacency matrices and \"pandas data frame\" for results, but doesn't specify input file formats like CSV or JSON.\n\n**JCR Suppressed Journal List:**\nNo mention of this dataset in the README.\n\n**Summary:**\nThis appears to be a code repository rather than a data repository. It provides the algorithm and workflow pipeline, but you'd need to separately obtain the Microsoft Academic Graph data to run the complete analysis.", "durationMs": 4459, "url": "https://github.com/skojaku/journal-citation-cartels"}
```

### [32] TOOL RESULT — WebFetch · 2026-07-08 23:09:50 UTC

```
{"bytes": 117668, "code": 200, "codeText": "OK", "result": "# Suppressed Journals List (2025)\n\nBased on the article, here are the 20 journals that lost their impact factors in 2025:\n\n| Journal Title | Publisher | Reason |\n|---|---|---|\n| Advances and Applications in Discrete Mathematics | Pushpa Publishing House | Self-citation |\n| Annals of Phytomedicine-An International Journal | Ukaaz Publications | Self-citation |\n| Applied Organometallic Chemistry | Wiley | Citation stacking |\n| Asian Journal of Agriculture and Biology | Life Sciences Society, Pakistan | Citation stacking |\n| Chemical Methodologies | Sami Publishing Co. | Citation stacking |\n| Clinical Hemorheology and Microcirculation | Sage Publications | Self-citation |\n| Genetic Resources and Crop Evolution | Springer | Citation stacking |\n| Indian Journal of Biochemistry & Biophysics | National Institute Of Science Communication and Policy Research | Self-citation |\n| Jordan Journal of Mechanical and Industrial Engineering | Hashemite University | Self-citation |\n| Journal of Earthquake and Tsunami | World Scientific Publishing Co. | Self-citation |\n| Journal of Mind and Medical Sciences | MDPI | Self-citation |\n| Lobachevskii Journal of Mathematics | MAIK Nauka/Interperiodica, Springer | Self-citation |\n| Mechanics of Advanced Materials and Structures | Taylor & Francis | Self-citation |\n| Media Education (Mediaobrazovanie) | Cherkas Global University Press | Self-citation |\n| Punjab University Journal of Mathematics | University of the Punjab | Self-citation |\n| Russian Chemical Bulletin | Springer | Self-citation |\n| Russian Journal of Physical Chemistry B | MAIK Nauka/Interperiodica, Springer | Self-citation |\n| TeMA – Journal of Land Use Mobility and Environment | University of Naples | Self-citation |\n| Transactions of FAMENA | University of Zagreb | Self-citation |\n| Vestnik St. Petersburg University, Mathematics | Pleiades Publishing, Springer | Self-citation |\n\n**Note:** The article does not include ISSN numbers or specific suppression years beyond the 2025 timeframe mentioned.", "durationMs": 7034, "url": "https://retractionwatch.com/2025/06/18/clarivate-impact-factor-suppression-list-2025-self-citation-stacking/"}
```

### [33] TOOL RESULT — WebSearch · 2026-07-08 23:09:50 UTC

```
{"query": "CIDRE journal-citation-cartels dataset MAG journal citation network download", "results": [{"tool_use_id": "srvtoolu_01HxvvbLKcQoHNRW78jqm5CZ", "content": [{"title": "Detecting citation cartels in journal networks", "url": "https://www.arxiv.org/pdf/2009.09097v1"}, {"title": "Detecting anomalous citation groups in journal networks", "url": "https://arxiv.org/pdf/2009.09097"}, {"title": "(PDF) Detecting citation cartels in journal networks", "url": "https://www.researchgate.net/publication/344334965_Detecting_citation_cartels_in_journal_networks"}, {"title": "(PDF) Detecting anomalous citation groups in journal networks", "url": "https://www.researchgate.net/publication/353266793_Detecting_anomalous_citation_groups_in_journal_networks"}, {"title": "Detecting anomalous citation groups in journal networks - PMC", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8282695/"}, {"title": "Detecting anomalous citation groups in journal networks | Scientific Reports", "url": "https://www.nature.com/articles/s41598-021-93572-3"}, {"title": "Mining the online infosphere: A survey", "url": "https://arxiv.org/pdf/2101.00454"}, {"title": "Detecting anomalous citation groups in journal networks", "url": "https://ouci.dntb.gov.ua/en/works/4Man3Xd4/"}]}, "Based on the search results, here's what I found about the CIDRE journal-citation-cartels dataset:\n\n## Overview\n\nCIDRE is an algorithm to detect anomalous groups of journals that exchange citations at excessively high rates when compared against a null model that accounts for scientific communities and journal size.\n\n## Dataset\n\nThe dataset uses a snapshot of Microsoft Academic Graph (MAG) released on January 30th, 2020, and contains bibliographic information including citations among 231,926,308 papers published from 48,821 journals in various research fields.\n\n## Code Availability\n\nThe Python code for CIDRE is available at GitHub.\n\n## Performance\n\nCIDRE detects more than half of the journals suspended from Journal Citation Reports due to anomalous citation behavior in the year of suspension or in advance.\n\nThe research has been published in *Scientific Reports* and is also available on arXiv. If you need more specific information about downloading the dataset or accessing the GitHub repository with the code, you may want to refer directly to the paper's supplementary materials or the GitHub link referenced as \"GitHub23\" in the publications."], "durationSeconds": 5.569105994999998, "searchCount": 1}
```

### [34] TOOL RESULT — WebSearch · 2026-07-08 23:09:50 UTC

```
{"query": "Hodge decomposition graph python networkx combinatorial curl computation triangle", "results": [{"tool_use_id": "srvtoolu_01UJ7td4HgMC8FLTR71ndxWC", "content": [{"title": "Disentangling Large-Scale Supply Networks: f-HiCoNE Framework for Flow-Hierarchical Clustering via Combinatorial Hodge Decomposition", "url": "https://arxiv.org/pdf/2604.04538"}, {"title": "Decentralized Trajectory Tracking Using Homology and Hodge Decomposition   in Sensor Networks", "url": "https://arxiv.org/pdf/1708.09129"}, {"title": "Brain Networks Flow-Topology via Variance Minimization in the Wasserstein Space", "url": "https://arxiv.org/pdf/2511.12990"}, {"title": "Graph-Hodge-decomposition/Graph_Hodge_decomposition_adjacency_mat.ipynb at main · yusuke-imoto-lab/Graph-Hodge-decomposition", "url": "https://github.com/yusuke-imoto-lab/Graph-Hodge-decomposition/blob/main/Graph_Hodge_decomposition_adjacency_mat.ipynb"}, {"title": "Hodge Decomposition for Urban Traffic Flow: Limits on Dense OD Graphs and Advantages on Road Networks - Los Angeles Case", "url": "https://arxiv.org/pdf/2509.17203"}, {"title": "Hodge Decomposition of Information Flow on Small-World Networks", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5039183/"}, {"title": "The Covariate-Assisted Bayesian Intransitive Bradley-Terry Model via Combinatorial Hodge Theory", "url": "https://arxiv.org/pdf/2601.07158"}, {"title": "A Hodge-Based Framework for Service Operational Analysis in Serverless Platforms", "url": "https://arxiv.org/pdf/2603.08192"}, {"title": "Helmholtz-Hodge Decomposition on Graphs", "url": "https://www.researchgate.net/publication/387053631_Helmholtz-Hodge_Decomposition_on_Graphs"}]}, "I found several relevant results about Hodge decomposition on graphs. Here's what the search revealed:\n\n## Key Concepts\n\nThe combinatorial gradient, curl, and divergence are defined as: gradient (s_j - s_i), curl (Y_ij + Y_jk + Y_ki for triangles), and divergence (sum of Y_ij over edges).\n\nThe combinatorial Hodge theory enables decomposition of any flow on a network into three mutually orthogonal components: gradient, harmonic and curl flows.\n\n## Theoretical Framework\n\nThe combinatorial Hodge decomposition takes the form: edge space = image(grad) ⊕ kernel(Δ₁) ⊕ image(curl*), where Δ₁ = grad ∘ grad* + curl* ∘ curl.\n\nThree spaces are defined on the graph: node space, edge space, and triangle space, corresponding to 0-simplicial complex, 1-simplicial complex, and 2-simplicial complex in algebraic topology.\n\n## Application\n\nCombinatorial Hodge theory can decompose information flow on networks into three components: gradient, harmonic and curl flows, with harmonic and curl flows representing globally circular and locally circular components, respectively.\n\nThere's also a GitHub repository (result index 4) that contains NetworkX implementations for graph Hodge decomposition using adjacency matrices, though the snippet was limited."], "durationSeconds": 6.468985575999999, "searchCount": 1}
```

### [35] ASSISTANT · 2026-07-08 23:10:00 UTC

```
Excellent. Let me now fetch the key implementation details for the Hodge decomposition and the JCR suppressed journal data.
```

### [36] TOOL CALL — WebFetch · 2026-07-08 23:10:00 UTC

```
URL: https://github.com/yusuke-imoto-lab/Graph-Hodge-decomposition/blob/main/Graph_Hodge_decomposition_adjacency_mat.ipynb
Prompt: Extract the Python code for computing the Hodge decomposition from an adjacency matrix - specifically the incidence matrix B construction, the gradient potential solve (lsqr), and curl/triangle computation
```

### [37] TOOL CALL — WebFetch · 2026-07-08 23:10:00 UTC

```
URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC8282695/
Prompt: Extract: (1) the journal citation network construction methodology (time window, aggregation), (2) the exact input format for CIDRE, (3) which JCR years are used as ground truth and how many journals were suppressed, (4) performance metrics reported (AUC, precision@k)
```

### [38] TOOL CALL — WebSearch · 2026-07-08 23:10:00 UTC

```
OpenAlex API journal level citation counts aggregate "cited_by_count" "primary_location" source venue filter 2020
```

### [39] TOOL RESULT — WebFetch · 2026-07-08 23:10:00 UTC

```
{"bytes": 276189, "code": 200, "codeText": "OK", "result": "I appreciate your request, but I cannot extract the Python code you're asking for based on the provided content. The webpage content shows only the GitHub repository navigation, metadata, and UI elements—it does not contain the actual notebook code or implementation details.\n\nThe page displays:\n- Repository header information for \"yusuke-imoto-lab/Graph-Hodge-decomposition\"\n- File path: \"Graph_Hodge_decomposition_adjacency_mat.ipynb\"\n- File statistics: \"185 lines (185 loc) · 42.1 KB\"\n\nHowever, the actual notebook content itself—including the incidence matrix construction, lsqr solver implementation, and curl/triangle computations—is not rendered in the provided text.\n\n**To access this code, you would need to:**\n\n1. Visit the GitHub repository directly and view the raw notebook file\n2. Download the `.ipynb` file and open it in Jupyter\n3. Use GitHub's raw file viewer to see the JSON notebook structure\n\nIf you can provide the actual notebook code content, I'd be happy to extract and summarize the specific implementations you're seeking.", "durationMs": 3749, "url": "https://github.com/yusuke-imoto-lab/Graph-Hodge-decomposition/blob/main/Graph_Hodge_decomposition_adjacency_mat.ipynb"}
```

### [40] TOOL RESULT — WebSearch · 2026-07-08 23:10:06 UTC

```
{"query": "OpenAlex API journal level citation counts aggregate \"cited_by_count\" \"primary_location\" source venue filter 2020", "results": [{"tool_use_id": "srvtoolu_0115T6Go7WZmQJCXEbfWkA7K", "content": [{"title": "API Overview - OpenAlex Developers", "url": "https://developers.openalex.org/api-reference/introduction"}, {"title": "Total works and cites don't match sums in counts by year", "url": "https://groups.google.com/g/openalex-community/c/1gUorSyDGT8"}, {"title": "Source object | OpenAlex technical documentation", "url": "https://docs.openalex.org/api-entities/sources/source-object"}, {"title": "Count incoming citations to any results set – OpenAlex", "url": "https://help.openalex.org/hc/en-us/articles/24830109246615-Count-incoming-citations-to-any-results-set"}, {"title": "openalex-api-tutorials/notebooks/authors/hirsch-index.ipynb at main · ourresearch/openalex-api-tutorials", "url": "https://github.com/ourresearch/openalex-api-tutorials/blob/main/notebooks/authors/hirsch-index.ipynb"}, {"title": "Getting Bibliographic Records from OpenAlex Database Using DSL API • openalexR", "url": "https://docs.ropensci.org/openalexR/"}, {"title": "OpenAlex API Examples", "url": "https://science-as-data.github.io/openalex/"}, {"title": "OpenAlex citation counts · GitHub", "url": "https://gist.github.com/caseydm/f999f8462d0d432e63fecbc52588ceb8"}, {"title": "Institution object | OpenAlex technical documentation", "url": "https://docs.openalex.org/api-entities/institutions/institution-object"}, {"title": "How much is my institution’s work cited?", "url": "https://help.openalex.org/hc/en-us/articles/24346743922071-How-much-is-my-institution-s-work-cited"}]}, "I've completed the web search for your query about the OpenAlex API with journal-level citation counts, aggregation, and filtering. Here are the key findings:\n\n## OpenAlex API Citation Count Functionality\n\nOpenAlex provides `works_count` and `cited_by_count` for each of the last ten years, binned by year, allowing you to see how many new works a source hosted and how many times any work in that source was cited.\n\n### Citation Count Field\n\nThe primary location block tells you where the work was published — journal name, ISSN, license, and version. Citation metrics include the raw count, field-weighted citation impact (FWCI), normalised percentile rankings, and a year-by-year breakdown.\n\n### Aggregation Considerations\n\nWhen aggregating citation numbers, OpenAlex sums individual `cited_by` values for each article, meaning if one article references multiple papers, each referenced paper gets counted as cited_by 1, and the sum differs from the count of citing articles.\n\n### Filtering and Sorting\n\nYou can filter entities by various parameters and retrieve records matching your query. The API supports filters for publication year and other metadata fields to narrow down results.\n\nThe total number of Works that cite a Work hosted in a source is captured in the source object, making it useful for journal-level citation analysis."], "durationSeconds": 6.458640585000001, "searchCount": 1}
```

### [41] TOOL RESULT — WebFetch · 2026-07-08 23:10:06 UTC

```
{"bytes": 208607, "code": 200, "codeText": "OK", "result": "# CIDRE: Citation Network Analysis Methodology\n\n## (1) Journal Citation Network Construction\n\n**Time Window & Aggregation:**\nThe researchers constructed directed weighted networks for each year between 2000-2019. Edge weights represent \"citations from papers published in [journal i] to papers published in [journal j] made in the time window used for calculating the JIF, i.e., last 2 years.\" For null model fitting, they created an aggregated network by summing citations across all years: W̄ᵢⱼ = Σ(2000-2019) Wᵢⱼ(t).\n\n## (2) CIDRE Input Format\n\nThe algorithm operates on directed weighted citation networks where:\n- **Nodes** = journals\n- **Edge weights** = citation counts between journals\n- **Processed through** a degree-corrected stochastic block model (dcSBM) to identify research field blocks\n- Output identifies \"groups of journals with excessive within-group citations relative to the null model\"\n\n## (3) Ground Truth Dataset\n\n**JCR Suspension Data (2007-2019):**\n- Total: 227 journals suspended due to excessive citations\n- 173 journals suspended for self-citations\n- 55 journals suspended for excessive pairwise citations\n- 1 journal suspended for both\n- **22 merged journal groups** identified from 46 pairs with excessive pairwise citations used for validation\n\n## (4) Performance Metrics Reported\n\nThe paper does **not report standard performance metrics** (AUC, precision@k). Instead, it uses:\n- **Overlap metric**: O = |U^JCR ∩ U^CI| / |U^CI| (≥0.5 with ≥2 shared journals = detection)\n- **Detection rate**: 12 of 22 JCR groups detected (55%); 10 groups detected before JCR suspension", "durationMs": 7575, "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8282695/"}
```

### [42] ASSISTANT · 2026-07-08 23:10:12 UTC

```
Let me get the CIDRE paper's specific details and the circular flow decomposition papers.
```

### [43] TOOL CALL — WebFetch · 2026-07-08 23:10:12 UTC

```
URL: https://arxiv.org/abs/2009.09097
Prompt: Extract: (1) the exact citation network they use (journal-level, time window used), (2) their null model details, (3) their performance on the JCR ground truth data (detection rates), (4) any data they make publicly available
```

### [44] TOOL CALL — WebSearch · 2026-07-08 23:10:12 UTC

```
OpenAlex snapshot parquet journal citation matrix download bulk data 2023 2024
```

### [45] TOOL CALL — WebSearch · 2026-07-08 23:10:12 UTC

```
"circular flow decomposition" OR "helmholtz hodge" citation network anomaly detection graph python 2024 2025
```

### [46] TOOL RESULT — WebFetch · 2026-07-08 23:10:16 UTC

```
{"bytes": 43017, "code": 200, "codeText": "OK", "result": "# Citation Network Study: Key Details\n\nBased on the arXiv page provided, here's what's available:\n\n## (1) Citation Network Details\nThe page doesn't specify the exact journal-level network composition or time window. Only the abstract mentions the research involves \"journal networks\" and detection of \"citation cartels.\"\n\n## (2) Null Model Details\nThe abstract indicates their CIDRE algorithm uses \"a null model that accounts for scientific communities and journal size,\" but specific mathematical formulation isn't detailed on this page.\n\n## (3) Performance on JCR Ground Truth\nThe abstract reports: \"CIDRE detects more than half of the journals suspended from Journal Citation Reports due to anomalous citation behavior in the year of suspension or in advance.\"\n\n## (4) Publicly Available Data\nThe page provides:\n- PDF access to the full paper\n- TeX source code available\n- Published in Scientific Reports (2021)\n- DOI: https://doi.org/10.1038/s41598-021-93572-3\n\n**Note:** For complete methodology details, null model specifications, and any supplementary datasets, you'd need to access the full paper PDF or supplementary materials linked through the published journal article.", "durationMs": 4688, "url": "https://arxiv.org/abs/2009.09097"}
```

### [47] TOOL RESULT — WebSearch · 2026-07-08 23:10:19 UTC

```
{"query": "OpenAlex snapshot parquet journal citation matrix download bulk data 2023 2024", "results": [{"tool_use_id": "srvtoolu_01M3UTnhX6SWuTBQi1RJfMyX", "content": [{"title": "Snapshot data format - OpenAlex Developers", "url": "https://docs.openalex.org/download-all-data/openalex-snapshot"}, {"title": "Systemic Gendered Citation Imbalance in Computer Science: Evidence from Conferences and Journals", "url": "https://arxiv.org/pdf/2603.23273"}, {"title": "Understanding discrepancies in the coverage of OpenAlex: the case of China", "url": "https://arxiv.org/pdf/2507.19302"}, {"title": "OpenAlex Snapshot | Zenodo", "url": "https://zenodo.org/records/13941458"}, {"title": "The Tilted Playing Field for Women in Science", "url": "https://arxiv.org/pdf/2606.26469"}, {"title": "Analysing the coverage of the University of Bologna's bibliographic and citation metadata in OpenCitations collections", "url": "https://arxiv.org/pdf/2501.05821"}, {"title": "Usage of OpenAlex for creating meaningful global overlay maps of science   on the individual and institutional levels", "url": "https://arxiv.org/pdf/2404.02732"}, {"title": "The OpenCitations Index", "url": "https://arxiv.org/pdf/2408.02321"}, {"title": "Atlas of Science Collaboration, 1971-2020", "url": "https://arxiv.org/pdf/2308.16810"}, {"title": "OpenAlex2Pajek -- an R Package for converting OpenAlex bibliographic   data into Pajek networks", "url": "https://arxiv.org/pdf/2501.06656"}]}, "Based on the search results, here's what I found about OpenAlex snapshot parquet data and bulk data downloads:\n\n## OpenAlex Snapshot Data Format\n\nThe Parquet copy is provided alongside JSONL formats, and if you only need one format, you can download a single format prefix.\n\n## Update Frequency and Access\n\nThe free public snapshot is refreshed quarterly, while a daily-refreshed snapshot and daily change files require a paid plan. Additionally, OpenAlex currently provides snapshots once a month.\n\n## Download Instructions\n\nInformation on how to download the entire data snapshot for OpenAlex can be found at: https://docs.openalex.org/download-all-data/openalex-snapshot\n\n## Recent Snapshot Versions\n\nSeveral studies have used different snapshots from 2023-2024:\n- The August 2023 snapshot contained 243,053,925 documents\n- The June 30th, 2024 snapshot contains a total of 256,997,006 scholarly works\n\n## Data Contents\n\nOpenAlex is an open, comprehensive index of scholarly papers, citations, authors, institutions, and journals.\n\nFor specific information about journal citation matrices, the search results don't provide detailed documentation on that particular feature, but the official documentation at docs.openalex.org would have comprehensive details about available data entities and formats."], "durationSeconds": 6.731811532000007, "searchCount": 1}
```

### [48] TOOL RESULT — WebSearch · 2026-07-08 23:10:21 UTC

```
{"query": "\"circular flow decomposition\" OR \"helmholtz hodge\" citation network anomaly detection graph python 2024 2025", "results": [{"tool_use_id": "srvtoolu_015Vw7tTKKY2AkCfMpUkAPaS", "content": [{"title": "Regional economic integration via detection of circular flow in   international value-added network", "url": "https://arxiv.org/pdf/2103.08179"}, {"title": "Causal Hierarchy in the Financial Market Network -- Uncovered by the   Helmholtz-Hodge-Kodaira Decomposition", "url": "https://arxiv.org/pdf/2408.12839"}, {"title": "Identifying the Hierarchical Influence Structure Behind Smart Sanctions   Using Network Analysis", "url": "https://arxiv.org/pdf/1909.00847"}, {"title": "GitHub - bhatiaharsh/naturalHHD: The natural Helmholtz-Hodge decomposition · GitHub", "url": "https://github.com/bhatiaharsh/naturalHHD"}, {"title": "Helmholtz-Hodge Decomposition on Graphs", "url": "https://www.researchgate.net/publication/387053631_Helmholtz-Hodge_Decomposition_on_Graphs"}, {"title": "Do economic effects of the anti-COVID-19 lockdowns in different regions   interact through supply chains?", "url": "https://arxiv.org/pdf/2009.06894"}, {"title": "Topological Effective Connectivity Modeling in Brain Networks", "url": "https://arxiv.org/pdf/2606.08407"}, {"title": "(PDF) HLSAD: Hodge Laplacian-based Simplicial Anomaly Detection", "url": "https://www.researchgate.net/publication/392314660_HLSAD_Hodge_Laplacian-based_Simplicial_Anomaly_Detection"}, {"title": "The Helmholtz-Hodge Decomposition—A Survey", "url": "https://www.sci.utah.edu/~hbhatia/pubs/2013_TVCG_survey.pdf"}, {"title": "Network sampling based path decomposition and anomaly detection", "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10205734"}]}, "I found relevant results for your search. Here's what the web search revealed:\n\n## Key Findings\n\n**Helmholtz-Hodge Decomposition (HHD) and Circular Flow:**\n\nHelmholtz–Hodge decomposition is used to extract potential and circular relationships from networks. The flow from node i to node j can be separated into circular flow and potential flow components.\n\nCircular flow corresponds to feedback loops inherent in networks, while gradient flow represents the hierarchical component where information flows from nodes with higher potentials to nodes with lower ones.\n\n**Recent Applications (2024-2025):**\n\nA recent approach (HLSAD - Hodge Laplacian-based Simplicial Anomaly Detection) leverages the spectral properties of Hodge Laplacians of simplicial complexes to model multi-way interactions, enhancing both detection accuracy and computational efficiency in anomaly detection.\n\nThe Helmholtz-Hodge-Kodaira Decomposition is a tool to analyze flux in networks and disentangle the flow into upstream and downstream directions.\n\n**Python Implementation:**\n\nThere are C++ and Python libraries available to compute the natural HHD, with Python tools for computation on regular/rectangular grids and simplicial meshes.\n\nThe search results show active research combining these mathematical tools with graph-based anomaly detection, particularly using higher-order topological structures."], "durationSeconds": 7.670549629000001, "searchCount": 1}
```

### [49] ASSISTANT · 2026-07-08 23:10:31 UTC

```
Let me get a few more key implementation details on the circular flow approach and the CIDRE data.
```

### [50] TOOL CALL — WebFetch · 2026-07-08 23:10:31 UTC

```
URL: https://docs.openalex.org/download-all-data/openalex-snapshot
Prompt: Extract: (1) the S3 bucket URL or download mechanism for journal-level citation data, (2) the schema/columns available in the works entity (especially source/journal fields and referenced_works), (3) estimated data size for works table, (4) whether there's a direct journal-journal citation matrix available
```

### [51] TOOL RESULT — WebFetch · 2026-07-08 23:10:31 UTC

```
{"bytes": 698, "code": 301, "codeText": "Moved Permanently", "result": "REDIRECT DETECTED: The URL redirects to a different host.\n\nOriginal URL: https://docs.openalex.org/download-all-data/openalex-snapshot\nRedirect URL: https://developers.openalex.org/\nStatus: 301 Moved Permanently\n\nTo complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:\n- url: \"https://developers.openalex.org/\"\n- prompt: \"Extract: (1) the S3 bucket URL or download mechanism for journal-level citation data, (2) the schema/columns available in the works entity (especially source/journal fields and referenced_works), (3) estimated data size for works table, (4) whether there's a direct journal-journal citation matrix available\"", "durationMs": 253, "url": "https://docs.openalex.org/download-all-data/openalex-snapshot"}
```

### [52] TOOL CALL — WebFetch · 2026-07-08 23:10:31 UTC

```
URL: https://www.researchgate.net/publication/392314660_HLSAD_Hodge_Laplacian-based_Simplicial_Anomaly_Detection
Prompt: Extract: (1) the mathematical formulation of the anomaly score using Hodge Laplacian, (2) how triangle-level curl is computed, (3) Python implementation details or pseudocode
```

### [53] TOOL RESULT — WebFetch · 2026-07-08 23:10:31 UTC

```
{"bytes": 0, "code": 403, "codeText": "Forbidden", "result": "The server returned HTTP 403 Forbidden.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.", "durationMs": 317, "url": "https://www.researchgate.net/publication/392314660_HLSAD_Hodge_Laplacian-based_Simplicial_Anomaly_Detection"}
```

### [54] TOOL CALL — WebSearch · 2026-07-08 23:10:31 UTC

```
retractionwatch JCR suppressed journals complete list 2018 2019 2020 2021 2022 ISSN citation stacking
```

### [55] TOOL RESULT — WebSearch · 2026-07-08 23:10:37 UTC

```
{"query": "retractionwatch JCR suppressed journals complete list 2018 2019 2020 2021 2022 ISSN citation stacking", "results": [{"tool_use_id": "srvtoolu_017hJLo2jvrseZen5hqSd2Qw", "content": [{"title": "Title Suppressions - Journal Citation Reports - Zendesk", "url": "https://journalcitationreports.zendesk.com/hc/en-gb/articles/28351398819089-Title-Suppressions"}, {"title": "The Retraction Watch Hijacked Journal Checker – Retraction Watch", "url": "https://retractionwatch.com/the-retraction-watch-hijacked-journal-checker/"}, {"title": "JCR 2025: Excluding Retraction Citations to Reinforce Integrity", "url": "https://clarivate.com/academia-government/blog/journal-citation-reports-2025-addressing-retractions-and-strengthening-research-integrity/"}, {"title": "Major indexing service rejects appeals by two suppressed journals – Retraction Watch", "url": "https://retractionwatch.com/2020/08/28/major-indexing-service-rejects-appeals-by-two-suppressed-journals/"}, {"title": "Title Suppressions - Journal Citation Reports - Clarivate", "url": "https://jcr.help.clarivate.com/Content/title-suppressions.htm"}, {"title": "Journal Citation Reports Editorial Expression of Concern", "url": "https://retractionwatch.com/wp-content/uploads/2020/06/2020-JCR-Editorial-Expression-of-Concern-FINAL-SENT-1-2.pdf"}, {"title": "Title Suppressions Editorial Expression of Concern", "url": "https://retractionwatch.com/wp-content/uploads/2020/06/Title-Suppress-2.pdf"}, {"title": "A bibliometric investigation of the journals that were repeatedly suppressed from Clarivate’s Journal Citation Reports: Accountability in Research: Vol 30, No 8", "url": "https://www.tandfonline.com/doi/abs/10.1080/08989621.2022.2071154"}, {"title": "Retraction Watch Revisited – Inside Science Resources", "url": "https://insidescienceresources.wordpress.com/2022/06/16/retraction-watch-revisited/"}, {"title": "Retraction Watch – Tracking retractions as a window into the scientific process", "url": "https://retractionwatch.com/"}]}, "Based on the search results, I found relevant information about JCR-suppressed journals related to citation stacking and self-citations. Here's what I found:\n\n## JCR Suppressed Journals - Citation Stacking\n\nThree journals were suppressed from the JCR for citation stacking: Nanoscience and Nanotechnology Letters, Journal of Biobased Materials and Bioenergy, and Journal of Biomedical Nanotechnology. Bone Research also had its metrics distorted by citation stacking from these journals, preventing accurate 2018 JCR citation data publication, though the title was not listed in the JCR that year.\n\n## General Suppression Information\n\nClarivate has been suppressing the Journal Impact Factor (JIF) for journals showing signs of anomalous citation behavior since the 2008 release. In July 2020, Clarivate suppressed 33 journals from its Journal Citation Reports, meaning they would not have a 2019 Impact Factor, because of excessive self-citation.\n\nA bibliometric investigation found that 18 journals were suppressed three or more times from the JCR, and these journals were repeatedly and exclusively suppressed for being excessive self-citers, with the 18 journals totaling 65 suppressions.\n\nThe search results reference PDF documents with complete suppression lists but don't provide the full detailed lists for each year (2018-2022) with specific ISBNs in the search excerpts. The official Clarivate JCR suppression page mentioned in the results would contain more comprehensive historical data."], "durationSeconds": 8.064281912999999, "searchCount": 1}
```

### [56] TOOL CALL — WebFetch · 2026-07-08 23:10:51 UTC

```
URL: https://jcr.help.clarivate.com/Content/title-suppressions.htm
Prompt: Extract the complete list of suppressed journals by year, including journal names, ISSNs, and whether suppressed for self-citation or citation stacking. Focus on 2018-2023.
```

### [57] TOOL RESULT — WebFetch [ERROR] · 2026-07-08 23:10:51 UTC

```
Error: getaddrinfo ENOTFOUND jcr.help.clarivate.com
```

### [58] TOOL CALL — WebFetch · 2026-07-08 23:10:51 UTC

```
URL: https://arxiv.org/pdf/2604.04538
Prompt: Extract: (1) exact steps to compute combinatorial Hodge decomposition on a directed weighted graph: incidence matrix B, gradient potential lsqr solve, curl projection, triangle enumeration, (2) any Python code snippets, (3) how the curl component is computed for triangles
```

### [59] TOOL RESULT — WebFetch · 2026-07-08 23:10:51 UTC

```
{"bytes": 2841878, "code": 200, "codeText": "OK", "result": "# Combinatorial Hodge Decomposition on Directed Weighted Graphs\n\nBased on the PDF content provided, here's what I can extract about the computational framework:\n\n## Steps for Combinatorial Hodge Decomposition\n\nThe document describes decomposing flows in directed weighted graphs into three components:\n\n1. **Incidence Matrix Construction**: Build the boundary operator matrix B from graph topology, representing edges and their incident nodes.\n\n2. **Gradient Component**: Solve a least-squares problem to find potential values that explain flow as gradients. The document references using \"lsqr solve\" methodology to recover potential differences across edges.\n\n3. **Curl Component**: Identify circulation patterns by enumerating triangles (3-cycles) in the graph and computing their contribution to non-conservative flow.\n\n4. **Triangle Enumeration**: Systematically identify all 3-node cycles to capture local rotational flow patterns.\n\n## Python Implementation\n\nWhile the PDF contains compressed PDF stream objects rather than readable code snippets, the framework is called **f-HiCoNE** (flow-hierarchical clustering via combinatorial Hodge decomposition), suggesting implementations would use standard numerical libraries (NumPy, SciPy) for matrix operations.\n\n## Curl Computation\n\nThe curl component captures flow that doesn't stem from potential differences—essentially measuring \"rotational\" behavior. For triangles, this involves summing directed edge flows around 3-cycles and normalizing by the triangle's properties.\n\nThe method appears designed specifically for supply chain network analysis, decomposing complex flow patterns into interpretable hierarchical structures.\n\n[Binary content (application/pdf, 2.7MB) also saved to /root/.claude/projects/-ai-inventor-aii-data-runs-run-io13l-LyCX8s-3-invention-loop-iter-1-gen-plan-gen-plan-experiment-1/f0a83916-0947-4834-b386-4a1c21fd630b/tool-results/webfetch-1783552243960-9delfi.pdf]", "durationMs": 6313, "url": "https://arxiv.org/pdf/2604.04538"}
```

### [60] TOOL CALL — WebSearch · 2026-07-08 23:10:55 UTC

```
hodge decomposition directed graph python code incidence matrix B gradient lsqr curl triangle numpy scipy example 2023
```

### [61] TOOL CALL — WebSearch · 2026-07-08 23:10:55 UTC

```
OpenAlex API "referenced_works" journal citation matrix build aggregate python pandas source_id 2024
```

### [62] TOOL RESULT — WebSearch · 2026-07-08 23:11:01 UTC

```
{"query": "OpenAlex API \"referenced_works\" journal citation matrix build aggregate python pandas source_id 2024", "results": [{"tool_use_id": "srvtoolu_018cugMBfBZTtzoqqbfH3Duq", "content": [{"title": "API Overview - OpenAlex Developers", "url": "https://developers.openalex.org/api-reference/introduction"}, {"title": "pyBiblioNet: a Python library for a comprehensive network-based bibliometric analysis", "url": "https://arxiv.org/pdf/2601.16990"}, {"title": "Atlas of Science Collaboration, 1971-2020", "url": "https://arxiv.org/pdf/2308.16810"}, {"title": "openalex-docs/api-entities/works/work-object/README.md at main · ourresearch/openalex-docs", "url": "https://github.com/ourresearch/openalex-docs/blob/main/api-entities/works/work-object/README.md"}, {"title": "Reference Coverage Analysis of OpenAlex compared to Web of Science and   Scopus", "url": "https://arxiv.org/pdf/2401.16359"}, {"title": "PreprintResolver: Improving Citation Quality by Resolving Published   Versions of ArXiv Preprints using Literature Databases", "url": "https://arxiv.org/pdf/2309.01373"}, {"title": "An analysis of the suitability of OpenAlex for bibliometric analyses", "url": "https://arxiv.org/pdf/2404.17663"}, {"title": "'Intelligence Studies Network': A human-curated database for indexing   resources with open-source tools", "url": "https://arxiv.org/pdf/2408.03868"}, {"title": "Geographical and Disciplinary Coverage of Open Access Journals:   OpenAlex, Scopus and WoS", "url": "https://arxiv.org/pdf/2411.03325"}, {"title": "GitHub - filipinascimento/openalexnet: OpenAlex Networks is a helper library to process and obtain data from the OpenAlex dataset via API. It also provides functionality to generate citation and coauthorship networks from queries. · GitHub", "url": "https://github.com/filipinascimento/openalexnet"}]}, "Based on the web search results, here's what I found regarding your query about OpenAlex API:\n\n## Key Information Found\n\n**OpenAlex referenced_works Field:**\nThe `referenced_works` field contains OpenAlex IDs for works that a work cites, representing citations that go from one work out to other works. The field stores an array of OpenAlex work IDs in the format like \"https://openalex.org/W2753353163\".\n\n**OpenAlex API Access:**\nOpenAlex offers a RESTful API for programmatic access to data, facilitating its integration into bibliometric tools and analyses. API keys are free and can be obtained from OpenAlex.\n\n**Python Libraries for OpenAlex:**\nThe search results reference several Python-based tools for working with OpenAlex data:\n- pyBiblioNet performs bibliometric analyses using data sourced from OpenAlex\n- OpenAlex Networks is a helper library to process and obtain data from the OpenAlex dataset via API, providing functionality to generate citation and coauthorship networks from queries\n\nHowever, the search results don't contain specific examples or documentation about building a citation matrix using pandas with `source_id` aggregation for 2024 data. For more detailed implementation guidance, you may want to check the official OpenAlex API documentation or look for tutorials on the OpenAlex GitHub repositories."], "durationSeconds": 6.010608724000019, "searchCount": 1}
```

### [63] TOOL RESULT — WebSearch · 2026-07-08 23:11:03 UTC

```
{"query": "hodge decomposition directed graph python code incidence matrix B gradient lsqr curl triangle numpy scipy example 2023", "results": [{"tool_use_id": "srvtoolu_01CeJEUDx7Kv63UMRdzV9J35", "content": [{"title": "pytspl.decomposition.hodge_decomposition — PyTSPL 0.1.5 documentation", "url": "https://pytspl.readthedocs.io/en/latest/autoapi/pytspl/decomposition/hodge_decomposition/"}, {"title": "Graph-Hodge-decomposition/Graph_Hodge_decomposition_adjacency_mat.ipynb at main · yusuke-imoto-lab/Graph-Hodge-decomposition", "url": "https://github.com/yusuke-imoto-lab/Graph-Hodge-decomposition/blob/main/Graph_Hodge_decomposition_adjacency_mat.ipynb"}, {"title": "Hodge-Decomposition of Brain Networks", "url": "https://arxiv.org/html/2211.10542v2"}, {"title": "Stationarity and Spectral Characterization of Random Signals on Simplicial Complexes", "url": "https://arxiv.org/pdf/2602.03055"}, {"title": "GitHub - kazumits/ddhodge: Modeling Latent Flow Structure using Hodge Decomposition", "url": "https://github.com/kazumits/ddhodge"}, {"title": "Statistical ranking and combinatorial Hodge theory", "url": "https://www.math.pku.edu.cn/teachers/yaoy/publications/HodgeRank.MathProg.B.2010.pdf"}, {"title": "Representing Edge Flows on Graphs via Sparse Cell Complexes Josef Hoppe", "url": "https://proceedings.mlr.press/v231/hoppe24a/hoppe24a.pdf"}, {"title": "Decentralized Trajectory Tracking Using Homology and Hodge Decomposition   in Sensor Networks", "url": "https://arxiv.org/pdf/1708.09129"}, {"title": "Discrete Hodge Theory on Graphs: A Tutorial", "url": "https://www.researchgate.net/publication/260712232_Discrete_Hodge_Theory_on_Graphs_A_Tutorial"}, {"title": "SVD Incidence Centrality: A Unified Spectral Framework for Node and Edge Analysis in Directed Networks and Hypergraphs", "url": "https://arxiv.org/pdf/2602.15736"}]}, "I've completed a web search on Hodge decomposition with directed graphs, incidence matrices, and Python implementations. Here are the key findings:\n\n## Overview of Hodge Decomposition\n\nHodge decomposition breaks data defined on edges (edge flow) into three orthogonal components: gradient, curl, and harmonic flows, each providing unique topological insights.\n\n## Mathematical Framework\n\nThe incidence matrices satisfy the property B_k · B_{k+1} = 0, and the Hodge decomposition allows decomposing simplicial signal spaces into three orthogonal subspaces where any k-signal can be uniquely decomposed into gradient, curl, and harmonic components.\n\nFor any 1-form, it can be decomposed as ω = df + δg + h, where h is a harmonic 1-form (divergence-free and curl-free), df is a gradient flow with a potential function defined on nodes, and δg is a curl flow with a potential function defined on faces.\n\n## Python Implementation Resources\n\nPyTSPL provides functions like `get_gradient_flow()` that takes the incidence matrix B1 (nodes to edges) and flow as inputs, and `get_curl_flow()` that takes the incidence matrix B2 (edges to triangles) and flow.\n\nThe ddhodge package is built on a mathematical framework of Hodge decomposition on simplicial complexes and can handle both acyclic and cyclic directed graph structures.\n\n## Applications\n\nThe Hodge-decomposition problem can be decomposed into orthogonal problems, where finding sparse gradient flows can be formulated as a regression problem to find node potentials using techniques like B⊤.\n\nThe search results contain documentation and research papers that discuss implementations using scipy sparse matrices and numpy for handling the incidence matrices and solving these decomposition problems."], "durationSeconds": 7.951490375999987, "searchCount": 1}
```

### [64] TOOL CALL — WebFetch · 2026-07-08 23:11:11 UTC

```
URL: https://pytspl.readthedocs.io/en/latest/autoapi/pytspl/decomposition/hodge_decomposition/
Prompt: Extract: exact function signatures for get_gradient_flow, get_curl_flow, get_harmonic_flow; input/output types; required incidence matrices B1 (node-edge) and B2 (edge-triangle); how to install pytspl
```

### [65] TOOL CALL — WebFetch · 2026-07-08 23:11:11 UTC

```
URL: https://github.com/kazumits/ddhodge
Prompt: Extract: installation instructions, main API functions for Hodge decomposition on graphs, key function signatures and their inputs/outputs
```

### [66] TOOL RESULT — WebFetch · 2026-07-08 23:11:11 UTC

````
{"bytes": 4102, "code": 200, "codeText": "OK", "result": "# Hodge Decomposition Functions in pytspl\n\n## Function Signatures\n\n**get_gradient_flow:**\n```python\nget_gradient_flow(B1: scipy.sparse.csr_matrix, flow: numpy.ndarray, \n                  round_fig: bool = True, round_sig_fig: int = 2) → numpy.ndarray\n```\n\n**get_curl_flow:**\n```python\nget_curl_flow(B2: scipy.sparse.csr_matrix, flow: numpy.ndarray,\n              round_fig: bool = True, round_sig_fig: int = 2) → numpy.ndarray\n```\n\n**get_harmonic_flow:**\n```python\nget_harmonic_flow(B1: scipy.sparse.csr_matrix, B2: scipy.sparse.csr_matrix,\n                  flow: numpy.ndarray, round_fig: bool = True, \n                  round_sig_fig: int = 2) → numpy.ndarray\n```\n\n## Incidence Matrices Required\n\n- **B1**: Node-to-edge incidence matrix (required for gradient and harmonic flows)\n- **B2**: Edge-to-triangle incidence matrix (required for curl and harmonic flows)\n\n## Installation\n\nThe provided documentation does not include installation instructions. You would typically install pytspl via pip using `pip install pytspl` or through the project's GitHub repository, but this specific information is not covered in the source material.", "durationMs": 3123, "url": "https://pytspl.readthedocs.io/en/latest/autoapi/pytspl/decomposition/hodge_decomposition/"}
````

### [67] TOOL RESULT — WebFetch · 2026-07-08 23:11:15 UTC

````
{"bytes": 328567, "code": 200, "codeText": "OK", "result": "# DDHodge Installation & API Reference\n\n## Installation\n\nThe package can be installed via:\n```r\ndevtools::install_github(\"kazumits/ddhodge\")\n```\n\n**Note:** Per the repository announcement (2025/3/12), this R package is outdated. Users should reference the Julia implementation [ddHodge.jl](https://github.com/kazumits/ddHodge.jl) for updated functionality.\n\n## Primary API Functions\n\n### `diffusionGraph()`\nConstructs a flow network from high-dimensional data using Hodge decomposition principles.\n\n**Key parameters:**\n- `X`: Data matrix (rows = observations, columns = features)\n- `group`: Boolean vector indicating root/source cells\n- `k`: Number of nearest neighbors for graph construction\n- `npc`: Principal components retained\n- `ndc`: Diffusion components used\n- `s`: Scaling parameter\n\n**Returns:** Graph object with node attributes including `div` (divergence), `u` (potential/pseudo-time)\n\n### `multimaxflow()`\nExtracts primary and secondary flow paths between specified source-sink cell clusters.\n\n**Parameters:**\n- `g`: Graph from `diffusionGraph()`\n- Source and sink cell indices (integer vectors)\n\n**Returns:** Modified graph with `flow` edge weights and `pass` node attributes\n\n## Core Mathematical Framework\n\nThe toolkit leverages Hodge decomposition on simplicial complexes to decompose flows into gradient (acyclic), curl (cyclic), and harmonic components—applicable to both directed and undirected graph structures.", "durationMs": 5525, "url": "https://github.com/kazumits/ddhodge"}
````

### [68] ASSISTANT · 2026-07-08 23:14:34 UTC

```
I now have sufficient technical detail to write a comprehensive, actionable plan. Let me compile it.
```

### [69] TOOL CALL — WebFetch · 2026-07-08 23:14:34 UTC

```
URL: https://pypi.org/project/cidre/
Prompt: Extract: current version, install command, Python version compatibility, and any known dependencies that might cause issues
```

### [70] TOOL CALL — WebSearch · 2026-07-08 23:14:34 UTC

```
OpenAlex API "primary_location.source.id" works filter "referenced_works" async python rate limit polite email
```

### [71] TOOL RESULT — WebFetch · 2026-07-08 23:14:34 UTC

````
{"bytes": 56991, "code": 200, "codeText": "OK", "result": "# CIDRE Package Information\n\n**Current Version:** 0.0.1 (released July 8, 2021)\n\n**Installation Command:** \n```\npip install cidre\n```\n\n**Python Compatibility:** Python 3.7 or later, with explicit support for versions 3.7, 3.8, and 3.9\n\n**Known Dependencies:** The package requires `numpy.array` or `list` objects for group membership data and accepts adjacency matrices as either NetworkX Graph objects or `scipy.sparse_csr_matrix` format. For visualization features, `matplotlib.pyplot` is needed.\n\n**Development Status:** The package is classified as \"3 - Alpha,\" indicating early-stage development with potential for changes.\n\n**License:** MIT License", "durationMs": 3409, "url": "https://pypi.org/project/cidre/"}
````

### [72] TOOL RESULT — WebSearch · 2026-07-08 23:14:38 UTC

```
{"query": "OpenAlex API \"primary_location.source.id\" works filter \"referenced_works\" async python rate limit polite email", "results": [{"tool_use_id": "srvtoolu_01XqNuR2vNMqrDrpyNe7Z1dz", "content": [{"title": "Works Overview - OpenAlex Developers", "url": "https://developers.openalex.org/api-reference/works"}, {"title": "openalex-docs/how-to-use-the-api/rate-limits-and-authentication.md at main · ourresearch/openalex-docs", "url": "https://github.com/ourresearch/openalex-docs/blob/main/how-to-use-the-api/rate-limits-and-authentication.md"}, {"title": "openalex-api-tutorials/notebooks/institutions/uw-collaborators.ipynb at main · ourresearch/openalex-api-tutorials", "url": "https://github.com/ourresearch/openalex-api-tutorials/blob/main/notebooks/institutions/uw-collaborators.ipynb"}, {"title": "GitHub - J535D165/pyalex: A Python library for OpenAlex (openalex.org) · GitHub", "url": "https://github.com/J535D165/pyalex"}, {"title": "Location object | OpenAlex technical documentation", "url": "https://docs.openalex.org/api-entities/works/work-object/location-object"}, {"title": "OpenAlex API Documentation Overview | PDF | Open Access | Pub Med", "url": "https://www.scribd.com/document/785054810/OpenAlex-Technical-Documentation"}]}, "I found relevant information about the OpenAlex API. Here's what the search results show:\n\n## Key Findings:\n\n**Rate Limiting:**\nAll users are limited to a maximum of 100 requests per second, and the OpenAlex API uses a credit-based rate limiting system with different endpoint types consuming different amounts of credits. The free allowance is 100,000 API calls per day. For academic researchers, support can be provided for free by contacting support@openalex.org.\n\n**API Key and Authentication:**\nStarting February 13, 2026, an API key is required to use the OpenAlex API, though API keys are free.\n\n**Works Filtering:**\nThe API supports filtering, sorting, and grouping on works fields with specific syntax.\n\n**Primary Location Information:**\nThe primary_location is the best (closest to the version of record) copy of a work, and you can filter by source type.\n\n**Python Implementation:**\nPyAlex is a lightweight Python interface to the OpenAlex API, and it supports pagination through the paginate() method, with each returned page having a maximum of per_page (default 25).\n\nThe search results don't contain specific details about the `referenced_works` filter or async Python implementations. Would you like me to search for more specific information on those topics?"], "durationSeconds": 6.362827492000012, "searchCount": 1}
```

### [73] ASSISTANT · 2026-07-08 23:16:45 UTC

```
I have all the technical details needed. Let me write the complete, concrete plan.
```

### [74] TOOL CALL — Skill · 2026-07-08 23:16:45 UTC

```
artifact-design
```

### [75] TOOL RESULT — Skill · 2026-07-08 23:16:45 UTC

```
{"success": true, "commandName": "artifact-design"}
```

### [76] ASSISTANT · 2026-07-08 23:20:05 UTC

```
That skill is for visual artifacts — not relevant here. I have all the technical research I need. Let me write the plan JSON now.
```

### [77] TOOL CALL — Write · 2026-07-08 23:20:05 UTC

````
File: /ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_1/gen_plan/gen_plan_experiment_1/.terminal_claude_agent_struct_out.json

{
  "title": "Hodge-Curl Cartel Detector on Citation Networks",
  "summary": "Build a journal citation network from OpenAlex, implement the combinatorial Hodge decomposition (gradient + curl + harmonic) on the net-flow matrix, use the per-node/triangle curl score as a manipulation detector, calibrate against a degree-preserving null, and compare head-to-head with CIDRE, reciprocity, within-group density, and PageRank on JCR-suppressed journal detection plus synthetic cartel injection tests.",
  "runpod_compute_profile": "cpu_heavy",
  "implementation_pseudocode": "# ============================================================\n# ENVIRONMENT SETUP\n# ============================================================\n# pip install cidre pytspl pyalex scipy numpy networkx pandas\n#             matplotlib scikit-learn tqdm requests aiohttp\n#\n# CIDRE: pip install cidre==0.0.1 (Python 3.7-3.11 compatible)\n# pyalex: lightweight OpenAlex API client with pagination\n# pytspl: clean Hodge decomposition library (get_gradient_flow/get_curl_flow)\n# Note: OpenAlex API requires a free API key since Feb 2026.\n#   Register at https://openalex.org/users and set env var OPENALEX_API_KEY\n#   OR use mailto polite crawling: append ?mailto=researcher@example.com to all calls\n\n# ============================================================\n# PHASE 0 — JCR GROUND TRUTH COMPILATION\n# File: build_ground_truth.py\n# ============================================================\n# Compile suppressed journal ISSNs from public sources:\n#\n# Source A: CIDRE paper supplementary (Kojaku et al. 2021, Scientific Reports)\n#   — 55 journals in 22 stacking groups, 2007-2019\n#   — Hardcode known groups from paper Table S1 (journal names + ISSNs)\n#   — These are the PRIMARY ground truth for citation STACKING (our focus)\n#\n# Source B: Retractionwatch/Clarivate public lists 2019-2025\n#   Fetch and parse these public URLs for names+reasons:\n#   - https://retractionwatch.com/2025/06/18/clarivate-impact-factor-suppression-list-2025-self-citation-stacking/\n#   - https://scholarlykitchen.sspnet.org/2018/06/27/ (2018, 20 journals)\n#   - https://retractionwatch.com/2021/06/30/ (2020, 10 journals)\n#   - Clarivate Title Suppressions Zendesk page (if accessible)\n#   Extract journal names and classify by reason (self-citation vs stacking)\n#\n# Output: suppressed_journals.json\n# Schema: [{\"name\": str, \"issn_l\": str, \"year_suppressed\": int,\n#            \"reason\": \"self_citation\" | \"citation_stacking\",\n#            \"openalex_id\": str | null}]\n#\n# IMPORTANT SUBSET DISTINCTION:\n#   label_stacking: only journals suppressed for citation stacking (cartel-type)\n#   label_all: all suppressions (self-citation + stacking)\n# Our primary evaluation uses label_stacking; report both.\n\n\n# ============================================================\n# PHASE 1 — BUILD JOURNAL CITATION NETWORK\n# File: build_network.py\n# ============================================================\n# We build a journal×journal citation matrix C where\n# C[i,j] = number of papers published in journal i in 2018-2020\n#           that cite any paper published in journal j in 2016-2020.\n# This mirrors the JIF 2-year citation window used by Clarivate.\n#\n# Step 1.1 — Get top journals from OpenAlex:\n#   GET https://api.openalex.org/sources\n#       ?filter=type:journal\n#       &sort=cited_by_count:desc\n#       &per_page=200\n#       &select=id,display_name,issn_l,issn,topics.field.display_name,cited_by_count\n#       &api_key={KEY}\n#   Paginate to collect TOP_N=3000 journals. Save journals.json.\n#\n# Step 1.2 — Ensure suppressed journals are included:\n#   For each ISSN in suppressed_journals.json NOT already in our set:\n#       GET /sources?filter=issn:{issn_l}&select=id,display_name,cited_by_count\n#       Add to journal set even if outside top 3000\n#   Total: ~3100-3200 journals (N).\n#\n# Step 1.3 — Build work→journal lookup incrementally:\n#   Maintain dict: work_id_to_journal = {}\n#   For each journal j:\n#       For each paper p published in journal j, years 2018-2020:\n#           work_id_to_journal[p.id] = j.index\n#\n# Step 1.4 — Build citation matrix using async requests:\n#   For each journal j in our set (async, concurrency=5, respect rate limit):\n#       cursor = '*'\n#       while cursor:\n#           GET /works?filter=primary_location.source.id:{j.openalex_id},\n#                       publication_year:2018-2020\n#                   &select=id,referenced_works\n#                   &per_page=200&cursor={cursor}\n#                   &api_key={KEY}\n#           For each paper p in response:\n#               for ref_id in p.referenced_works:\n#                   if ref_id in work_id_to_journal:\n#                       C[j.index, work_id_to_journal[ref_id]] += 1\n#                   else:\n#                       unresolved_refs.add(ref_id)\n#           cursor = meta.next_cursor\n#\n# Step 1.5 — Batch-resolve unresolved reference work IDs:\n#   chunk_size = 100 (URL length limit)\n#   for chunk in chunks(unresolved_refs, chunk_size):\n#       GET /works?filter=ids.openalex:{id1}|{id2}|...\n#                &select=id,primary_location.source.id\n#       For each result: update work_id_to_journal[id] = source_idx\n#   Re-sweep unresolved refs and update C matrix.\n#\n# Step 1.6 — Save network:\n#   scipy.sparse.save_npz('data/citation_matrix.npz', C_csr)\n#   journal_index.json: [{\"row\": int, \"openalex_id\": str, \"name\": str,\n#                          \"issn_l\": str, \"field\": str}]\n#\n# MINI TEST (run first, ~20 min API time):\n#   TOP_N=100, years=2019-2020, cursor_only 1 page per journal (200 papers max)\n#   Expected: 100×100 matrix, ~50K-200K citations\n#   Sanity checks:\n#     - C.diagonal() should be ~0 or small (self-citation exists but we focus on pairs)\n#     - High-cited journals (Nature, Science) should have high column sums\n#     - Matrix should be highly asymmetric (C != C.T)\n#\n# SCALING: Full run with TOP_N=3000 may take 2-3 hours with async.\n# If time is tight: use TOP_N=1000 for the evaluation, ensuring all suppressed journals included.\n\n\n# ============================================================\n# PHASE 2 — NETWORK PREPROCESSING\n# File: preprocess.py\n# ============================================================\n# 2.1 Apply edge threshold to reduce noise:\n#   THRESH = 3  # keep only edges where C[i,j] + C[j,i] >= THRESH\n#   mask = (C + C.T) >= THRESH\n#   C_thresh = C.multiply(mask)\n#   # Reduces E dramatically; typical: 3M raw edges → 200K thresholded edges\n#\n# 2.2 Remove isolated nodes (no connections after thresholding)\n#   active_nodes = np.where(np.asarray(C_thresh.sum(1)).squeeze() +\n#                            np.asarray(C_thresh.sum(0)).squeeze() > 0)[0]\n#   C_active = C_thresh[active_nodes][:, active_nodes]\n#   N = len(active_nodes)\n#\n# 2.3 Compute net flow matrix:\n#   Y = C_active - C_active.T  # antisymmetric N×N matrix\n#   # Y[i,j] > 0 means i sends more citations to j than j to i\n#\n# 2.4 Build oriented edge list (canonical: i < j):\n#   cx = C_active.tocoo()\n#   edges_set = set()\n#   for i, j in zip(cx.row, cx.col):\n#       if i != j:\n#           edges_set.add((min(i,j), max(i,j)))\n#   edges = sorted(edges_set)  # list of (i,j) with i < j\n#   E = len(edges)\n#   edge_to_idx = {e: idx for idx, e in enumerate(edges)}\n#\n# 2.5 Build edge flow vector:\n#   Y_dense = np.asarray(Y.todense())\n#   Y_e = np.array([Y_dense[i,j] for (i,j) in edges])\n#   # Y_e[e] > 0: net flow in canonical i→j direction\n#\n# Log: N, E, threshold used, network density\n\n\n# ============================================================\n# PHASE 3 — HODGE DECOMPOSITION\n# File: hodge.py\n# ============================================================\n# 3.1 Build B1 — node×edge signed incidence matrix:\n#   # B1[head, e] = +1, B1[tail, e] = -1 for canonical orientation (i→j, i<j)\n#   rows_B1, cols_B1, data_B1 = [], [], []\n#   for e_idx, (i, j) in enumerate(edges):\n#       rows_B1.extend([i, j])\n#       cols_B1.extend([e_idx, e_idx])\n#       data_B1.extend([-1.0, +1.0])  # i is tail (-1), j is head (+1)\n#   B1 = sparse.csr_matrix((data_B1, (rows_B1, cols_B1)), shape=(N, E))\n#   # Shape: N×E. B1.T @ s gives node potential differences on edges.\n#\n# 3.2 Enumerate triangles (3-cliques) in the undirected thresholded graph:\n#   adj_list = defaultdict(set)\n#   for (i, j) in edges:\n#       adj_list[i].add(j)\n#       adj_list[j].add(i)\n#\n#   triangles = []\n#   for (i, j) in edges:\n#       # Find common neighbors k > j (canonical ordering i < j < k)\n#       common = adj_list[i] & adj_list[j]\n#       for k in common:\n#           if k > j:\n#               triangles.append((i, j, k))\n#\n#   T = len(triangles)\n#   # Performance note: For E=200K edges, expect ~few hundred K triangles\n#   # If T > 5M: apply secondary threshold (keep only edges C[i,j]+C[j,i] >= 10)\n#   # Time estimate: <60s for T < 2M\n#\n# 3.3 Build B2 — edge×triangle incidence matrix:\n#   # Orientation convention: triangle (i,j,k) with i<j<k has circuit i→j→k→i\n#   # B2[e_ij, t] = +1 (i→j matches circuit)\n#   # B2[e_jk, t] = +1 (j→k matches circuit)\n#   # B2[e_ik, t] = -1 (circuit goes k→i, but edge is oriented i→k)\n#   rows_B2, cols_B2, data_B2 = [], [], []\n#   for t_idx, (i, j, k) in enumerate(triangles):\n#       # All three edge indices (all pairs with canonical orientation)\n#       e_ij = edge_to_idx[(i, j)]\n#       e_jk = edge_to_idx[(j, k)]\n#       e_ik = edge_to_idx[(i, k)]\n#       rows_B2.extend([e_ij, e_jk, e_ik])\n#       cols_B2.extend([t_idx, t_idx, t_idx])\n#       data_B2.extend([+1.0, +1.0, -1.0])\n#   B2 = sparse.csr_matrix((data_B2, (rows_B2, cols_B2)), shape=(E, T))\n#\n#   # VERIFY: B1 @ B2 should be (near) zero matrix:\n#   check = B1 @ B2  # N×T matrix, should be all zeros\n#   assert np.allclose(check.data, 0, atol=1e-10), \"Hodge identity violated!\"\n#\n# 3.4 Solve for gradient potential (HodgeRank prestige scores):\n#   from scipy.sparse.linalg import lsqr\n#   # Solve: min_s ||B1^T @ s - Y_e||^2  (B1^T is E×N)\n#   # s_star is N-vector of prestige potentials per journal\n#   result = lsqr(B1.T, Y_e, damp=1e-6, atol=1e-10, btol=1e-10, iter_lim=20000)\n#   s_star = result[0]  # prestige/potential score per journal\n#   Y_grad = B1.T @ s_star  # E-vector: gradient component of flow\n#   # s_star is the HodgeRank prestige ranking (analog of Eigenfactor)\n#\n# 3.5 Solve for curl component:\n#   residual = Y_e - Y_grad  # residual = curl + harmonic\n#   # Solve: min_h ||B2^T @ h - residual||^2 (B2^T is T×E)\n#   result_curl = lsqr(B2.T, residual, damp=1e-6, atol=1e-10, iter_lim=20000)\n#   h_star = result_curl[0]  # T-vector: triangle potentials\n#   Y_curl = B2 @ h_star   # E-vector: curl component\n#   Y_harm = residual - Y_curl  # E-vector: harmonic component\n#\n# 3.6 Compute energy fractions (orthogonality check):\n#   total_energy = np.dot(Y_e, Y_e)\n#   grad_fraction = np.dot(Y_grad, Y_grad) / total_energy\n#   curl_fraction = np.dot(Y_curl, Y_curl) / total_energy\n#   harm_fraction = np.dot(Y_harm, Y_harm) / total_energy\n#   cross_check = abs(grad_fraction + curl_fraction + harm_fraction - 1.0)\n#   assert cross_check < 0.01, f\"Non-orthogonal decomposition: {cross_check}\"\n#\n# 3.7 Compute per-triangle curl values:\n#   # triangle_curl[t] = B2^T @ Y_e evaluated at triangle t\n#   triangle_curls = B2.T @ Y_e  # T-vector\n#   # Interpretation: large |triangle_curl[t]| = this triangle carries strong\n#   # circulating flow inconsistent with any global prestige ordering\n#\n# 3.8 Compute per-node curl scores:\n#   node_curl_sum = np.zeros(N)\n#   node_tri_count = np.zeros(N, dtype=int)\n#   for t_idx, (i, j, k) in enumerate(triangles):\n#       val = abs(triangle_curls[t_idx])\n#       for node in [i, j, k]:\n#           node_curl_sum[node] += val\n#           node_tri_count[node] += 1\n#   node_curl_score = node_curl_sum / (node_tri_count + 1e-10)\n#   # Zero-impute nodes with no triangles (isolated from any 3-cycle)\n#\n# 3.9 Degree-normalized curl score (reduces degree bias):\n#   degree = np.asarray(C_active.sum(1)).squeeze() + \\\n#             np.asarray(C_active.sum(0)).squeeze()\n#   node_curl_norm = node_curl_score / (np.log1p(degree) + 1e-10)\n\n\n# ============================================================\n# PHASE 4 — NULL MODEL CALIBRATION\n# File: null_model.py\n# ============================================================\n# Degree-preserving row-permutation null:\n#   For each null sample:\n#     C_null = C_active.tolil().copy()\n#     For each row i:\n#         cols = C_null[i].nonzero()[1]\n#         vals = np.asarray(C_null[i, cols]).squeeze()\n#         np.random.shuffle(vals)\n#         C_null[i, cols] = vals  # shuffle which journal gets each weight\n#     Convert to CSR, recompute Y, build Y_e, run Hodge, get node_curl_score\n#\n# n_null = 500 (use 200 if slow; N=3000 run should still be <30 min for 500)\n# Collect null_node_curl_scores: shape (n_null, N)\n#\n# Per-node statistics:\n#   null_mean = null_node_curl_scores.mean(0)  # N-vector\n#   null_std  = null_node_curl_scores.std(0) + 1e-10\n#   z_score   = (node_curl_score - null_mean) / null_std  # z-score per journal\n#   p_value   = (null_node_curl_scores >= node_curl_score).mean(0)  # fraction exceeding\n#\n# Also compute degree-corrected null for between-community edges:\n#   Use the Louvain field communities as block labels\n#   For community-preserving null: only permute within-community edges\n#   Compare community-preserving z-score vs degree-only z-score\n\n\n# ============================================================\n# PHASE 5 — BASELINES\n# File: baselines.py\n# ============================================================\n# 5.1 Reciprocity score per node:\n#   For each node i:\n#     partners_j = nonzero columns in row i of C_active\n#     reci_vals = [min(C[i,j], C[j,i]) / (C[i,j] + C[j,i] + 1e-10) for j in partners_j]\n#     weights = [(C[i,j] + C[j,i]) for j in partners_j]\n#     reciprocity[i] = weighted mean of reci_vals  # high = symmetric exchange\n#\n# 5.2 Field community detection and within-group density:\n#   adj_undirected = (C_active + C_active.T) / 2\n#   G_nx = networkx.from_scipy_sparse_array(adj_undirected)\n#   communities = networkx.community.louvain_communities(G_nx, seed=42, weight='weight')\n#   # Assign community index per node\n#   comm_label = np.zeros(N, dtype=int)\n#   for c_idx, comm in enumerate(communities):\n#       for node in comm:\n#           comm_label[node] = c_idx\n#   # Compute within-community density per node:\n#   for node in range(N):\n#       c = comm_label[node]\n#       group = list(communities[c])\n#       internal = C_active[group][:, group].sum()\n#       possible = len(group) * (len(group) - 1)\n#       density_score[node] = internal / (possible + 1e-10)\n#\n# 5.3 PageRank:\n#   G_directed = networkx.from_scipy_sparse_array(C_active, create_using=networkx.DiGraph)\n#   pr = networkx.pagerank(G_directed, alpha=0.85, max_iter=200)\n#   pagerank_scores = np.array([pr[n] for n in range(N)])\n#\n# 5.4 CIDRE:\n#   import cidre\n#   # Provide field labels from Louvain OR from OpenAlex field assignments\n#   field_membership = comm_label  # or: map OpenAlex field → int\n#   alg = cidre.Cidre(group_membership=field_membership)\n#   try:\n#       cidre_groups = alg.detect(C_active, threshold=0.15)\n#   except Exception:\n#       # Try different thresholds if no groups found\n#       for thresh in [0.10, 0.05, 0.01]:\n#           cidre_groups = alg.detect(C_active, threshold=thresh)\n#           if cidre_groups:\n#               break\n#   # Convert group membership to per-node anomaly score:\n#   cidre_scores = np.zeros(N)\n#   for group in cidre_groups:\n#       for node_id, score in group.donors.items():\n#           cidre_scores[node_id] = max(cidre_scores[node_id], score)\n#       for node_id, score in group.recipients.items():\n#           cidre_scores[node_id] = max(cidre_scores[node_id], score)\n#   cidre_binary = (cidre_scores > 0).astype(int)\n#   # IMPORTANT: CIDRE returns sparse binary flags (0/positive).\n#   # For AUC with binary predictions use cidre_binary as score too.\n\n\n# ============================================================\n# PHASE 6 — EVALUATION ON JCR GROUND TRUTH\n# File: evaluate.py\n# ============================================================\n# 6.1 Build label arrays:\n#   labels_stacking = np.zeros(N)  # 1 = suppressed for citation stacking\n#   labels_all = np.zeros(N)       # 1 = suppressed for any reason\n#   for journal_info in suppressed_journals:\n#       if journal_info['openalex_id'] in active_journal_set:\n#           idx = journal_to_idx[journal_info['openalex_id']]\n#           if journal_info['reason'] == 'citation_stacking':\n#               labels_stacking[idx] = 1\n#           labels_all[idx] = 1\n#   # Log: how many suppressed journals matched to active network nodes\n#\n# 6.2 Compute metrics for each method on labels_stacking (primary):\n#   from sklearn.metrics import roc_auc_score, average_precision_score\n#   import numpy as np\n#\n#   scores_dict = {\n#       'hodge_curl_raw':     node_curl_score,\n#       'hodge_curl_z':       z_score,          # null-calibrated\n#       'hodge_curl_norm':    node_curl_norm,    # degree-normalized\n#       'reciprocity':        reciprocity_score,\n#       'within_group_density': density_score,\n#       'pagerank':           pagerank_scores,\n#       'cidre':              cidre_scores,\n#   }\n#\n#   B = 2000  # bootstrap resamples\n#   results = {}\n#   for method, scores in scores_dict.items():\n#       if labels_stacking.sum() < 2:\n#           print(\"Too few positives for AUC; continuing with labels_all\")\n#           labels_eval = labels_all\n#       else:\n#           labels_eval = labels_stacking\n#\n#       auc_roc = roc_auc_score(labels_eval, scores)\n#       auc_pr  = average_precision_score(labels_eval, scores)\n#\n#       # Precision@k\n#       ranked = np.argsort(scores)[::-1]\n#       prec_at_k = {k: float(labels_eval[ranked[:k]].mean())\n#                    for k in [10, 50, 100]}\n#\n#       # Bootstrap CI\n#       boot_aucs = []\n#       for _ in range(B):\n#           idx = np.random.randint(0, len(labels_eval), len(labels_eval))\n#           if labels_eval[idx].sum() > 0:\n#               boot_aucs.append(roc_auc_score(labels_eval[idx], scores[idx]))\n#       ci = (np.percentile(boot_aucs, 2.5), np.percentile(boot_aucs, 97.5))\n#\n#       results[method] = {\n#           'auc': float(auc_roc), 'auc_pr': float(auc_pr),\n#           'prec_at_k': prec_at_k, 'ci': list(ci)\n#       }\n#\n# 6.3 Key comparison test (DeLong via permutation):\n#   n_perm = 10000\n#   delta_obs = roc_auc_score(labels_eval, z_score) - roc_auc_score(labels_eval, cidre_scores)\n#   perm_deltas = []\n#   for _ in range(n_perm):\n#       perm = np.random.permutation(len(labels_eval))\n#       d = roc_auc_score(labels_eval[perm], z_score) - \\\n#           roc_auc_score(labels_eval[perm], cidre_scores)\n#       perm_deltas.append(d)\n#   p_val_comparison = (np.abs(perm_deltas) >= np.abs(delta_obs)).mean()\n#   # Report: delta_obs, p_val_comparison, and whether curl CI excludes CIDRE AUC\n\n\n# ============================================================\n# PHASE 7 — SYNTHETIC CARTEL INJECTION\n# File: synthetic_injection.py\n# ============================================================\n# Inject cartels into the REAL network and measure detection.\n# This tests the core claim: curl detects manipulation at lower density than CIDRE/density.\n#\n# 7.1 Injection functions:\n#   def inject_cyclic_cartel(C, k, w, exclude_nodes=None):\n#       \"\"\"k-node ring: A→B→C→...→A\"\"\"\n#       nodes = random_sample(N, k, exclude=exclude_nodes)\n#       C = C.tolil().copy()\n#       for idx in range(k):\n#           u, v = nodes[idx], nodes[(idx+1) % k]\n#           C[u, v] += w\n#       return C.tocsr(), set(nodes)\n#\n#   def inject_reciprocal_cartel(C, k, w, exclude_nodes=None):\n#       \"\"\"k-node clique: all pairs exchange\"\"\"\n#       nodes = random_sample(N, k, exclude=exclude_nodes)\n#       C = C.tolil().copy()\n#       for u in nodes:\n#           for v in nodes:\n#               if u != v:\n#                   C[u, v] += w\n#       return C.tocsr(), set(nodes)\n#\n# 7.2 Sweep parameters:\n#   mean_edge_weight = C_active.data.mean()  # baseline weight scale\n#   k_values    = [3, 5, 10, 20]\n#   w_factors   = [0.01, 0.05, 0.1, 0.3, 0.5, 1.0, 2.0]  # × mean_edge_weight\n#   cartel_types = ['cyclic', 'reciprocal']\n#   n_repeats   = 20  # independent random placements per condition\n#\n# 7.3 For each (cartel_type, k, w_factor, repeat):\n#   w = w_factor * mean_edge_weight\n#   # Exclude known suppressed journals from injection targets\n#   exclude = suppressed_node_set\n#   if cartel_type == 'cyclic':\n#       C_mod, injected_nodes = inject_cyclic_cartel(C_active, k, w, exclude)\n#   else:\n#       C_mod, injected_nodes = inject_reciprocal_cartel(C_active, k, w, exclude)\n#\n#   # Recompute Hodge on modified network (fast: reuse B1, B2 with updated Y_e)\n#   Y_mod = C_mod - C_mod.T\n#   Y_e_mod = [Y_mod[i,j] for (i,j) in edges]\n#   s_mod  = lsqr(B1.T, Y_e_mod)[0]\n#   Y_grad_mod = B1.T @ s_mod\n#   res_mod = Y_e_mod - Y_grad_mod\n#   h_mod   = lsqr(B2.T, res_mod)[0]\n#   Y_curl_mod = B2 @ h_mod\n#   # node curl from triangle curls on Y_e_mod\n#   tc_mod = B2.T @ np.array(Y_e_mod)\n#   node_curl_mod = compute_node_curl(tc_mod, triangles, N)\n#\n#   # Detection AUC: injected nodes = 1, others = 0\n#   binary_labels = np.zeros(N)\n#   for n in injected_nodes: binary_labels[n] = 1\n#\n#   auc_curl    = roc_auc_score(binary_labels, node_curl_mod)\n#   auc_density = roc_auc_score(binary_labels, density_score_updated)\n#   # Rerun CIDRE on modified network:\n#   cidre_mod  = run_cidre(C_mod, field_membership)\n#   auc_cidre  = roc_auc_score(binary_labels, cidre_mod)\n#   auc_recip  = roc_auc_score(binary_labels, compute_reciprocity(C_mod))\n#\n#   record = {\n#       'cartel_type': cartel_type, 'k': k, 'w_factor': w_factor,\n#       'repeat': repeat,\n#       'auc_hodge_curl': auc_curl, 'auc_cidre': auc_cidre,\n#       'auc_density': auc_density, 'auc_reciprocity': auc_recip\n#   }\n#\n# 7.4 Aggregate: for each (cartel_type, k, w_factor), compute mean ± std AUC over repeats\n# PREDICTION: Hodge-curl AUC degrades more slowly than CIDRE/density as w_factor → 0\n# PREDICTION: cyclic (curl-only) cartel detected with much higher AUC by curl vs density\n\n\n# ============================================================\n# PHASE 8 — CONFOUND TEST\n# File: confound.py\n# ============================================================\n# Test the key claim: dense legitimate communities have LOW curl; cartels have HIGH curl.\n# This separates curl from density — the main novel claim of the hypothesis.\n#\n# 8.1 Identify dense legitimate clusters:\n#   # Use the Louvain communities (computed in Phase 5)\n#   # Exclude any community containing >=1 suppressed journal\n#   legitimate_communities = [\n#       comm for comm in communities\n#       if not any(node in suppressed_node_set for node in comm)\n#       and len(comm) >= 5\n#   ]\n#   # Rank by internal citation density, take top 5\n#   top_legit = sorted(legitimate_communities,\n#                       key=lambda g: C_active[list(g)][:,list(g)].sum() / (len(g)*(len(g)-1)),\n#                       reverse=True)[:5]\n#\n# 8.2 Identify known cartel groups:\n#   # From suppressed_journals, known citation-stacking groups (from CIDRE paper Table S1)\n#   # Group suppressed journals by their stacking group (they come in pairs/triples)\n#   # Each stacking group is a cluster of 2-10 journals that cite each other\n#   cartel_groups = [list_of_group for group in known_stacking_groups\n#                    if all nodes resolved to our network]\n#\n# 8.3 Compute group-level metrics for each cluster:\n#   def group_metrics(group_nodes):\n#       G_set = set(group_nodes)\n#       T_sub = [(i,j,k) for (i,j,k) in triangles\n#                if i in G_set and j in G_set and k in G_set]\n#       internal_curl = sum(abs(triangle_curls[t]) for t in range(T) if triangles[t] in T_sub_set)\n#       density = C_active[group_nodes][:,group_nodes].sum() / (len(G_set)*(len(G_set)-1)+1e-10)\n#       mean_recip = reciprocity_score[list(G_set)].mean()\n#       curl_frac = internal_curl / (density * len(G_set)**2 + 1e-10)\n#       return {'density': density, 'curl': internal_curl, 'curl_fraction': curl_frac,\n#               'mean_reciprocity': mean_recip, 'n_triangles': len(T_sub)}\n#\n# 8.4 Statistical tests:\n#   # Mann-Whitney U for each metric (legit vs cartel):\n#   from scipy.stats import mannwhitneyu\n#   for metric in ['density', 'curl_fraction', 'mean_reciprocity']:\n#       stat, p = mannwhitneyu([g[metric] for g in legit_metrics],\n#                               [g[metric] for g in cartel_metrics],\n#                               alternative='two-sided')\n#       # Expected: density p > 0.05 (no separation), curl_fraction p < 0.05 (separates)\n#\n# 8.5 Ablation — partial correlation of curl score with suppressed label\n#     after regressing out density and reciprocity:\n#   from sklearn.linear_model import LinearRegression\n#   X = np.stack([density_score, reciprocity_score], axis=1)\n#   model = LinearRegression().fit(X, labels_all)\n#   label_resid = labels_all - model.predict(X)\n#   model2 = LinearRegression().fit(X, z_score)\n#   curl_resid = z_score - model2.predict(X)\n#   partial_r = np.corrcoef(curl_resid, label_resid)[0,1]\n#   # Bootstrap CI for partial_r:\n#   boot_rs = [np.corrcoef(curl_resid[idx], label_resid[idx])[0,1]\n#              for idx in (np.random.randint(0, N, N) for _ in range(2000))]\n#   partial_r_ci = (np.percentile(boot_rs, 2.5), np.percentile(boot_rs, 97.5))\n\n\n# ============================================================\n# PHASE 9 — FORMAT OUTPUT\n# File: format_output.py\n# ============================================================\nimport json, numpy as np\n\n# Build method_out.json following the schema below\n# All numpy floats must be cast to python float/int before JSON serialization\n# Use float(x) for all numpy scalars\n\nresult = {\n    \"network_stats\": {\n        \"n_journals_raw\": int(TOP_N_requested),\n        \"n_active_nodes\": int(N),\n        \"n_edges_thresholded\": int(E),\n        \"n_triangles\": int(T),\n        \"edge_threshold\": int(THRESH),\n        \"years\": \"2018-2020\",\n        \"hodge_energy\": {\n            \"grad_fraction\": float(grad_fraction),\n            \"curl_fraction\": float(curl_fraction),\n            \"harm_fraction\": float(harm_fraction)\n        }\n    },\n    \"hodge_scores\": [\n        {\"journal_idx\": int(i),\n         \"journal_name\": str(journal_names[i]),\n         \"issn_l\": str(issn_map[i]),\n         \"prestige_score\": float(s_star[i]),\n         \"node_curl_raw\": float(node_curl_score[i]),\n         \"node_curl_z\": float(z_score[i]),\n         \"node_curl_norm\": float(node_curl_norm[i]),\n         \"p_value_null\": float(p_value[i]),\n         \"is_suppressed_stacking\": bool(labels_stacking[i]),\n         \"is_suppressed_any\": bool(labels_all[i])}\n        for i in range(N)\n    ],\n    \"baseline_scores\": [\n        {\"journal_idx\": int(i),\n         \"cidre_score\": float(cidre_scores[i]),\n         \"reciprocity\": float(reciprocity_score[i]),\n         \"group_density\": float(density_score[i]),\n         \"pagerank\": float(pagerank_scores[i])}\n        for i in range(N)\n    ],\n    \"evaluation\": {\n        \"label_primary\": \"citation_stacking\",\n        \"n_positives_stacking\": int(labels_stacking.sum()),\n        \"n_positives_all\": int(labels_all.sum()),\n        \"methods\": results,  # from Phase 6\n        \"curl_vs_cidre_delta_auc\": float(delta_obs),\n        \"p_value_comparison\": float(p_val_comparison)\n    },\n    \"synthetic_injection\": synthetic_records,  # list from Phase 7\n    \"confound_test\": {\n        \"legit_clusters\": legit_metrics_list,\n        \"cartel_groups\": cartel_metrics_list,\n        \"mannwhitney_density_p\": float(p_density),\n        \"mannwhitney_curl_p\": float(p_curl),\n        \"partial_corr_curl\": float(partial_r),\n        \"partial_corr_ci\": [float(partial_r_ci[0]), float(partial_r_ci[1])]\n    },\n    \"top_triangles_by_curl\": [\n        {\"nodes\": [int(i), int(j), int(k)],\n         \"journal_names\": [journal_names[i], journal_names[j], journal_names[k]],\n         \"curl_value\": float(triangle_curls[t_idx]),\n         \"any_suppressed\": bool(labels_all[[i,j,k]].any())}\n        for t_idx, (i,j,k) in sorted(enumerate(triangles),\n                                     key=lambda x: abs(triangle_curls[x[0]]),\n                                     reverse=True)[:50]\n    ],\n    \"prestige_ranking_top100\": [\n        {\"rank\": r+1,\n         \"journal_name\": journal_names[rank_idx],\n         \"prestige_score\": float(s_star[rank_idx]),\n         \"curl_z_score\": float(z_score[rank_idx]),\n         \"is_suppressed_any\": bool(labels_all[rank_idx])}\n        for r, rank_idx in enumerate(np.argsort(s_star)[::-1][:100])\n    ]\n}\nwith open('method_out.json', 'w') as f:\n    json.dump(result, f, indent=2)\nprint(\"Done. method_out.json written.\")",
  "fallback_plan": "## Fallback A — Simulated journal network if OpenAlex API is unavailable or slow\n\nIf the OpenAlex API data acquisition cannot complete within 2 hours (e.g., rate limits, auth issues, or data volume), replace Phase 1 with a synthetic network generator that still produces realistic properties:\n\n```python\ndef generate_synthetic_citation_network(N=500, n_fields=10, n_cartels=5, cartel_size=5, seed=42):\n    # Create a hierarchical prestige structure (DAG-like with noise)\n    # N journals in n_fields communities\n    # Add within-field citations (high density), cross-field citations (low density)\n    # Inject n_cartels cyclic/reciprocal groups\n    # Return C sparse matrix + ground truth labels\n```\n\nWith a synthetic network, all downstream phases (Hodge decomposition, CIDRE, evaluation, synthetic injection) remain identical. The confound test and synthetic injection phases are especially valid on synthetic data. **Report clearly** that ground truth evaluation uses synthetic cartels, not real JCR suppressions.\n\n## Fallback B — If CIDRE installation fails\n\nCIDRE v0.0.1 requires Python 3.7-3.9. If the executor environment has Python 3.10+ and CIDRE fails, implement a simplified CIDRE-like baseline manually:\n\n```python\ndef simple_cidre_baseline(C, group_membership):\n    # For each community block:\n    # Expected_ij = degree_i * degree_j / total_weight (Poisson null)\n    # Score_ij = C[i,j] / Expected_ij\n    # Node anomaly score = max over neighbors of Score_ij within same community\n    # This captures the core CIDRE idea without the full SBM fit\n```\n\nLabel this `cidre_approx` in results. Try `pip install cidre --python-version 3.9` in a venv if the system Python is newer.\n\n## Fallback C — If triangle enumeration is too slow (E > 500K)\n\nApply a stricter edge threshold (THRESH=10 instead of 3). This reduces E dramatically while retaining only the citation relationships strong enough to form manipulation signals. Journal pairs with < 10 mutual citations are unlikely to represent structured cartels. Alternatively, limit triangle enumeration to nodes within the same Louvain community (cartels typically operate within-field), which reduces the effective graph size by ~10× while preserving most relevant triangles.\n\n## Fallback D — Simplified curl score without full B2 construction\n\nIf B2 construction is too memory-intensive (T > 10M triangles), compute a direct triangle-aggregation score without building the sparse matrix:\n\n```python\n# Direct triangle curl score: skip B2, iterate triangles directly\nnode_curl = np.zeros(N)\nfor (i, j, k) in triangles:\n    tc = Y_net[i,j] + Y_net[j,k] - Y_net[i,k]  # signed triangle curl\n    node_curl[i] += abs(tc)\n    node_curl[j] += abs(tc)\n    node_curl[k] += abs(tc)\n# Skip the B2 @ lsqr projection step; use raw triangle sum as curl score\n```\n\nThis is equivalent to the projection for scoring purposes (the projected curl and raw triangle sum correlate highly). Report that the simplified version was used.\n\n## Fallback E — Minimal viable output if time runs short\n\nPrioritize in this order:\n1. Network construction + Hodge decomposition on top-500 journals (all phases)\n2. Evaluation on JCR ground truth with bootstrap CIs\n3. Synthetic injection for cyclic cartels at k=5 only\n4. Skip confound test if <30 min remain\n\nAlways write method_out.json with whatever results are available, marking missing fields as null rather than omitting them.",
  "testing_plan": "## Testing Strategy: Mini → Medium → Full\n\n### Step 0: Smoke test on tiny synthetic graph (~2 min)\nBefore any data acquisition, run a unit test of the Hodge decomposition on a hand-crafted 6-node graph with one known cyclic cartel:\n\n```python\n# Synthetic test: 6 nodes\n# Hierarchical part: 0→1→2→3 (prestige chain)\n# Cartel: 3→4→5→3 (cyclic with weight 10)\nC_test = sparse.lil_matrix((6,6))\nC_test[0,1]=100; C_test[1,2]=80; C_test[2,3]=60; C_test[3,4]=5; C_test[4,5]=5; C_test[5,3]=5\nC_test = C_test.tocsr()\n# Expected: nodes 3,4,5 get HIGH curl score; nodes 0,1,2 get LOW curl score\n# Expected energy: grad_fraction > 0.8 (mostly hierarchical)\n# Verify B1@B2 == 0 (Hodge identity)\n# Verify s_star[0] > s_star[3] (foundational nodes have higher prestige)\n```\n\n### Step 1: Mini run on N=100 journals (no API — use cached/synthetic) (~10 min)\n- If OpenAlex API is available: fetch top 100 journals, 1 page of papers each\n- Verify citation matrix is non-zero, asymmetric\n- Run all Hodge phases, check energy fractions sum to ~1.0\n- Verify z_scores are computable (null model runs)\n- Run CIDRE on the 100-journal matrix; verify it returns some groups or empty list\n- Run all 6 baselines without errors\n- Write a stub method_out.json — check schema is valid JSON\n- **Key signals**: grad_fraction > 0.5 (citation networks are mostly hierarchical); some nodes have z_score > 2\n\n### Step 2: Ground truth compilation test (~10 min)\n- Verify suppressed_journals.json is written with ≥20 entries\n- Verify ISSNs are valid format (4-digit-hyphen-4-digit)\n- Test ISSN matching: at least 5 suppressed journals should resolve to OpenAlex IDs\n- **If matching fails**: try fuzzy name matching as backup\n\n### Step 3: Medium run on N=500 journals (~45 min including API)\n- Acquire full citation matrix, verify N_active ≥ 400\n- Run complete evaluation pipeline\n- **Check**: at least 3 suppressed journals are in active node set\n- **Check**: curl detector AUC > 0.5 (beats random)\n- **Check**: synthetic injection k=5 cyclic AUC > 0.6 at w_factor=1.0\n- If these pass: confidence that full N=3000 run will produce valid results\n\n### Step 4: Full run on N=3000 journals (2-3 hours total)\n- Run all 9 phases end-to-end\n- Monitor: n_triangles, lsqr convergence (check result[1] code: 0=converged)\n- lsqr convergence code: 1=first-order optim, 2=relative change small — any of 0-3 is acceptable\n- **Critical check before Phase 9**: verify labels_stacking.sum() >= 5 for meaningful AUC\n  - If < 5: fall back to labels_all (all suppressions)\n\n### Ongoing checks throughout\n- B1 @ B2 == 0 (tolerance 1e-10): fundamental Hodge identity\n- energy fractions sum to 1.0 ± 0.01\n- lsqr exit codes not 6 or 7 (abnormal termination)\n- No NaN/Inf in z_scores (guard: replace with null_mean if std=0)\n- method_out.json is valid JSON before reporting success\n- Log intermediate sizes at each phase: N, E, T, time elapsed"
}
````

### [78] TOOL RESULT — Write · 2026-07-08 23:20:05 UTC

````
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_1/gen_plan/gen_plan_experiment_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Hodge-Curl Cartel Detector on Citation Networks\",\n  \"summary\": \"Build a journal citation network from OpenAlex, implement the combinatorial Hodge decomposition (gradient + curl + harmonic) on the net-flow matrix, use the per-node/triangle curl score as a manipulation detector, calibrate against a degree-preserving null, and compare head-to-head with CIDRE, reciprocity, within-group density, and PageRank on JCR-suppressed journal detection plus synthetic cartel injection tests.\",\n  \"runpod_compute_profile\": \"cpu_heavy\",\n  \"implementation_pseudocode\": \"# ============================================================\\n# ENVIRONMENT SETUP\\n# ============================================================\\n# pip install cidre pytspl pyalex scipy numpy networkx pandas\\n#             matplotlib scikit-learn tqdm requests aiohttp\\n#\\n# CIDRE: pip install cidre==0.0.1 (Python 3.7-3.11 compatible)\\n# pyalex: lightweight OpenAlex API client with pagination\\n# pytspl: clean Hodge decomposition library (get_gradient_flow/get_curl_flow)\\n# Note: OpenAlex API requires a free API key since Feb 2026.\\n#   Register at https://openalex.org/users and set env var OPENALEX_API_KEY\\n#   OR use mailto polite crawling: append ?mailto=researcher@example.com to all calls\\n\\n# ============================================================\\n# PHASE 0 — JCR GROUND TRUTH COMPILATION\\n# File: build_ground_truth.py\\n# ============================================================\\n# Compile suppressed journal ISSNs from public sources:\\n#\\n# Source A: CIDRE paper supplementary (Kojaku et al. 2021, Scientific Reports)\\n#   — 55 journals in 22 stacking groups, 2007-2019\\n#   — Hardcode known groups from paper Table S1 (journal names + ISSNs)\\n#   — These are the PRIMARY ground truth for citation STACKING (our focus)\\n#\\n# Source B: Retractionwatch/Clarivate public lists 2019-2025\\n#   Fetch and parse these public URLs for names+reasons:\\n#   - https://retractionwatch.com/2025/06/18/clarivate-impact-factor-suppression-list-2025-self-citation-stacking/\\n#   - https://scholarlykitchen.sspnet.org/2018/06/27/ (2018, 20 journals)\\n#   - https://retractionwatch.com/2021/06/30/ (2020, 10 journals)\\n#   - Clarivate Title Suppressions Zendesk page (if accessible)\\n#   Extract journal names and classify by reason (self-citation vs stacking)\\n#\\n# Output: suppressed_journals.json\\n# Schema: [{\\\"name\\\": str, \\\"issn_l\\\": str, \\\"year_suppressed\\\": int,\\n#            \\\"reason\\\": \\\"self_citation\\\" | \\\"citation_stacking\\\",\\n#            \\\"openalex_id\\\": str | null}]\\n#\\n# IMPORTANT SUBSET DISTINCTION:\\n#   label_stacking: only journals suppressed for citation stacking (cartel-type)\\n#   label_all: all suppressions (self-citation + stacking)\\n# Our primary evaluation uses label_stacking; report both.\\n\\n\\n# ============================================================\\n# PHASE 1 — BUILD JOURNAL CITATION NETWORK\\n# File: build_network.py\\n# ============================================================\\n# We build a journal×journal citation matrix C where\\n# C[i,j] = number of papers published in journal i in 2018-2020\\n#           that cite any paper published in journal j in 2016-2020.\\n# This mirrors the JIF 2-year citation window used by Clarivate.\\n#\\n# Step 1.1 — Get top journals from OpenAlex:\\n#   GET https://api.openalex.org/sources\\n#       ?filter=type:journal\\n#       &sort=cited_by_count:desc\\n#       &per_page=200\\n#       &select=id,display_name,issn_l,issn,topics.field.display_name,cited_by_count\\n#       &api_key={KEY}\\n#   Paginate to collect TOP_N=3000 journals. Save journals.json.\\n#\\n# Step 1.2 — Ensure suppressed journals are included:\\n#   For each ISSN in suppressed_journals.json NOT already in our set:\\n#       GET /sources?filter=issn:{issn_l}&select=id,display_name,cited_by_count\\n#       Add to journal set even if outside top 3000\\n#   Total: ~3100-3200 journals (N).\\n#\\n# Step 1.3 — Build work→journal lookup incrementally:\\n#   Maintain dict: work_id_to_journal = {}\\n#   For each journal j:\\n#       For each paper p published in journal j, years 2018-2020:\\n#           work_id_to_journal[p.id] = j.index\\n#\\n# Step 1.4 — Build citation matrix using async requests:\\n#   For each journal j in our set (async, concurrency=5, respect rate limit):\\n#       cursor = '*'\\n#       while cursor:\\n#           GET /works?filter=primary_location.source.id:{j.openalex_id},\\n#                       publication_year:2018-2020\\n#                   &select=id,referenced_works\\n#                   &per_page=200&cursor={cursor}\\n#                   &api_key={KEY}\\n#           For each paper p in response:\\n#               for ref_id in p.referenced_works:\\n#                   if ref_id in work_id_to_journal:\\n#                       C[j.index, work_id_to_journal[ref_id]] += 1\\n#                   else:\\n#                       unresolved_refs.add(ref_id)\\n#           cursor = meta.next_cursor\\n#\\n# Step 1.5 — Batch-resolve unresolved reference work IDs:\\n#   chunk_size = 100 (URL length limit)\\n#   for chunk in chunks(unresolved_refs, chunk_size):\\n#       GET /works?filter=ids.openalex:{id1}|{id2}|...\\n#                &select=id,primary_location.source.id\\n#       For each result: update work_id_to_journal[id] = source_idx\\n#   Re-sweep unresolved refs and update C matrix.\\n#\\n# Step 1.6 — Save network:\\n#   scipy.sparse.save_npz('data/citation_matrix.npz', C_csr)\\n#   journal_index.json: [{\\\"row\\\": int, \\\"openalex_id\\\": str, \\\"name\\\": str,\\n#                          \\\"issn_l\\\": str, \\\"field\\\": str}]\\n#\\n# MINI TEST (run first, ~20 min API time):\\n#   TOP_N=100, years=2019-2020, cursor_only 1 page per journal (200 papers max)\\n#   Expected: 100×100 matrix, ~50K-200K citations\\n#   Sanity checks:\\n#     - C.diagonal() should be ~0 or small (self-citation exists but we focus on pairs)\\n#     - High-cited journals (Nature, Science) should have high column sums\\n#     - Matrix should be highly asymmetric (C != C.T)\\n#\\n# SCALING: Full run with TOP_N=3000 may take 2-3 hours with async.\\n# If time is tight: use TOP_N=1000 for the evaluation, ensuring all suppressed journals included.\\n\\n\\n# ============================================================\\n# PHASE 2 — NETWORK PREPROCESSING\\n# File: preprocess.py\\n# ============================================================\\n# 2.1 Apply edge threshold to reduce noise:\\n#   THRESH = 3  # keep only edges where C[i,j] + C[j,i] >= THRESH\\n#   mask = (C + C.T) >= THRESH\\n#   C_thresh = C.multiply(mask)\\n#   # Reduces E dramatically; typical: 3M raw edges → 200K thresholded edges\\n#\\n# 2.2 Remove isolated nodes (no connections after thresholding)\\n#   active_nodes = np.where(np.asarray(C_thresh.sum(1)).squeeze() +\\n#                            np.asarray(C_thresh.sum(0)).squeeze() > 0)[0]\\n#   C_active = C_thresh[active_nodes][:, active_nodes]\\n#   N = len(active_nodes)\\n#\\n# 2.3 Compute net flow matrix:\\n#   Y = C_active - C_active.T  # antisymmetric N×N matrix\\n#   # Y[i,j] > 0 means i sends more citations to j than j to i\\n#\\n# 2.4 Build oriented edge list (canonical: i < j):\\n#   cx = C_active.tocoo()\\n#   edges_set = set()\\n#   for i, j in zip(cx.row, cx.col):\\n#       if i != j:\\n#           edges_set.add((min(i,j), max(i,j)))\\n#   edges = sorted(edges_set)  # list of (i,j) with i < j\\n#   E = len(edges)\\n#   edge_to_idx = {e: idx for idx, e in enumerate(edges)}\\n#\\n# 2.5 Build edge flow vector:\\n#   Y_dense = np.asarray(Y.todense())\\n#   Y_e = np.array([Y_dense[i,j] for (i,j) in edges])\\n#   # Y_e[e] > 0: net flow in canonical i→j direction\\n#\\n# Log: N, E, threshold used, network density\\n\\n\\n# ============================================================\\n# PHASE 3 — HODGE DECOMPOSITION\\n# File: hodge.py\\n# ============================================================\\n# 3.1 Build B1 — node×edge signed incidence matrix:\\n#   # B1[head, e] = +1, B1[tail, e] = -1 for canonical orientation (i→j, i<j)\\n#   rows_B1, cols_B1, data_B1 = [], [], []\\n#   for e_idx, (i, j) in enumerate(edges):\\n#       rows_B1.extend([i, j])\\n#       cols_B1.extend([e_idx, e_idx])\\n#       data_B1.extend([-1.0, +1.0])  # i is tail (-1), j is head (+1)\\n#   B1 = sparse.csr_matrix((data_B1, (rows_B1, cols_B1)), shape=(N, E))\\n#   # Shape: N×E. B1.T @ s gives node potential differences on edges.\\n#\\n# 3.2 Enumerate triangles (3-cliques) in the undirected thresholded graph:\\n#   adj_list = defaultdict(set)\\n#   for (i, j) in edges:\\n#       adj_list[i].add(j)\\n#       adj_list[j].add(i)\\n#\\n#   triangles = []\\n#   for (i, j) in edges:\\n#       # Find common neighbors k > j (canonical ordering i < j < k)\\n#       common = adj_list[i] & adj_list[j]\\n#       for k in common:\\n#           if k > j:\\n#               triangles.append((i, j, k))\\n#\\n#   T = len(triangles)\\n#   # Performance note: For E=200K edges, expect ~few hundred K triangles\\n#   # If T > 5M: apply secondary threshold (keep only edges C[i,j]+C[j,i] >= 10)\\n#   # Time estimate: <60s for T < 2M\\n#\\n# 3.3 Build B2 — edge×triangle incidence matrix:\\n#   # Orientation convention: triangle (i,j,k) with i<j<k has circuit i→j→k→i\\n#   # B2[e_ij, t] = +1 (i→j matches circuit)\\n#   # B2[e_jk, t] = +1 (j→k matches circuit)\\n#   # B2[e_ik, t] = -1 (circuit goes k→i, but edge is oriented i→k)\\n#   rows_B2, cols_B2, data_B2 = [], [], []\\n#   for t_idx, (i, j, k) in enumerate(triangles):\\n#       # All three edge indices (all pairs with canonical orientation)\\n#       e_ij = edge_to_idx[(i, j)]\\n#       e_jk = edge_to_idx[(j, k)]\\n#       e_ik = edge_to_idx[(i, k)]\\n#       rows_B2.extend([e_ij, e_jk, e_ik])\\n#       cols_B2.extend([t_idx, t_idx, t_idx])\\n#       data_B2.extend([+1.0, +1.0, -1.0])\\n#   B2 = sparse.csr_matrix((data_B2, (rows_B2, cols_B2)), shape=(E, T))\\n#\\n#   # VERIFY: B1 @ B2 should be (near) zero matrix:\\n#   check = B1 @ B2  # N×T matrix, should be all zeros\\n#   assert np.allclose(check.data, 0, atol=1e-10), \\\"Hodge identity violated!\\\"\\n#\\n# 3.4 Solve for gradient potential (HodgeRank prestige scores):\\n#   from scipy.sparse.linalg import lsqr\\n#   # Solve: min_s ||B1^T @ s - Y_e||^2  (B1^T is E×N)\\n#   # s_star is N-vector of prestige potentials per journal\\n#   result = lsqr(B1.T, Y_e, damp=1e-6, atol=1e-10, btol=1e-10, iter_lim=20000)\\n#   s_star = result[0]  # prestige/potential score per journal\\n#   Y_grad = B1.T @ s_star  # E-vector: gradient component of flow\\n#   # s_star is the HodgeRank prestige ranking (analog of Eigenfactor)\\n#\\n# 3.5 Solve for curl component:\\n#   residual = Y_e - Y_grad  # residual = curl + harmonic\\n#   # Solve: min_h ||B2^T @ h - residual||^2 (B2^T is T×E)\\n#   result_curl = lsqr(B2.T, residual, damp=1e-6, atol=1e-10, iter_lim=20000)\\n#   h_star = result_curl[0]  # T-vector: triangle potentials\\n#   Y_curl = B2 @ h_star   # E-vector: curl component\\n#   Y_harm = residual - Y_curl  # E-vector: harmonic component\\n#\\n# 3.6 Compute energy fractions (orthogonality check):\\n#   total_energy = np.dot(Y_e, Y_e)\\n#   grad_fraction = np.dot(Y_grad, Y_grad) / total_energy\\n#   curl_fraction = np.dot(Y_curl, Y_curl) / total_energy\\n#   harm_fraction = np.dot(Y_harm, Y_harm) / total_energy\\n#   cross_check = abs(grad_fraction + curl_fraction + harm_fraction - 1.0)\\n#   assert cross_check < 0.01, f\\\"Non-orthogonal decomposition: {cross_check}\\\"\\n#\\n# 3.7 Compute per-triangle curl values:\\n#   # triangle_curl[t] = B2^T @ Y_e evaluated at triangle t\\n#   triangle_curls = B2.T @ Y_e  # T-vector\\n#   # Interpretation: large |triangle_curl[t]| = this triangle carries strong\\n#   # circulating flow inconsistent with any global prestige ordering\\n#\\n# 3.8 Compute per-node curl scores:\\n#   node_curl_sum = np.zeros(N)\\n#   node_tri_count = np.zeros(N, dtype=int)\\n#   for t_idx, (i, j, k) in enumerate(triangles):\\n#       val = abs(triangle_curls[t_idx])\\n#       for node in [i, j, k]:\\n#           node_curl_sum[node] += val\\n#           node_tri_count[node] += 1\\n#   node_curl_score = node_curl_sum / (node_tri_count + 1e-10)\\n#   # Zero-impute nodes with no triangles (isolated from any 3-cycle)\\n#\\n# 3.9 Degree-normalized curl score (reduces degree bias):\\n#   degree = np.asarray(C_active.sum(1)).squeeze() + \\\\\\n#             np.asarray(C_active.sum(0)).squeeze()\\n#   node_curl_norm = node_curl_score / (np.log1p(degree) + 1e-10)\\n\\n\\n# ============================================================\\n# PHASE 4 — NULL MODEL CALIBRATION\\n# File: null_model.py\\n# ============================================================\\n# Degree-preserving row-permutation null:\\n#   For each null sample:\\n#     C_null = C_active.tolil().copy()\\n#     For each row i:\\n#         cols = C_null[i].nonzero()[1]\\n#         vals = np.asarray(C_null[i, cols]).squeeze()\\n#         np.random.shuffle(vals)\\n#         C_null[i, cols] = vals  # shuffle which journal gets each weight\\n#     Convert to CSR, recompute Y, build Y_e, run Hodge, get node_curl_score\\n#\\n# n_null = 500 (use 200 if slow; N=3000 run should still be <30 min for 500)\\n# Collect null_node_curl_scores: shape (n_null, N)\\n#\\n# Per-node statistics:\\n#   null_mean = null_node_curl_scores.mean(0)  # N-vector\\n#   null_std  = null_node_curl_scores.std(0) + 1e-10\\n#   z_score   = (node_curl_score - null_mean) / null_std  # z-score per journal\\n#   p_value   = (null_node_curl_scores >= node_curl_score).mean(0)  # fraction exceeding\\n#\\n# Also compute degree-corrected null for between-community edges:\\n#   Use the Louvain field communities as block labels\\n#   For community-preserving null: only permute within-community edges\\n#   Compare community-preserving z-score vs degree-only z-score\\n\\n\\n# ============================================================\\n# PHASE 5 — BASELINES\\n# File: baselines.py\\n# ============================================================\\n# 5.1 Reciprocity score per node:\\n#   For each node i:\\n#     partners_j = nonzero columns in row i of C_active\\n#     reci_vals = [min(C[i,j], C[j,i]) / (C[i,j] + C[j,i] + 1e-10) for j in partners_j]\\n#     weights = [(C[i,j] + C[j,i]) for j in partners_j]\\n#     reciprocity[i] = weighted mean of reci_vals  # high = symmetric exchange\\n#\\n# 5.2 Field community detection and within-group density:\\n#   adj_undirected = (C_active + C_active.T) / 2\\n#   G_nx = networkx.from_scipy_sparse_array(adj_undirected)\\n#   communities = networkx.community.louvain_communities(G_nx, seed=42, weight='weight')\\n#   # Assign community index per node\\n#   comm_label = np.zeros(N, dtype=int)\\n#   for c_idx, comm in enumerate(communities):\\n#       for node in comm:\\n#           comm_label[node] = c_idx\\n#   # Compute within-community density per node:\\n#   for node in range(N):\\n#       c = comm_label[node]\\n#       group = list(communities[c])\\n#       internal = C_active[group][:, group].sum()\\n#       possible = len(group) * (len(group) - 1)\\n#       density_score[node] = internal / (possible + 1e-10)\\n#\\n# 5.3 PageRank:\\n#   G_directed = networkx.from_scipy_sparse_array(C_active, create_using=networkx.DiGraph)\\n#   pr = networkx.pagerank(G_directed, alpha=0.85, max_iter=200)\\n#   pagerank_scores = np.array([pr[n] for n in range(N)])\\n#\\n# 5.4 CIDRE:\\n#   import cidre\\n#   # Provide field labels from Louvain OR from OpenAlex field assignments\\n#   field_membership = comm_label  # or: map OpenAlex field → int\\n#   alg = cidre.Cidre(group_membership=field_membership)\\n#   try:\\n#       cidre_groups = alg.detect(C_active, threshold=0.15)\\n#   except Exception:\\n#       # Try different thresholds if no groups found\\n#       for thresh in [0.10, 0.05, 0.01]:\\n#           cidre_groups = alg.detect(C_active, threshold=thresh)\\n#           if cidre_groups:\\n#               break\\n#   # Convert group membership to per-node anomaly score:\\n#   cidre_scores = np.zeros(N)\\n#   for group in cidre_groups:\\n#       for node_id, score in group.donors.items():\\n#           cidre_scores[node_id] = max(cidre_scores[node_id], score)\\n#       for node_id, score in group.recipients.items():\\n#           cidre_scores[node_id] = max(cidre_scores[node_id], score)\\n#   cidre_binary = (cidre_scores > 0).astype(int)\\n#   # IMPORTANT: CIDRE returns sparse binary flags (0/positive).\\n#   # For AUC with binary predictions use cidre_binary as score too.\\n\\n\\n# ============================================================\\n# PHASE 6 — EVALUATION ON JCR GROUND TRUTH\\n# File: evaluate.py\\n# ============================================================\\n# 6.1 Build label arrays:\\n#   labels_stacking = np.zeros(N)  # 1 = suppressed for citation stacking\\n#   labels_all = np.zeros(N)       # 1 = suppressed for any reason\\n#   for journal_info in suppressed_journals:\\n#       if journal_info['openalex_id'] in active_journal_set:\\n#           idx = journal_to_idx[journal_info['openalex_id']]\\n#           if journal_info['reason'] == 'citation_stacking':\\n#               labels_stacking[idx] = 1\\n#           labels_all[idx] = 1\\n#   # Log: how many suppressed journals matched to active network nodes\\n#\\n# 6.2 Compute metrics for each method on labels_stacking (primary):\\n#   from sklearn.metrics import roc_auc_score, average_precision_score\\n#   import numpy as np\\n#\\n#   scores_dict = {\\n#       'hodge_curl_raw':     node_curl_score,\\n#       'hodge_curl_z':       z_score,          # null-calibrated\\n#       'hodge_curl_norm':    node_curl_norm,    # degree-normalized\\n#       'reciprocity':        reciprocity_score,\\n#       'within_group_density': density_score,\\n#       'pagerank':           pagerank_scores,\\n#       'cidre':              cidre_scores,\\n#   }\\n#\\n#   B = 2000  # bootstrap resamples\\n#   results = {}\\n#   for method, scores in scores_dict.items():\\n#       if labels_stacking.sum() < 2:\\n#           print(\\\"Too few positives for AUC; continuing with labels_all\\\")\\n#           labels_eval = labels_all\\n#       else:\\n#           labels_eval = labels_stacking\\n#\\n#       auc_roc = roc_auc_score(labels_eval, scores)\\n#       auc_pr  = average_precision_score(labels_eval, scores)\\n#\\n#       # Precision@k\\n#       ranked = np.argsort(scores)[::-1]\\n#       prec_at_k = {k: float(labels_eval[ranked[:k]].mean())\\n#                    for k in [10, 50, 100]}\\n#\\n#       # Bootstrap CI\\n#       boot_aucs = []\\n#       for _ in range(B):\\n#           idx = np.random.randint(0, len(labels_eval), len(labels_eval))\\n#           if labels_eval[idx].sum() > 0:\\n#               boot_aucs.append(roc_auc_score(labels_eval[idx], scores[idx]))\\n#       ci = (np.percentile(boot_aucs, 2.5), np.percentile(boot_aucs, 97.5))\\n#\\n#       results[method] = {\\n#           'auc': float(auc_roc), 'auc_pr': float(auc_pr),\\n#           'prec_at_k': prec_at_k, 'ci': list(ci)\\n#       }\\n#\\n# 6.3 Key comparison test (DeLong via permutation):\\n#   n_perm = 10000\\n#   delta_obs = roc_auc_score(labels_eval, z_score) - roc_auc_score(labels_eval, cidre_scores)\\n#   perm_deltas = []\\n#   for _ in range(n_perm):\\n#       perm = np.random.permutation(len(labels_eval))\\n#       d = roc_auc_score(labels_eval[perm], z_score) - \\\\\\n#           roc_auc_score(labels_eval[perm], cidre_scores)\\n#       perm_deltas.append(d)\\n#   p_val_comparison = (np.abs(perm_deltas) >= np.abs(delta_obs)).mean()\\n#   # Report: delta_obs, p_val_comparison, and whether curl CI excludes CIDRE AUC\\n\\n\\n# ============================================================\\n# PHASE 7 — SYNTHETIC CARTEL INJECTION\\n# File: synthetic_injection.py\\n# ============================================================\\n# Inject cartels into the REAL network and measure detection.\\n# This tests the core claim: curl detects manipulation at lower density than CIDRE/density.\\n#\\n# 7.1 Injection functions:\\n#   def inject_cyclic_cartel(C, k, w, exclude_nodes=None):\\n#       \\\"\\\"\\\"k-node ring: A→B→C→...→A\\\"\\\"\\\"\\n#       nodes = random_sample(N, k, exclude=exclude_nodes)\\n#       C = C.tolil().copy()\\n#       for idx in range(k):\\n#           u, v = nodes[idx], nodes[(idx+1) % k]\\n#           C[u, v] += w\\n#       return C.tocsr(), set(nodes)\\n#\\n#   def inject_reciprocal_cartel(C, k, w, exclude_nodes=None):\\n#       \\\"\\\"\\\"k-node clique: all pairs exchange\\\"\\\"\\\"\\n#       nodes = random_sample(N, k, exclude=exclude_nodes)\\n#       C = C.tolil().copy()\\n#       for u in nodes:\\n#           for v in nodes:\\n#               if u != v:\\n#                   C[u, v] += w\\n#       return C.tocsr(), set(nodes)\\n#\\n# 7.2 Sweep parameters:\\n#   mean_edge_weight = C_active.data.mean()  # baseline weight scale\\n#   k_values    = [3, 5, 10, 20]\\n#   w_factors   = [0.01, 0.05, 0.1, 0.3, 0.5, 1.0, 2.0]  # × mean_edge_weight\\n#   cartel_types = ['cyclic', 'reciprocal']\\n#   n_repeats   = 20  # independent random placements per condition\\n#\\n# 7.3 For each (cartel_type, k, w_factor, repeat):\\n#   w = w_factor * mean_edge_weight\\n#   # Exclude known suppressed journals from injection targets\\n#   exclude = suppressed_node_set\\n#   if cartel_type == 'cyclic':\\n#       C_mod, injected_nodes = inject_cyclic_cartel(C_active, k, w, exclude)\\n#   else:\\n#       C_mod, injected_nodes = inject_reciprocal_cartel(C_active, k, w, exclude)\\n#\\n#   # Recompute Hodge on modified network (fast: reuse B1, B2 with updated Y_e)\\n#   Y_mod = C_mod - C_mod.T\\n#   Y_e_mod = [Y_mod[i,j] for (i,j) in edges]\\n#   s_mod  = lsqr(B1.T, Y_e_mod)[0]\\n#   Y_grad_mod = B1.T @ s_mod\\n#   res_mod = Y_e_mod - Y_grad_mod\\n#   h_mod   = lsqr(B2.T, res_mod)[0]\\n#   Y_curl_mod = B2 @ h_mod\\n#   # node curl from triangle curls on Y_e_mod\\n#   tc_mod = B2.T @ np.array(Y_e_mod)\\n#   node_curl_mod = compute_node_curl(tc_mod, triangles, N)\\n#\\n#   # Detection AUC: injected nodes = 1, others = 0\\n#   binary_labels = np.zeros(N)\\n#   for n in injected_nodes: binary_labels[n] = 1\\n#\\n#   auc_curl    = roc_auc_score(binary_labels, node_curl_mod)\\n#   auc_density = roc_auc_score(binary_labels, density_score_updated)\\n#   # Rerun CIDRE on modified network:\\n#   cidre_mod  = run_cidre(C_mod, field_membership)\\n#   auc_cidre  = roc_auc_score(binary_labels, cidre_mod)\\n#   auc_recip  = roc_auc_score(binary_labels, compute_reciprocity(C_mod))\\n#\\n#   record = {\\n#       'cartel_type': cartel_type, 'k': k, 'w_factor': w_factor,\\n#       'repeat': repeat,\\n#       'auc_hodge_curl': auc_curl, 'auc_cidre': auc_cidre,\\n#       'auc_density': auc_density, 'auc_reciprocity': auc_recip\\n#   }\\n#\\n# 7.4 Aggregate: for each (cartel_type, k, w_factor), compute mean ± std AUC over repeats\\n# PREDICTION: Hodge-curl AUC degrades more slowly than CIDRE/density as w_factor → 0\\n# PREDICTION: cyclic (curl-only) cartel detected with much higher AUC by curl vs density\\n\\n\\n# ============================================================\\n# PHASE 8 — CONFOUND TEST\\n# File: confound.py\\n# ============================================================\\n# Test the key claim: dense legitimate communities have LOW curl; cartels have HIGH curl.\\n# This separates curl from density — the main novel claim of the hypothesis.\\n#\\n# 8.1 Identify dense legitimate clusters:\\n#   # Use the Louvain communities (computed in Phase 5)\\n#   # Exclude any community containing >=1 suppressed journal\\n#   legitimate_communities = [\\n#       comm for comm in communities\\n#       if not any(node in suppressed_node_set for node in comm)\\n#       and len(comm) >= 5\\n#   ]\\n#   # Rank by internal citation density, take top 5\\n#   top_legit = sorted(legitimate_communities,\\n#                       key=lambda g: C_active[list(g)][:,list(g)].sum() / (len(g)*(len(g)-1)),\\n#                       reverse=True)[:5]\\n#\\n# 8.2 Identify known cartel groups:\\n#   # From suppressed_journals, known citation-stacking groups (from CIDRE paper Table S1)\\n#   # Group suppressed journals by their stacking group (they come in pairs/triples)\\n#   # Each stacking group is a cluster of 2-10 journals that cite each other\\n#   cartel_groups = [list_of_group for group in known_stacking_groups\\n#                    if all nodes resolved to our network]\\n#\\n# 8.3 Compute group-level metrics for each cluster:\\n#   def group_metrics(group_nodes):\\n#       G_set = set(group_nodes)\\n#       T_sub = [(i,j,k) for (i,j,k) in triangles\\n#                if i in G_set and j in G_set and k in G_set]\\n#       internal_curl = sum(abs(triangle_curls[t]) for t in range(T) if triangles[t] in T_sub_set)\\n#       density = C_active[group_nodes][:,group_nodes].sum() / (len(G_set)*(len(G_set)-1)+1e-10)\\n#       mean_recip = reciprocity_score[list(G_set)].mean()\\n#       curl_frac = internal_curl / (density * len(G_set)**2 + 1e-10)\\n#       return {'density': density, 'curl': internal_curl, 'curl_fraction': curl_frac,\\n#               'mean_reciprocity': mean_recip, 'n_triangles': len(T_sub)}\\n#\\n# 8.4 Statistical tests:\\n#   # Mann-Whitney U for each metric (legit vs cartel):\\n#   from scipy.stats import mannwhitneyu\\n#   for metric in ['density', 'curl_fraction', 'mean_reciprocity']:\\n#       stat, p = mannwhitneyu([g[metric] for g in legit_metrics],\\n#                               [g[metric] for g in cartel_metrics],\\n#                               alternative='two-sided')\\n#       # Expected: density p > 0.05 (no separation), curl_fraction p < 0.05 (separates)\\n#\\n# 8.5 Ablation — partial correlation of curl score with suppressed label\\n#     after regressing out density and reciprocity:\\n#   from sklearn.linear_model import LinearRegression\\n#   X = np.stack([density_score, reciprocity_score], axis=1)\\n#   model = LinearRegression().fit(X, labels_all)\\n#   label_resid = labels_all - model.predict(X)\\n#   model2 = LinearRegression().fit(X, z_score)\\n#   curl_resid = z_score - model2.predict(X)\\n#   partial_r = np.corrcoef(curl_resid, label_resid)[0,1]\\n#   # Bootstrap CI for partial_r:\\n#   boot_rs = [np.corrcoef(curl_resid[idx], label_resid[idx])[0,1]\\n#              for idx in (np.random.randint(0, N, N) for _ in range(2000))]\\n#   partial_r_ci = (np.percentile(boot_rs, 2.5), np.percentile(boot_rs, 97.5))\\n\\n\\n# ============================================================\\n# PHASE 9 — FORMAT OUTPUT\\n# File: format_output.py\\n# ============================================================\\nimport json, numpy as np\\n\\n# Build method_out.json following the schema below\\n# All numpy floats must be cast to python float/int before JSON serialization\\n# Use float(x) for all numpy scalars\\n\\nresult = {\\n    \\\"network_stats\\\": {\\n        \\\"n_journals_raw\\\": int(TOP_N_requested),\\n        \\\"n_active_nodes\\\": int(N),\\n        \\\"n_edges_thresholded\\\": int(E),\\n        \\\"n_triangles\\\": int(T),\\n        \\\"edge_threshold\\\": int(THRESH),\\n        \\\"years\\\": \\\"2018-2020\\\",\\n        \\\"hodge_energy\\\": {\\n            \\\"grad_fraction\\\": float(grad_fraction),\\n            \\\"curl_fraction\\\": float(curl_fraction),\\n            \\\"harm_fraction\\\": float(harm_fraction)\\n        }\\n    },\\n    \\\"hodge_scores\\\": [\\n        {\\\"journal_idx\\\": int(i),\\n         \\\"journal_name\\\": str(journal_names[i]),\\n         \\\"issn_l\\\": str(issn_map[i]),\\n         \\\"prestige_score\\\": float(s_star[i]),\\n         \\\"node_curl_raw\\\": float(node_curl_score[i]),\\n         \\\"node_curl_z\\\": float(z_score[i]),\\n         \\\"node_curl_norm\\\": float(node_curl_norm[i]),\\n         \\\"p_value_null\\\": float(p_value[i]),\\n         \\\"is_suppressed_stacking\\\": bool(labels_stacking[i]),\\n         \\\"is_suppressed_any\\\": bool(labels_all[i])}\\n        for i in range(N)\\n    ],\\n    \\\"baseline_scores\\\": [\\n        {\\\"journal_idx\\\": int(i),\\n         \\\"cidre_score\\\": float(cidre_scores[i]),\\n         \\\"reciprocity\\\": float(reciprocity_score[i]),\\n         \\\"group_density\\\": float(density_score[i]),\\n         \\\"pagerank\\\": float(pagerank_scores[i])}\\n        for i in range(N)\\n    ],\\n    \\\"evaluation\\\": {\\n        \\\"label_primary\\\": \\\"citation_stacking\\\",\\n        \\\"n_positives_stacking\\\": int(labels_stacking.sum()),\\n        \\\"n_positives_all\\\": int(labels_all.sum()),\\n        \\\"methods\\\": results,  # from Phase 6\\n        \\\"curl_vs_cidre_delta_auc\\\": float(delta_obs),\\n        \\\"p_value_comparison\\\": float(p_val_comparison)\\n    },\\n    \\\"synthetic_injection\\\": synthetic_records,  # list from Phase 7\\n    \\\"confound_test\\\": {\\n        \\\"legit_clusters\\\": legit_metrics_list,\\n        \\\"cartel_groups\\\": cartel_metrics_list,\\n        \\\"mannwhitney_density_p\\\": float(p_density),\\n        \\\"mannwhitney_curl_p\\\": float(p_curl),\\n        \\\"partial_corr_curl\\\": float(partial_r),\\n        \\\"partial_corr_ci\\\": [float(partial_r_ci[0]), float(partial_r_ci[1])]\\n    },\\n    \\\"top_triangles_by_curl\\\": [\\n        {\\\"nodes\\\": [int(i), int(j), int(k)],\\n         \\\"journal_names\\\": [journal_names[i], journal_names[j], journal_names[k]],\\n         \\\"curl_value\\\": float(triangle_curls[t_idx]),\\n         \\\"any_suppressed\\\": bool(labels_all[[i,j,k]].any())}\\n        for t_idx, (i,j,k) in sorted(enumerate(triangles),\\n                                     key=lambda x: abs(triangle_curls[x[0]]),\\n                                     reverse=True)[:50]\\n    ],\\n    \\\"prestige_ranking_top100\\\": [\\n        {\\\"rank\\\": r+1,\\n         \\\"journal_name\\\": journal_names[rank_idx],\\n         \\\"prestige_score\\\": float(s_star[rank_idx]),\\n         \\\"curl_z_score\\\": float(z_score[rank_idx]),\\n         \\\"is_suppressed_any\\\": bool(labels_all[rank_idx])}\\n        for r, rank_idx in enumerate(np.argsort(s_star)[::-1][:100])\\n    ]\\n}\\nwith open('method_out.json', 'w') as f:\\n    json.dump(result, f, indent=2)\\nprint(\\\"Done. method_out.json written.\\\")\",\n  \"fallback_plan\": \"## Fallback A — Simulated journal network if OpenAlex API is unavailable or slow\\n\\nIf the OpenAlex API data acquisition cannot complete within 2 hours (e.g., rate limits, auth issues, or data volume), replace Phase 1 with a synthetic network generator that still produces realistic properties:\\n\\n```python\\ndef generate_synthetic_citation_network(N=500, n_fields=10, n_cartels=5, cartel_size=5, seed=42):\\n    # Create a hierarchical prestige structure (DAG-like with noise)\\n    # N journals in n_fields communities\\n    # Add within-field citations (high density), cross-field citations (low density)\\n    # Inject n_cartels cyclic/reciprocal groups\\n    # Return C sparse matrix + ground truth labels\\n```\\n\\nWith a synthetic network, all downstream phases (Hodge decomposition, CIDRE, evaluation, synthetic injection) remain identical. The confound test and synthetic injection phases are especially valid on synthetic data. **Report clearly** that ground truth evaluation uses synthetic cartels, not real JCR suppressions.\\n\\n## Fallback B — If CIDRE installation fails\\n\\nCIDRE v0.0.1 requires Python 3.7-3.9. If the executor environment has Python 3.10+ and CIDRE fails, implement a simplified CIDRE-like baseline manually:\\n\\n```python\\ndef simple_cidre_baseline(C, group_membership):\\n    # For each community block:\\n    # Expected_ij = degree_i * degree_j / total_weight (Poisson null)\\n    # Score_ij = C[i,j] / Expected_ij\\n    # Node anomaly score = max over neighbors of Score_ij within same community\\n    # This captures the core CIDRE idea without the full SBM fit\\n```\\n\\nLabel this `cidre_approx` in results. Try `pip install cidre --python-version 3.9` in a venv if the system Python is newer.\\n\\n## Fallback C — If triangle enumeration is too slow (E > 500K)\\n\\nApply a stricter edge threshold (THRESH=10 instead of 3). This reduces E dramatically while retaining only the citation relationships strong enough to form manipulation signals. Journal pairs with < 10 mutual citations are unlikely to represent structured cartels. Alternatively, limit triangle enumeration to nodes within the same Louvain community (cartels typically operate within-field), which reduces the effective graph size by ~10× while preserving most relevant triangles.\\n\\n## Fallback D — Simplified curl score without full B2 construction\\n\\nIf B2 construction is too memory-intensive (T > 10M triangles), compute a direct triangle-aggregation score without building the sparse matrix:\\n\\n```python\\n# Direct triangle curl score: skip B2, iterate triangles directly\\nnode_curl = np.zeros(N)\\nfor (i, j, k) in triangles:\\n    tc = Y_net[i,j] + Y_net[j,k] - Y_net[i,k]  # signed triangle curl\\n    node_curl[i] += abs(tc)\\n    node_curl[j] += abs(tc)\\n    node_curl[k] += abs(tc)\\n# Skip the B2 @ lsqr projection step; use raw triangle sum as curl score\\n```\\n\\nThis is equivalent to the projection for scoring purposes (the projected curl and raw triangle sum correlate highly). Report that the simplified version was used.\\n\\n## Fallback E — Minimal viable output if time runs short\\n\\nPrioritize in this order:\\n1. Network construction + Hodge decomposition on top-500 journals (all phases)\\n2. Evaluation on JCR ground truth with bootstrap CIs\\n3. Synthetic injection for cyclic cartels at k=5 only\\n4. Skip confound test if <30 min remain\\n\\nAlways write method_out.json with whatever results are available, marking missing fields as null rather than omitting them.\",\n  \"testing_plan\": \"## Testing Strategy: Mini → Medium → Full\\n\\n### Step 0: Smoke test on tiny synthetic graph (~2 min)\\nBefore any data acquisition, run a unit test of the Hodge decomposition on a hand-crafted 6-node graph with one known cyclic cartel:\\n\\n```python\\n# Synthetic test: 6 nodes\\n# Hierarchical part: 0→1→2→3 (prestige chain)\\n# Cartel: 3→4→5→3 (cyclic with weight 10)\\nC_test = sparse.lil_matrix((6,6))\\nC_test[0,1]=100; C_test[1,2]=80; C_test[2,3]=60; C_test[3,4]=5; C_test[4,5]=5; C_test[5,3]=5\\nC_test = C_test.tocsr()\\n# Expected: nodes 3,4,5 get HIGH curl score; nodes 0,1,2 get LOW curl score\\n# Expected energy: grad_fraction > 0.8 (mostly hierarchical)\\n# Verify B1@B2 == 0 (Hodge identity)\\n# Verify s_star[0] > s_star[3] (foundational nodes have higher prestige)\\n```\\n\\n### Step 1: Mini run on N=100 journals (no API — use cached/synthetic) (~10 min)\\n- If OpenAlex API is available: fetch top 100 journals, 1 page of papers each\\n- Verify citation matrix is non-zero, asymmetric\\n- Run all Hodge phases, check energy fractions sum to ~1.0\\n- Verify z_scores are computable (null model runs)\\n- Run CIDRE on the 100-journal matrix; verify it returns some groups or empty list\\n- Run all 6 baselines without errors\\n- Write a stub method_out.json — check schema is valid JSON\\n- **Key signals**: grad_fraction > 0.5 (citation networks are mostly hierarchical); some nodes have z_score > 2\\n\\n### Step 2: Ground truth compilation test (~10 min)\\n- Verify suppressed_journals.json is written with ≥20 entries\\n- Verify ISSNs are valid format (4-digit-hyphen-4-digit)\\n- Test ISSN matching: at least 5 suppressed journals should resolve to OpenAlex IDs\\n- **If matching fails**: try fuzzy name matching as backup\\n\\n### Step 3: Medium run on N=500 journals (~45 min including API)\\n- Acquire full citation matrix, verify N_active ≥ 400\\n- Run complete evaluation pipeline\\n- **Check**: at least 3 suppressed journals are in active node set\\n- **Check**: curl detector AUC > 0.5 (beats random)\\n- **Check**: synthetic injection k=5 cyclic AUC > 0.6 at w_factor=1.0\\n- If these pass: confidence that full N=3000 run will produce valid results\\n\\n### Step 4: Full run on N=3000 journals (2-3 hours total)\\n- Run all 9 phases end-to-end\\n- Monitor: n_triangles, lsqr convergence (check result[1] code: 0=converged)\\n- lsqr convergence code: 1=first-order optim, 2=relative change small — any of 0-3 is acceptable\\n- **Critical check before Phase 9**: verify labels_stacking.sum() >= 5 for meaningful AUC\\n  - If < 5: fall back to labels_all (all suppressions)\\n\\n### Ongoing checks throughout\\n- B1 @ B2 == 0 (tolerance 1e-10): fundamental Hodge identity\\n- energy fractions sum to 1.0 ± 0.01\\n- lsqr exit codes not 6 or 7 (abnormal termination)\\n- No NaN/Inf in z_scores (guard: replace with null_mean if std=0)\\n- method_out.json is valid JSON before reporting success\\n- Log intermediate sizes at each phase: N, E, T, time elapsed\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
````

### [79] ASSISTANT · 2026-07-08 23:20:25 UTC

```
The plan has been written to `.terminal_claude_agent_struct_out.json`. Here's what the plan covers:

**Title**: Hodge-Curl Cartel Detector on Citation Networks

**Key research findings incorporated**:
- **CIDRE**: `pip install cidre==0.0.1`, takes scipy CSR matrix, requires `group_membership` array for community-aware null model, returns per-journal donor/recipient scores
- **OpenAlex API**: requires free API key (since Feb 2026), 100 req/s limit, `referenced_works` field on works endpoint enables citation matrix construction
- **pytspl**: provides `get_gradient_flow(B1, Y_e)` and `get_curl_flow(B2, Y_e)` — clean Hodge decomposition library
- **JCR ground truth**: 227 journals suppressed 2007-2019 (55 for stacking in 22 groups = primary positives), 2019-2025 additions from Retractionwatch public lists

**9-phase plan**:
1. JCR ground truth compilation (Retractionwatch + CIDRE paper Table S1)
2. Journal citation matrix via OpenAlex API (async, top 3000 journals, 2018-2020 window)
3. Network preprocessing (edge threshold, antisymmetric Y matrix, edge list)
4. Hodge decomposition (B1/B2 incidence matrices with correct sign conventions, lsqr gradient/curl solve, per-triangle and per-node curl scores)
5. Null model calibration (500 degree-preserving shuffles, z-scores, p-values)
6. Baselines (CIDRE, reciprocity, within-group density, PageRank)
7. JCR evaluation (AUC-ROC, AUC-PR, precision@k, bootstrap CIs, permutation test vs CIDRE)
8. Synthetic injection sweep (cyclic vs reciprocal, k∈{3,5,10,20}, w∈{0.01×–2×})
9. Confound test (dense legitimate communities vs cartels, Mann-Whitney, partial correlation ablation)

**Compute profile**: `cpu_heavy` — pure sparse linear algebra (scipy lsqr), no GPU needed.
```

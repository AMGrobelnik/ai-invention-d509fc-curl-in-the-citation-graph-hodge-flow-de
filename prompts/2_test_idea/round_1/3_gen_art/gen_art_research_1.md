# gen_art_research_1 — test_idea

> Phase: `invention_loop` · round 1 · `gen_art`
> Run: `run_io13l_LyCX8s` — Curl in the Citation Graph: Hodge Flow Decomposition Detects Citation Cartels via Field-Aware Calibration
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_research_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-07-08 23:22:10 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: An artifact executor (Step 3.3: GEN_ART in the invention loop)

Executing a plan to produce a concrete artifact.
GEN_PAPER_TEXT will use your artifact in the next paper draft.

Rigorous artifact with clear results → strong paper. Sloppy artifact → misdirected research.
</your_role>
</ai_inventor_context>

<task>
Conduct thorough, unbiased research on the given topic.
Adapt your investigation approach based on the research question and domain.
</task>

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

<critical_requirements>
1. SOURCE DIVERSITY - Consult MANY sources (10+), not just the first few results
2. AVOID SELECTION BIAS - Actively seek contradicting viewpoints, not just confirming ones
3. TRIANGULATE - Cross-reference claims across multiple independent sources
4. ACKNOWLEDGE UNCERTAINTY - Be honest about confidence levels and limitations
5. SYNTHESIZE - Produce a coherent answer that accounts for conflicting evidence
</critical_requirements>

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

Read and STRICTLY follow these skills: aii-web-tools.

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_1/gen_art/gen_art_research_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_1/gen_art/gen_art_research_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_1/gen_art/gen_art_research_1/file.py`, `/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_1/gen_art/gen_art_research_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_io13l_LyCX8s/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. Use it for prior work and the field's landscape to ground your research.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>

<artifact_plan>
id: gen_plan_research_1_idx1
type: research
title: Hodge Decomposition & Citation Cartel Detection Specs
summary: >-
  Gather precise technical specifications for HodgeRank/Hodge decomposition on graphs, CIDRE's algorithm and data, the 2025
  circular-flow decomposition papers, Clarivate JCR suppression lists (2018-2025), and OpenAlex API endpoints for building
  a journal-level citation matrix.
runpod_compute_profile: cpu_light
question: >-
  What are the exact algorithmic, mathematical, and data specifications needed to implement the Helmholtz-Hodge citation-cartel
  detector: (1) the HodgeRank sparse least-squares system and curl extraction; (2) CIDRE's donor/recipient scoring, dcSBM
  null, and bundled dataset format; (3) the 2025 circular-flow decomposition papers' key equations and implementation notes;
  (4) Clarivate JCR suppressed-journal lists 2018-2025 and their format; (5) the OpenAlex API call pattern to build a journal×journal
  citation matrix?
research_plan: |-
  ## Overview

  This is a web-research artifact. The executor should produce `research_report.md` and `research_out.json`. All five topics must be covered in full; each section below gives concrete search queries, URLs to fetch, content to extract, and a fallback if the primary source is blocked.

  ---

  ## SECTION A — HodgeRank / Combinatorial Hodge Decomposition

  ### What to collect
  The executor needs the exact mathematical system, not a vague description.

  **A1. Primary source: Stanford PDF**
  Fetch `https://web.stanford.edu/~yyye/hodgeRank2011.pdf` using the `aii_fast_web_fetch.py` script (not WebFetch, which fails on raw PDFs). Then grep for:
  - `grep -P "(B_1|B1|boundary|coboundary|Laplacian|L_1|L1|least square|lsqr|gradient|curl|harmonic)" --context-chars 400`
  - The paper is Jiang, Lim, Yao, Ye, Mathematical Programming 2011.

  **A2. Backup source: alternative PDF**
  Fetch `https://geometry.stanford.edu/lgl_2024/papers/jlyy-lrcht-09/jlyy-lrcht-09.pdf` (preprint version) and grep similarly.

  **A3. Supplementary source: arXiv:1011.1716**
  Fetch `https://arxiv.org/pdf/1011.1716` — this is a companion tutorial paper on least-squares ranking on graphs that spells out boundary operators explicitly.

  **A4. What to extract and document (be precise)**

  - **Edge orientation convention**: Every undirected edge {i,j} is assigned a canonical orientation (e.g., i < j). The flow Y_ij on that edge is the net signed flow: Y_ij = W_ij - W_ji (difference of directed citation counts). This is the input to the decomposition.

  - **Boundary operator B₁** (size m×n, where m = #edges, n = #nodes): Row for edge e=(i→j) has +1 in column j and -1 in column i. Build as a scipy.sparse.csr_matrix.

  - **Boundary operator B₂** (size t×m, where t = #triangles): Row for triangle (i,j,k) has +1 for edges consistent with orientation of the triangle and -1 otherwise. Only needed for the curl projection.

  - **HodgeRank (gradient potential) least-squares system**:
    - Solve `min_s ‖B₁ᵀ s - Y‖₂²` (where s is an n-vector of node potentials).
    - Normal equations: `(B₁ B₁ᵀ) s = B₁ Y`, i.e., `L₀ s = B₁ Y` where L₀ = B₁ B₁ᵀ is the standard graph Laplacian.
    - L₀ is singular (null space = constant vector); solve with `scipy.sparse.linalg.lsqr` or pin one node to 0. Use `scipy.sparse.linalg.lsqr(B1, Y)` directly (it handles underdetermined/overdetermined systems robustly).
    - The gradient flow component is then `Y_grad = B₁ᵀ s`.

  - **Extracting the three components**:
    1. Gradient: `Y_grad = B₁ᵀ @ s` (projects onto gradient space)
    2. Curl residual: `Y_resid = Y - Y_grad`
    3. Curl (local): `Y_curl = B₂ᵀ @ (B₂ B₂ᵀ)⁺ @ B₂ @ Y_resid` (project residual onto image of B₂ᵀ). For practical purposes: solve `B₂ᵀ β = Y_resid` in least-squares, then `Y_curl = B₂ᵀ @ β`.
    4. Harmonic: `Y_harmonic = Y_resid - Y_curl` (lies in null space of both B₁ and B₂, i.e., null(L₁)).

  - **Curl per triangle**: For triangle (i,j,k) with canonical edge ordering, curl_triangle = Y_ij + Y_jk + Y_ki (sum of net flows around the loop). A non-zero value means the triangle is ranking-inconsistent.

  - **Isolated nodes**: Nodes with degree zero have no edges in B₁; they are trivially zero-potential and can be excluded or assigned potential 0.

  - **Normalization for edge energies**: The gradient energy is `‖Y_grad‖² / ‖Y‖²`, curl energy is `‖Y_curl‖² / ‖Y‖²`, harmonic energy is `‖Y_harmonic‖² / ‖Y‖²`. These sum to 1.

  **A5. Confirm with this search if PDFs are blocked**
  Search: `"HodgeRank" "B1" "boundary operator" "least squares" site:arxiv.org`
  Also search: `"Hodge decomposition" "citation" implementation python scipy`

  ---

  ## SECTION B — CIDRE Algorithm, Code, and Dataset

  ### What to collect

  **B1. GitHub repository**
  Fetch `https://github.com/skojaku/cidre` — extract:
  - Installation (`pip install cidre`)
  - API: what input format does `cidre.CIDRE` accept (scipy sparse CSR or NetworkX DiGraph)?
  - Key parameters (threshold controlling group tightness, significance level)
  - What the output object provides (detected groups, donor/recipient scores, p-values)

  **B2. Bundled data**
  Fetch `https://github.com/skojaku/cidre/tree/main/data/journal-citation` to list files.
  Then fetch the raw content of:
  - `https://raw.githubusercontent.com/skojaku/cidre/main/data/journal-citation/edge-table-2013.csv` — extract column names and first rows (citation from/to journal IDs, count, year)
  - `https://raw.githubusercontent.com/skojaku/cidre/main/data/journal-citation/journal_names.csv` — journal ID → name mapping
  - `https://raw.githubusercontent.com/skojaku/cidre/main/data/journal-citation/community-label.csv` — journal → field/community label

  If raw GitHub returns 429 (rate limit), use the GitHub API:
  `https://api.github.com/repos/skojaku/cidre/contents/data/journal-citation`

  **B3. CIDRE algorithm details (already found — record these precisely)**

  - **Donor score**: `x_d(i, U) = (1/s_i^out) Σ_{j∈U, j≠i} W_ij h(i,j)`
  - **Recipient score**: `x_r(i, U) = (1/s_i^in) Σ_{j∈U, j≠i} W_ji h(j,i)`
  - where `h(i,j)` is an indicator that edge (i,j) carries 'excessive' weight relative to the null model.
  - **dcSBM null**: Expected weight `λ_ij = (s_i^out * s_j^in * Λ_{g_i, g_j}) / (S_{g_i}^out * S_{g_j}^in)` clipped to `max(1, λ_ij)` to prevent false positives.
  - `Λ_{ab}` = total citations from community a to community b.
  - Edge weight follows Poisson(λ_ij) null; p-value = P(Poisson(λ) ≥ W_ij).
  - FDR correction: Benjamini-Hochberg at α = 0.01.

  **B4. Source paper for algorithm and dataset description**
  Fetch `https://pmc.ncbi.nlm.nih.gov/articles/PMC8282695/` (the PubMed Central open access version of the CIDRE Sci. Rep. paper).
  Grep for: `"Microsoft Academic Graph"`, `"MAG"`, `"dataset"`, `"journal"`.
  Record: the MAG snapshot date (Jan 30 2020), the number of papers (231,926,308), journals (48,821), and year range (2000-2019).

  **B5. Example notebook**
  Fetch `https://github.com/skojaku/cidre/blob/main/examples/example.ipynb` or the raw notebook.
  Extract the minimal working example: how to load the data, instantiate CIDRE, run detection, and access results.

  **B6. Confirm whether CIDRE's bundled 2013 citation data is the same MAG slice as used in the paper** (look for any README note in the repository).

  ---

  ## SECTION C — 2025 Circular-Flow Decomposition Papers

  ### C1. arXiv:2506.12546 — Circular Directional Flow Decomposition

  **Fetch**: `https://arxiv.org/html/2506.12546` (HTML version, easier to parse than PDF)
  Also try PDF: `https://arxiv.org/pdf/2506.12546`

  **Grep patterns** (use `aii_fast_web_fetch.py grep`):
  - `"minimum cost flow"`, `"BFF"`, `"balanced flow forwarding"`, `"circularity index"`, `"acyclic"`, `"decomposition"`, `"algorithm"`, `"scipy"`, `"python"`, `"code"`

  **Key equations already found (verify and expand)**:
  - Decomposition: `w = c + d` where c is balanced (∀i: Σⱼ c_ij = Σⱼ c_ji) and d is acyclic.
  - Constraint: `0 ≤ c_ij, d_ij ≤ w_ij` for all edges.
  - Circularity index: `CI = Σ c_ij / Σ w_ij`
  - BFF algorithm update rule: `a_ij(t) = a_i^out(t) * (w_ij / w_i^out)`, `a_i^out(t+1) = min(a_i^in(t), a_i^out(t))`
  - Maximum circularity: solve minimum cost flow problem; complexity O((m log n)(m + n log n))

  **What to extract additionally**:
  - Is there a GitHub repository linked in the paper? Check references and appendices.
  - Does the paper describe how to apply the decomposition at the subgraph level (for a group of journals)?
  - What is the relationship between CDFD's circularity index and HodgeRank's curl energy fraction? (They are related but not identical — CDFD captures balanced/divergence-free flow, HodgeRank's curl is the local-loop component. Document the relationship.)
  - Any comparison with HodgeRank or Trophic coherence mentioned?

  **Fallback**: If arxiv.org HTML is slow/blocked, search `"Homs-Dones" "MacKay" "Sansom" "circular" 2025 site:arxiv.org`

  ### C2. arXiv:2408.12839 — Causal Hierarchy via HHK Decomposition

  **Fetch**: `https://arxiv.org/html/2408.12839` or `https://arxiv.org/pdf/2408.12839`

  **Grep patterns**:
  - `"Hodge-Kodaira"`, `"rotational"`, `"gradient"`, `"harmonic"`, `"Laplacian"`, `"implementation"`, `"python"`, `"sparse"`, `"algorithm"`

  **Key aspects to extract**:
  - How they construct the directed weighted graph (Granger causality values as edge weights)
  - The exact linear algebra for decomposing into gradient/curl/harmonic (should be similar to HodgeRank but on a fully-connected graph)
  - Whether they compute curl per-edge or per-triangle (the latter is more informative)
  - Any code repository link
  - How they normalize the Hodge Laplacian when graph has complete edges (relevant for fully-connected citation matrices)

  **Also fetch** the 'How circular is a directed network?' paper from Royal Society Open Science 2025:
  Search: `"How circular is a directed network" Royal Society Open Science 2025`
  This may give additional implementation perspective.

  ---

  ## SECTION D — Clarivate JCR Suppression Lists (2018–2025)

  ### What to collect
  The executor needs: journal names, publishers, year, reason (self-citation vs. citation stacking), and total count per year.

  **D1. Already found — record these as facts**:
  - 2018: 20 journals (14 self-citation, 6 citation stacking) — source: Scholarly Kitchen
  - 2020: 33 journals
  - 2021: 10 journals
  - 2022: 3 journals (+ 6 warnings)
  - 2023: 4 journals
  - 2024: 17 journals (list found at Retraction Watch 2024-06-27 — named above in research findings)
  - 2025: 20 journals (list found at Retraction Watch 2025-06-18 — named above in research findings)

  **D2. Sources to fetch for full named lists**:

  - **2018 full list**: Fetch `https://scholarlykitchen.sspnet.org/2018/06/27/impact-factor-denied-20-journals-self-citation-stacking/`
    - Grep for journal names listed in the article.

  - **2019 list**: Search `site:retractionwatch.com journals suppressed impact factor 2019`

  - **2020 list**: Fetch `https://retractionwatch.com/2021/06/30/ten-journals-denied-2020-impact-factors-because-of-excessive-self-citation-or-citation-stacking/`

  - **2021/2022 lists**: Search `Clarivate JCR suppressed journals 2021 2022 list retractionwatch`

  - **2023 list**: Search `Clarivate suppressed 4 journals 2023 impact factor citation stacking retractionwatch`

  - **Bibliometric study covering 2018-2021**: Fetch `https://pubmed.ncbi.nlm.nih.gov/35469511/` — this paper studied journals with repeated suppressions and may provide a compiled list; the DOI is 10.1080/08989621.2022.2071154.

  - **Clarivate official page**: Try `https://clarivate.com/academia-government/blog/refresher-course-jcr-journal-suppression-policies/` for their methodology description and any year-by-year summary.

  **D3. Format considerations**:
  - The suppression lists are not available as a single downloadable CSV; they must be compiled from news articles.
  - The executor should compile a structured summary table: `year | journal_name | publisher | reason | source_url`
  - For ground-truth use: cite-stacking journals are of primary interest (cartels = coordinated between journals); self-citation journals are a secondary category.
  - Note: Clarivate distinguishes between 'suppressed' (no JIF assigned that year) and 'Editorial Expression of Concern' (warning). Record both.

  **D4. Check the Clarivate JCR zendesk page** (which returned 403 earlier):
  - Try `https://journalcitationreports.zendesk.com/hc/en-gb/articles/28351398819089-Title-Suppressions` via the `aii_fast_web_fetch.py` script (which may handle cookies differently than WebFetch).
  - If still blocked, try searching `site:journalcitationreports.zendesk.com suppressed`.

  **D5. Total count**:
  Record the approximate total: as of 2025, roughly 80-120 unique journals have been suppressed at least once since 2018. The PubMed bibliometric study says 18 journals suppressed 3+ times (totaling 65 suppressions for those 18 alone through ~2022).

  ---

  ## SECTION E — OpenAlex API for Journal×Journal Citation Matrix

  ### What to collect
  The executor needs an exact, working API call pattern for building a weighted journal×journal citation matrix over a multi-year time window, without hitting rate limits.

  **E1. Core approach (document this step-by-step)**

  OpenAlex does not have a direct endpoint returning a citation matrix. The workflow is:

  1. **Get the universe of journals**: Query `/sources?filter=type:journal&sort=works_count:desc` to get the top-N journals by size. Each source has an OpenAlex ID like `S1983995261`.

  2. **For each source (journal) A**, query all works published in A during the target years:
     ```
     GET /works?filter=primary_location.source.id:SA,publication_year:2010-2019
                 &select=id,referenced_works
                 &per-page=200
                 &cursor=*
     ```
     Paginate using cursor-based pagination (`cursor=*` → use `meta.next_cursor` for next page).

  3. **For each work in A**, the `referenced_works` field is a list of OpenAlex work IDs (e.g., `["W2362...", ...]`) that this work cites.

  4. **Resolve reference IDs to source IDs**: Either batch-resolve using `/works?filter=openalex_id:W123|W456|...&select=id,primary_location.source.id` (200 IDs per request), or use the pre-built OpenAlex snapshot.

  5. **Aggregate**: Count how many works from A cite works in each journal B → build the A→B edge weight.

  **E2. Practical rate limit and performance details**

  Fetch `https://developers.openalex.org/api-reference/rate-limits` (or search `OpenAlex API rate limits polite pool 2025`).
  - Without API key: 100,000 requests/day, 10 req/sec
  - With API key (free, self-registered): higher limits; add `?api_key=YOUR_KEY` to every request
  - Polite pool: add `mailto=your@email.com` to requests for higher reliability
  - Recommended: 0.1–0.2s sleep between requests to stay in the polite pool
  - For building a 5000×5000 journal matrix over 10 years: expect ~500K–1M API calls (too slow). Use the **snapshot** instead.

  **E3. Snapshot as the preferred alternative**

  For large-scale journal citation matrices, the OpenAlex snapshot is far more efficient:
  - URL: `https://zenodo.org/records/13941458` (latest Zenodo snapshot) or AWS S3 `s3://openalex/`
  - Format: gzipped JSONL per entity type. Works contain `referenced_works` and `primary_location.source.id`.
  - Size: Works file is very large (~100s of GB); filter to journals of interest.
  - The CIDRE paper used MAG (OpenAlex's predecessor); for a new study, the OpenAlex snapshot is the open equivalent.

  Fetch `https://docs.openalex.org/download-all-data/openalex-snapshot` for exact S3 bucket details and file structure.

  **E4. Alternative: CIDRE's own bundled dataset**

  The CIDRE repository already provides a pre-built journal citation network at `data/journal-citation/edge-table-2013.csv` containing directed edge weights between journals for 2013 (MAG-derived). This is a ready-made starting point that avoids the OpenAlex API entirely for prototyping.

  Fetch the raw file:
  ```
  https://raw.githubusercontent.com/skojaku/cidre/main/data/journal-citation/edge-table-2013.csv
  ```
  Document the columns: likely `source_journal_id, target_journal_id, weight` (possibly also `year`).

  **E5. Specific API call for time-window aggregation** (for executor to document exactly)

  Search for: `OpenAlex API "counts_by_year" source journal citation 2025` and fetch a Source object for a known journal:
  ```
  https://api.openalex.org/sources/S1983995261
  ```
  The `counts_by_year` field gives `[{year: 2019, cited_by_count: N}, ...]` for how many times works in that journal were cited that year — useful for checking data completeness, but not for citation directionality.

  For actual directed citation counts between journals, only the Works approach (E1) or the snapshot (E3) works.

  **E6. Fetch the openalexnet library**
  Fetch `https://github.com/filipinascimento/openalexnet` — this library specifically builds citation and coauthorship networks from OpenAlex queries. Document its API.

  ---

  ## OUTPUT FORMAT

  The executor should produce two files:

  ### `research_report.md`
  Structured with these sections:
  - **A. HodgeRank Formulation** — exact equations (B₁, L₀, least-squares system, gradient/curl/harmonic extraction, curl per triangle, isolated-node handling, energy normalization), implementation notes for scipy
  - **B. CIDRE Algorithm and Data** — donor/recipient formulas, dcSBM null, Poisson p-value, FDR, input format, bundled dataset column schema, example usage, MAG data description
  - **C. Circular-Flow Decomposition Papers** — key equations from arXiv:2506.12546 (CDFD), relationship to HodgeRank curl, BFF algorithm, any code; summary of arXiv:2408.12839 (HHK in finance); 'How circular' paper
  - **D. Clarivate JCR Suppression Lists** — per-year table (2018-2025) with counts, named journals, reasons, and source URLs; discussion of self-citation vs. citation-stacking distinction; total universe size
  - **E. OpenAlex API** — exact endpoint pattern for building citation matrix, rate limits, pagination details, snapshot alternative (S3 path), the CIDRE dataset as a ready proxy, the openalexnet library

  ### `research_out.json`
  ```json
  {
    "answer": "<one-paragraph summary of key findings>",
    "sources": [
      {"title": "...", "url": "...", "accessed": "2026-07-08"}
    ],
    "follow_up_questions": [
      "Does HodgeRank's curl component on journals always separate citation-stacking from genuine dense communities?",
      "Is the CIDRE bundled edge-table-2013.csv large enough for a meaningful Hodge decomposition (~N journals)?",
      "Can the harmonic component (global cycles) be distinguished from noise without extremely large journal graphs?"
    ]
  }
  ```

  ---

  ## EXECUTION ORDER

  **Round 1 (parallel)**: Fetch all five primary sources simultaneously:
  1. HodgeRank PDF (Stanford URL) via `aii_fast_web_fetch.py`
  2. CIDRE GitHub README
  3. arXiv:2506.12546 HTML
  4. Retraction Watch 2025 suppression article
  5. OpenAlex snapshot docs

  **Round 2 (parallel, after Round 1)**: Fetch secondary sources:
  1. arXiv:1011.1716 (Hodge ranking tutorial PDF)
  2. CIDRE PMC article
  3. CIDRE data files (edge-table CSV, journal_names CSV)
  4. Retraction Watch 2024 and 2020 suppression articles
  5. openalexnet GitHub

  **Round 3 (targeted grep)**: For any PDF sources, use `aii_fast_web_fetch.py grep` to extract specific formulas and equation blocks.

  **Round 4 (gap-fill)**: If any section is incomplete, run targeted web searches with specific queries listed in each section above.

  ---

  ## WHAT THE EXECUTOR SHOULD NOT DO
  - Do not run any Python code (this is a RESEARCH artifact; no code execution)
  - Do not download files to disk
  - Do not compute anything — only find, read, and synthesize information
  - Do not attempt to build the citation matrix — only document the API pattern
  - Do not spend LLM API budget (this task has $0 LLM budget; only web tools)

  ## FAILURE FALLBACKS
  - If the HodgeRank Stanford PDF is inaccessible, use arXiv:1011.1716 + the SciSpace abstract (https://scispace.com/papers/statistical-ranking-and-combinatorial-hodge-theory-3xl9wq12k2) + the Springer abstract (https://link.springer.com/article/10.1007/s10107-010-0419-x)
  - If CIDRE PMC is blocked, use the arXiv preprint (https://arxiv.org/abs/2009.09097) via `aii_fast_web_fetch.py`
  - If Clarivate JCR pages are 403-blocked, compile from Retraction Watch and Scholarly Kitchen articles (all years are documented there)
  - If OpenAlex API docs redirect, use `https://github.com/ourresearch/openalex-docs` GitHub repository directly
explanation: >-
  This research artifact is the critical first step of the entire investigation. Before implementing anything, the executor
  working on the Hodge decomposition citation-cartel detector needs exact, verified specifications — not approximate descriptions
  — for five things: (1) the HodgeRank sparse linear algebra (wrong boundary-operator conventions will silently produce garbage
  curl estimates); (2) CIDRE's precise donor/recipient scoring and dcSBM null (needed to implement an apples-to-apples comparison
  and to reuse its bundled dataset for prototyping); (3) the 2025 circular-flow papers (which provide a complementary decomposition
  approach — the CDFD circularity index may be a better group-level summary than HodgeRank curl energy, and its BFF algorithm
  is simpler to implement than the full Hodge apparatus); (4) the Clarivate JCR suppression lists (the ground truth — without
  a compiled, year-by-year list of suppressed journals, the detector cannot be validated); and (5) the OpenAlex API pattern
  (knowing whether to use the API vs. the snapshot vs. CIDRE's bundled data determines the entire data pipeline design and
  avoids a multi-day detour). Getting these specifications wrong costs a full experiment iteration; getting them right front-loads
  the work where it is cheapest.
</artifact_plan>

<investigation_process>
1. DIVERGE: Brainstorm multiple angles/framings of the question before searching. Think across fields — what adjacent domains might have relevant insights?
2. SEARCH: Multiple queries per angle with different phrasings to discover the landscape
3. FETCH: Read promising URLs at high level. Snippets are NOT enough — fetch full pages
4. DETAIL: aii-web-tools fetch_grep for specifics from key pages/PDFs
5. CONTRAST: Actively try to disprove your emerging conclusions. Search with different phrasings, "[topic] criticism", "[topic] limitations". Check across fields — the same finding may exist under different names
6. SYNTHESIZE: Integrate into balanced conclusion
7. ITERATE: Expect to repeat steps 2-6 if findings are incomplete or one-sided. Don't settle on first results
8. SUMMARIZE: Output JSON must include 'title' and 'summary' fields
</investigation_process>

<output_requirements>
- Write research_out.json to your workspace with all findings
- Provide your finding as clear prose WITH NUMBERED CITATIONS
- EVERY factual claim must have a citation number in brackets: [1], [2], [1, 3], etc.
- Include BOTH supporting AND contradicting evidence
- Be explicit about confidence level and what would change it
- End with follow-up questions for further investigation
</output_requirements>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

Research everything specified in the artifact plan, but you may also investigate additional relevant aspects beyond what's listed. Investigate this question thoroughly.

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ResearchExpectedFiles": {
      "description": "All expected output files from research artifact.",
      "properties": {
        "output": {
          "description": "Path to research output JSON. Example: 'research_out.json'",
          "title": "Output",
          "type": "string"
        }
      },
      "required": [
        "output"
      ],
      "title": "ResearchExpectedFiles",
      "type": "object"
    },
    "Source": {
      "description": "A source used in the research.",
      "properties": {
        "index": {
          "description": "Citation number (1, 2, 3, ...)",
          "title": "Index",
          "type": "integer"
        },
        "url": {
          "description": "Full URL of the source",
          "title": "Url",
          "type": "string"
        },
        "title": {
          "description": "Title of the article/page",
          "title": "Title",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this source contributed",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "index",
        "url",
        "title",
        "summary"
      ],
      "title": "Source",
      "type": "object"
    }
  },
  "description": "Research artifact \u2014 structured output + file metadata.\n\nConducts thorough web research using the aii-web-tools skill.\nReturns structured JSON output with citations.",
  "properties": {
    "title": {
      "default": "",
      "description": "Artifact title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); describe the content, not a status.",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "layman_summary": {
      "default": "",
      "description": "One-sentence plain-language summary of what this artifact does, accessible to non-experts. Used only in the per-artifact README, not in downstream prompts.",
      "maxLength": 250,
      "minLength": 80,
      "title": "Layman Summary",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Summary for downstream artifacts: what this artifact provides",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/ResearchExpectedFiles",
      "description": "All output files you created. Must include research_out.json with your research findings."
    },
    "upload_ignore_regexes": {
      "description": "Regex patterns for workspace paths that must NOT be published to the GitHub repo, matched against each file's path relative to this artifact's workspace root (POSIX form, e.g. 'cache/abc.json'). Applied ON TOP OF the deploy step's built-in exclusions. Use this for executor-specific caches, large transient intermediates, or content-addressed blob stores (e.g. a cache/ dir of thousands of hash-named files) that would bloat the repo. Examples: ['(^|/)cache/', '(^|/)\\\\.weight_cache/', '(^|/)checkpoints/']. Leave empty if every workspace file should be published.",
      "items": {
        "type": "string"
      },
      "title": "Upload Ignore Regexes",
      "type": "array"
    },
    "answer": {
      "description": "Comprehensive answer with NUMBERED CITATIONS. Cite sources by number: 'Claim [1].' or 'According to [2, 3]...'",
      "title": "Answer",
      "type": "string"
    },
    "sources": {
      "description": "All sources used, with index matching citation numbers in answer",
      "items": {
        "$ref": "#/$defs/Source"
      },
      "title": "Sources",
      "type": "array"
    },
    "follow_up_questions": {
      "description": "2-3 follow-up questions that emerged from the investigation",
      "items": {
        "type": "string"
      },
      "title": "Follow Up Questions",
      "type": "array"
    }
  },
  "required": [
    "out_expected_files",
    "answer",
    "sources",
    "follow_up_questions"
  ],
  "title": "ResearchArtifact",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-07-08 23:22:10 UTC

```
Propose a simple, novel graph-based method for detecting citation patterns in academic networks and validate it.
```

### [3] SKILL-INPUT — aii-web-tools · 2026-07-08 23:22:14 UTC

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

### [4] SYSTEM-USER prompt · 2026-07-08 23:32:52 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `layman_summary`: 'This research gathered the exact mathematical formulas, code APIs, and real-world data needed to build a tool that detects coordinated citation manipulation among academic journals by finding circular patterns in citation networks using a technique from algebraic topology.' is too long (at most 250 characters, got 273)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

### [5] SYSTEM-USER prompt · 2026-07-08 23:33:08 UTC

```
<verification_failed>
Your research output failed verification (attempt 1/10).
</verification_failed>

<schema_errors>
JSON SCHEMA ERRORS:
  - research_out.json: Missing required 'title' field
  - research_out.json: Missing required 'summary' field

Fix: research_out.json must have:
     {
       "answer": "comprehensive answer with [1], [2] citations",
       "sources": [{"index": 1, "url": "...", "title": "...", "summary": "..."}],
       "follow_up_questions": ["Question 1?", "Question 2?"],
       "summary": "what was found"
     }

     Each citation [N] in answer MUST match a source with that index.
</schema_errors>

<content_warnings>
CONTENT ISSUES:
  - research_out.json: 'title' is too short

Fix: Ensure answer is comprehensive, has proper citations, and all sources are cited.
</content_warnings>

<task>
FIX ISSUES:
1. Output valid research_out.json with all required fields
2. Ensure every factual claim has a numbered citation [1], [2], etc.
3. Ensure every source has a matching citation in the answer
</task>
```

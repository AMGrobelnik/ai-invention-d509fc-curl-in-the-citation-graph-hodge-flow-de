# gen_art_research_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_art`
> Run: `run_io13l_LyCX8s` — Academic Citation Patterns
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_art_research_1` (terminal_claude_agent, claude-sonnet-4-6)

### [1] CONFIG · 2026-07-09 00:50:05 UTC

```
model: claude-sonnet-4-6 | effort: high | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/gen_art/gen_art_research_1
```

### [2] SYSTEM-USER prompt · 2026-07-09 00:50:11 UTC

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
Your workspace: `/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/gen_art/gen_art_research_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/gen_art/gen_art_research_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/gen_art/gen_art_research_1/file.py`, `/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/gen_art/gen_art_research_1/results/out.json`
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

<context>
<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
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
out_dependency_files:
  file_list:
  - research_out.json

Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</dependencies>
</context>

<artifact_plan>
id: gen_plan_research_1_idx1
type: research
title: HLSAD positioning & suppression-type annotation
summary: >-
  Retrieve HLSAD (arXiv:2505.24534) technical methodology to write an accurate 3-4 sentence Related Work paragraph; enumerate
  all ~40 suppressed journals in the OpenAlex/CIDRE dataset with stacking vs. self-citation type annotations so the experiment
  can restrict positive labels to stacking-only journals.
runpod_compute_profile: cpu_light
question: >-
  What are HLSAD's exact methodology and the right contrast for Related Work? Which suppressed journals in the dataset were
  stacking vs. self-citation, year by year?
research_plan: |-
  ## Context from dependency (art_Md6TNdV-FZYE)
  The prior research artifact documents:
  - 2025 stacking (4): Applied Organometallic Chemistry, Asian Journal of Agriculture and Biology, Chemical Methodologies, Genetic Resources and Crop Evolution
  - 2024 stacking: Climate Change Economics + Environmental Science & Pollution Research pair (plus others)
  - 2023 stacking (3): Genetika, Bioscience Research, Bioinspired-Biomimetic-Nanobiomaterials
  - 2021: 10 suppressed (suppression-type breakdown unknown; Frontiers + Scientific Reports claim needs verification)
  - 2020: 33 all self-citation (MDPI mass suppression — confirmed)
  - 2019: 17 suppressed (~3-4 stacking, 4 carry-over from 2018 distortions)
  - 2018: 20 suppressed, 6 stacking (names publicly unavailable from Clarivate pages — primary gap)

  Note: Oncotarget's 2018 removal was for 'not meeting standards' with 24% self-citation rate — classify as self-citation, NOT stacking. Bone Research was a VICTIM of stacking (its metrics were distorted by other journals stacking onto it) — it is NOT a suppressed journal itself.

  ---

  ## STEP 1 — HLSAD methodology (arXiv:2505.24534)

  ### What is already confirmed by pre-planning research:
  - **Authors**: Florian Frantzen and Michael T. Schaub (KDD 2025)
  - **Laplacian degree**: L₁ (edge-level Hodge Laplacian, 1-simplices)
  - **Graph type**: TEMPORAL / DYNAMIC — targets time-evolving simplicial complexes via change-point and event detection
  - **Anomaly score**: Spectral eigenvalue deviations from a baseline Hodge Laplacian spectrum
  - **Key contrast with this paper**: HLSAD = 'when did the graph structure change over time?' (change-point detection); this paper = 'is this static cumulative flow currently manipulated?' (static flow decomposition into gradient + curl components)
  - **Domain**: General graph anomaly detection; NOT citation networks, NOT citation integrity, NOT labeled-ground-truth validation

  ### Executor actions for STEP 1:

  **1a. Fetch paper abstract + intro for exact methodological language:**
  ```
  Fetch: https://arxiv.org/abs/2505.24534
  Prompt: Extract the full abstract and any key methodological sentences. Confirm: (a) which Hodge Laplacian degree (L0/L1/L2) is the primary operator; (b) how the anomaly score is defined; (c) what real-world datasets are evaluated.
  ```

  **1b. Grep PDF for technical formula and datasets:**
  ```
  Fetch-grep: https://arxiv.org/pdf/2505.24534
  Pattern: 'Hodge Laplacian|anomaly score|L_1|eigenval|dataset|benchmark|change.?point|simplicial'
  Context: 400 chars around each match
  ```
  This extracts the specific equation for the anomaly score and lists real datasets used.

  **1c. Synthesize into the Related Work paragraph:**
  Write 3-4 sentences using this template:
  > 'HLSAD (Frantzen & Schaub, KDD 2025) applies the L₁ Hodge Laplacian's spectral properties to detect structural change-points and events in time-evolving simplicial complexes. Unlike static flow decomposition, HLSAD tracks how the eigenvalue spectrum of the edge-level Hodge Laplacian changes over time, flagging moments when the higher-order interaction structure departs from its baseline. Our work, by contrast, decomposes a single static cumulative net-flow matrix into orthogonal gradient and curl components, where the curl magnitude directly quantifies citation manipulation against a labeled ground truth (JCR suppression lists); we target citation integrity rather than general temporal anomaly detection.'
  Adjust the sentence based on what you extract in 1a/1b — specifically confirm L₁ vs L₀/L₂ and the temporal vs. static distinction.

  ---

  ## STEP 2 — Suppression-type annotation

  The goal: produce a JSON mapping `{journal_name: 'stacking'|'self_citation', issn_if_known: '...', year_suppressed: N}` for ALL ~40 suppressed journals in the CIDRE/OpenAlex dataset.

  ### Approach A: CIDRE paper supplementary (highest priority)
  The CIDRE paper (Kojaku et al., Scientific Reports 2021) uses JCR-suppressed journals as ground truth. The open-access PMC version has supplementary tables that may list specific journal names.

  ```
  Fetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC8282695/
  Prompt: List ALL specific journal names mentioned, including supplementary tables. Look for any table listing suppressed journals by year and suppression type.
  ```

  Also try the Nature.com full paper:
  ```
  Fetch: https://www.nature.com/articles/s41598-021-93572-3
  Prompt: List all journal names in any supplementary tables or in the main text that were used as ground truth for validation.
  ```

  Also search for the CIDRE GitHub repository:
  ```
  Search: 'kojaku CIDRE GitHub citation anomaly suppressed journals ground truth'
  Search: 'site:github.com kojaku cidre'
  ```
  If a GitHub repo exists, look for a data file (CSV/JSON) listing the suppressed journals used as ground truth.

  ### Approach B: Scholarly Kitchen 2018 article via web archive
  The Scholarly Kitchen article from June 2018 lists all 6 stacking journals from the 2018 JCR. The live URL returns 404; use the Internet Archive:

  ```
  Fetch: https://web.archive.org/web/2018*/https://scholarlykitchen.sspnet.org/2018/06/27/impact-factor-denied-to-20-journals-self-citation-stacking/
  ```
  This lists all archived snapshots. Then fetch the specific snapshot URL, e.g.:
  ```
  Fetch: https://web.archive.org/web/20180630000000*/https://scholarlykitchen.sspnet.org/2018/06/27/impact-factor-denied-to-20-journals-self-citation-stacking/
  ```

  ### Approach C: PMC article on suppressed journals' feature analysis
  ```
  Fetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC9424957/
  Prompt: List all journal names mentioned as suppressed from JCR. Specify which were for stacking vs self-citation, and the year.
  ```

  ### Approach D: Retraction Watch 2025 suppression article (already accessible)
  ```
  Fetch: https://retractionwatch.com/2025/06/18/clarivate-impact-factor-suppression-list-2025-self-citation-stacking/
  Prompt: List all 2025 suppressed journals by name and reason (stacking vs self-citation). Also list any historical examples mentioned.
  ```
  NOTE: 2025 stacking list was already confirmed in pre-planning: Applied Organometallic Chemistry, Asian Journal of Agriculture and Biology, Chemical Methodologies, Genetic Resources and Crop Evolution.

  ### Approach E: Targeted searches for 2019 and 2021 stacking journals
  ```
  Search: 'JCR 2019 suppressed journals stacking names list Clarivate journal impact factor 2020'
  Search: '"citation stacking" 2021 suppressed journals JCR names Science or Medicine'
  Search: 'Frontiers journals Scientific Reports 2021 JCR suppression stacking impact factor'
  ```

  ### Approach F: Enago Academy article on 2020 suppressions
  ```
  Fetch: https://www.enago.com/academy/journals-suppressed-in-the-journal-citation-reports-fight-back/
  Prompt: List all MDPI journals suppressed in 2020 and any other journals named as suppressed in 2019 or 2021, with reasons.
  ```

  ### Annotation logic for the JSON output:
  - If year_suppressed=2020: type='self_citation' (confirmed — all 33 were MDPI self-citation journals)
  - If a journal is identified as part of a mutual citation exchange ring: type='stacking'
  - If a journal shows abnormally high self-citation rate: type='self_citation'
  - Oncotarget (2018): type='self_citation' (24% self-citation rate, removed from all Clarivate products)
  - Mark any journal where suppression type is uncertain as type='unknown'
  - Include ISSN from any source that provides it (CIDRE CSV has MAG numeric IDs; cross-reference to journal name)

  ### Expected output format:
  ```json
  [
    {"journal": "Applied Organometallic Chemistry", "issn": "1099-0739", "year_suppressed": 2025, "type": "stacking"},
    {"journal": "Asian Journal of Agriculture and Biology", "issn": "2307-3462", "year_suppressed": 2025, "type": "stacking"},
    ...
    {"journal": "[name]", "issn": "unknown", "year_suppressed": 2018, "type": "stacking"},
    ...
  ]
  ```

  ---

  ## STEP 3 — Concurrent work scan

  Searches to run in parallel:

  **3a. Hodge/circularity + citation integrity:**
  ```
  Search: 'Hodge decomposition citation network academic integrity manipulation 2024 2025 arXiv'
  Search: 'circularity index citation cartel journal network detection 2024 2025'
  Search: 'HodgeRank citation bibliometric anomaly 2024'
  ```

  **3b. New cartel detection methods:**
  ```
  Search: 'citation cartel detection method 2024 2025 graph network journal arXiv'
  Search: 'citation stacking detection machine learning 2024 2025'
  ```

  **3c. Fetch HLSAD citing papers if the paper is available:**
  Check if any citing papers of arXiv:2505.24534 apply Hodge decomposition to citation networks:
  ```
  Fetch: https://arxiv.org/abs/2505.24534
  Look for any citing papers section or Google Scholar-style links
  ```

  ### If any new concurrent papers are found:
  - Record title, arXiv/DOI, venue, authors, year
  - Note key methodological distinction from this paper (temporal vs. static, spectral vs. flow decomposition, etc.)
  - Note whether they use citation networks or labeled ground truth

  ---

  ## OUTPUT FORMAT

  Write `research_out.json` with structure:
  ```json
  {
    "answer": {
      "hlsad_summary": {
        "title": "HLSAD: Hodge Laplacian-based Simplicial Anomaly Detection",
        "authors": "Frantzen & Schaub",
        "venue": "KDD 2025",
        "arxiv": "2505.24534",
        "hodge_laplacian_degree": "L1 (edge-level / 1-simplices)",
        "temporal_or_static": "temporal",
        "anomaly_score_method": "spectral change-point detection via Hodge Laplacian eigenvalue deviations over time",
        "evaluation_datasets": ["..."],
        "related_work_paragraph": "3-4 sentence paragraph ready for insertion into paper",
        "key_contrast_with_this_paper": "..."
      },
      "suppressed_journals": [
        {"journal": "...", "issn": "...", "year_suppressed": 2025, "type": "stacking|self_citation|unknown"}
      ],
      "suppression_type_summary": {
        "stacking_total": "N",
        "self_citation_total": "N",
        "unknown_total": "N",
        "stacking_journals_by_year": {"2025": [...], "2024": [...], "2023": [...], "2021": [...], "2019": [...], "2018": [...]}
      },
      "concurrent_works_beyond_hlsad": [
        {"title": "...", "arxiv": "...", "year": 2025, "key_distinction": "..."}
      ]
    },
    "sources": [
      {"url": "...", "description": "..."}
    ],
    "follow_up_questions": [
      "..."
    ]
  }
  ```

  Also write `research_report.md` summarizing findings in human-readable form with the Related Work paragraph prominently included.

  ---

  ## FALLBACK NOTES FOR EXECUTOR

  - **If CIDRE PMC supplementary doesn't list journals**: Search for 'Kojaku 2021 CIDRE supplementary data journals list stacking' and try the LSE Research Online version: http://eprints.lse.ac.uk/111532/
  - **If 2018 stacking names can't be found**: Mark as 'unknown' and note in the JSON; the 2020/2021/2022/2023/2024/2025 lists are sufficient to annotate a majority of suppressed journals. The 2018 list (6 stacking out of 20) is important but the failure to name them should be explicitly documented so the experiment designer knows to exclude 2018 suppressions from the validated stacking-positive class.
  - **If Frontiers/Scientific Reports 2021 claim can't be verified**: Mark 2021 as 'type=unknown' and note this in the report. Do NOT classify as stacking without confirmation.
  - **HLSAD: if exact formula can't be extracted from PDF**: The confirmed facts (L1, temporal, change-point detection via eigenvalues, KDD 2025) are sufficient for the Related Work positioning. The paragraph should emphasize the temporal vs. static distinction as the primary differentiator.
  - **Cost**: All research is web-based ($0 LLM cost). No API calls needed.
explanation: >-
  This research directly enables two critical path items for the Hodge decomposition citation cartel detector paper: (1) accurate
  Related Work positioning against HLSAD — the only known concurrent work using Hodge Laplacians near this topic — which requires
  knowing its exact methodology (temporal change-point detection via L₁ spectral properties on evolving simplicial complexes,
  NOT static flow decomposition) to write a precise 3-4 sentence contrast paragraph; and (2) ground-truth label annotation
  for the evaluation, where using ALL suppressed journals as positives would inflate recall numbers because the Hodge curl
  cannot detect self-citation suppression by design (self-citation inflates a node's self-loop, not the net-flow between pairs),
  so the experiment must restrict the positive class to stacking-only journals. Pre-planning web research confirmed HLSAD
  is L₁/temporal, confirmed 2025 stacking names, and established that direct Clarivate suppression pages return 403 errors
  — so the executor must use alternative routes (CIDRE PMC supplementary, web archive, PMC secondary articles) which are spelled
  out concretely in the plan.
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

### [3] HUMAN-USER prompt · 2026-07-09 00:50:11 UTC

```
Propose a simple, novel graph-based method for detecting citation patterns in academic networks and validate it.
```

### [4] TOOL CALL — Skill · 2026-07-09 00:50:17 UTC

```
aii-web-tools
```

### [5] TOOL RESULT — Skill · 2026-07-09 00:50:17 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [6] TOOL CALL — ToolSearch · 2026-07-09 00:50:21 UTC

```
{'query': 'select:WebSearch,WebFetch'}
```

### [7] TOOL RESULT — ToolSearch · 2026-07-09 00:50:21 UTC

```
{"matches": ["WebSearch", "WebFetch"], "query": "select:WebSearch,WebFetch", "total_deferred_tools": 21}
```

### [8] ASSISTANT · 2026-07-09 00:50:31 UTC

```
Now I'll launch all parallel searches for HLSAD methodology, suppressed journal annotations, and concurrent work.
```

### [9] TOOL CALL — WebFetch · 2026-07-09 00:50:31 UTC

```
URL: https://arxiv.org/abs/2505.24534
Prompt: Extract the full abstract and key methodological details. Confirm: (a) which Hodge Laplacian degree (L0/L1/L2) is the primary operator; (b) how the anomaly score is defined; (c) what real-world datasets are evaluated; (d) whether the approach is temporal/dynamic or static.
```

### [10] TOOL CALL — WebFetch · 2026-07-09 00:50:31 UTC

```
URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC8282695/
Prompt: List ALL specific journal names mentioned, including any supplementary tables. Look for tables listing suppressed journals by year and suppression type (stacking vs. self-citation).
```

### [11] TOOL CALL — WebSearch · 2026-07-09 00:50:31 UTC

```
JCR 2019 suppressed journals stacking names list Clarivate journal impact factor 2020
```

### [12] TOOL CALL — WebSearch · 2026-07-09 00:50:31 UTC

```
"citation stacking" 2021 suppressed journals JCR names Clarivate impact factor
```

### [13] TOOL CALL — WebSearch · 2026-07-09 00:50:31 UTC

```
Hodge decomposition citation network academic integrity manipulation 2024 2025 arXiv
```

### [14] TOOL RESULT — WebFetch · 2026-07-09 00:50:34 UTC

```
{"bytes": 42385, "code": 200, "codeText": "OK", "result": "# HLSAD Paper Analysis\n\nBased on the arXiv page content provided, here's what can be confirmed:\n\n## Full Abstract\n\"In this paper, we propose HLSAD, a novel method for detecting anomalies in time-evolving simplicial complexes. While traditional graph anomaly detection techniques have been extensively studied, they often fail to capture changes in higher-order interactions that are crucial for identifying complex structural anomalies. These higher-order interactions can arise either directly from the underlying data itself or through graph lifting techniques. Our approach leverages the spectral properties of Hodge Laplacians of simplicial complexes to effectively model multi-way interactions among data points. By incorporating higher-dimensional simplicial structures into our method, our method enhances both detection accuracy and computational efficiency. Through comprehensive experiments on both synthetic and real-world datasets, we demonstrate that our approach outperforms existing graph methods in detecting both events and change points.\"\n\n## Key Methodological Details\n\n**(a) Hodge Laplacian Degree:** The page does not specify which degree (L0/L1/L2) is primary—only that the method \"leverages the spectral properties of Hodge Laplacians\" generally.\n\n**(b) Anomaly Score Definition:** Not detailed in the abstract or page summary provided.\n\n**(c) Real-World Datasets:** The abstract mentions \"synthetic and real-world datasets\" but does not name specific datasets on this page.\n\n**(d) Temporal/Dynamic vs. Static:** The approach is **temporal/dynamic**—explicitly described as operating on \"time-evolving simplicial complexes\" with evaluation on \"change points.\"\n\n**Note:** Full methodological details require accessing the complete PDF.", "durationMs": 5385, "url": "https://arxiv.org/abs/2505.24534"}
```

### [15] TOOL RESULT — WebFetch · 2026-07-09 00:50:38 UTC

```
{"bytes": 208607, "code": 200, "codeText": "OK", "result": "# Journal Names and Suspension Data from CIDRE Study\n\n## Explicitly Named Journals in Article Text\n\nThe paper mentions specific journals in detailed case studies (Groups 1-14):\n\n**Group 1 (Anthropology):** American Anthropologist, Social Anthropology, Anthropological Quarterly, Cultural Anthropology, Focaal, Journal of the Royal Anthropological Institute\n\n**Group 2 (Crystallography):** Acta Crystallographica Section C, IUCrData, Acta Crystallographica Section E\n\n**Group 3 (Engineering):** International Journal of Intelligent Systems and Applications\n\n**Group 4 (Veterinary Science):** Journal of Veterinary Medicine, Journal of Animal Physiology and Animal Nutrition\n\n**Group 5 (Business):** Journal of Security and Sustainability Issues, Entrepreneurship and Sustainability Issues\n\n**Group 6 (Laser Science):** Laser Physics, Laser Physics Letters\n\n**Group 7 (Engineering):** International Journal of Automotive and Mechanical Engineering, Journal of Mechanical Engineering and Sciences\n\n**Group 8 (Literature):** Keats Shelley Journal\n\n**2019 Groups (9-14):** International Journal of Surgery, Annals of Medicine and Surgery, International Journal of Surgery Case Reports, Journal of Low Frequency Noise/Vibration/Active Control, Thermal Science, Crystallography Reviews, Regulation and Governance, Annals of American Academy of Political and Social Science, Journal of Mathematical Sciences and Cryptography, Journal of Information and Optimization Science\n\n## JCR Suspension Data\n\nThe article states: \"As of 2019, JCR has suspended...46 pairs of journals—featuring 55 journals in total.\" However, **no comprehensive table listing all suspended journals appears in the provided text**. The paper references JCR groups J1-J22 but does not enumerate all individual journal names from the official JCR suspension list.", "durationMs": 6958, "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8282695/"}
```

### [16] TOOL RESULT — WebSearch · 2026-07-09 00:50:38 UTC

```
{"query": "JCR 2019 suppressed journals stacking names list Clarivate journal impact factor 2020", "results": [{"tool_use_id": "srvtoolu_014B2zeDWCEsGAhX4mvRYxWL", "content": [{"title": "Title Suppressions", "url": "https://help.incites.clarivate.com/incitesLiveJCR/JCRGroup/titleSuppressions.html"}, {"title": "A bibliometric investigation of the journals that were repeatedly suppressed from Clarivate's Journal Citation Reports - PubMed", "url": "https://pubmed.ncbi.nlm.nih.gov/35469511/"}, {"title": "Title Suppressions - Journal Citation Reports - Zendesk", "url": "https://journalcitationreports.zendesk.com/hc/en-gb/articles/28351398819089-Title-Suppressions"}, {"title": "A Refresher Course on JCR Journal Suppression Policies | Clarivate", "url": "https://clarivate.com/academia-government/blog/refresher-course-jcr-journal-suppression-policies/"}, {"title": "Impact Factor Denied to 20 Journals For Self-Citation, Stacking - The Scholarly Kitchen", "url": "https://scholarlykitchen.sspnet.org/2018/06/27/impact-factor-denied-20-journals-self-citation-stacking/"}, {"title": "Journals removed from JCR by high levels of self-citation and by concentration of citations between journals | ResearchGate", "url": "https://www.researchgate.net/post/Journals_removed_from_JCR_by_high_levels_of_self-citation_and_by_concentration_of_citations_between_journals"}, {"title": "“Stunned, very confused”: Two more journals push back against Impact Factor suppression", "url": "https://retractionwatch.com/2020/07/13/stunned-very-confused-two-more-journals-push-back-against-impact-factor-suppression/"}, {"title": "JCR Editorial Expression of Concern – Journal Citation Reports", "url": "https://journalcitationreports.zendesk.com/hc/en-gb/articles/28351368597521-JCR-Editorial-Expression-of-Concern"}, {"title": "The ICSP and the Microbiology Society’s appeal to Clarivate regarding suppression of the IJSEM from the 2019 Impact Factor | Microbiology Society", "url": "https://www.microbiologyresearch.org/journal/ijsem/clarivate_appeal"}, {"title": "Citation issues cost these 20 journals their impact factors this year – Retraction Watch", "url": "https://retractionwatch.com/2025/06/18/clarivate-impact-factor-suppression-list-2025-self-citation-stacking/"}]}, "Based on the search results, I found information about JCR journal suppressions. Here's what the data shows:\n\n## JCR 2019 Suppressed Journals\n\nJournals were suppressed from the 2018 JCR Data (2019 release) due to anomalous citation patterns found in the 2018 citation data. Journals indexed by Clarivate are temporarily suppressed from the Journal Citation Reports (JCR) if their Journal Impact Factor (JIF) scores are distorted through excessive self-citations or citation stacking with other journals.\n\n## Citation Stacking and Self-Citation Issues\n\nThe suppressed titles data lists the recipient and donor journal pairs along with the percentage of citations in the Journal Impact Factor numerator that are from the donor to the recipient. Clarivate Analytics suppressed 20 journals in one year, 14 for high levels of self-citation and six for citation stacking — a pattern known informally as a \"citation cartel.\"\n\n## Suppression Overview\n\nAn investigation covered the 18 journals that were suppressed three or more times from the JCR, and results indicate that these 18 journals were repeatedly and exclusively suppressed for being excessive self-citers.\n\nThe search results provide general information about suppression policies and examples from 2019, but don't include a complete list of specific journal names with their impact factors. For a detailed list with specific journal names and their 2020 impact factors, you may need to access the official Clarivate JCR documentation directly or check the Zendesk JCR help pages referenced in the search results."], "durationSeconds": 6.891753269999997, "searchCount": 1}
```

### [17] TOOL RESULT — WebSearch · 2026-07-09 00:50:40 UTC

```
{"query": "Hodge decomposition citation network academic integrity manipulation 2024 2025 arXiv", "results": [{"tool_use_id": "srvtoolu_01EjxXL18SjpxiR5mLndDZKk", "content": [{"title": "arXiv:2503.23414v1 [cs.DL] 30 Mar 2025", "url": "https://arxiv.org/pdf/2503.23414"}, {"title": "arXiv:2504.02767v1 [cs.DL] 3 Apr 2025", "url": "https://arxiv.org/pdf/2504.02767"}, {"title": "Topological Effective Connectivity Modeling in Brain Networks", "url": "https://arxiv.org/pdf/2606.08407"}, {"title": "Tensor Manifold-Based Graph-Vector Fusion for AI-Native Academic Literature Retrieval", "url": "https://arxiv.org/pdf/2604.16416"}, {"title": "[2601.04326] Hodge Decomposition Guides the Optimization of Synchronization over Simplicial Complexes", "url": "https://arxiv.org/abs/2601.04326"}, {"title": "Vector Space of Cycles", "url": "https://arxiv.org/pdf/2606.08202"}, {"title": "Topology-preserving Hodge Decomposition in the Eulerian Representation", "url": "https://arxiv.org/pdf/2408.14356"}, {"title": "Retracted: Relieving the Incompatibility of Network Representation and Classification for Long-Tailed Data Distribution", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10322380/"}, {"title": "Retracted: Analysis of College Students' Network Moral Behavior by the History of Ideological and Political Education under Deep Learning", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10432742/"}]}, "Based on the web search results, I found relevant information related to your query:\n\n## Academic Integrity and Citation Manipulation\n\nSuspicious academic documents from ResearchGate dated 2024–2025 have been found to follow consistent structural and stylistic patterns and frequently cite earlier work despite lacking thematic relevance or scholarly depth. Gaming of citation metrics misrepresents academic influence and skews global rankings, hiring decisions, grant evaluations, and editorial opportunities.\n\n## Hodge Decomposition Research\n\nThe search results also revealed several recent arXiv papers on Hodge decomposition in different contexts:\n\n- Hodge decomposition decomposes differential forms into exact, co-exact, and harmonic components, providing a tool for feature extraction and noise reduction of graph data for academic literature retrieval.\n\n- Discrete Hodge theory provides a combinatorial analogue of the classical Hodge–Helmholtz decomposition and has become a versatile data-analytic tool for network flows over the past decade.\n\nThe results show current research (2024-2025) on both Hodge decomposition methods and academic integrity issues related to citation manipulation, though the specific intersection of these topics in relation to citation networks is not directly addressed in the search results."], "durationSeconds": 8.975733107000003, "searchCount": 1}
```

### [18] TOOL RESULT — WebSearch · 2026-07-09 00:50:42 UTC

```
{"query": "\"citation stacking\" 2021 suppressed journals JCR names Clarivate impact factor", "results": [{"tool_use_id": "srvtoolu_01VM1YTLvV3MbCWgEZmUubbY", "content": [{"title": "Journal Citation Reports 2021 published by Clarivate - Research Information", "url": "https://www.researchinformation.info/news/journal-citation-reports-2021-published-clarivate/"}, {"title": "Journal Citation Reports 2021 - Enago Academy", "url": "https://www.enago.com/academy/journal-citation-reports-2021-identify-worlds-leading-journals-with-clarivates-journal-citation-indicator-jci/"}, {"title": "Ten journals denied 2020 Impact Factors because of excessive self-citation or “citation stacking”", "url": "https://retractionwatch.com/2021/06/30/ten-journals-denied-2020-impact-factors-because-of-excessive-self-citation-or-citation-stacking/"}, {"title": "A bibliometric investigation of the journals that were repeatedly suppressed from Clarivate's Journal Citation Reports - PubMed", "url": "https://pubmed.ncbi.nlm.nih.gov/35469511/"}, {"title": "JCR Editorial Expression of Concern – Journal Citation Reports", "url": "https://journalcitationreports.zendesk.com/hc/en-gb/articles/28351368597521-JCR-Editorial-Expression-of-Concern"}, {"title": "Impact Factor Denied to 20 Journals For Self-Citation, Stacking - The Scholarly Kitchen", "url": "https://scholarlykitchen.sspnet.org/2018/06/27/impact-factor-denied-20-journals-self-citation-stacking/"}, {"title": "A Refresher Course on JCR Journal Suppression Policies | Clarivate", "url": "https://clarivate.com/academia-government/blog/refresher-course-jcr-journal-suppression-policies/"}, {"title": "A bibliometric investigation of the journals that were repeatedly suppressed from Clarivate’s Journal Citation Reports: Accountability in Research: Vol 30, No 8", "url": "https://www.tandfonline.com/doi/abs/10.1080/08989621.2022.2071154"}, {"title": "Citation issues cost these 20 journals their impact factors this year – Retraction Watch", "url": "https://retractionwatch.com/2025/06/18/clarivate-impact-factor-suppression-list-2025-self-citation-stacking/"}, {"title": "Title Suppressions - Journal Citation Reports - Zendesk", "url": "https://journalcitationreports.zendesk.com/hc/en-gb/articles/28351398819089-Title-Suppressions"}]}, "I've found comprehensive information about citation stacking and the 2021 Journal Citation Reports. Here are the key findings:\n\n## Citation Stacking and 2021 JCR Suppressions\n\nClarivate monitors and excludes journals that demonstrate anomalous citation behavior including where there is evidence of excessive journal self-citation and citation stacking.\n\n### Number of Suppressed Journals\n\nClarivate suppressed 10 journals from the JCR in 2021, representing 0.05% of the journals listed. Additionally, an 'editorial expression of concern' has been issued for 11 journals with one or more published items with an atypically high-value contribution to the JIF numerator and a pattern of journal citations disproportionately concentrated into the JIF numerator.\n\n### Reasons for Suppression\n\nThese journals were suppressed on the basis of Clarivate's monitoring of journals that demonstrate atypical citation behavior including where there is evidence of excessive journal self-citation and citation stacking.\n\n### Methodology Updates\n\nThe methodology and parameters for the effect of journal self-citation on JCR metrics were updated in 2020 to better account for discipline norms.\n\n### What Suppression Means\n\nIt's important to note that the suppression of a journal from the JCR does not equate to a de-listing from the Web of Science Core Collection.\n\nThe search results don't provide the specific names of the 10 journals that were suppressed in 2021, only that they were suppressed for citation anomalies detected by Clarivate."], "durationSeconds": 11.604837784999999, "searchCount": 1}
```

### [19] TOOL CALL — WebFetch · 2026-07-09 00:50:56 UTC

```
URL: https://arxiv.org/pdf/2505.24534
Prompt: Extract: (1) which Hodge Laplacian degree (L0/L1/L2) is used as the primary operator; (2) exact formula for anomaly score; (3) real-world datasets evaluated; (4) section headings and key equations. Focus on the methodology/methods section.
```

### [20] TOOL CALL — WebFetch · 2026-07-09 00:50:56 UTC

```
URL: https://retractionwatch.com/2021/06/30/ten-journals-denied-2020-impact-factors-because-of-excessive-self-citation-or-citation-stacking/
Prompt: List all 10 journal names that were denied 2020 Impact Factors. For each, specify whether the reason was self-citation or citation stacking.
```

### [21] TOOL CALL — WebFetch · 2026-07-09 00:50:56 UTC

```
URL: https://scholarlykitchen.sspnet.org/2018/06/27/impact-factor-denied-20-journals-self-citation-stacking/
Prompt: List all 20 journal names denied impact factors in 2018. For each, specify whether the reason was self-citation or citation stacking. List all 6 stacking journal names specifically.
```

### [22] TOOL CALL — WebFetch · 2026-07-09 00:50:56 UTC

```
URL: https://retractionwatch.com/2025/06/18/clarivate-impact-factor-suppression-list-2025-self-citation-stacking/
Prompt: List all suppressed journals for 2025 by name, and specify for each whether suppression was for self-citation or stacking. Also list any historical examples mentioned.
```

### [23] TOOL CALL — WebSearch · 2026-07-09 00:50:56 UTC

```
citation cartel detection method 2024 2025 graph network journal arXiv machine learning
```

### [24] TOOL RESULT — WebFetch · 2026-07-09 00:50:56 UTC

```
{"bytes": 822594, "code": 200, "codeText": "OK", "result": "# HLSAD: Hodge Laplacian-based Simplicial Anomaly Detection\n\n## Hodge Laplacian Degree Used\nThe paper employs **L₁** (the Hodge Laplacian of degree 1) as the primary operator for detecting anomalies in simplicial complexes. This targets pairwise interactions and higher-order structures beyond simple node relationships.\n\n## Anomaly Score Formula\nThe exact anomaly scoring mechanism involves spectral methods applied to the Hodge Laplacian. The methodology leverages eigenvalue decomposition of L₁ to identify deviations from expected structural patterns in temporal simplicial data.\n\n## Real-World Datasets Evaluated\nThe paper tests HLSAD on practical datasets spanning:\n- **Temporal networks** with documented ground-truth anomalies\n- **Contact/interaction data** (referenced in methodology sections)\n- **Dynamic simplicial complexes** representing evolving higher-order relationships\n\n## Key Section Headings & Equations\nPrimary sections include:\n- Introduction (establishing motivation for higher-order anomaly detection)\n- Preliminaries on simplicial complexes and algebraic topology\n- Methodology section detailing the Hodge Laplacian framework\n- Experimental evaluation with comparative benchmarks\n- Appendices covering mathematical proofs and supplementary experiments\n\n**Core innovation**: Using spectral properties of L₁ to capture \"anomalous deviations in the topology and dynamics of simplicial complexes,\" enabling detection of structural irregularities not visible in traditional graph-based approaches.\n\n[Binary content (application/pdf, 803.3KB) also saved to /root/.claude/projects/-ai-inventor-aii-data-runs-run-io13l-LyCX8s-3-invention-loop-iter-2-gen-art-gen-art-research-1/0ec55ec7-16df-4fa3-9ddb-27e03100d7eb/tool-results/webfetch-1783558248712-fteo8a.pdf]", "durationMs": 5677, "url": "https://arxiv.org/pdf/2505.24534"}
```

### [25] TOOL RESULT — WebFetch · 2026-07-09 00:50:56 UTC

```
{"bytes": 113808, "code": 200, "codeText": "OK", "result": "# Journals Denied 2020 Impact Factors\n\nHere are the 10 journals that were suppressed from receiving a 2020 Impact Factor:\n\n1. **Archivos Latinoamericanos de Nutrition** – Citation stacking\n2. **Journal of Intelligent & Fuzzy Systems** – Citation stacking\n3. **Materials Express** – Citation stacking\n4. **Hellenic Journal of Cardiology** – Excessive self-citation\n5. **International Journal of Engine Research** – Excessive self-citation\n6. **Journal of Enhanced Heat Transfer** – Excessive self-citation\n7. **Journal of Family and Economic Issues** – Excessive self-citation\n8. **Mechanics-Based Design of Structures and Machines** – Excessive self-citation\n9. **Journal of Biomolecular Structure and Dynamics** – Excessive self-citation\n10. **Liquid Crystals** – Excessive self-citation\n\nAccording to Clarivate, these journals engaged in practices that \"inflates the Impact Factor\" through manipulated citation patterns, with four journals cited for \"citation stacking\" and six for problematic self-referencing practices.", "durationMs": 4208, "url": "https://retractionwatch.com/2021/06/30/ten-journals-denied-2020-impact-factors-because-of-excessive-self-citation-or-citation-stacking/"}
```

### [26] TOOL RESULT — WebFetch · 2026-07-09 00:51:00 UTC

```
{"bytes": 112697, "code": 200, "codeText": "OK", "result": "# Journals Denied Impact Factor in 2018\n\n## 14 Journals Suppressed for Self-Citation:\n\n1. Aquaculture Economics & Management\n2. Archives of Budo\n3. Canadian Historical Review\n4. Chinese Journal of International Law\n5. Chinese Journal of Mechanical Engineering\n6. Eurasia Journal of Mathematics Science and Technology Education\n7. International Journal of American Linguistics\n8. International Journal of Applied Mechanics\n9. International Journal of Civil Engineering\n10. Journal of Micropalaeontology\n11. Journal of Voice\n12. Maritime Policy & Management\n13. Pediatric Dentistry\n14. Psychoanalytic Quarterly\n\n## 6 Journals Suppressed for Citation Stacking:\n\n1. European Journal of the History of Economic Thought\n2. Journal of the History of Economic Thought\n3. Liver Cancer (recipient from Digestive Diseases)\n4. Liver Cancer (recipient from Oncology)\n\n**Note:** The article lists citation stacking as involving \"donor\" and \"recipient\" journal pairs. The four entries above represent the unique journals involved in the stacking violations identified.\n\n## 5 Additional Journals Receiving Editorial Expression of Concern:\n\nNanoscience and Nanotechnology Letters, Journal of Biobased Materials and Bioenergy, Journal of Biomedical Nanotechnology, Journal of Nanoscience and Nanotechnology, and Bone Research", "durationMs": 5954, "url": "https://scholarlykitchen.sspnet.org/2018/06/27/impact-factor-denied-20-journals-self-citation-stacking/"}
```

### [27] TOOL RESULT — WebFetch · 2026-07-09 00:51:00 UTC

```
{"bytes": 117725, "code": 200, "codeText": "OK", "result": "# 2025 Suppressed Journals by Citation Issue Type\n\n## Self-Citation (16 journals)\n1. Advances and Applications in Discrete Mathematics\n2. Annals of Phytomedicine-An International Journal\n3. Clinical Hemorheology and Microcirculation\n4. Indian Journal of Biochemistry & Biophysics\n5. Jordan Journal of Mechanical and Industrial Engineering\n6. Journal of Earthquake and Tsunami\n7. Journal of Mind and Medical Sciences\n8. Lobachevskii Journal of Mathematics\n9. Mechanics of Advanced Materials and Structures\n10. Media Education (Mediaobrazovanie)\n11. Punjab University Journal of Mathematics\n12. Russian Chemical Bulletin\n13. Russian Journal of Physical Chemistry B\n14. TeMA – Journal of Land Use Mobility and Environment\n15. Transactions of FAMENA\n16. Vestnik St. Petersburg University, Mathematics\n\n## Citation Stacking (4 journals)\n1. Applied Organometallic Chemistry\n2. Asian Journal of Agriculture and Biology\n3. Chemical Methodologies\n4. Genetic Resources and Crop Evolution\n\n## Historical Examples Mentioned\n- **2024**: 17 journals lost impact factors for citation manipulation\n- **2023**: 4 journals lost impact factors for citation issues", "durationMs": 4859, "url": "https://retractionwatch.com/2025/06/18/clarivate-impact-factor-suppression-list-2025-self-citation-stacking/"}
```

### [28] TOOL RESULT — WebSearch · 2026-07-09 00:51:02 UTC

```
{"query": "citation cartel detection method 2024 2025 graph network journal arXiv machine learning", "results": [{"tool_use_id": "srvtoolu_01LBra19v3TuRpxqZFsWBJ1u", "content": [{"title": "Machine Learning-Based Cartel Detection", "url": "https://www.emergentmind.com/topics/machine-learning-based-cartel-detection-algorithms"}, {"title": "Catching Bid-rigging Cartels with Graph Attention Neural Networks", "url": "https://arxiv.org/pdf/2507.12369"}, {"title": "Detecting Miscitation on the Scholarly Web through LLM-Augmented Text-Rich Graph Learning", "url": "https://arxiv.org/pdf/2603.12290"}, {"title": "Who are you? Cartel detection using unlabeled data - ScienceDirect", "url": "https://www.sciencedirect.com/science/article/abs/pii/S0167718723000139"}, {"title": "Deep Graph Learning for Anomalous Citation Detection", "url": "https://arxiv.org/pdf/2202.11360"}, {"title": "Collusion Detection with Graph Neural Networks", "url": "https://arxiv.org/pdf/2410.07091"}, {"title": "Unsupervised Anomaly Detection in Journal-Level Citation Networks | Proceedings of the ACM/IEEE Joint Conference on Digital Libraries in 2020", "url": "https://dl.acm.org/doi/10.1145/3383583.3398531"}]}, "Based on the search results, here are the key findings related to citation cartel detection methods using graph networks and machine learning:\n\n## Citation Cartel Detection Methods\n\nThere is research on detecting citation cartels in journal networks published on arXiv, and deep graph learning approaches for anomalous citation detection have been published in IEEE Transactions on Neural Networks and Learning Systems.\n\n## Graph Neural Network Approaches\n\nRecent work has focused on graph-based methods for cartel detection. A 2024 working paper from the University of Hamburg addresses collusion detection with graphical neural networks. Additionally, machine learning using convolutional neural networks has been applied to flag cartel participants, published in the International Journal of Industrial Organization.\n\n## Machine Learning Techniques\n\nSuper Learner Ensembles, which use weighted convex combinations of diverse learners (random forest, lasso, boosting, neural networks), have been shown to achieve superior generalization in recent studies from 2021-2025. Classification rates in modern studies range from 80% to 95%, with ensemble methods frequently outperforming single algorithms.\n\n## Recent Developments\n\nRecent 2025 research includes detecting anomalous self-citations using citation network analysis and LLMs, published in Engineering Applications of Neural Networks, indicating an emerging integration of large language models with network analysis methods for citation anomaly detection."], "durationSeconds": 7.908198842999998, "searchCount": 1}
```

### [29] TOOL CALL — Bash · 2026-07-09 00:51:24 UTC

```
Grep HLSAD PDF for Hodge Laplacian degree, anomaly score, datasets:
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://arxiv.org/pdf/2505.24534" --pattern "Hodge Laplacian|L_1|L_\{1\}|anomaly score|eigenval|spectral|dataset|change.point|temporal" -i --max-matches 30 --context-chars 300 2>&1 | head -200
```

### [30] TOOL RESULT — Bash · 2026-07-09 00:51:24 UTC

```
{"stdout": "URL: https://arxiv.org/pdf/2505.24534\nType: PDF\nPattern: Hodge Laplacian|L_1|L_\\{1\\}|anomaly score|eigenval|spectral|dataset|change.point|temporal (170 matches in 64844 chars)\n\n--- Content ---\n\n48:arXiv:2505.24534v1  [cs.LG]  30 May 2025\nHLSAD: Hodge Laplacian-based Simplicial Anomaly Detection\nFlorian Frantzen\nRWTH Aachen University\nDepartment of Computer Science\nAachen, Germany\nflorian.frantzen@cs.rwth-aachen.de\nMichael T. Schaub\nRWTH Aachen University\nDepartment of Computer Science\nAachen, Germany\nschaub@cs.rwth-aachen.de\nFigure 1: Illustrative process of anomaly detection on a toy-example simplicial complex sequence. Starting from a time-evolving\nsimplicial complex, we compute the Hodge Laplacians for each snapshot and extract spectral features for each. We employ\na sliding window approach to identify anomalies by evaluating the deviation of current spectral features from established\ntemporal patterns. In this illustrative example, HLSAD successfully detects all three artificially introduced anomalies, whereas\ntraditional graph-based analysis fails to identify the final anomaly that manifests in higher-order interactions.\nAbstract\nIn this paper, we propose HLSAD, a novel method for dete...\n--\n1436:...ively stud-\nied, they often fail to capture changes in higher-order interactions\nthat are crucial for identifying complex structural anomalies. These\nhigher-order interactions can arise either directly from the under-\nlying data itself or through graph lifting techniques. Our approach\nleverages the spectral properties of Hodge Laplacians of simplicial\ncomplexes to effectively model multi-way interactions among data\npoints. By incorporating higher-dimensional simplicial structures\ninto our method, our method enhances both detection accuracy\nand computational efficiency. Through comprehensive experiments\non both synthetic and real-world datasets, we demonstrate that our\napproach outperforms existing graph methods in detecting both\nevents and change points.\nCCS Concepts\n• Mathematics of computing →Graph theory; Topology; • Com-\nputing methodologies →Anomaly detection; Temporal rea-\nsoning; Spectral methods; • Theory of computation →Dynamic\ngraph algorithms.\nThis work is licensed under a Creative Commons Attribution 4.0 International License.\nKDD ’25, Toronto, ON, Canada\n© 2025 Copyright held by the owner/author(s).\nACM ISBN 979-8-4007-1454-2/2025/08\nhttps://doi.org/10.1145/3711896.3736998\nKeywords\nanomaly detection, change point detection, event detection, simpli-\ncial complex, spectral methods\nACM Reference Format:\nFlorian Frantzen and Michael T. Schaub. 2025. HLSAD: Hodge Laplacian-\nbased Simplicial Anomaly Detection. In Proceedings of the 31st ACM SIGKDD\nConference on Knowledge Discovery and Data Mining V.2 (KDD ’25), August\n3–7, 2025, Toronto, ON, Canada. ACM, New York, NY, USA, 11 pages. https:\n//doi.org/10.1145/3711896.3736998\nKDD Availability Link:\nThe source code of thi...\n--\n3928:...teractions that can\n\nKDD ’25, August 3–7, 2025, Toronto, ON, Canada\nFlorian Frantzen and Michael T. Schaub\nbe essential for identifying complex structural anomalies in the un-\nderlying system. Such higher-order data can manifest itself through\ndifferent mechanisms:\nHigher-Order Data Many real-world datasets inherently contain\nmulti-way interactions that extend beyond dyadic relation-\nships. Traditional graph-based methods are fundamentally\nlimited in their ability to capture and analyze these higher-\norder structures. For instance, during the COVID-19 pan-\ndemic, social distancing measures disproport...\n--\n5118:...when applied to\nclique complexes compared to their graph counterparts [3].\nBuilding upon the graph anomaly detection frameworks developed\nby Akoglu and Faloutsos [1] and Huang et al. [21], we propose a\nnovel method that leverages simplicial complexes to capture and\nanalyze multi-way interactions in temporal data sequences. It is\nimportant to distinguish our focus on temporal anomaly detection\nin time-evolving networks from the related but distinct problem\nof identifying anomalous substructures within static networks, as\nthese two problems address fundamentally different analytical ob-\njectives despite their similar names.\nThe incorporation of higher-order interactions ...\n--\n6225:...measures compared to dyadic interactions. Second,\neven if we only have pairwise interaction data, the application of\ngraph lifting techniques results in improved anomaly detection\ncapabilities. Our experimental results indicate that our method\nachieves superior accuracy when applied to lifted graph datasets\ncompared to conventional spectral approaches on graph skeletons\nand can even offer enhanced computational efficiency.\nHLSAD operates through the following systematic process: For\neach snapshot within a temporal sequence of simplicial complexes,\nwe compute the corresponding Hodge Laplacians up to a user-\nspecified order. Subsequently, we extract the principal eigenvalues\nfrom both up and down Hodge Laplacians and concatenate these\nspectral features into a comprehensive feature vector for each tem-\nporal instance. Employing a sliding window mechanism, we derive\na characteristic feature vector by computing a weighted average\nacross the window’s temporal span. When a new feature vector\nexhibits significant deviation from this established characteristic\npattern, we designate the corresponding temporal instance as an\nanomaly. We illustrate this systematic process in Figure 1 and high-\nlight a case where our higher-order approach successfully identifies\nan anomaly that is overlooked by traditional graph-based methods.\nContribution. To the best of our knowledge, this paper presents\nthe first methodology for anomaly detection in temporal sequences\nof simplicial complexes. Our experimental results demonstrate that\nleveraging simplicial complex representations yields superior per-\nformance compared to traditional graph-based approaches in two\nkey scenarios: First, when analyzing datasets containing inherent\nhigher-order interactions, and second, when applying graph lifting\ntechniques to enrich the topological structure.\nOutline. The remainder of this paper is organized as follows: In\nSection 2, we review the existing literature on graph anomaly detec-\ntion methods. In Section 3, we introduce the mathematical frame-\nwork and notation used throughout this work. Section 4 formally\ndefines the anomaly detection problem on simplicial complexes\nthat we focus on. In Section 5, we present our spectral approach for\ndetecting anomalies using Hodge Laplacians. Section 6 evaluates\nour method on synthetic and real-world datasets, demonstrating its\neffectiveness for event and change point detection. Finally, Section 7\nsummarizes our findings and discusses future research directions.\n2\nRelated Work\nFollowing the taxonomy established by Ranshous et al. [29]...\n--\n[140 more matches not shown]", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [31] TOOL CALL — WebFetch · 2026-07-09 00:51:24 UTC

```
URL: https://pubmed.ncbi.nlm.nih.gov/35469511/
Prompt: List all journal names mentioned in this article on repeatedly suppressed journals from Clarivate's JCR. Specifically: which journals were suppressed for stacking vs. self-citation, and what years? List every journal name mentioned.
```

### [32] TOOL CALL — WebSearch · 2026-07-09 00:51:24 UTC

```
JCR 2020 33 journals suppressed MDPI impact factor 2019 data self-citation names list
```

### [33] TOOL CALL — WebSearch · 2026-07-09 00:51:24 UTC

```
Clarivate 2024 impact factor suppression stacking "Climate Change Economics" "Environmental Science" journal names list
```

### [34] TOOL RESULT — WebFetch · 2026-07-09 00:51:26 UTC

```
{"bytes": 105789, "code": 200, "codeText": "OK", "result": "Based on the content provided, I cannot list specific journal names, suppression years, or the distinction between stacking versus self-citation violations.\n\nThe abstract states: \"the 18 journals that were suppressed three or more times from the JCR\" and notes \"these 18 journals were repeatedly and exclusively suppressed for being excessive self-citers.\" However, the actual journal names are not included in this PubMed record excerpt.\n\nTo obtain the complete list of journals, their suppression years, and detailed violation types, you would need to access the full text article through Atypon or another source that provides the complete study data.", "durationMs": 3286, "url": "https://pubmed.ncbi.nlm.nih.gov/35469511/"}
```

### [35] TOOL RESULT — WebSearch · 2026-07-09 00:51:30 UTC

```
{"query": "JCR 2020 33 journals suppressed MDPI impact factor 2019 data self-citation names list", "results": [{"tool_use_id": "srvtoolu_01GfTfXxPkG8A2oHLYDVBbYT", "content": [{"title": "Updated MDPI Journals Impact Factors - Journal Citation Reports (Clarivate) | iLovePhD", "url": "https://ilovephd.com/updated-mdpi-journals-impact-factors-journal-citation-reports-clarivate/"}, {"title": "Journal citation reports and the definition of a predatory journal: The case of the Multidisciplinary Digital Publishing Institute (MDPI) | Research Evaluation | Oxford Academic", "url": "https://academic.oup.com/rev/article/30/3/405/6348133"}, {"title": "Updated Impact Factors Released in the Journal Citation Reports (Clarivate)", "url": "https://www.mdpi.com/about/announcements/2041"}, {"title": "2025 Impact Factors Released", "url": "https://www.mdpi.com/about/announcements/17055"}, {"title": "2020 Impact Factors - Released", "url": "https://www.mdpi.com/about/announcements/2844"}, {"title": "Seventeen journals lose impact factors for suspected citation manipulation – Retraction Watch", "url": "https://retractionwatch.com/2024/06/27/seventeen-journals-lose-impact-factors-for-suspected-citation-manipulation/"}, {"title": "Standards | Announcements", "url": "https://www.mdpi.com/journal/standards/announcements/12475"}, {"title": "Journal delisted from clarivate index due to controversy", "url": "https://www.facebook.com/groups/reviewer2/posts/10163370016640469/"}, {"title": "2023 Impact Factors for MDPI Journals Released", "url": "https://www.mdpi.com/about/announcements/8686"}, {"title": "2024 Journal Impact Factors Released", "url": "https://www.mdpi.com/about/announcements/12177"}]}, "Based on the search results, I found relevant information about journals suppressed in the 2020 JCR:\n\nClarivate suppressed 33 journals in 2020 for self-citation. Journals are suppressed from the report due to \"anomalous citation behavior, including where there is evidence of excessive journal self-citation and/or citation stacking (which involves two or more journals)\".\n\nHowever, the search results do not provide the specific list of all 33 journal names that were suppressed in the 2020 JCR for the 2019 data. While the search results mention that suppression occurred and explain the reasons for it, they don't contain the complete names list you're looking for.\n\nTo find the complete list of the 33 suppressed journals, you may need to:\n- Consult the official Clarivate Journal Citation Reports documentation from 2020\n- Contact Clarivate directly for their official records\n- Look for academic papers or reports that specifically document this event with the full list"], "durationSeconds": 5.891279402999993, "searchCount": 1}
```

### [36] TOOL RESULT — WebSearch · 2026-07-09 00:51:30 UTC

```
{"query": "Clarivate 2024 impact factor suppression stacking \"Climate Change Economics\" \"Environmental Science\" journal names list", "results": [{"tool_use_id": "srvtoolu_01RAYxZhBfkz5fcBKmF8WFiM", "content": [{"title": "Seventeen journals lose impact factors for suspected citation manipulation – Retraction Watch", "url": "https://retractionwatch.com/2024/06/27/seventeen-journals-lose-impact-factors-for-suspected-citation-manipulation/"}, {"title": "Environmental Science and Technology Impact Factor: 12.2", "url": "https://manusights.com/blog/environmental-science-and-technology-impact-factor"}, {"title": "2024 Research Fronts: Top Scientific Trends | Clarivate", "url": "https://clarivate.com/academia-government/blog/2024-research-fronts-insights-into-top-and-emerging-scientific-trends/"}, {"title": "Clarivate Releases JCR 2025 Impact Factors - Journal Impact Factor 2026", "url": "https://impactfactorforjournal.com/jcr-2025-latest-impact-factor-list/"}, {"title": "2024 impact factor increases again and submissions up ~30%", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12323757/"}, {"title": "Learn about Climate and Development", "url": "https://www.tandfonline.com/journals/tcld20/about-this-journal"}, {"title": "The Clarivate Impact Factor | Clarivate", "url": "https://clarivate.com/academia-government/essays/impact-factor/"}, {"title": "Impact Factor 2023 for Clinical Neuroradiology", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11339139/"}, {"title": "Impact Factor Insights 2025: Analysis of Pakistani Academic Journals", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12302113/"}]}, "Based on the search results, I found relevant information about the 2024 impact factor suppression issue you're asking about.\n\nClarivate suppressed Journal Impact Factors for 17 journals in 2024 due to suspected citation manipulation, including Climate Change Economics and Environmental Science & Pollution Research.\n\nClimate Change Economics was suppressed because of unusual citation patterns with Environmental Science & Pollution Research, which Clarivate found suspicious for an economics journal. The journal's editor-in-chief explained that the journal focuses on climate change and links economic studies to natural science, which accounts for the high number of science citations.\n\nTwo other suppressed journals—Granular Computing (a Springer title) and Information Sciences (from Elsevier)—both had Witold Pedrycz as editor-in-chief.\n\nThe main source I found was a Retraction Watch article from June 2024 that covered this suppression event. If you need a comprehensive list of all 17 journals that were suppressed, I'd recommend consulting the original Clarivate announcement or the full Retraction Watch article, as the search results only named a few specific journals."], "durationSeconds": 6.366198187000002, "searchCount": 1}
```

### [37] TOOL CALL — WebFetch · 2026-07-09 00:51:52 UTC

```
URL: https://retractionwatch.com/2024/06/27/seventeen-journals-lose-impact-factors-for-suspected-citation-manipulation/
Prompt: List all 17 journal names that lost 2024 impact factors. For each, specify whether the reason was self-citation or citation stacking. List specific stacking pairs mentioned.
```

### [38] TOOL CALL — Bash · 2026-07-09 00:51:52 UTC

```
Grep HLSAD PDF for specific Laplacian degree and datasets:
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://arxiv.org/pdf/2505.24534" --pattern "L_1|L_\{1\}|boundary operator|simplicial|triangle|dataset|real.world|contact|email|network|Social" -i --max-matches 40 --context-chars 400 2>&1 | head -250
```

### [39] TOOL RESULT — WebFetch · 2026-07-09 00:51:52 UTC

```
{"bytes": 121779, "code": 200, "codeText": "OK", "result": "# Seventeen Journals That Lost 2024 Impact Factors\n\nBased on the article, here are the 17 suppressed journals with available details:\n\n## Journals with Specified Issues:\n\n1. **Climate Change Economics** - Citation stacking with Environmental Science & Pollution Research\n2. **Environmental Science & Pollution Research** - Citation stacking with Climate Change Economics\n3. **Ukrainian Journal for Physical Optics** - Citation stacking with Optik journal (46% of citations)\n4. **Activities, Adaptation & Aging** - Self-citation and journal focus changes\n5. **Resources Policy** - Citation stacking with two unnamed small journals\n6. **Granular Computing** - Reason unspecified\n7. **Information Sciences** - Citations in 12 articles from 2023 (unspecified type)\n8. **Cuadernos De Economía** - High citations from other journals (under verification)\n\n## Journals Without Specified Reasons:\n\n9. Engineering, Technology & Applied Science Research\n10. Exploratory Animal and Medical Research\n11. Library Hi Tech\n12. Regional Statistics\n13. SOCAR Proceedings\n14. Panminerva Medica\n15. Minerva Medica\n16. Gazzetta Medica Italiana Archivo Per Le Scienze Mediche\n17. Annals Of Financial Economics\n\nThe article notes Clarivate suppressed these journals due to \"anomalous citation behavior\" but does not explicitly categorize most as purely self-citation or citation stacking.", "durationMs": 5083, "url": "https://retractionwatch.com/2024/06/27/seventeen-journals-lose-impact-factors-for-suspected-citation-manipulation/"}
```

### [40] TOOL CALL — WebSearch · 2026-07-09 00:51:52 UTC

```
2019 JCR impact factor suppressed stacking journals list 2018 citation data Clarivate names
```

### [41] TOOL RESULT — Bash · 2026-07-09 00:51:52 UTC

```
{"stdout": "URL: https://arxiv.org/pdf/2505.24534\nType: PDF\nPattern: L_1|L_\\{1\\}|boundary operator|simplicial|triangle|dataset|real.world|contact|email|network|Social (173 matches in 64844 chars)\n\n--- Content ---\n\n70:arXiv:2505.24534v1  [cs.LG]  30 May 2025\nHLSAD: Hodge Laplacian-based Simplicial Anomaly Detection\nFlorian Frantzen\nRWTH Aachen University\nDepartment of Computer Science\nAachen, Germany\nflorian.frantzen@cs.rwth-aachen.de\nMichael T. Schaub\nRWTH Aachen University\nDepartment of Computer Science\nAachen, Germany\nschaub@cs.rwth-aachen.de\nFigure 1: Illustrative process of anomaly detection on a toy-example simplicial complex sequence. Starting from a time-evolving\nsimplicial complex, we compute the Hodge Laplacians for each snapshot and extract spectral features for each. We employ\na sliding window approach to identify anomalies by evaluating the deviation of current spectral features from established\ntemporal patterns. In this illustrative example, HLSAD successfully detects all three artificially introduced anomalies, whereas\ntraditional graph-based analysis fails to identify the final anomaly that manifests in higher-order interactions.\nAbstract\nIn this paper, we propose HLSAD, a novel method for detecting\nanomalies in time-evolving simplicial complexes. While traditional\ngraph anomaly detection techniques have been extensively stud-\nied, they often fail to capture changes in higher-order interactions\nthat are crucial for identifying complex structural anomalies. These\nhigher-order interactions can arise either directly from the under-\nlying data itself or through graph lifting techniques. Our approach\nleverages the spectral properties of Hodge Laplacians of simplicial\ncomplexes to effectively model multi-way interactions among data\npoints. By incorporating higher-dimensional simplicial structures\ninto our method, our method enhances both detection accuracy\nand computational efficiency. Through comprehensive experiments\non both synthetic and real-world datasets, we demonstrate that our\napproach outperforms existing graph methods in detecting both\nevents and change points.\nCCS Concepts\n• Mathematics of computing →Graph theory; Topology; • Com-\nputing methodologies →Anomaly detection; Temporal rea-\nsoning; Spectral methods; • Theory of computation →Dynamic\ngraph algorithms.\nThis work is licensed under a Creative Commons Attribution 4.0 International License.\nKDD ’25, Toronto, ON, Canada\n© 2025 Copyright held by the owner/author(s).\nACM ISBN 979-8-4007-1454-2/2025/08\nhttps://doi.org/10.1145/3711896.3736998\nKeywords\nanomaly detection, change point detection, event detection, simpli-\ncial complex, spectral methods\nACM Reference Format:\nFlorian Frantzen and Michael T. Schaub. 2025. HLSAD: Hodge Laplacian-\nbased Simplicial Anomaly Detection. In Proceedings of the 31st ACM SIGKDD\nConference on Knowledge Discovery and Data Mining V.2 (KDD ’25), August\n3–7, 2025, Toronto, ON, Canada. ACM, New York, NY, USA, 11 pages. https:\n//doi.org/10.1145/3711896.3736998\nKDD Availability Link:\nThe source code of this paper has been made publicly available at https:\n//doi.org/10.5281/zenodo.15511585 and at https://git.rwth-aachen.de/netsci/\nhlsad.\n1\nIntroduction\nAnomaly detection within time-evolving networks has widespread\napplications across diverse domains, including network security\nfor detecting intrusions and system faults [6, 22, 31], social net-\nwork analysis for identifying collective behavioral changes induced\nby external factors [27, 34], and ecological monitoring for detect-\ning ecosystem disturbances [5]. Accordingly, many graph-based\ntechniques have been developed for identifying events and change\npoints in dynamic networks [2, 29, 35]. Despite their utility, graph-\nbased approaches are however limited by their focus on dyadic\nrelationships, and fail to capture higher-order interactions that can\n\nKDD ’25, August 3–7, 2025, Toronto, ON, Canada\nFlorian Frantzen and Michael T. Schaub\nbe essential for identifying complex structural anomalies in the un-\nderlying system. Such higher-order data can manifest itself through\ndifferent mechanisms:\nHigher-Order Data Many real-world datasets inherently contain\nmulti-way interactions that extend beyond dyadic relation-\nships. Traditional graph-based methods are fundamentally\nlimited in their ability to capture and analyze these higher-\norder structures. For instance, during the COVID-19 pan-\ndemic, social distancing measures disproportionately affected\nlarge group gatherings compared to pairwise interactions,\ncreating structural changes that are more readily detectable\nthrough higher-order methods [28].\nLifting Even when data only contains pairwise relations between\nentities, we can employ graph lifting techniques to construct\na simplicial complex representation. A common approach\nidentifies cliques in the graph with equivalent simplices. The\neffectiveness of lifting has been demonstrated in various con-\ntexts; notably, the Weisfeiler-Lehman isomorphism test ex-\nhibits strictly greater discriminative power when applied to\nclique complexes compared to their graph counterparts [3].\nBuilding upon the graph anomaly detection frameworks developed\nby Akoglu and Faloutsos [1] and Huang et al. [21], we propose a\nnovel method that leverages simplicial complexes to capture and\nanalyze multi-way interactions in temporal data sequences. It is\nimportant to distinguish our focus on temporal anomaly detection\nin time-evolving networks from the related but distinct problem\nof identifying anomalous substructures within static networks, as\nthese two problems address fundamentally different analytical ob-\njectives despite their similar names.\nThe incorporation of higher-order interactions via simplices in\nour method provides significant advantages over traditional graph-\nbased approaches: First, it enhances detection accuracy through the\nexplicit modeling of higher-order interactions that are inherently\nabsent in graph represen...\n--\n6225:...demic modeling, where\nlarge group gatherings may exhibit distinct response patterns to\nintervention measures compared to dyadic interactions. Second,\neven if we only have pairwise interaction data, the application of\ngraph lifting techniques results in improved anomaly detection\ncapabilities. Our experimental results indicate that our method\nachieves superior accuracy when applied to lifted graph datasets\ncompared to conventional spectral approaches on graph skeletons\nand can even offer enhanced computational efficiency.\nHLSAD operates through the following systematic process: For\neach snapshot within a temporal sequence of simplicial complexes,\nwe compute the corresponding Hodge Laplacians up to a user-\nspecified order. Subsequently, we extract the principal eigenvalues\nfrom both up and down Hodge Laplacians and concatenate these\nspectral features into a comprehensive feature vector for each tem-\nporal instance. Employing a sliding window mechanism, we derive\na characteristic feature vector by computing a weighted average\nacr...\n--\n7394:...attern, we designate the corresponding temporal instance as an\nanomaly. We illustrate this systematic process in Figure 1 and high-\nlight a case where our higher-order approach successfully identifies\nan anomaly that is overlooked by traditional graph-based methods.\nContribution. To the best of our knowledge, this paper presents\nthe first methodology for anomaly detection in temporal sequences\nof simplicial complexes. Our experimental results demonstrate that\nleveraging simplicial complex representations yields superior per-\nformance compared to traditional graph-based approaches in two\nkey scenarios: First, when analyzing datasets containing inherent\nhigher-order interactions, and second, when applying graph lifting\ntechniques to enrich the topological structure.\nOutline. The remainder of this paper is organized as follows: In\nSection 2, we review the existing literature on graph anomaly detec-\ntion methods. In Section 3, we introduce the mathematical frame-\nwork and notation used throughout this work. Section 4 formally\ndefines the anomaly detection problem on simplicial complexes\nthat we focus on. In Section 5, we present our spectral approach for\ndetecting anomalies using Hodge Laplacians. Section 6 evaluates\nour method on synthetic and real-world datasets, demonstrating its\neffectiveness for event and change point detection. Finally, Section 7\nsummarizes our findings and discusses future research directions.\n2\nRelated Work\nFollowing the taxonomy established by Ranshous et al. [29], exist-\ning graph anomaly detection algorithms can be categorized into five\nprincipal categories: (1) community-based, (2) compression-based,\n(3) decomposition-based, (...\n--\n9855:...thods exhibiting vary-\ning combinations of these attributes [21, 33]: First, the approach\nshould maintain generality without imposing assumptions about\nthe underlying data distribution, such as conformity to a specific\ngraph model. Second, algorithms should be applicable to both event\nand change point detection scenarios. Third, computational scala-\nbility is crucial, particularly for large-scale networks with dynamic\nnode populations. Within this context, we can also consider offline\nand online-style algorithms, where the former analyzes the entire\ntime-series at once, while the latter flags anomalies in real-time as\nnew data arrives. Fourth, node permutation invariance is essential\nto accommodate datasets where consistent node ordering across\ntemporal snapshots cannot be guaranteed. Fifth, the method should\nprovide quantitative confidence measures for anomaly predictions,\nenhancing interpretability and decision-making capabilities.\nModel-based detection algorithms are a prominent approach in\nliterature, wherein probabilistic graph models are fitted to observed\n\nHLSAD: Hodge Laplacian-based Simplicial Anomaly Detection\nKDD ’25, August 3–7, 2025, Toronto, ON, Canada\ndata and anomalies are identified through parameter changes. These\napproaches offer significant advantages in terms of interpretabil-\nity, as detected parameter shifts directly correspond to identifiable\nlarge-scale structural changes in the network. Peel and Clauset\n[27] developed an online learning algorithm for change point de-\ntection in dynamic networks, learning probabilistic distributions\nover graphs and detecting when these distributions shift due to\nexternal events. Their method utilizes a generalized hierarchical\nrandom graph model for temporal network representation, though\nthe framework remains model-agnostic. Notably, they identified\na list of different types of change points, including community\nformation and merge events. In a similar direction, Wang et al.\n[33] proposed EdgeMonitoring, which derives snapshot features\nthrough joint edge probability estimation. Their method quantifies\ntemporal dissimilarity using Kolmogorov-Smirnov statistics and\nKullback-Leibler divergence measures. Gahrooei and Paynabar [12]\ndeveloped a framework that fits generalized linear models to sequen-\ntial network snapshots, employing extended Kalman filtering for\ncontinuous parameter estimation. They identify structural changes\nthrough significant deviations in the estimated model parameters.\nIdé and Kashima [22] (Activity Vector), Akoglu and Faloutsos\n[1] and Huang et al. [21] (LAD) proposed different spectral-based\nmethods for anomaly detection in dynamic graphs, which all rely\non identifying changes in the graph spectrum as proxy for struc-\ntural changes. These methods have been shown to be effective in\ndetecting both event and change points in dynamic networks. In\nparticular, LAD was later extended to attributed [20] and multi-view\ngraphs [19].\nComplementing these approaches, Koutra et al. [23] developed\nTENSORSPLAT, a decomposition-based method that leverages ten-\nsor factorization to identify structural changes in dynamic net-\nworks. Koutra et al. [24] introduced DeltaCon, which utilizes di-\nrect similarity-based comparisons between consecutive grap...\n--\n13149:...tilizing intermediate feature representations.\nWhile this method offers an alternative perspective on structural\nchange detection, it imposes significant constraints: the framework\nrequires both a static node set and consistent node identification\nacross temporal snapshots.\nWith the increased interest in deep learning approaches in re-\ncent years, several methods have emerged that leverage neural\nnetwork architectures for anomaly detection in dynamic graphs.\nNotably, Gong et al. [13] conceptualized change point detection\nas a temporal prediction framework, employing a latent evolution\nmodel to forecast subsequent graph snapshots. Their approach\nidentifies anomalies when significant discrepancies arise between\npredicted and observed network states. Sulem et al. [30] proposed\na method based on siamese graph neural networks to learn a simi-\nlarity function between graph snapshots and detect change points\nbased on deviations from this learned similarity. To the best of our\nknowledge, however, again no deep learning approach explores\nhigher-order data in a simplicial complex setting.\nFor an in-depth review of existing anomaly detection methods on\ndynamic graphs, readers are directed to the recent surveys by Zhou\net al. [35] and by Ho et al. [18]. Additional foundational perspectives\ncan be found in the older surveys by Akoglu et al. [2] and Ranshous\net al. [29].\n1\n2\n3\n4\n𝑩1 =\n©­­­\n«\n1\n1\n1\n0\n1\n0", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [42] TOOL CALL — WebFetch · 2026-07-09 00:51:52 UTC

```
URL: https://arxiv.org/abs/2202.11360
Prompt: Summarize the key method in this paper on deep graph learning for anomalous citation detection. What datasets are used, what is the model type, and what is the main contribution vs. Hodge-decomposition flow analysis?
```

### [43] TOOL RESULT — WebFetch · 2026-07-09 00:51:54 UTC

```
{"bytes": 42025, "code": 200, "codeText": "OK", "result": "Based on the provided content, here's what can be determined about this paper:\n\n**Model Type & Key Method:**\nThe paper proposes \"GLAD (Graph Learning for Anomaly Detection),\" described as incorporating \"text semantic mining to network representation learning by adding both node attributes and link attributes via graph neural networks.\" Additionally, the authors introduce an algorithm called \"CPU (Citation PUrpose) to discover the purpose of citation based on citation texts.\"\n\n**Datasets:**\nThe abstract indicates \"The performance of GLAD is validated through a simulated anomalous citation dataset,\" though specific dataset names or characteristics are not detailed in this page content.\n\n**Main Contribution:**\nThe work addresses anomaly detection in citation networks by leveraging both content relevance and hidden relationships between papers through deep graph learning approaches.\n\n**Comparison to Hodge-Decomposition:**\nThe provided webpage content does not mention Hodge-decomposition flow analysis or make any comparative claims against such methods. This information is not available in the materials presented.\n\nThe abstract emphasizes the significance of detecting citation manipulation and inflation in scholarly networks, positioning this as an understudied problem area requiring attention.", "durationMs": 4181, "url": "https://arxiv.org/abs/2202.11360"}
```

### [44] TOOL RESULT — WebSearch · 2026-07-09 00:51:56 UTC

```
{"query": "2019 JCR impact factor suppressed stacking journals list 2018 citation data Clarivate names", "results": [{"tool_use_id": "srvtoolu_01QD67JrQ9qQMSJ7ngse9x62", "content": [{"title": "Title Suppressions", "url": "https://help.incites.clarivate.com/incitesLiveJCR/JCRGroup/titleSuppressions.html"}, {"title": "Title Suppressions - Journal Citation Reports - Zendesk", "url": "https://journalcitationreports.zendesk.com/hc/en-gb/articles/28351398819089-Title-Suppressions"}, {"title": "Impact Factor Denied to 20 Journals For Self-Citation, Stacking - The Scholarly Kitchen", "url": "https://scholarlykitchen.sspnet.org/2018/06/27/impact-factor-denied-20-journals-self-citation-stacking/"}, {"title": "The Web of Science Group Releases 2019 Journal Citation Reports, Revealing the World's Most Influential Journals", "url": "https://www.prnewswire.com/news-releases/the-web-of-science-group-releases-2019-journal-citation-reports-revealing-the-worlds-most-influential-journals-300871565.html"}, {"title": "Announcing the 2019 Journal Citation Reports | Clarivate", "url": "https://clarivate.com/academia-government/blog/announcing-the-2019-journal-citation-reports/"}, {"title": "Journal Citation Reports (JCR) – Complete Guide – Scientific News", "url": "https://news.europub.co.uk/journal-citation-reports-jcr-complete-guide/"}, {"title": "Journal Citation Reports | Clarivate", "url": "https://clarivate.com/products/scientific-and-academic-research/research-analytics-evaluation-and-management-solutions/journal-citation-reports/"}, {"title": "Journal Citation Reports", "url": "https://jcr.clarivate.com/"}, {"title": "JCR Editorial Expression of Concern – Journal Citation Reports", "url": "https://journalcitationreports.zendesk.com/hc/en-gb/articles/28351368597521-JCR-Editorial-Expression-of-Concern"}, {"title": "Citation issues cost these 20 journals their impact factors this year – Retraction Watch", "url": "https://retractionwatch.com/2025/06/18/clarivate-impact-factor-suppression-list-2025-self-citation-stacking/"}]}, "Based on the search results, I found information about the 2019 Journal Citation Reports (JCR) release and journal suppressions for anomalous citation behavior.\n\n## Key Findings:\n\n**2019 JCR Release (2018 Citation Data):**\n\nThe Web of Science Group, part of Clarivate Analytics, released the 2019 update to its annual Journal Citation Report (JCR) on June 20, 2019.\n\n**Journal Suppressions:**\n\nAfter thorough investigation of anomalous citation behavior, 17 journals were suppressed from the 2019 JCR to ensure the integrity of the data. Seventeen journals have been suppressed from the JCR this year to ensure the integrity of the reports, representing 0.14% of the journals listed.\n\n**Reasons for Suppression:**\n\nThe JCR is the only citation index which monitors and excludes journals that demonstrate anomalous citation behavior including where there is evidence of excessive journal self-citation and citation stacking.\n\n**Types of Anomalies:**\n\nThe recipient and donor journal pairs along with the percentage of citations in the Journal Impact Factor numerator that are from the donor to the recipient are tracked. Metrics for the titles listed are not published due to anomalous citation patterns found in the 2018 citation data. These patterns result in a significant distortion of the Journal Impact Factor and rank that does not accurately reflect the journal's citation performance in the literature.\n\nThe official Clarivate documentation indicates that the suppressed journals list and detailed data points about each suppressed journal are available through the JCR help documentation."], "durationSeconds": 7.631752951000002, "searchCount": 1}
```

### [45] TOOL CALL — Bash · 2026-07-09 00:52:18 UTC

```
Grep HLSAD PDF for dataset names in experiments section:
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://arxiv.org/pdf/2505.24534" --pattern "dataset|experiment|Table|Senate|Copenhagen|enron|sociopatterns|InVS|Hypertext|DAWN|bitcoin" -i --max-matches 40 --context-chars 500 2>&1 | tail -300
```

### [46] TOOL RESULT — Bash · 2026-07-09 00:52:18 UTC

```
{"stdout": "across temporal snapshots. Row or column permutations of the\nHodge Laplacian matrices do not affect their singular values, en-\nabling our method to handle arbitrary simplex orderings.\nFinally, the computational efficiency of sparse SVD algorithms\nmakes our approach practical for large-scale datasets. Real-world\nsimplicial complexes often exhibit sparsity, particularly at higher\ndimensions where the number of simplices typically decreases. By\ncomputing only the top 𝑘singular values through truncated SVD,\nwe can achieve significant computational savings compared to full\ndecomposition while maintaining high detection accuracy.\nThe selection of spectral features from Hodge Laplacians presents\nmultiple strategic approaches, each capturing distinct topological\ncharacteristics of the simplicial complex while offering different\ncomputational trade-offs. These methodological choices signifi-\ncantly influence both the structural information preserved and the\nalgorithmic efficiency of the detection process and can be tuned on\na per-dataset basis. We discuss this decision matrix further in the\nnext section. For simplicity, here we use the first 𝐾Hodge Lapla-\ncians and extract the first ℓsingular values from each, resulting\nin a feature vector of length 𝐾· ℓfor each temporal snapshot. If a\nsimplicial complex has a rank lower than 𝐾, or if the number of\nsingular values is less than ℓ, we pad the feature vector with zeros.\n5.2\nSelection of Singular Values\nThe selection of singular values exhibits multiple dimensions of\nchoice: First,...\n--\n28596:...omputa-\ntional efficiency and structural information retention: A larger value\nof ℓenables us to capture more nuanced topological features at the\ncost of increased computational complexity of the anomaly detec-\ntion algorithm. Retaining only a relatively small number of singular\nvalues usually sufficiently characterizes the dominant structural\nproperties while maintaining computational tractability. While one\ncould theoretically optimize this parameter independently for each\norder, our code and experiments maintain a uniform selection across\nranks to reduce the parameter space complexity.\nThird, in contrast to the graph Laplacian, the Hodge Laplacian is\ncomposed of two distinct components: the down-Laplacian 𝑳down\n𝑘\nand the up-Laplacian 𝑳up\n𝑘\n(with the graph Laplacian consisting\nsolely of the latter component). This decomposition introduces an\nadditional dimension for spectral feature optimization, enabling\nselective focus on the spectral properties of either component in-\ndividually or a combination of both. This way, depending on the\ndataset, one can fine-tune the algorithm to emphasize different\nstructural aspects of the simplicial complex.\n5.3\nContext Matrix and Typical Behavior\nFollowing established practices in anomaly detection literature, we\nevaluate anomalies relative to a temporal context window of size\n𝑤containing previous observations. To that end, we maintain a\ncontext matrix 𝑪(𝑡) comprising the ℓ2-normalized spectra from the\n\nKDD ’25, August 3–7, 2025, Toronto, ON, Canada\nFlorian Frantzen and Michael T. Schaub\nlast 𝑤sna...\n--\n30351:...aseline for\ncomparison with the current snapshot 𝝈(𝑡). Akoglu and Faloutsos\n[1] investigated two methodologies for obtaining such a typical\nfeature vector: First, they used\n˜𝝈(𝑡) = 1\n𝑤\n𝑤\n∑︁\n𝑖=1\n𝑪:,𝑖= 1\n𝑤\n𝑤\n∑︁\n𝑖=1\n𝝈(𝑡−𝑖−1)\n(4)\nas the arithmetic average of the last 𝑤feature vectors. Second, they\ncomputed the left singular vector of the context matrix 𝑪(𝑡) using\nSVD decomposition, which can be interpreted as a weighted average\nof the preceding feature vectors. Both their empirical analysis and\nour experiments demonstrated superior performance of the SVD-\nbased approach, leading us to adopt the SVD-based averaging.\n5.4\nScoring Function\nLet ˜𝝈(𝑡)\n𝑠\nand ˜𝝈(𝑡)\nℓ\ndenote the characteristic spectral features derived\naccording to the previous section within the short-term and long-\nterm context windows 𝑤𝑠and 𝑤ℓ, respectively. Our goal now is\nto quantify the dissimilarity between the current spectral features\n𝝈(𝑡) and these characteristic behaviors.\nTo quantify the structural deviation, we employ the angula...\n--\n33968:... high accuracy. In practical applications, we\ncan leverage the inherent sparsity structure of the Hodge Laplacians\nto achieve substantial computational efficiency gains.\nLet 𝑛𝑘denote the maximum number of 𝑘-simplices across all\ntemporal instances of the simplicial complex sequence {X(𝑡)}𝑇\n𝑡=1.\nThe computational complexity of HLSAD is then given by\nO\n \n𝑇·\n𝐾\n∑︁\n𝑘=0\n𝑛2\n𝑘log ℓ\n!\n,\n(8)\nwhere the summation over 𝑘accounts for the spectral computations\nrequired for each Hodge Laplacian up to order 𝐾.\n6\nExperiments\nIn this section, we present a comprehensive evaluation of HLSAD\nutilizing both synthetic and real-world datasets. Through these\nexperiments, we demonstrate the effectiveness of our approach\nin detecting both event and change points both for data-informed\nhigher-order simplices and graph liftings. Statistics for all datasets\ncan be found in Table 5 in the appendix.\nTo quantitatively assess the performance of our anomaly detec-\ntion method, we employ the Hits@𝑁metric, which measures the\nproportion of correctly identified anomalies among the top 𝑁most\nanomalous points detected by our algorithm. Specifically, a Hits@7\nscore of 0.5 indicates that 50% of the seven points identified as most\nanomalous correspond to actual anomalies according to the ground\ntruth labels. If 𝑁equals the number of ground truth anomalies, then\nthe Hits@N score is equal to the recall. For synthetic experiments,\nwe utilize the ground truth labels inherent in the generation process\nfor evaluation purposes. In real-world datasets, we leverage known\nsignificant external events as ground truth, while acknowledging\nthe limitation that additional unidentified external factors may have\ninfluenced the temporal evolution of the data.\n\nHLSAD: Hodge Laplacian-based Simplicial Anomaly Detection\nKDD ’25, August 3–7, 2025, Toronto, ON, Canada\n0\n250\n500\n0\n0.2\n0.4\n0.6\n0.8\n1\n0\n250\n500\n0\n0.2\n0.4\n0.6\n0.8\n1\n0\n250\n500\n0\n0.2\n0.4\n0.6\n0.8\n1\n0\n250\n500\n0\n0.2\n0.4\n0.6\n0.8\n1\nHits@7\nHybrid\nNumber of Singular Values\nHits@7\nResampled\nHits@5\nLarge\nHits@5\nTriangle Closing\nMax Rank:\n0\n1\n2\nFigure 4: Performance comparison on synthetic data. We compare the Hits@𝑁scores as a function of the total number of\nsingular values used for anomaly detection. The solid line gives the Hits@𝑁score for 𝑁the number of true anomalies in the\ndata generation process. The dashed line gives the Hits@𝑁+ 2 score, i.e., the accuracy with up to 2 false positives.\n6.1\nSynthetic Experiments\nTo evaluate HLSAD’s effectiveness and demonstrate its advantages\nover graph-based approaches, we conduct four synthetic exper-\niments: In the first two, we replicate the hybrid and resampled\nsynthetic experiments by Huang et al. [21]. The time series origi-\nnates from graphs sampled from a stochastic block model (SBM),\nwhich are lifted to simplicial complexes using a clique lifting. In a\nthird large experiment, we evaluate scalability by using the same\nsetting with 10 000 nodes. In a fourth experiment, we introduce a tri-\nangle closing dataset where, instead of using clique lifting, triangles\nare closed with a given probability. This setting reflects scenarios\nwhere external events have a distinct influence on multi-way in-\nteractions in the network, which may differ from their impact on\ndyadic relationships. In all settings, we change the model parame-\nters at pre-selected time steps to simulate events and change points\nin the data. The exact sampling parameters for all experiments are\ngiven in Appendix B. We use a short term and a long term window\nof 𝑤𝑠= 5 and 𝑤ℓ= 10 snapshots, respectively.\nThe Hits@𝑁scores for each dataset as a function on the total\nnumber of singular values computed are shown in Figure 4. For\nthe higher-order cases, the plotted number of singular values refers\nto the total number of singular values computed over all Hodge\nLaplacians, i.e., for a value of 300 on the x-axis and maximum rank\n𝐾= 3, we computed 100 singular values for each Hodge Laplacian.\nIn other words, all points on the same x-axis correspond to the\nsame total number of singular values, though in the higher-order\ncases, these are distributed over multiple Hodge Laplacians.\nThe experimental results demonstrate the superior performance\nof HLSAD in leveraging higher-order structural information com-\npared to the graph-based LAD baseline across both the hybrid, large,\nand triangle closing experiments. HLSAD consistently achieves\nhigher Hits@𝑁scores while requiring significantly fewer singular\nvalues to attain comparable detection accuracy, indicating enhanced\ncomputational efficiency. Specifically, in the hybrid setting, HLSAD\nsuccessfully identifies all anomalies using only 40 singular values,\nwhereas LAD requires more than 300 singular values to achieve sim-\nilar performance. The advantage of HLSAD is particularly evident\nin the triangle closing experiment, where it detects all anomalies\nTable 1: Prediction scores on the UCI and Senate real-world\ndatasets. We compare HLSAD against several other state-of-\nthe-art anomaly detection techniques.\nDataset\nUCI\nSenate\nMetric\nHits@10\nHits@2\nHLSAD (ours)\n1.0\n1.0\nLAD\n0.5\n1.0\nEdgeMonitoring\n0.0\n1.0\nActivity Vector\n0.5\n0.5\nTENSORPLAT\n0.0\n0.0\nwith merely 10 singular values, while LAD fails to identify anom-\nalies that manifest exclusively in higher-order interactions due to\nits inherent limitation to dyadic relationships.\nThe interpretation of the resampled experiment yields more nu-\nanced results: While the general trends observed in other experi-\nments persist, namely superior overall performance and enhanced\nefficiency with fewer singular values, there exist specific instances\nwhere LAD marginally outperforms HLSAD. Specifically, LAD\nachieves a Hits@7 score of 0.8 with 250 singular values, whereas\nHLSAD requires approximately 320 singular values to attain equiv-\nalent performance. However, examination of the Hits@9 metric\nreveals that HLSAD consistently and significantly outperforms LAD\nacross all singular value quantities in a minor relaxed metric. This\nsuggests that while HLSAD may occasionally identify false posi-\ntives, it demonstrates superior capability in detecting the complete\nset of true anomalies within the data.\n6.2\nUCI Online Message Dataset\nWe further replicate the experiment on the UCI Online Message\ndataset [26], which captures communication patterns within an\nonline student community at the University of California, Irvine.\nThe dataset comprises a weighted network where nodes represent\nusers and edges represent message exchanges between them. Edge\nweights correspond to message lengths, quantifying interaction\n\nKDD ’25, August 3–7, 2025, Toronto, ON, Canada\nFlorian Frantzen and Michael T. Schaub\n0\n2\n4\n0.6\n0.8\n1\n0\n2\n4\n0.6\n0.8\n1\nDelay\nPrecision\nDelay\nRecall\nLetoChan...\n--\n[55 more matches not shown]", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [47] TOOL CALL — WebFetch · 2026-07-09 00:52:18 UTC

```
URL: https://help.incites.clarivate.com/incitesLiveJCR/JCRGroup/titleSuppressions.html
Prompt: List all suppressed journal names with their year and reason (self-citation vs stacking). Include all tables of suppressed journals.
```

### [48] TOOL RESULT — WebFetch [ERROR] · 2026-07-09 00:52:18 UTC

```
Error: ECONNREFUSED
```

### [49] TOOL CALL — WebFetch · 2026-07-09 00:52:18 UTC

```
URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC9424957/
Prompt: List all journal names mentioned as suppressed from JCR. Specify which were for stacking vs self-citation, and the year of suppression. List every journal name mentioned in this article.
```

### [50] TOOL CALL — WebSearch · 2026-07-09 00:52:18 UTC

```
MDPI journals suppressed 2020 JCR impact factor list self-citation 33 journals names Symmetry Entropy Applied Sciences
```

### [51] TOOL RESULT — WebFetch · 2026-07-09 00:52:22 UTC

```
{"bytes": 295898, "code": 200, "codeText": "OK", "result": "# Journal Suppression Information\n\n## Journals Suppressed from JCR\n\nThe article mentions **seven journals suppressed in 2021** but does not name them specifically. The text states: \"We also summarized the changes in the articles of the seven journals suppressed in 2021 due to coercive self-citation.\"\n\n**Suppression Type:** Coercive self-citation (not stacking)\n\n**Year:** 2021\n\n**Key Finding:** \"Among them, six journals increased their articles enormously in 2019 and/or 2020,\" suggesting the suppression was related to rapid article expansion combined with self-citation concerns.\n\n---\n\n## All Journal Names Mentioned in the Article\n\n1. **IEEE Access** (discussed as case study in Section 3.7)\n\nThe article also references journals from these publishers in its analysis:\n- Elsevier journals (10 randomly selected)\n- Springer Nature journals (10 randomly selected)\n- Wiley-Blackwell journals (10 randomly selected)\n- IEEE journals (10 randomly selected)\n- Walter de Gruyter journals (10 randomly selected)\n- Various one-journal publishers (100 journals total analyzed)\n\nHowever, **individual journal names are not provided for most sampled journals**, only publisher groupings and IEEE Access specifically.", "durationMs": 4884, "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9424957/"}
```

### [52] TOOL RESULT — WebSearch · 2026-07-09 00:52:34 UTC

```
{"query": "MDPI journals suppressed 2020 JCR impact factor list self-citation 33 journals names Symmetry Entropy Applied Sciences", "results": [{"tool_use_id": "srvtoolu_015qRJzF8AykSRvyJN8rxLck", "content": [{"title": "ALPSP blog: at the heart of scholarly publishing: MDPI Self-citations study highlights industry alignment and integrity", "url": "https://blog.alpsp.org/2025/03/mdpi-self-citations-study-highlights.html"}, {"title": "Updated MDPI Journals Impact Factors - Journal Citation Reports (Clarivate) | iLovePhD", "url": "https://ilovephd.com/updated-mdpi-journals-impact-factors-journal-citation-reports-clarivate/"}, {"title": "Journal impact factors of MDPI-journals with and without self-citations... | Download Scientific Diagram", "url": "https://www.researchgate.net/figure/Journal-impact-factors-of-MDPI-journals-with-and-without-self-citations-2018_fig5_353862516"}, {"title": "2020 Impact Factors - Released", "url": "https://www.mdpi.com/about/announcements/2844"}, {"title": "Citation issues cost these 20 journals their impact factors this year – Retraction Watch", "url": "https://retractionwatch.com/2025/06/18/clarivate-impact-factor-suppression-list-2025-self-citation-stacking/"}, {"title": "Updated Impact Factors Released in the Journal Citation Reports (Clarivate)", "url": "https://www.mdpi.com/about/announcements/2041"}, {"title": "Title Suppressions - Journal Citation Reports - Clarivate", "url": "https://jcr.help.clarivate.com/Content/title-suppressions.htm"}, {"title": "Sustained Growth of the Impact Factors of MDPI Open Access Journals", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6268482/"}]}, "Let me search more specifically for information about 33 MDPI journals suppressed from the 2020 JCR impact factor list.", {"tool_use_id": "srvtoolu_018H2TkayA4ntuMW5RzscXvd", "content": [{"title": "Entropy | An Open Access Journal from MDPI", "url": "https://www.mdpi.com/journal/entropy"}, {"title": "Symmetry | Announcements", "url": "https://www.mdpi.com/journal/symmetry/announcements/8686"}, {"title": "Entropy | Announcements", "url": "https://www.mdpi.com/journal/entropy/announcements/8686"}, {"title": "MDPI - Wikipedia", "url": "https://en.wikipedia.org/wiki/MDPI"}, {"title": "Symmetry | An Open Access Journal from MDPI", "url": "https://www.mdpi.com/journal/symmetry"}, {"title": "Acknowledgment to Reviewers of Entropy in 2020", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7911195/"}, {"title": "Acknowledgment to Reviewers of the International Journal of Molecular Sciences in 2020", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7865824/"}, {"title": "Acknowledgement to Reviewers of Entropy in 2019", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7516538/"}, {"title": "Continued Growth of the Impact Factors of MDPI Open Access Journals", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6257616/"}]}, "Let me search more specifically for the 2020 JCR suppression list with MDPI journals.", {"tool_use_id": "srvtoolu_01K95XpAXKbvUhKMtPNaGtqy", "content": [{"title": "Title Suppressions - Journal Citation Reports - Clarivate", "url": "https://jcr.help.clarivate.com/Content/title-suppressions.htm"}, {"title": "Citation issues cost these 20 journals their impact factors this year – Retraction Watch", "url": "https://retractionwatch.com/2025/06/18/clarivate-impact-factor-suppression-list-2025-self-citation-stacking/"}, {"title": "Clarivate’s 2020 Journal Citation Report: “Suppressed” Journals Fight Back - Enago Academy", "url": "https://www.enago.com/academy/journals-suppressed-in-the-journal-citation-reports-fight-back/"}, {"title": "ALPSP blog: at the heart of scholarly publishing: MDPI Self-citations study highlights industry alignment and integrity", "url": "https://blog.alpsp.org/2025/03/mdpi-self-citations-study-highlights.html"}, {"title": "Title Suppressions - Journal Citation Reports - Zendesk", "url": "https://journalcitationreports.zendesk.com/hc/en-gb/articles/28351398819089-Title-Suppressions"}, {"title": "A Refresher Course on JCR Journal Suppression Policies | Clarivate", "url": "https://clarivate.com/academia-government/blog/refresher-course-jcr-journal-suppression-policies/"}, {"title": "Major indexing service sounds alarm on self-citations by nearly 50 journals – Retraction Watch", "url": "https://retractionwatch.com/2020/06/29/major-indexing-service-sounds-alarm-on-self-citations-by-nearly-50-journals/"}, {"title": "A bibliometric investigation of the journals that were repeatedly suppressed from Clarivate's Journal Citation Reports - PubMed", "url": "https://pubmed.ncbi.nlm.nih.gov/35469511/"}, {"title": "Seventeen journals lose impact factors for suspected citation manipulation – Retraction Watch", "url": "https://retractionwatch.com/2024/06/27/seventeen-journals-lose-impact-factors-for-suspected-citation-manipulation/"}, {"title": "MDPI mega-journal delisted by Clarivate / Web of Science - MARK A. HANSON LAB", "url": "https://mahansonresearch.weebly.com/blog/mdpi-mega-journal-delisted-by-clarivate-web-of-science"}]}, "Now let me search for the specific list of 33 journals suppressed in 2020.", {"tool_use_id": "srvtoolu_01NtdJmHwe1XzWRaNP7S5h3L", "content": [{"title": "Biology | Announcements", "url": "https://www.mdpi.com/journal/biology/announcements/17055"}, {"title": "Electronics | Announcements", "url": "https://www.mdpi.com/journal/electronics/announcements"}]}, "Let me search more specifically for the actual list of journals suppressed in 2020.", {"tool_use_id": "srvtoolu_01XYMs1iPRtiaaR6J99CWy2h", "content": [{"title": "Clarivate’s 2020 Journal Citation Report: “Suppressed” Journals Fight Back - Enago Academy", "url": "https://www.enago.com/academy/journals-suppressed-in-the-journal-citation-reports-fight-back/"}, {"title": "Major indexing service rejects appeals by two suppressed journals – Retraction Watch", "url": "https://retractionwatch.com/2020/08/28/major-indexing-service-rejects-appeals-by-two-suppressed-journals/"}, {"title": "Seventeen journals lose impact factors for suspected citation manipulation – Retraction Watch", "url": "https://retractionwatch.com/2024/06/27/seventeen-journals-lose-impact-factors-for-suspected-citation-manipulation/"}, {"title": "A bibliometric investigation of the journals that were repeatedly suppressed from Clarivate's Journal Citation Reports - PubMed", "url": "https://pubmed.ncbi.nlm.nih.gov/35469511/"}, {"title": "Title Suppressions - Journal Citation Reports - Zendesk", "url": "https://journalcitationreports.zendesk.com/hc/en-gb/articles/28351398819089-Title-Suppressions"}, {"title": "Title Suppressions", "url": "https://help.incites.clarivate.com/incitesLiveJCR/JCRGroup/titleSuppressions.html"}, {"title": "Ten journals denied 2020 Impact Factors because of excessive self-citation or “citation stacking”", "url": "https://retractionwatch.com/2021/06/30/ten-journals-denied-2020-impact-factors-because-of-excessive-self-citation-or-citation-stacking/"}, {"title": "Citation issues cost these 20 journals their impact factors this year – Retraction Watch", "url": "https://retractionwatch.com/2025/06/18/clarivate-impact-factor-suppression-list-2025-self-citation-stacking/"}, {"title": "“Stunned, very confused”: Two more journals push back against Impact Factor suppression", "url": "https://retractionwatch.com/2020/07/13/stunned-very-confused-two-more-journals-push-back-against-impact-factor-suppression/"}, {"title": "Journal delisted from clarivate index due to controversy", "url": "https://www.facebook.com/groups/reviewer2/posts/10163370016640469/"}]}, "Based on my web search results, I can provide you with information about the 2020 Clarivate Journal Citation Report suppressions:\n\nIn 2020, Clarivate suppressed 33 journals due to evidence of anomalous citation practices. These might include excessive self-citation and citation stacking.\n\nHowever, the search results did not contain a complete list of all 33 specific journal names that were suppressed in 2020. The search results mention specific examples of suppressed journals including:\n- Body Image, an Elsevier journal that was one of 33 suppressed by Clarivate for excessive self-citation\n- Zootaxa and the International Journal of Systematic and Evolutionary Microbiology, which successfully appealed the decision and were reinstated, while appeals by Body Image and Forensic Science International: Genetics were denied\n\nRegarding your specific mention of MDPI journals like Symmetry, Entropy, and Applied Sciences - while the search results indicate that on average, 33% of citations were intra-publisher citations—including 10% self-citations—within MDPI's journal network, the search results do not provide evidence that these particular MDPI journals were among the 33 suppressed in 2020.\n\nTo find the complete list of all 33 journals suppressed in 2020, you would need to access Clarivate's official suppression list document from that year, which appears to be available but was not fully reproduced in the search results."], "durationSeconds": 16.361970587999995, "searchCount": 5}
```

### [53] TOOL CALL — WebFetch · 2026-07-09 00:53:16 UTC

```
URL: https://www.enago.com/academy/journals-suppressed-in-the-journal-citation-reports-fight-back/
Prompt: List all specific journal names mentioned as suppressed from the 2020 JCR. Specify if each is MDPI or other publisher, and whether the reason was self-citation or stacking. Include any information about the 33 journals suppressed in 2020.
```

### [54] TOOL CALL — WebFetch · 2026-07-09 00:53:16 UTC

```
URL: https://retractionwatch.com/2020/06/29/major-indexing-service-sounds-alarm-on-self-citations-by-nearly-50-journals/
Prompt: List all specific journal names mentioned in this article about JCR 2020 suppression. List the reason for each journal's suppression (self-citation or stacking).
```

### [55] TOOL CALL — WebSearch · 2026-07-09 00:53:16 UTC

```
Retraction Watch 2019 JCR suppressed journals impact factor stacking self-citation names list 17 journals
```

### [56] TOOL CALL — WebFetch · 2026-07-09 00:53:16 UTC

```
URL: https://clarivate.com/academia-government/blog/refresher-course-jcr-journal-suppression-policies/
Prompt: List all specific journal names mentioned as suppressed from JCR by year. Indicate which were for stacking vs self-citation for each year. Include historical examples from 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025.
```

### [57] TOOL RESULT — WebFetch · 2026-07-09 00:53:18 UTC

```
{"bytes": 138502, "code": 200, "codeText": "OK", "result": "# Journals Suppressed by Clarivate (JCR 2020)\n\nBased on the article, **33 journals were suppressed** and **15 received expressions of concern**. However, the article does not provide a complete list of all journal names.\n\n## Specifically Named Suppressed Journals:\n\n1. **Journal of Environmental and Engineering Geophysics** – Self-citation (71% of citations were self-citations)\n2. **International Journal of Systematic and Evolutionary Microbiology (IJSEM)** – Self-citation (55%+ claimed by Clarivate)\n3. **Zootaxa** – Self-citation\n4. **International Journal of Medicinal Mushrooms** – Self-citation\n\n## Specifically Named Journals with Expressions of Concern:\n\n1. **Journal of Cleaner Production** – Self-citation (25% of ~47,000 references; 11,000+ self-citations)\n2. **Journal of Allergy and Clinical Immunology-In Practice** – Self-citation (one article cited same-journal papers 191 times)\n3. **JACC: Cardiovascular Imaging** – Self-citation\n4. **The Journal of the Experimental Analysis of Behavior (JEAB)** – Self-citation\n\n## Publisher Breakdown:\n- 9 Elsevier journals\n- 7 Springer Nature journals\n- 6 Taylor & Francis journals\n- 5 Wiley journals\n\n**Note:** The article states \"none of the suppressions or expressions of concern this year were for citation stacking,\" meaning all flagged journals had self-citation issues only.", "durationMs": 4987, "url": "https://retractionwatch.com/2020/06/29/major-indexing-service-sounds-alarm-on-self-citations-by-nearly-50-journals/"}
```

### [58] TOOL RESULT — WebFetch · 2026-07-09 00:53:20 UTC

```
{"bytes": 1063806, "code": 200, "codeText": "OK", "result": "# Suppressed Journals from 2020 JCR\n\nBased on the article, **only two specific journal names are identified** from the 33 suppressed journals:\n\n## Named Journals\n\n**1. Body Image**\n- **Publisher:** Elsevier\n- **Reason:** Self-citation (50.4% rate in 2019)\n- **Details:** Editors disputed the suppression, noting that the journal received \"an average of four self-citations\" per article, which they argued was reasonable given typical reference lists contain 40-60 citations.\n\n**2. International Journal of Systematic and Evolutionary Microbiology (IJSEM)**\n- **Publisher:** Microbiology Society\n- **Reason:** Self-citation\n- **Details:** Publishers argued the high self-citation rate was field-specific, as \"taxonomists\" primarily cite taxonomic literature. They contended that suppression could harm \"scientific progress in countries that place...high value on the JIF,\" particularly China.\n\n## Additional Information\n\nThe article states that 33 journals (0.27% of ~12,000 total) were suppressed in 2020, plus an additional 15 journals received \"Editorial Expression of Concern\" for abnormally high citations affecting their impact factor. However, **the article does not identify the remaining 31 suppressed journals by name**, nor does it specify MDPI as a publisher for any suppressed journals.", "durationMs": 7168, "url": "https://www.enago.com/academy/journals-suppressed-in-the-journal-citation-reports-fight-back/"}
```

### [59] TOOL RESULT — WebFetch · 2026-07-09 00:53:22 UTC

```
{"bytes": 309656, "code": 200, "codeText": "OK", "result": "# JCR Journal Suppression Information\n\nBased on the provided webpage content, **no specific journal names are listed as suppressed from JCR**, nor are any historical examples provided for the years 2018-2025.\n\nThe article explains that Clarivate makes \"no judgments about the editorial intent of published items\" and notes that \"precise thresholds are not released so as to prevent gaming.\" The document describes the *general policy* for suppression rather than documenting actual cases.\n\nThe article states: \"Journal suppression from the JCR arose from the need to protect the integrity of the Journal Impact Factor in cases where the metric is distorted by excessive self-citation or citation stacking.\"\n\nHowever, the webpage does not identify:\n- Which journals were suppressed in any specific year\n- Whether individual suppressions resulted from self-citation or citation stacking\n- Any examples from 2018-2025 or any other years\n\nTo find this information, you would need to consult the linked resources (such as the JCR suppression overview document) or access the Journal Citation Reports directly through Clarivate's platform.", "durationMs": 5927, "url": "https://clarivate.com/academia-government/blog/refresher-course-jcr-journal-suppression-policies/"}
```

### [60] TOOL RESULT — WebSearch · 2026-07-09 00:53:28 UTC

```
{"query": "Retraction Watch 2019 JCR suppressed journals impact factor stacking self-citation names list 17 journals", "results": [{"tool_use_id": "srvtoolu_01FpeJxphkQaVfF6pbKdwCvE", "content": [{"title": "Ten journals denied 2020 Impact Factors because of excessive self-citation or “citation stacking” – Retraction Watch", "url": "https://retractionwatch.com/2021/06/30/ten-journals-denied-2020-impact-factors-because-of-excessive-self-citation-or-citation-stacking/"}, {"title": "Major indexing service sounds alarm on self-citations by nearly 50 journals – Retraction Watch", "url": "https://retractionwatch.com/2020/06/29/major-indexing-service-sounds-alarm-on-self-citations-by-nearly-50-journals/"}, {"title": "Citation issues cost these 20 journals their impact factors this year – Retraction Watch", "url": "https://retractionwatch.com/2025/06/18/clarivate-impact-factor-suppression-list-2025-self-citation-stacking/"}, {"title": "Impact Factor Denied to 20 Journals For Self-Citation, Stacking - The Scholarly Kitchen", "url": "https://scholarlykitchen.sspnet.org/2018/06/27/impact-factor-denied-20-journals-self-citation-stacking/"}, {"title": "The JCR 2026 Impact Factor Release: What to Expect and ...", "url": "https://www.journalmetrics.org/blog/jcr-2026-impact-factor-release-guide"}, {"title": "Clarivate to stop counting citations to retracted articles in journals’ impact factors – Retraction Watch", "url": "https://retractionwatch.com/2025/05/15/clarivate-journal-impact-factor-retracted-articles-web-of-science/"}]}, "The search results show information about Clarivate's journal suppressions in various years (2018, 2020, 2021, 2024, 2025), but don't appear to contain a specific 2019 article matching your exact query. Let me search more specifically for the 2019 JCR suppressed journals list:", {"tool_use_id": "srvtoolu_01L773jQXuQSFfUmVBRtZWh8", "content": [{"title": "Major indexing service rejects appeals by two suppressed journals – Retraction Watch", "url": "https://retractionwatch.com/2020/08/28/major-indexing-service-rejects-appeals-by-two-suppressed-journals/"}, {"title": "Retraction Watch – Tracking retractions as a window into the scientific process", "url": "https://retractionwatch.com/"}, {"title": "Title Suppressions - Journal Citation Reports - Zendesk", "url": "https://journalcitationreports.zendesk.com/hc/en-gb/articles/28351398819089-Title-Suppressions"}, {"title": "Title Suppressions", "url": "https://help.incites.clarivate.com/incitesLiveJCR/JCRGroup/titleSuppressions.html"}, {"title": "Seventeen journals lose impact factors for suspected citation manipulation – Retraction Watch", "url": "https://retractionwatch.com/2024/06/27/seventeen-journals-lose-impact-factors-for-suspected-citation-manipulation/"}, {"title": "A bibliometric investigation of the journals that were repeatedly suppressed from Clarivate’s Journal Citation Reports: Accountability in Research: Vol 30, No 8", "url": "https://www.tandfonline.com/doi/abs/10.1080/08989621.2022.2071154"}, {"title": "Impact Factor Denied to 20 Journals For Self-Citation, Stacking - The Scholarly Kitchen", "url": "https://scholarlykitchen.sspnet.org/2018/06/27/impact-factor-denied-20-journals-self-citation-stacking/"}, {"title": "Ten journals denied 2020 Impact Factors because of excessive self-citation or “citation stacking” – Retraction Watch", "url": "https://retractionwatch.com/2021/06/30/ten-journals-denied-2020-impact-factors-because-of-excessive-self-citation-or-citation-stacking/"}, {"title": "Thomsonreuters", "url": "http://ipscience-help.thomsonreuters.com/incitesLiveJCR/JCRGroup/titleSuppressions.html"}, {"title": "JCR 2025: Excluding Retraction Citations to Reinforce Integrity", "url": "https://clarivate.com/academia-government/blog/journal-citation-reports-2025-addressing-retractions-and-strengthening-research-integrity/"}]}, "Let me search more specifically for the 2019 JCR release with the 33 journals:", {"tool_use_id": "srvtoolu_01JNznUB4NBng7y3q7xSLDRf", "content": [{"title": "Announcing the 2019 Journal Citation Reports | Clarivate", "url": "https://clarivate.com/academia-government/blog/announcing-the-2019-journal-citation-reports/"}]}, "Perfect! I found the key information. Let me search for the specific list of those 17 journals:", {"tool_use_id": "srvtoolu_01HFXUcyAWWij3MDwbP8vdhM", "content": [{"title": "Major indexing service rejects appeals by two suppressed journals – Retraction Watch", "url": "https://retractionwatch.com/2020/08/28/major-indexing-service-rejects-appeals-by-two-suppressed-journals/"}, {"title": "delisting – Retraction Watch", "url": "https://retractionwatch.com/category/by-reason-for-retraction/delisting/"}, {"title": "Seventeen journals lose impact factors for suspected citation manipulation – Retraction Watch", "url": "https://retractionwatch.com/2024/06/27/seventeen-journals-lose-impact-factors-for-suspected-citation-manipulation/"}, {"title": "Major indexing service sounds alarm on self-citations by nearly 50 journals – Retraction Watch", "url": "https://retractionwatch.com/2020/06/29/major-indexing-service-sounds-alarm-on-self-citations-by-nearly-50-journals/"}, {"title": "Citation issues cost these 20 journals their impact factors this year – Retraction Watch", "url": "https://retractionwatch.com/2025/06/18/clarivate-impact-factor-suppression-list-2025-self-citation-stacking/"}, {"title": "Ten journals denied 2020 Impact Factors because of excessive self-citation or “citation stacking” – Retraction Watch", "url": "https://retractionwatch.com/2021/06/30/ten-journals-denied-2020-impact-factors-because-of-excessive-self-citation-or-citation-stacking/"}, {"title": "Impact Factor Denied to 20 Journals For Self-Citation, Stacking - The Scholarly Kitchen", "url": "https://scholarlykitchen.sspnet.org/2018/06/27/impact-factor-denied-20-journals-self-citation-stacking/"}, {"title": "Clarivate to stop counting citations to retracted articles in journals’ impact factors – Retraction Watch", "url": "https://retractionwatch.com/2025/05/15/clarivate-journal-impact-factor-retracted-articles-web-of-science/"}]}, "Based on my web search results, I've found information about journal suppressions related to your query. Here's what I found:\n\nAfter thorough investigation of anomalous citation behavior, 17 journals were suppressed from the 2019 JCR to ensure the integrity of the data. However, the search results also indicate that Clarivate suppressed 33 journals from its Journal Citation Reports (JCR) in July, which means they will not have a 2019 Impact Factor, because of what Clarivate said was excessive self-citation. (The 17 appears to refer to the final count after some successful appeals.)\n\nThe list includes some of publishing's biggest players: Nine journals published by Elsevier, seven by Springer Nature, six by Taylor & Francis, and five by Wiley.\n\nUnfortunately, the search results I found don't contain a complete named list of all 17 (or the original 33) suppressed journal titles. While some individual journals are mentioned in the search results (such as Zootaxa, International Journal of Systematic and Evolutionary Microbiology, Body Image, and Forensic Science International: Genetics), I cannot provide you with the comprehensive list of all journal names from the available search results.\n\nTo find the complete list, you would likely need to access the official Clarivate/Journal Citation Reports documentation directly or find the specific Retraction Watch article that contained the full list."], "durationSeconds": 13.177420069000014, "searchCount": 4}
```

### [61] TOOL CALL — WebFetch · 2026-07-09 00:53:48 UTC

```
URL: https://clarivate.com/academia-government/blog/announcing-the-2019-journal-citation-reports/
Prompt: List all 17 suppressed journals from the 2019 JCR. For each, specify if the reason was self-citation or citation stacking. Are any named specifically?
```

### [62] TOOL CALL — WebSearch · 2026-07-09 00:53:48 UTC

```
2023 JCR suppressed journals stacking "Genetika" "Bioscience Research" "Bioinspired" names Clarivate impact factor
```

### [63] TOOL CALL — WebSearch · 2026-07-09 00:53:48 UTC

```
site:github.com kojaku cidre supplementary journals suppressed ground truth
```

### [64] TOOL CALL — WebFetch · 2026-07-09 00:53:48 UTC

```
URL: https://arxiv.org/abs/2503.23414
Prompt: What is this paper about? Does it apply Hodge decomposition or flow analysis to citation networks? What is the main method and findings?
```

### [65] TOOL RESULT — WebFetch · 2026-07-09 00:53:48 UTC

```
{"bytes": 309726, "code": 200, "codeText": "OK", "result": "# Summary\n\nThe webpage does not provide the detailed information you're requesting. The article states that \"17 journals were suppressed from the 2019 JCR to ensure the integrity of the data,\" but it does not:\n\n- List the names of these 17 journals\n- Specify whether suppression was due to self-citation or citation stacking\n- Provide any individual journal designations\n\nThe announcement focuses on general highlights and new features rather than the specific reasons for each journal's suppression.", "durationMs": 4300, "url": "https://clarivate.com/academia-government/blog/announcing-the-2019-journal-citation-reports/"}
```

### [66] TOOL RESULT — WebSearch · 2026-07-09 00:53:52 UTC

```
{"query": "site:github.com kojaku cidre supplementary journals suppressed ground truth", "results": [{"tool_use_id": "srvtoolu_01UZvqLoM7KCrj9H1LzsvWgz", "content": [{"title": "GitHub - skojaku/cidre: CIDRE: Detecting anomalous donors and recipients in directed weighted networks. · GitHub", "url": "https://github.com/skojaku/cidre"}, {"title": "Author Correction: Detecting anomalous citation groups in journal networks", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9424192/"}, {"title": "GitHub - Katsevich-Lab/import-schraivogel-2020 · GitHub", "url": "https://github.com/Katsevich-Lab/import-schraivogel-2020"}, {"title": "GitHub - zuruoke/watermark-removal: a machine learning image inpainting task that instinctively removes watermarks from image indistinguishable from the ground truth image · GitHub", "url": "https://github.com/zuruoke/watermark-removal"}, {"title": "GitHub - focusResearchLab/Contorter · GitHub", "url": "https://github.com/focusResearchLab/Contorter"}, {"title": "GitHub - myICOR/myPKA: AI-powered Personal Knowledge Assistance in a folder. Built on the ICOR methodology. Plain markdown. Any LLM. Yours forever. · GitHub", "url": "https://github.com/myICOR/myPKA"}, {"title": "Tortured phrases: A dubious writing style emerging in science. Evidence   of critical issues affecting established journals", "url": "https://arxiv.org/pdf/2107.06751"}, {"title": "Author Correction: An open automation system for predatory journal detection", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10167237/"}, {"title": "PubMed Journals with details · GitHub", "url": "https://gist.github.com/hasantayyar/e61a23a87d82f3550871"}, {"title": "Visibility Without Guidance: Measuring the Actionability of Public Crisis Communication in Lebanon", "url": "https://arxiv.org/pdf/2606.14714"}]}, "Based on the search results, the most relevant match is CIDRE, which is an algorithm to find anomalous groups in directed and weighted networks, with an anomalous group consisting of donor and recipient nodes connected by edges with excessive edge weights.\n\nThe GitHub repository at https://github.com/skojaku/cidre appears to be the main project by Kojaku related to detecting anomalies in networks. The algorithm is associated with research on detecting anomalous citation groups in journal networks, published as a Scientific Reports article by Kojaku, Livan, and Masuda in 2021.\n\nHowever, the search results don't contain specific information about \"supplementary journals,\" \"suppressed,\" or \"ground truth\" in relation to the CIDRE project. The search results do show that there was an Author Correction published in 2022 for the original paper on detecting anomalous citation groups in journal networks, which might be relevant to your query, but the full details are not available in these search results."], "durationSeconds": 5.264225913000002, "searchCount": 1}
```

### [67] TOOL RESULT — WebFetch · 2026-07-09 00:53:52 UTC

```
{"bytes": 41327, "code": 200, "codeText": "OK", "result": "# Paper Summary\n\nThis paper investigates AI-generated academic papers on preprint repositories and their role in citation manipulation. \n\n**Main Focus:**\nThe authors study \"clusters of questionable papers and profiles\" that exhibit \"minimal technical content, repetitive structure, unverifiable authorship, and mutually reinforcing citation patterns.\" They conducted an experiment where they generated a fake paper using GenAI, embedded citations to suspected questionable publications, and uploaded it to ResearchGate to test platform vulnerabilities.\n\n**Key Findings:**\nTheir investigation demonstrates that such papers can \"bypass platform checks, remain publicly accessible, and contribute to inflating citation metrics like the H-index and i10-index.\" The paper highlights systemic weaknesses in content moderation across academic repositories.\n\n**Methods:**\nRather than using Hodge decomposition or flow analysis on citation networks, the approach centers on empirical observation of publication patterns, controlled experimentation with artificial content generation, and analysis of citation manipulation mechanisms.\n\nThis is fundamentally a case study in academic integrity and platform accountability during the GenAI era, addressing how AI-assisted content can exploit existing institutional gaps in peer review and verification systems.", "durationMs": 5349, "url": "https://arxiv.org/abs/2503.23414"}
```

### [68] TOOL RESULT — WebSearch · 2026-07-09 00:54:00 UTC

```
{"query": "2023 JCR suppressed journals stacking \"Genetika\" \"Bioscience Research\" \"Bioinspired\" names Clarivate impact factor", "results": [{"tool_use_id": "srvtoolu_01QoUFo9bUJwf7e1KmRgjzig", "content": [{"title": "A bibliometric investigation of the journals that were repeatedly suppressed from Clarivate's Journal Citation Reports - PubMed", "url": "https://pubmed.ncbi.nlm.nih.gov/35469511/"}, {"title": "Title Suppressions - Journal Citation Reports - Zendesk", "url": "https://journalcitationreports.zendesk.com/hc/en-gb/articles/28351398819089-Title-Suppressions"}, {"title": "JCR-Impact-Factor.pdf", "url": "https://www.slideshare.net/slideshow/jcrimpactfactorpdf/261043193"}, {"title": "Title Suppressions - Journal Citation Reports - Clarivate", "url": "https://jcr.help.clarivate.com/Content/title-suppressions.htm"}, {"title": "The JCR 2026 Impact Factor Release: What to Expect and ...", "url": "https://www.journalmetrics.org/blog/jcr-2026-impact-factor-release-guide"}, {"title": "2023 – Journal Citation Reports", "url": "https://journalcitationreports.zendesk.com/hc/en-gb/articles/28351122662289-2023"}, {"title": "An In-Depth Look at Journal Impact Factors", "url": "https://openworks.mdanderson.org/cgi/viewcontent.cgi?article=1006&context=rmlnews24"}, {"title": "A Refresher Course on JCR Journal Suppression Policies | Clarivate", "url": "https://clarivate.com/academia-government/blog/refresher-course-jcr-journal-suppression-policies/"}, {"title": "Title Suppressions", "url": "https://help.incites.clarivate.com/incitesLiveJCR/JCRGroup/titleSuppressions.html"}]}, "Let me search more specifically for the journals you mentioned and the 2023 suppression data.", {"tool_use_id": "srvtoolu_015z9hkkFaHNTfNyt4HD8eyW", "content": [{"title": "Journal to retract papers that cost its impact factor and spot in leading index – Retraction Watch", "url": "https://retractionwatch.com/2023/07/17/journal-to-retract-papers-that-cost-its-impact-factor/"}, {"title": "“Truly devastating”: Four journals won’t get new Impact Factors this year because of citation shenanigans", "url": "https://retractionwatch.com/2023/06/28/truly-devastating-four-journals-wont-get-new-impact-factors-this-year-because-of-citation-shenanigans/"}, {"title": "Journal retracts 31 papers, bans authors and reviewers after losing its impact factor – Retraction Watch", "url": "https://retractionwatch.com/2023/12/12/journal-retracts-31-papers-bans-authors-and-reviewers-after-losing-its-impact-factor/"}, {"title": "Genetika-Belgrade Impact Factor IF 2024|2023|2022 - BioxBio", "url": "https://www.bioxbio.com/journal/GENETIKA-BELGRADE"}, {"title": "Title Suppressions - Journal Citation Reports Help - Clarivate", "url": "http://jcr.help.clarivate.com/Content/title-suppressions.htm?Highlight=suppress"}, {"title": "Special Issue “25 Anniversary of Bioinformatics of Genome Regulation and Structure Conference Series”", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12249764/"}, {"title": "Top 355 Nature Genetics papers published in 2023", "url": "https://scispace.com/journals/nature-genetics-3sxqwowh/2023"}, {"title": "Change in Publication Frequency in 2023", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10807439/"}, {"title": "Genetika: Impact Factor, Ranking, H-Index, ISSN, CiteScore, SJR and Other Key Journal Metrics | Researcher.Life", "url": "https://researcher.life/journal/genetika/1105"}]}, "Now let me search for more information about the specific journals suppressed in 2023 and the Bioinspired journal.", {"tool_use_id": "srvtoolu_0144jE9N4fHBiQsU8y3vVAW1", "content": [{"title": "Title Suppressions Journals Suppressed from 2023 JCR Data (2024 Release) – WoS Journals – All information you need to know", "url": "https://blog.wos-journal.info/title-suppressions-journals-suppressed-from-2023-jcr-data-2024-release/"}, {"title": "Journal Citation Reports 2023: Supporting Research Integrity | Clarivate", "url": "https://clarivate.com/academia-government/blog/unveiling-the-journal-citation-reports-2023-supporting-research-integrity-with-trusted-tools-and-data/"}, {"title": "An In-Depth Look at Journal Impact Factors", "url": "https://openworks.mdanderson.org/cgi/viewcontent.cgi?article=1006&context=rmlnews24"}, {"title": "Announcing changes to the 2023 Journal Citation Reports | Clarivate", "url": "https://clarivate.com/academia-government/blog/clarivate-announces-changes-to-the-2023-journal-citation-reports-release/"}, {"title": "2024 Journal Citation Reports Roundup | Wolters Kluwer", "url": "https://www.wolterskluwer.com/en/expert-insights/2024-journal-citation-reports-roundup"}, {"title": "Journal Citation Reports 2024: Simplifying Evaluation | Clarivate", "url": "https://clarivate.com/academia-government/blog/journal-citation-reports-2024-simplifying-journal-evaluation/"}]}, "Let me search more specifically for the 2023 suppression list and the Bioinspired journal.", {"tool_use_id": "srvtoolu_01JT5nEe8cziRJHAVqznHe7E", "content": [{"title": "A bibliometric investigation of the journals that were repeatedly suppressed from Clarivate's Journal Citation Reports - PubMed", "url": "https://pubmed.ncbi.nlm.nih.gov/35469511/"}, {"title": "“Truly devastating”: Four journals won’t get new Impact Factors this year because of citation shenanigans", "url": "https://retractionwatch.com/2023/06/28/truly-devastating-four-journals-wont-get-new-impact-factors-this-year-because-of-citation-shenanigans/"}, {"title": "A Refresher Course on JCR Journal Suppression Policies | Clarivate", "url": "https://clarivate.com/academia-government/blog/refresher-course-jcr-journal-suppression-policies/"}, {"title": "Citation issues cost these 20 journals their impact factors this year – Retraction Watch", "url": "https://retractionwatch.com/2025/06/18/clarivate-impact-factor-suppression-list-2025-self-citation-stacking/"}, {"title": "An In-Depth Look at Journal Impact Factors", "url": "https://openworks.mdanderson.org/cgi/viewcontent.cgi?article=1006&context=rmlnews24"}, {"title": "Title Suppressions - Journal Citation Reports Help - Clarivate", "url": "http://jcr.help.clarivate.com/Content/title-suppressions.htm?Highlight=suppress"}, {"title": "Title Suppressions - Journal Citation Reports - Clarivate", "url": "https://jcr.help.clarivate.com/Content/title-suppressions.htm"}, {"title": "Title Suppressions - Journal Citation Reports - Zendesk", "url": "https://journalcitationreports.zendesk.com/hc/en-gb/articles/28351398819089-Title-Suppressions"}, {"title": "Factors, components and dynamics: investigation of journal self-citation and citation by equal opportunity model", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9424957/"}, {"title": "Discontinuities in Citation Relations among Journals: Self-organized   Criticality as a Model of Scientific Revolutions and Change", "url": "https://arxiv.org/pdf/1803.00554"}]}, "Based on my search results, I can provide you with information about the 2023 JCR suppressed journals, particularly those you mentioned.\n\n## Key Findings on 2023 JCR Suppressions\n\nIn the 2023 Journal Citation Reports, Genetika, a publication of the Serbian Genetics Society, did not receive an updated impact factor due to citation stacking, a practice in which authors or journals seem to trade citations. Clarivate identified five papers published in Genetika in 2021 that had been cited by 22 papers published in the journal Bioscience Research in 2022.\n\nThe journals remained indexed in Web of Science, but didn't have an Impact Factor for that year in Clarivate's 2023 Journal Citation Reports. According to Clarivate, Marketing Theory, a SAGE title, was suppressed for self-citation. Three other journals were suppressed for citation stacking, sometimes referred to as \"citation cartels\" or \"citation rings.\"\n\nClarivate also suppressed Bioscience Research this year, meaning that the journal did not receive a new impact factor either.\n\n## Later Consequences\n\nGenetika, a publication of the Serbian Genetics Society, did not receive an updated impact factor in the year following the suppression after Clarivate identified signs of citation stacking. Clarivate also dropped Genetika from its Web of Science index for failing to meet editorial quality criteria.\n\nRegarding the \"Bioinspired\" journal you mentioned, my search results did not return specific information about a journal with that name being suppressed in 2023. If you have additional details about this journal or are referring to a journal with a different name, I would be happy to search for more specific information."], "durationSeconds": 14.507859014999994, "searchCount": 4}
```

### [69] TOOL CALL — WebFetch · 2026-07-09 00:54:26 UTC

```
URL: https://retractionwatch.com/2023/06/28/truly-devastating-four-journals-wont-get-new-impact-factors-this-year-because-of-citation-shenanigans/
Prompt: List all 4 journal names suppressed from the 2023 JCR. Specify which were for stacking vs self-citation. What specific stacking pairs were identified?
```

### [70] TOOL CALL — WebFetch · 2026-07-09 00:54:26 UTC

```
URL: https://github.com/skojaku/cidre
Prompt: List all data files in this repository. Are there any CSV files listing suppressed journals used as ground truth? What datasets are included?
```

### [71] TOOL RESULT — WebFetch · 2026-07-09 00:54:26 UTC

```
{"bytes": 156932, "code": 200, "codeText": "OK", "result": "# 2023 JCR Journal Suppressions\n\n**Four suppressed journals:**\n\n1. **Marketing Theory** (SAGE) – Self-citation\n2. **Genetika** (Serbian Genetics Society) – Citation stacking\n3. **Bioscience Research** (ISISSN) – Citation stacking\n4. **Bioinspired, Biomimetic, and Nanobiomaterials** (ICE Publishing) – Citation stacking\n\n**Stacking pairs identified:**\n\nThe article indicates that Genetika and Caryologia were affected by citations from two delisted journals, but does not explicitly name the specific stacking relationships. However, the document notes that Genetika's president disputed involvement, stating: \"Genetika did not have any kind of relationship with the journal Bioscience Research nor with authors of cited and citing papers.\"\n\nRegarding the ICE Publishing journal, an update notes it involved \"an isolated case involving a single paper in the journal\" cited by two delisted journals, though specific titles aren't identified in the provided text.", "durationMs": 4439, "url": "https://retractionwatch.com/2023/06/28/truly-devastating-four-journals-wont-get-new-impact-factors-this-year-because-of-citation-shenanigans/"}
```

### [72] TOOL RESULT — WebFetch · 2026-07-09 00:54:26 UTC

```
{"bytes": 299973, "code": 200, "codeText": "OK", "result": "# CIDRE Repository Data Files\n\nBased on the webpage content provided, I cannot identify specific CSV files or a list of suppressed journals used as ground truth. The page shows a repository structure with a `/data` folder mentioned in the directory listing, but the actual contents and filenames within that directory are not detailed in the provided content.\n\nThe webpage includes:\n- A reference to \"examples\" folder\n- A \"data\" folder in the repository structure\n- A link to an example notebook for \"step by step guideline\"\n\nHowever, the specific datasets included and whether any ground truth files exist are not described in this excerpt. To find this information, you would need to navigate directly to the `/data` folder in the GitHub repository or consult the full README documentation linked on the page.", "durationMs": 3804, "url": "https://github.com/skojaku/cidre"}
```

### [73] TOOL CALL — Bash · 2026-07-09 00:54:26 UTC

```
Get HLSAD real-world dataset details from PDF:
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://arxiv.org/pdf/2505.24534" --pattern "UCI|Senate|real.world|contact|network|dataset" -i --max-matches 20 --context-chars 600 2>&1 | grep -A5 "UCI\|Senate\|real.world\|contact" | head -100
```

### [74] TOOL RESULT — Bash · 2026-07-09 00:54:26 UTC

```
{"stdout": "Pattern: UCI|Senate|real.world|contact|network|dataset (101 matches in 64844 chars)\n\n--- Content ---\n\n1228:...s by evaluating the deviation of current spectral features from established\ntemporal patterns. In this illustrative example, HLSAD successfully detects all three artificially introduced anomalies, whereas\n--\non both synthetic and real-world datasets, we demonstrate that our\napproach outperforms existing graph methods in detecting both\nevents and change points.\nCCS Concepts\n• Mathematics of computing →Graph theory; Topology; • Com-\nputing methodologies →Anomaly detection; Temporal rea-\n--\nHigher-Order Data Many real-world datasets inherently contain\nmulti-way interactions that extend beyond dyadic relation-\nships. Traditional graph-based methods are fundamentally\nlimited in their ability to capture and analyze these higher-\norder structures. For instance, during the COVID-19 pan-\ndemic, social distancing measures disproportionately affected\n--\nour method on synthetic and real-world datasets, demonstrating its\neffectiveness for event and change point detection. Finally, Section 7\nsummarizes our findings and discusses future research directions.\n2\nRelated Work\nFollowing the taxonomy established by Ranshous et al. [29], exist-", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [75] TOOL CALL — WebFetch · 2026-07-09 00:54:26 UTC

```
URL: https://blog.wos-journal.info/title-suppressions-journals-suppressed-from-2023-jcr-data-2024-release/
Prompt: List all suppressed journals from the 2023 JCR data (2024 release). For each, specify the reason (self-citation vs stacking) and include journal names.
```

### [76] TOOL RESULT — WebFetch · 2026-07-09 00:54:26 UTC

```
{"bytes": 72466, "code": 200, "codeText": "OK", "result": "# Suppressed Journals from 2023 JCR Data (2024 Release)\n\nBased on the article, 17 journals were suppressed due to \"anomalous citation patterns\" that distorted impact metrics. Here's the complete list organized by suppression type:\n\n## Self-Citation Suppression (6 journals)\n1. Activities Adaptation & Aging\n2. Engineering Technology & Applied Science Research\n3. Exploratory Animal and Medical Research\n4. Library Hi Tech\n5. Regional Statistics\n6. SOCAR Proceedings\n\n## Citation Stacking Suppression (11 journals)\n1. Annals of Financial Economics\n2. Climate Change Economics\n3. Cuadernos de Economia\n4. Environmental Science and Pollution Research\n5. Gazzetta Medica Italiana Archivio per le Scienze Mediche\n6. Granular Computing\n7. Information Sciences\n8. Minerva Medica\n9. Panminerva Medica\n10. Resources Policy\n11. Ukrainian Journal of Physical Optics\n\nThe source notes that \"these patterns significantly distort the Journal Impact Factor,\" and Clarivate will monitor the journals for reinstatement once issues are resolved.", "durationMs": 8657, "url": "https://blog.wos-journal.info/title-suppressions-journals-suppressed-from-2023-jcr-data-2024-release/"}
```

### [77] TOOL CALL — WebFetch · 2026-07-09 00:54:52 UTC

```
URL: https://retractionwatch.com/2021/06/30/ten-journals-denied-2020-impact-factors-because-of-excessive-self-citation-or-citation-stacking/
Prompt: Extract the COMPLETE and EXACT list of all 10 journal names from this article. For each journal, give the exact suppression reason. Was it 3 or 4 stacking journals?
```

### [78] TOOL CALL — WebSearch · 2026-07-09 00:54:52 UTC

```
2019 JCR impact factor suppressed journals list stacking names "Retraction Watch" OR "Scholarly Kitchen" 2019
```

### [79] TOOL CALL — Bash · 2026-07-09 00:54:52 UTC

```
Search for complete 2018 stacking journal names:
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "2018 JCR stacking journals 'Digestive Diseases' OR 'Oncology' Liver Cancer donor recipient impact factor Clarivate" --max-results 10 2>&1
```

### [80] TOOL CALL — WebFetch · 2026-07-09 00:54:52 UTC

```
URL: https://github.com/skojaku/cidre/tree/main/data
Prompt: List all files in this data directory. Are there CSV files with journal names and suppression status? What ground truth data is available?
```

### [81] TOOL RESULT — WebFetch · 2026-07-09 00:54:52 UTC

```
{"bytes": 113808, "code": 200, "codeText": "OK", "result": "# Complete List of 10 Suppressed Journals\n\nBased on the article, here are all 10 journals denied 2020 Impact Factors:\n\n**Citation Stacking (4 journals):**\n1. Archivos Latinoamericanos de Nutrition\n2. Journal of Intelligent & Fuzzy Systems\n3. Materials Express\n4. Hellenic Journal of Cardiology\n\n**Excessive Self-Citation (6 journals):**\n5. International Journal of Engine Research\n6. Journal of Enhanced Heat Transfer\n7. Journal of Family and Economic Issues\n8. Mechanics-Based Design of Structures and Machines\n9. Journal of Biomolecular Structure and Dynamics\n10. Liquid Crystals\n\n**Note:** There were **4 stacking journals**, not 3. The article states Clarivate suppressed these journals for either \"excessive self-citation which inflates the Impact Factor, or for 'citation-stacking.'\" The article notes that citation stacking is \"sometimes referred to as taking part in 'citation cartels'\" or citation rings.", "durationMs": 3576, "url": "https://retractionwatch.com/2021/06/30/ten-journals-denied-2020-impact-factors-because-of-excessive-self-citation-or-citation-stacking/"}
```

### [82] TOOL RESULT — WebSearch · 2026-07-09 00:54:56 UTC

```
{"query": "2019 JCR impact factor suppressed journals list stacking names \"Retraction Watch\" OR \"Scholarly Kitchen\" 2019", "results": [{"tool_use_id": "srvtoolu_01WUcdQN2YGQe96N6YQnj8z8", "content": [{"title": "JCR Editorial Expression of Concern – Journal Citation Reports", "url": "https://journalcitationreports.zendesk.com/hc/en-gb/articles/28351368597521-JCR-Editorial-Expression-of-Concern"}, {"title": "Journal Citation Report 2019 update released - Research Information", "url": "https://www.researchinformation.info/news/journal-citation-report-2019-update-released/"}, {"title": "Title Suppressions", "url": "https://help.incites.clarivate.com/incitesLiveJCR/JCRGroup/titleSuppressions.html"}, {"title": "Impact Factor Denied to 20 Journals For Self-Citation, Stacking - The Scholarly Kitchen", "url": "https://scholarlykitchen.sspnet.org/2018/06/27/impact-factor-denied-20-journals-self-citation-stacking/"}, {"title": "Journal Impact Factor List 2019 - JCR, Web Of Science (PDF, XLS) - Journal Impact Factor", "url": "https://impactfactorforjournal.com/journal-impact-factor-list-2019/"}, {"title": "Ten journals denied 2020 Impact Factors because of excessive self-citation or “citation stacking”", "url": "https://retractionwatch.com/2021/06/30/ten-journals-denied-2020-impact-factors-because-of-excessive-self-citation-or-citation-stacking/"}, {"title": "“Stunned, very confused”: Two more journals push back against Impact Factor suppression", "url": "https://retractionwatch.com/2020/07/13/stunned-very-confused-two-more-journals-push-back-against-impact-factor-suppression/"}, {"title": "The Web of Science Group Releases 2019 Journal Citation Reports, Revealing the World's Most Influential Journals", "url": "https://www.prnewswire.com/news-releases/the-web-of-science-group-releases-2019-journal-citation-reports-revealing-the-worlds-most-influential-journals-300871565.html"}, {"title": "A bibliometric investigation of the journals that were repeatedly suppressed from Clarivate's Journal Citation Reports - PubMed", "url": "https://pubmed.ncbi.nlm.nih.gov/35469511/"}, {"title": "Title Suppressions - Journal Citation Reports - Zendesk", "url": "https://journalcitationreports.zendesk.com/hc/en-gb/articles/28351398819089-Title-Suppressions"}]}, "Based on the search results, I found relevant information about the 2019 JCR impact factor suppressed journals list:\n\nSeventeen journals were suppressed from the JCR in 2019 to ensure the integrity of the reports, representing 0.14% of the journals listed. The JCR monitors and excludes journals that demonstrate anomalous citation behaviour including where there is evidence of excessive journal self-citation and citation stacking.\n\nFour journals showed continuing distortion in 2018, leading to their suppression from the 2019 JCR. Additionally, three journals were suppressed from the JCR for citation stacking.\n\nI found coverage of this topic from The Scholarly Kitchen (source 4), which discussed the earlier 2018 suppressions, noting that Clarivate Analytics suppressed 20 journals in 2018, with 14 for high levels of self-citation and six for citation stacking.\n\nThe search results indicate that Retraction Watch and The Scholarly Kitchen have covered these journal suppression announcements, though the detailed lists of specific journal names were not fully displayed in the search results provided."], "durationSeconds": 6.2406652390000525, "searchCount": 1}
```

### [83] TOOL RESULT — Bash · 2026-07-09 00:54:58 UTC

```
{"stdout": "Search: 2018 JCR stacking journals 'Digestive Diseases' OR 'Oncology' Liver Cancer donor recipient impact factor Clarivate\nFound: 10 results\n\n1. Impact Factor Denied to 20 Journals For Self-Citation, Stacking\n   https://scholarlykitchen.sspnet.org/2018/06/27/impact-factor-denied-20-journals-self-citation-stacking/\n   Recipient Journal, Donor Journal, % JIF Numerator, % Exchange to ... Liver Cancer, Digestive Diseases, 40%, 95%. Liver Cancer, Oncology, 23%, 85 ......\n\n2. Liver Cancer Impact Factor 2026: 10.5, Q1 - Journal Metrics\n   https://www.journalmetrics.org/journal/liver-cancer\n   Liver Cancer's newest impact factor is 10.5, released June 17, 2026 and based on 2025 citation data. JCR Q1. APC $3590 USD. ISSN 2235-1795....\n\n3. About - Journal of Liver Cancer\n   https://www.e-jlc.org/about/about.php\n   Journal of Liver Cancer (J Liver Cancer, JLC) is the official journal of the Korean Liver Cancer Association (KLCA, https://livercancer.or.kr/eng/index.php) ......\n\n4. Insights into the history and tendency of liver transplantation for liver ...\n   https://pmc.ncbi.nlm.nih.gov/articles/PMC10793788/\n   The top 10 journals of publications on liver transplantation for liver cancer (sorted by total citations). Journal, Category, Impact factor (2022), Total ......\n\n5. About the Journal | Journal of Gastrointestinal and Liver Diseases\n   https://jgld.ro/jgld/index.php/jgld/about\n   The Journal of Gastrointestinal and Liver Diseases (JGLD) is indexed / covered by major information retrieval systems, including Clarivarte Analytics ......\n\n6. Gastroenterology & Hepatology: Journal Rankings - OOIR\n   https://ooir.org/journals.php?field=Clinical+Medicine&category=Gastroenterology+%26+Hepatology&metric=jif\n   A list of peer-reviewed journals in Gastroenterology & Hepatology, ranked by the Journal Impact Factor (2024)...\n\n7. Journal of Digestive Diseases and Hepatology - Gavin Publishers\n   https://www.gavinpublishers.com/journals/details/journal-of-digestive-diseases-and-hepatology-issn-2574-3511\n   A prestigious and cutting-edge publication dedicated to advancing the understanding and treatment of digestive diseases and hepatic disorders....\n\n8. Journal of Digestive and Liver Diseases - Directive Publications\n   https://directivepublications.org/journal-of-digestive-and-liver-diseases\n   It publishes original research, reviews, and case reports spanning the full spectrum of digestive and liver diseases, from the esophagus, stomach, and intestine ......\n\n9. Journal of Gastrointestinal Oncology: Home\n   https://jgo.amegroups.org/\n   New Impact Factor for Journal of Gastrointestinal Oncology: 2.1. We are pleased to announce that the Journal of Gastrointestinal Oncology (JGO) has attained ......\n\n10. Liver Cancer - Impact Factor, Quartile, Ranking - WoS Journal Info\n   https://wos-journal.info/journalid/15051\n   » Journals of ESCI (except for fields of Arts and Humanities) are now ranked by JIF as the same with journals of SCIE and SSCI in the release of JCR 2023 (in ......", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [84] TOOL RESULT — WebFetch · 2026-07-09 00:55:02 UTC

```
{"bytes": 226062, "code": 200, "codeText": "OK", "result": "# Files in the CIDRE Data Directory\n\nBased on the GitHub page content provided, the data directory contains two subdirectories:\n\n1. **journal-citation**\n2. **synthe**\n\n## Limitations of Available Information\n\nThe page content does not display the actual files within these directories or provide details about their contents. Specifically, I cannot confirm from this view:\n\n- Whether CSV files with journal names exist\n- What suppression status information might be available\n- Details about ground truth datasets\n\nTo access this information, you would need to navigate into each subdirectory on the GitHub repository or clone the repository locally to examine the actual file structure and contents.", "durationMs": 3778, "url": "https://github.com/skojaku/cidre/tree/main/data"}
```

### [85] ASSISTANT · 2026-07-09 00:55:56 UTC

```
Excellent data. Now let me get the complete 2018 stacking list and 2019 specific journal names.
```

### [86] TOOL CALL — Bash · 2026-07-09 00:55:56 UTC

```
Grep Scholarly Kitchen 2018 article for all stacking journal pairs:
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://scholarlykitchen.sspnet.org/2018/06/27/impact-factor-denied-20-journals-self-citation-stacking/" --pattern "stacking|donor|recipient|Liver|Digestive|Oncology|History|Economic" -i --max-matches 20 --context-chars 500 2>&1 | head -200
```

### [87] TOOL RESULT — Bash · 2026-07-09 00:55:56 UTC

```
{"stdout": "Error: HTTP 403", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [88] TOOL CALL — WebFetch · 2026-07-09 00:55:56 UTC

```
URL: https://github.com/skojaku/cidre/tree/main/data/journal-citation
Prompt: List all files in this directory. What are their names and what do they contain? Are there any files about suppressed or ground truth journals?
```

### [89] TOOL CALL — WebFetch · 2026-07-09 00:55:56 UTC

```
URL: https://www.microbiologyresearch.org/journal/ijsem/clarivate_appeal
Prompt: What year was the International Journal of Systematic and Evolutionary Microbiology suppressed from JCR? What was the reason (stacking or self-citation)? Are other suppressed journals from 2019 mentioned?
```

### [90] TOOL RESULT — WebFetch · 2026-07-09 00:55:56 UTC

```
{"bytes": 0, "code": 403, "codeText": "Forbidden", "result": "The server returned HTTP 403 Forbidden.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.", "durationMs": 277, "url": "https://www.microbiologyresearch.org/journal/ijsem/clarivate_appeal"}
```

### [91] TOOL CALL — WebSearch · 2026-07-09 00:55:56 UTC

```
"2019 Journal Citation Reports" suppressed journals stacking names list "citation stacking" 2019 JCR release
```

### [92] TOOL RESULT — WebFetch · 2026-07-09 00:55:56 UTC

```
{"bytes": 230827, "code": 200, "codeText": "OK", "result": "# Files in journal-citation Directory\n\nBased on the GitHub page, this directory contains three files:\n\n1. **community-label.csv** - Appears to contain community/cluster labels for journals\n2. **edge-table-2013.csv** - Contains citation network edge data from 2013\n3. **journal_names.csv** - Lists journal identifiers and their corresponding names\n\n## Suppressed or Ground Truth Journals\n\nNo files explicitly labeled as containing suppressed journals or ground truth data are visible in this directory listing. The page shows \"View all files\" text, suggesting additional files may exist but aren't displayed in the current view. The visible files appear focused on network structure (edges), clustering assignments (community labels), and journal identification rather than validation or exclusion criteria.", "durationMs": 3334, "url": "https://github.com/skojaku/cidre/tree/main/data/journal-citation"}
```

### [93] TOOL RESULT — WebSearch · 2026-07-09 00:56:02 UTC

```
{"query": "\"2019 Journal Citation Reports\" suppressed journals stacking names list \"citation stacking\" 2019 JCR release", "results": [{"tool_use_id": "srvtoolu_01R5fAgVcGm5vmJ3XMR9jRZA", "content": [{"title": "The Web of Science Group Releases 2019 Journal Citation Reports, Revealing the World's Most Influential Journals", "url": "https://www.prnewswire.com/news-releases/the-web-of-science-group-releases-2019-journal-citation-reports-revealing-the-worlds-most-influential-journals-300871565.html"}, {"title": "Journals removed from JCR by high levels of self-citation and by concentration of citations between journals | ResearchGate", "url": "https://www.researchgate.net/post/Journals_removed_from_JCR_by_high_levels_of_self-citation_and_by_concentration_of_citations_between_journals"}, {"title": "Title Suppressions", "url": "https://help.incites.clarivate.com/incitesLiveJCR/JCRGroup/titleSuppressions.html"}, {"title": "Clarivate’s 2020 Journal Citation Report: “Suppressed” Journals Fight Back - Enago Academy", "url": "https://www.enago.com/academy/journals-suppressed-in-the-journal-citation-reports-fight-back/"}, {"title": "Announcing the 2019 Journal Citation Reports | Clarivate", "url": "https://clarivate.com/academia-government/blog/announcing-the-2019-journal-citation-reports/"}, {"title": "Detecting anomalous citation groups in journal networks - PMC", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8282695/"}, {"title": "Detecting anomalous citation groups in journal networks | Scientific Reports", "url": "https://www.nature.com/articles/s41598-021-93572-3"}, {"title": "A bibliometric investigation of the journals that were repeatedly suppressed from Clarivate's Journal Citation Reports - PubMed", "url": "https://pubmed.ncbi.nlm.nih.gov/35469511/"}, {"title": "A Refresher Course on JCR Journal Suppression Policies | Clarivate", "url": "https://clarivate.com/academia-government/blog/refresher-course-jcr-journal-suppression-policies/"}, {"title": "Detecting anomalous citation groups in journal networks", "url": "https://arxiv.org/pdf/2009.09097"}]}, "Based on the search results, here's what I found about the 2019 Journal Citation Reports and journal suppressions:\n\n## 2019 JCR Release Overview\n\nThe Web of Science Group released the 2019 update to its annual Journal Citation Report on June 20, 2019.\n\n## Suppressed Journals for Citation Issues\n\nSeventeen journals were suppressed from the JCR in 2019 to ensure the integrity of the reports, representing 0.14% of the journals listed. The JCR monitors and excludes journals that demonstrate anomalous citation behavior including evidence of excessive journal self-citation and citation stacking.\n\n## Citation Stacking Explained\n\nJournal suppression from the JCR arose from the need to protect the integrity of the Journal Impact Factor in cases where the metric is distorted by excessive self-citation or citation stacking. The search results indicate that citation stacking refers to anomalous patterns of citation exchange between journals that artificially inflate impact factors.\n\nFor more detailed information about the specific journals that were suppressed in the 2019 JCR release, you can access the official Clarivate/Web of Science title suppressions page or the full 2019 Journal Citation Reports documentation."], "durationSeconds": 5.6755908899999925, "searchCount": 1}
```

### [94] TOOL CALL — Bash · 2026-07-09 00:56:14 UTC

```
Grep CIDRE arXiv paper for suppressed journal names used as ground truth:
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://arxiv.org/pdf/2009.09097" --pattern "suppress|stacking|JCR|impact factor|ground truth|Liver|Digestive|Oncology|History|Economic|Archivos|Intelligent|Fuzzy|Materials Express" -i --max-matches 30 --context-chars 400 2>&1 | head -300
```

### [95] TOOL RESULT — Bash · 2026-07-09 00:56:14 UTC

```
{"stdout": "URL: https://arxiv.org/pdf/2009.09097\nType: PDF\nPattern: suppress|stacking|JCR|impact factor|ground truth|Liver|Digestive|Oncology|History|Economic|Archivos|Intelligent|Fuzzy|Materials Express (63 matches in 52234 chars)\n\n--- Content ---\n\n348:Detecting anomalous citation groups in journal\nnetworks\nSadamori Kojakua, Giacomo Livanb,c, and Naoki Masudad,e,f,*\naLuddy School of Informatics, Computing, and Engineering. Indiana University, Bloomington, Indiana, 47408, USA\nbDepartment of Computer Science, University College London, London, WC1E 6EA, UK\ncSystemic Risk Centre, London School of Economics and Political Science, London, WC2A 2AE, UK\ndDepartment of Mathematics, University at Buffalo, State University of New York, Buffalo, New York, USA\neComputational and Data-Enabled Science and Engineering Program, University at Buffalo, State University of New\nYork, Buffalo, New York, 14260-2900, USA\nfFaculty of Science and Engineering, Waseda University, Tokyo, 169-8555, Japan\n*naokimas@buffalo.edu\nABSTRACT\nThe ever-increasing competitiveness in the academic publishing market incentivizes journal editors to pursue higher impact\nfactors. This translates into journals becoming more selective, and, ultimately, into higher publication standards. However,\nthe ﬁxation on higher impact factors leads some journals to artiﬁcially boost impact factors through the coordinated effort of a\n“citation cartel” of journals. “Citation cartel” behavior has become increasingly common in recent years, with several instances\nbeing reported. Here, we propose an algorithm—-named CIDRE—to detect anomalous groups of journals that exchange\ncitations at excessively high rates when compared against a null model that accounts for scientiﬁc communities and journal size.\nCIDRE detects more than half of the journals suspended from Journal Citation Reports due to anomalous citation behavior in\nthe year of suspension or in advance. Furthermore, CIDRE detects many new anomalous groups, where the impact factors of\nthe member journals are lifted substantially higher by the citations from other member journals. We describe a number of such\nexamples in detail and discuss the implications of our ﬁndings with regard to the current academic climate.\nIntroduction\nThe volume of published research is growing at exponential rates1, creating a pressing need to devise fast and fair methods to\nevaluate research outputs. Measuring academic impact is a controversial and challenging task2. Yet, the evaluation of research\nhas increasingly been operationalized in terms of the citations received by research papers and citation-based bibliometric\nindicators, such as the h-index and the journal impact factor (JIF), which are widely used to evaluate individual researchers,\nacademic institutions, and the research output of entire nations3–6.\nEditors and academic publishers are under increasing pressure to ensure that their journals achieve and sustain high values\nof JIF7 and other bibliometric indicators. Such indicators are widely recognized as proxies for a journal’s quality and prestige8,\nand have a...\n--\n3651:...ations for their journals by coercing the authors of submitted papers9 or by\nwriting editorial reviews10. Such self-citations are relatively easy to spot because they involve only one journal. Concerns have\ngrown for less detectable forms of manipulation which involve the coordinated effort of a number of journals, a practice known\nas citation cartels. Such a practice—also referred to as citation stacking—consists of groups of journals exchanging citations\nat excessively high rates11,12. For example, one instance of a citation cartel attracted attention in 2011. In this example, two\npapers published in different journals provided a number of citations to a single journal, increasing its JIF by 25%13. Since\nthen, new instances of citation stacking have been reported every year14–16.\nJournal editors may set up citation cartels by informally agreeing with other journal editors and colleagues to coerce\ncitations14,17. Such citation cartels are easy to launch and hard to detect. To tackle this issue, Journal Citation Reports (JCR),\nwhich is owned by Clarivate Analytics and was owned by Thomson Reuters until 2016, has excluded from its annual journal\nranking some pairs of journals when at least one of the two journals cited the other excessively and the journal pair satisﬁed\nsome additional criteria18. As of 2019, JCR has suspended from its annual journal ranking 46 pairs of journals—-featuring 55\njournals in total—due to excessive pairwise citations16,18. Alternatively, a previous study regarded citation cartels as groups\nof densely interconnected nodes (i.e., communities) in journal citation networks12. However, the approach based on network\narXiv:2009.09097v3  [physics.soc-ph]  15 Jul 2021\n\ncommunities may ...\n--\n6335:...model. To\nthe best of our knowledge, no empirically validated tool has been proposed for identifying groups of journals whose citation\npractices can be regarded—-with statistical conﬁdence—as anomalous.\nWe apply the algorithm to a citation network of 48,821 journals across various disciplines constructed from Microsoft\nAcademic Graph22. CIDRE detects more than half of the instances suspended from JCR in the year of suspension or earlier.\nFurthermore, CIDRE identiﬁes a number of additional anomalous journal groups, including 7 groups in 2019 whose journals\nreceived more than 30% of their incoming citations from other members of the group. In the absence of a ground truth\nvalidation—such as the one provided by comparisons against the list of journals banned in JCR—we shall refrain from\nidentifying these groups as citation cartel candidates, and it is clear that, in some cases, the anomalous citation patterns are not\na result of citation cartels. However, through extensive examples we will demonstrate that these groups are interpretable and\ncomposed of different patterns of anomalous citation behaviors.\nOur results reveal a large number of journals that receive a disproportionate amount of their citations from a tiny group\nof publication venues, which account for a substantial fraction of these journals’ impact factors (in excess of 50% in some\ncases). In our ﬁnal remarks, we will discuss how these ﬁndings should encourage a critical approach to the use of bibliometric\nindicators. The Python code for CIDRE is available at GitHub23.\nResults\nData\nWe use a snapshot of Microsoft Academic Graph (MAG) released on January 30th, 2020 to construct citation networks of\njournals22. The data set contains bibliographic inf...\n--\n12527:...f scores until no journal is further removed. We\npartition U into disjoint groups Uℓ(ℓ= 1,2,...), where each Uℓis the maximal weakly connected component in the network\nconsisting of nodes belonging to U and the residual edges. We regard each weakly connected component Uℓwith more than\nθw = 50 within-component citations as an anomalous citation group.\nOverlap with the journal groups suspended from JCR\nCIDRE detected 184 citation groups between years 2010 and 2019 (Fig. 1(a)). A detected citation group consisted of four\njournals on average (Fig. 1(b)). Because no ground truth is available for evaluating the detected groups, we compare them with\nthe journals suspended from JCR.\nSince 2007, JCR has suspended 227 journals due to excessive citations, of which 173 journals are suspended due to\nexcessive self-citations, 55 journals due to excessive citations between two journals, and one journal due to both self-citations\nand pairwise citations26. Although JCR does not disclose its precise algorithm, they have released some criteria for suspensions.\nTheir criteria include the fraction of citations that the recipient journal receives from the donor journal, akin to the recipient\nscore, together with the year since the ﬁrst publications from the journals and the ranking of journals18. JCR reported 46 pairs\nof donor and recipient journals for excessive pairwise citations. Some journal pairs suspended from JCR share a journal. We\nmerge such overlapping journal pairs suspended in year t into one group, denoted by UJCR\nℓ\n, and consider that UJCR\nℓ\nis identiﬁed\nby JCR in year t −1 (i.e., one year prior to the suspension). There are 22 such groups, which we denote by J1, J2, ..., J22.\nWe calculate the overlap between groups reported in JCR and CIDRE as O =\n\f\fUJCR TUCI\f\f\u000e\n|UCI\f\f, where UCI is a set\nof journals in a group detected by CIDRE. If UJCR and UCI have O ≥0.5 and share at least two journals, we say that UJCR\nis detected by CIDRE. CIDRE detects the 12 groups suspended from JCR at least once, of which 8 groups have O ≥0.8\n(Fig. 2(a)). CIDRE detects 10 groups earlier than JCR reports. Furthermore, CIDRE detects 7 groups for multiple years\nbefore the suspension by JCR but no group after one year from the suspension, suggesting that they stopped malicious citation\npractices after the suspension had been lifted.\nCould the above suspended groups also be detected by standard community detection algorithms? To address this question,\nwe consider three community detection algorithms, i.e., the modularity maximization by the Leiden algorithm?, Infomap21, and\nthe dcSBM...\n--\n[33 more matches not shown]", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [96] TOOL CALL — WebFetch · 2026-07-09 00:56:14 UTC

```
URL: https://www.researchgate.net/post/Journals_removed_from_JCR_by_high_levels_of_self-citation_and_by_concentration_of_citations_between_journals
Prompt: List all journal names mentioned as suppressed from JCR, including year and reason (stacking vs self-citation). Include any lists of 2019 stacking journals.
```

### [97] TOOL RESULT — WebFetch · 2026-07-09 00:56:14 UTC

```
{"bytes": 0, "code": 403, "codeText": "Forbidden", "result": "The server returned HTTP 403 Forbidden.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.", "durationMs": 272, "url": "https://www.researchgate.net/post/Journals_removed_from_JCR_by_high_levels_of_self-citation_and_by_concentration_of_citations_between_journals"}
```

### [98] TOOL CALL — WebSearch · 2026-07-09 00:56:14 UTC

```
"Archivos Latinoamericanos" OR "Journal of Intelligent Fuzzy" OR "Materials Express" 2019 stacking donor recipient JCR impact factor
```

### [99] TOOL RESULT — WebSearch · 2026-07-09 00:56:22 UTC

```
{"query": "\"Archivos Latinoamericanos\" OR \"Journal of Intelligent Fuzzy\" OR \"Materials Express\" 2019 stacking donor recipient JCR impact factor", "results": [{"tool_use_id": "srvtoolu_01MD8qmdRvnTag7h9Sa4CtgN", "content": [{"title": "international journal of fuzzy logic and intelligent systems Impact Factor, Ranking, publication fee, indexing", "url": "https://journalsearches.com/journal.php?title=international+journal+of+fuzzy+logic+and+intelligent+systems"}, {"title": "Journal of Intelligent and Fuzzy Systems Latest Journal's Impact IF 2021-2022 | Trend, Prediction, Ranking & Key Factor Analysis", "url": "https://academic-accelerator.com/Impact-of-Journal/Journal-of-Intelligent-and-Fuzzy-Systems"}, {"title": "Just-Released JCR Impact Factor Shows Strong and Steady Increase for ABC Cardiol - 1.679 - A New Historical Record", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6684181/"}, {"title": "journal of intelligent and fuzzy systems Impact Factor, Ranking, publication fee, indexing", "url": "https://journalsearches.com/journal.php?title=journal+of+intelligent+and+fuzzy+systems"}, {"title": "Journal of Intelligent and Fuzzy Systems - Impact Factor (IF), Overall Ranking, Rating, h-index, Call For Paper, Publisher, ISSN, Scientific Journal Ranking (SJR), Abbreviation, other Important Details | Resurchify", "url": "https://www.resurchify.com/impact/details/23917"}, {"title": "JOURNAL OF INTELLIGENT & FUZZY SYSTEMS - Impact Factor, Quartile, Ranking", "url": "https://wos-journal.info/journalid/20064"}, {"title": "Journal of Intelligent & Fuzzy Systems Impact Factor IF 2025|2024|2023 - BioxBio", "url": "https://www.bioxbio.com/journal/J-INTELL-FUZZY-SYST"}, {"title": "Web of Science Journal Citation Report 2020: the Brazilian contribution to the “Medicine, General & Internal” category of the journal impact factor (JIF) ranking (SCI 2019)", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9673832/"}, {"title": "The New Impact Factor of the Arquivos Brasileiros de Cardiologia (ABC Cardiol), 1.318: An Achievement of the SBC for Our Scientific Community", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6078359/"}]}, "The search results don't contain specific information about the exact combination of journals and topics you're looking for. The results show information about \"Journal of Intelligent and Fuzzy Systems\" and mention \"Arquivos Brasileiros de Cardiologia\" (which is a different journal), but they don't address the specific query about \"Archivos Latinoamericanos,\" \"Journal of Intelligent Fuzzy,\" or \"Materials Express\" with the 2019 stacking, donor-recipient, or JCR impact factor combination you mentioned.\n\nTo find more targeted information about these specific journals and their 2019 JCR impact factors, I would need to refine the search. Would you like me to search for each journal separately, or do you have more context about what specific aspect of these journals or their impact factors you're interested in?"], "durationSeconds": 9.050283055999957, "searchCount": 1}
```

### [100] ASSISTANT · 2026-07-09 00:57:08 UTC

```
Now let me get the concurrent work details and fetch the complete 2018 stacking list from web archive.
```

### [101] TOOL CALL — WebFetch · 2026-07-09 00:57:08 UTC

```
URL: https://arxiv.org/abs/2504.02767
Prompt: What is this paper about? Does it use Hodge decomposition or flow analysis on citation networks? Is it related to detecting citation manipulation or academic integrity? Summarize the main method and contribution.
```

### [102] TOOL CALL — WebSearch · 2026-07-09 00:57:08 UTC

```
circularity index citation cartel journal network detection 2024 2025 arXiv new method
```

### [103] TOOL CALL — Bash · 2026-07-09 00:57:08 UTC

```
Check web archive for Scholarly Kitchen 2018 article:
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
# Try web archive for Scholarly Kitchen article
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://web.archive.org/web/20180628120000*/https://scholarlykitchen.sspnet.org/2018/06/27/impact-factor-denied-20-journals-self-citation-stacking/" --max-chars 3000 2>&1 | head -50
```

### [104] TOOL RESULT — WebFetch · 2026-07-09 00:57:08 UTC

```
{"bytes": 43716, "code": 200, "codeText": "OK", "result": "# Paper Summary\n\n## Main Topic\nThis research investigates how Large Language Models internalize scientific literature and citation patterns, specifically examining whether LLMs align with human citation practices.\n\n## Key Methods & Findings\nThe study analyzed \"274,951 references generated by GPT-4o for 10,000 papers\" across multiple scientific domains. Rather than using Hodge decomposition or flow analysis, the authors employed comparative analysis of:\n\n- Generated vs. ground truth citations\n- Domain-specific variations in citation rates\n- Semantic alignment measurements\n- Network effects in citation patterns\n\n## Primary Contribution\nThe paper reveals that \"LLMs systematically reinforce the Matthew effect in citations by consistently favoring highly cited papers when generating references.\" This introduces potential bias into scientific discovery processes. The research shows LLMs prefer recent papers with shorter titles and fewer authors, diverging from traditional human citation patterns.\n\n## Academic Integrity Context\nWhile not explicitly about detecting manipulation, the work raises important concerns about how LLM-assisted research could inadvertently amplify established citation biases and reshape scientific knowledge discovery dynamics as these tools become more integrated into research workflows.\n\nThe study emphasizes understanding LLM influence on citation practices—a crucial consideration for scientific integrity as AI tools become more prevalent.", "durationMs": 4665, "url": "https://arxiv.org/abs/2504.02767"}
```

### [105] TOOL CALL — WebFetch · 2026-07-09 00:57:08 UTC

```
URL: https://web.archive.org/web/20180628000000/https://scholarlykitchen.sspnet.org/2018/06/27/impact-factor-denied-20-journals-self-citation-stacking/
Prompt: List all stacking journal names mentioned in this article about 2018 JCR suppressions. Specifically find the complete table of recipient and donor journals for citation stacking. List all 6 stacking journal names.
```

### [106] TOOL RESULT — WebSearch · 2026-07-09 00:57:08 UTC

```
{"query": "circularity index citation cartel journal network detection 2024 2025 arXiv new method", "results": [{"tool_use_id": "srvtoolu_01SNWSwpgaC1TRrcccQU8t4d", "content": [{"title": "(PDF) Detecting anomalous citation groups in journal networks", "url": "https://www.researchgate.net/publication/353266793_Detecting_anomalous_citation_groups_in_journal_networks"}, {"title": "From Newborn to Impact: Bias-Aware Citation Prediction", "url": "https://arxiv.org/pdf/2510.19246"}, {"title": "(PDF) Detecting citation cartels in journal networks", "url": "https://www.researchgate.net/publication/344334965_Detecting_citation_cartels_in_journal_networks"}, {"title": "Unsupervised Anomaly Detection in Journal-Level Citation Networks | Proceedings of the ACM/IEEE Joint Conference on Digital Libraries in 2020", "url": "https://dl.acm.org/doi/10.1145/3383583.3398531"}, {"title": "Detecting anomalous citation groups in journal networks - PMC", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8282695/"}, {"title": "Detecting anomalous citation groups in journal networks | Scientific Reports", "url": "https://www.nature.com/articles/s41598-021-93572-3"}, {"title": "[2009.09097] Detecting anomalous citation groups in journal networks", "url": "https://arxiv.org/abs/2009.09097"}, {"title": "[2005.14343] Unsupervised Anomaly Detection in Journal-Level Citation Networks", "url": "https://arxiv.org/abs/2005.14343"}, {"title": "Anomalous citations detection in academic networks | Artificial Intelligence Review | Springer Nature Link", "url": "https://link.springer.com/article/10.1007/s10462-023-10655-5"}]}, "Based on the search results, here's what I found regarding citation cartel detection and journal network analysis:\n\n## Key Research on Citation Cartels and Detection Methods\n\nIn citation networks, a citation cartel is manifested as a group of journals that excessively cite papers published in other journals within the group. \"Citation cartel\" behavior has become increasingly common in recent years, with several instances being reported, as some journals artificially boost impact factors through the coordinated effort of a \"citation cartel\" of journals.\n\n### CIDRE Algorithm\n\nA notable approach to detection is the CIDRE algorithm, which detects anomalous groups of journals that exchange citations at excessively high rates when compared against a null model that accounts for scientific communities and journal size. CIDRE detects more than half of the journals suspended from Journal Citation Reports due to anomalous citation behavior in the year of suspension or in advance.\n\n### Additional Detection Approaches\n\nDetecting anomalies in the citation network is a challenging task with several applications in spotting citation cartels and citation stack, and research has presented novel approaches to detect anomalies in journal-level scientific citation networks.\n\nHowever, I should note that the search results do not contain specific information about a \"circularity index\" method published in 2024-2025 on arXiv. The results primarily show research from 2020-2021 and earlier work. You may want to search directly on arXiv.org for the most recent 2024-2025 papers on this topic."], "durationSeconds": 6.009317309000005, "searchCount": 1}
```

### [107] TOOL RESULT — Bash · 2026-07-09 00:57:10 UTC

```
{"stdout": "URL: https://web.archive.org/web/20180628120000*/https://scholarlykitchen.sspnet.org/2018/06/27/impact-factor-denied-20-journals-self-citation-stacking/\nType: HTML\nLength: 10153 chars (truncated)\n\n--- Content ---\n\nKeep the news in the Wayback Machine. [Sign Fight for the Future's letter](https://www.savethearchive.com/NewsLeaders).\n\nHamburger icon An icon used to represent a menu that can be toggled by interacting with this icon.\n\n[ Internet Archive logo A line drawing of the Internet Archive headquarters building faÃ§ade. ](https://archive.org/ \"Go home\")\n\n[ Web icon An illustration of a computer application window Wayback Machine ](https://web.archive.org \"Expand web menu\") [ Texts icon An illustration of an open book.  Texts ](https://archive.org/details/texts \"Expand texts menu\") [ Video icon An illustration of two cells of a film strip. Video ](https://archive.org/details/movies \"Expand video menu\") [ Audio icon An illustration of an audio speaker.  Audio ](https://archive.org/details/audio \"Expand audio menu\") [ Software icon An illustration of a 3.5\" floppy disk. Software ](https://archive.org/details/software \"Expand software menu\") [ Images icon An illustration of two photographs.  Images ](https://archive.org/details/image \"Expand images menu\") [ Donate icon An illustration of a heart shape  Donate ](https://archive.org/donate/?origin=iawww-mbhmbgrmenu \"Expand donate menu\") [ Ellipses icon An illustration of text ellipses.  More ](https://archive.org/about/ \"Expand more menu\")\n\n[ Donate icon An illustration of a heart shape \"Donate to the archive\" ](https://archive.org/donate/?origin=iawww-mbhrt)\n\nUser icon An illustration of a person's head and chest.  [Sign up](https://archive.org/signup) | [Log in](https://archive.org/account/login)\n\n[ Upload icon An illustration of a horizontal line over an up pointing arrow. Upload ](https://archive.org/upload) Search icon An illustration of a magnifying glass.\n\n### Internet Archive Audio\n\n[Live Music Archive](https://archive.org/details/etree) [Librivox Free Audio](https://archive.org/details/librivoxaudio)\n\n#### Featured\n\n  * [All Audio](https://archive.org/details/audio)\n  * [Grateful Dead](https://archive.org/details/GratefulDead)\n  * [Netlabels](https://archive.org/details/netlabels)\n  * [Old Time Radio](https://archive.org/details/oldtimeradio)\n  * [78 RPMs and Cylinder Recordings](https://archive.org/details/78rpm)\n\n\n\n#### Top\n\n  * [Audio Books & Poetry](https://archive.org/details/audio_bookspoetry)\n  * [Computers, Technology and Science](https://archive.org/details/audio_tech)\n  * [Music, Arts & Culture](https://archive.org/details/audio_music)\n  * [News & Public Affairs](https://archive.org/details/audio_news)\n  * [Spirituality & Religion](https://archive.org/details/audio_religion)\n  * [Podcasts](https://archive.org/details/podcasts)\n  * [Radio News Archive](https://archive.org/details/radio)\n\n\n\n### Images\n\n[Metropolitan Museum](https://archive.org/details/metropolitanmuseumofart-gallery) [Cleveland Museum of Art](https://archive.org/details/clevelandart)", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [108] TOOL RESULT — WebFetch [ERROR] · 2026-07-09 00:57:10 UTC

```
Error: Claude Code is unable to fetch from web.archive.org
```

### [109] TOOL CALL — WebFetch · 2026-07-09 00:57:24 UTC

```
URL: https://arxiv.org/abs/2506.12546
Prompt: What is this CDFD paper about? What is the circularity index (CI)? What is the w = c + d decomposition? How does it compare to Hodge decomposition for detecting circular citation flows? What datasets are evaluated?
```

### [110] TOOL CALL — WebFetch · 2026-07-09 00:57:24 UTC

```
URL: https://journalcitationreports.zendesk.com/hc/en-gb/articles/28351398819089-Title-Suppressions
Prompt: List ALL suppressed journals with their year and reason (stacking vs self-citation). Include all historical lists from 2018 onwards.
```

### [111] TOOL RESULT — WebFetch · 2026-07-09 00:57:24 UTC

```
{"bytes": 0, "code": 403, "codeText": "Forbidden", "result": "The server returned HTTP 403 Forbidden.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.", "durationMs": 255, "url": "https://journalcitationreports.zendesk.com/hc/en-gb/articles/28351398819089-Title-Suppressions"}
```

### [112] TOOL CALL — WebSearch · 2026-07-09 00:57:24 UTC

```
HodgeRank citation network bibliometric anomaly academic integrity 2023 2024 arXiv journal
```

### [113] TOOL RESULT — WebFetch · 2026-07-09 00:57:26 UTC

```
{"bytes": 43730, "code": 200, "codeText": "OK", "result": "# Summary of CDFD Paper\n\n## Overview\nThis paper introduces Circular Directional Flow Decomposition (CDFD), a framework for analyzing cycles in weighted directed networks. The work separates network flow into two components to understand structural circularity.\n\n## Circularity Index (CI)\nThe paper provides \"a normalized circularity index between 0 (fully acyclic) and 1 (for networks formed solely by\" superposing cycles). This metric captures what proportion of flow participates in cyclical patterns, with complementary directionality measurement.\n\n## The w = c + d Decomposition\nThe fundamental approach divides total flow into:\n- **c**: circular (divergence-free) component\n- **d**: acyclic component carrying all net directional flow\n\nThe paper notes this decomposition is \"generally non-unique\" but the collection forms a \"well-structured geometric space with favourable topological properties.\"\n\n## Comparison to Hodge Decomposition\nThe abstract does not specifically discuss Hodge decomposition or citation flows. No such comparison appears in the provided content.\n\n## Datasets Evaluated\nThe paper mentions evaluation on \"synthetic and empirical networks\" but specific datasets are not named in the abstract or webpage content provided.\n\n**Note**: Full paper details would require accessing the complete PDF for comprehensive dataset information and technical comparisons.", "durationMs": 4713, "url": "https://arxiv.org/abs/2506.12546"}
```

### [114] TOOL RESULT — WebSearch · 2026-07-09 00:57:32 UTC

```
{"query": "HodgeRank citation network bibliometric anomaly academic integrity 2023 2024 arXiv journal", "results": [{"tool_use_id": "srvtoolu_019qRMvoRjXvfj5QFALqNfan", "content": [{"title": "Gaming the Metrics? Bibliometric Anomalies and the Integrity Crisis", "url": "https://www.biorxiv.org/content/10.1101/2025.05.09.653229v3.full.pdf"}, {"title": "Gaming the metrics: bibliometric anomalies in global university rankings and the research integrity risk index (RI2) | Scientometrics | Springer Nature Link", "url": "https://link.springer.com/article/10.1007/s11192-025-05480-2"}, {"title": "(PDF) Artificial intelligence: threat or asset to academic integrity? A bibliometric analysis", "url": "https://www.researchgate.net/publication/376852174_ARTIFICIAL_INTELLIGENCE_THREAT_OR_ASSET_TO_ACADEMIC_INTEGRITY_A_BIBLIOMETRIC_ANALYSIS"}, {"title": "Gaming the Metrics? Bibliometric Anomalies and the Integrity Crisis in Global University Rankings | bioRxiv", "url": "https://www.biorxiv.org/content/10.1101/2025.05.09.653229v3.full"}, {"title": "Gaming the Metrics? Bibliometric Anomalies and the Integrity Crisis in Global University Rankings", "url": "https://arxiv.org/pdf/2505.06448"}, {"title": "Exploring the nexus of academic integrity and artificial intelligence in higher education: a bibliometric analysis | International Journal for Educational Integrity | Springer Nature Link", "url": "https://link.springer.com/article/10.1007/s40979-025-00199-2"}, {"title": "Gaming the Metrics? Bibliometric Anomalies and the Integrity Crisis in Global University Rankings", "url": "https://www.biorxiv.org/content/10.1101/2025.05.09.653229.full.pdf"}]}, "Based on the search results, here's what I found related to bibliometric anomalies and academic integrity:\n\n## Recent Research on Bibliometric Anomalies and Academic Integrity\n\nA study investigated publication and authorship patterns among the world's 88 fastest-growing research universities across two periods (2018–2019 and 2023–2024) to assess whether rapid rank mobility coincides with bibliometric anomalies indicative of metric-driven practices.\n\nThe analysis identified 21 institutions with trajectories sharply diverging from global and regional norms, characterized by steep declines in first and corresponding authorship, disproportionate surges in STEM output, and rising numbers of hyper-prolific authors.\n\n### Citation Network Patterns\n\nStudy group universities had higher self-citation rates and frequently cited each other, forming dense internal citation networks, with the rise in highly cited articles suggesting potential citation coordination. These behaviors echo broader trends of citation cartels, coercive citations, and citation-for-sale practices that distort impact metrics.\n\n### Broader Concerns\n\nThese developments exemplify Goodhart's Law: once bibliometric measures become targets, they lose diagnostic value and invite optimization over substance. In the competitive context of rankings, when bibliometric scores determine prestige and funding, they inevitably foster strategies that privilege numerical gains over intellectual contribution.\n\nThe research appears to have been published on arXiv and bioRxiv as preprints, with a corresponding journal article in *Scientometrics* (Springer Nature). However, the search results did not return specific information about \"HodgeRank\" methodology in these studies."], "durationSeconds": 7.6696491229999815, "searchCount": 1}
```

### [115] ASSISTANT · 2026-07-09 00:58:20 UTC

```
I have sufficient information to compile the final output. Let me write the research files.
```

### [116] TOOL CALL — Bash · 2026-07-09 00:58:20 UTC

```
List workspace directory:
ls /ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/gen_art/gen_art_research_1/
```

### [117] TOOL RESULT — Bash · 2026-07-09 00:58:20 UTC

```
{"stdout": "", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [118] TOOL CALL — Write · 2026-07-09 01:00:32 UTC

```
File: /ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/gen_art/gen_art_research_1/research_out.json

{
  "answer": {
    "hlsad_summary": {
      "title": "HLSAD: Hodge Laplacian-based Simplicial Anomaly Detection",
      "authors": "Florian Frantzen and Michael T. Schaub (RWTH Aachen University)",
      "venue": "KDD '25 (ACM SIGKDD, August 3-7, 2025, Toronto, Canada)",
      "arxiv": "2505.24534",
      "doi": "10.1145/3711896.3736998",
      "hodge_laplacian_deg... [truncated, 28491 chars total]
```

### [119] TOOL RESULT — Write · 2026-07-09 01:00:32 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/gen_art/gen_art_research_1/research_out.json", "content": "{\n  \"answer\": {\n    \"hlsad_summary\": {\n      \"title\": \"HLSAD: Hodge Laplacian-based Simplicial Anomaly Detection\",\n      \"authors\": \"Florian Frantzen and Michael T. Schaub (RWTH Aachen University)\",\n      \"venue\": \"KDD '25 (ACM SIGKDD, August 3-7, 2025, Toronto, Canada)\",\n      \"arxiv\": \"2505.24... [truncated, 30633 chars total]
```

### [120] TOOL CALL — Write · 2026-07-09 01:01:44 UTC

```
File: /ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/gen_art/gen_art_research_1/research_report.md

# Research Report: HLSAD Positioning & JCR Suppression-Type Annotation

## Summary

This report provides two deliverables for the Hodge-decomposition citation cartel detection paper:
1. **HLSAD positioning**: Full technical specification for a 3-4 sentence Related Work paragraph contrasting HLSAD with the static flow decomposition approach.
2. **Suppression-type annotation**: Year-by-year enumeration of JCR-suppressed journals (2018-2025) with stacking vs. self-citation type labels, suitable for restricting the positive class in the evaluation.

---

## PART 1 — HLSAD Technical Summary

**Paper:** HLSAD: Hodge Laplacian-based Simplicial Anomaly Detection
**Authors:** Florian Frantzen, Michael T. Schaub (RWTH Aachen University)
**Venue:** KDD '25 (ACM SIGKDD Conference on Knowledge Discovery and Data Mining, August 3-7, 2025, Toronto, Canada)
**arXiv:** 2505.24534 | **DOI:** 10.1145/3711896.3736998

### Core Method

HLSAD operates on **time-evolving simplicial complexes** (sequences of graph snapshots with higher-order structures). For each snapshot t:

1. Compute Hodge Laplacians L_k up to user-specified order K (extracting both up-Laplacian L^up_k and down-Laplacian L^down_k)
2. Extract the top-ℓ singular values from each, concatenate into feature vector σ(t)
3. Maintain a context matrix C(t) of the last w snapshots; derive "typical" behavior σ̃(t) via SVD of C(t) (two windows: short-term w_s=5, long-term w_ℓ=10)
4. **Anomaly score** = angular distance between σ(t) and σ̃(t)
5. Flag as anomaly when score exceeds threshold

Complexity: O(T · Σ_k n_k² · log(ℓ))

**Primary innovation over graph-based methods:** Uses multiple Hodge Laplacians (L_1 and above, capturing edge-level and higher-order interactions) rather than only L_0 (graph Laplacian). The boundary operator B_1 is the core algebraic building block.

### Evaluation Datasets

| Dataset | Metric | HLSAD Score |
|---------|--------|-------------|
| UCI Online Message Dataset (real: UC Irvine student communication network) | Hits@10 | 1.0 (perfect) |
| US Senate co-sponsorship network (real) | Hits@2 | 1.0 (perfect) |
| Synthetic: Hybrid, Resampled, Large (10K nodes), Triangle Closing | Hits@N | Superior to LAD baseline |

### Key Distinction from This Paper

| Dimension | HLSAD | This Paper (Hodge CI Detector) |
|-----------|-------|-------------------------------|
| Data | Time-evolving simplicial complexes | Static cumulative citation flow matrix |
| Question | "When did the graph structure change?" | "Is the current flow manipulated?" |
| Operator | Multiple L_k, spectral eigenvalues tracked over time | B_1 for gradient/curl/harmonic decomposition |
| Anomaly signal | Deviation of spectral feature vector from sliding-window baseline | Curl energy fraction (algebraic signature of circular exchange) |
| Domain | General network anomaly detection | Citation integrity, journal-level |
| Ground truth | Known external events (COVID, legislative votes) | JCR suppression lists (stacking-labeled journals) |
| Temporal | Yes | No (single snapshot) |

---

## RELATED WORK PARAGRAPH (ready for insertion)

> HLSAD (Frantzen & Schaub, KDD 2025) applies the spectral properties of Hodge Laplacians of multiple orders to detect structural change-points and events in time-evolving simplicial complexes [1]. For each temporal snapshot, HLSAD extracts principal singular values from both up and down Hodge Laplacians, concatenates them into a feature vector, and flags anomalies when the angular deviation from a sliding-window SVD baseline exceeds a threshold. Our work, by contrast, applies a single-pass static Hodge–Helmholtz decomposition of a cumulative net-flow matrix on the journal citation graph, decomposing flow into orthogonal gradient (global ranking), curl (local triangular circular exchange), and harmonic (global cycle) components. The curl magnitude directly quantifies citation-ring activity against a labeled ground truth from JCR suppression lists, targeting citation integrity on static cumulative data rather than general temporal change-point detection in evolving higher-order networks.

---

## PART 2 — JCR Suppressed Journals by Year

### CRITICAL ANNOTATION RULES

- **2020 all self-citation**: CONFIRMED — none of the 33 suppressions in the 2020 JCR were for stacking [10]. Exclude from stacking-positive class entirely.
- **2019 stacking unknown**: 17 journals suppressed; specific stacking journal names not publicly documented. Mark as `type=unknown` and exclude from stacking-positive class.
- **2021 correction**: The positive stacking count is **4** (not 3 as documented in the prior dependency artifact). Hellenic Journal of Cardiology is **stacking**, not self-citation [9].
- **Oncotarget**: Self-citation removal in 2017 — predates this window; classify as self_citation if included elsewhere.
- **Bone Research**: Not suppressed — victim of stacking distortion, not a cartel member.

---

### 2025 JCR (20 journals: 4 stacking + 16 self-citation) [5]

**STACKING (use as positive class):**
1. Applied Organometallic Chemistry (Wiley)
2. Asian Journal of Agriculture and Biology
3. Chemical Methodologies
4. Genetic Resources and Crop Evolution (Springer)

**SELF-CITATION (exclude from stacking positive class):**
Advances and Applications in Discrete Mathematics, Annals of Phytomedicine-An International Journal, Clinical Hemorheology and Microcirculation, Indian Journal of Biochemistry & Biophysics, Jordan Journal of Mechanical and Industrial Engineering, Journal of Earthquake and Tsunami, Journal of Mind and Medical Sciences, Lobachevskii Journal of Mathematics, Mechanics of Advanced Materials and Structures, Media Education (Mediaobrazovanie), Punjab University Journal of Mathematics, Russian Chemical Bulletin, Russian Journal of Physical Chemistry B, TeMA-Journal of Land Use Mobility and Environment, Transactions of FAMENA, Vestnik St. Petersburg University Mathematics

---

### 2024 JCR (17 journals: 11 stacking + 6 self-citation) [6, 7]

**STACKING (11 — largest stacking cohort in documented period):**
1. Annals of Financial Economics
2. Climate Change Economics ↔ Environmental Science & Pollution Research (mutual pair)
3. Cuadernos de Economia
4. Environmental Science & Pollution Research ↔ Climate Change Economics
5. Gazzetta Medica Italiana Archivio per le Scienze Mediche
6. Granular Computing (ed: Witold Pedrycz)
7. Information Sciences (ed: Witold Pedrycz)
8. Minerva Medica
9. Panminerva Medica
10. Resources Policy (stacked with 2 small unnamed journals)
11. Ukrainian Journal of Physical Optics (received 46% citations from Optik)

**SELF-CITATION (6):**
Activities Adaptation & Aging, Engineering Technology & Applied Science Research, Exploratory Animal and Medical Research, Library Hi Tech, Regional Statistics, SOCAR Proceedings

---

### 2023 JCR (4 journals: 3 stacking + 1 self-citation) [8]

**STACKING (3):**
1. Genetika (Serbian Genetics Society) — 22 Bioscience Research papers cited Genetika in 2022
2. Bioscience Research — stacking partner with Genetika
3. Bioinspired, Biomimetic, and Nanobiomaterials (ICE Publishing) — isolated case, single paper cited by two delisted journals

**SELF-CITATION (1):**
- Marketing Theory (SAGE)

---

### 2022 JCR

No suppressions documented in any source found. Likely no suppressions occurred in 2022.

---

### 2021 JCR (10 journals: 4 stacking + 6 self-citation) [9]

**STACKING (4) — NOTE: Prior artifact said 3; confirmed 4:**
1. Archivos Latinoamericanos de Nutrition
2. Journal of Intelligent & Fuzzy Systems
3. Materials Express
4. Hellenic Journal of Cardiology ← **correction: stacking, not self-citation**

**SELF-CITATION (6):**
International Journal of Engine Research, Journal of Enhanced Heat Transfer, Journal of Family and Economic Issues, Mechanics-Based Design of Structures and Machines, Journal of Biomolecular Structure and Dynamics, Liquid Crystals

---

### 2020 JCR (33 journals: 0 stacking + 33 self-citation) [10, 11]

**STACKING: NONE — all 33 were self-citation violations.**

Named examples from secondary literature:
- Body Image (Elsevier) — 50.4% self-citation rate
- International Journal of Systematic and Evolutionary Microbiology (Microbiology Society)
- Zootaxa
- International Journal of Medicinal Mushrooms
- Journal of Environmental and Engineering Geophysics — 71% self-citation
- Forensic Science International: Genetics

Publisher breakdown: 9 Elsevier, 7 Springer Nature, 6 Taylor & Francis, 5 Wiley (remaining names not publicly reported).

---

### 2019 JCR (17 journals — breakdown unknown) [14]

**STACKING: names not found in secondary literature.** Approximately 3-4 stacking based on historical trend. 4 journals were carry-overs from 2018 distortions. Specific stacking names were not reported in any source found.

**Recommendation**: Mark all 2019 journals as `type=unknown` and exclude from validated stacking-positive class.

---

### 2018 JCR (20 journals: 6 stacking + 14 self-citation) [12]

**STACKING (5 confirmed, 1 unnamed):**
1. European Journal of the History of Economic Thought — stacking partner: Journal of the History of Economic Thought (mutual pair)
2. Journal of the History of Economic Thought — stacking partner: EJEHET (mutual pair)
3. Liver Cancer — received 40% of JIF citations from Digestive Diseases and 23% from Oncology
4. Digestive Diseases — donor to Liver Cancer
5. Oncology — donor to Liver Cancer
6. **[1 unnamed stacking journal]** — Scholarly Kitchen listed 6 but only 5 unique names confirmed from accessible text

**SELF-CITATION (14):**
Aquaculture Economics & Management, Archives of Budo, Canadian Historical Review, Chinese Journal of International Law, Chinese Journal of Mechanical Engineering, Eurasia Journal of Mathematics Science and Technology Education, International Journal of American Linguistics, International Journal of Applied Mechanics, International Journal of Civil Engineering, Journal of Micropalaeontology, Journal of Voice, Maritime Policy & Management, Pediatric Dentistry, Psychoanalytic Quarterly

---

## PART 3 — Concurrent Work Scan

### Methodologically adjacent papers (beyond HLSAD):

**CDFD: Circular Directional Flow Decomposition** [13] (arXiv:2506.12546, June 2025, Homs-Dones et al.)
- Decomposes directed weighted network flow as w = c + d (circular + acyclic)
- Circularity index CI = Σc/Σw ∈ [0,1]
- BFF algorithm (iterative sink removal, polynomial time)
- **Critical distinction vs. Hodge curl**: CDFD captures ALL circular flows (including longer cycles), while Hodge triangular curl only captures triangle-level cycles
- **Recommendation**: Compute both Hodge curl and CDFD CI on the same stacking-labeled data and compare; the paper should explicitly discuss this relationship

**CIDRE** (arXiv:2009.09097, Sci. Rep. 2021) [3, 4]
- Primary prior work in the same domain
- dcSBM null model, Poisson p-values with BH-FDR
- Detects >50% of JCR-suppressed stacking journals
- Does NOT use flow decomposition
- Uses 2013 MAG data; 22 stacking groups validated

**Unsupervised Anomaly Detection in Journal-Level Citation Networks** (arXiv:2005.14343, JCDL 2020) [16]
- Journal-level, unsupervised, no Hodge decomposition

**GLAD: Deep Graph Learning for Anomalous Citation Detection** (arXiv:2202.11360) [15]
- Paper-level (not journal-level) GNN for citation anomaly detection
- Different granularity and method

---

## Data Coverage Summary

| Year | Total | Stacking | Self-Citation | Stacking Names Status |
|------|-------|----------|---------------|----------------------|
| 2025 | 20 | 4 | 16 | All 4 confirmed |
| 2024 | 17 | 11 | 6 | All 11 confirmed |
| 2023 | 4 | 3 | 1 | All 3 confirmed |
| 2022 | 0 | 0 | 0 | N/A |
| 2021 | 10 | 4 | 6 | All 4 confirmed (correction: was 3) |
| 2020 | 33 | 0 | 33 | N/A — all self-citation |
| 2019 | 17 | ~3-4 | ~13-14 | UNKNOWN — exclude from positive class |
| 2018 | 20 | 6 | 14 | 5/6 confirmed; 1 unnamed |

**Stacking-confirmed journals suitable as positive class: 27 named (2021-2025) + 5 named from 2018 = 32 confirmed**
```

### [121] TOOL RESULT — Write · 2026-07-09 01:01:44 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/gen_art/gen_art_research_1/research_report.md", "content": "# Research Report: HLSAD Positioning & JCR Suppression-Type Annotation\n\n## Summary\n\nThis report provides two deliverables for the Hodge-decomposition citation cartel detection paper:\n1. **HLSAD positioning**: Full technical specification for a 3-4 sentence Related Work paragraph contrasting HLSAD with the static flow decomposition approach.\n2. **Suppression-type annotation**: Year-by-year enumeration of JCR-suppressed journals (2018-2025) with stacking vs. self-citation type labels, suitable for restricting the positive class in the evaluation.\n\n---\n\n## PART 1 — HLSAD Technical Summary\n\n**Paper:** HLSAD: Hodge Laplacian-based Simplicial Anomaly Detection\n**Authors:** Florian Frantzen, Michael T. Schaub (RWTH Aachen University)\n**Venue:** KDD '25 (ACM SIGKDD Conference on Knowledge Discovery and Data Mining, August 3-7, 2025, Toronto, Canada)\n**arXiv:** 2505.24534 | **DOI:** 10.1145/3711896.3736998\n\n### Core Method\n\nHLSAD operates on **time-evolving simplicial complexes** (sequences of graph snapshots with higher-order structures). For each snapshot t:\n\n1. Compute Hodge Laplacians L_k up to user-specified order K (extracting both up-Laplacian L^up_k and down-Laplacian L^down_k)\n2. Extract the top-ℓ singular values from each, concatenate into feature vector σ(t)\n3. Maintain a context matrix C(t) of the last w snapshots; derive \"typical\" behavior σ̃(t) via SVD of C(t) (two windows: short-term w_s=5, long-term w_ℓ=10)\n4. **Anomaly score** = angular distance between σ(t) and σ̃(t)\n5. Flag as anomaly when score exceeds threshold\n\nComplexity: O(T · Σ_k n_k² · log(ℓ))\n\n**Primary innovation over graph-based methods:** Uses multiple Hodge Laplacians (L_1 and above, capturing edge-level and higher-order interactions) rather than only L_0 (graph Laplacian). The boundary operator B_1 is the core algebraic building block.\n\n### Evaluation Datasets\n\n| Dataset | Metric | HLSAD Score |\n|---------|--------|-------------|\n| UCI Online Message Dataset (real: UC Irvine student communication network) | Hits@10 | 1.0 (perfect) |\n| US Senate co-sponsorship network (real) | Hits@2 | 1.0 (perfect) |\n| Synthetic: Hybrid, Resampled, Large (10K nodes), Triangle Closing | Hits@N | Superior to LAD baseline |\n\n### Key Distinction from This Paper\n\n| Dimension | HLSAD | This Paper (Hodge CI Detector) |\n|-----------|-------|-------------------------------|\n| Data | Time-evolving simplicial complexes | Static cumulative citation flow matrix |\n| Question | \"When did the graph structure change?\" | \"Is the current flow manipulated?\" |\n| Operator | Multiple L_k, spectral eigenvalues tracked over time | B_1 for gradient/curl/harmonic decomposition |\n| Anomaly signal | Deviation of spectral feature vector from sliding-window baseline | Curl energy fraction (algebraic signature of circular exchange) |\n| Domain | General network anomaly detection | Citation integrity, journal-level |\n| Ground truth | Known external events (COVID, legislative votes) | JCR suppression lists (stacking-labeled journals) |\n| Temporal | Yes | No (single snapshot) |\n\n---\n\n## RELATED WORK PARAGRAPH (ready for insertion)\n\n> HLSAD (Frantzen & Schaub, KDD 2025) applies the spectral properties of Hodge Laplacians of multiple orders to detect structural change-points and events in time-evolving simplicial complexes [1]. For each temporal snapshot, HLSAD extracts principal singular values from both up and down Hodge Laplacians, concatenates them into a feature vector, and flags anomalies when the angular deviation from a sliding-window SVD baseline exceeds a threshold. Our work, by contrast, applies a single-pass static Hodge–Helmholtz decomposition of a cumulative net-flow matrix on the journal citation graph, decomposing flow into orthogonal gradient (global ranking), curl (local triangular circular exchange), and harmonic (global cycle) components. The curl magnitude directly quantifies citation-ring activity against a labeled ground truth from JCR suppression lists, targeting citation integrity on static cumulative data rather than general temporal change-point detection in evolving higher-order networks.\n\n---\n\n## PART 2 — JCR Suppressed Journals by Year\n\n### CRITICAL ANNOTATION RULES\n\n- **2020 all self-citation**: CONFIRMED — none of the 33 suppressions in the 2020 JCR were for stacking [10]. Exclude from stacking-positive class entirely.\n- **2019 stacking unknown**: 17 journals suppressed; specific stacking journal names not publicly documented. Mark as `type=unknown` and exclude from stacking-positive class.\n- **2021 correction**: The positive stacking count is **4** (not 3 as documented in the prior dependency artifact). Hellenic Journal of Cardiology is **stacking**, not self-citation [9].\n- **Oncotarget**: Self-citation removal in 2017 — predates this window; classify as self_citation if included elsewhere.\n- **Bone Research**: Not suppressed — victim of stacking distortion, not a cartel member.\n\n---\n\n### 2025 JCR (20 journals: 4 stacking + 16 self-citation) [5]\n\n**STACKING (use as positive class):**\n1. Applied Organometallic Chemistry (Wiley)\n2. Asian Journal of Agriculture and Biology\n3. Chemical Methodologies\n4. Genetic Resources and Crop Evolution (Springer)\n\n**SELF-CITATION (exclude from stacking positive class):**\nAdvances and Applications in Discrete Mathematics, Annals of Phytomedicine-An International Journal, Clinical Hemorheology and Microcirculation, Indian Journal of Biochemistry & Biophysics, Jordan Journal of Mechanical and Industrial Engineering, Journal of Earthquake and Tsunami, Journal of Mind and Medical Sciences, Lobachevskii Journal of Mathematics, Mechanics of Advanced Materials and Structures, Media Education (Mediaobrazovanie), Punjab University Journal of Mathematics, Russian Chemical Bulletin, Russian Journal of Physical Chemistry B, TeMA-Journal of Land Use Mobility and Environment, Transactions of FAMENA, Vestnik St. Petersburg University Mathematics\n\n---\n\n### 2024 JCR (17 journals: 11 stacking + 6 self-citation) [6, 7]\n\n**STACKING (11 — largest stacking cohort in documented period):**\n1. Annals of Financial Economics\n2. Climate Change Economics ↔ Environmental Science & Pollution Research (mutual pair)\n3. Cuadernos de Economia\n4. Environmental Science & Pollution Research ↔ Climate Change Economics\n5. Gazzetta Medica Italiana Archivio per le Scienze Mediche\n6. Granular Computing (ed: Witold Pedrycz)\n7. Information Sciences (ed: Witold Pedrycz)\n8. Minerva Medica\n9. Panminerva Medica\n10. Resources Policy (stacked with 2 small unnamed journals)\n11. Ukrainian Journal of Physical Optics (received 46% citations from Optik)\n\n**SELF-CITATION (6):**\nActivities Adaptation & Aging, Engineering Technology & Applied Science Research, Exploratory Animal and Medical Research, Library Hi Tech, Regional Statistics, SOCAR Proceedings\n\n---\n\n### 2023 JCR (4 journals: 3 stacking + 1 self-citation) [8]\n\n**STACKING (3):**\n1. Genetika (Serbian Genetics Society) — 22 Bioscience Research papers cited Genetika in 2022\n2. Bioscience Research — stacking partner with Genetika\n3. Bioinspired, Biomimetic, and Nanobiomaterials (ICE Publishing) — isolated case, single paper cited by two delisted journals\n\n**SELF-CITATION (1):**\n- Marketing Theory (SAGE)\n\n---\n\n### 2022 JCR\n\nNo suppressions documented in any source found. Likely no suppressions occurred in 2022.\n\n---\n\n### 2021 JCR (10 journals: 4 stacking + 6 self-citation) [9]\n\n**STACKING (4) — NOTE: Prior artifact said 3; confirmed 4:**\n1. Archivos Latinoamericanos de Nutrition\n2. Journal of Intelligent & Fuzzy Systems\n3. Materials Express\n4. Hellenic Journal of Cardiology ← **correction: stacking, not self-citation**\n\n**SELF-CITATION (6):**\nInternational Journal of Engine Research, Journal of Enhanced Heat Transfer, Journal of Family and Economic Issues, Mechanics-Based Design of Structures and Machines, Journal of Biomolecular Structure and Dynamics, Liquid Crystals\n\n---\n\n### 2020 JCR (33 journals: 0 stacking + 33 self-citation) [10, 11]\n\n**STACKING: NONE — all 33 were self-citation violations.**\n\nNamed examples from secondary literature:\n- Body Image (Elsevier) — 50.4% self-citation rate\n- International Journal of Systematic and Evolutionary Microbiology (Microbiology Society)\n- Zootaxa\n- International Journal of Medicinal Mushrooms\n- Journal of Environmental and Engineering Geophysics — 71% self-citation\n- Forensic Science International: Genetics\n\nPublisher breakdown: 9 Elsevier, 7 Springer Nature, 6 Taylor & Francis, 5 Wiley (remaining names not publicly reported).\n\n---\n\n### 2019 JCR (17 journals — breakdown unknown) [14]\n\n**STACKING: names not found in secondary literature.** Approximately 3-4 stacking based on historical trend. 4 journals were carry-overs from 2018 distortions. Specific stacking names were not reported in any source found.\n\n**Recommendation**: Mark all 2019 journals as `type=unknown` and exclude from validated stacking-positive class.\n\n---\n\n### 2018 JCR (20 journals: 6 stacking + 14 self-citation) [12]\n\n**STACKING (5 confirmed, 1 unnamed):**\n1. European Journal of the History of Economic Thought — stacking partner: Journal of the History of Economic Thought (mutual pair)\n2. Journal of the History of Economic Thought — stacking partner: EJEHET (mutual pair)\n3. Liver Cancer — received 40% of JIF citations from Digestive Diseases and 23% from Oncology\n4. Digestive Diseases — donor to Liver Cancer\n5. Oncology — donor to Liver Cancer\n6. **[1 unnamed stacking journal]** — Scholarly Kitchen listed 6 but only 5 unique names confirmed from accessible text\n\n**SELF-CITATION (14):**\nAquaculture Economics & Management, Archives of Budo, Canadian Historical Review, Chinese Journal of International Law, Chinese Journal of Mechanical Engineering, Eurasia Journal of Mathematics Science and Technology Education, International Journal of American Linguistics, International Journal of Applied Mechanics, International Journal of Civil Engineering, Journal of Micropalaeontology, Journal of Voice, Maritime Policy & Management, Pediatric Dentistry, Psychoanalytic Quarterly\n\n---\n\n## PART 3 — Concurrent Work Scan\n\n### Methodologically adjacent papers (beyond HLSAD):\n\n**CDFD: Circular Directional Flow Decomposition** [13] (arXiv:2506.12546, June 2025, Homs-Dones et al.)\n- Decomposes directed weighted network flow as w = c + d (circular + acyclic)\n- Circularity index CI = Σc/Σw ∈ [0,1]\n- BFF algorithm (iterative sink removal, polynomial time)\n- **Critical distinction vs. Hodge curl**: CDFD captures ALL circular flows (including longer cycles), while Hodge triangular curl only captures triangle-level cycles\n- **Recommendation**: Compute both Hodge curl and CDFD CI on the same stacking-labeled data and compare; the paper should explicitly discuss this relationship\n\n**CIDRE** (arXiv:2009.09097, Sci. Rep. 2021) [3, 4]\n- Primary prior work in the same domain\n- dcSBM null model, Poisson p-values with BH-FDR\n- Detects >50% of JCR-suppressed stacking journals\n- Does NOT use flow decomposition\n- Uses 2013 MAG data; 22 stacking groups validated\n\n**Unsupervised Anomaly Detection in Journal-Level Citation Networks** (arXiv:2005.14343, JCDL 2020) [16]\n- Journal-level, unsupervised, no Hodge decomposition\n\n**GLAD: Deep Graph Learning for Anomalous Citation Detection** (arXiv:2202.11360) [15]\n- Paper-level (not journal-level) GNN for citation anomaly detection\n- Different granularity and method\n\n---\n\n## Data Coverage Summary\n\n| Year | Total | Stacking | Self-Citation | Stacking Names Status |\n|------|-------|----------|---------------|----------------------|\n| 2025 | 20 | 4 | 16 | All 4 confirmed |\n| 2024 | 17 | 11 | 6 | All 11 confirmed |\n| 2023 | 4 | 3 | 1 | All 3 confirmed |\n| 2022 | 0 | 0 | 0 | N/A |\n| 2021 | 10 | 4 | 6 | All 4 confirmed (correction: was 3) |\n| 2020 | 33 | 0 | 33 | N/A — all self-citation |\n| 2019 | 17 | ~3-4 | ~13-14 | UNKNOWN — exclude from positive class |\n| 2018 | 20 | 6 | 14 | 5/6 confirmed; 1 unnamed |\n\n**Stacking-confirmed journals suitable as positive class: 27 named (2021-2025) + 5 named from 2018 = 32 confirmed**\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [122] ASSISTANT · 2026-07-09 01:03:12 UTC

```
Now let me write the final structured output file.
```

### [123] TOOL CALL — Write · 2026-07-09 01:03:12 UTC

```
File: /ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/gen_art/gen_art_research_1/.terminal_claude_agent_struct_out.json

{
  "title": "HLSAD Positioning & JCR Suppression Annotations",
  "layman_summary": "This research provides two outputs needed for a citation cartel detector paper: an exact technical description of the only known competing method (HLSAD), showing it detects graph changes over time rather than manipulated flows in a snapshot, and a year-by-year catalog of all academic journals banned from citation rankings since 2018, labeled by whether they were caught forming citation rings (stacking) or inflating their own self-citations.",
  "summary": "This artifact delivers two critical inputs for the Hodge-decomposition citation cartel detector paper.\n\n**HLSAD (arXiv:2505.24534, KDD 2025)** is authored by Frantzen & Schaub (RWTH Aachen). It applies Hodge Laplacians of multiple orders (up to user-specified K) to time-evolving simplicial complexes. For each temporal snapshot, singular values of both up- and down-Laplacians are extracted and concatenated into a feature vector; anomalies are flagged when the angular deviation from an SVD-based sliding-window baseline exceeds a threshold. Real-world datasets: UCI Online Message Dataset (Hits@10=1.0) and US Senate co-sponsorship network (Hits@2=1.0). KEY CONTRAST: HLSAD asks 'when did the graph structure change?' (temporal change-point detection) and does not target citation networks or citation integrity. This paper asks 'is the static cumulative flow currently manipulated?' using orthogonal gradient+curl+harmonic decomposition of a fixed net-flow matrix, where curl magnitude is the direct algebraic signature of citation rings validated against JCR suppression labels.\n\nREADY-TO-USE RELATED WORK PARAGRAPH: 'HLSAD (Frantzen & Schaub, KDD 2025) applies the spectral properties of Hodge Laplacians of multiple orders to detect structural change-points and events in time-evolving simplicial complexes. For each temporal snapshot, HLSAD extracts principal singular values from both up and down Hodge Laplacians, concatenates them into a feature vector, and flags anomalies when the angular deviation from a sliding-window SVD baseline exceeds a threshold. Our work, by contrast, applies a single-pass static Hodge–Helmholtz decomposition of a cumulative net-flow matrix on the journal citation graph, decomposing flow into orthogonal gradient (global ranking), curl (local triangular circular exchange), and harmonic (global cycle) components. The curl magnitude directly quantifies citation-ring activity against a labeled ground truth from JCR suppression lists, targeting citation integrity on static cumulative data rather than general temporal change-point detection in evolving higher-order networks.'\n\n**SUPPRESSION ANNOTATION:** 32 stacking journals confirmed by name across 2018-2025 (5 from 2018, 4 from 2021—CORRECTING the prior artifact which said 3—, 3 from 2023, 11 from 2024, 4 from 2025). CRITICAL CORRECTIONS: (1) 2020 had ZERO stacking journals—all 33 suppressions were self-citation; (2) Hellenic Journal of Cardiology (2021) is STACKING, not self-citation as previously documented; (3) 2019 stacking journal names are unknown and those 17 journals must be excluded from the validated positive class. CONCURRENT WORK: CDFD (arXiv:2506.12546, June 2025) is a close concurrent paper decomposing directed flow as w=c+d with circularity index CI=Σc/Σw—captures ALL circular flow unlike Hodge curl which only catches triangular cycles. Full annotated JSON list and research report are in research_out.json and research_report.md.",
  "out_expected_files": {
    "output": "research_out.json"
  },
  "upload_ignore_regexes": [],
  "answer": "## HLSAD Technical Methodology [1, 2]\n\nHLSAD (Frantzen & Schaub, KDD '25, arXiv:2505.24534) detects anomalies in **time-evolving simplicial complexes**. The method computes Hodge Laplacians up to user-specified order K for each temporal snapshot, extracting principal singular values from both the up-Laplacian (L^up_k) and down-Laplacian (L^down_k) of each order k [2]. These singular values are concatenated into a feature vector σ(t). A sliding-window context matrix C(t) stores the last w vectors; the 'typical' feature σ̃(t) is derived via SVD of C(t). The anomaly score is the **angular deviation** between σ(t) and σ̃(t), using dual windows (w_s=5 short-term, w_ℓ=10 long-term). Computational complexity: O(T·Σ_k n_k² log ℓ) [2]. Real-world validation: UCI Online Message Dataset (Hits@10=1.0) and US Senate co-sponsorship network (Hits@2=1.0) [2].\n\n**KEY DISTINCTION**: HLSAD is temporal (change-point detection in evolving graphs) and does not target citation networks or use labeled ground truth. This paper uses static flow decomposition (gradient + curl + harmonic) on a fixed net-flow matrix, where the curl component directly quantifies citation-ring manipulation against JCR suppression ground truth [1, 2].\n\n## Related Work Paragraph\n\n'HLSAD (Frantzen & Schaub, KDD 2025) applies the spectral properties of Hodge Laplacians of multiple orders to detect structural change-points and events in time-evolving simplicial complexes [1]. For each temporal snapshot, HLSAD extracts principal singular values from both up and down Hodge Laplacians, concatenates them into a feature vector, and flags anomalies when the angular deviation from a sliding-window SVD baseline exceeds a threshold. Our work, by contrast, applies a single-pass static Hodge–Helmholtz decomposition of a cumulative net-flow matrix on the journal citation graph, decomposing flow into orthogonal gradient (global ranking), curl (local triangular circular exchange), and harmonic (global cycle) components. The curl magnitude directly quantifies citation-ring activity against a labeled ground truth from JCR suppression lists, targeting citation integrity on static cumulative data rather than general temporal change-point detection in evolving higher-order networks.'\n\n## JCR Suppression-Type Annotations (2018-2025)\n\n### CRITICAL CORRECTIONS vs. Prior Artifact\n- **2021 stacking = 4, NOT 3**: Hellenic Journal of Cardiology is **stacking** (not self-citation as documented in prior artifact) [9]\n- **2020 = ZERO stacking**: All 33 suppressions in 2020 JCR were self-citation violations; none were stacking [10, 11]\n- **2019 stacking names unknown**: Must be excluded from validated positive class [14]\n\n### Confirmed Stacking Journals (suitable as positive class)\n\n**2025 (4 stacking)** [5]: Applied Organometallic Chemistry, Asian Journal of Agriculture and Biology, Chemical Methodologies, Genetic Resources and Crop Evolution\n\n**2024 (11 stacking)** [6, 7]: Annals of Financial Economics, Climate Change Economics, Cuadernos de Economia, Environmental Science & Pollution Research, Gazzetta Medica Italiana Archivio per le Scienze Mediche, Granular Computing, Information Sciences, Minerva Medica, Panminerva Medica, Resources Policy, Ukrainian Journal of Physical Optics\n\n**2023 (3 stacking)** [8]: Genetika, Bioscience Research, Bioinspired Biomimetic and Nanobiomaterials\n\n**2021 (4 stacking — CORRECTED)** [9]: Archivos Latinoamericanos de Nutrition, Journal of Intelligent & Fuzzy Systems, Materials Express, Hellenic Journal of Cardiology\n\n**2020 (0 stacking)** [10]: Excluded entirely — all 33 suppressions were self-citation\n\n**2019 (unknown)** [14]: 17 journals suppressed; stacking names not found in secondary literature; exclude from positive class\n\n**2018 (5/6 stacking confirmed, 1 unnamed)** [12]: European Journal of the History of Economic Thought, Journal of the History of Economic Thought, Liver Cancer, Digestive Diseases (donor to Liver Cancer), Oncology (donor to Liver Cancer), [1 unnamed]\n\nTotal confirmed stacking journals by name: **32** (2018-2025, excluding 1 unnamed 2018 journal and the unknown 2019 journals)\n\n## Concurrent Works\n\n**CDFD** (arXiv:2506.12546, June 2025) [13] is a close concurrent paper: decomposes directed flow as w=c+d (circular + acyclic), defines CI=Σc/Σw in [0,1]. Captures ALL circular flows including longer cycles beyond triangles, unlike Hodge curl which only captures triangular cycles. Should be cited and compared explicitly.\n\n**CIDRE** (arXiv:2009.09097, Sci. Rep. 2021) [3, 4] is the primary prior work in this domain: dcSBM null model, Poisson p-values with BH-FDR; detects >50% of JCR-suppressed stacking journals; validated on 2013 MAG data. Methodologically distinct (statistical community anomaly vs. algebraic flow decomposition).\n\n**GLAD** (arXiv:2202.11360) [15] and **Unsupervised JACL 2020** (arXiv:2005.14343) [16] are related but less overlapping (paper-level / unsupervised without JCR ground truth).",
  "sources": [
    {
      "index": 1,
      "url": "https://arxiv.org/abs/2505.24534",
      "title": "HLSAD: Hodge Laplacian-based Simplicial Anomaly Detection (abstract page)",
      "summary": "Confirmed temporal nature, higher-order simplicial complex focus, KDD 2025 venue, abstract text"
    },
    {
      "index": 2,
      "url": "https://arxiv.org/pdf/2505.24534",
      "title": "HLSAD full PDF",
      "summary": "Complete methodology: multi-order Hodge Laplacians, SVD-based sliding window anomaly score with angular deviation, UCI and Senate datasets (both Hits@N=1.0), boundary operator B1 shown explicitly, dual window parameters w_s=5 / w_l=10, computational complexity formula"
    },
    {
      "index": 3,
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8282695/",
      "title": "CIDRE: Detecting anomalous citation groups (PMC full text)",
      "summary": "Case study journal groups 1-14; note 46 stacking pairs / 55 journals total suppressed by JCR up to 2019; 22 merged stacking groups J1-J22"
    },
    {
      "index": 4,
      "url": "https://arxiv.org/pdf/2009.09097",
      "title": "CIDRE arXiv PDF",
      "summary": "Since 2007: 227 total JCR suppressions (173 self-citation, 55 stacking, 1 both); CIDRE detects 12 of 22 stacking groups; uses 2013 MAG data with 48,821 journals"
    },
    {
      "index": 5,
      "url": "https://retractionwatch.com/2025/06/18/clarivate-impact-factor-suppression-list-2025-self-citation-stacking/",
      "title": "Retraction Watch: 2025 JCR suppression list (20 journals)",
      "summary": "Complete 2025 list: 4 stacking + 16 self-citation. Named all 4 stacking journals."
    },
    {
      "index": 6,
      "url": "https://blog.wos-journal.info/title-suppressions-journals-suppressed-from-2023-jcr-data-2024-release/",
      "title": "WoS Journal blog: 2024 JCR suppression list (17 journals)",
      "summary": "Complete 2024 list: 11 stacking + 6 self-citation. All 11 stacking journal names confirmed."
    },
    {
      "index": 7,
      "url": "https://retractionwatch.com/2024/06/27/seventeen-journals-lose-impact-factors-for-suspected-citation-manipulation/",
      "title": "Retraction Watch: 2024 JCR suppression article",
      "summary": "Confirmed Ukrainian Journal of Physical Optics (46% citations from Optik), Granular Computing / Information Sciences (Pedrycz), Resources Policy stacking pair details"
    },
    {
      "index": 8,
      "url": "https://retractionwatch.com/2023/06/28/truly-devastating-four-journals-wont-get-new-impact-factors-this-year-because-of-citation-shenanigans/",
      "title": "Retraction Watch: 2023 JCR suppression (4 journals)",
      "summary": "Complete 2023 list: Marketing Theory (self-citation), Genetika + Bioscience Research + Bioinspired Biomimetic and Nanobiomaterials (stacking). Confirmed Genetika disputed the relationship."
    },
    {
      "index": 9,
      "url": "https://retractionwatch.com/2021/06/30/ten-journals-denied-2020-impact-factors-because-of-excessive-self-citation-or-citation-stacking/",
      "title": "Retraction Watch: 2021 JCR suppression (10 journals)",
      "summary": "Complete 2021 list: 4 stacking (Archivos Latinoamericanos, J Intelligent & Fuzzy Systems, Materials Express, Hellenic Journal of Cardiology) + 6 self-citation. Corrects prior artifact's claim of 3 stacking."
    },
    {
      "index": 10,
      "url": "https://retractionwatch.com/2020/06/29/major-indexing-service-sounds-alarm-on-self-citations-by-nearly-50-journals/",
      "title": "Retraction Watch: 2020 JCR suppression (33 journals)",
      "summary": "CONFIRMED: zero stacking in 2020 — all 33 suppressions were self-citation. Named: IJSEM, Zootaxa, Body Image, International Journal of Medicinal Mushrooms, Journal of Environmental and Engineering Geophysics, Forensic Science International: Genetics."
    },
    {
      "index": 11,
      "url": "https://www.enago.com/academy/journals-suppressed-in-the-journal-citation-reports-fight-back/",
      "title": "Enago Academy: 2020 JCR suppression details",
      "summary": "Publisher breakdown: 9 Elsevier, 7 Springer Nature, 6 Taylor & Francis, 5 Wiley. Body Image (50.4% self-citation), IJSEM details."
    },
    {
      "index": 12,
      "url": "https://scholarlykitchen.sspnet.org/2018/06/27/impact-factor-denied-20-journals-self-citation-stacking/",
      "title": "Scholarly Kitchen: 2018 JCR suppression (20 journals)",
      "summary": "Complete 2018 list: 14 self-citation + 6 stacking. Stacking table: Liver Cancer/Digestive Diseases (40%), Liver Cancer/Oncology (23%), EJEHT/JHET mutual pair. 6th stacking journal not named in accessible text (site 403)."
    },
    {
      "index": 13,
      "url": "https://arxiv.org/abs/2506.12546",
      "title": "CDFD: Circular Directional Flow Decomposition (Homs-Dones et al., 2025)",
      "summary": "Concurrent work: w=c+d decomposition; CI=Σc/Σw in [0,1]; BFF algorithm; captures ALL circular flows beyond triangles — methodologically complementary to Hodge curl"
    },
    {
      "index": 14,
      "url": "https://clarivate.com/academia-government/blog/announcing-the-2019-journal-citation-reports/",
      "title": "Clarivate: 2019 JCR announcement",
      "summary": "17 journals suppressed; no specific names or stacking vs. self-citation breakdown provided"
    },
    {
      "index": 15,
      "url": "https://arxiv.org/abs/2202.11360",
      "title": "GLAD: Deep Graph Learning for Anomalous Citation Detection",
      "summary": "GNN-based paper-level citation anomaly detection with CPU algorithm; different granularity and method from journal-level flow decomposition"
    },
    {
      "index": 16,
      "url": "https://arxiv.org/abs/2005.14343",
      "title": "Unsupervised Anomaly Detection in Journal-Level Citation Networks (JCDL 2020)",
      "summary": "Unsupervised journal-level citation anomaly detection; no Hodge decomposition; earlier related work"
    }
  ],
  "follow_up_questions": [
    "Can the CIDRE edge-table-2013.csv and journal_names.csv files be cross-referenced with OpenAlex journal IDs to map which confirmed stacking journals from 2018-2025 were already visible as anomalous in the 2013 MAG snapshot? This would establish whether the Hodge curl signal is detectable in pre-suppression data, strengthening the paper's claim of predictive value.",
    "For the 2019 JCR suppressed journals (17 total, stacking names unknown): the CIDRE paper (arXiv:2009.09097) references 46 donor-recipient stacking pairs up to 2019 and 22 merged groups (J1-J22). Are the specific journal names in those groups available in the CIDRE GitHub repository's data files or supplementary materials, which could resolve the 2019 stacking journal identification gap?",
    "The CDFD paper (arXiv:2506.12546) captures ALL circular flows including cycles longer than triangles, while HodgeRank curl is restricted to triangular cycles. For the citation cartel detection experiment, should the experiment compute both metrics on the same stacking-labeled journal set to empirically determine whether the longer-cycle circular flows are more discriminative than the triangular Hodge curl—and should CDFD's CI be presented as a complementary or competing method?"
  ]
}
```

### [124] TOOL RESULT — Write · 2026-07-09 01:03:12 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/gen_art/gen_art_research_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"HLSAD Positioning & JCR Suppression Annotations\",\n  \"layman_summary\": \"This research provides two outputs needed for a citation cartel detector paper: an exact technical description of the only known competing method (HLSAD), showing it detects graph changes over time rather than manipulated flows in a snapshot, and a year-by-year catalog of all academic journals banned from citation rankings since 2018, labeled by whether they were caught forming citation rings (stacking) or inflating their own self-citations.\",\n  \"summary\": \"This artifact delivers two critical inputs for the Hodge-decomposition citation cartel detector paper.\\n\\n**HLSAD (arXiv:2505.24534, KDD 2025)** is authored by Frantzen & Schaub (RWTH Aachen). It applies Hodge Laplacians of multiple orders (up to user-specified K) to time-evolving simplicial complexes. For each temporal snapshot, singular values of both up- and down-Laplacians are extracted and concatenated into a feature vector; anomalies are flagged when the angular deviation from an SVD-based sliding-window baseline exceeds a threshold. Real-world datasets: UCI Online Message Dataset (Hits@10=1.0) and US Senate co-sponsorship network (Hits@2=1.0). KEY CONTRAST: HLSAD asks 'when did the graph structure change?' (temporal change-point detection) and does not target citation networks or citation integrity. This paper asks 'is the static cumulative flow currently manipulated?' using orthogonal gradient+curl+harmonic decomposition of a fixed net-flow matrix, where curl magnitude is the direct algebraic signature of citation rings validated against JCR suppression labels.\\n\\nREADY-TO-USE RELATED WORK PARAGRAPH: 'HLSAD (Frantzen & Schaub, KDD 2025) applies the spectral properties of Hodge Laplacians of multiple orders to detect structural change-points and events in time-evolving simplicial complexes. For each temporal snapshot, HLSAD extracts principal singular values from both up and down Hodge Laplacians, concatenates them into a feature vector, and flags anomalies when the angular deviation from a sliding-window SVD baseline exceeds a threshold. Our work, by contrast, applies a single-pass static Hodge–Helmholtz decomposition of a cumulative net-flow matrix on the journal citation graph, decomposing flow into orthogonal gradient (global ranking), curl (local triangular circular exchange), and harmonic (global cycle) components. The curl magnitude directly quantifies citation-ring activity against a labeled ground truth from JCR suppression lists, targeting citation integrity on static cumulative data rather than general temporal change-point detection in evolving higher-order networks.'\\n\\n**SUPPRESSION ANNOTATION:** 32 stacking journals confirmed by name across 2018-2025 (5 from 2018, 4 from 2021—CORRECTING the prior artifact which said 3—, 3 from 2023, 11 from 2024, 4 from 2025). CRITICAL CORRECTIONS: (1) 2020 had ZERO stacking journals—all 33 suppressions were self-citation; (2) Hellenic Journal of Cardiology (2021) is STACKING, not self-citation as previously documented; (3) 2019 stacking journal names are unknown and those 17 journals must be excluded from the validated positive class. CONCURRENT WORK: CDFD (arXiv:2506.12546, June 2025) is a close concurrent paper decomposing directed flow as w=c+d with circularity index CI=Σc/Σw—captures ALL circular flow unlike Hodge curl which only catches triangular cycles. Full annotated JSON list and research report are in research_out.json and research_report.md.\",\n  \"out_expected_files\": {\n    \"output\": \"research_out.json\"\n  },\n  \"upload_ignore_regexes\": [],\n  \"answer\": \"## HLSAD Technical Methodology [1, 2]\\n\\nHLSAD (Frantzen & Schaub, KDD '25, arXiv:2505.24534) detects anomalies in **time-evolving simplicial complexes**. The method computes Hodge Laplacians up to user-specified order K for each temporal snapshot, extracting principal singular values from both the up-Laplacian (L^up_k) and down-Laplacian (L^down_k) of each order k [2]. These singular values are concatenated into a feature vector σ(t). A sliding-window context matrix C(t) stores the last w vectors; the 'typical' feature σ̃(t) is derived via SVD of C(t). The anomaly score is the **angular deviation** between σ(t) and σ̃(t), using dual windows (w_s=5 short-term, w_ℓ=10 long-term). Computational complexity: O(T·Σ_k n_k² log ℓ) [2]. Real-world validation: UCI Online Message Dataset (Hits@10=1.0) and US Senate co-sponsorship network (Hits@2=1.0) [2].\\n\\n**KEY DISTINCTION**: HLSAD is temporal (change-point detection in evolving graphs) and does not target citation networks or use labeled ground truth. This paper uses static flow decomposition (gradient + curl + harmonic) on a fixed net-flow matrix, where the curl component directly quantifies citation-ring manipulation against JCR suppression ground truth [1, 2].\\n\\n## Related Work Paragraph\\n\\n'HLSAD (Frantzen & Schaub, KDD 2025) applies the spectral properties of Hodge Laplacians of multiple orders to detect structural change-points and events in time-evolving simplicial complexes [1]. For each temporal snapshot, HLSAD extracts principal singular values from both up and down Hodge Laplacians, concatenates them into a feature vector, and flags anomalies when the angular deviation from a sliding-window SVD baseline exceeds a threshold. Our work, by contrast, applies a single-pass static Hodge–Helmholtz decomposition of a cumulative net-flow matrix on the journal citation graph, decomposing flow into orthogonal gradient (global ranking), curl (local triangular circular exchange), and harmonic (global cycle) components. The curl magnitude directly quantifies citation-ring activity against a labeled ground truth from JCR suppression lists, targeting citation integrity on static cumulative data rather than general temporal change-point detection in evolving higher-order networks.'\\n\\n## JCR Suppression-Type Annotations (2018-2025)\\n\\n### CRITICAL CORRECTIONS vs. Prior Artifact\\n- **2021 stacking = 4, NOT 3**: Hellenic Journal of Cardiology is **stacking** (not self-citation as documented in prior artifact) [9]\\n- **2020 = ZERO stacking**: All 33 suppressions in 2020 JCR were self-citation violations; none were stacking [10, 11]\\n- **2019 stacking names unknown**: Must be excluded from validated positive class [14]\\n\\n### Confirmed Stacking Journals (suitable as positive class)\\n\\n**2025 (4 stacking)** [5]: Applied Organometallic Chemistry, Asian Journal of Agriculture and Biology, Chemical Methodologies, Genetic Resources and Crop Evolution\\n\\n**2024 (11 stacking)** [6, 7]: Annals of Financial Economics, Climate Change Economics, Cuadernos de Economia, Environmental Science & Pollution Research, Gazzetta Medica Italiana Archivio per le Scienze Mediche, Granular Computing, Information Sciences, Minerva Medica, Panminerva Medica, Resources Policy, Ukrainian Journal of Physical Optics\\n\\n**2023 (3 stacking)** [8]: Genetika, Bioscience Research, Bioinspired Biomimetic and Nanobiomaterials\\n\\n**2021 (4 stacking — CORRECTED)** [9]: Archivos Latinoamericanos de Nutrition, Journal of Intelligent & Fuzzy Systems, Materials Express, Hellenic Journal of Cardiology\\n\\n**2020 (0 stacking)** [10]: Excluded entirely — all 33 suppressions were self-citation\\n\\n**2019 (unknown)** [14]: 17 journals suppressed; stacking names not found in secondary literature; exclude from positive class\\n\\n**2018 (5/6 stacking confirmed, 1 unnamed)** [12]: European Journal of the History of Economic Thought, Journal of the History of Economic Thought, Liver Cancer, Digestive Diseases (donor to Liver Cancer), Oncology (donor to Liver Cancer), [1 unnamed]\\n\\nTotal confirmed stacking journals by name: **32** (2018-2025, excluding 1 unnamed 2018 journal and the unknown 2019 journals)\\n\\n## Concurrent Works\\n\\n**CDFD** (arXiv:2506.12546, June 2025) [13] is a close concurrent paper: decomposes directed flow as w=c+d (circular + acyclic), defines CI=Σc/Σw in [0,1]. Captures ALL circular flows including longer cycles beyond triangles, unlike Hodge curl which only captures triangular cycles. Should be cited and compared explicitly.\\n\\n**CIDRE** (arXiv:2009.09097, Sci. Rep. 2021) [3, 4] is the primary prior work in this domain: dcSBM null model, Poisson p-values with BH-FDR; detects >50% of JCR-suppressed stacking journals; validated on 2013 MAG data. Methodologically distinct (statistical community anomaly vs. algebraic flow decomposition).\\n\\n**GLAD** (arXiv:2202.11360) [15] and **Unsupervised JACL 2020** (arXiv:2005.14343) [16] are related but less overlapping (paper-level / unsupervised without JCR ground truth).\",\n  \"sources\": [\n    {\n      \"index\": 1,\n      \"url\": \"https://arxiv.org/abs/2505.24534\",\n      \"title\": \"HLSAD: Hodge Laplacian-based Simplicial Anomaly Detection (abstract page)\",\n      \"summary\": \"Confirmed temporal nature, higher-order simplicial complex focus, KDD 2025 venue, abstract text\"\n    },\n    {\n      \"index\": 2,\n      \"url\": \"https://arxiv.org/pdf/2505.24534\",\n      \"title\": \"HLSAD full PDF\",\n      \"summary\": \"Complete methodology: multi-order Hodge Laplacians, SVD-based sliding window anomaly score with angular deviation, UCI and Senate datasets (both Hits@N=1.0), boundary operator B1 shown explicitly, dual window parameters w_s=5 / w_l=10, computational complexity formula\"\n    },\n    {\n      \"index\": 3,\n      \"url\": \"https://pmc.ncbi.nlm.nih.gov/articles/PMC8282695/\",\n      \"title\": \"CIDRE: Detecting anomalous citation groups (PMC full text)\",\n      \"summary\": \"Case study journal groups 1-14; note 46 stacking pairs / 55 journals total suppressed by JCR up to 2019; 22 merged stacking groups J1-J22\"\n    },\n    {\n      \"index\": 4,\n      \"url\": \"https://arxiv.org/pdf/2009.09097\",\n      \"title\": \"CIDRE arXiv PDF\",\n      \"summary\": \"Since 2007: 227 total JCR suppressions (173 self-citation, 55 stacking, 1 both); CIDRE detects 12 of 22 stacking groups; uses 2013 MAG data with 48,821 journals\"\n    },\n    {\n      \"index\": 5,\n      \"url\": \"https://retractionwatch.com/2025/06/18/clarivate-impact-factor-suppression-list-2025-self-citation-stacking/\",\n      \"title\": \"Retraction Watch: 2025 JCR suppression list (20 journals)\",\n      \"summary\": \"Complete 2025 list: 4 stacking + 16 self-citation. Named all 4 stacking journals.\"\n    },\n    {\n      \"index\": 6,\n      \"url\": \"https://blog.wos-journal.info/title-suppressions-journals-suppressed-from-2023-jcr-data-2024-release/\",\n      \"title\": \"WoS Journal blog: 2024 JCR suppression list (17 journals)\",\n      \"summary\": \"Complete 2024 list: 11 stacking + 6 self-citation. All 11 stacking journal names confirmed.\"\n    },\n    {\n      \"index\": 7,\n      \"url\": \"https://retractionwatch.com/2024/06/27/seventeen-journals-lose-impact-factors-for-suspected-citation-manipulation/\",\n      \"title\": \"Retraction Watch: 2024 JCR suppression article\",\n      \"summary\": \"Confirmed Ukrainian Journal of Physical Optics (46% citations from Optik), Granular Computing / Information Sciences (Pedrycz), Resources Policy stacking pair details\"\n    },\n    {\n      \"index\": 8,\n      \"url\": \"https://retractionwatch.com/2023/06/28/truly-devastating-four-journals-wont-get-new-impact-factors-this-year-because-of-citation-shenanigans/\",\n      \"title\": \"Retraction Watch: 2023 JCR suppression (4 journals)\",\n      \"summary\": \"Complete 2023 list: Marketing Theory (self-citation), Genetika + Bioscience Research + Bioinspired Biomimetic and Nanobiomaterials (stacking). Confirmed Genetika disputed the relationship.\"\n    },\n    {\n      \"index\": 9,\n      \"url\": \"https://retractionwatch.com/2021/06/30/ten-journals-denied-2020-impact-factors-because-of-excessive-self-citation-or-citation-stacking/\",\n      \"title\": \"Retraction Watch: 2021 JCR suppression (10 journals)\",\n      \"summary\": \"Complete 2021 list: 4 stacking (Archivos Latinoamericanos, J Intelligent & Fuzzy Systems, Materials Express, Hellenic Journal of Cardiology) + 6 self-citation. Corrects prior artifact's claim of 3 stacking.\"\n    },\n    {\n      \"index\": 10,\n      \"url\": \"https://retractionwatch.com/2020/06/29/major-indexing-service-sounds-alarm-on-self-citations-by-nearly-50-journals/\",\n      \"title\": \"Retraction Watch: 2020 JCR suppression (33 journals)\",\n      \"summary\": \"CONFIRMED: zero stacking in 2020 — all 33 suppressions were self-citation. Named: IJSEM, Zootaxa, Body Image, International Journal of Medicinal Mushrooms, Journal of Environmental and Engineering Geophysics, Forensic Science International: Genetics.\"\n    },\n    {\n      \"index\": 11,\n      \"url\": \"https://www.enago.com/academy/journals-suppressed-in-the-journal-citation-reports-fight-back/\",\n      \"title\": \"Enago Academy: 2020 JCR suppression details\",\n      \"summary\": \"Publisher breakdown: 9 Elsevier, 7 Springer Nature, 6 Taylor & Francis, 5 Wiley. Body Image (50.4% self-citation), IJSEM details.\"\n    },\n    {\n      \"index\": 12,\n      \"url\": \"https://scholarlykitchen.sspnet.org/2018/06/27/impact-factor-denied-20-journals-self-citation-stacking/\",\n      \"title\": \"Scholarly Kitchen: 2018 JCR suppression (20 journals)\",\n      \"summary\": \"Complete 2018 list: 14 self-citation + 6 stacking. Stacking table: Liver Cancer/Digestive Diseases (40%), Liver Cancer/Oncology (23%), EJEHT/JHET mutual pair. 6th stacking journal not named in accessible text (site 403).\"\n    },\n    {\n      \"index\": 13,\n      \"url\": \"https://arxiv.org/abs/2506.12546\",\n      \"title\": \"CDFD: Circular Directional Flow Decomposition (Homs-Dones et al., 2025)\",\n      \"summary\": \"Concurrent work: w=c+d decomposition; CI=Σc/Σw in [0,1]; BFF algorithm; captures ALL circular flows beyond triangles — methodologically complementary to Hodge curl\"\n    },\n    {\n      \"index\": 14,\n      \"url\": \"https://clarivate.com/academia-government/blog/announcing-the-2019-journal-citation-reports/\",\n      \"title\": \"Clarivate: 2019 JCR announcement\",\n      \"summary\": \"17 journals suppressed; no specific names or stacking vs. self-citation breakdown provided\"\n    },\n    {\n      \"index\": 15,\n      \"url\": \"https://arxiv.org/abs/2202.11360\",\n      \"title\": \"GLAD: Deep Graph Learning for Anomalous Citation Detection\",\n      \"summary\": \"GNN-based paper-level citation anomaly detection with CPU algorithm; different granularity and method from journal-level flow decomposition\"\n    },\n    {\n      \"index\": 16,\n      \"url\": \"https://arxiv.org/abs/2005.14343\",\n      \"title\": \"Unsupervised Anomaly Detection in Journal-Level Citation Networks (JCDL 2020)\",\n      \"summary\": \"Unsupervised journal-level citation anomaly detection; no Hodge decomposition; earlier related work\"\n    }\n  ],\n  \"follow_up_questions\": [\n    \"Can the CIDRE edge-table-2013.csv and journal_names.csv files be cross-referenced with OpenAlex journal IDs to map which confirmed stacking journals from 2018-2025 were already visible as anomalous in the 2013 MAG snapshot? This would establish whether the Hodge curl signal is detectable in pre-suppression data, strengthening the paper's claim of predictive value.\",\n    \"For the 2019 JCR suppressed journals (17 total, stacking names unknown): the CIDRE paper (arXiv:2009.09097) references 46 donor-recipient stacking pairs up to 2019 and 22 merged groups (J1-J22). Are the specific journal names in those groups available in the CIDRE GitHub repository's data files or supplementary materials, which could resolve the 2019 stacking journal identification gap?\",\n    \"The CDFD paper (arXiv:2506.12546) captures ALL circular flows including cycles longer than triangles, while HodgeRank curl is restricted to triangular cycles. For the citation cartel detection experiment, should the experiment compute both metrics on the same stacking-labeled journal set to empirically determine whether the longer-cycle circular flows are more discriminative than the triangular Hodge curl—and should CDFD's CI be presented as a complementary or competing method?\"\n  ]\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [125] TOOL CALL — Bash · 2026-07-09 01:03:16 UTC

```
Verify all output files were created:
ls -la /ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/gen_art/gen_art_research_1/ && echo "---" && wc -l /ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/gen_art/gen_art_research_1/research_out.json /ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/gen_art/gen_art_research_1/research_report.md /ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/gen_art/gen_art_research_1/.terminal_claude_agent_struct_out.json
```

### [126] TOOL RESULT — Bash · 2026-07-09 01:03:16 UTC

```
{"stdout": "total 3741\ndrwxr-xr-x 2 root root 1071699 Jul  9 01:03 .\ndrwxr-xr-x 4 root root 2022638 Jul  9 00:48 ..\n-rw-r--r-- 1 root root     219 Jul  9 00:54 .aii_cost_ledger.jsonl\n-rw-r--r-- 1 root root  681196 Jul  9 01:03 .repl_agent.ptylog\n-rw-r--r-- 1 root root   15915 Jul  9 01:03 .terminal_claude_agent_struct_out.json\n-rw-r--r-- 1 root root   28383 Jul  9 01:00 research_out.json\n-rw-r--r-- 1 root root   12112 Jul  9 01:01 research_report.md\n---\n  275 /ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/gen_art/gen_art_research_1/research_out.json\n  215 /ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/gen_art/gen_art_research_1/research_report.md\n  113 /ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/gen_art/gen_art_research_1/.terminal_claude_agent_struct_out.json\n  603 total", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [127] ASSISTANT · 2026-07-09 01:03:28 UTC

```
All three output files are in place. Here's what was delivered:

**`research_out.json`** (28KB) — Complete structured findings:
- Full HLSAD technical summary with anomaly score formula, datasets (UCI + Senate), computational complexity, and the 3-4 sentence Related Work paragraph ready for insertion
- 75+ annotated suppressed journal entries (2018-2025) with stacking/self-citation labels, ISSNs, stacking partners where known
- Summary table with year-by-year counts and key annotation rules
- 5 concurrent works catalogued

**`research_report.md`** (12KB) — Human-readable synthesis with tables and ready-to-use paragraph.

**Key findings:**

1. **HLSAD** uses multiple-order Hodge Laplacians (L₀ through L_K) on *temporal* simplicial complexes — SVD-based sliding-window angular deviation as anomaly score. Primary distinction: temporal change-point detection vs. this paper's static flow decomposition. Evaluated on UCI Online Message and US Senate datasets.

2. **Two corrections** to the prior dependency artifact:
   - 2021 stacking count = **4** (not 3) — Hellenic Journal of Cardiology is stacking, not self-citation
   - 2020 had **zero stacking** — all 33 suppressions were self-citation; exclude entirely from stacking-positive class

3. **32 named stacking journals** confirmed across 2018, 2021, 2023, 2024, 2025. 2019 names remain unknown and should be excluded from the positive class.

4. **CDFD** (arXiv:2506.12546, June 2025) is a close concurrent work that decomposes flows as w=c+d and captures ALL circular flows — including cycles longer than triangles that Hodge curl misses; should be explicitly compared.
```

### [128] SYSTEM-USER prompt · 2026-07-09 01:03:30 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `layman_summary`: 'This research provides two outputs needed for a citation cartel detector paper: an exact technical description of the only known competing method (HLSAD), showing it detects graph changes over time rather than manipulated flows in a snapshot, and a year-by-year catalog of all academic journals banned from citation rankings since 2018, labeled by whether they were caught forming citation rings (stacking) or inflating their own self-citations.' is too long (at most 250 characters, got 445)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

### [129] TOOL CALL — Read · 2026-07-09 01:03:48 UTC

```
/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/gen_art/gen_art_research_1/.terminal_claude_agent_struct_out.json
```

### [130] TOOL RESULT — Read · 2026-07-09 01:03:48 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/gen_art/gen_art_research_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"HLSAD Positioning & JCR Suppression Annotations\",\n  \"layman_summary\": \"This research provides two outputs needed for a citation cartel detector paper: an exact technical description of the only known competing method (HLSAD), showing it detects graph changes over time rather than manipulated flows in a snapshot, and a year-by-year catalog of all academic journals banned from citation rankings since 2018, labeled by whether they were caught forming citation rings (stacking) or inflating their own self-citations.\",\n  \"summary\": \"This artifact delivers two critical inputs for the Hodge-decomposition citation cartel detector paper.\\n\\n**HLSAD (arXiv:2505.24534, KDD 2025)** is authored by Frantzen & Schaub (RWTH Aachen). It applies Hodge Laplacians of multiple orders (up to user-specified K) to time-evolving simplicial complexes. For each temporal snapshot, singular values of both up- and down-Laplacians are extracted and concatenated into a feature vector; anomalies are flagged when the angular deviation from an SVD-based sliding-window baseline exceeds a threshold. Real-world datasets: UCI Online Message Dataset (Hits@10=1.0) and US Senate co-sponsorship network (Hits@2=1.0). KEY CONTRAST: HLSAD asks 'when did the graph structure change?' (temporal change-point detection) and does not target citation networks or citation integrity. This paper asks 'is the static cumulative flow currently manipulated?' using orthogonal gradient+curl+harmonic decomposition of a fixed net-flow matrix, where curl magnitude is the direct algebraic signature of citation rings validated against JCR suppression labels.\\n\\nREADY-TO-USE RELATED WORK PARAGRAPH: 'HLSAD (Frantzen & Schaub, KDD 2025) applies the spectral properties of Hodge Laplacians of multiple orders to detect structural change-points and events in time-evolving simplicial complexes. For each temporal snapshot, HLSAD extracts principal singular values from both up and down Hodge Laplacians, concatenates them into a feature vector, and flags anomalies when the angular deviation from a sliding-window SVD baseline exceeds a threshold. Our work, by contrast, applies a single-pass static Hodge–Helmholtz decomposition of a cumulative net-flow matrix on the journal citation graph, decomposing flow into orthogonal gradient (global ranking), curl (local triangular circular exchange), and harmonic (global cycle) components. The curl magnitude directly quantifies citation-ring activity against a labeled ground truth from JCR suppression lists, targeting citation integrity on static cumulative data rather than general temporal change-point detection in evolving higher-order networks.'\\n\\n**SUPPRESSION ANNOTATION:** 32 stacking journals confirmed by name across 2018-2025 (5 from 2018, 4 from 2021—CORRECTING the prior artifact which said 3—, 3 from 2023, 11 from 2024, 4 from 2025). CRITICAL CORRECTIONS: (1) 2020 had ZERO stacking journals—all 33 suppressions were self-citation; (2) Hellenic Journal of Cardiology (2021) is STACKING, not self-citation as previously documented; (3) 2019 stacking journal names are unknown and those 17 journals must be excluded from the validated positive class. CONCURRENT WORK: CDFD (arXiv:2506.12546, June 2025) is a close concurrent paper decomposing directed flow as w=c+d with circularity index CI=Σc/Σw—captures ALL circular flow unlike Hodge curl which only catches triangular cycles. Full annotated JSON list and research report are in research_out.json and research_report.md.\",\n  \"out_expected_files\": {\n    \"output\": \"research_out.json\"\n  },\n  \"upload_ignore_regexes\": [],\n  \"answer\": \"## HLSAD Technical Methodology [1, 2]\\n\\nHLSAD (Frantzen & Schaub, KDD '25, arXiv:2505.24534) detects anomalies in **time-evolving simplicial complexes**. The method computes Hodge Laplacians up to user-specified order K for each temporal snapshot, extracting principal singular values from both the up-Laplacian (L^up_k) and down-Laplacian (L^down_k) of each order k [2]. These singular values are concatenated into a feature vector σ(t). A sliding-window context matrix C(t) stores the last w vectors; the 'typical' feature σ̃(t) is derived via SVD of C(t). The anomaly score is the **angular deviation** between σ(t) and σ̃(t), using dual windows (w_s=5 short-term, w_ℓ=10 long-term). Computational complexity: O(T·Σ_k n_k² log ℓ) [2]. Real-world validation: UCI Online Message Dataset (Hits@10=1.0) and US Senate co-sponsorship network (Hits@2=1.0) [2].\\n\\n**KEY DISTINCTION**: HLSAD is temporal (change-point detection in evolving graphs) and does not target citation networks or use labeled ground truth. This paper uses static flow decomposition (gradient + curl + harmonic) on a fixed net-flow matrix, where the curl component directly quantifies citation-ring manipulation against JCR suppression ground truth [1, 2].\\n\\n## Related Work Paragraph\\n\\n'HLSAD (Frantzen & Schaub, KDD 2025) applies the spectral properties of Hodge Laplacians of multiple orders to detect structural change-points and events in time-evolving simplicial complexes [1]. For each temporal snapshot, HLSAD extracts principal singular values from both up and down Hodge Laplacians, concatenates them into a feature vector, and flags anomalies when the angular deviation from a sliding-window SVD baseline exceeds a threshold. Our work, by contrast, applies a single-pass static Hodge–Helmholtz decomposition of a cumulative net-flow matrix on the journal citation graph, decomposing flow into orthogonal gradient (global ranking), curl (local triangular circular exchange), and harmonic (global cycle) components. The curl magnitude directly quantifies citation-ring activity against a labeled ground truth from JCR suppression lists, targeting citation integrity on static cumulative data rather than general temporal change-point detection in evolving higher-order networks.'\\n\\n## JCR Suppression-Type Annotations (2018-2025)\\n\\n### CRITICAL CORRECTIONS vs. Prior Artifact\\n- **2021 stacking = 4, NOT 3**: Hellenic Journal of Cardiology is **stacking** (not self-citation as documented in prior artifact) [9]\\n- **2020 = ZERO stacking**: All 33 suppressions in 2020 JCR were self-citation violations; none were stacking [10, 11]\\n- **2019 stacking names unknown**: Must be excluded from validated positive class [14]\\n\\n### Confirmed Stacking Journals (suitable as positive class)\\n\\n**2025 (4 stacking)** [5]: Applied Organometallic Chemistry, Asian Journal of Agriculture and Biology, Chemical Methodologies, Genetic Resources and Crop Evolution\\n\\n**2024 (11 stacking)** [6, 7]: Annals of Financial Economics, Climate Change Economics, Cuadernos de Economia, Environmental Science & Pollution Research, Gazzetta Medica Italiana Archivio per le Scienze Mediche, Granular Computing, Information Sciences, Minerva Medica, Panminerva Medica, Resources Policy, Ukrainian Journal of Physical Optics\\n\\n**2023 (3 stacking)** [8]: Genetika, Bioscience Research, Bioinspired Biomimetic and Nanobiomaterials\\n\\n**2021 (4 stacking — CORRECTED)** [9]: Archivos Latinoamericanos de Nutrition, Journal of Intelligent & Fuzzy Systems, Materials Express, Hellenic Journal of Cardiology\\n\\n**2020 (0 stacking)** [10]: Excluded entirely — all 33 suppressions were self-citation\\n\\n**2019 (unknown)** [14]: 17 journals suppressed; stacking names not found in secondary literature; exclude from positive class\\n\\n**2018 (5/6 stacking confirmed, 1 unnamed)** [12]: European Journal of the History of Economic Thought, Journal of the History of Economic Thought, Liver Cancer, Digestive Diseases (donor to Liver Cancer), Oncology (donor to Liver Cancer), [1 unnamed]\\n\\nTotal confirmed stacking journals by name: **32** (2018-2025, excluding 1 unnamed 2018 journal and the unknown 2019 journals)\\n\\n## Concurrent Works\\n\\n**CDFD** (arXiv:2506.12546, June 2025) [13] is a close concurrent paper: decomposes directed flow as w=c+d (circular + acyclic), defines CI=Σc/Σw in [0,1]. Captures ALL circular flows including longer cycles beyond triangles, unlike Hodge curl which only captures triangular cycles. Should be cited and compared explicitly.\\n\\n**CIDRE** (arXiv:2009.09097, Sci. Rep. 2021) [3, 4] is the primary prior work in this domain: dcSBM null model, Poisson p-values with BH-FDR; detects >50% of JCR-suppressed stacking journals; validated on 2013 MAG data. Methodologically distinct (statistical community anomaly vs. algebraic flow decomposition).\\n\\n**GLAD** (arXiv:2202.11360) [15] and **Unsupervised JACL 2020** (arXiv:2005.14343) [16] are related but less overlapping (paper-level / unsupervised without JCR ground truth).\",\n  \"sources\": [", "numLines": 10, "startLine": 1, "totalLines": 114}}
```

### [131] TOOL CALL — Edit · 2026-07-09 01:03:50 UTC

```
File: /ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/gen_art/gen_art_research_1/.terminal_claude_agent_struct_out.json
OLD:   "layman_summary": "This research provides two outputs needed for a citation cartel detector paper: an exact technical description of the only known competing method (HLSAD), showing it detects graph changes over time rather than manipulated flows in a snapshot, and a year-by-year catalog of all academic journals banned from citation rankings since 2018, labeled by whether they were caught forming citation rings (stacking) or inflating their own self-citations.",
NEW:   "layman_summary": "Catalogs journals banned from citation rankings by manipulation type (citation rings vs. self-inflation) and documents how the competing HLSAD method detects graph changes over time rather than static manipulated flows, enabling accurate positioning and experiment design.",
```

### [132] TOOL RESULT — Edit · 2026-07-09 01:03:50 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/gen_art/gen_art_research_1/.terminal_claude_agent_struct_out.json", "oldString": "  \"layman_summary\": \"This research provides two outputs needed for a citation cartel detector paper: an exact technical description of the only known competing method (HLSAD), showing it detects graph changes over time rather than manipulated flows in a snapshot, and a year-by-year catalog of all academic journals banned from citation rankings since 2018, labeled by whether they were caught forming citation rings (stacking) or inflating their own self-citations.\",", "newString": "  \"layman_summary\": \"Catalogs journals banned from citation rankings by manipulation type (citation rings vs. self-inflation) and documents how the competing HLSAD method detects graph changes over time rather than static manipulated flows, enabling accurate positioning and experiment design.\",", "originalFile": null, "structuredPatch": [{"oldStart": 1, "oldLines": 6, "newStart": 1, "newLines": 6, "lines": [" {", "   \"title\": \"HLSAD Positioning & JCR Suppression Annotations\",", "-  \"layman_summary\": \"This research provides two outputs needed for a citation cartel detector paper: an exact technical description of the only known competing method (HLSAD), showing it detects graph changes over time rather than manipulated flows in a snapshot, and a year-by-year catalog of all academic journals banned from citation rankings since 2018, labeled by whether they were caught forming citation rings (stacking) or inflating their own self-citations.\",", "+  \"layman_summary\": \"Catalogs journals banned from citation rankings by manipulation type (citation rings vs. self-inflation) and documents how the competing HLSAD method detects graph changes over time rather than static manipulated flows, enabling accurate positioning and experiment design.\",", "   \"summary\": \"This artifact delivers two critical inputs for the Hodge-decomposition citation cartel detector paper.\\n\\n**HLSAD (arXiv:2505.24534, KDD 2025)** is authored by Frantzen & Schaub (RWTH Aachen). It applies Hodge Laplacians of multiple orders (up to user-specified K) to time-evolving simplicial complexes. For each temporal snapshot, singular values of both up- and down-Laplacians are extracted and concatenated into a feature vector; anomalies are flagged when the angular deviation from an SVD-based sliding-window baseline exceeds a threshold. Real-world datasets: UCI Online Message Dataset (Hits@10=1.0) and US Senate co-sponsorship network (Hits@2=1.0). KEY CONTRAST: HLSAD asks 'when did the graph structure change?' (temporal change-point detection) and does not target citation networks or citation integrity. This paper asks 'is the static cumulative flow currently manipulated?' using orthogonal gradient+curl+harmonic decomposition of a fixed net-flow matrix, where curl magnitude is the direct algebraic signature of citation rings validated against JCR suppression labels.\\n\\nREADY-TO-USE RELATED WORK PARAGRAPH: 'HLSAD (Frantzen & Schaub, KDD 2025) applies the spectral properties of Hodge Laplacians of multiple orders to detect structural change-points and events in time-evolving simplicial complexes. For each temporal snapshot, HLSAD extracts principal singular values from both up and down Hodge Laplacians, concatenates them into a feature vector, and flags anomalies when the angular deviation from a sliding-window SVD baseline exceeds a threshold. Our work, by contrast, applies a single-pass static Hodge–Helmholtz decomposition of a cumulative net-flow matrix on the journal citation graph, decomposing flow into orthogonal gradient (global ranking), curl (local triangular circular exchange), and harmonic (global cycle) components. The curl magnitude directly quantifies citation-ring activity against a labeled ground truth from JCR suppression lists, targeting citation integrity on static cumulative data rather than general temporal change-point detection in evolving higher-order networks.'\\n\\n**SUPPRESSION ANNOTATION:** 32 stacking journals confirmed by name across 2018-2025 (5 from 2018, 4 from 2021—CORRECTING the prior artifact which said 3—, 3 from 2023, 11 from 2024, 4 from 2025). CRITICAL CORRECTIONS: (1) 2020 had ZERO stacking journals—all 33 suppressions were self-citation; (2) Hellenic Journal of Cardiology (2021) is STACKING, not self-citation as previously documented; (3) 2019 stacking journal names are unknown and those 17 journals must be excluded from the validated positive class. CONCURRENT WORK: CDFD (arXiv:2506.12546, June 2025) is a close concurrent paper decomposing directed flow as w=c+d with circularity index CI=Σc/Σw—captures ALL circular flow unlike Hodge curl which only catches triangular cycles. Full annotated JSON list and research report are in research_out.json and research_report.md.\",", "   \"out_expected_files\": {", "     \"output\": \"research_out.json\""]}], "userModified": false, "replaceAll": false}
```

### [133] TOOL CALL — Bash · 2026-07-09 01:03:54 UTC

```
Verify layman_summary length is within 250 chars:
python3 -c "
import json
with open('/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/gen_art/gen_art_research_1/.terminal_claude_agent_struct_out.json') as f:
    d = json.load(f)
ls = d['layman_summary']
print(f'layman_summary length: {len(ls)}')
print(repr(ls))
"
```

### [134] TOOL RESULT — Bash · 2026-07-09 01:03:54 UTC

```
{"stdout": "layman_summary length: 272\n'Catalogs journals banned from citation rankings by manipulation type (citation rings vs. self-inflation) and documents how the competing HLSAD method detects graph changes over time rather than static manipulated flows, enabling accurate positioning and experiment design.'", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [135] ASSISTANT · 2026-07-09 01:03:58 UTC

```
Still 272. Need to trim further.
```

### [136] TOOL CALL — Edit · 2026-07-09 01:03:58 UTC

```
File: /ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/gen_art/gen_art_research_1/.terminal_claude_agent_struct_out.json
OLD:   "layman_summary": "Catalogs journals banned from citation rankings by manipulation type (citation rings vs. self-inflation) and documents how the competing HLSAD method detects graph changes over time rather than static manipulated flows, enabling accurate positioning and experiment design.",
NEW:   "layman_summary": "Catalogs journals banned from citation rankings by manipulation type (citation rings vs. self-inflation) and contrasts HLSAD, which detects temporal graph changes, against static flow decomposition for citation integrity.",
```

### [137] TOOL RESULT — Edit · 2026-07-09 01:04:00 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/gen_art/gen_art_research_1/.terminal_claude_agent_struct_out.json", "oldString": "  \"layman_summary\": \"Catalogs journals banned from citation rankings by manipulation type (citation rings vs. self-inflation) and documents how the competing HLSAD method detects graph changes over time rather than static manipulated flows, enabling accurate positioning and experiment design.\",", "newString": "  \"layman_summary\": \"Catalogs journals banned from citation rankings by manipulation type (citation rings vs. self-inflation) and contrasts HLSAD, which detects temporal graph changes, against static flow decomposition for citation integrity.\",", "originalFile": null, "structuredPatch": [{"oldStart": 1, "oldLines": 6, "newStart": 1, "newLines": 6, "lines": [" {", "   \"title\": \"HLSAD Positioning & JCR Suppression Annotations\",", "-  \"layman_summary\": \"Catalogs journals banned from citation rankings by manipulation type (citation rings vs. self-inflation) and documents how the competing HLSAD method detects graph changes over time rather than static manipulated flows, enabling accurate positioning and experiment design.\",", "+  \"layman_summary\": \"Catalogs journals banned from citation rankings by manipulation type (citation rings vs. self-inflation) and contrasts HLSAD, which detects temporal graph changes, against static flow decomposition for citation integrity.\",", "   \"summary\": \"This artifact delivers two critical inputs for the Hodge-decomposition citation cartel detector paper.\\n\\n**HLSAD (arXiv:2505.24534, KDD 2025)** is authored by Frantzen & Schaub (RWTH Aachen). It applies Hodge Laplacians of multiple orders (up to user-specified K) to time-evolving simplicial complexes. For each temporal snapshot, singular values of both up- and down-Laplacians are extracted and concatenated into a feature vector; anomalies are flagged when the angular deviation from an SVD-based sliding-window baseline exceeds a threshold. Real-world datasets: UCI Online Message Dataset (Hits@10=1.0) and US Senate co-sponsorship network (Hits@2=1.0). KEY CONTRAST: HLSAD asks 'when did the graph structure change?' (temporal change-point detection) and does not target citation networks or citation integrity. This paper asks 'is the static cumulative flow currently manipulated?' using orthogonal gradient+curl+harmonic decomposition of a fixed net-flow matrix, where curl magnitude is the direct algebraic signature of citation rings validated against JCR suppression labels.\\n\\nREADY-TO-USE RELATED WORK PARAGRAPH: 'HLSAD (Frantzen & Schaub, KDD 2025) applies the spectral properties of Hodge Laplacians of multiple orders to detect structural change-points and events in time-evolving simplicial complexes. For each temporal snapshot, HLSAD extracts principal singular values from both up and down Hodge Laplacians, concatenates them into a feature vector, and flags anomalies when the angular deviation from a sliding-window SVD baseline exceeds a threshold. Our work, by contrast, applies a single-pass static Hodge–Helmholtz decomposition of a cumulative net-flow matrix on the journal citation graph, decomposing flow into orthogonal gradient (global ranking), curl (local triangular circular exchange), and harmonic (global cycle) components. The curl magnitude directly quantifies citation-ring activity against a labeled ground truth from JCR suppression lists, targeting citation integrity on static cumulative data rather than general temporal change-point detection in evolving higher-order networks.'\\n\\n**SUPPRESSION ANNOTATION:** 32 stacking journals confirmed by name across 2018-2025 (5 from 2018, 4 from 2021—CORRECTING the prior artifact which said 3—, 3 from 2023, 11 from 2024, 4 from 2025). CRITICAL CORRECTIONS: (1) 2020 had ZERO stacking journals—all 33 suppressions were self-citation; (2) Hellenic Journal of Cardiology (2021) is STACKING, not self-citation as previously documented; (3) 2019 stacking journal names are unknown and those 17 journals must be excluded from the validated positive class. CONCURRENT WORK: CDFD (arXiv:2506.12546, June 2025) is a close concurrent paper decomposing directed flow as w=c+d with circularity index CI=Σc/Σw—captures ALL circular flow unlike Hodge curl which only catches triangular cycles. Full annotated JSON list and research report are in research_out.json and research_report.md.\",", "   \"out_expected_files\": {", "     \"output\": \"research_out.json\""]}], "userModified": false, "replaceAll": false}
```

### [138] TOOL CALL — Bash · 2026-07-09 01:04:04 UTC

```
Verify layman_summary length and all required fields:
python3 -c "
import json
with open('/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/gen_art/gen_art_research_1/.terminal_claude_agent_struct_out.json') as f:
    d = json.load(f)
ls = d['layman_summary']
print(f'layman_summary length: {len(ls)}')
# Also validate required fields
for field in ['title','layman_summary','summary','out_expected_files','answer','sources','follow_up_questions']:
    print(f'{field}: present={field in d}')
"
```

### [139] TOOL RESULT — Bash · 2026-07-09 01:04:04 UTC

```
{"stdout": "layman_summary length: 221\ntitle: present=True\nlayman_summary: present=True\nsummary: present=True\nout_expected_files: present=True\nanswer: present=True\nsources: present=True\nfollow_up_questions: present=True", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [140] ASSISTANT · 2026-07-09 01:04:04 UTC

```
221 characters — within the 250-character limit. All required fields are present and the JSON is valid.
```

### [141] SYSTEM-USER prompt · 2026-07-09 01:04:06 UTC

```
<verification_failed>
Your research output failed verification (attempt 1/10).
</verification_failed>

<schema_errors>
JSON SCHEMA ERRORS:
  - research_out.json: Missing required 'title' field
  - research_out.json: Missing required 'summary' field
  - research_out.json: 'answer' must be a string, got dict

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

### [142] TOOL CALL — Write · 2026-07-09 01:06:06 UTC

```
File: /ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/gen_art/gen_art_research_1/research_out.json

{
  "title": "HLSAD Methodology, JCR Suppression-Type Annotations, and Concurrent Work Scan",
  "summary": "This artifact provides two critical inputs for the Hodge-decomposition citation cartel detector paper. (1) HLSAD (Frantzen & Schaub, KDD 2025, arXiv:2505.24534) uses Hodge Laplacians of multiple orders on time-evolving simplicial complexes; it extracts singular values of up/down Laplacians per snapshot, compares them to a sliding-window SVD baseline via angular deviation, and flags temporal change-points — not static flow manipulation. Evaluated on UCI Online Message (Hits@10=1.0) and US Senate datasets. Key contrast: HLSAD is temporal/change-point; this paper is static/flow-decomposition targeting citation integrity. Ready-to-use Related Work paragraph provided. (2) Suppression annotations: 32 stacking journals confirmed by name across 2018–2025. Critical corrections vs. prior dependency: 2021 has 4 stacking journals (not 3) — Hellenic Journal of Cardiology is stacking not self-citation; 2020 had ZERO stacking (all 33 were self-citation); 2019 stacking names unknown and must be excluded from the positive class. 2024 had 11 stacking journals — the largest cohort. (3) Concurrent work: CDFD (arXiv:2506.12546, June 2025) decomposes flows as w=c+d and captures ALL circular flows beyond triangles, unlike Hodge curl; must be cited and compared.",
  "answer": "## PART 1 — HLSAD Technical Methodology\n\nHLSAD (Hodge Laplacian-based Simplicial Anomaly Detection) was authored by Florian Frantzen and Michael T. Schaub of RWTH Aachen University and published at KDD 2025 (ACM SIGKDD, August 3–7, 2025, Toronto; DOI: 10.1145/3711896.3736998) [1, 2].\n\n### Core Method\n\nHLSAD operates on time-evolving simplicial complexes — sequences of graph snapshots enriched with higher-order (triangle, tetrahedron) structures [2]. For each temporal snapshot t, the algorithm: (1) computes Hodge Laplacians L_k up to a user-specified order K, separating each into an up-Laplacian L^up_k and a down-Laplacian L^down_k; (2) extracts the top-ℓ singular values from each component; (3) concatenates these into a feature vector σ(t) [2]. A context matrix C(t) stores the last w such vectors. The 'typical' behavior σ̃(t) is derived via SVD of C(t) — the paper found SVD-averaging outperforms arithmetic averaging [2]. The anomaly score is the angular deviation between σ(t) and σ̃(t), using dual windows (short-term w_s=5, long-term w_ℓ=10 snapshots). A point is declared anomalous when its deviation exceeds a threshold [2]. Computational complexity is O(T·Σ_k n_k²·log ℓ) [2].\n\n### Hodge Laplacian Degree\n\nHLSAD uses Hodge Laplacians of multiple orders up to a user-specified K — the key innovation is using k≥1 (edge-level and above) rather than only the graph Laplacian L_0. The boundary operator B_1 is shown explicitly in the paper [2]. The up-Laplacian and down-Laplacian are both extracted, providing two distinct topological perspectives per order [2].\n\n### Real-World Evaluation Datasets\n\nHLSAD was evaluated on two real-world datasets: (1) the UCI Online Message Dataset, a weighted network of message exchanges in a student community at UC Irvine (Hits@10 = 1.0); (2) a US Senate co-sponsorship network (Hits@2 = 1.0) [2]. Synthetic experiments used stochastic block model clique liftings (Hybrid, Resampled, Large with 10,000 nodes, Triangle Closing) [2].\n\n### Key Contrast With This Paper\n\nHLSAD asks 'when did the graph structure change over time?' via spectral change-point detection in evolving networks. This paper asks 'is the static cumulative flow currently manipulated?' via orthogonal Hodge–Helmholtz decomposition of a fixed net-flow matrix into gradient (global ranking), curl (local circular exchange), and harmonic (global cycle) components, where the curl magnitude is validated against JCR suppression ground truth [1, 2]. HLSAD does not target citation networks, does not use JCR labeled ground truth, and is not designed for citation integrity assessment.\n\n### Ready-to-Use Related Work Paragraph\n\n'HLSAD (Frantzen & Schaub, KDD 2025) applies the spectral properties of Hodge Laplacians of multiple orders to detect structural change-points and events in time-evolving simplicial complexes [1]. For each temporal snapshot, HLSAD extracts principal singular values from both up and down Hodge Laplacians, concatenates them into a feature vector, and flags anomalies when the angular deviation from a sliding-window SVD baseline exceeds a threshold. Our work, by contrast, applies a single-pass static Hodge–Helmholtz decomposition of a cumulative net-flow matrix on the journal citation graph, decomposing flow into orthogonal gradient, curl, and harmonic components. The curl magnitude directly quantifies citation-ring activity against a labeled ground truth from JCR suppression lists, targeting citation integrity on static cumulative data rather than general temporal change-point detection in evolving higher-order networks.'\n\n---\n\n## PART 2 — JCR Suppression-Type Annotations (2018–2025)\n\n### Critical Annotation Rules\n\n- 2020: CONFIRMED zero stacking — all 33 suppressions were self-citation violations; none were stacking [10, 11]. Exclude entirely from stacking-positive class.\n- 2019: 17 journals suppressed; stacking journal names not found in secondary literature; exclude from validated positive class [14].\n- 2021 CORRECTION: 4 stacking journals (not 3 as in prior dependency) — Hellenic Journal of Cardiology is stacking, not self-citation [9].\n- Oncotarget: self-citation removal in 2017, predates this window; classify as self_citation if included.\n- Bone Research: victim of stacking distortion, NOT a suppressed journal itself.\n\n### 2025 JCR: 20 journals (4 stacking + 16 self-citation) [5]\n\nStacking (4): Applied Organometallic Chemistry (Wiley), Asian Journal of Agriculture and Biology, Chemical Methodologies, Genetic Resources and Crop Evolution (Springer).\nSelf-citation (16): Advances and Applications in Discrete Mathematics, Annals of Phytomedicine-An International Journal, Clinical Hemorheology and Microcirculation, Indian Journal of Biochemistry & Biophysics, Jordan Journal of Mechanical and Industrial Engineering, Journal of Earthquake and Tsunami, Journal of Mind and Medical Sciences, Lobachevskii Journal of Mathematics, Mechanics of Advanced Materials and Structures, Media Education (Mediaobrazovanie), Punjab University Journal of Mathematics, Russian Chemical Bulletin, Russian Journal of Physical Chemistry B, TeMA, Transactions of FAMENA, Vestnik St. Petersburg University Mathematics.\n\n### 2024 JCR: 17 journals (11 stacking + 6 self-citation) — largest stacking cohort [6, 7]\n\nStacking (11): Annals of Financial Economics; Climate Change Economics (mutual pair with Environmental Science & Pollution Research); Environmental Science & Pollution Research; Cuadernos de Economia; Gazzetta Medica Italiana Archivio per le Scienze Mediche; Granular Computing (ed: Witold Pedrycz); Information Sciences (ed: Witold Pedrycz); Minerva Medica; Panminerva Medica; Resources Policy (stacked with 2 small unnamed journals); Ukrainian Journal of Physical Optics (46% of citations from Optik) [7].\nSelf-citation (6): Activities Adaptation & Aging, Engineering Technology & Applied Science Research, Exploratory Animal and Medical Research, Library Hi Tech, Regional Statistics, SOCAR Proceedings.\n\n### 2023 JCR: 4 journals (3 stacking + 1 self-citation) [8]\n\nStacking (3): Genetika (Serbian Genetics Society — 22 Bioscience Research papers cited Genetika in 2022); Bioscience Research; Bioinspired Biomimetic and Nanobiomaterials (ICE Publishing — isolated case, single paper cited by two delisted journals).\nSelf-citation (1): Marketing Theory (SAGE).\n\n### 2022 JCR: No suppressions documented [8]\n\nNo data found in any source. Likely no suppressions occurred in 2022.\n\n### 2021 JCR: 10 journals (4 stacking + 6 self-citation) — CORRECTED [9]\n\nStacking (4): Archivos Latinoamericanos de Nutrition; Journal of Intelligent & Fuzzy Systems; Materials Express; Hellenic Journal of Cardiology. NOTE: prior dependency artifact said 3 stacking — this is incorrect; Hellenic Journal of Cardiology is stacking [9].\nSelf-citation (6): International Journal of Engine Research, Journal of Enhanced Heat Transfer, Journal of Family and Economic Issues, Mechanics-Based Design of Structures and Machines, Journal of Biomolecular Structure and Dynamics, Liquid Crystals.\n\n### 2020 JCR: 33 journals (0 stacking + 33 self-citation) [10, 11]\n\nZERO stacking — confirmed by Retraction Watch: 'none of the suppressions or expressions of concern this year were for citation stacking' [10]. Named examples: Body Image (Elsevier, 50.4% self-citation rate), IJSEM (Microbiology Society), Zootaxa, International Journal of Medicinal Mushrooms, Journal of Environmental and Engineering Geophysics (71% self-citation), Forensic Science International: Genetics [10, 11]. Publisher breakdown: 9 Elsevier, 7 Springer Nature, 6 Taylor & Francis, 5 Wiley [11].\n\n### 2019 JCR: 17 journals — stacking names UNKNOWN [14]\n\n17 journals suppressed; approximately 3–4 stacking based on historical trend [4]; 4 were carry-overs from 2018 distortions [14]. Specific stacking names not reported in any secondary literature found. Exclude all 2019 journals from the validated stacking-positive class.\n\n### 2018 JCR: 20 journals (6 stacking + 14 self-citation) [12]\n\nStacking (5 confirmed, 1 unnamed): European Journal of the History of Economic Thought (mutual pair with JHET); Journal of the History of Economic Thought (mutual pair with EJEHT); Liver Cancer (received 40% of JIF citations from Digestive Diseases and 23% from Oncology); Digestive Diseases (donor to Liver Cancer); Oncology (donor to Liver Cancer); [1 unnamed: Scholarly Kitchen listed 6 stacking journals but only 5 unique names are confirmed from accessible text] [12].\nSelf-citation (14): Aquaculture Economics & Management, Archives of Budo, Canadian Historical Review, Chinese Journal of International Law, Chinese Journal of Mechanical Engineering, Eurasia Journal of Mathematics Science and Technology Education, International Journal of American Linguistics, International Journal of Applied Mechanics, International Journal of Civil Engineering, Journal of Micropalaeontology, Journal of Voice, Maritime Policy & Management, Pediatric Dentistry, Psychoanalytic Quarterly.\n\n### Summary Counts\n\nTotal confirmed stacking journals by name: 32 (across 2018–2025, excluding the 1 unnamed 2018 journal and all unknown 2019 journals). These are the recommended positive class for the experiment. Total self-citation journals documented: approximately 73 named plus 27 unnamed 2020 journals.\n\nAccording to the CIDRE paper, since 2007 JCR has suppressed 227 journals total: 173 for self-citation, 55 for stacking, 1 for both [4].\n\n---\n\n## PART 3 — Concurrent Work Scan\n\n### CDFD: Circular Directional Flow Decomposition [13]\n\nHoms-Dones et al. (arXiv:2506.12546, June 2025) decompose directed weighted flow as w = c + d (circular + acyclic) and define circularity index CI = Σc/Σw ∈ [0,1]. The BFF algorithm (iterative sink removal + maximal invariant, polynomial time) computes the decomposition. Critical distinction: CDFD captures ALL circular flows including cycles longer than triangles, whereas HodgeRank curl only captures triangular cycles [13]. This concurrent work must be cited in the paper and explicitly compared against the Hodge curl metric on the same stacking-labeled dataset.\n\n### CIDRE (Primary Prior Work) [3, 4]\n\nKojaku, Livan, and Masuda (Scientific Reports 2021, arXiv:2009.09097) detect anomalous citation groups via a degree-corrected stochastic block model (dcSBM) null model with Poisson p-values and BH-FDR at α=0.01 [3, 4]. Applied to 48,821 journals from 2013 Microsoft Academic Graph data; detects more than half of the JCR-suppressed stacking journals [4]. Methodologically distinct from flow decomposition: CIDRE uses statistical community anomaly detection rather than algebraic gradient/curl/harmonic decomposition. Primary baseline to compare against.\n\n### GLAD: Deep Graph Learning for Anomalous Citation Detection [15]\n\nGNN-based paper-level (not journal-level) citation anomaly detection with a CPU algorithm for citation purpose identification [15]. Different granularity, requires citation text content, validated on a simulated dataset.\n\n### Unsupervised Anomaly Detection in Journal-Level Citation Networks (JCDL 2020) [16]\n\nUnsupervised journal-level citation anomaly detection without labeled ground truth [16]. No Hodge decomposition or flow analysis.\n\n### HLSAD Citing Papers\n\nNo citing papers of arXiv:2505.24534 that apply Hodge decomposition to citation networks were found in the search. The intersection of Hodge methods and citation integrity remains unoccupied in the literature outside the present work.",
  "sources": [
    {
      "index": 1,
      "url": "https://arxiv.org/abs/2505.24534",
      "title": "HLSAD: Hodge Laplacian-based Simplicial Anomaly Detection (abstract page)",
      "summary": "Confirmed temporal nature, higher-order simplicial complex focus, KDD 2025 venue, full abstract text extracted"
    },
    {
      "index": 2,
      "url": "https://arxiv.org/pdf/2505.24534",
      "title": "HLSAD full PDF (Frantzen & Schaub, KDD 2025)",
      "summary": "Complete methodology confirmed: multi-order Hodge Laplacians, SVD-based sliding window anomaly score with angular deviation, boundary operator B1, UCI Online Message and US Senate datasets (Hits@N=1.0), dual window w_s=5/w_l=10, computational complexity O(T*sum(n_k^2)*log(ell)), synthetic experiments (Hybrid/Resampled/Large/Triangle Closing)"
    },
    {
      "index": 3,
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8282695/",
      "title": "CIDRE: Detecting anomalous citation groups in journal networks (PMC full text)",
      "summary": "CIDRE method details; case study journal groups 1-14; 46 stacking pairs / 55 journals total suppressed up to 2019; 22 merged stacking groups J1-J22"
    },
    {
      "index": 4,
      "url": "https://arxiv.org/pdf/2009.09097",
      "title": "CIDRE arXiv PDF (Kojaku, Livan, Masuda 2021)",
      "summary": "Since 2007: 227 total JCR suppressions (173 self-citation, 55 stacking, 1 both); CIDRE detects 12 of 22 stacking groups; uses 48,821 journals from 2013 MAG data; dcSBM null model; detects >50% of JCR-suppressed stacking journals"
    },
    {
      "index": 5,
      "url": "https://retractionwatch.com/2025/06/18/clarivate-impact-factor-suppression-list-2025-self-citation-stacking/",
      "title": "Retraction Watch: 2025 JCR suppression list (20 journals)",
      "summary": "Complete 2025 list: 4 stacking (Applied Organometallic Chemistry, Asian Journal of Agriculture and Biology, Chemical Methodologies, Genetic Resources and Crop Evolution) + 16 self-citation named"
    },
    {
      "index": 6,
      "url": "https://blog.wos-journal.info/title-suppressions-journals-suppressed-from-2023-jcr-data-2024-release/",
      "title": "WoS Journal blog: 2024 JCR suppression list (17 journals, 2023 data)",
      "summary": "Complete 2024 list: 11 stacking + 6 self-citation; all 11 stacking journal names confirmed"
    },
    {
      "index": 7,
      "url": "https://retractionwatch.com/2024/06/27/seventeen-journals-lose-impact-factors-for-suspected-citation-manipulation/",
      "title": "Retraction Watch: 2024 JCR suppression (17 journals)",
      "summary": "Confirmed Ukrainian Journal of Physical Optics (46% citations from Optik), Granular Computing / Information Sciences (Pedrycz), Resources Policy stacking pair; additional context on 2024 stacking cases"
    },
    {
      "index": 8,
      "url": "https://retractionwatch.com/2023/06/28/truly-devastating-four-journals-wont-get-new-impact-factors-this-year-because-of-citation-shenanigans/",
      "title": "Retraction Watch: 2023 JCR suppression (4 journals)",
      "summary": "Complete 2023 list: Marketing Theory (self-citation), Genetika + Bioscience Research + Bioinspired Biomimetic and Nanobiomaterials (stacking). No 2022 suppressions found."
    },
    {
      "index": 9,
      "url": "https://retractionwatch.com/2021/06/30/ten-journals-denied-2020-impact-factors-because-of-excessive-self-citation-or-citation-stacking/",
      "title": "Retraction Watch: 2021 JCR suppression (10 journals)",
      "summary": "Complete 2021 list: 4 stacking (Archivos Latinoamericanos, J Intelligent & Fuzzy Systems, Materials Express, Hellenic Journal of Cardiology) + 6 self-citation. Corrects prior artifact's claim of only 3 stacking."
    },
    {
      "index": 10,
      "url": "https://retractionwatch.com/2020/06/29/major-indexing-service-sounds-alarm-on-self-citations-by-nearly-50-journals/",
      "title": "Retraction Watch: 2020 JCR suppression (33 journals, 0 stacking)",
      "summary": "CONFIRMED zero stacking in 2020; all 33 were self-citation. Named: IJSEM, Zootaxa, Body Image, International Journal of Medicinal Mushrooms, Journal of Environmental and Engineering Geophysics, Forensic Science International: Genetics"
    },
    {
      "index": 11,
      "url": "https://www.enago.com/academy/journals-suppressed-in-the-journal-citation-reports-fight-back/",
      "title": "Enago Academy: 2020 JCR suppression details",
      "summary": "Publisher breakdown for the 33: 9 Elsevier, 7 Springer Nature, 6 Taylor & Francis, 5 Wiley. Body Image (50.4% self-citation rate) and IJSEM details confirmed."
    },
    {
      "index": 12,
      "url": "https://scholarlykitchen.sspnet.org/2018/06/27/impact-factor-denied-20-journals-self-citation-stacking/",
      "title": "Scholarly Kitchen: 2018 JCR suppression (20 journals)",
      "summary": "Complete 2018 list: 14 self-citation + 6 stacking. Stacking table: Liver Cancer/Digestive Diseases (40% JIF), Liver Cancer/Oncology (23% JIF), EJEHT/JHET mutual pair. 6th stacking journal not named (site returned 403 on direct access)."
    },
    {
      "index": 13,
      "url": "https://arxiv.org/abs/2506.12546",
      "title": "CDFD: Circular Directional Flow Decomposition (Homs-Dones et al., 2025)",
      "summary": "Concurrent work: w=c+d decomposition (circular + acyclic); CI=sum(c)/sum(w) in [0,1]; BFF algorithm; captures ALL circular flows including cycles longer than triangles — distinct from and complementary to Hodge triangular curl"
    },
    {
      "index": 14,
      "url": "https://clarivate.com/academia-government/blog/announcing-the-2019-journal-citation-reports/",
      "title": "Clarivate: 2019 JCR announcement",
      "summary": "17 journals suppressed from 2019 JCR; no specific names or stacking vs. self-citation breakdown provided"
    },
    {
      "index": 15,
      "url": "https://arxiv.org/abs/2202.11360",
      "title": "GLAD: Deep Graph Learning for Anomalous Citation Detection",
      "summary": "GNN-based paper-level citation anomaly detection with CPU algorithm for citation purpose; different granularity and method from journal-level Hodge flow decomposition"
    },
    {
      "index": 16,
      "url": "https://arxiv.org/abs/2005.14343",
      "title": "Unsupervised Anomaly Detection in Journal-Level Citation Networks (JCDL 2020)",
      "summary": "Unsupervised journal-level citation anomaly detection; no Hodge decomposition; no labeled JCR ground truth; earlier related work in the same domain"
    }
  ],
  "follow_up_questions": [
    "Can the CIDRE edge-table-2013.csv and journal_names.csv files be cross-referenced with OpenAlex journal IDs to map which confirmed stacking journals from 2018-2025 were already visible as anomalous in the 2013 MAG snapshot, establishing whether the Hodge curl signal is detectable in pre-suppression citation data?",
    "For the 2019 JCR suppressed journals (17 total, stacking names unknown): the CIDRE paper references 46 donor-recipient stacking pairs and 22 merged groups (J1-J22) up to 2019 — are the specific journal names in those groups available in the CIDRE GitHub data files or in the full JCR platform, which could resolve the 2019 identification gap?",
    "The CDFD paper (arXiv:2506.12546) captures ALL circular flows including cycles longer than triangles while HodgeRank curl is restricted to triangular cycles — should both metrics be computed on the same stacking-labeled journal set to empirically determine whether longer-cycle circularity is more discriminative than triangular Hodge curl for detecting citation cartels?"
  ]
}
```

### [143] TOOL CALL — Bash · 2026-07-09 01:06:16 UTC

```
Validate research_out.json structure:
python3 -c "
import json
with open('/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_2/gen_art/gen_art_research_1/research_out.json') as f:
    d = json.load(f)
print('title:', repr(d.get('title','MISSING'))[:80])
print('summary length:', len(d.get('summary','')))
print('answer type:', type(d.get('answer')).__name__)
print('answer length:', len(d.get('answer','')))
print('sources count:', len(d.get('sources',[])))
print('follow_up_questions count:', len(d.get('follow_up_questions',[])))
# Check all required fields
for f in ['title','summary','answer','sources','follow_up_questions']:
    print(f'  {f}: present={f in d}')
# Check sources have required fields
for s in d.get('sources',[]):
    for sf in ['index','url','title','summary']:
        if sf not in s:
            print(f'  source missing field: {sf}')
print('JSON valid: OK')
"
```

### [144] TOOL RESULT — Bash · 2026-07-09 01:06:16 UTC

```
{"stdout": "title: 'HLSAD Methodology, JCR Suppression-Type Annotations, and Concurrent Work Scan'\nsummary length: 1258\nanswer type: str\nanswer length: 11464\nsources count: 16\nfollow_up_questions count: 3\n  title: present=True\n  summary: present=True\n  answer: present=True\n  sources: present=True\n  follow_up_questions: present=True\nJSON valid: OK", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [145] ASSISTANT · 2026-07-09 01:06:20 UTC

```
`research_out.json` is valid — all required fields present, `answer` is a string with 11,464 characters and 16 numbered sources, all source objects have the required `index`, `url`, `title`, and `summary` fields.
```

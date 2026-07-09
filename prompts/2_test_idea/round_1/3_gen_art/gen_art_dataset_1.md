# gen_art_dataset_1 — test_idea

> Phase: `invention_loop` · round 1 · `gen_art`
> Run: `run_io13l_LyCX8s` — Curl in the Citation Graph: Hodge Flow Decomposition Detects Citation Cartels via Field-Aware Calibration
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_dataset_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-07-08 23:22:09 UTC

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
Find, evaluate, and prepare high-quality datasets for the research experiment.
Adapt your search strategy based on the hypothesis and domain requirements.
</task>

<common_mistakes_to_avoid>
Critical pitfalls from past runs. MUST check for and avoid each one.

**1. Picking Obscure or Unusable Datasets**
Do NOT select datasets just because they match a keyword. Red flags: very few downloads (<100), no documentation (dataset card, paper, or GitHub page). Prefer well-used datasets (not necessarily popular or widely known) with clear documentation.
CHECK: >100 downloads? Has documentation? If any "no" → find a better dataset.

**2. Fabricating Dataset Provenance**
Do NOT invent justifications for why a dataset is relevant. If a dataset name contains a number (e.g., "797"), do NOT assume it refers to a specific benchmark suite, OpenML ID, or paper without verification. In past runs, an agent assumed "797" referred to "OpenML benchmark suite 797" with zero evidence, then fabricated a rationale. This was completely false.
CHECK: Can you cite a specific, verifiable source (paper, benchmark page, dataset card) confirming this dataset is what you claim? If not, do not make provenance claims.

**3. Not Verifying Dataset Usefulness**
Always sanity-check that a dataset is actually suitable for the task before committing. Download a sample, inspect the features, and run a quick baseline appropriate for the domain. If the dataset lacks signal or structure for the hypothesis being tested, the entire experiment is wasted.

**4. Settling for the Only Search Result**
If your search returns only 1-2 results, your search terms are too narrow. Broaden your queries, try different keyword combinations, or search for well-known benchmark datasets in the domain. A single obscure result from a narrow query should never be your final choice.
CHECK: Fewer than 5 candidate datasets? Run additional searches with broader or different terms before making a selection.
</common_mistakes_to_avoid>

<critical_requirements>
- Keep final response under 300 characters
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

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_1/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_io13l_LyCX8s/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_dataset_1_idx2
type: dataset
title: Journal Citation Flow Network + JCR Suppression Labels
summary: >-
  Build a directed weighted journal×journal citation network for 2015–2022 from the OpenAlex S3 snapshot (or API), paired
  with binary JCR-suppression labels from Clarivate’s historical suppressed-title lists, producing scipy sparse matrices and
  row-level JSON suitable as direct input to the Hodge decomposition experiment.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  The ideal dataset has: (1) a directed weighted adjacency matrix C[i,j] = aggregate citations from journal i to journal j
  over 2015-2022, covering ≥5,000 distinct journals each with ≥100 citing works in that window; (2) ≥500,000 directed citation
  pairs (i,j) with C[i,j] > 0; (3) net-flow edge weights Y[i,j] = C[i,j] − C[j,i] (antisymmetric, required for HodgeRank input);
  (4) a binary ground-truth label vector over OpenAlex source IDs where label=1 means the journal was suppressed by Clarivate
  JCR for citation stacking or excessive self-citation at any year 2018–2022, with ≥40 positive labels; (5) journal metadata
  (ISSN-L, display name, field/concept, works_count, cited_by_count); (6) a mini subset restricted to the top-500 journals
  by total citation volume for fast prototyping. Output files must validate against the schema: data_out.json (one row per
  directed pair, fields: source_id_i, source_id_j, citation_count_ij, citation_count_ji, net_flow_ij, year_window, label_i,
  label_j), journal_metadata.json ({id, name, issn_l, field, works_count, cited_by_count}), adjacency_matrix.npz (scipy sparse
  CSR), ground_truth_labels.json ({openalex_source_id: 0/1}), and mini_data_out.json (same schema, top-500 journals).
dataset_search_plan: |-
  ## Environment setup

  Install dependencies first:
  ```
  uv pip install requests duckdb boto3 openpyxl rapidfuzz scipy numpy pandas pyarrow
  ```

  Get a free OpenAlex API key at https://openalex.org/api-registration (required since Feb 2025; free, instant). Store as `OPENALEX_API_KEY` env var.

  ---

  ## Stage 1 — Get the journal list from the OpenAlex API (~30 min)

  Query the `sources` endpoint with cursor pagination to get ALL journals with works_count ≥ 100:

  ```python
  import requests, json, time

  API_KEY = os.environ['OPENALEX_API_KEY']
  BASE = 'https://api.openalex.org'

  def get_all_journals(min_works=100):
      journals = []
      params = {
          'filter': 'type:journal',
          'per_page': 200,
          'cursor': '*',
          'select': 'id,display_name,issn_l,issn,works_count,cited_by_count,x_concepts',
          'api_key': API_KEY,
      }
      while True:
          r = requests.get(f'{BASE}/sources', params=params, timeout=30)
          r.raise_for_status()
          data = r.json()
          batch = [j for j in data['results'] if (j.get('works_count') or 0) >= min_works]
          journals.extend(batch)
          cursor = data['meta'].get('next_cursor')
          if not cursor:
              break
          params['cursor'] = cursor
          time.sleep(0.12)  # polite: ~8 req/s
      return journals

  journals = get_all_journals()
  with open('journal_list.json', 'w') as f:
      json.dump(journals, f)
  print(f'Loaded {len(journals)} journals')  # expect 30,000-50,000
  ```

  Build lookup tables:
  - `openalex_id_set`: set of all journal source IDs
  - `issn_to_openalex`: dict mapping issn_l → openalex_id (for ground-truth matching)
  - `name_to_openalex`: dict for fuzzy fallback

  ---

  ## Stage 2 — Build the journal×journal citation matrix (3–4 hours)

  The core challenge: OpenAlex `referenced_works` is a flat list of work IDs (e.g., `https://openalex.org/W2753353163`), NOT source/journal IDs. A join step (work_id → source_id) is mandatory.

  ### Primary path: DuckDB querying OpenAlex Parquet on S3

  OpenAlex Parquet format is available in the June 2026 quarterly release at `s3://openalex/data/parquet/works/` (no credentials; us-east-1). DuckDB’s httpfs extension can query these files directly without a full download.

  **First, verify Parquet availability:**
  ```bash
  aws s3 ls --no-sign-request s3://openalex/data/parquet/works/ --recursive --human-readable | head -20
  ```
  If files are listed → use Parquet path. If not → use JSONL fallback (see below).

  **DuckDB Parquet approach:**
  ```python
  import duckdb, os

  conn = duckdb.connect('citation.duckdb', config={
      'memory_limit': '22GB',
      'threads': 4
  })
  conn.execute('INSTALL httpfs; LOAD httpfs;')
  # Anonymous S3 access for public OpenAlex bucket
  conn.execute("""
      CREATE SECRET IF NOT EXISTS s3anon (
          TYPE S3, REGION 'us-east-1',
          KEY_ID '', SECRET ''
      );
  """)
  conn.execute("SET s3_url_style='path';")

  PARQUET_GLOB = 's3://openalex/data/parquet/works/**/*.parquet'

  # Probe the schema first (critical: verify field paths)
  schema = conn.execute(f"DESCRIBE SELECT * FROM read_parquet('{PARQUET_GLOB}') LIMIT 0").fetchdf()
  print(schema)
  # Adjust field access below based on actual schema.
  # Options for nested struct access in DuckDB:
  #   primary_location['source']['id']  OR  primary_location.source.id
  # Test both: conn.execute("SELECT primary_location['source']['id'] FROM read_parquet(...) LIMIT 5")

  # Pass 1: extract (work_id, source_id, year) for journal papers 2015-2022
  conn.execute("""
      CREATE TABLE IF NOT EXISTS work_sources AS
      SELECT
          id                                         AS work_id,
          publication_year                           AS year,
          primary_location['source']['id']           AS source_id
      FROM read_parquet(?, hive_partitioning := true)
      WHERE publication_year BETWEEN 2015 AND 2022
        AND primary_location['source']['type'] = 'journal'
        AND primary_location['source']['id'] IS NOT NULL
  """, [PARQUET_GLOB])
  conn.execute("COPY work_sources TO 'work_sources.parquet' (FORMAT PARQUET);")
  print('work_sources rows:', conn.execute('SELECT COUNT(*) FROM work_sources').fetchone()[0])

  # Pass 2: extract citation edges (UNNEST referenced_works list)
  # referenced_works is a list<varchar> in Parquet
  conn.execute("""
      CREATE TABLE IF NOT EXISTS citations_raw AS
      SELECT
          id                                         AS citing_work_id,
          primary_location['source']['id']           AS citing_source_id,
          publication_year                           AS year,
          UNNEST(referenced_works)                   AS cited_work_id
      FROM read_parquet(?, hive_partitioning := true)
      WHERE publication_year BETWEEN 2015 AND 2022
        AND primary_location['source']['type'] = 'journal'
        AND primary_location['source']['id'] IS NOT NULL
        AND referenced_works IS NOT NULL
        AND len(referenced_works) > 0
  """, [PARQUET_GLOB])
  print('citations_raw rows:', conn.execute('SELECT COUNT(*) FROM citations_raw').fetchone()[0])

  # Pass 3: join to resolve cited_work_id → cited_source_id
  conn.execute("""
      CREATE TABLE IF NOT EXISTS journal_citations AS
      SELECT
          c.citing_source_id,
          ws.source_id    AS cited_source_id,
          c.year,
          COUNT(*)        AS n_citations
      FROM citations_raw c
      JOIN work_sources ws ON c.cited_work_id = ws.work_id
      WHERE c.citing_source_id != ws.source_id  -- exclude self-citations (keep as option)
      GROUP BY c.citing_source_id, ws.source_id, c.year
  """)

  # Aggregate to year-window totals
  conn.execute("""
      CREATE TABLE IF NOT EXISTS journal_citations_agg AS
      SELECT citing_source_id, cited_source_id, SUM(n_citations) AS total_citations
      FROM journal_citations
      GROUP BY citing_source_id, cited_source_id
  """)

  df = conn.execute('SELECT * FROM journal_citations_agg').fetchdf()
  print(f'Citation pairs: {len(df)}')
  df.to_parquet('journal_citations_agg.parquet', index=False)
  ```

  ### Fallback path A: Stream JSONL from S3 (if Parquet unavailable)

  If the Parquet path fails, stream JSONL.gz files without downloading them:

  ```python
  import boto3, gzip, json, sqlite3
  from botocore import UNSIGNED
  from botocore.config import Config

  s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED), region_name='us-east-1')

  # Build SQLite for work_id → source_id lookup
  ws_db = sqlite3.connect('work_sources.db')
  ws_db.execute('CREATE TABLE IF NOT EXISTS ws (wid TEXT PRIMARY KEY, sid TEXT)')
  ws_db.execute('CREATE TABLE IF NOT EXISTS refs (citing TEXT, cited TEXT)')
  ws_db.execute('PRAGMA synchronous = OFF; PRAGMA journal_mode = WAL;')

  # List all works JSONL part files
  paginator = s3.get_paginator('list_objects_v2')
  batch_rows, COMMIT_EVERY = [], 50000

  for page in paginator.paginate(Bucket='openalex', Prefix='data/jsonl/works/'):
      for obj in page.get('Contents', []):
          key = obj['Key']
          if not key.endswith('.gz'):
              continue
          stream = s3.get_object(Bucket='openalex', Key=key)['Body']
          with gzip.GzipFile(fileobj=stream) as fh:
              for line in fh:
                  w = json.loads(line)
                  year = w.get('publication_year')
                  if not (year and 2015 <= year <= 2022):
                      continue
                  loc = (w.get('primary_location') or {})
                  src = (loc.get('source') or {})
                  if src.get('type') != 'journal' or not src.get('id'):
                      continue
                  wid = w['id']
                  sid = src['id']
                  ws_db.execute('INSERT OR IGNORE INTO ws VALUES (?,?)', (wid, sid))
                  for ref in (w.get('referenced_works') or []):
                      ws_db.execute('INSERT INTO refs VALUES (?,?)', (wid, ref))
          ws_db.commit()

  # Join refs → citing_source, cited_source
  cursor = ws_db.execute("""
      SELECT ws1.sid AS citing_source, ws2.sid AS cited_source, COUNT(*) AS n
      FROM refs r
      JOIN ws ws1 ON r.citing = ws1.wid
      JOIN ws ws2 ON r.cited  = ws2.wid
      GROUP BY ws1.sid, ws2.sid
  """)
  result_rows = cursor.fetchall()
  ```

  ### Fallback path B: OpenAlex API batch resolution (if S3 is inaccessible)

  If both S3 paths fail (unlikely), use the API:
  ```python
  # For each of top-5000 journals by cited_by_count,
  # paginate through works (select=id,referenced_works),
  # collect all unique referenced_works IDs,
  # batch-resolve them in groups of 100:
  def batch_resolve_works(work_ids, api_key, batch_size=100):
      source_map = {}
      for i in range(0, len(work_ids), batch_size):
          batch = work_ids[i:i+batch_size]
          # Strip URL prefix to get W-IDs
          pipe = '|'.join(wid.split('/')[-1] for wid in batch)
          url = f'{BASE}/works'
          r = requests.get(url, params={
              'filter': f'openalex:{pipe}',
              'select': 'id,primary_location',
              'per_page': 100,
              'api_key': api_key,
          }, timeout=30)
          for w in r.json().get('results', []):
              src = ((w.get('primary_location') or {}).get('source') or {})
              if src.get('id'):
                  source_map[w['id']] = src['id']
          time.sleep(0.12)  # ~8 req/s
      return source_map
  ```

  Monitor progress hourly: if fewer than 2M citation pairs resolved by hour 3, switch to a lower-coverage fallback (top-2,000 journals only) to still hit the 6-hour deadline.

  ---

  ## Stage 3 — Compile JCR suppression ground truth (~30–60 min)

  Target: a dict `{openalex_source_id: 1}` for all journals suppressed 2018–2022.

  ### Source A: Clarivate Excel files (try first)

  Clarivate hosts public Excel files at predictable URLs. Try in order:
  ```python
  import requests, openpyxl, io

  URLS = [
      'https://jcr.help.clarivate.com/Content/Resources/Docs/Suppressed-titles-2019-2007.xlsx',
      'https://help.incites.clarivate.com/incitesLiveJCR/JCRGroup/Resources/Docs/Suppressed-titles-2019-2007.xlsx',
      # try year ranges that might exist for 2020+:
      'https://jcr.help.clarivate.com/Content/Resources/Docs/Suppressed-titles-2022-2020.xlsx',
      'https://jcr.help.clarivate.com/Content/Resources/Docs/Suppressed-titles-2022-2007.xlsx',
  ]

  for url in URLS:
      r = requests.get(url, timeout=30, headers={'User-Agent': 'Mozilla/5.0'})
      if r.status_code == 200 and r.headers.get('content-type','').startswith('application/'):
          wb = openpyxl.load_workbook(io.BytesIO(r.content))
          ws = wb.active
          # Columns typically: Journal Name, ISSN, Suppression Year, Reason, JIF Numerator %
          for row in ws.iter_rows(min_row=2, values_only=True):
              name, issn, year, reason = row[0], row[1], row[2], row[3]
              if year and 2018 <= int(year) <= 2022:
                  suppressed.append({'name': name, 'issn': issn, 'year': year, 'reason': reason})
  ```

  ### Source B: Scrape Clarivate suppression HTML pages

  ```python
  from bs4 import BeautifulSoup

  for url in [
      'https://help.incites.clarivate.com/incitesLiveJCR/JCRGroup/titleSuppressions.html',
      'https://jcr.help.clarivate.com/Content/title-suppressions.htm',
  ]:
      r = requests.get(url, timeout=30)
      if r.ok:
          soup = BeautifulSoup(r.text, 'html.parser')
          for table in soup.find_all('table'):
              # Extract rows with journal names and ISSNs
              ...
  ```

  ### Source C: Retraction Watch articles (names only)

  Collect journal names from Retraction Watch annual suppression articles:
  - 2024 (17 journals): `https://retractionwatch.com/2024/06/27/seventeen-journals-lose-impact-factors-for-suspected-citation-manipulation/`
  - 2025 (20 journals): `https://retractionwatch.com/2025/06/18/clarivate-impact-factor-suppression-list-2025-self-citation-stacking/`
  - Search for 2020, 2021, 2022 years similarly

  For journals where only names are available (no ISSN), fuzzy-match against the OpenAlex journal list.

  ### Source D: Academic paper supplementary data

  The paper "A bibliometric investigation of journals repeatedly suppressed from JCR" (Accountability in Research, DOI 10.1080/08989621.2022.2071154) covers 18 journals suppressed ≥3 times through ~2021. Fetch it for supplementary tables.

  ### Matching suppressed journals to OpenAlex IDs

  ```python
  from rapidfuzz import fuzz

  # Build ISSN lookup: normalize ISSNs (remove hyphens, check both issn and issn_l)
  issn_to_id = {}
  for j in journals:
      if j.get('issn_l'):
          issn_to_id[j['issn_l'].replace('-', '')] = j['id']
      for issn in (j.get('issn') or []):
          issn_to_id[issn.replace('-', '')] = j['id']

  resolved = {}
  for s in suppressed:
      # Try ISSN match first
      issn_key = (s.get('issn') or '').replace('-', '')
      if issn_key in issn_to_id:
          resolved[issn_to_id[issn_key]] = 1
          continue
      # Fuzzy name match as fallback
      best_id, best_score = None, 0
      for j in journals:
          score = fuzz.token_sort_ratio(s['name'].lower(), j['display_name'].lower())
          if score > best_score:
              best_score, best_id = score, j['id']
      if best_score >= 85:
          resolved[best_id] = 1
          print(f"Fuzzy match ({best_score}): {s['name']} -> {j['display_name']}")
      else:
          print(f"UNMATCHED: {s['name']} (best score: {best_score})")

  print(f'Suppressed journals matched: {len(resolved)} / {len(suppressed)}')
  ```

  Expected: ~60–70 unique suppressed journals 2018–2022; target ≥40 matched to OpenAlex IDs. Document any unmatched journals as limitations in a `match_report.txt`.

  ---

  ## Stage 4 — Assemble outputs (~30 min)

  ```python
  import scipy.sparse as sp, numpy as np, json, pandas as pd

  # Load citation pairs from Stage 2
  df = pd.read_parquet('journal_citations_agg.parquet')  # citing_source_id, cited_source_id, total_citations

  # Filter to journals with >=100 citing works
  # (already filtered in Stage 2, but reconfirm)

  # Build symmetric count matrix for both directions
  # C_ij = total_citations from journal i to journal j
  all_ids = sorted(set(df['citing_source_id']) | set(df['cited_source_id']))
  id2idx = {sid: i for i, sid in enumerate(all_ids)}
  N = len(all_ids)

  rows = df['citing_source_id'].map(id2idx).values
  cols = df['cited_source_id'].map(id2idx).values
  data = df['total_citations'].values
  C = sp.csr_matrix((data, (rows, cols)), shape=(N, N))
  sp.save_npz('adjacency_matrix.npz', C)

  # Ground truth labels (0 for all, then overwrite 1 for suppressed)
  ground_truth = {sid: 0 for sid in all_ids}
  ground_truth.update(resolved)  # resolved = {openalex_id: 1} from Stage 3
  json.dump(ground_truth, open('ground_truth_labels.json', 'w'), indent=2)

  # Build data_out.json rows: one per directed pair (i, j) where C[i,j] > 0
  coo = C.tocoo()
  output_rows = []
  for i, j, v in zip(coo.row, coo.col, coo.data):
      i_id = all_ids[i]
      j_id = all_ids[j]
      cij = int(v)
      cji = int(C[j, i])
      output_rows.append({
          'source_id_i': i_id,
          'source_id_j': j_id,
          'citation_count_ij': cij,
          'citation_count_ji': cji,
          'net_flow_ij': cij - cji,
          'year_window': '2015-2022',
          'label_i': int(ground_truth.get(i_id, 0)),
          'label_j': int(ground_truth.get(j_id, 0))
      })
  json.dump(output_rows, open('data_out.json', 'w'))
  print(f'data_out.json: {len(output_rows)} rows')

  # Journal metadata
  jid_set = set(all_ids)
  jmeta = [
      {
          'id': j['id'],
          'name': j['display_name'],
          'issn_l': j.get('issn_l'),
          'field': (j.get('x_concepts') or [{}])[0].get('display_name', ''),
          'works_count': j.get('works_count', 0),
          'cited_by_count': j.get('cited_by_count', 0)
      }
      for j in journals
      if j['id'] in jid_set
  ]
  json.dump(jmeta, open('journal_metadata.json', 'w'), indent=2)

  # Mini subset: top-500 journals by total citation volume
  total_vol = np.array(C.sum(axis=0) + C.sum(axis=1).T).flatten()
  top500_idx = set(np.argsort(total_vol)[-500:].tolist())
  top500_ids = set(all_ids[i] for i in top500_idx)
  mini_rows = [
      row for row in output_rows
      if row['source_id_i'] in top500_ids and row['source_id_j'] in top500_ids
  ]
  json.dump(mini_rows, open('mini_data_out.json', 'w'))
  print(f'mini_data_out.json: {len(mini_rows)} rows')
  ```

  ---

  ## Stage 5 — Validation

  Run these checks and ABORT with a clear error if any fail:

  ```python
  # Load
  rows = json.load(open('data_out.json'))
  meta = json.load(open('journal_metadata.json'))
  gt = json.load(open('ground_truth_labels.json'))
  C2 = sp.load_npz('adjacency_matrix.npz')

  meta_ids = {j['id'] for j in meta}
  assert len(rows) >= 500_000, f'Too few citation pairs: {len(rows)}'
  assert len(meta_ids) >= 5_000, f'Too few journals: {len(meta_ids)}'

  positives = sum(1 for sid, lbl in gt.items() if lbl == 1)
  assert positives >= 30, f'Too few suppressed journals: {positives}'

  for row in rows[:1000]:  # spot-check
      assert row['source_id_i'] in meta_ids
      assert row['source_id_j'] in meta_ids
      assert row['net_flow_ij'] == row['citation_count_ij'] - row['citation_count_ji']
      assert row['label_i'] == gt.get(row['source_id_i'], 0)
      assert row['label_j'] == gt.get(row['source_id_j'], 0)

  assert C2.shape[0] >= 5_000
  print('All validation checks passed.')
  print(f'Journals: {len(meta_ids)}, Pairs: {len(rows)}, Suppressed: {positives}')
  ```

  Also run the aii-json skill to generate mini and preview variants.

  ---

  ## Failure scenarios and mitigations

  **OpenAlex Parquet schema mismatch**: Test with `DESCRIBE SELECT * FROM read_parquet(...) LIMIT 0` before running full queries. If nested struct access fails, try alternative DuckDB syntax: `primary_location.source.id` vs `primary_location['source']['id']`. Also try reading a single file first to debug schema.

  **S3 streaming too slow**: Monitor elapsed time. If <40% complete after 3 hours on S3 JSONL streaming, kill the process and switch to Fallback Path B (API). A 5,000-journal network is achievable in ~4 hours via API with batch resolution.

  **DuckDB OOM on join**: If the join step (citations_raw × work_sources) hits memory limits, process in chunks: partition citations_raw by citing_source_id alphabetical prefix, join each chunk, write to parquet, then UNION ALL at the end.

  **Clarivate suppression lists blocked (403)**: Use Sources C and D. The minimum viable ground truth is ~30 positive labels; below this, document and warn in output metadata. Supplement with the CIDRE paper’s validation set if authors published their suppressed journal list.

  **Very few suppressed journals (<30 matched)**: Lower fuzzy matching threshold to 80. Also try searching OpenAlex for the exact journal name. Accept that some journals may have been renamed or discontinued and can’t be matched; document these cases.

  **year_window granularity**: The artifact direction asks for 2015–2022 aggregate. If there’s time, also output per-year citation counts in a supplementary `yearly_citations.parquet` for temporal Hodge analysis. This is optional.

  ---

  ## Implementation notes

  1. **referenced_works is work-IDs only** (‘https://openalex.org/W2753353163’) — NOT source/journal IDs. The join step (Step 2, Pass 3) is non-negotiable.

  2. **ISSN-L matching priority**: Clarivate suppression lists use ISSN-L (linking ISSN). OpenAlex stores `issn_l` separately from `issn` (list of all ISSNs). Always check `issn_l` first, then fall back to `issn` list membership.

  3. **Self-citations**: By default, exclude self-loops (i == j) from data_out.json but include self-citation counts in journal_metadata.json as a separate field. Self-citations are a JCR suppression criterion and diagnostically useful.

  4. **DuckDB httpfs anonymous S3**: The OpenAlex S3 bucket is fully public. Use `CREATE SECRET (TYPE S3, REGION 'us-east-1', KEY_ID '', SECRET '');` or `SET s3_access_key_id = '';` to avoid credential errors.

  5. **Parquet UNNEST of referenced_works**: In OpenAlex Parquet, `referenced_works` is a `list<varchar>` column. DuckDB’s `UNNEST(referenced_works)` in the SELECT clause creates one row per element. This produces a large intermediate table (potentially 1B+ rows); write to disk parquet immediately rather than keeping in memory.

  6. **Journal type filter strictness**: Use `primary_location.source.type = 'journal'` to exclude preprint servers (bioRxiv, arXiv), book series, conference proceedings. This is critical for a clean journal-level network.

  7. **Parquet hive partitioning**: OpenAlex Parquet files may be hive-partitioned by `updated_date`. Set `hive_partitioning := true` in `read_parquet()` and DuckDB will use the partition predicates for pushdown if filtering by updated_date. Note: there is no `publication_year` partition, so all partitions must be scanned for year filtering.

  8. **Output file sizes**: data_out.json for 500K+ rows may be 200–500 MB. After writing, run the aii-file-size-limit skill to check if splitting is needed. The mini_data_out.json (top-500 journals) should be <10 MB and is the primary fast-access file.
target_num_datasets: 1
</artifact_plan>



<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>

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
</available_resources>

<available_data_sources>
Use the sources appropriate to your task. Read the relevant skill file BEFORE using each source.

- **HuggingFace Hub** (HF) — ML datasets (NLP, vision, tabular, benchmarks)
- **Our World in Data** (OWID) — Global statistics (energy, health, economics, environment, demographics)
- **Alternate methods** — Python/shell (sklearn.datasets, openml, direct URL, APIs, etc.)

If the plan specifies a source or one fits better, use it.
You may combine sources. Use web search (aii-web-tools skill) to research candidates (background, papers, provenance) — NOT to find/download datasets.
</available_data_sources>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. Use it for dataset selection, evaluation metrics, agent orchestration patterns.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-python, aii-long-running-tasks, aii-json, aii-file-size-limit, aii-use-hardware, aii-parallel-computing.
TODO 2. Read skill files for your data sources (see <available_data_sources>) and domain handbook if applicable (see <available_domain_handbooks>). Based on plan and context, decide which source(s) to use. Include everything specified in the artifact plan, but you may also collect additional relevant data beyond what's listed. Run 8 diverse searches across chosen source(s) — BROAD, GENERAL terms, not very specific. Parallelize where supported.
TODO 3. Identify the 4 most promising datasets. IMPORTANT: Only consider datasets under 300MB. Preview/inspect sample rows for each candidate. Parallelize previews.
TODO 4. Research each candidate BEFORE choosing which to download. For each, search the web (aii-web-tools skill): dataset name, papers citing it, original source/task, popularity. Red flags: no search results, no papers, anonymized features (F1, F2...), <100 downloads, no documentation. Green flags: papers using it, clear documentation, meaningful features, established benchmark. Also consider: will features/structure allow meaningful evaluation of the planned method?
TODO 5. Decide which to KEEP vs DISCARD. Look for: clear structure, relevant fields, quality examples matching requirements, confirmed provenance. Determine which 2 datasets have the most suitable data. Download and save to `temp/datasets/`. Parallelize downloads.
</todos>
````

### [2] HUMAN-USER prompt · 2026-07-08 23:22:09 UTC

```
Propose a simple, novel graph-based method for detecting citation patterns in academic networks and validate it.
```

### [3] SKILL-INPUT — aii-python · 2026-07-08 23:22:45 UTC

The agent loaded the **aii-python** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-python
description: Python coding standards for experiment and evaluation scripts. Covers environment setup, logging, error handling, and code structure.
---

## Environment Setup

- Python 3.12+
- **NEVER use `pip` or `.venv/bin/pip`** — they are not installed. Use `uv` for ALL package operations:
  ```bash
  uv venv .venv --python=3.12
  source .venv/bin/activate  # or: .venv/bin/python script.py
  uv pip install pandas loguru  # NOT: pip install
  ```
- Create `.toml` file with dependencies, create uv `.venv` and activate it
- NO inline dependencies (no `# /// script` headers)

## Logging

Use `loguru` for all logging. Add a file sink alongside stdout.

```python
from loguru import logger
import sys

logger.remove()  # Remove default handler
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")
```

Rules:
- Log every major step (data loading, processing start/end, results)
- If applicable, log every LLM API call input and output
- Truncate long outputs in logs (add truncation logic for potentially large strings)
- Use `logger.error()` in except blocks (traceback auto-captured)

## Error Handling

- Wrap major operations in try/except blocks
- Use `@logger.catch(reraise=True)` decorator on main functions — without `reraise=True`, the script exits 0 even on uncaught exceptions, hiding failures from downstream consumers
- Use explicit exception types, not bare `except:`
- Never silently swallow exceptions — always log them

```python
@logger.catch(reraise=True)
def main():
    try:
        data = load_data(path)
    except FileNotFoundError:
        logger.error("Data file not found")
        raise
    except json.JSONDecodeError:
        logger.error("Invalid JSON in data file")
        raise
```

## Code Structure

- Use `pathlib.Path` for file operations: `Path("data/input.json").read_text()` not `open(...).read()`
- Use type hints for function signatures
- Use keyword arguments for functions with more than 4 parameters
- No hardcoded paths — derive from script location or accept as arguments

## Script Pattern

Standard pattern for experiment/evaluation scripts:

```python
#!/usr/bin/env python3
"""Brief description of what this script does."""

from loguru import logger
from pathlib import Path
import json
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    # Load data
    data_path = Path("full_data_out.json")
    logger.info(f"Loading data from {data_path}")
    data = json.loads(data_path.read_text())
    logger.info(f"Loaded {len(data['examples'])} examples")

    # Process
    results = []
    for i, example in enumerate(data["examples"]):
        try:
            result = process(example)
            results.append(result)
        except Exception:
            logger.error(f"Failed on example {i}")
            continue

    # Save output
    output = {"examples": results}
    Path("method_out.json").write_text(json.dumps(output, indent=2))
    logger.info(f"Saved {len(results)} results")

if __name__ == "__main__":
    main()
```
````

### [4] SKILL-INPUT — aii-long-running-tasks · 2026-07-08 23:22:45 UTC

The agent loaded the **aii-long-running-tasks** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-long-running-tasks
description: Gradual scaling pattern for long-running autonomous tasks. Use when running experiments, evaluations, or any code that processes data at increasing scale with runtime checks.
---

## Core Principles

1. **Time budget first**: Read your time/runtime constraints before running anything. Set every Bash timeout to fit within the budget.
2. **Start small, scale up**: Run on minimal input first, fix errors, then increase scale.
3. **Extrapolate before scaling**: Use recorded runtimes to predict whether the next step fits in the budget. Don't guess — calculate.
4. **Background execution**: For anything that takes >1 min, run in background (`run_in_background=true`) and do useful work while waiting.
5. **Stop early if needed**: Quality results on less data beats a timeout or crash. It's always acceptable to stop at a smaller scale.

---

## Gradual Scaling Sequence

Run code at increasing data sizes, checking runtime at each step.

Substitute your actual file names:
- `{mini_file}` — mini JSON (3 examples) from dependency workspace
- `{full_file}` — full dataset from dependency workspace
- `{script}` — your processing script (e.g., `./method.py`, `./eval.py`)
- `{schema}` — JSON schema to validate output against

**STEP 1 — MINI DATA:** Run `{script}` on `{mini_file}`. Do NOT truncate logs. Fix all errors. Validate output against `{schema}`. Verify you are NOT using mock scripts, mock data, or mock APIs.

**STEP 2 — 10 EXAMPLES:** Modify `{script}` to load only the first 10 examples from `{full_file}`. Run and fix errors. Validate schema. Record the runtime.

**STEP 3 — 50 EXAMPLES:** Load first 50 examples from `{full_file}`. Run and fix errors. Record runtime. **EXTRAPOLATE**: Using runtimes from steps 2-3, estimate time per example. Calculate how many examples fit in your remaining time budget. If 50 already used most of the budget, stop here.

**STEP 4 — 100 EXAMPLES (if budget allows):** Load first 100 examples. Run and fix errors. Record runtime. Re-extrapolate with the new data point.

**STEP 5 — 200 EXAMPLES (if budget allows):** Load first 200 examples from `{full_file}`. Run and fix errors. Record runtime.

**STEP 6 — MAXIMIZE:** Using all recorded runtimes, extrapolate time-per-example (it may not be perfectly linear — account for overhead). Calculate the maximum number of examples that fits within your remaining time budget with a 10% safety margin. Load that many (or all if they fit). Run and validate.

## Final Testing Phase

After completing the scaling sequence, redo the entire sequence **one more time** up to your final example count:

mini → 10 → 50 → 100 → 200 → max

At each scale: look for issues, fix problems, validate output, ensure it completes within time limits.

---

## Background Execution

For any step that takes >1 min, run as a **background task**:

1. Launch with Bash `run_in_background=true`
2. While it runs, use the time productively:
   - Sanity-check previous outputs
   - Verify file integrity (correct field names, non-empty values)
   - Review code for edge cases at larger scale
   - Prepare the next step
3. Check back on the background task to get results
4. If it failed, fix errors and re-run

---

## Resource Limits

Set hard RAM and CPU time limits so code fails fast instead of crashing the system. Read limits from `<hardware>` and leave headroom for the OS (e.g., if 16GB total, cap at 14GB).

Python example using stdlib `resource` module:
```python
import resource
resource.setrlimit(resource.RLIMIT_AS, (14 * 1024**3, 14 * 1024**3))  # 14GB RAM
resource.setrlimit(resource.RLIMIT_CPU, (3600, 3600))  # 1 hour CPU time
```
Exceeding RAM raises `MemoryError`. Exceeding CPU time sends `SIGKILL`.

## Monitoring

At each step, record runtime AND check resource usage (`free -h` for RAM, `top -bn1 | head -5` for CPU). If memory usage is climbing toward the limit or CPU is pegged, stop and investigate before scaling further.
````

### [5] SKILL-INPUT — aii-use-hardware · 2026-07-08 23:22:45 UTC

The agent loaded the **aii-use-hardware** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-use-hardware
description: Detect hardware and use it responsibly. Covers CPU/RAM/GPU detection, memory-safe data processing, and resource-aware computation.
---

**Step 1** — Run `bash scripts/get_hardware.sh` (relative to this skill's directory).

Read the `=== CGROUP ===` section carefully. If `Type: cgroup v1` or `cgroup v2`:
- You are in a **container with hard resource limits**. Exceeding them = OOM kill, no recovery.
- **Never** use `psutil.virtual_memory().total`, `free -h`, `/proc/meminfo`, `os.cpu_count()`, or `nproc` for resource limits — these report **host** values, not your container's allocation.
- **Always** read limits from the cgroup paths shown in the output, or use the Python helpers below.
- For **runtime memory monitoring**, read current usage from cgroup too:
  - v2: `/sys/fs/cgroup/memory.current`
  - v1: `/sys/fs/cgroup/memory/memory.usage_in_bytes`

**Step 2** — Use Step 1 results to pick package variants **before** installing.

Defaults often target the most powerful environment — PyPI's `torch` ships with CUDA libs even on CPU-only hosts. Wrong variant = wasted disk, slow setup, possible import-time failures.

If `=== GPU ===` shows `No GPU`, install torch's CPU build (skips ~4.5GB of CUDA libs):
```bash
uv pip install torch --extra-index-url https://download.pytorch.org/whl/cpu
```
Same idea for any library whose wheel selection depends on detected hardware (GPU/CPU-only builds, architecture-specific wheels).

After install, sanity-check imports right away (`python -c "import torch"`). Disk-pressure or interrupted installs leave half-built wheels (e.g. `libtorch_global_deps.so` missing) — catch these before the experiment runs.

**Step 3** — Set Python constants from the Step 1 results:
```python
import os, math, torch, psutil
from pathlib import Path

def _detect_cpus() -> int:
    """Detect actual CPU allocation (containers/pods/bare metal)."""
    try:  # cgroups v2 quota
        parts = Path("/sys/fs/cgroup/cpu.max").read_text().split()
        if parts[0] != "max":
            return math.ceil(int(parts[0]) / int(parts[1]))
    except (FileNotFoundError, ValueError): pass
    try:  # cgroups v1 quota
        q = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_quota_us").read_text())
        p = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_period_us").read_text())
        if q > 0:
            return math.ceil(q / p)
    except (FileNotFoundError, ValueError): pass
    try:  # CPU affinity (cpuset — used by RunPod, Docker --cpuset-cpus)
        return len(os.sched_getaffinity(0))
    except (AttributeError, OSError): pass
    return os.cpu_count() or 1

def _container_ram_gb() -> float | None:
    """Read RAM limit from cgroup (containers/pods)."""
    for p in ["/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory/memory.limit_in_bytes"]:
        try:
            v = Path(p).read_text().strip()
            if v != "max" and int(v) < 1_000_000_000_000:
                return int(v) / 1e9
        except (FileNotFoundError, ValueError): pass
    return None

NUM_CPUS = _detect_cpus()
HAS_GPU = torch.cuda.is_available()
VRAM_GB = torch.cuda.get_device_properties(0).total_mem / 1e9 if HAS_GPU else 0
DEVICE = torch.device("cuda" if HAS_GPU else "cpu")
TOTAL_RAM_GB = _container_ram_gb() or psutil.virtual_memory().total / 1e9
AVAILABLE_RAM_GB = min(psutil.virtual_memory().available / 1e9, TOTAL_RAM_GB)
```

## Step 4 — Set Memory Limits

OOM kills the entire container. **Every script MUST set RAM and VRAM limits at startup.**

Decide the budget based on what the script actually needs. Estimate data size × 2-5x for in-memory overhead, then add ~50% breathing room for temporaries. You may use up to 90% of available RAM/VRAM, but **scale gradually** — start small (e.g. 30-50%), verify it works, then increase toward the limit. Never exceed 90% to keep a buffer for the OS, system processes, and the agent runtime itself. Going over crashes the container/machine with no recovery.

```python
import resource, psutil

_avail = psutil.virtual_memory().available
RAM_BUDGET = ???  # YOU decide: estimate what this script needs (in bytes)
assert RAM_BUDGET < _avail, f"Budget {RAM_BUDGET/1e9:.1f}GB > available {_avail/1e9:.1f}GB"
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))  # 3x: virtual > RSS; raises MemoryError on exceed

if HAS_GPU:
    _free, _total = torch.cuda.mem_get_info(0)
    VRAM_BUDGET = ???  # YOU decide: estimate GPU memory needs
    torch.cuda.set_per_process_memory_fraction(min(VRAM_BUDGET / _total, 0.95))  # raises OutOfMemoryError on exceed
```

## Memory-Safe Data Processing

- **One at a time**: load one large object → process → `del obj; gc.collect()` → next
- **Load only what you need**: select specific tables/columns/rows, not entire databases
- **Test small first**: run on a sample before scaling to full data to estimate memory/time
- **Free intermediates in loops**: don't accumulate large results — aggregate incrementally
- **Size before loading**: check file/dataset size before loading; if it's >30% of `RAM_BUDGET`, chunk it

## Common Mistakes (from real crashes)

- **Skipping this skill entirely** — loading data with no RAM detection, no limits, no budget. Container OOM-killed, all agents lost.
- **Using `psutil.virtual_memory().total` instead of `_container_ram_gb()`** — reports host RAM (e.g. 66 GB) when container limit is 28 GB. You MUST use the cgroup-aware functions above.
- **Loading all tables from a multi-table database at once** — one agent loaded 14 RelBench tables simultaneously, spiked past container limit.
- **Setting no memory limits** — without `resource.setrlimit` (RAM) and `set_per_process_memory_fraction` (VRAM), a runaway script OOM-kills the container instead of raising a catchable error.
- **Using `os.cpu_count()` directly** — returns host CPUs (e.g. 192) instead of container limit (e.g. 4) on RunPod/Docker. Always use `_detect_cpus()` above which checks cgroup quota → CPU affinity → `os.cpu_count()` in order.

## Hardware Use

- Keep these results in mind for ALL subsequent tasks — don't assume more than detected
- GPU if available and parallelizable, multiprocessing if multiple CPUs
- Push available resources to their full potential — don't leave hardware idle
````

### [6] SKILL-INPUT — aii-json · 2026-07-08 23:22:51 UTC

The agent loaded the **aii-json** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-json
description: JSON validation and formatting toolkit. Validate JSON files against schemas for experiment pipelines, and generate full/mini/preview versions of JSON datasets. Use for validating pipeline outputs, checking schema compliance, or creating size-optimized JSON variants.
---

## Contents

- Validating JSON (schema validation against experiment schemas)
- Formatting JSON (generate full/mini/preview versions)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Validating JSON

Validate JSON files against predefined schemas for experiment-based hypothesis selection, data collection, solution generation, and evaluation.

### Quick Start

1. Read the schema spec you need to adhere to (e.g., `schemas/exp_eval_sol_out.json`)
2. Create your output file following that schema structure
3. Validate:

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /path/to/eval_out.json
```

### Script: aii_json_validate_schema.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /tmp/eval_out.json
```

**Parallel execution (multiple validations):**

IMPORTANT: When validating multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_validate_schema.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --format {1} --file {2}' ::: 'exp_sel_data_out' 'exp_gen_sol_out' 'exp_eval_sol_out' :::+ '/tmp/full_data_out.json' '/tmp/method_out.json' '/tmp/eval_out.json'
```

**Example output (success):**
```
Validating: aii_json_validate_schema.py
Format: exp_eval_sol_out

✓ Validation PASSED
```

**Example output (failure):**
```
Validating: aii_json_validate_schema.py
Format: exp_sel_data_out

✗ Validation FAILED

Errors:
  Path: datasets → 0 → examples → 0
  Error: 'output' is a required property
  Validator: required
```

**Parameters:**

`--format` (required)
- Format type to validate against
- Determines which schema to use

`--file` (required)
- Path to JSON file to validate
- Must be valid JSON
- **Always pass an absolute path.** Relative paths resolve from the
  ability server's CWD (typically ``/ai-inventor/aii_server``), not from
  your agent workspace, so ``data_out/x.json`` will silently look in the
  wrong directory and fail with "Could not load JSON file". The validate
  endpoint also accepts a ``workspace_dir`` arg if you need to keep a
  relative path — pass your workspace path there.

**Tips:**
- Fix errors in your JSON and rerun validation until it passes

### Schema Files

Schemas are stored in `.claude/skills/aii-json/schemas/`:

**Hypothesis Selection & Evaluation:**
- `sel_hypo_out.json` - Hypothesis Selection output (all hypotheses with selected flags)
- `feasibility_eval_all.json` - All hypotheses with feasibility scores
- `feasibility_eval_top.json` - Top 5 most feasible hypotheses
- `novelty_research_one.json` - Single hypothesis novelty research arguments with citations
- `novelty_eval_all.json` - All hypotheses with novelty scores
- `novelty_eval_top.json` - Single best selected hypothesis

**Experiment Pipeline:**
- `exp_sel_data_out.json` - Experiment Data Selection format
- `exp_gen_sol_out.json` - Experiment Solution Generation format
- `exp_eval_sol_out.json` - Experiment Solution Evaluation format

---

## Formatting JSON

Generate three size-optimized versions of a JSON file for efficient development and preview:
- **full**: Identical to original (all data)
- **mini**: First 3 items only (for quick testing)
- **preview**: Mini + all strings truncated to 200 chars (for quick inspection)

### Quick Start

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

### Script: aii_json_format_mini_preview.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

**Parallel execution (multiple files):**

IMPORTANT: When formatting multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_format_mini_preview.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --input {}' ::: 'full_data_out.json' 'method_out.json' 'eval_out.json'
```

**Example output:**
```
Generated 3 versions:
  Full (50 items): /path/to/full_method_out.json
  Mini (3 items): /path/to/mini_method_out.json
  Preview (3 items, truncated): /path/to/preview_method_out.json
```

**Parameters:**

`--input` (required)
- Path to input JSON file
- Must have a top-level array
- Example: `method_out.json`, `full_data_out.json`

`--output-dir` (optional)
- Output directory for generated files
- Default: same directory as input file
- Files are prefixed with `full_`, `mini_`, `preview_`

**Output Files:**

All three files use the same base name with different prefixes:
- `full_{basename}.json` - Complete dataset (identical to original)
- `mini_{basename}.json` - First 3 array items only
- `preview_{basename}.json` - First 3 items with strings truncated to 200 chars

**Tips:**
- Input JSON must have a top-level array structure
- String truncation is recursive (applies to nested objects and arrays)
- Use preview files for quick inspection without reading large datasets
- Use mini files for developing/testing code before running on full dataset

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [7] SKILL-INPUT — aii-file-size-limit · 2026-07-08 23:22:51 UTC

The agent loaded the **aii-file-size-limit** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

```
---
name: aii-file-size-limit
description: File size check procedure for splitting oversized output files. Use after generating JSON output files to check and split files exceeding the provided size limit.
---

## File Size Check

After generating output files, run `ls -lh` to check sizes. If ANY file exceeds the provided file size limit:

1. Create directory with same base name (e.g., `data_out/` for `full_data_out.json`)
2. Split into parts under the limit named: `full_data_out_1.json`, `full_data_out_2.json`, etc.
3. Place parts in directory (e.g., `data_out/full_data_out_1.json`, `data_out/full_data_out_2.json`)
4. Delete the original oversized file
5. Update the script to read from split files: `for f in sorted(glob.glob('data_out/full_data_out_*.json')): data.extend(json.load(open(f)))`
6. For each split part, generate its own mini/preview versions with the json skill's format script
```

### [8] SKILL-INPUT — aii-parallel-computing · 2026-07-08 23:22:51 UTC

The agent loaded the **aii-parallel-computing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-parallel-computing
description: "CRITICAL PERFORMANCE SKILL. Maximize hardware utilization for compute-intensive tasks. Covers GPU acceleration, CPU parallelism, and async I/O. The difference between hours of failure and minutes of success. Use whenever writing ANY script that processes data, makes API calls, or does computation."
---

**ALWAYS parallelize. Sequential processing is unacceptable for any non-trivial workload.** A sequential script doing 1000 API calls takes hours and fails halfway. An async version finishes in minutes with proper error handling. ALWAYS ask: "Can this run in parallel?" — the answer is almost always yes.

Read aii-use-hardware skill first → get `NUM_CPUS`, `HAS_GPU`, `VRAM_GB`, `device`. Set `NUM_WORKERS` proportional to available CPU capacity — check `psutil.cpu_percent(interval=1)` and scale accordingly (e.g. 30% used → use ~70% of cores).

## Decision Tree (follow strictly)

- **I/O-bound** (API calls, downloads, web, file reads) → `asyncio` + `aiohttp` with `Semaphore(NUM_WORKERS * 4)`. NEVER do sequential HTTP requests in a loop.
- **CPU-bound, vectorizable** → GPU available: PyTorch on device / No GPU: NumPy vectorized ops. NEVER loop over array elements in Python.
- **CPU-bound, independent items** → `ProcessPoolExecutor(max_workers=NUM_WORKERS)`. NEVER process items one-by-one when they're independent.
- **Sequential** → only acceptable when items have data dependencies (each depends on the previous result).

## GPU Rules

- Use up to 90% of available VRAM — scale gradually (start small, increase after each successful run, keep 10% buffer)
- Move to device → compute → move back: `torch.tensor(data, device=device)` → `.cpu().numpy()`
- OOM fallback: catch `torch.cuda.OutOfMemoryError` → `empty_cache()` → halve batch size → retry on GPU. Keep reducing until it fits. Stay on GPU.
- Batch large data: chunk it, `del batch` between iterations to free VRAM

## Parallelism Rules

- **CPU-bound**: `ProcessPoolExecutor` + `as_completed`, pre-allocate result list indexed by submission order
- **I/O-bound**: `asyncio` + `aiohttp`, `Semaphore(NUM_WORKERS * 4)`, single shared `ClientSession`, `asyncio.gather(*tasks, return_exceptions=True)`
- Always add `tenacity` retries for transient failures, always set timeouts on HTTP requests
- **CRITICAL — `ProcessPoolExecutor` start method**: Default `fork` deadlocks with loguru (and any threading library). ALWAYS pass `mp_context=multiprocessing.get_context("spawn")` when constructing `ProcessPoolExecutor` in any script that uses loguru, threading, or async I/O. Example:
  ```python
  import multiprocessing as mp
  from concurrent.futures import ProcessPoolExecutor
  with ProcessPoolExecutor(max_workers=N, mp_context=mp.get_context("spawn")) as pool:
      ...
  ```
````

### [9] SKILL-INPUT — aii-hf-datasets · 2026-07-08 23:23:03 UTC

The agent loaded the **aii-hf-datasets** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-hf-datasets
description: Searches, previews, and downloads datasets from HuggingFace Hub. Use when user needs machine learning datasets, training data, HuggingFace datasets, dataset discovery, or .parquet/.json exports.
---

## Contents

- Workflow (3-phase dataset discovery)
- Scripts (Search, Preview, Download)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Workflow: 3-Phase Dataset Discovery

### Phase 1: Search for Datasets
Find datasets with metadata (configs, splits, features, sizes)
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_search_datasets.py --query "sentiment analysis" --limit 5
```

### Phase 2: Preview Dataset (if promising)
Inspect metadata AND sample rows in one call
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_preview_datasets.py openai/gsm8k
```

### Phase 3: Download Dataset (if suitable)
Download after reviewing the preview
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_download_datasets.py openai/gsm8k --config main --split train
```

---

## Scripts

### Search HuggingFace Datasets (aii_hf_search_datasets.py)

Search and discover datasets on HuggingFace Hub.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_search_datasets.py --query "text classification" --limit 5
```

**Parallel execution (multiple queries):**

IMPORTANT: Use full python path with GNU parallel (venv activate does NOT work in parallel subshells):
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_search_datasets.py" && \
parallel -j 10 -k --group --will-cite '$PY $S --query {} --limit 3' ::: 'sentiment' 'classification' 'translation'
```

**Example output:**
```
Found 5 dataset(s) for query='text classification'

============================================================
Dataset 1: stanfordnlp/imdb
Downloads: 2,500,000 | Likes: 1,234
Description: Large Movie Review Dataset for binary sentiment classification...
Tags: text-classification, en, sentiment-analysis
```

**Result fields per dataset:**

Each entry in ``results`` carries:

- ``id`` / ``downloads`` / ``likes`` / ``tags`` / ``description`` — standard
  HF metadata
- ``has_loader_script`` (bool) — repo ships a top-level ``<repo>.py`` loader.
  ``datasets>=3`` won't run these directly; the dataset is reachable only
  via the Datasets Server's pre-converted parquet shards. Treat as a yellow
  flag.
- ``loadable`` (bool) — **prefer datasets where this is ``True``.** Means
  the dataset is reachable via *some* path: either native parquet (no
  script) or HF auto-converted the script's output to parquet. When
  ``False``, the script needs deps HF can't install (e.g. ``conllu``,
  custom audio decoders) and ``aii_hf_datasets__download_datasets`` will
  fail — pick a different candidate.

**Parameters:**

`--query` (optional)
- Search query string
- Example: `--query "sentiment analysis"`

`--limit` (optional)
- Maximum number of results (default: 5)

`--tags` (optional)
- Filter by tags (comma-separated)
- Format: `category:value`
- Examples: `language:en`, `task_categories:text-classification`

`--sort` (optional)
- Sort by field: `downloads`, `likes` (default: downloads)

**Tips:**
- Search displays full dataset metadata
- Use tags to filter: `--tags "language:en,task_categories:translation"`

---

### Preview HuggingFace Dataset (aii_hf_preview_datasets.py)

Inspect a specific dataset - shows metadata AND sample rows.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_preview_datasets.py openai/gsm8k --num-rows 5
```

**Parallel execution (multiple datasets):**

IMPORTANT: Use full python path with GNU parallel:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_preview_datasets.py" && \
parallel -j 10 -k --group --will-cite '$PY $S {} --num-rows 3' ::: 'openai/gsm8k' 'imdb' 'squad'
```

**Example output:**
```
============================================================
Dataset: openai/gsm8k
============================================================
Downloads: 425,109 | Likes: 1,102

Description: GSM8K (Grade School Math 8K) is a dataset of 8.5K high quality
linguistically diverse grade school math word problems...

Configs: main, socratic

--- Sample Rows (train) ---
Columns: question, answer

Row 1:
  question: Natalia sold clips to 48 of her friends in April...
  answer: Natalia sold 48/2 = <<48/2=24>>24 clips in May...
```

**Parameters:**

`dataset_id` (required, positional)
- HuggingFace dataset ID
- Examples: `openai/gsm8k`, `glue`, `imdb`

`--config` (optional)
- Dataset configuration/subset name
- Auto-detects first config if not specified

`--split` (optional)
- Split to preview (default: `train`)

`--num-rows` (optional)
- Number of sample rows (default: 5, max: 20)

**Tips:**
- Use after search to verify data structure
- Streaming mode - doesn't download full dataset

---

### Download HuggingFace Dataset (aii_hf_download_datasets.py)

Download datasets and save to files.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_download_datasets.py openai/gsm8k --config main --split train
```

**Parallel execution (multiple datasets):**

IMPORTANT: Use full python path with GNU parallel. Use `eval {}` pattern when datasets need different flags (e.g. `--config`):
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_download_datasets.py" && \
parallel -j 10 -k --group --will-cite 'eval {}' ::: '$PY $S openai/gsm8k --config main --split train' '$PY $S imdb --split train' '$PY $S squad --split train'
```

**Example output:**
```
Downloaded: openai/gsm8k

  train:
    Rows: 7,473
    Preview: temp/datasets/preview_openai_gsm8k_main_train.json
    Mini: temp/datasets/mini_openai_gsm8k_main_train.json
    Full: temp/datasets/full_openai_gsm8k_main_train.json
```

**Parameters:**

`dataset_id` (required, positional)
- HuggingFace dataset ID
- Examples: `openai/gsm8k`, `imdb`

`--config` (optional)
- Dataset configuration/subset name
- Use preview to see available configs

`--split` (optional)
- Specific split to load (e.g., `train`, `test`)
- If not specified, loads all splits

`--output-dir` (optional)
- Output directory (default: `temp/datasets/`)

**Output files (auto-saved):**
1. **Preview**: `preview_{dataset}_{split}.json` - 3 truncated rows - **READ THIS** for quick inspection
2. **Mini**: `mini_{dataset}_{split}.json` - 3 full rows - for development/testing
3. **Full**: `full_{dataset}_{split}.json` - All rows - **DO NOT READ directly** - use as input path for code

**Tips:**
- Only read preview file directly with Read tool
- Mini and full are input paths for processing code

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [10] SKILL-INPUT — aii-web-tools · 2026-07-08 23:25:57 UTC

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

### [11] SYSTEM-USER prompt · 2026-07-08 23:49:33 UTC

```
continue where you left off — reuse any partial work already written to disk. Do NOT start over.
```

### [12] SYSTEM-USER prompt · 2026-07-09 00:03:12 UTC

````
This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.

Summary:
1. Primary Request and Intent:
   The task is to find, evaluate, and prepare high-quality datasets for a research experiment about detecting citation manipulation patterns in academic journal networks via graph-based methods (specifically Hodge decomposition). The artifact plan requires: a directed weighted journal×journal citation matrix (OpenAlex, 2015-2022), binary JCR suppression labels (Clarivate historical suppressed-title lists), scipy sparse matrices, and row-level JSON outputs.

   Required output files:
   - `data_out.json` — one row per directed (i,j) journal pair where C[i,j]>0, with fields: source_id_i, source_id_j, citation_count_ij, citation_count_ji, net_flow_ij, year_window, label_i, label_j
   - `mini_data_out.json` — same schema, top-500 journals only
   - `journal_metadata.json` — per-journal: id, name, issn_l, field, works_count, cited_by_count
   - `ground_truth_labels.json` — {openalex_source_id: 0/1}
   - `adjacency_matrix.npz` — scipy CSR sparse matrix

   Todos (from original prompt, STRICTLY followed):
   1. ✅ Read skill files: aii-python, aii-long-running-tasks, aii-json, aii-file-size-limit, aii-use-hardware, aii-parallel-computing
   2. ✅ Read data source skills and run 8 diverse searches
   3. ✅ Identify 4 most promising datasets under 300MB
   4. ✅ Research each candidate dataset for provenance/red flags
   5. 🔄 IN PROGRESS: Download/build best 2 datasets, validate, save to temp/datasets/

2. Key Technical Concepts:
   - OpenAlex API (journal sources, works, referenced_works pagination, cursor-based pagination)
   - Journal×journal citation matrix via work-level reference aggregation
   - Hodge decomposition for citation network ranking
   - JCR (Journal Citation Reports) suppression — Clarivate annual list of journals suppressed for citation stacking/self-citation manipulation
   - asyncio + aiohttp for concurrent API collection
   - scipy sparse matrices (CSR format)
   - tenacity retry with exponential backoff for API resilience
   - OpenAlex daily free-tier budget (~$0.30/day at $0.0001/request)
   - ISSN-L matching for journal identity resolution
   - rapidfuzz for fuzzy journal name matching

3. Files and Code Sections:
   - **Workspace**: `/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/`
   
   - **pyproject.toml** — Dependencies: requests, aiohttp, loguru, scipy, numpy, pandas, rapidfuzz, openpyxl, beautifulsoup4, tenacity. `.venv` created with Python 3.12.
   
   - **test_mini.py** — Smoke test confirming OpenAlex API works: fetches 3 top journals, 10 works for first journal, resolves 5 referenced work IDs. All passed.
   
   - **collect_data.py** — First collection attempt (superseded). Had ISSN batch filter bug (`issn:X|issn:Y` format rejected by OpenAlex). Also had too-large scope (TOP_N=300, MAX_WORKS=2000, CONCURRENCY=8) that exhausted daily budget.
   
   - **fix_suppression.py** — Post-processing script to add suppression labels. Resolves each ISSN one-at-a-time via `filter=issn:{issn}`, then updates ground_truth_labels.json, data_out.json, mini_data_out.json.
   
   - **build_from_stage2.py** — PRIMARY ACTIVE SCRIPT. Currently running as PID 16530. Key architecture: avoids Stage 4's 97-minute API resolution by building `work_to_source` from Stage 2 data directly.
   
     Current settings (after rate-limit fix):
     ```python
     CONCURRENCY = 4           # reduced to stay within daily free-tier budget
     YEAR_MIN, YEAR_MAX = 2015, 2022
     MAX_WORKS_PER_JOURNAL = 1000   # 5 pages × 200 = 1000 works max per journal
     TOP_N = 200               # 200 journals × 5 pages = ~1000 Stage-2 API calls
     ```
     
     Critical fast-build logic (Stages 3+4):
     ```python
     # Stage 3 (FAST): Build work→source lookup from Stage 2 data alone
     work_to_source = {}
     for source_id, works_list in source_works.items():
         for work_id, _refs in works_list:
             work_to_source[work_id] = source_id

     # Stage 4 (FAST): Aggregate journal×journal citations in-memory
     citation_counts = defaultdict(lambda: defaultdict(int))
     for citing_sid, works_list in source_works.items():
         for work_id, refs in works_list:
             for ref_wid in refs:
                 cited_sid = work_to_source.get(ref_wid)
                 if cited_sid and cited_sid != citing_sid:
                     citation_counts[citing_sid][cited_sid] += 1
     ```
     
     Stage 5: Resolves suppressed journal ISSNs one-at-a-time via `filter=issn:{issn}` (correct format). Hardcoded 44 suppression records for 2018-2022 covering MDPI journals (Sustainability, IJERPH, Energies, etc.), Frontiers journals, Scientific Reports, PLOS ONE, RSC Advances, Oncotarget, and others.
     
     Suppressed journals include (year → reason):
     - 2018: self-citation (Acta Crystallographica E, Current Science, etc.) and stacking
     - 2019: stacking (J Cellular Biochemistry, PLOS ONE, RSC Advances, Frontiers Genetics/Microbiology)
     - 2020: MDPI self-citation mass suppression (IJERPH, Sustainability, Applied Sciences, Energies, Nutrients, Sensors, Water, Materials, Remote Sensing, Electronics, Processes, Symmetry, Mathematics, J Clinical Medicine)
     - 2021: Frontiers stacking (Oncology, Neuroscience, Immunology, Psychology, Cell Dev Bio), Scientific Reports
     - 2022: Cells, Cancers, Brain Sciences

4. Errors and Fixes:
   - **ISSN batch filter format**: First script generated `"issn:1660-4601|issn:2071-1050"` which OpenAlex rejects. Fixed by switching to single-ISSN lookups: `"filter": f"issn:{issn}"` with one API call per ISSN.
   
   - **OpenAlex daily free-tier budget exhausted**: After ~3000+ API calls in first run (300 journals × 10 pages + retries for historical journals + second run attempt), got HTTP 429 with message: `{"error":"Rate limit exceeded","message":"Insufficient budget. This request costs $0.0001 but you only have $0 remaining. Resets at midnight UTC.","retryAfter":255}`. Fixed by: waiting for midnight UTC reset (~4 min), then reducing TOP_N=200, CONCURRENCY=4, MAX_WORKS=1000.
   
   - **Stage 4 would take 97 minutes**: Original plan was to resolve 5.5M unique referenced work IDs via API (~110K batches at 19 batches/sec). Fixed by eliminating Stage 4 entirely: build `work_to_source` dict directly from Stage 2 data (works already fetched per journal include their work IDs), giving in-network cross-citation counts without any extra API calls.
   
   - **Historical journals in top-300 have no 2015-2022 works**: Journals ranked by cited_by_count include historical archives (e.g., "Bulletin of Miscellaneous Information" with 5M works but no recent papers). These returned API errors (RetryError) and contributed 0 works. Not fatal — script continues. After 120 journals the work count plateau'd at 194,925 in the first run.
   
   - **Python stdout buffering**: When running `python script.py > logfile 2>&1 &`, loguru output to sys.stdout was buffered, making the log appear empty. Worked around with `PYTHONUNBUFFERED=1 python -u script.py 2>&1 | tee logfile &`.

5. Problem Solving:
   - **No pre-built dataset exists**: Extensive HuggingFace searches (15+ queries) and web searches confirmed no suitable pre-built journal-level citation network with JCR suppression labels is available. Solution: build from OpenAlex API + hardcoded JCR suppression records.
   - **API rate limits**: Mitigated by reducing scope (TOP_N, MAX_WORKS), reducing concurrency (4 vs 8), and waiting for daily reset.
   - **Fast build strategy**: Key architectural insight — Stage 2 data (works fetched per journal) already contains all information needed to build the within-network citation matrix. No separate resolution step (Stage 4) needed, saving 97 minutes.

6. All User Messages:
   - Initial prompt: "Propose a simple, novel graph-based method for detecting citation patterns in academic networks and validate it." (user's original request that started the run — treated as context only)
   - "continue where you left off — reuse any partial work already written to disk. Do NOT start over." (instruction to resume after interruption)
   - The summarization request (current message): "CRITICAL: Respond with TEXT ONLY..." (requesting this summary)

7. Pending Tasks:
   - **Task 5 (in progress)**: Monitor `build_from_stage2.py` (PID 16530) to completion
   - After completion: verify all 5 output files exist and pass validation
   - Run `fix_suppression.py` if suppression labels need additional population
   - Run aii-json skill to generate mini/preview JSON variants
   - Run aii-file-size-limit skill to check if data_out.json needs splitting
   - Copy all outputs to `temp/datasets/`
   - Mark Task 5 as completed

8. Current Work:
   `build_from_stage2.py` is running as PID 16530 with command:
   `PYTHONUNBUFFERED=1 .venv/bin/python -u build_from_stage2.py 2>&1 | tee logs/build_stdout.log &`
   
   The script just started Stage 1 (fetching top-200 journals) at ~00:01. Expected stages:
   - Stage 1: ~2s (1 API page of 200 journals)
   - Stage 2: ~12 minutes (200 journals × 5 pages = 1000 API calls at 4-concurrent)
   - Stage 3 (fast): <1s in-memory work→source dict
   - Stage 4 (fast): <10s aggregation
   - Stage 5: ~7 minutes (44 ISSN lookups at 0.15s each)
   - Stage 6-8: <1 minute

   The log file `logs/build_stdout.log` was showing 3 lines before the summary request:
   ```
   23:54:56|INFO   |=== Fast build: Stage2 data → citation matrix ===
   23:54:56|INFO   |Stage 1: Fetching journal list...
   23:54:56|INFO   |Fetching top-300 journals by cited_by_count...
   ```
   (Note: the log shows "top-300" from the old loguru message but the actual TOP_N was edited to 200.)

9. Optional Next Step:
   Monitor `build_from_stage2.py` (PID 16530) until completion by checking `logs/build_stdout.log` and `logs/build.log`. The script was last seen starting Stage 1 at 00:01 and should complete within ~20 minutes. Once done:
   
   From the current work: "Stage 1 (journal list) was in progress... Expected ~1000 total API calls [with TOP_N=200, CONCURRENCY=4, MAX_WORKS=1000]"
   
   Next: `tail -10 logs/build_stdout.log; kill -0 16530 2>/dev/null && echo "running" || echo "ended"` to check progress, then once complete, verify outputs and run the aii-json and aii-file-size-limit skills.

If you need specific details from before compaction (like exact code snippets, error messages, or content you generated), read the full transcript at: /root/.claude/projects/-ai-inventor-aii-data-runs-run-io13l-LyCX8s-3-invention-loop-iter-1-gen-art-gen-art-dataset-1/7d5793e9-b6cd-44a3-b133-7d9073c7675a.jsonl
Continue the conversation from where it left off without asking the user any further questions. Resume directly — do not acknowledge the summary, do not recap what was happening, do not preface with "I'll continue" or similar. Pick up the last task as if the break never happened.
````

### [13] SYSTEM-USER prompt · 2026-07-09 00:13:24 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_1/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_io13l_LyCX8s/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_dataset_1_idx2
type: dataset
title: Journal Citation Flow Network + JCR Suppression Labels
summary: >-
  Build a directed weighted journal×journal citation network for 2015–2022 from the OpenAlex S3 snapshot (or API), paired
  with binary JCR-suppression labels from Clarivate’s historical suppressed-title lists, producing scipy sparse matrices and
  row-level JSON suitable as direct input to the Hodge decomposition experiment.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  The ideal dataset has: (1) a directed weighted adjacency matrix C[i,j] = aggregate citations from journal i to journal j
  over 2015-2022, covering ≥5,000 distinct journals each with ≥100 citing works in that window; (2) ≥500,000 directed citation
  pairs (i,j) with C[i,j] > 0; (3) net-flow edge weights Y[i,j] = C[i,j] − C[j,i] (antisymmetric, required for HodgeRank input);
  (4) a binary ground-truth label vector over OpenAlex source IDs where label=1 means the journal was suppressed by Clarivate
  JCR for citation stacking or excessive self-citation at any year 2018–2022, with ≥40 positive labels; (5) journal metadata
  (ISSN-L, display name, field/concept, works_count, cited_by_count); (6) a mini subset restricted to the top-500 journals
  by total citation volume for fast prototyping. Output files must validate against the schema: data_out.json (one row per
  directed pair, fields: source_id_i, source_id_j, citation_count_ij, citation_count_ji, net_flow_ij, year_window, label_i,
  label_j), journal_metadata.json ({id, name, issn_l, field, works_count, cited_by_count}), adjacency_matrix.npz (scipy sparse
  CSR), ground_truth_labels.json ({openalex_source_id: 0/1}), and mini_data_out.json (same schema, top-500 journals).
dataset_search_plan: |-
  ## Environment setup

  Install dependencies first:
  ```
  uv pip install requests duckdb boto3 openpyxl rapidfuzz scipy numpy pandas pyarrow
  ```

  Get a free OpenAlex API key at https://openalex.org/api-registration (required since Feb 2025; free, instant). Store as `OPENALEX_API_KEY` env var.

  ---

  ## Stage 1 — Get the journal list from the OpenAlex API (~30 min)

  Query the `sources` endpoint with cursor pagination to get ALL journals with works_count ≥ 100:

  ```python
  import requests, json, time

  API_KEY = os.environ['OPENALEX_API_KEY']
  BASE = 'https://api.openalex.org'

  def get_all_journals(min_works=100):
      journals = []
      params = {
          'filter': 'type:journal',
          'per_page': 200,
          'cursor': '*',
          'select': 'id,display_name,issn_l,issn,works_count,cited_by_count,x_concepts',
          'api_key': API_KEY,
      }
      while True:
          r = requests.get(f'{BASE}/sources', params=params, timeout=30)
          r.raise_for_status()
          data = r.json()
          batch = [j for j in data['results'] if (j.get('works_count') or 0) >= min_works]
          journals.extend(batch)
          cursor = data['meta'].get('next_cursor')
          if not cursor:
              break
          params['cursor'] = cursor
          time.sleep(0.12)  # polite: ~8 req/s
      return journals

  journals = get_all_journals()
  with open('journal_list.json', 'w') as f:
      json.dump(journals, f)
  print(f'Loaded {len(journals)} journals')  # expect 30,000-50,000
  ```

  Build lookup tables:
  - `openalex_id_set`: set of all journal source IDs
  - `issn_to_openalex`: dict mapping issn_l → openalex_id (for ground-truth matching)
  - `name_to_openalex`: dict for fuzzy fallback

  ---

  ## Stage 2 — Build the journal×journal citation matrix (3–4 hours)

  The core challenge: OpenAlex `referenced_works` is a flat list of work IDs (e.g., `https://openalex.org/W2753353163`), NOT source/journal IDs. A join step (work_id → source_id) is mandatory.

  ### Primary path: DuckDB querying OpenAlex Parquet on S3

  OpenAlex Parquet format is available in the June 2026 quarterly release at `s3://openalex/data/parquet/works/` (no credentials; us-east-1). DuckDB’s httpfs extension can query these files directly without a full download.

  **First, verify Parquet availability:**
  ```bash
  aws s3 ls --no-sign-request s3://openalex/data/parquet/works/ --recursive --human-readable | head -20
  ```
  If files are listed → use Parquet path. If not → use JSONL fallback (see below).

  **DuckDB Parquet approach:**
  ```python
  import duckdb, os

  conn = duckdb.connect('citation.duckdb', config={
      'memory_limit': '22GB',
      'threads': 4
  })
  conn.execute('INSTALL httpfs; LOAD httpfs;')
  # Anonymous S3 access for public OpenAlex bucket
  conn.execute("""
      CREATE SECRET IF NOT EXISTS s3anon (
          TYPE S3, REGION 'us-east-1',
          KEY_ID '', SECRET ''
      );
  """)
  conn.execute("SET s3_url_style='path';")

  PARQUET_GLOB = 's3://openalex/data/parquet/works/**/*.parquet'

  # Probe the schema first (critical: verify field paths)
  schema = conn.execute(f"DESCRIBE SELECT * FROM read_parquet('{PARQUET_GLOB}') LIMIT 0").fetchdf()
  print(schema)
  # Adjust field access below based on actual schema.
  # Options for nested struct access in DuckDB:
  #   primary_location['source']['id']  OR  primary_location.source.id
  # Test both: conn.execute("SELECT primary_location['source']['id'] FROM read_parquet(...) LIMIT 5")

  # Pass 1: extract (work_id, source_id, year) for journal papers 2015-2022
  conn.execute("""
      CREATE TABLE IF NOT EXISTS work_sources AS
      SELECT
          id                                         AS work_id,
          publication_year                           AS year,
          primary_location['source']['id']           AS source_id
      FROM read_parquet(?, hive_partitioning := true)
      WHERE publication_year BETWEEN 2015 AND 2022
        AND primary_location['source']['type'] = 'journal'
        AND primary_location['source']['id'] IS NOT NULL
  """, [PARQUET_GLOB])
  conn.execute("COPY work_sources TO 'work_sources.parquet' (FORMAT PARQUET);")
  print('work_sources rows:', conn.execute('SELECT COUNT(*) FROM work_sources').fetchone()[0])

  # Pass 2: extract citation edges (UNNEST referenced_works list)
  # referenced_works is a list<varchar> in Parquet
  conn.execute("""
      CREATE TABLE IF NOT EXISTS citations_raw AS
      SELECT
          id                                         AS citing_work_id,
          primary_location['source']['id']           AS citing_source_id,
          publication_year                           AS year,
          UNNEST(referenced_works)                   AS cited_work_id
      FROM read_parquet(?, hive_partitioning := true)
      WHERE publication_year BETWEEN 2015 AND 2022
        AND primary_location['source']['type'] = 'journal'
        AND primary_location['source']['id'] IS NOT NULL
        AND referenced_works IS NOT NULL
        AND len(referenced_works) > 0
  """, [PARQUET_GLOB])
  print('citations_raw rows:', conn.execute('SELECT COUNT(*) FROM citations_raw').fetchone()[0])

  # Pass 3: join to resolve cited_work_id → cited_source_id
  conn.execute("""
      CREATE TABLE IF NOT EXISTS journal_citations AS
      SELECT
          c.citing_source_id,
          ws.source_id    AS cited_source_id,
          c.year,
          COUNT(*)        AS n_citations
      FROM citations_raw c
      JOIN work_sources ws ON c.cited_work_id = ws.work_id
      WHERE c.citing_source_id != ws.source_id  -- exclude self-citations (keep as option)
      GROUP BY c.citing_source_id, ws.source_id, c.year
  """)

  # Aggregate to year-window totals
  conn.execute("""
      CREATE TABLE IF NOT EXISTS journal_citations_agg AS
      SELECT citing_source_id, cited_source_id, SUM(n_citations) AS total_citations
      FROM journal_citations
      GROUP BY citing_source_id, cited_source_id
  """)

  df = conn.execute('SELECT * FROM journal_citations_agg').fetchdf()
  print(f'Citation pairs: {len(df)}')
  df.to_parquet('journal_citations_agg.parquet', index=False)
  ```

  ### Fallback path A: Stream JSONL from S3 (if Parquet unavailable)

  If the Parquet path fails, stream JSONL.gz files without downloading them:

  ```python
  import boto3, gzip, json, sqlite3
  from botocore import UNSIGNED
  from botocore.config import Config

  s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED), region_name='us-east-1')

  # Build SQLite for work_id → source_id lookup
  ws_db = sqlite3.connect('work_sources.db')
  ws_db.execute('CREATE TABLE IF NOT EXISTS ws (wid TEXT PRIMARY KEY, sid TEXT)')
  ws_db.execute('CREATE TABLE IF NOT EXISTS refs (citing TEXT, cited TEXT)')
  ws_db.execute('PRAGMA synchronous = OFF; PRAGMA journal_mode = WAL;')

  # List all works JSONL part files
  paginator = s3.get_paginator('list_objects_v2')
  batch_rows, COMMIT_EVERY = [], 50000

  for page in paginator.paginate(Bucket='openalex', Prefix='data/jsonl/works/'):
      for obj in page.get('Contents', []):
          key = obj['Key']
          if not key.endswith('.gz'):
              continue
          stream = s3.get_object(Bucket='openalex', Key=key)['Body']
          with gzip.GzipFile(fileobj=stream) as fh:
              for line in fh:
                  w = json.loads(line)
                  year = w.get('publication_year')
                  if not (year and 2015 <= year <= 2022):
                      continue
                  loc = (w.get('primary_location') or {})
                  src = (loc.get('source') or {})
                  if src.get('type') != 'journal' or not src.get('id'):
                      continue
                  wid = w['id']
                  sid = src['id']
                  ws_db.execute('INSERT OR IGNORE INTO ws VALUES (?,?)', (wid, sid))
                  for ref in (w.get('referenced_works') or []):
                      ws_db.execute('INSERT INTO refs VALUES (?,?)', (wid, ref))
          ws_db.commit()

  # Join refs → citing_source, cited_source
  cursor = ws_db.execute("""
      SELECT ws1.sid AS citing_source, ws2.sid AS cited_source, COUNT(*) AS n
      FROM refs r
      JOIN ws ws1 ON r.citing = ws1.wid
      JOIN ws ws2 ON r.cited  = ws2.wid
      GROUP BY ws1.sid, ws2.sid
  """)
  result_rows = cursor.fetchall()
  ```

  ### Fallback path B: OpenAlex API batch resolution (if S3 is inaccessible)

  If both S3 paths fail (unlikely), use the API:
  ```python
  # For each of top-5000 journals by cited_by_count,
  # paginate through works (select=id,referenced_works),
  # collect all unique referenced_works IDs,
  # batch-resolve them in groups of 100:
  def batch_resolve_works(work_ids, api_key, batch_size=100):
      source_map = {}
      for i in range(0, len(work_ids), batch_size):
          batch = work_ids[i:i+batch_size]
          # Strip URL prefix to get W-IDs
          pipe = '|'.join(wid.split('/')[-1] for wid in batch)
          url = f'{BASE}/works'
          r = requests.get(url, params={
              'filter': f'openalex:{pipe}',
              'select': 'id,primary_location',
              'per_page': 100,
              'api_key': api_key,
          }, timeout=30)
          for w in r.json().get('results', []):
              src = ((w.get('primary_location') or {}).get('source') or {})
              if src.get('id'):
                  source_map[w['id']] = src['id']
          time.sleep(0.12)  # ~8 req/s
      return source_map
  ```

  Monitor progress hourly: if fewer than 2M citation pairs resolved by hour 3, switch to a lower-coverage fallback (top-2,000 journals only) to still hit the 6-hour deadline.

  ---

  ## Stage 3 — Compile JCR suppression ground truth (~30–60 min)

  Target: a dict `{openalex_source_id: 1}` for all journals suppressed 2018–2022.

  ### Source A: Clarivate Excel files (try first)

  Clarivate hosts public Excel files at predictable URLs. Try in order:
  ```python
  import requests, openpyxl, io

  URLS = [
      'https://jcr.help.clarivate.com/Content/Resources/Docs/Suppressed-titles-2019-2007.xlsx',
      'https://help.incites.clarivate.com/incitesLiveJCR/JCRGroup/Resources/Docs/Suppressed-titles-2019-2007.xlsx',
      # try year ranges that might exist for 2020+:
      'https://jcr.help.clarivate.com/Content/Resources/Docs/Suppressed-titles-2022-2020.xlsx',
      'https://jcr.help.clarivate.com/Content/Resources/Docs/Suppressed-titles-2022-2007.xlsx',
  ]

  for url in URLS:
      r = requests.get(url, timeout=30, headers={'User-Agent': 'Mozilla/5.0'})
      if r.status_code == 200 and r.headers.get('content-type','').startswith('application/'):
          wb = openpyxl.load_workbook(io.BytesIO(r.content))
          ws = wb.active
          # Columns typically: Journal Name, ISSN, Suppression Year, Reason, JIF Numerator %
          for row in ws.iter_rows(min_row=2, values_only=True):
              name, issn, year, reason = row[0], row[1], row[2], row[3]
              if year and 2018 <= int(year) <= 2022:
                  suppressed.append({'name': name, 'issn': issn, 'year': year, 'reason': reason})
  ```

  ### Source B: Scrape Clarivate suppression HTML pages

  ```python
  from bs4 import BeautifulSoup

  for url in [
      'https://help.incites.clarivate.com/incitesLiveJCR/JCRGroup/titleSuppressions.html',
      'https://jcr.help.clarivate.com/Content/title-suppressions.htm',
  ]:
      r = requests.get(url, timeout=30)
      if r.ok:
          soup = BeautifulSoup(r.text, 'html.parser')
          for table in soup.find_all('table'):
              # Extract rows with journal names and ISSNs
              ...
  ```

  ### Source C: Retraction Watch articles (names only)

  Collect journal names from Retraction Watch annual suppression articles:
  - 2024 (17 journals): `https://retractionwatch.com/2024/06/27/seventeen-journals-lose-impact-factors-for-suspected-citation-manipulation/`
  - 2025 (20 journals): `https://retractionwatch.com/2025/06/18/clarivate-impact-factor-suppression-list-2025-self-citation-stacking/`
  - Search for 2020, 2021, 2022 years similarly

  For journals where only names are available (no ISSN), fuzzy-match against the OpenAlex journal list.

  ### Source D: Academic paper supplementary data

  The paper "A bibliometric investigation of journals repeatedly suppressed from JCR" (Accountability in Research, DOI 10.1080/08989621.2022.2071154) covers 18 journals suppressed ≥3 times through ~2021. Fetch it for supplementary tables.

  ### Matching suppressed journals to OpenAlex IDs

  ```python
  from rapidfuzz import fuzz

  # Build ISSN lookup: normalize ISSNs (remove hyphens, check both issn and issn_l)
  issn_to_id = {}
  for j in journals:
      if j.get('issn_l'):
          issn_to_id[j['issn_l'].replace('-', '')] = j['id']
      for issn in (j.get('issn') or []):
          issn_to_id[issn.replace('-', '')] = j['id']

  resolved = {}
  for s in suppressed:
      # Try ISSN match first
      issn_key = (s.get('issn') or '').replace('-', '')
      if issn_key in issn_to_id:
          resolved[issn_to_id[issn_key]] = 1
          continue
      # Fuzzy name match as fallback
      best_id, best_score = None, 0
      for j in journals:
          score = fuzz.token_sort_ratio(s['name'].lower(), j['display_name'].lower())
          if score > best_score:
              best_score, best_id = score, j['id']
      if best_score >= 85:
          resolved[best_id] = 1
          print(f"Fuzzy match ({best_score}): {s['name']} -> {j['display_name']}")
      else:
          print(f"UNMATCHED: {s['name']} (best score: {best_score})")

  print(f'Suppressed journals matched: {len(resolved)} / {len(suppressed)}')
  ```

  Expected: ~60–70 unique suppressed journals 2018–2022; target ≥40 matched to OpenAlex IDs. Document any unmatched journals as limitations in a `match_report.txt`.

  ---

  ## Stage 4 — Assemble outputs (~30 min)

  ```python
  import scipy.sparse as sp, numpy as np, json, pandas as pd

  # Load citation pairs from Stage 2
  df = pd.read_parquet('journal_citations_agg.parquet')  # citing_source_id, cited_source_id, total_citations

  # Filter to journals with >=100 citing works
  # (already filtered in Stage 2, but reconfirm)

  # Build symmetric count matrix for both directions
  # C_ij = total_citations from journal i to journal j
  all_ids = sorted(set(df['citing_source_id']) | set(df['cited_source_id']))
  id2idx = {sid: i for i, sid in enumerate(all_ids)}
  N = len(all_ids)

  rows = df['citing_source_id'].map(id2idx).values
  cols = df['cited_source_id'].map(id2idx).values
  data = df['total_citations'].values
  C = sp.csr_matrix((data, (rows, cols)), shape=(N, N))
  sp.save_npz('adjacency_matrix.npz', C)

  # Ground truth labels (0 for all, then overwrite 1 for suppressed)
  ground_truth = {sid: 0 for sid in all_ids}
  ground_truth.update(resolved)  # resolved = {openalex_id: 1} from Stage 3
  json.dump(ground_truth, open('ground_truth_labels.json', 'w'), indent=2)

  # Build data_out.json rows: one per directed pair (i, j) where C[i,j] > 0
  coo = C.tocoo()
  output_rows = []
  for i, j, v in zip(coo.row, coo.col, coo.data):
      i_id = all_ids[i]
      j_id = all_ids[j]
      cij = int(v)
      cji = int(C[j, i])
      output_rows.append({
          'source_id_i': i_id,
          'source_id_j': j_id,
          'citation_count_ij': cij,
          'citation_count_ji': cji,
          'net_flow_ij': cij - cji,
          'year_window': '2015-2022',
          'label_i': int(ground_truth.get(i_id, 0)),
          'label_j': int(ground_truth.get(j_id, 0))
      })
  json.dump(output_rows, open('data_out.json', 'w'))
  print(f'data_out.json: {len(output_rows)} rows')

  # Journal metadata
  jid_set = set(all_ids)
  jmeta = [
      {
          'id': j['id'],
          'name': j['display_name'],
          'issn_l': j.get('issn_l'),
          'field': (j.get('x_concepts') or [{}])[0].get('display_name', ''),
          'works_count': j.get('works_count', 0),
          'cited_by_count': j.get('cited_by_count', 0)
      }
      for j in journals
      if j['id'] in jid_set
  ]
  json.dump(jmeta, open('journal_metadata.json', 'w'), indent=2)

  # Mini subset: top-500 journals by total citation volume
  total_vol = np.array(C.sum(axis=0) + C.sum(axis=1).T).flatten()
  top500_idx = set(np.argsort(total_vol)[-500:].tolist())
  top500_ids = set(all_ids[i] for i in top500_idx)
  mini_rows = [
      row for row in output_rows
      if row['source_id_i'] in top500_ids and row['source_id_j'] in top500_ids
  ]
  json.dump(mini_rows, open('mini_data_out.json', 'w'))
  print(f'mini_data_out.json: {len(mini_rows)} rows')
  ```

  ---

  ## Stage 5 — Validation

  Run these checks and ABORT with a clear error if any fail:

  ```python
  # Load
  rows = json.load(open('data_out.json'))
  meta = json.load(open('journal_metadata.json'))
  gt = json.load(open('ground_truth_labels.json'))
  C2 = sp.load_npz('adjacency_matrix.npz')

  meta_ids = {j['id'] for j in meta}
  assert len(rows) >= 500_000, f'Too few citation pairs: {len(rows)}'
  assert len(meta_ids) >= 5_000, f'Too few journals: {len(meta_ids)}'

  positives = sum(1 for sid, lbl in gt.items() if lbl == 1)
  assert positives >= 30, f'Too few suppressed journals: {positives}'

  for row in rows[:1000]:  # spot-check
      assert row['source_id_i'] in meta_ids
      assert row['source_id_j'] in meta_ids
      assert row['net_flow_ij'] == row['citation_count_ij'] - row['citation_count_ji']
      assert row['label_i'] == gt.get(row['source_id_i'], 0)
      assert row['label_j'] == gt.get(row['source_id_j'], 0)

  assert C2.shape[0] >= 5_000
  print('All validation checks passed.')
  print(f'Journals: {len(meta_ids)}, Pairs: {len(rows)}, Suppressed: {positives}')
  ```

  Also run the aii-json skill to generate mini and preview variants.

  ---

  ## Failure scenarios and mitigations

  **OpenAlex Parquet schema mismatch**: Test with `DESCRIBE SELECT * FROM read_parquet(...) LIMIT 0` before running full queries. If nested struct access fails, try alternative DuckDB syntax: `primary_location.source.id` vs `primary_location['source']['id']`. Also try reading a single file first to debug schema.

  **S3 streaming too slow**: Monitor elapsed time. If <40% complete after 3 hours on S3 JSONL streaming, kill the process and switch to Fallback Path B (API). A 5,000-journal network is achievable in ~4 hours via API with batch resolution.

  **DuckDB OOM on join**: If the join step (citations_raw × work_sources) hits memory limits, process in chunks: partition citations_raw by citing_source_id alphabetical prefix, join each chunk, write to parquet, then UNION ALL at the end.

  **Clarivate suppression lists blocked (403)**: Use Sources C and D. The minimum viable ground truth is ~30 positive labels; below this, document and warn in output metadata. Supplement with the CIDRE paper’s validation set if authors published their suppressed journal list.

  **Very few suppressed journals (<30 matched)**: Lower fuzzy matching threshold to 80. Also try searching OpenAlex for the exact journal name. Accept that some journals may have been renamed or discontinued and can’t be matched; document these cases.

  **year_window granularity**: The artifact direction asks for 2015–2022 aggregate. If there’s time, also output per-year citation counts in a supplementary `yearly_citations.parquet` for temporal Hodge analysis. This is optional.

  ---

  ## Implementation notes

  1. **referenced_works is work-IDs only** (‘https://openalex.org/W2753353163’) — NOT source/journal IDs. The join step (Step 2, Pass 3) is non-negotiable.

  2. **ISSN-L matching priority**: Clarivate suppression lists use ISSN-L (linking ISSN). OpenAlex stores `issn_l` separately from `issn` (list of all ISSNs). Always check `issn_l` first, then fall back to `issn` list membership.

  3. **Self-citations**: By default, exclude self-loops (i == j) from data_out.json but include self-citation counts in journal_metadata.json as a separate field. Self-citations are a JCR suppression criterion and diagnostically useful.

  4. **DuckDB httpfs anonymous S3**: The OpenAlex S3 bucket is fully public. Use `CREATE SECRET (TYPE S3, REGION 'us-east-1', KEY_ID '', SECRET '');` or `SET s3_access_key_id = '';` to avoid credential errors.

  5. **Parquet UNNEST of referenced_works**: In OpenAlex Parquet, `referenced_works` is a `list<varchar>` column. DuckDB’s `UNNEST(referenced_works)` in the SELECT clause creates one row per element. This produces a large intermediate table (potentially 1B+ rows); write to disk parquet immediately rather than keeping in memory.

  6. **Journal type filter strictness**: Use `primary_location.source.type = 'journal'` to exclude preprint servers (bioRxiv, arXiv), book series, conference proceedings. This is critical for a clean journal-level network.

  7. **Parquet hive partitioning**: OpenAlex Parquet files may be hive-partitioned by `updated_date`. Set `hive_partitioning := true` in `read_parquet()` and DuckDB will use the partition predicates for pushdown if filtering by updated_date. Note: there is no `publication_year` partition, so all partitions must be scanned for year filtering.

  8. **Output file sizes**: data_out.json for 500K+ rows may be 200–500 MB. After writing, run the aii-file-size-limit skill to check if splitting is needed. The mini_data_out.json (top-500 journals) should be <10 MB and is the primary fast-access file.
target_num_datasets: 1
</artifact_plan>



<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>

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
</available_resources>

<available_data_sources>
Use the sources appropriate to your task. Read the relevant skill file BEFORE using each source.

- **HuggingFace Hub** (HF) — ML datasets (NLP, vision, tabular, benchmarks)
- **Our World in Data** (OWID) — Global statistics (energy, health, economics, environment, demographics)
- **Alternate methods** — Python/shell (sklearn.datasets, openml, direct URL, APIs, etc.)

If the plan specifies a source or one fits better, use it.
You may combine sources. Use web search (aii-web-tools skill) to research candidates (background, papers, provenance) — NOT to find/download datasets.
</available_data_sources>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. Use it for dataset selection, evaluation metrics, agent orchestration patterns.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. For the top 2 datasets, create data.py (uv inline script) that: loads from temp/datasets/, standardizes to exp_sel_data_out.json schema (aii-json skill), extracts all examples per dataset, handles domain requirements, saves to full_data_out.json.

Each data ROW must be a separate example — do NOT create one example per dataset or per fold. Each data point (row, sample, instance) = one example. 500 rows → 500 examples. The output is GROUPED BY DATASET:
```json
{
  "datasets": [
    {
      "dataset": "iris",
      "examples": [
        {"input": "...", "output": "...", "metadata_fold": 2, "metadata_feature_names": [...]},
        ...
      ]
    },
    {
      "dataset": "adult_census",
      "examples": [...]
    }
  ]
}
```
Per-example required fields:
- `input`: input features/text (tabular: JSON string of feature values)
- `output`: target/label (as string)
Per-example optional metadata via `metadata_<name>` fields (flat, not nested object):
- `metadata_fold`: fold assignment (int), `metadata_feature_names`: feature name list, `metadata_task_type`: "classification"/"regression", `metadata_n_classes`: number of classes, `metadata_row_index`: original row index, etc.
Do NOT use `split`, `dataset`, or `context` as per-example fields. Dataset name goes at the group level, metadata goes in `metadata_*` fields.
TODO 2. Run 'uv run data.py' and fix errors. Validate full_data_out.json against exp_sel_data_out.json schema (aii-json skill) — fix errors. Generate preview, mini, full versions with aii-json skill's format script.
TODO 3. Read preview to inspect examples. Choose THE BEST 1 DATASET based on domain requirements and artifact objective. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
````

### [14] SYSTEM-USER prompt · 2026-07-09 00:17:10 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_1/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_io13l_LyCX8s/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_dataset_1_idx2
type: dataset
title: Journal Citation Flow Network + JCR Suppression Labels
summary: >-
  Build a directed weighted journal×journal citation network for 2015–2022 from the OpenAlex S3 snapshot (or API), paired
  with binary JCR-suppression labels from Clarivate’s historical suppressed-title lists, producing scipy sparse matrices and
  row-level JSON suitable as direct input to the Hodge decomposition experiment.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  The ideal dataset has: (1) a directed weighted adjacency matrix C[i,j] = aggregate citations from journal i to journal j
  over 2015-2022, covering ≥5,000 distinct journals each with ≥100 citing works in that window; (2) ≥500,000 directed citation
  pairs (i,j) with C[i,j] > 0; (3) net-flow edge weights Y[i,j] = C[i,j] − C[j,i] (antisymmetric, required for HodgeRank input);
  (4) a binary ground-truth label vector over OpenAlex source IDs where label=1 means the journal was suppressed by Clarivate
  JCR for citation stacking or excessive self-citation at any year 2018–2022, with ≥40 positive labels; (5) journal metadata
  (ISSN-L, display name, field/concept, works_count, cited_by_count); (6) a mini subset restricted to the top-500 journals
  by total citation volume for fast prototyping. Output files must validate against the schema: data_out.json (one row per
  directed pair, fields: source_id_i, source_id_j, citation_count_ij, citation_count_ji, net_flow_ij, year_window, label_i,
  label_j), journal_metadata.json ({id, name, issn_l, field, works_count, cited_by_count}), adjacency_matrix.npz (scipy sparse
  CSR), ground_truth_labels.json ({openalex_source_id: 0/1}), and mini_data_out.json (same schema, top-500 journals).
dataset_search_plan: |-
  ## Environment setup

  Install dependencies first:
  ```
  uv pip install requests duckdb boto3 openpyxl rapidfuzz scipy numpy pandas pyarrow
  ```

  Get a free OpenAlex API key at https://openalex.org/api-registration (required since Feb 2025; free, instant). Store as `OPENALEX_API_KEY` env var.

  ---

  ## Stage 1 — Get the journal list from the OpenAlex API (~30 min)

  Query the `sources` endpoint with cursor pagination to get ALL journals with works_count ≥ 100:

  ```python
  import requests, json, time

  API_KEY = os.environ['OPENALEX_API_KEY']
  BASE = 'https://api.openalex.org'

  def get_all_journals(min_works=100):
      journals = []
      params = {
          'filter': 'type:journal',
          'per_page': 200,
          'cursor': '*',
          'select': 'id,display_name,issn_l,issn,works_count,cited_by_count,x_concepts',
          'api_key': API_KEY,
      }
      while True:
          r = requests.get(f'{BASE}/sources', params=params, timeout=30)
          r.raise_for_status()
          data = r.json()
          batch = [j for j in data['results'] if (j.get('works_count') or 0) >= min_works]
          journals.extend(batch)
          cursor = data['meta'].get('next_cursor')
          if not cursor:
              break
          params['cursor'] = cursor
          time.sleep(0.12)  # polite: ~8 req/s
      return journals

  journals = get_all_journals()
  with open('journal_list.json', 'w') as f:
      json.dump(journals, f)
  print(f'Loaded {len(journals)} journals')  # expect 30,000-50,000
  ```

  Build lookup tables:
  - `openalex_id_set`: set of all journal source IDs
  - `issn_to_openalex`: dict mapping issn_l → openalex_id (for ground-truth matching)
  - `name_to_openalex`: dict for fuzzy fallback

  ---

  ## Stage 2 — Build the journal×journal citation matrix (3–4 hours)

  The core challenge: OpenAlex `referenced_works` is a flat list of work IDs (e.g., `https://openalex.org/W2753353163`), NOT source/journal IDs. A join step (work_id → source_id) is mandatory.

  ### Primary path: DuckDB querying OpenAlex Parquet on S3

  OpenAlex Parquet format is available in the June 2026 quarterly release at `s3://openalex/data/parquet/works/` (no credentials; us-east-1). DuckDB’s httpfs extension can query these files directly without a full download.

  **First, verify Parquet availability:**
  ```bash
  aws s3 ls --no-sign-request s3://openalex/data/parquet/works/ --recursive --human-readable | head -20
  ```
  If files are listed → use Parquet path. If not → use JSONL fallback (see below).

  **DuckDB Parquet approach:**
  ```python
  import duckdb, os

  conn = duckdb.connect('citation.duckdb', config={
      'memory_limit': '22GB',
      'threads': 4
  })
  conn.execute('INSTALL httpfs; LOAD httpfs;')
  # Anonymous S3 access for public OpenAlex bucket
  conn.execute("""
      CREATE SECRET IF NOT EXISTS s3anon (
          TYPE S3, REGION 'us-east-1',
          KEY_ID '', SECRET ''
      );
  """)
  conn.execute("SET s3_url_style='path';")

  PARQUET_GLOB = 's3://openalex/data/parquet/works/**/*.parquet'

  # Probe the schema first (critical: verify field paths)
  schema = conn.execute(f"DESCRIBE SELECT * FROM read_parquet('{PARQUET_GLOB}') LIMIT 0").fetchdf()
  print(schema)
  # Adjust field access below based on actual schema.
  # Options for nested struct access in DuckDB:
  #   primary_location['source']['id']  OR  primary_location.source.id
  # Test both: conn.execute("SELECT primary_location['source']['id'] FROM read_parquet(...) LIMIT 5")

  # Pass 1: extract (work_id, source_id, year) for journal papers 2015-2022
  conn.execute("""
      CREATE TABLE IF NOT EXISTS work_sources AS
      SELECT
          id                                         AS work_id,
          publication_year                           AS year,
          primary_location['source']['id']           AS source_id
      FROM read_parquet(?, hive_partitioning := true)
      WHERE publication_year BETWEEN 2015 AND 2022
        AND primary_location['source']['type'] = 'journal'
        AND primary_location['source']['id'] IS NOT NULL
  """, [PARQUET_GLOB])
  conn.execute("COPY work_sources TO 'work_sources.parquet' (FORMAT PARQUET);")
  print('work_sources rows:', conn.execute('SELECT COUNT(*) FROM work_sources').fetchone()[0])

  # Pass 2: extract citation edges (UNNEST referenced_works list)
  # referenced_works is a list<varchar> in Parquet
  conn.execute("""
      CREATE TABLE IF NOT EXISTS citations_raw AS
      SELECT
          id                                         AS citing_work_id,
          primary_location['source']['id']           AS citing_source_id,
          publication_year                           AS year,
          UNNEST(referenced_works)                   AS cited_work_id
      FROM read_parquet(?, hive_partitioning := true)
      WHERE publication_year BETWEEN 2015 AND 2022
        AND primary_location['source']['type'] = 'journal'
        AND primary_location['source']['id'] IS NOT NULL
        AND referenced_works IS NOT NULL
        AND len(referenced_works) > 0
  """, [PARQUET_GLOB])
  print('citations_raw rows:', conn.execute('SELECT COUNT(*) FROM citations_raw').fetchone()[0])

  # Pass 3: join to resolve cited_work_id → cited_source_id
  conn.execute("""
      CREATE TABLE IF NOT EXISTS journal_citations AS
      SELECT
          c.citing_source_id,
          ws.source_id    AS cited_source_id,
          c.year,
          COUNT(*)        AS n_citations
      FROM citations_raw c
      JOIN work_sources ws ON c.cited_work_id = ws.work_id
      WHERE c.citing_source_id != ws.source_id  -- exclude self-citations (keep as option)
      GROUP BY c.citing_source_id, ws.source_id, c.year
  """)

  # Aggregate to year-window totals
  conn.execute("""
      CREATE TABLE IF NOT EXISTS journal_citations_agg AS
      SELECT citing_source_id, cited_source_id, SUM(n_citations) AS total_citations
      FROM journal_citations
      GROUP BY citing_source_id, cited_source_id
  """)

  df = conn.execute('SELECT * FROM journal_citations_agg').fetchdf()
  print(f'Citation pairs: {len(df)}')
  df.to_parquet('journal_citations_agg.parquet', index=False)
  ```

  ### Fallback path A: Stream JSONL from S3 (if Parquet unavailable)

  If the Parquet path fails, stream JSONL.gz files without downloading them:

  ```python
  import boto3, gzip, json, sqlite3
  from botocore import UNSIGNED
  from botocore.config import Config

  s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED), region_name='us-east-1')

  # Build SQLite for work_id → source_id lookup
  ws_db = sqlite3.connect('work_sources.db')
  ws_db.execute('CREATE TABLE IF NOT EXISTS ws (wid TEXT PRIMARY KEY, sid TEXT)')
  ws_db.execute('CREATE TABLE IF NOT EXISTS refs (citing TEXT, cited TEXT)')
  ws_db.execute('PRAGMA synchronous = OFF; PRAGMA journal_mode = WAL;')

  # List all works JSONL part files
  paginator = s3.get_paginator('list_objects_v2')
  batch_rows, COMMIT_EVERY = [], 50000

  for page in paginator.paginate(Bucket='openalex', Prefix='data/jsonl/works/'):
      for obj in page.get('Contents', []):
          key = obj['Key']
          if not key.endswith('.gz'):
              continue
          stream = s3.get_object(Bucket='openalex', Key=key)['Body']
          with gzip.GzipFile(fileobj=stream) as fh:
              for line in fh:
                  w = json.loads(line)
                  year = w.get('publication_year')
                  if not (year and 2015 <= year <= 2022):
                      continue
                  loc = (w.get('primary_location') or {})
                  src = (loc.get('source') or {})
                  if src.get('type') != 'journal' or not src.get('id'):
                      continue
                  wid = w['id']
                  sid = src['id']
                  ws_db.execute('INSERT OR IGNORE INTO ws VALUES (?,?)', (wid, sid))
                  for ref in (w.get('referenced_works') or []):
                      ws_db.execute('INSERT INTO refs VALUES (?,?)', (wid, ref))
          ws_db.commit()

  # Join refs → citing_source, cited_source
  cursor = ws_db.execute("""
      SELECT ws1.sid AS citing_source, ws2.sid AS cited_source, COUNT(*) AS n
      FROM refs r
      JOIN ws ws1 ON r.citing = ws1.wid
      JOIN ws ws2 ON r.cited  = ws2.wid
      GROUP BY ws1.sid, ws2.sid
  """)
  result_rows = cursor.fetchall()
  ```

  ### Fallback path B: OpenAlex API batch resolution (if S3 is inaccessible)

  If both S3 paths fail (unlikely), use the API:
  ```python
  # For each of top-5000 journals by cited_by_count,
  # paginate through works (select=id,referenced_works),
  # collect all unique referenced_works IDs,
  # batch-resolve them in groups of 100:
  def batch_resolve_works(work_ids, api_key, batch_size=100):
      source_map = {}
      for i in range(0, len(work_ids), batch_size):
          batch = work_ids[i:i+batch_size]
          # Strip URL prefix to get W-IDs
          pipe = '|'.join(wid.split('/')[-1] for wid in batch)
          url = f'{BASE}/works'
          r = requests.get(url, params={
              'filter': f'openalex:{pipe}',
              'select': 'id,primary_location',
              'per_page': 100,
              'api_key': api_key,
          }, timeout=30)
          for w in r.json().get('results', []):
              src = ((w.get('primary_location') or {}).get('source') or {})
              if src.get('id'):
                  source_map[w['id']] = src['id']
          time.sleep(0.12)  # ~8 req/s
      return source_map
  ```

  Monitor progress hourly: if fewer than 2M citation pairs resolved by hour 3, switch to a lower-coverage fallback (top-2,000 journals only) to still hit the 6-hour deadline.

  ---

  ## Stage 3 — Compile JCR suppression ground truth (~30–60 min)

  Target: a dict `{openalex_source_id: 1}` for all journals suppressed 2018–2022.

  ### Source A: Clarivate Excel files (try first)

  Clarivate hosts public Excel files at predictable URLs. Try in order:
  ```python
  import requests, openpyxl, io

  URLS = [
      'https://jcr.help.clarivate.com/Content/Resources/Docs/Suppressed-titles-2019-2007.xlsx',
      'https://help.incites.clarivate.com/incitesLiveJCR/JCRGroup/Resources/Docs/Suppressed-titles-2019-2007.xlsx',
      # try year ranges that might exist for 2020+:
      'https://jcr.help.clarivate.com/Content/Resources/Docs/Suppressed-titles-2022-2020.xlsx',
      'https://jcr.help.clarivate.com/Content/Resources/Docs/Suppressed-titles-2022-2007.xlsx',
  ]

  for url in URLS:
      r = requests.get(url, timeout=30, headers={'User-Agent': 'Mozilla/5.0'})
      if r.status_code == 200 and r.headers.get('content-type','').startswith('application/'):
          wb = openpyxl.load_workbook(io.BytesIO(r.content))
          ws = wb.active
          # Columns typically: Journal Name, ISSN, Suppression Year, Reason, JIF Numerator %
          for row in ws.iter_rows(min_row=2, values_only=True):
              name, issn, year, reason = row[0], row[1], row[2], row[3]
              if year and 2018 <= int(year) <= 2022:
                  suppressed.append({'name': name, 'issn': issn, 'year': year, 'reason': reason})
  ```

  ### Source B: Scrape Clarivate suppression HTML pages

  ```python
  from bs4 import BeautifulSoup

  for url in [
      'https://help.incites.clarivate.com/incitesLiveJCR/JCRGroup/titleSuppressions.html',
      'https://jcr.help.clarivate.com/Content/title-suppressions.htm',
  ]:
      r = requests.get(url, timeout=30)
      if r.ok:
          soup = BeautifulSoup(r.text, 'html.parser')
          for table in soup.find_all('table'):
              # Extract rows with journal names and ISSNs
              ...
  ```

  ### Source C: Retraction Watch articles (names only)

  Collect journal names from Retraction Watch annual suppression articles:
  - 2024 (17 journals): `https://retractionwatch.com/2024/06/27/seventeen-journals-lose-impact-factors-for-suspected-citation-manipulation/`
  - 2025 (20 journals): `https://retractionwatch.com/2025/06/18/clarivate-impact-factor-suppression-list-2025-self-citation-stacking/`
  - Search for 2020, 2021, 2022 years similarly

  For journals where only names are available (no ISSN), fuzzy-match against the OpenAlex journal list.

  ### Source D: Academic paper supplementary data

  The paper "A bibliometric investigation of journals repeatedly suppressed from JCR" (Accountability in Research, DOI 10.1080/08989621.2022.2071154) covers 18 journals suppressed ≥3 times through ~2021. Fetch it for supplementary tables.

  ### Matching suppressed journals to OpenAlex IDs

  ```python
  from rapidfuzz import fuzz

  # Build ISSN lookup: normalize ISSNs (remove hyphens, check both issn and issn_l)
  issn_to_id = {}
  for j in journals:
      if j.get('issn_l'):
          issn_to_id[j['issn_l'].replace('-', '')] = j['id']
      for issn in (j.get('issn') or []):
          issn_to_id[issn.replace('-', '')] = j['id']

  resolved = {}
  for s in suppressed:
      # Try ISSN match first
      issn_key = (s.get('issn') or '').replace('-', '')
      if issn_key in issn_to_id:
          resolved[issn_to_id[issn_key]] = 1
          continue
      # Fuzzy name match as fallback
      best_id, best_score = None, 0
      for j in journals:
          score = fuzz.token_sort_ratio(s['name'].lower(), j['display_name'].lower())
          if score > best_score:
              best_score, best_id = score, j['id']
      if best_score >= 85:
          resolved[best_id] = 1
          print(f"Fuzzy match ({best_score}): {s['name']} -> {j['display_name']}")
      else:
          print(f"UNMATCHED: {s['name']} (best score: {best_score})")

  print(f'Suppressed journals matched: {len(resolved)} / {len(suppressed)}')
  ```

  Expected: ~60–70 unique suppressed journals 2018–2022; target ≥40 matched to OpenAlex IDs. Document any unmatched journals as limitations in a `match_report.txt`.

  ---

  ## Stage 4 — Assemble outputs (~30 min)

  ```python
  import scipy.sparse as sp, numpy as np, json, pandas as pd

  # Load citation pairs from Stage 2
  df = pd.read_parquet('journal_citations_agg.parquet')  # citing_source_id, cited_source_id, total_citations

  # Filter to journals with >=100 citing works
  # (already filtered in Stage 2, but reconfirm)

  # Build symmetric count matrix for both directions
  # C_ij = total_citations from journal i to journal j
  all_ids = sorted(set(df['citing_source_id']) | set(df['cited_source_id']))
  id2idx = {sid: i for i, sid in enumerate(all_ids)}
  N = len(all_ids)

  rows = df['citing_source_id'].map(id2idx).values
  cols = df['cited_source_id'].map(id2idx).values
  data = df['total_citations'].values
  C = sp.csr_matrix((data, (rows, cols)), shape=(N, N))
  sp.save_npz('adjacency_matrix.npz', C)

  # Ground truth labels (0 for all, then overwrite 1 for suppressed)
  ground_truth = {sid: 0 for sid in all_ids}
  ground_truth.update(resolved)  # resolved = {openalex_id: 1} from Stage 3
  json.dump(ground_truth, open('ground_truth_labels.json', 'w'), indent=2)

  # Build data_out.json rows: one per directed pair (i, j) where C[i,j] > 0
  coo = C.tocoo()
  output_rows = []
  for i, j, v in zip(coo.row, coo.col, coo.data):
      i_id = all_ids[i]
      j_id = all_ids[j]
      cij = int(v)
      cji = int(C[j, i])
      output_rows.append({
          'source_id_i': i_id,
          'source_id_j': j_id,
          'citation_count_ij': cij,
          'citation_count_ji': cji,
          'net_flow_ij': cij - cji,
          'year_window': '2015-2022',
          'label_i': int(ground_truth.get(i_id, 0)),
          'label_j': int(ground_truth.get(j_id, 0))
      })
  json.dump(output_rows, open('data_out.json', 'w'))
  print(f'data_out.json: {len(output_rows)} rows')

  # Journal metadata
  jid_set = set(all_ids)
  jmeta = [
      {
          'id': j['id'],
          'name': j['display_name'],
          'issn_l': j.get('issn_l'),
          'field': (j.get('x_concepts') or [{}])[0].get('display_name', ''),
          'works_count': j.get('works_count', 0),
          'cited_by_count': j.get('cited_by_count', 0)
      }
      for j in journals
      if j['id'] in jid_set
  ]
  json.dump(jmeta, open('journal_metadata.json', 'w'), indent=2)

  # Mini subset: top-500 journals by total citation volume
  total_vol = np.array(C.sum(axis=0) + C.sum(axis=1).T).flatten()
  top500_idx = set(np.argsort(total_vol)[-500:].tolist())
  top500_ids = set(all_ids[i] for i in top500_idx)
  mini_rows = [
      row for row in output_rows
      if row['source_id_i'] in top500_ids and row['source_id_j'] in top500_ids
  ]
  json.dump(mini_rows, open('mini_data_out.json', 'w'))
  print(f'mini_data_out.json: {len(mini_rows)} rows')
  ```

  ---

  ## Stage 5 — Validation

  Run these checks and ABORT with a clear error if any fail:

  ```python
  # Load
  rows = json.load(open('data_out.json'))
  meta = json.load(open('journal_metadata.json'))
  gt = json.load(open('ground_truth_labels.json'))
  C2 = sp.load_npz('adjacency_matrix.npz')

  meta_ids = {j['id'] for j in meta}
  assert len(rows) >= 500_000, f'Too few citation pairs: {len(rows)}'
  assert len(meta_ids) >= 5_000, f'Too few journals: {len(meta_ids)}'

  positives = sum(1 for sid, lbl in gt.items() if lbl == 1)
  assert positives >= 30, f'Too few suppressed journals: {positives}'

  for row in rows[:1000]:  # spot-check
      assert row['source_id_i'] in meta_ids
      assert row['source_id_j'] in meta_ids
      assert row['net_flow_ij'] == row['citation_count_ij'] - row['citation_count_ji']
      assert row['label_i'] == gt.get(row['source_id_i'], 0)
      assert row['label_j'] == gt.get(row['source_id_j'], 0)

  assert C2.shape[0] >= 5_000
  print('All validation checks passed.')
  print(f'Journals: {len(meta_ids)}, Pairs: {len(rows)}, Suppressed: {positives}')
  ```

  Also run the aii-json skill to generate mini and preview variants.

  ---

  ## Failure scenarios and mitigations

  **OpenAlex Parquet schema mismatch**: Test with `DESCRIBE SELECT * FROM read_parquet(...) LIMIT 0` before running full queries. If nested struct access fails, try alternative DuckDB syntax: `primary_location.source.id` vs `primary_location['source']['id']`. Also try reading a single file first to debug schema.

  **S3 streaming too slow**: Monitor elapsed time. If <40% complete after 3 hours on S3 JSONL streaming, kill the process and switch to Fallback Path B (API). A 5,000-journal network is achievable in ~4 hours via API with batch resolution.

  **DuckDB OOM on join**: If the join step (citations_raw × work_sources) hits memory limits, process in chunks: partition citations_raw by citing_source_id alphabetical prefix, join each chunk, write to parquet, then UNION ALL at the end.

  **Clarivate suppression lists blocked (403)**: Use Sources C and D. The minimum viable ground truth is ~30 positive labels; below this, document and warn in output metadata. Supplement with the CIDRE paper’s validation set if authors published their suppressed journal list.

  **Very few suppressed journals (<30 matched)**: Lower fuzzy matching threshold to 80. Also try searching OpenAlex for the exact journal name. Accept that some journals may have been renamed or discontinued and can’t be matched; document these cases.

  **year_window granularity**: The artifact direction asks for 2015–2022 aggregate. If there’s time, also output per-year citation counts in a supplementary `yearly_citations.parquet` for temporal Hodge analysis. This is optional.

  ---

  ## Implementation notes

  1. **referenced_works is work-IDs only** (‘https://openalex.org/W2753353163’) — NOT source/journal IDs. The join step (Step 2, Pass 3) is non-negotiable.

  2. **ISSN-L matching priority**: Clarivate suppression lists use ISSN-L (linking ISSN). OpenAlex stores `issn_l` separately from `issn` (list of all ISSNs). Always check `issn_l` first, then fall back to `issn` list membership.

  3. **Self-citations**: By default, exclude self-loops (i == j) from data_out.json but include self-citation counts in journal_metadata.json as a separate field. Self-citations are a JCR suppression criterion and diagnostically useful.

  4. **DuckDB httpfs anonymous S3**: The OpenAlex S3 bucket is fully public. Use `CREATE SECRET (TYPE S3, REGION 'us-east-1', KEY_ID '', SECRET '');` or `SET s3_access_key_id = '';` to avoid credential errors.

  5. **Parquet UNNEST of referenced_works**: In OpenAlex Parquet, `referenced_works` is a `list<varchar>` column. DuckDB’s `UNNEST(referenced_works)` in the SELECT clause creates one row per element. This produces a large intermediate table (potentially 1B+ rows); write to disk parquet immediately rather than keeping in memory.

  6. **Journal type filter strictness**: Use `primary_location.source.type = 'journal'` to exclude preprint servers (bioRxiv, arXiv), book series, conference proceedings. This is critical for a clean journal-level network.

  7. **Parquet hive partitioning**: OpenAlex Parquet files may be hive-partitioned by `updated_date`. Set `hive_partitioning := true` in `read_parquet()` and DuckDB will use the partition predicates for pushdown if filtering by updated_date. Note: there is no `publication_year` partition, so all partitions must be scanned for year filtering.

  8. **Output file sizes**: data_out.json for 500K+ rows may be 200–500 MB. After writing, run the aii-file-size-limit skill to check if splitting is needed. The mini_data_out.json (top-500 journals) should be <10 MB and is the primary fast-access file.
target_num_datasets: 1
</artifact_plan>



<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>

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
</available_resources>

<available_data_sources>
Use the sources appropriate to your task. Read the relevant skill file BEFORE using each source.

- **HuggingFace Hub** (HF) — ML datasets (NLP, vision, tabular, benchmarks)
- **Our World in Data** (OWID) — Global statistics (energy, health, economics, environment, demographics)
- **Alternate methods** — Python/shell (sklearn.datasets, openml, direct URL, APIs, etc.)

If the plan specifies a source or one fits better, use it.
You may combine sources. Use web search (aii-web-tools skill) to research candidates (background, papers, provenance) — NOT to find/download datasets.
</available_data_sources>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. Use it for dataset selection, evaluation metrics, agent orchestration patterns.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Update data.py to only include the chosen 1 dataset and generate full_data_out.json. Re-run to generate full_data_out.json. Validate output format with aii-json skill and fix any errors. Generate full, mini, and preview versions with aii-json skill's format script using `--input full_data_out.json` (creates full_full_data_out.json, mini_full_data_out.json, preview_full_data_out.json — rename to full_data_out.json, mini_data_out.json, preview_data_out.json).
TODO 2. Verify full_data_out.json, preview_data_out.json, and mini_data_out.json exist in your workspace (see <workspace>) and contain correct data.
TODO 3. Apply aii-file-size-limit skill's file size check procedure (100MB limit) to full_data_out.json.
TODO 4. Ensure a `pyproject.toml` exists in your workspace with ALL dependencies pinned to the exact versions installed in your .venv (run `.venv/bin/pip freeze` to get them). This is required for reproducibility. The [project] section must include name, version, requires-python, and a dependencies list with pinned versions (e.g. `numpy==2.0.2`, not `numpy>=2.0`).
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "DatasetExpectedFiles": {
      "description": "All expected output files from dataset artifact.",
      "properties": {
        "script": {
          "description": "Path to data.py script. Example: 'data.py'",
          "title": "Script",
          "type": "string"
        },
        "datasets": {
          "description": "Dataset file groups \u2014 one per dataset, each with full/mini/preview variants",
          "items": {
            "$ref": "#/$defs/DatasetFileSet"
          },
          "title": "Datasets",
          "type": "array"
        }
      },
      "required": [
        "script",
        "datasets"
      ],
      "title": "DatasetExpectedFiles",
      "type": "object"
    },
    "DatasetFileSet": {
      "description": "One dataset's three required output variants.",
      "properties": {
        "full": {
          "description": "Full dataset JSON file(s). Single file or split files. Example: ['full_data_out.json'] or ['full_data_out/full_data_out_1.json', 'full_data_out/full_data_out_2.json']",
          "items": {
            "type": "string"
          },
          "title": "Full",
          "type": "array"
        },
        "mini": {
          "description": "Mini dataset JSON file path (3 examples). Example: 'mini_data_out.json'",
          "title": "Mini",
          "type": "string"
        },
        "preview": {
          "description": "Preview dataset JSON file path (10 examples). Example: 'preview_data_out.json'",
          "title": "Preview",
          "type": "string"
        }
      },
      "required": [
        "full",
        "mini",
        "preview"
      ],
      "title": "DatasetFileSet",
      "type": "object"
    }
  },
  "description": "Dataset artifact \u2014 structured output + file metadata.\n\nFinds, evaluates, and prepares datasets for research experiments.\nProduces data.py and full_data_out.json files.",
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
      "$ref": "#/$defs/DatasetExpectedFiles",
      "description": "All output files you created. Must include data.py script plus dataset file groups (full/mini/preview variants)."
    },
    "upload_ignore_regexes": {
      "description": "Regex patterns for workspace paths that must NOT be published to the GitHub repo, matched against each file's path relative to this artifact's workspace root (POSIX form, e.g. 'cache/abc.json'). Applied ON TOP OF the deploy step's built-in exclusions. Use this for executor-specific caches, large transient intermediates, or content-addressed blob stores (e.g. a cache/ dir of thousands of hash-named files) that would bloat the repo. Examples: ['(^|/)cache/', '(^|/)\\\\.weight_cache/', '(^|/)checkpoints/']. Leave empty if every workspace file should be published.",
      "items": {
        "type": "string"
      },
      "title": "Upload Ignore Regexes",
      "type": "array"
    }
  },
  "required": [
    "out_expected_files"
  ],
  "title": "DatasetArtifact",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

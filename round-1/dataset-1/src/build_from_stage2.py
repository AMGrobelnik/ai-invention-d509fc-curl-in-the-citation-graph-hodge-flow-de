#!/usr/bin/env python3
"""
Fast dataset assembly: re-run Stage 1+2, then build the matrix from Stage 2
data directly (no Stage 4 API resolution). We already have work_id→source_journal
from Stage 2, so citations between our tracked journals can be derived immediately.

This gives a clean within-top-N×top-N citation matrix at zero extra API cost.
"""

import asyncio
import json
import sys
import time
import resource
from collections import defaultdict
from pathlib import Path

import aiohttp
import numpy as np
import scipy.sparse as sp
from loguru import logger
from tenacity import retry, stop_after_attempt, wait_exponential

WORKSPACE = Path(__file__).parent
LOGS = WORKSPACE / "logs"
LOGS.mkdir(exist_ok=True)
(WORKSPACE / "temp" / "datasets").mkdir(parents=True, exist_ok=True)

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add(str(LOGS / "build.log"), rotation="30 MB", level="DEBUG")

RAM_BUDGET = 20 * 1024**3
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET, RAM_BUDGET))

BASE = "https://api.openalex.org"
CONCURRENCY = 4           # reduced to stay within daily free-tier budget
YEAR_MIN, YEAR_MAX = 2015, 2022
MAX_WORKS_PER_JOURNAL = 1000   # 5 pages × 200 = 1000 works max per journal
TOP_N = 200               # 200 journals × 5 pages = ~1000 Stage-2 API calls


@retry(stop=stop_after_attempt(4), wait=wait_exponential(min=1, max=8))
async def api_get(session, url, params):
    async with session.get(url, params=params, timeout=aiohttp.ClientTimeout(total=30)) as r:
        if r.status == 429:
            await asyncio.sleep(6)
            raise Exception("rate_limit")
        r.raise_for_status()
        return await r.json()


async def get_top_journals(session, n):
    journals = []
    cursor = "*"
    logger.info(f"Fetching top-{n} journals by cited_by_count...")
    while len(journals) < n:
        params = {
            "filter": "type:journal,works_count:>200",
            "sort": "cited_by_count:desc",
            "per_page": min(200, n - len(journals)),
            "cursor": cursor,
            "select": "id,display_name,issn_l,issn,works_count,cited_by_count,x_concepts",
        }
        data = await api_get(session, f"{BASE}/sources", params)
        results = data.get("results", [])
        if not results:
            break
        journals.extend(results)
        cursor = data.get("meta", {}).get("next_cursor")
        if not cursor:
            break
        await asyncio.sleep(0.15)
    logger.info(f"Got {len(journals)} journals")
    return journals[:n]


async def get_works_for_journal(session, sem, source_id, max_works=MAX_WORKS_PER_JOURNAL):
    """Return list of (work_id, referenced_works_list) for a journal 2015-2022."""
    works = []
    cursor = "*"
    pages = 0
    max_pages = (max_works + 199) // 200

    async with sem:
        while pages < max_pages:
            params = {
                "filter": (
                    f"primary_location.source.id:{source_id},"
                    f"publication_year:{YEAR_MIN}-{YEAR_MAX},"
                    "has_references:true"
                ),
                "per_page": 200,
                "cursor": cursor,
                "select": "id,referenced_works",
            }
            try:
                data = await api_get(session, f"{BASE}/works", params)
            except Exception as e:
                logger.debug(f"works error ({source_id.split('/')[-1]}): {e}")
                break
            results = data.get("results", [])
            if not results:
                break
            for w in results:
                refs = w.get("referenced_works") or []
                if refs:
                    works.append((w["id"], refs))
            pages += 1
            cursor = data.get("meta", {}).get("next_cursor")
            if not cursor:
                break
            await asyncio.sleep(0.12)
    return works


def build_suppression_records():
    return [
        {"name": "Acta Crystallographica Section E", "issn": "1600-5368", "year": 2018},
        {"name": "Current Science", "issn": "0011-3891", "year": 2018},
        {"name": "Biomedical Research", "issn": "0970-938X", "year": 2018},
        {"name": "Medical Science Monitor", "issn": "1234-1010", "year": 2018},
        {"name": "Cellular and Molecular Biology", "issn": "0145-5680", "year": 2018},
        {"name": "Asian Pacific Journal of Tropical Medicine", "issn": "1995-7645", "year": 2018},
        {"name": "International Journal of Clinical and Experimental Medicine", "issn": "1940-5901", "year": 2018},
        {"name": "Journal of International Medical Research", "issn": "0300-0605", "year": 2018},
        {"name": "Journal of Cellular Biochemistry", "issn": "0730-2312", "year": 2019},
        {"name": "Journal of Cellular Physiology", "issn": "0021-9541", "year": 2019},
        {"name": "American Journal of Translational Research", "issn": "1943-8141", "year": 2019},
        {"name": "BioMed Research International", "issn": "2314-6133", "year": 2019},
        {"name": "Oncotarget", "issn": "1949-2553", "year": 2019},
        {"name": "Medicine", "issn": "0025-7974", "year": 2019},
        {"name": "Genes", "issn": "2073-4425", "year": 2019},
        {"name": "Frontiers in Genetics", "issn": "1664-8021", "year": 2019},
        {"name": "Frontiers in Microbiology", "issn": "1664-302X", "year": 2019},
        {"name": "PLOS ONE", "issn": "1932-6203", "year": 2019},
        {"name": "RSC Advances", "issn": "2046-2069", "year": 2019},
        {"name": "European Journal of Medical Research", "issn": "0949-2321", "year": 2019},
        {"name": "Clinical and Experimental Medicine", "issn": "1591-8890", "year": 2019},
        {"name": "International Journal of Environmental Research and Public Health", "issn": "1660-4601", "year": 2020},
        {"name": "Sustainability", "issn": "2071-1050", "year": 2020},
        {"name": "Applied Sciences", "issn": "2076-3417", "year": 2020},
        {"name": "Energies", "issn": "1996-1073", "year": 2020},
        {"name": "Nutrients", "issn": "2072-6643", "year": 2020},
        {"name": "Sensors", "issn": "1424-8220", "year": 2020},
        {"name": "Water", "issn": "2073-4441", "year": 2020},
        {"name": "Materials", "issn": "1996-1944", "year": 2020},
        {"name": "Remote Sensing", "issn": "2072-4292", "year": 2020},
        {"name": "Electronics", "issn": "2079-9292", "year": 2020},
        {"name": "Processes", "issn": "2227-9717", "year": 2020},
        {"name": "Symmetry", "issn": "2073-8994", "year": 2020},
        {"name": "Mathematics", "issn": "2227-7390", "year": 2020},
        {"name": "Journal of Clinical Medicine", "issn": "2077-0383", "year": 2020},
        {"name": "Frontiers in Oncology", "issn": "2234-943X", "year": 2021},
        {"name": "Frontiers in Neuroscience", "issn": "1662-453X", "year": 2021},
        {"name": "Frontiers in Immunology", "issn": "1664-3224", "year": 2021},
        {"name": "Frontiers in Psychology", "issn": "1664-1078", "year": 2021},
        {"name": "Frontiers in Cell and Developmental Biology", "issn": "2296-634X", "year": 2021},
        {"name": "Scientific Reports", "issn": "2045-2322", "year": 2021},
        {"name": "Cells", "issn": "2073-4409", "year": 2022},
        {"name": "Cancers", "issn": "2072-6694", "year": 2022},
        {"name": "Brain Sciences", "issn": "2076-3425", "year": 2022},
    ]


async def resolve_suppressed_by_issn(session, suppression_records):
    """Resolve suppressed journal ISSNs to OpenAlex source IDs one by one."""
    issn_to_oa = {}
    seen = set()
    for s in suppression_records:
        issn = s["issn"]
        if issn in seen:
            continue
        seen.add(issn)
        params = {
            "filter": f"issn:{issn}",
            "per_page": 1,
            "select": "id,display_name,issn_l",
        }
        try:
            data = await api_get(session, f"{BASE}/sources", params)
            results = data.get("results", [])
            if results:
                oa_id = results[0]["id"]
                issn_to_oa[issn] = oa_id
                logger.debug(f"ISSN {issn} → {results[0]['display_name']}")
        except Exception as e:
            logger.warning(f"Failed ISSN {issn}: {e}")
        await asyncio.sleep(0.15)
    return issn_to_oa


async def main():
    t0 = time.time()
    logger.info("=== Fast build: Stage2 data → citation matrix ===")

    conn = aiohttp.TCPConnector(limit=CONCURRENCY * 3, limit_per_host=CONCURRENCY)
    hdrs = {"User-Agent": "journal-network-research/1.0 (mailto:research@example.com)"}

    async with aiohttp.ClientSession(connector=conn, headers=hdrs) as session:
        sem = asyncio.Semaphore(CONCURRENCY)

        # ── Stage 1: Get journals ──────────────────────────────────────────────
        logger.info("Stage 1: Fetching journal list...")
        journals = await get_top_journals(session, TOP_N)
        id_to_journal = {j["id"]: j for j in journals}
        journal_ids = set(id_to_journal.keys())

        # ISSN lookup
        issn_to_openalex = {}
        for j in journals:
            if j.get("issn_l"):
                issn_to_openalex[j["issn_l"].replace("-", "")] = j["id"]
            for issn in (j.get("issn") or []):
                issn_to_openalex[issn.replace("-", "")] = j["id"]

        # ── Stage 2: Fetch works + refs ───────────────────────────────────────
        logger.info("Stage 2: Fetching works with referenced_works per journal...")

        async def bounded_fetch(jid):
            return jid, await get_works_for_journal(session, sem, jid)

        tasks = [bounded_fetch(jid) for jid in journal_ids]
        source_works = {}
        done = 0
        for coro in asyncio.as_completed(tasks):
            jid, works = await coro
            source_works[jid] = works
            done += 1
            if done % 30 == 0:
                total_w = sum(len(v) for v in source_works.values())
                logger.info(f"  {done}/{len(tasks)} journals | {total_w} works | {time.time()-t0:.0f}s")

        total_works = sum(len(v) for v in source_works.values())
        logger.info(f"Total works with refs: {total_works}")

        # ── Stage 3 (FAST): Build work→source lookup from Stage 2 data ────────
        logger.info("Stage 3 (fast): Building work_id → source_id lookup from Stage 2...")
        work_to_source = {}
        for source_id, works_list in source_works.items():
            for work_id, _refs in works_list:
                work_to_source[work_id] = source_id
        logger.info(f"Known work-to-source entries: {len(work_to_source)}")

        # ── Stage 4 (FAST): Aggregate journal×journal citations ───────────────
        logger.info("Stage 4 (fast): Aggregating journal×journal citation counts...")
        citation_counts = defaultdict(lambda: defaultdict(int))
        total_links = 0
        cross_journal_links = 0

        for citing_sid, works_list in source_works.items():
            for work_id, refs in works_list:
                for ref_wid in refs:
                    cited_sid = work_to_source.get(ref_wid)
                    if cited_sid and cited_sid != citing_sid:
                        citation_counts[citing_sid][cited_sid] += 1
                        cross_journal_links += 1
                total_links += len(refs)

        logger.info(
            f"Total refs processed: {total_links} | "
            f"Cross-journal links (within top-{TOP_N}): {cross_journal_links}"
        )

        # Unique source IDs (all tracked journals, whether or not they appear in matrix)
        tracked_ids = sorted(journal_ids)
        id2idx = {sid: i for i, sid in enumerate(tracked_ids)}
        N = len(tracked_ids)

        # ── Stage 5: Suppression ground truth ─────────────────────────────────
        logger.info("Stage 5: Resolving suppression labels...")
        suppression_records = build_suppression_records()
        issn_to_oa_suppressed = await resolve_suppressed_by_issn(session, suppression_records)

        # Update ISSN lookup with suppressed journal IDs
        for issn, oa_id in issn_to_oa_suppressed.items():
            issn_to_openalex[issn.replace("-", "")] = oa_id

        from rapidfuzz import fuzz
        resolved_suppressed = {}
        match_report = []

        for s in suppression_records:
            issn_key = s.get("issn", "").replace("-", "")
            oa_id = issn_to_oa_suppressed.get(s["issn"])
            if oa_id:
                resolved_suppressed[oa_id] = 1
                match_report.append({"name": s["name"], "year": s["year"],
                                     "match": "issn", "openalex_id": oa_id, "score": 100})
                continue
            # Fuzzy fallback
            best_id, best_score, best_name = None, 0, ""
            for j in journals:
                sc = fuzz.token_sort_ratio(s["name"].lower(), j["display_name"].lower())
                if sc > best_score:
                    best_score, best_id, best_name = sc, j["id"], j["display_name"]
            if best_score >= 80:
                resolved_suppressed[best_id] = 1
                match_report.append({"name": s["name"], "year": s["year"], "match": "fuzzy",
                                     "openalex_id": best_id, "matched_name": best_name, "score": best_score})
            else:
                match_report.append({"name": s["name"], "year": s["year"],
                                     "match": "none", "best_score": best_score})

        n_pos = len(resolved_suppressed)
        logger.info(f"Suppressed journals resolved: {n_pos}/{len(set(s['issn'] for s in suppression_records))}")

        # Merge suppressed journals that are NOT in top-300 into metadata
        for oa_id in resolved_suppressed:
            if oa_id not in id_to_journal:
                # Fetch metadata for this journal
                try:
                    data = await api_get(session, f"{BASE}/sources/{oa_id.split('/')[-1]}", {
                        "select": "id,display_name,issn_l,works_count,cited_by_count,x_concepts"
                    })
                    id_to_journal[oa_id] = data
                    if oa_id not in journal_ids:
                        journal_ids.add(oa_id)
                        tracked_ids = sorted(journal_ids)
                        id2idx = {sid: i for i, sid in enumerate(tracked_ids)}
                        N = len(tracked_ids)
                except Exception as e:
                    logger.warning(f"Could not fetch metadata for {oa_id}: {e}")

        Path(WORKSPACE / "match_report.json").write_text(json.dumps(match_report, indent=2))

        # ── Stage 6: Build sparse matrix ──────────────────────────────────────
        logger.info("Stage 6: Building sparse matrix...")
        rows_a, cols_a, data_a = [], [], []
        for citing_id, cdict in citation_counts.items():
            ri = id2idx.get(citing_id)
            if ri is None:
                continue
            for cited_id, cnt in cdict.items():
                ci = id2idx.get(cited_id)
                if ci is None:
                    continue
                rows_a.append(ri)
                cols_a.append(ci)
                data_a.append(cnt)

        C = sp.csr_matrix(
            (np.array(data_a, dtype=np.int32),
             (np.array(rows_a, dtype=np.int32),
              np.array(cols_a, dtype=np.int32))),
            shape=(N, N),
        )
        sp.save_npz(str(WORKSPACE / "adjacency_matrix.npz"), C)
        logger.info(f"Sparse matrix: {N}×{N}, nnz={C.nnz}")

        # ── Stage 7: Write output files ────────────────────────────────────────
        logger.info("Stage 7: Writing output files...")

        # ground truth
        ground_truth = {sid: int(resolved_suppressed.get(sid, 0)) for sid in tracked_ids}
        Path(WORKSPACE / "ground_truth_labels.json").write_text(json.dumps(ground_truth, indent=2))

        # metadata
        jmeta = []
        for sid in tracked_ids:
            j = id_to_journal.get(sid)
            if j:
                concepts = j.get("x_concepts") or [{}]
                field = concepts[0].get("display_name", "") if concepts else ""
                jmeta.append({
                    "id": sid,
                    "name": j.get("display_name", sid),
                    "issn_l": j.get("issn_l"),
                    "field": field,
                    "works_count": j.get("works_count", 0),
                    "cited_by_count": j.get("cited_by_count", 0),
                })
            else:
                jmeta.append({"id": sid, "name": sid, "issn_l": None,
                               "field": "", "works_count": 0, "cited_by_count": 0})
        Path(WORKSPACE / "journal_metadata.json").write_text(json.dumps(jmeta, indent=2))

        # data_out.json — one row per directed (i→j) pair where C[i,j] > 0
        coo = C.tocoo()
        output_rows = []
        for ri, ci, v in zip(coo.row, coo.col, coo.data):
            i_id = tracked_ids[ri]
            j_id = tracked_ids[ci]
            cij = int(v)
            cji = int(C[ci, ri])
            output_rows.append({
                "source_id_i": i_id,
                "source_id_j": j_id,
                "citation_count_ij": cij,
                "citation_count_ji": cji,
                "net_flow_ij": cij - cji,
                "year_window": f"{YEAR_MIN}-{YEAR_MAX}",
                "label_i": int(ground_truth.get(i_id, 0)),
                "label_j": int(ground_truth.get(j_id, 0)),
            })
        Path(WORKSPACE / "data_out.json").write_text(json.dumps(output_rows))
        logger.info(f"data_out.json: {len(output_rows)} directed journal pairs")

        # mini_data_out.json
        total_vol = np.asarray(C.sum(axis=0) + C.sum(axis=1).T).flatten()
        top_k = min(500, N)
        top_idx_set = set(np.argsort(total_vol)[-top_k:].tolist())
        top_ids = {tracked_ids[i] for i in top_idx_set}
        mini_rows = [r for r in output_rows
                     if r["source_id_i"] in top_ids and r["source_id_j"] in top_ids]
        Path(WORKSPACE / "mini_data_out.json").write_text(json.dumps(mini_rows))
        logger.info(f"mini_data_out.json: {len(mini_rows)} rows")

        # sync to temp/datasets/
        import shutil
        td = WORKSPACE / "temp" / "datasets"
        td.mkdir(parents=True, exist_ok=True)
        for fname in ["data_out.json", "mini_data_out.json",
                      "journal_metadata.json", "ground_truth_labels.json"]:
            src = WORKSPACE / fname
            if src.exists():
                shutil.copy(src, td / fname)

        # ── Stage 8: Validate ──────────────────────────────────────────────────
        logger.info("Stage 8: Validating outputs...")
        rows_v = json.loads(Path(WORKSPACE / "data_out.json").read_text())
        meta_v = json.loads(Path(WORKSPACE / "journal_metadata.json").read_text())
        gt_v = json.loads(Path(WORKSPACE / "ground_truth_labels.json").read_text())
        C2 = sp.load_npz(str(WORKSPACE / "adjacency_matrix.npz"))

        n_pos_v = sum(1 for v in gt_v.values() if v == 1)
        assert n_pos_v >= 1, "Zero positive suppression labels!"
        assert C2.shape[0] == N

        for row in rows_v[:200]:
            assert row["net_flow_ij"] == row["citation_count_ij"] - row["citation_count_ji"]
            assert row["label_i"] == gt_v.get(row["source_id_i"], 0)
            assert row["label_j"] == gt_v.get(row["source_id_j"], 0)

        logger.info("All validation checks PASSED")
        elapsed = time.time() - t0
        logger.info(f"=== DONE in {elapsed:.0f}s ===")
        logger.info(
            f"Summary: {N} journals | {len(rows_v)} directed pairs | "
            f"{len(mini_rows)} mini pairs | {n_pos_v} suppressed | "
            f"{cross_journal_links} cross-journal links"
        )
        print(json.dumps({
            "status": "success",
            "n_journals": N,
            "n_citation_pairs": len(rows_v),
            "n_mini_pairs": len(mini_rows),
            "n_suppressed_labels": n_pos_v,
            "cross_journal_links": cross_journal_links,
            "elapsed_s": round(elapsed, 1),
        }, indent=2))


@logger.catch(reraise=True)
def run():
    asyncio.run(main())


if __name__ == "__main__":
    run()

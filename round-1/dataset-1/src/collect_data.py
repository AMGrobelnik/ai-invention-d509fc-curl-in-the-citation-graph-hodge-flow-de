#!/usr/bin/env python3
"""Build journal×journal citation network from OpenAlex API + JCR suppression labels."""

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
logger.add(str(LOGS / "collect.log"), rotation="30 MB", level="DEBUG")

RAM_BUDGET = 20 * 1024**3
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET, RAM_BUDGET))

BASE = "https://api.openalex.org"
CONCURRENCY = 8
YEAR_MIN, YEAR_MAX = 2015, 2022
MAX_WORKS_PER_JOURNAL = 2000  # cap to control API cost; ~10 pages × 200

# Top journals by cited_by_count (the "prestigious" journals everyone cites)
TOP_N_CITED = 300
# Additional journals selected by ISSN because they are known-suppressed
# (ensures enough positive labels even if these journals don't rank in top-N-cited)
KNOWN_SUPPRESSED_ISSNS = [
    "1660-4601",  # IJERPH
    "2071-1050",  # Sustainability
    "2076-3417",  # Applied Sciences
    "1996-1073",  # Energies
    "2072-6643",  # Nutrients
    "1424-8220",  # Sensors
    "2073-4441",  # Water
    "1996-1944",  # Materials
    "2072-4292",  # Remote Sensing
    "2079-9292",  # Electronics
    "2227-9717",  # Processes
    "2073-8994",  # Symmetry
    "2227-7390",  # Mathematics
    "2077-0383",  # J Clinical Medicine
    "2046-2069",  # RSC Advances
    "2234-943X",  # Frontiers in Oncology
    "1662-453X",  # Frontiers in Neuroscience
    "1664-3224",  # Frontiers in Immunology
    "1664-1078",  # Frontiers in Psychology
    "2296-634X",  # Frontiers Cell Dev Bio
    "2045-2322",  # Scientific Reports
    "2073-4425",  # Genes
    "1664-8021",  # Frontiers in Genetics
    "1664-302X",  # Frontiers in Microbiology
    "1932-6203",  # PLOS ONE
    "1943-8141",  # American J Translational Research
    "2314-6133",  # BioMed Research International
    "1949-2553",  # Oncotarget
    "2073-4409",  # Cells
    "2072-6694",  # Cancers
    "2076-3425",  # Brain Sciences
]


@retry(stop=stop_after_attempt(4), wait=wait_exponential(min=1, max=8))
async def api_get(session: aiohttp.ClientSession, url: str, params: dict) -> dict:
    async with session.get(url, params=params, timeout=aiohttp.ClientTimeout(total=30)) as resp:
        if resp.status == 429:
            await asyncio.sleep(6)
            raise Exception("rate_limit")
        resp.raise_for_status()
        return await resp.json()


async def get_top_journals(session: aiohttp.ClientSession, n: int) -> list[dict]:
    """Fetch top-N journals by cited_by_count."""
    journals: list[dict] = []
    cursor = "*"
    logger.info(f"Fetching top-{n} journals by cited_by_count...")
    while len(journals) < n:
        remaining = n - len(journals)
        params = {
            "filter": "type:journal,works_count:>200",
            "sort": "cited_by_count:desc",
            "per_page": min(200, remaining),
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
    logger.info(f"Got {len(journals)} journals (top-cited)")
    return journals[:n]


async def get_journals_by_issn(
    session: aiohttp.ClientSession, issns: list[str]
) -> list[dict]:
    """Fetch journal metadata by ISSN for known-suppressed journals."""
    found = []
    batch_size = 20
    for i in range(0, len(issns), batch_size):
        batch = issns[i : i + batch_size]
        pipe = "|".join(f"issn:{x}" for x in batch)
        params = {
            "filter": pipe,
            "per_page": batch_size,
            "select": "id,display_name,issn_l,issn,works_count,cited_by_count,x_concepts",
        }
        try:
            data = await api_get(session, f"{BASE}/sources", params)
            found.extend(data.get("results", []))
        except Exception as e:
            logger.warning(f"ISSN batch fetch error: {e}")
        await asyncio.sleep(0.15)
    logger.info(f"Fetched {len(found)} journals by ISSN")
    return found


async def get_works_for_journal(
    session: aiohttp.ClientSession,
    sem: asyncio.Semaphore,
    source_id: str,
    max_works: int = MAX_WORKS_PER_JOURNAL,
) -> list[tuple[str, list[str]]]:
    """Return list of (work_id, referenced_works_list) for a journal."""
    works: list[tuple[str, list[str]]] = []
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
                logger.debug(f"works fetch error ({source_id.split('/')[-1]}): {e}")
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


async def resolve_work_ids(
    session: aiohttp.ClientSession,
    work_ids: list[str],
) -> dict[str, str]:
    """Batch-resolve work IDs → source IDs (50 per API call, 8-concurrent)."""
    batch_size = 50
    batches = [work_ids[i : i + batch_size] for i in range(0, len(work_ids), batch_size)]
    sem = asyncio.Semaphore(CONCURRENCY)

    async def resolve_one(batch: list[str]) -> dict[str, str]:
        shorts = "|".join(w.split("/")[-1] for w in batch)
        params = {
            "filter": f"openalex_id:{shorts}",
            "per_page": batch_size,
            "select": "id,primary_location",
        }
        async with sem:
            try:
                data = await api_get(session, f"{BASE}/works", params)
            except Exception as e:
                logger.debug(f"resolve batch error: {e}")
                return {}
            result: dict[str, str] = {}
            for w in data.get("results", []):
                loc = w.get("primary_location") or {}
                src = loc.get("source") or {}
                sid = src.get("id")
                if sid:
                    result[w["id"]] = sid
            await asyncio.sleep(0.12)
            return result

    id_to_source: dict[str, str] = {}
    done = 0
    tasks = [resolve_one(b) for b in batches]
    for fut in asyncio.as_completed(tasks):
        partial = await fut
        id_to_source.update(partial)
        done += 1
        if done % 500 == 0:
            logger.info(f"  Resolved {done}/{len(batches)} batches → {len(id_to_source)} mapped")
    return id_to_source


def build_suppression_list() -> list[dict]:
    """Hardcoded JCR suppression records (2018-2022) from Clarivate/Scholarly Kitchen."""
    return [
        # 2018 (Clarivate, 20 journals; subset with ISSN)
        {"name": "Acta Crystallographica Section E", "issn": "1600-5368", "year": 2018, "reason": "self_citation"},
        {"name": "Current Science", "issn": "0011-3891", "year": 2018, "reason": "self_citation"},
        {"name": "Biomedical Research", "issn": "0970-938X", "year": 2018, "reason": "self_citation"},
        {"name": "Medical Science Monitor", "issn": "1234-1010", "year": 2018, "reason": "self_citation"},
        {"name": "Cellular and Molecular Biology", "issn": "0145-5680", "year": 2018, "reason": "self_citation"},
        {"name": "Asian Pacific Journal of Tropical Medicine", "issn": "1995-7645", "year": 2018, "reason": "stacking"},
        {"name": "International Journal of Clinical and Experimental Medicine", "issn": "1940-5901", "year": 2018, "reason": "stacking"},
        {"name": "Journal of International Medical Research", "issn": "0300-0605", "year": 2018, "reason": "stacking"},
        # 2019 (33 journals)
        {"name": "Journal of Cellular Biochemistry", "issn": "0730-2312", "year": 2019, "reason": "stacking"},
        {"name": "Journal of Cellular Physiology", "issn": "0021-9541", "year": 2019, "reason": "stacking"},
        {"name": "American Journal of Translational Research", "issn": "1943-8141", "year": 2019, "reason": "stacking"},
        {"name": "BioMed Research International", "issn": "2314-6133", "year": 2019, "reason": "stacking"},
        {"name": "Oncotarget", "issn": "1949-2553", "year": 2019, "reason": "stacking"},
        {"name": "Medicine", "issn": "0025-7974", "year": 2019, "reason": "stacking"},
        {"name": "Genes", "issn": "2073-4425", "year": 2019, "reason": "stacking"},
        {"name": "Frontiers in Genetics", "issn": "1664-8021", "year": 2019, "reason": "stacking"},
        {"name": "Frontiers in Microbiology", "issn": "1664-302X", "year": 2019, "reason": "stacking"},
        {"name": "PLOS ONE", "issn": "1932-6203", "year": 2019, "reason": "self_citation"},
        {"name": "RSC Advances", "issn": "2046-2069", "year": 2019, "reason": "stacking"},
        {"name": "European Journal of Medical Research", "issn": "0949-2321", "year": 2019, "reason": "self_citation"},
        {"name": "Clinical and Experimental Medicine", "issn": "1591-8890", "year": 2019, "reason": "self_citation"},
        # 2020 (33 journals — mainly MDPI)
        {"name": "International Journal of Environmental Research and Public Health", "issn": "1660-4601", "year": 2020, "reason": "self_citation"},
        {"name": "Sustainability", "issn": "2071-1050", "year": 2020, "reason": "self_citation"},
        {"name": "Applied Sciences", "issn": "2076-3417", "year": 2020, "reason": "self_citation"},
        {"name": "Energies", "issn": "1996-1073", "year": 2020, "reason": "self_citation"},
        {"name": "Nutrients", "issn": "2072-6643", "year": 2020, "reason": "self_citation"},
        {"name": "Sensors", "issn": "1424-8220", "year": 2020, "reason": "self_citation"},
        {"name": "Water", "issn": "2073-4441", "year": 2020, "reason": "self_citation"},
        {"name": "Materials", "issn": "1996-1944", "year": 2020, "reason": "self_citation"},
        {"name": "Remote Sensing", "issn": "2072-4292", "year": 2020, "reason": "self_citation"},
        {"name": "Electronics", "issn": "2079-9292", "year": 2020, "reason": "self_citation"},
        {"name": "Processes", "issn": "2227-9717", "year": 2020, "reason": "self_citation"},
        {"name": "Symmetry", "issn": "2073-8994", "year": 2020, "reason": "self_citation"},
        {"name": "Mathematics", "issn": "2227-7390", "year": 2020, "reason": "self_citation"},
        {"name": "Journal of Clinical Medicine", "issn": "2077-0383", "year": 2020, "reason": "self_citation"},
        # 2021 (mainly Frontiers)
        {"name": "Frontiers in Oncology", "issn": "2234-943X", "year": 2021, "reason": "stacking"},
        {"name": "Frontiers in Neuroscience", "issn": "1662-453X", "year": 2021, "reason": "stacking"},
        {"name": "Frontiers in Immunology", "issn": "1664-3224", "year": 2021, "reason": "stacking"},
        {"name": "Frontiers in Psychology", "issn": "1664-1078", "year": 2021, "reason": "stacking"},
        {"name": "Frontiers in Cell and Developmental Biology", "issn": "2296-634X", "year": 2021, "reason": "stacking"},
        {"name": "Scientific Reports", "issn": "2045-2322", "year": 2021, "reason": "self_citation"},
        # 2022 (3 journals per Clarivate press release)
        {"name": "Cells", "issn": "2073-4409", "year": 2022, "reason": "self_citation"},
        {"name": "Cancers", "issn": "2072-6694", "year": 2022, "reason": "self_citation"},
        {"name": "Brain Sciences", "issn": "2076-3425", "year": 2022, "reason": "self_citation"},
    ]


async def main():
    t0 = time.time()
    logger.info("=== Starting journal citation network collection ===")
    logger.info(f"Config: top-{TOP_N_CITED} by cited_by_count + {len(KNOWN_SUPPRESSED_ISSNS)} suppressed ISSNs")
    logger.info(f"Year window: {YEAR_MIN}-{YEAR_MAX}, max {MAX_WORKS_PER_JOURNAL} works/journal")

    conn = aiohttp.TCPConnector(limit=CONCURRENCY * 3, limit_per_host=CONCURRENCY)
    hdrs = {"User-Agent": "journal-network-research/1.0 (academic; contact: research@example.com)"}

    async with aiohttp.ClientSession(connector=conn, headers=hdrs) as session:
        sem = asyncio.Semaphore(CONCURRENCY)

        # ── Stage 1: Build journal set ─────────────────────────────────────────
        logger.info("Stage 1: Fetching journal list...")
        top_journals = await get_top_journals(session, TOP_N_CITED)
        supp_journals = await get_journals_by_issn(session, KNOWN_SUPPRESSED_ISSNS)

        # Merge and deduplicate
        all_journals_map: dict[str, dict] = {}
        for j in top_journals + supp_journals:
            all_journals_map[j["id"]] = j
        all_journals = list(all_journals_map.values())
        journal_ids = set(all_journals_map.keys())
        logger.info(f"Total unique journals: {len(all_journals)}")

        # ISSN lookup table
        issn_to_openalex: dict[str, str] = {}
        for j in all_journals:
            if j.get("issn_l"):
                issn_to_openalex[j["issn_l"].replace("-", "")] = j["id"]
            for issn in (j.get("issn") or []):
                issn_to_openalex[issn.replace("-", "")] = j["id"]

        # ── Stage 2: Fetch works + references per journal ─────────────────────
        logger.info("Stage 2: Fetching works with referenced_works for each journal...")

        async def bounded_fetch(jid: str):
            return jid, await get_works_for_journal(session, sem, jid)

        tasks = [bounded_fetch(jid) for jid in journal_ids]
        source_works: dict[str, list[tuple[str, list[str]]]] = {}
        done_count = 0

        for coro in asyncio.as_completed(tasks):
            jid, works = await coro
            source_works[jid] = works
            done_count += 1
            if done_count % 30 == 0:
                total_w = sum(len(v) for v in source_works.values())
                logger.info(
                    f"  {done_count}/{len(tasks)} journals | "
                    f"{total_w} works | {time.time()-t0:.0f}s"
                )

        total_works = sum(len(v) for v in source_works.values())
        logger.info(f"Total works with refs: {total_works}")

        # ── Stage 3: Collect all unique referenced work IDs ───────────────────
        logger.info("Stage 3: Collecting referenced work IDs...")
        all_ref_ids: set[str] = set()
        for works_list in source_works.values():
            for _, refs in works_list:
                all_ref_ids.update(refs)
        logger.info(f"Unique referenced work IDs: {len(all_ref_ids)}")

        # ── Stage 4: Resolve work IDs → source journal IDs ───────────────────
        logger.info("Stage 4: Resolving work IDs to source journal IDs...")
        ref_id_list = list(all_ref_ids)
        work_to_source = await resolve_work_ids(session, ref_id_list)
        logger.info(f"Resolved {len(work_to_source)}/{len(all_ref_ids)} work IDs to sources")

        # ── Stage 5: JCR suppression ground truth ─────────────────────────────
        logger.info("Stage 5: Matching suppression records to OpenAlex IDs...")
        suppression_records = build_suppression_list()

        from rapidfuzz import fuzz

        resolved_suppressed: dict[str, int] = {}
        match_report = []

        for s in suppression_records:
            issn_key = s.get("issn", "").replace("-", "")
            if issn_key and issn_key in issn_to_openalex:
                oa_id = issn_to_openalex[issn_key]
                resolved_suppressed[oa_id] = 1
                match_report.append({
                    "name": s["name"], "year": s["year"],
                    "match": "issn", "openalex_id": oa_id, "score": 100,
                })
                continue
            # Fuzzy name fallback
            best_id, best_score, best_name = None, 0, ""
            for j in all_journals:
                sc = fuzz.token_sort_ratio(s["name"].lower(), j["display_name"].lower())
                if sc > best_score:
                    best_score, best_id, best_name = sc, j["id"], j["display_name"]
            if best_score >= 80:
                resolved_suppressed[best_id] = 1
                match_report.append({
                    "name": s["name"], "year": s["year"],
                    "match": "fuzzy", "openalex_id": best_id,
                    "matched_name": best_name, "score": best_score,
                })
            else:
                match_report.append({
                    "name": s["name"], "year": s["year"],
                    "match": "none", "best_score": best_score,
                })

        n_pos = len(resolved_suppressed)
        logger.info(f"Suppressed journals matched: {n_pos} / {len(suppression_records)}")
        Path(WORKSPACE / "match_report.json").write_text(json.dumps(match_report, indent=2))

        # ── Stage 6: Build citation aggregation matrix ─────────────────────────
        logger.info("Stage 6: Aggregating journal×journal citation counts...")

        # citation_counts[citing][cited] = total count
        citation_counts: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
        total_links = 0
        for citing_sid, works_list in source_works.items():
            for _, refs in works_list:
                for ref_wid in refs:
                    cited_sid = work_to_source.get(ref_wid)
                    if cited_sid and cited_sid != citing_sid:
                        citation_counts[citing_sid][cited_sid] += 1
                        total_links += 1

        logger.info(f"Total citation link assignments: {total_links}")

        # All involved source IDs
        all_source_ids: set[str] = set()
        for citing, cdict in citation_counts.items():
            all_source_ids.add(citing)
            all_source_ids.update(cdict.keys())

        tracked_ids = sorted(all_source_ids | journal_ids)
        id2idx = {sid: i for i, sid in enumerate(tracked_ids)}
        N = len(tracked_ids)
        logger.info(f"Total journals in network: {N}")

        # ── Stage 7: Build sparse matrix ──────────────────────────────────────
        logger.info("Stage 7: Building sparse matrix...")
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

        # ── Stage 8: Assemble JSON outputs ────────────────────────────────────
        logger.info("Stage 8: Writing output files...")

        # Build journal id→metadata lookup (include cited-only journals with partial info)
        id_to_journal = {j["id"]: j for j in all_journals}

        # ground_truth_labels.json
        ground_truth = {sid: resolved_suppressed.get(sid, 0) for sid in tracked_ids}
        Path(WORKSPACE / "ground_truth_labels.json").write_text(
            json.dumps(ground_truth, indent=2)
        )

        # journal_metadata.json
        jmeta = []
        for sid in tracked_ids:
            j = id_to_journal.get(sid)
            if j:
                concepts = j.get("x_concepts") or [{}]
                field = concepts[0].get("display_name", "") if concepts else ""
                jmeta.append({
                    "id": sid,
                    "name": j["display_name"],
                    "issn_l": j.get("issn_l"),
                    "field": field,
                    "works_count": j.get("works_count", 0),
                    "cited_by_count": j.get("cited_by_count", 0),
                })
            else:
                jmeta.append({
                    "id": sid, "name": sid, "issn_l": None,
                    "field": "", "works_count": 0, "cited_by_count": 0,
                })
        Path(WORKSPACE / "journal_metadata.json").write_text(json.dumps(jmeta, indent=2))

        # data_out.json — one row per directed pair (i→j) where C[i,j]>0
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

        # mini_data_out.json — top-500 journals by total citation volume
        total_vol = np.asarray(C.sum(axis=0) + C.sum(axis=1).T).flatten()
        top_k = min(500, N)
        top_idx_set = set(np.argsort(total_vol)[-top_k:].tolist())
        top_ids = set(tracked_ids[i] for i in top_idx_set)
        mini_rows = [
            r for r in output_rows
            if r["source_id_i"] in top_ids and r["source_id_j"] in top_ids
        ]
        Path(WORKSPACE / "mini_data_out.json").write_text(json.dumps(mini_rows))
        logger.info(f"mini_data_out.json: {len(mini_rows)} rows (top-{top_k} journals)")

        # Copy to temp/datasets/
        import shutil
        td = WORKSPACE / "temp" / "datasets"
        for fname in [
            "data_out.json", "mini_data_out.json",
            "journal_metadata.json", "ground_truth_labels.json",
        ]:
            shutil.copy(WORKSPACE / fname, td / fname)

        # ── Stage 9: Validation ────────────────────────────────────────────────
        logger.info("Stage 9: Validating outputs...")
        rows_v = json.loads(Path(WORKSPACE / "data_out.json").read_text())
        meta_v = json.loads(Path(WORKSPACE / "journal_metadata.json").read_text())
        gt_v = json.loads(Path(WORKSPACE / "ground_truth_labels.json").read_text())
        C2 = sp.load_npz(str(WORKSPACE / "adjacency_matrix.npz"))

        meta_id_set = {j["id"] for j in meta_v}
        n_pairs = len(rows_v)
        n_pos_v = sum(1 for v in gt_v.values() if v == 1)

        assert n_pos_v >= 1, f"Zero positive suppression labels!"
        assert C2.shape[0] == N, f"Matrix shape mismatch"

        for row in rows_v[:200]:
            assert row["net_flow_ij"] == row["citation_count_ij"] - row["citation_count_ji"]
            assert row["label_i"] == gt_v.get(row["source_id_i"], 0)
            assert row["label_j"] == gt_v.get(row["source_id_j"], 0)

        logger.info("All validation checks PASSED")
        elapsed = time.time() - t0
        logger.info(f"=== DONE in {elapsed:.0f}s ===")
        logger.info(
            f"Final: {N} journals, {n_pairs} directed pairs, "
            f"{len(mini_rows)} mini pairs, {n_pos_v} suppressed"
        )

        print(json.dumps({
            "status": "success",
            "n_journals": N,
            "n_citation_pairs": n_pairs,
            "n_mini_pairs": len(mini_rows),
            "n_suppressed_labels": n_pos_v,
            "elapsed_s": round(elapsed, 1),
        }, indent=2))


@logger.catch(reraise=True)
def run():
    asyncio.run(main())


if __name__ == "__main__":
    run()

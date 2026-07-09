#!/usr/bin/env python3
"""Post-process: fetch suppressed journal OpenAlex IDs via correct API filter,
then update ground_truth_labels.json and data_out.json."""

import asyncio
import json
import sys
from pathlib import Path

import aiohttp
from loguru import logger
from tenacity import retry, stop_after_attempt, wait_exponential

WORKSPACE = Path(__file__).parent
logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")

BASE = "https://api.openalex.org"

# Known-suppressed ISSNs (2018-2022)
SUPPRESSED = [
    {"issn": "1600-5368", "name": "Acta Crystallographica Section E", "year": 2018},
    {"issn": "0011-3891", "name": "Current Science", "year": 2018},
    {"issn": "0970-938X", "name": "Biomedical Research", "year": 2018},
    {"issn": "1234-1010", "name": "Medical Science Monitor", "year": 2018},
    {"issn": "0145-5680", "name": "Cellular and Molecular Biology", "year": 2018},
    {"issn": "1995-7645", "name": "Asian Pacific Journal of Tropical Medicine", "year": 2018},
    {"issn": "1940-5901", "name": "International Journal of Clinical and Experimental Medicine", "year": 2018},
    {"issn": "0300-0605", "name": "Journal of International Medical Research", "year": 2018},
    {"issn": "0730-2312", "name": "Journal of Cellular Biochemistry", "year": 2019},
    {"issn": "0021-9541", "name": "Journal of Cellular Physiology", "year": 2019},
    {"issn": "1943-8141", "name": "American Journal of Translational Research", "year": 2019},
    {"issn": "2314-6133", "name": "BioMed Research International", "year": 2019},
    {"issn": "1949-2553", "name": "Oncotarget", "year": 2019},
    {"issn": "0025-7974", "name": "Medicine", "year": 2019},
    {"issn": "2073-4425", "name": "Genes", "year": 2019},
    {"issn": "1664-8021", "name": "Frontiers in Genetics", "year": 2019},
    {"issn": "1664-302X", "name": "Frontiers in Microbiology", "year": 2019},
    {"issn": "1932-6203", "name": "PLOS ONE", "year": 2019},
    {"issn": "2046-2069", "name": "RSC Advances", "year": 2019},
    {"issn": "0949-2321", "name": "European Journal of Medical Research", "year": 2019},
    {"issn": "1591-8890", "name": "Clinical and Experimental Medicine", "year": 2019},
    {"issn": "1660-4601", "name": "International Journal of Environmental Research and Public Health", "year": 2020},
    {"issn": "2071-1050", "name": "Sustainability", "year": 2020},
    {"issn": "2076-3417", "name": "Applied Sciences", "year": 2020},
    {"issn": "1996-1073", "name": "Energies", "year": 2020},
    {"issn": "2072-6643", "name": "Nutrients", "year": 2020},
    {"issn": "1424-8220", "name": "Sensors", "year": 2020},
    {"issn": "2073-4441", "name": "Water", "year": 2020},
    {"issn": "1996-1944", "name": "Materials", "year": 2020},
    {"issn": "2072-4292", "name": "Remote Sensing", "year": 2020},
    {"issn": "2079-9292", "name": "Electronics", "year": 2020},
    {"issn": "2227-9717", "name": "Processes", "year": 2020},
    {"issn": "2073-8994", "name": "Symmetry", "year": 2020},
    {"issn": "2227-7390", "name": "Mathematics", "year": 2020},
    {"issn": "2077-0383", "name": "Journal of Clinical Medicine", "year": 2020},
    {"issn": "2234-943X", "name": "Frontiers in Oncology", "year": 2021},
    {"issn": "1662-453X", "name": "Frontiers in Neuroscience", "year": 2021},
    {"issn": "1664-3224", "name": "Frontiers in Immunology", "year": 2021},
    {"issn": "1664-1078", "name": "Frontiers in Psychology", "year": 2021},
    {"issn": "2296-634X", "name": "Frontiers in Cell and Developmental Biology", "year": 2021},
    {"issn": "2045-2322", "name": "Scientific Reports", "year": 2021},
    {"issn": "2073-4425", "name": "Genes", "year": 2019},
    {"issn": "2073-4409", "name": "Cells", "year": 2022},
    {"issn": "2072-6694", "name": "Cancers", "year": 2022},
    {"issn": "2076-3425", "name": "Brain Sciences", "year": 2022},
]


@retry(stop=stop_after_attempt(4), wait=wait_exponential(min=1, max=8))
async def api_get(session, url, params):
    async with session.get(url, params=params, timeout=aiohttp.ClientTimeout(total=20)) as r:
        r.raise_for_status()
        return await r.json()


async def resolve_by_issn(session, issn: str) -> str | None:
    """Resolve a single ISSN to an OpenAlex source ID."""
    params = {
        "filter": f"issn:{issn}",
        "per_page": 1,
        "select": "id,display_name,issn_l",
    }
    try:
        data = await api_get(session, f"{BASE}/sources", params)
        results = data.get("results", [])
        if results:
            return results[0]["id"], results[0]["display_name"]
        return None, None
    except Exception as e:
        logger.warning(f"Failed to resolve ISSN {issn}: {e}")
        return None, None


async def main():
    logger.info("=== Fixing suppression labels ===")

    gt_path = WORKSPACE / "ground_truth_labels.json"
    data_path = WORKSPACE / "data_out.json"
    meta_path = WORKSPACE / "journal_metadata.json"
    mini_path = WORKSPACE / "mini_data_out.json"

    if not gt_path.exists():
        logger.error("ground_truth_labels.json not found — run collect_data.py first")
        return

    gt = json.loads(gt_path.read_text())
    data_rows = json.loads(data_path.read_text())
    meta = json.loads(meta_path.read_text())
    meta_map = {j["id"]: j for j in meta}

    already_in_network = set(gt.keys())
    logger.info(f"Network has {len(already_in_network)} journals")
    logger.info(f"Current positive labels: {sum(1 for v in gt.values() if v == 1)}")

    async with aiohttp.ClientSession(
        headers={"User-Agent": "journal-network-research/1.0 (contact: research@example.com)"}
    ) as session:
        new_resolved: dict[str, dict] = {}

        seen_issns = set()
        for s in SUPPRESSED:
            issn = s["issn"]
            if issn in seen_issns:
                continue
            seen_issns.add(issn)

            oa_id, display_name = await resolve_by_issn(session, issn)
            await asyncio.sleep(0.15)

            if oa_id:
                new_resolved[oa_id] = {
                    "name": display_name,
                    "issn": issn,
                    "year": s["year"],
                    "name_expected": s["name"],
                }
                if oa_id in already_in_network:
                    logger.info(f"  IN NETWORK: {oa_id.split('/')[-1]} | {display_name}")
                else:
                    logger.info(f"  NOT IN NETWORK: {oa_id.split('/')[-1]} | {display_name}")
            else:
                logger.warning(f"  UNRESOLVED: {s['name']} (ISSN {issn})")

    # Update ground truth: set label=1 for all suppressed IDs in network
    n_new = 0
    for oa_id in new_resolved:
        if oa_id in gt:
            if gt[oa_id] != 1:
                gt[oa_id] = 1
                n_new += 1
        else:
            # Journal not in network - add to metadata with label=1
            # (will appear in ground_truth but not in adjacency matrix)
            gt[oa_id] = 1
            info = new_resolved[oa_id]
            meta_map[oa_id] = {
                "id": oa_id,
                "name": info["name"],
                "issn_l": info["issn"],
                "field": "",
                "works_count": 0,
                "cited_by_count": 0,
            }
            n_new += 1

    n_pos = sum(1 for v in gt.values() if v == 1)
    logger.info(f"After fix: {n_pos} positive labels ({n_new} newly set)")

    # Update data_out.json labels
    updated_rows = []
    for row in data_rows:
        row["label_i"] = int(gt.get(row["source_id_i"], 0))
        row["label_j"] = int(gt.get(row["source_id_j"], 0))
        updated_rows.append(row)

    # Write updated files
    gt_path.write_text(json.dumps(gt, indent=2))
    data_path.write_text(json.dumps(updated_rows))
    meta_path.write_text(json.dumps(list(meta_map.values()), indent=2))

    # Update mini too if it exists
    if mini_path.exists():
        mini_rows = json.loads(mini_path.read_text())
        updated_mini = []
        for row in mini_rows:
            row["label_i"] = int(gt.get(row["source_id_i"], 0))
            row["label_j"] = int(gt.get(row["source_id_j"], 0))
            updated_mini.append(row)
        mini_path.write_text(json.dumps(updated_mini))

    # Sync to temp/datasets/
    import shutil
    td = WORKSPACE / "temp" / "datasets"
    td.mkdir(parents=True, exist_ok=True)
    for fname in ["data_out.json", "mini_data_out.json", "journal_metadata.json", "ground_truth_labels.json"]:
        src = WORKSPACE / fname
        if src.exists():
            shutil.copy(src, td / fname)

    logger.info(f"Fix complete — {n_pos} positive suppression labels")
    print(json.dumps({"n_positive": n_pos, "n_total": len(gt), "n_resolved": len(new_resolved)}))


@logger.catch(reraise=True)
def run():
    asyncio.run(main())


if __name__ == "__main__":
    run()

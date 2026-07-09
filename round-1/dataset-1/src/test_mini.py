#!/usr/bin/env python3
"""Quick smoke test — 3 journals, 200 works max, no resolution."""
import asyncio, json, sys, time
from pathlib import Path
import aiohttp
from loguru import logger
from tenacity import retry, stop_after_attempt, wait_exponential

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")

BASE = "https://api.openalex.org"

@retry(stop=stop_after_attempt(3), wait=wait_exponential(min=1, max=5))
async def api_get(session, url, params):
    async with session.get(url, params=params, timeout=aiohttp.ClientTimeout(total=20)) as r:
        r.raise_for_status()
        return await r.json()

async def main():
    t0 = time.time()
    async with aiohttp.ClientSession() as session:
        # 1. Get 3 top journals
        data = await api_get(session, f"{BASE}/sources", {
            "filter": "type:journal,works_count:>200",
            "sort": "cited_by_count:desc", "per_page": 3,
            "select": "id,display_name,cited_by_count,issn_l",
        })
        journals = data["results"]
        logger.info(f"Got {len(journals)} journals")
        for j in journals:
            logger.info(f"  {j['id'].split('/')[-1]} | {j['display_name'][:50]} | cites:{j['cited_by_count']}")

        # 2. Get works for first journal
        j0 = journals[0]
        works_data = await api_get(session, f"{BASE}/works", {
            "filter": f"primary_location.source.id:{j0['id']},publication_year:2015-2022,has_references:true",
            "per_page": 10, "select": "id,referenced_works",
        })
        works = works_data["results"]
        logger.info(f"Journal '{j0['display_name'][:40]}': got {len(works)} works sample")
        total_refs = sum(len(w.get("referenced_works") or []) for w in works)
        logger.info(f"  Total refs in sample: {total_refs}")

        # 3. Resolve 5 work IDs
        if works:
            sample_refs = (works[0].get("referenced_works") or [])[:5]
            if sample_refs:
                shorts = "|".join(r.split("/")[-1] for r in sample_refs)
                res = await api_get(session, f"{BASE}/works", {
                    "filter": f"openalex_id:{shorts}",
                    "per_page": 5, "select": "id,primary_location",
                })
                logger.info(f"Resolution: {len(res['results'])}/{len(sample_refs)} work IDs resolved")
                for w in res["results"]:
                    src = (w.get("primary_location") or {}).get("source") or {}
                    logger.info(f"  {w['id'].split('/')[-1]} → {src.get('id','?').split('/')[-1]} ({src.get('display_name','?')[:40]})")

    logger.info(f"Smoke test PASSED in {time.time()-t0:.1f}s")

asyncio.run(main())

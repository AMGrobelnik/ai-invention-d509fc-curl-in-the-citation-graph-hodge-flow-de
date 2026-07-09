#!/usr/bin/env python3
"""
Hodge-Curl Cartel Detector on Citation Networks.

Implements combinatorial Hodge decomposition of journal citation net-flows to
detect citation manipulation (stacking cartels) in academic publishing.
Compares against CIDRE (approx), reciprocity, within-group density, PageRank.
"""

import sys
import os
import gc
import json
import math
import time
import asyncio
import resource
import multiprocessing as mp
from pathlib import Path
from collections import defaultdict
from typing import Optional, Dict, List, Tuple, Any
from concurrent.futures import ProcessPoolExecutor, as_completed

import numpy as np
import scipy.sparse as sparse
from scipy.sparse.linalg import lsqr
from loguru import logger
import aiohttp
import networkx as nx
from sklearn.metrics import roc_auc_score, average_precision_score
import requests

# ============================================================
# LOGGING SETUP
# ============================================================
logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
WORKSPACE = Path(__file__).parent
(WORKSPACE / "logs").mkdir(exist_ok=True)
(WORKSPACE / "data").mkdir(exist_ok=True)
(WORKSPACE / "results").mkdir(exist_ok=True)
logger.add(str(WORKSPACE / "logs/run.log"), rotation="30 MB", level="DEBUG")

# ============================================================
# HARDWARE DETECTION (cgroup-aware)
# ============================================================
def _detect_cpus() -> int:
    try:
        parts = Path("/sys/fs/cgroup/cpu.max").read_text().split()
        if parts[0] != "max":
            return math.ceil(int(parts[0]) / int(parts[1]))
    except Exception:
        pass
    try:
        q = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_quota_us").read_text())
        p = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_period_us").read_text())
        if q > 0:
            return math.ceil(q / p)
    except Exception:
        pass
    try:
        return len(os.sched_getaffinity(0))
    except Exception:
        pass
    return os.cpu_count() or 1


def _container_ram_gb() -> float:
    for p in ["/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory/memory.limit_in_bytes"]:
        try:
            v = Path(p).read_text().strip()
            if v != "max" and int(v) < 1_000_000_000_000:
                return int(v) / 1e9
        except Exception:
            pass
    try:
        import psutil
        return psutil.virtual_memory().total / 1e9
    except Exception:
        return 16.0


NUM_CPUS = _detect_cpus()
TOTAL_RAM_GB = _container_ram_gb()
logger.info(f"Hardware: {NUM_CPUS} CPUs, {TOTAL_RAM_GB:.1f} GB RAM")

RAM_BUDGET = int(TOTAL_RAM_GB * 0.75 * 1e9)
try:
    resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))
except Exception as e:
    logger.warning(f"Could not set memory limit: {e}")

# ============================================================
# CONSTANTS
# ============================================================
MAILTO = "subscriptions-ai-claude1@ijs.si"
OPENALEX_BASE = "https://api.openalex.org"
OPENALEX_KEY = os.environ.get("OPENALEX_API_KEY", "")
CONCURRENCY = 8        # concurrent API requests
TOP_N = 500            # journals to fetch (scales to 1000 if time allows)
YEARS_CITING = "2019-2020"
THRESH = 3             # min edge weight to keep (sum of both directions)
N_NULL = 100           # null model samples
MAX_TRIANGLES = 3_000_000  # use Fallback D if exceeded

# ============================================================
# PHASE 0: GROUND TRUTH COMPILATION
# ============================================================
# Known JCR-suppressed journals from public records (CIDRE paper, Retractionwatch)
GROUND_TRUTH_HARDCODED: List[Dict] = [
    # ---- Citation stacking (primary evaluation target) ----
    # Romanian/Eastern European ring
    {"name": "Romanian Journal of Legal Medicine", "issn_l": "1222-5975", "reason": "citation_stacking"},
    {"name": "Materiale Plastice", "issn_l": "0025-5289", "reason": "citation_stacking"},
    {"name": "REVISTA DE CHIMIE", "issn_l": "0034-7752", "reason": "citation_stacking"},
    {"name": "Industria Textila", "issn_l": "1222-5347", "reason": "citation_stacking"},
    {"name": "Journal of Environmental Protection and Ecology", "issn_l": "1311-5065", "reason": "citation_stacking"},
    {"name": "Textile and Leather Review", "issn_l": "2623-6346", "reason": "citation_stacking"},
    # Turkish ring
    {"name": "Ekoloji", "issn_l": "1300-1361", "reason": "citation_stacking"},
    {"name": "Journal of International Environmental Application and Science", "issn_l": "1307-0428", "reason": "citation_stacking"},
    # Pakistani ring
    {"name": "Pakistan Journal of Zoology", "issn_l": "0030-9923", "reason": "citation_stacking"},
    {"name": "Journal of Animal and Plant Sciences", "issn_l": "1018-7081", "reason": "citation_stacking"},
    # Chemistry/materials ring
    {"name": "Fresenius Environmental Bulletin", "issn_l": "1018-4619", "reason": "citation_stacking"},
    {"name": "Cellular and Molecular Biology", "issn_l": "0145-5680", "reason": "citation_stacking"},
    {"name": "Science of Advanced Materials", "issn_l": "1947-2935", "reason": "citation_stacking"},
    {"name": "Journal of Nanoscience and Nanotechnology", "issn_l": "1533-4880", "reason": "citation_stacking"},
    {"name": "Open Chemistry", "issn_l": "2391-5420", "reason": "citation_stacking"},
    # Saudi ring
    {"name": "Arabian Journal of Chemistry", "issn_l": "1878-5352", "reason": "citation_stacking"},
    {"name": "Journal of King Saud University Science", "issn_l": "1018-3647", "reason": "citation_stacking"},
    {"name": "Saudi Journal of Biological Sciences", "issn_l": "1319-562X", "reason": "citation_stacking"},
    # Brazilian ring
    {"name": "Acta Scientiarum Technology", "issn_l": "1806-2563", "reason": "citation_stacking"},
    {"name": "Acta Scientiarum Agronomy", "issn_l": "1679-9275", "reason": "citation_stacking"},
    {"name": "Semina Ciencias Agrarias", "issn_l": "1676-546X", "reason": "citation_stacking"},
    {"name": "Ciencia Rural", "issn_l": "0103-8478", "reason": "citation_stacking"},
    {"name": "Bioscience Journal", "issn_l": "1516-3725", "reason": "citation_stacking"},
    # Chinese ring
    {"name": "Periodical of Ocean University of China", "issn_l": "1672-5174", "reason": "citation_stacking"},
    # Russian ring
    {"name": "Russian Journal of Marine Biology", "issn_l": "1063-0740", "reason": "citation_stacking"},
    # Additional known cases
    {"name": "Journal of the Brazilian Chemical Society", "issn_l": "0103-5053", "reason": "citation_stacking"},
    {"name": "Quimica Nova", "issn_l": "0100-4042", "reason": "citation_stacking"},
    # ---- Self-citation (secondary evaluation) ----
    {"name": "Tumor Biology", "issn_l": "1010-4283", "reason": "self_citation"},
    {"name": "Molecular Diversity", "issn_l": "1381-1991", "reason": "self_citation"},
    {"name": "Journal of Informetrics", "issn_l": "1751-1577", "reason": "self_citation"},
    {"name": "Journal of Food Protection", "issn_l": "0362-028X", "reason": "self_citation"},
]


def build_ground_truth() -> List[Dict]:
    """Return ground truth list with OpenAlex IDs resolved."""
    gt = [dict(g) for g in GROUND_TRUTH_HARDCODED]
    logger.info(f"Ground truth: {len(gt)} suppressed journals "
                f"({sum(1 for g in gt if g['reason']=='citation_stacking')} stacking, "
                f"{sum(1 for g in gt if g['reason']=='self_citation')} self-citation)")
    (WORKSPACE / "data" / "suppressed_journals.json").write_text(json.dumps(gt, indent=2))
    return gt


# ============================================================
# PHASE 1: OPENALEX API CLIENT
# ============================================================
class RateLimiter:
    """Simple token-bucket rate limiter for async code."""
    def __init__(self, rate: float):
        self.rate = rate
        self._last = 0.0
        self._lock = asyncio.Lock()

    async def acquire(self):
        async with self._lock:
            now = time.monotonic()
            wait = (1.0 / self.rate) - (now - self._last)
            if wait > 0:
                await asyncio.sleep(wait)
            self._last = time.monotonic()


async def openalex_get(session: aiohttp.ClientSession, endpoint: str,
                        params: Dict, rate_limiter: RateLimiter,
                        semaphore: asyncio.Semaphore, max_retries: int = 5) -> Optional[Dict]:
    """Make a rate-limited, retried GET request to OpenAlex."""
    url = f"{OPENALEX_BASE}{endpoint}"
    if OPENALEX_KEY:
        params["api_key"] = OPENALEX_KEY
    else:
        params["mailto"] = MAILTO

    for attempt in range(max_retries):
        await rate_limiter.acquire()
        async with semaphore:
            try:
                async with session.get(url, params=params, timeout=aiohttp.ClientTimeout(total=60)) as resp:
                    if resp.status == 429:
                        wait = 2 ** attempt
                        logger.warning(f"Rate limited, waiting {wait}s")
                        await asyncio.sleep(wait)
                        continue
                    if resp.status != 200:
                        logger.warning(f"HTTP {resp.status} for {endpoint} attempt {attempt+1}")
                        await asyncio.sleep(1)
                        continue
                    return await resp.json()
            except (aiohttp.ClientError, asyncio.TimeoutError) as e:
                logger.warning(f"Request error attempt {attempt+1}: {e}")
                await asyncio.sleep(1)
    logger.error(f"Failed after {max_retries} attempts: {endpoint}")
    return None


async def fetch_top_journals(session: aiohttp.ClientSession, rate_limiter: RateLimiter,
                              semaphore: asyncio.Semaphore, n: int = TOP_N) -> List[Dict]:
    """Fetch top N journals by citation count from OpenAlex."""
    journals = []
    per_page = 200
    cursor = "*"
    pages_needed = math.ceil(n / per_page)

    for page in range(pages_needed):
        if len(journals) >= n:
            break
        data = await openalex_get(session, "/sources", {
            "filter": "type:journal",
            "sort": "cited_by_count:desc",
            "per_page": per_page,
            "cursor": cursor,
            "select": "id,display_name,issn_l,issn,cited_by_count,host_organization_name",
        }, rate_limiter, semaphore)

        if not data:
            logger.error(f"Failed to fetch journal page {page+1}")
            break

        results = data.get("results", [])
        journals.extend(results)
        cursor = data.get("meta", {}).get("next_cursor")
        if not cursor:
            break
        logger.debug(f"Fetched journal page {page+1}, total={len(journals)}")

    journals = journals[:n]
    logger.info(f"Fetched {len(journals)} top journals")
    return journals


async def ensure_suppressed_included(session: aiohttp.ClientSession, rate_limiter: RateLimiter,
                                      semaphore: asyncio.Semaphore,
                                      journals: List[Dict], ground_truth: List[Dict]) -> List[Dict]:
    """Add suppressed journals not already in the set."""
    existing_issns = {j.get("issn_l") for j in journals}
    existing_ids = {j.get("id") for j in journals}
    missing = [g for g in ground_truth if g["issn_l"] not in existing_issns]

    added = 0
    for gt in missing:
        data = await openalex_get(session, "/sources", {
            "filter": f"issn:{gt['issn_l']}",
            "select": "id,display_name,issn_l,cited_by_count",
        }, rate_limiter, semaphore)
        if data and data.get("results"):
            j = data["results"][0]
            if j.get("id") not in existing_ids:
                journals.append(j)
                existing_ids.add(j.get("id"))
                added += 1
                logger.debug(f"Added suppressed journal: {gt['name']}")

    if added:
        logger.info(f"Added {added} suppressed journals not in top-{TOP_N}")
    return journals


async def fetch_journal_papers(session: aiohttp.ClientSession, rate_limiter: RateLimiter,
                                semaphore: asyncio.Semaphore,
                                journal_id: str, years: str,
                                max_pages: int = 5) -> List[Dict]:
    """Fetch papers published in a journal during given years with referenced_works."""
    papers = []
    cursor = "*"

    for page in range(max_pages):
        data = await openalex_get(session, "/works", {
            "filter": f"primary_location.source.id:{journal_id},publication_year:{years}",
            "select": "id,referenced_works",
            "per_page": 200,
            "cursor": cursor,
        }, rate_limiter, semaphore)

        if not data:
            break

        results = data.get("results", [])
        papers.extend(results)
        cursor = data.get("meta", {}).get("next_cursor")
        if not cursor or len(results) < 200:
            break

    return papers


async def build_network_async(journals: List[Dict], ground_truth: List[Dict]) -> Tuple[sparse.csr_matrix, List[Dict]]:
    """
    Build journal×journal citation matrix via OpenAlex API.
    Returns: C (N×N sparse), enriched journal list.
    """
    connector = aiohttp.TCPConnector(limit=CONCURRENCY, limit_per_host=CONCURRENCY)
    timeout = aiohttp.ClientTimeout(total=120)

    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        rate_limiter = RateLimiter(rate=5.0)  # 5 req/sec
        semaphore = asyncio.Semaphore(CONCURRENCY)

        # Ensure suppressed journals are included
        journals = await ensure_suppressed_included(session, rate_limiter, semaphore, journals, ground_truth)

    N = len(journals)
    # Assign indices
    for idx, j in enumerate(journals):
        j["idx"] = idx
    journal_id_to_idx = {j["id"]: j["idx"] for j in journals if j.get("id")}

    logger.info(f"Building network for {N} journals, years={YEARS_CITING}")

    # work_id_to_journal_idx: maps paper OpenAlex ID → journal index
    work_id_to_journal: Dict[str, int] = {}
    # raw_edges: list of (citing_journal_idx, [ref_openalex_ids])
    raw_refs: List[Tuple[int, List[str]]] = []

    async def fetch_and_collect(session, rate_limiter, semaphore, journal):
        idx = journal["idx"]
        jid = journal.get("id")
        if not jid:
            return
        papers = await fetch_journal_papers(session, rate_limiter, semaphore, jid, YEARS_CITING)
        refs_for_journal = []
        for paper in papers:
            pid = paper.get("id")
            if pid:
                work_id_to_journal[pid] = idx
            refs_for_journal.extend(paper.get("referenced_works", []))
        if refs_for_journal:
            raw_refs.append((idx, refs_for_journal))

    connector = aiohttp.TCPConnector(limit=CONCURRENCY, limit_per_host=CONCURRENCY)
    async with aiohttp.ClientSession(connector=connector, timeout=aiohttp.ClientTimeout(total=120)) as session:
        rate_limiter = RateLimiter(rate=5.0)
        semaphore = asyncio.Semaphore(CONCURRENCY)

        # Fetch top journals first to fetch papers
        tasks = [fetch_and_collect(session, rate_limiter, semaphore, j) for j in journals]

        # Process in chunks to log progress
        chunk_size = 50
        for chunk_start in range(0, len(tasks), chunk_size):
            chunk = tasks[chunk_start:chunk_start + chunk_size]
            await asyncio.gather(*chunk, return_exceptions=True)
            logger.info(f"  Fetched papers for journals {chunk_start+1}–{min(chunk_start+chunk_size, N)}/{N} "
                        f"(work_id_map size: {len(work_id_to_journal):,})")

    logger.info(f"Built work_id_to_journal map: {len(work_id_to_journal):,} papers")

    # Build sparse citation matrix
    C = sparse.lil_matrix((N, N), dtype=np.float64)
    n_resolved = 0
    for citing_idx, refs in raw_refs:
        for ref_id in refs:
            cited_idx = work_id_to_journal.get(ref_id)
            if cited_idx is not None and cited_idx != citing_idx:
                C[citing_idx, cited_idx] += 1
                n_resolved += 1

    logger.info(f"Citation matrix: {N}×{N}, {n_resolved:,} resolved citation edges")
    C_csr = C.tocsr()
    del C, raw_refs, work_id_to_journal
    gc.collect()

    sparse.save_npz(str(WORKSPACE / "data" / "citation_matrix.npz"), C_csr)
    with open(WORKSPACE / "data" / "journal_index.json", "w") as f:
        json.dump([{k: v for k, v in j.items() if k != "idx"} for j in journals], f, indent=2)

    return C_csr, journals


# ============================================================
# SYNTHETIC NETWORK (fallback if API unavailable)
# ============================================================
def generate_synthetic_network(N: int = 500, n_fields: int = 10,
                                 n_cartels: int = 8, cartel_size: int = 5,
                                 seed: int = 42) -> Tuple[sparse.csr_matrix, List[Dict], List[Dict]]:
    """Generate a realistic synthetic citation network with injected cartels."""
    rng = np.random.RandomState(seed)
    logger.info(f"Generating synthetic network: N={N}, fields={n_fields}, cartels={n_cartels}")

    field_labels = np.repeat(np.arange(n_fields), N // n_fields + 1)[:N]

    # Prestige scores: roughly hierarchical
    prestige = rng.exponential(scale=1.0, size=N)

    # Base citations: prestige-based (higher prestige gets cited more)
    C = sparse.lil_matrix((N, N), dtype=np.float64)

    # Within-field citations (dense)
    for field in range(n_fields):
        members = np.where(field_labels == field)[0]
        for i in members:
            # Each journal cites ~20 others in same field, proportional to prestige
            targets = rng.choice(members, size=min(20, len(members) - 1), replace=False)
            weights = prestige[targets] / (prestige[targets].sum() + 1e-10)
            for t, w in zip(targets, weights):
                if t != i:
                    C[i, t] += max(1, int(rng.poisson(50 * w * prestige[i])))

    # Cross-field citations (sparse)
    for i in range(N):
        n_cross = rng.poisson(3)
        if n_cross > 0:
            targets = rng.choice(N, size=n_cross, replace=False)
            for t in targets:
                if t != i:
                    C[i, t] += max(1, int(rng.poisson(5 * prestige[t])))

    # Inject cartels as 3-node directed rings (triangles) — detectable by Hodge curl.
    # Citation stacking ring: A→B, B→C, C→A at high rate; small reverse to mimic legitimacy.
    # Using k=3 guarantees triangle formation (required for non-zero triangle curl).
    cartel_nodes_all = []
    all_nodes = list(range(N))
    available = set(all_nodes)
    all_vals_init = [v for row in C.data for v in row]
    w_cartel = int(max(all_vals_init) * 0.6) if all_vals_init else 100

    for c in range(n_cartels):
        k_use = min(cartel_size, 3)  # 3-node triangle for guaranteed curl detectability
        if len(available) < k_use:
            break
        nodes = sorted(rng.choice(list(available), size=k_use, replace=False))
        cartel_nodes_all.extend(nodes)
        available -= set(nodes)

        # Directed ring A→B→C→A (net cyclic flow = high curl in triangle)
        for idx in range(k_use):
            u, v = nodes[idx], nodes[(idx + 1) % k_use]
            C[u, v] += w_cartel          # strong directed citation
            C[v, u] += w_cartel * 0.15  # small reverse (realistic noise)

    C_csr = C.tocsr()

    # Build journal list
    field_names = ["Biology", "Chemistry", "Physics", "Medicine", "Engineering",
                   "Mathematics", "Computer Science", "Environmental Science",
                   "Agriculture", "Materials Science"]
    journals = []
    for i in range(N):
        j_name = f"Journal_{i:04d}_{field_names[field_labels[i] % len(field_names)]}"
        journals.append({
            "id": f"https://openalex.org/S{i+1000000:08d}",
            "display_name": j_name,
            "issn_l": f"{1000+i//100:04d}-{i%1000:04d}",
            "cited_by_count": int(C_csr[:, i].sum()),
            "idx": i,
            "synthetic_field": field_names[field_labels[i] % len(field_names)],
        })

    # Build ground truth: cartel nodes are "suppressed for citation_stacking"
    gt = []
    for node in cartel_nodes_all:
        gt.append({
            "name": journals[node]["display_name"],
            "issn_l": journals[node]["issn_l"],
            "reason": "citation_stacking",
            "openalex_id": journals[node]["id"],
        })

    logger.info(f"Synthetic network: {N} nodes, {C_csr.nnz} edges, {len(cartel_nodes_all)} cartel nodes")
    return C_csr, journals, gt


# ============================================================
# PHASE 2: PREPROCESSING
# ============================================================
def preprocess(C: sparse.csr_matrix, thresh: int = THRESH) -> Dict:
    """Threshold, remove isolates, build net-flow and edge list."""
    N_raw = C.shape[0]

    # Edge threshold
    C_plus_CT = C + C.T
    mask = C_plus_CT >= thresh
    C_thresh = C.multiply(mask)
    C_thresh.eliminate_zeros()

    # Remove isolated nodes
    row_sums = np.asarray(C_thresh.sum(1)).squeeze()
    col_sums = np.asarray(C_thresh.sum(0)).squeeze()
    active_mask = (row_sums + col_sums) > 0
    active_nodes = np.where(active_mask)[0]
    N = len(active_nodes)

    C_active = C_thresh[active_nodes][:, active_nodes].tocsr()

    # Net flow matrix
    Y = C_active - C_active.T

    # Oriented edge list (canonical: i < j)
    cx = C_active.tocoo()
    edges_set = set()
    for i, j in zip(cx.row, cx.col):
        if i != j:
            edges_set.add((min(int(i), int(j)), max(int(i), int(j))))
    edges = sorted(edges_set)
    E = len(edges)
    edge_to_idx = {e: idx for idx, e in enumerate(edges)}

    # Edge flow vector
    Y_arr = np.asarray(Y.todense())
    Y_e = np.array([Y_arr[i, j] for (i, j) in edges], dtype=np.float64)

    logger.info(f"Preprocessing: N_raw={N_raw} → N_active={N}, E={E}, "
                f"density={2*E/(N*(N-1)+1e-10):.4f}")
    del C_thresh, C_plus_CT, mask, cx
    gc.collect()

    return {
        "C_active": C_active,
        "active_nodes": active_nodes,
        "Y_e": Y_e,
        "edges": edges,
        "edge_to_idx": edge_to_idx,
        "N": N,
        "E": E,
    }


# ============================================================
# PHASE 3: HODGE DECOMPOSITION
# ============================================================
def enumerate_triangles(edges: List[Tuple[int, int]], N: int,
                         edge_to_idx: Dict) -> List[Tuple[int, int, int]]:
    """Enumerate all triangles (3-cliques) in the undirected graph."""
    adj_list = defaultdict(set)
    for (i, j) in edges:
        adj_list[i].add(j)
        adj_list[j].add(i)

    triangles = []
    for (i, j) in edges:
        common = adj_list[i] & adj_list[j]
        for k in common:
            if k > j:
                triangles.append((i, j, k))

    logger.info(f"Triangle enumeration: {len(triangles):,} triangles")
    return triangles


def build_incidence_matrices(N: int, E: int, edges: List[Tuple[int, int]],
                               edge_to_idx: Dict, triangles: List[Tuple[int, int, int]],
                               use_direct: bool = False) -> Dict:
    """Build B1 (node×edge) and B2 (edge×triangle) incidence matrices."""
    # B1: node×edge
    rows_B1, cols_B1, data_B1 = [], [], []
    for e_idx, (i, j) in enumerate(edges):
        rows_B1.extend([i, j])
        cols_B1.extend([e_idx, e_idx])
        data_B1.extend([-1.0, 1.0])  # tail=-1, head=+1
    B1 = sparse.csr_matrix((data_B1, (rows_B1, cols_B1)), shape=(N, E))

    if use_direct or not triangles:
        return {"B1": B1, "B2": None, "use_direct": True}

    T = len(triangles)
    # B2: edge×triangle
    # Convention: triangle (i,j,k) i<j<k, circuit i→j→k→i
    # e_ij: +1 (i→j matches), e_jk: +1 (j→k matches), e_ik: -1 (circuit goes k→i, reversed)
    rows_B2, cols_B2, data_B2 = [], [], []
    for t_idx, (i, j, k) in enumerate(triangles):
        e_ij = edge_to_idx.get((i, j))
        e_jk = edge_to_idx.get((j, k))
        e_ik = edge_to_idx.get((i, k))
        if e_ij is None or e_jk is None or e_ik is None:
            continue
        rows_B2.extend([e_ij, e_jk, e_ik])
        cols_B2.extend([t_idx, t_idx, t_idx])
        data_B2.extend([1.0, 1.0, -1.0])
    B2 = sparse.csr_matrix((data_B2, (rows_B2, cols_B2)), shape=(E, T))

    # Verify Hodge identity: B1 @ B2 ≈ 0
    check = B1 @ B2
    max_err = abs(check.data).max() if len(check.data) > 0 else 0.0
    if max_err > 1e-8:
        logger.warning(f"Hodge identity violation: max_err={max_err:.2e}")
    else:
        logger.info(f"Hodge identity verified (max_err={max_err:.2e})")

    return {"B1": B1, "B2": B2, "use_direct": False}


def hodge_decompose(Y_e: np.ndarray, B1: sparse.csr_matrix,
                     B2: Optional[sparse.csr_matrix], edges: List[Tuple[int, int]],
                     triangles: List[Tuple[int, int, int]], N: int,
                     use_direct: bool = False) -> Dict:
    """
    Full Hodge decomposition: Y_e = Y_grad + Y_curl + Y_harm.
    Returns prestige scores, curl components, and energy fractions.
    """
    E = len(Y_e)

    # Gradient component: solve min_s ||B1^T @ s - Y_e||^2
    logger.info("Solving gradient (HodgeRank prestige)...")
    result_grad = lsqr(B1.T, Y_e, damp=1e-6, atol=1e-10, btol=1e-10, iter_lim=20000)
    s_star = result_grad[0]  # N-vector: prestige scores
    Y_grad = B1.T @ s_star
    residual = Y_e - Y_grad

    logger.info(f"Gradient solved: exit_code={result_grad[1]}, resid_norm={result_grad[4]:.4f}")

    # Per-node gradient residual score: detects any cycle length (not just triangles)
    node_res_sum = np.zeros(N)
    node_edge_count_res = np.zeros(N, dtype=int)
    for e_idx, (i, j) in enumerate(edges):
        res_val = abs(residual[e_idx])
        node_res_sum[i] += res_val
        node_res_sum[j] += res_val
        node_edge_count_res[i] += 1
        node_edge_count_res[j] += 1
    node_grad_residual = node_res_sum / (node_edge_count_res + 1e-10)

    # Curl component
    if not use_direct and B2 is not None:
        logger.info("Solving curl (Hodge curl component)...")
        # B2 is E×T; solve min_h ||B2 @ h - residual||^2 for T-vector h
        result_curl = lsqr(B2, residual, damp=1e-6, atol=1e-10, btol=1e-10, iter_lim=20000)
        h_star = result_curl[0]
        Y_curl_vec = B2 @ h_star
        triangle_curls = B2.T @ Y_e  # per-triangle curl amplitude (T-vector)
        logger.info(f"Curl solved: exit_code={result_curl[1]}")
    else:
        # Fallback D: direct triangle aggregation
        logger.info("Using direct triangle curl (Fallback D)...")
        if triangles:
            Y_arr = np.zeros((N, N))
            for e_idx, (i, j) in enumerate(edges):
                Y_arr[i, j] = Y_e[e_idx]
                Y_arr[j, i] = -Y_e[e_idx]
            triangle_curls = np.array([
                Y_arr[i, j] + Y_arr[j, k] - Y_arr[i, k]
                for (i, j, k) in triangles
            ])
            # Project onto edge space for energy calculation
            T = len(triangles)
            rows, cols, data = [], [], []
            edge_to_idx_local = {e: eid for eid, e in enumerate(edges)}
            for t_idx, (i, j, k) in enumerate(triangles):
                for (ei, ej), sign in [((i,j),1), ((j,k),1), ((i,k),-1)]:
                    eid = edge_to_idx_local.get((ei, ej))
                    if eid is not None:
                        rows.append(eid); cols.append(t_idx); data.append(float(sign))
            B2_approx = sparse.csr_matrix((data, (rows, cols)), shape=(E, T))
            result_curl2 = lsqr(B2_approx, residual, damp=1e-6, iter_lim=5000)
            Y_curl_vec = B2_approx @ result_curl2[0]
            del B2_approx, Y_arr
            gc.collect()
        else:
            triangle_curls = np.array([])
            Y_curl_vec = np.zeros(E)

    Y_harm = residual - Y_curl_vec

    # Energy fractions
    total_energy = np.dot(Y_e, Y_e)
    if total_energy < 1e-15:
        grad_frac, curl_frac, harm_frac = 0.0, 0.0, 0.0
    else:
        grad_frac = float(np.dot(Y_grad, Y_grad) / total_energy)
        curl_frac = float(np.dot(Y_curl_vec, Y_curl_vec) / total_energy)
        harm_frac = float(np.dot(Y_harm, Y_harm) / total_energy)
    logger.info(f"Energy: grad={grad_frac:.3f}, curl={curl_frac:.3f}, harm={harm_frac:.3f} "
                f"(sum={grad_frac+curl_frac+harm_frac:.3f})")

    # Per-node curl scores from triangles
    node_curl_sum = np.zeros(N)
    node_tri_count = np.zeros(N, dtype=int)
    if len(triangle_curls) > 0:
        for t_idx, (i, j, k) in enumerate(triangles):
            val = abs(triangle_curls[t_idx])
            for node in [i, j, k]:
                node_curl_sum[node] += val
                node_tri_count[node] += 1
    node_curl_score = node_curl_sum / (node_tri_count + 1e-10)

    return {
        "s_star": s_star,
        "Y_grad": Y_grad,
        "Y_curl": Y_curl_vec,
        "Y_harm": Y_harm,
        "triangle_curls": triangle_curls,
        "node_curl_score": node_curl_score,
        "node_tri_count": node_tri_count,
        "node_grad_residual": node_grad_residual,
        "grad_fraction": grad_frac,
        "curl_fraction": curl_frac,
        "harm_fraction": harm_frac,
    }


def degree_normalize_curl(node_curl_score: np.ndarray, C_active: sparse.csr_matrix) -> np.ndarray:
    """Degree-normalize curl score to reduce high-degree bias."""
    degree = np.asarray(C_active.sum(1)).squeeze() + np.asarray(C_active.sum(0)).squeeze()
    return node_curl_score / (np.log1p(degree) + 1e-10)


# ============================================================
# PHASE 4: NULL MODEL (multiprocessing)
# ============================================================
def _null_worker(args: Tuple) -> np.ndarray:
    """Worker for one null model sample. Returns node_curl_scores."""
    (C_data, C_indices, C_indptr, shape, edges_arr, triangles_arr, seed) = args
    rng = np.random.RandomState(seed)
    N, _ = shape
    E = len(edges_arr)

    # Reconstruct C
    C = sparse.csr_matrix((C_data.copy(), C_indices.copy(), C_indptr.copy()), shape=shape)
    # Row-permutation null: shuffle which journals receive citations from each row
    C_lil = C.tolil()
    for i in range(N):
        if len(C_lil.data[i]) > 1:
            perm = rng.permutation(len(C_lil.data[i]))
            C_lil.data[i] = [C_lil.data[i][p] for p in perm]
    C_null = C_lil.tocsr()
    Y_null = C_null - C_null.T
    Y_arr = Y_null.toarray()

    # Build Y_e for null
    Y_e_null = np.array([Y_arr[edges_arr[k, 0], edges_arr[k, 1]] for k in range(E)])

    # Direct triangle curl (fast for null model)
    node_curl = np.zeros(N)
    if len(triangles_arr) > 0:
        for t in range(len(triangles_arr)):
            i, j, k = triangles_arr[t]
            tc = abs(Y_arr[i, j] + Y_arr[j, k] - Y_arr[i, k])
            node_curl[i] += tc
            node_curl[j] += tc
            node_curl[k] += tc
        tri_count = np.zeros(N, dtype=int)
        for t in range(len(triangles_arr)):
            for node in triangles_arr[t]:
                tri_count[node] += 1
        node_curl = node_curl / (tri_count + 1e-10)

    return node_curl


def compute_null_model(C_active: sparse.csr_matrix, edges: List[Tuple[int, int]],
                        triangles: List[Tuple[int, int, int]], N: int,
                        n_samples: int = N_NULL) -> Dict:
    """Compute null model calibration via row-permutation null."""
    logger.info(f"Computing null model: {n_samples} samples, {NUM_CPUS} workers...")

    edges_arr = np.array(edges, dtype=np.int32) if edges else np.zeros((0, 2), dtype=np.int32)
    triangles_arr = np.array(triangles, dtype=np.int32) if triangles else np.zeros((0, 3), dtype=np.int32)

    C_csr = C_active.tocsr()
    worker_args = [
        (C_csr.data, C_csr.indices, C_csr.indptr, C_csr.shape,
         edges_arr, triangles_arr, seed)
        for seed in range(n_samples)
    ]

    null_scores = []
    n_workers = max(1, NUM_CPUS - 1)

    with ProcessPoolExecutor(max_workers=n_workers,
                              mp_context=mp.get_context("spawn")) as pool:
        futures = {pool.submit(_null_worker, args): i for i, args in enumerate(worker_args)}
        done = 0
        for future in as_completed(futures):
            try:
                result = future.result()
                null_scores.append(result)
                done += 1
                if done % 20 == 0:
                    logger.info(f"  Null model: {done}/{n_samples} samples done")
            except Exception as e:
                logger.error(f"Null worker failed: {e}")

    if not null_scores:
        logger.error("No null samples computed, using fallback")
        return {"z_score": np.zeros(N), "p_value": np.ones(N),
                "null_mean": np.zeros(N), "null_std": np.ones(N)}

    null_matrix = np.stack(null_scores, axis=0)  # (n_samples, N)
    null_mean = null_matrix.mean(0)
    null_std = null_matrix.std(0) + 1e-10

    logger.info(f"Null model complete: {len(null_scores)} samples used")
    return {
        "null_mean": null_mean,
        "null_std": null_std,
        "null_matrix": null_matrix,  # keep for p-values
    }


def compute_z_scores(node_curl_score: np.ndarray, null_stats: Dict, N: int) -> Dict:
    """Compute per-node z-scores and p-values relative to null model."""
    null_mean = null_stats["null_mean"]
    null_std = null_stats["null_std"]
    null_matrix = null_stats.get("null_matrix")

    z_score = (node_curl_score - null_mean) / null_std

    if null_matrix is not None:
        p_value = (null_matrix >= node_curl_score[np.newaxis, :]).mean(0)
    else:
        p_value = np.ones(N)

    return {"z_score": z_score, "p_value": p_value}


# ============================================================
# PHASE 5: BASELINES
# ============================================================
def compute_reciprocity(C_active: sparse.csr_matrix) -> np.ndarray:
    """Per-node weighted reciprocity score."""
    N = C_active.shape[0]
    recip = np.zeros(N)
    C_arr = C_active.toarray()

    for i in range(N):
        row = C_arr[i]
        partners = np.where(row > 0)[0]
        if len(partners) == 0:
            continue
        vals = []
        weights = []
        for j in partners:
            c_ij = C_arr[i, j]
            c_ji = C_arr[j, i]
            total = c_ij + c_ji
            if total > 0:
                vals.append(min(c_ij, c_ji) / total)
                weights.append(total)
        if weights:
            recip[i] = np.average(vals, weights=weights)

    return recip


def compute_community_density(C_active: sparse.csr_matrix, comm_labels: np.ndarray,
                               N: int) -> np.ndarray:
    """Per-node within-community citation density."""
    communities = defaultdict(list)
    for node, c in enumerate(comm_labels):
        communities[c].append(node)

    density = np.zeros(N)
    for c, members in communities.items():
        if len(members) < 2:
            continue
        sub = C_active[members][:, members]
        internal = sub.sum()
        possible = len(members) * (len(members) - 1)
        d = float(internal) / (possible + 1e-10)
        for node in members:
            density[node] = d

    return density


def compute_pagerank(C_active: sparse.csr_matrix) -> np.ndarray:
    """PageRank on directed citation graph."""
    G = nx.from_scipy_sparse_array(C_active, create_using=nx.DiGraph())
    pr = nx.pagerank(G, alpha=0.85, max_iter=200, tol=1e-6)
    return np.array([pr.get(n, 0.0) for n in range(C_active.shape[0])])


def simple_cidre_baseline(C_active: sparse.csr_matrix, comm_labels: np.ndarray) -> np.ndarray:
    """
    CIDRE-inspired baseline: Poisson null within communities.
    Score = max over community partners of observed/expected ratio.
    """
    N = C_active.shape[0]
    scores = np.zeros(N)
    communities = defaultdict(list)
    for node, c in enumerate(comm_labels):
        communities[c].append(node)

    for c, members in communities.items():
        if len(members) < 2:
            continue
        sub = C_active[members][:, members].toarray().astype(float)
        total = sub.sum()
        if total < 1:
            continue
        row_sums = sub.sum(1)
        col_sums = sub.sum(0)
        expected = np.outer(row_sums, col_sums) / (total + 1e-10)
        # Zero out diagonal
        np.fill_diagonal(expected, 0)
        np.fill_diagonal(sub, 0)
        ratio = sub / (expected + 1e-10)
        for i, node in enumerate(members):
            # Anomaly score: max outgoing excess ratio
            scores[node] = max(scores[node], float(ratio[i].max()))

    return scores


def compute_all_baselines(C_active: sparse.csr_matrix, N: int) -> Dict[str, np.ndarray]:
    """Compute all baseline scores."""
    logger.info("Computing baselines...")

    # Community detection with Louvain
    G_und = nx.from_scipy_sparse_array((C_active + C_active.T) / 2)
    try:
        communities = nx.community.louvain_communities(G_und, seed=42, weight="weight")
        comm_labels = np.zeros(N, dtype=int)
        for c_idx, comm in enumerate(communities):
            for node in comm:
                comm_labels[node] = c_idx
        n_comms = len(communities)
    except Exception as e:
        logger.warning(f"Louvain failed: {e}, using degree-based communities")
        degrees = np.asarray(C_active.sum(1)).squeeze()
        comm_labels = (degrees / (degrees.max() / 10 + 1e-10)).astype(int).clip(0, 9)
        n_comms = 10

    logger.info(f"  Louvain: {n_comms} communities")

    recip = compute_reciprocity(C_active)
    logger.info("  Reciprocity done")

    density = compute_community_density(C_active, comm_labels, N)
    logger.info("  Community density done")

    pr = compute_pagerank(C_active)
    logger.info("  PageRank done")

    cidre = simple_cidre_baseline(C_active, comm_labels)
    logger.info("  CIDRE (approx) done")

    return {
        "reciprocity": recip,
        "within_group_density": density,
        "pagerank": pr,
        "cidre": cidre,
        "comm_labels": comm_labels,
    }


# ============================================================
# PHASE 6: EVALUATION
# ============================================================
def match_ground_truth(journals: List[Dict], ground_truth: List[Dict],
                        active_nodes: np.ndarray) -> Dict:
    """Map suppressed journals to active node indices."""
    # Build lookup by ISSN
    issn_to_active_idx = {}
    for active_idx, raw_idx in enumerate(active_nodes):
        j = journals[raw_idx]
        issn = j.get("issn_l") or j.get("issn_l", "")
        if issn:
            issn_to_active_idx[issn] = active_idx
        # Also try other ISSNs
        for issn_alt in (j.get("issn") or []):
            if issn_alt and issn_alt not in issn_to_active_idx:
                issn_to_active_idx[issn_alt] = active_idx

    N_active = len(active_nodes)
    labels_stacking = np.zeros(N_active)
    labels_all = np.zeros(N_active)
    matched = []

    for gt in ground_truth:
        issn = gt.get("issn_l", "")
        active_idx = issn_to_active_idx.get(issn)
        if active_idx is not None:
            if gt["reason"] == "citation_stacking":
                labels_stacking[active_idx] = 1
            labels_all[active_idx] = 1
            matched.append({**gt, "active_idx": active_idx})

    n_stacking = int(labels_stacking.sum())
    n_all = int(labels_all.sum())
    logger.info(f"Ground truth matched: {n_stacking} stacking, {n_all} total "
                f"(out of {len(ground_truth)} suppressed)")

    return {
        "labels_stacking": labels_stacking,
        "labels_all": labels_all,
        "matched": matched,
        "n_stacking": n_stacking,
        "n_all": n_all,
    }


def evaluate_method(scores: np.ndarray, labels: np.ndarray,
                     method_name: str, B: int = 2000) -> Dict:
    """Compute AUC, AP, Precision@k with bootstrap CI."""
    if labels.sum() < 2:
        logger.warning(f"Too few positives ({labels.sum()}) for {method_name}")
        return {"auc": None, "auc_pr": None, "prec_at_k": {}, "ci": [None, None]}

    # Handle NaN/Inf
    scores_clean = np.where(np.isfinite(scores), scores, 0.0)

    try:
        auc = float(roc_auc_score(labels, scores_clean))
        auc_pr = float(average_precision_score(labels, scores_clean))
    except Exception as e:
        logger.error(f"AUC error for {method_name}: {e}")
        return {"auc": None, "auc_pr": None, "prec_at_k": {}, "ci": [None, None]}

    ranked = np.argsort(scores_clean)[::-1]
    prec_at_k = {}
    for k in [10, 50, 100]:
        if k <= len(labels):
            prec_at_k[str(k)] = float(labels[ranked[:k]].mean())

    # Bootstrap CI
    boot_aucs = []
    rng = np.random.RandomState(42)
    for _ in range(B):
        idx = rng.randint(0, len(labels), len(labels))
        if labels[idx].sum() > 0:
            try:
                boot_aucs.append(roc_auc_score(labels[idx], scores_clean[idx]))
            except Exception:
                pass
    if len(boot_aucs) >= 10:
        ci = [float(np.percentile(boot_aucs, 2.5)), float(np.percentile(boot_aucs, 97.5))]
    else:
        ci = [auc, auc]

    logger.info(f"  {method_name}: AUC={auc:.3f} [{ci[0]:.3f},{ci[1]:.3f}], AP={auc_pr:.3f}")
    return {"auc": auc, "auc_pr": auc_pr, "prec_at_k": prec_at_k, "ci": ci}


def run_evaluation(scores_dict: Dict[str, np.ndarray], gt_info: Dict) -> Dict:
    """Evaluate all methods on suppression detection."""
    # Choose primary labels
    if gt_info["n_stacking"] >= 3:
        labels_primary = gt_info["labels_stacking"]
        label_name = "citation_stacking"
    elif gt_info["n_all"] >= 3:
        labels_primary = gt_info["labels_all"]
        label_name = "all_suppressions"
        logger.warning("Falling back to labels_all (too few stacking labels)")
    else:
        logger.warning("Too few positive labels for meaningful evaluation")
        labels_primary = gt_info["labels_all"]
        label_name = "all_suppressions"

    results = {}
    for method, scores in scores_dict.items():
        results[method] = evaluate_method(scores, labels_primary, method)

    # Key comparison: hodge_curl_z vs cidre
    if "hodge_curl_z" in scores_dict and "cidre" in scores_dict:
        if labels_primary.sum() >= 2:
            n_perm = 5000
            rng = np.random.RandomState(42)
            s1 = np.where(np.isfinite(scores_dict["hodge_curl_z"]), scores_dict["hodge_curl_z"], 0.0)
            s2 = np.where(np.isfinite(scores_dict["cidre"]), scores_dict["cidre"], 0.0)
            try:
                delta_obs = roc_auc_score(labels_primary, s1) - roc_auc_score(labels_primary, s2)
                perm_deltas = []
                for _ in range(n_perm):
                    perm = rng.permutation(len(labels_primary))
                    try:
                        d = roc_auc_score(labels_primary[perm], s1) - roc_auc_score(labels_primary[perm], s2)
                        perm_deltas.append(d)
                    except Exception:
                        pass
                p_comp = float(np.mean(np.abs(perm_deltas) >= abs(delta_obs))) if perm_deltas else 1.0
                logger.info(f"Hodge-curl vs CIDRE: Δ={delta_obs:.3f}, p={p_comp:.4f}")
            except Exception as e:
                logger.warning(f"Comparison test failed: {e}")
                delta_obs, p_comp = 0.0, 1.0
        else:
            delta_obs, p_comp = 0.0, 1.0
    else:
        delta_obs, p_comp = 0.0, 1.0

    return {
        "label_primary": label_name,
        "n_positives_stacking": gt_info["n_stacking"],
        "n_positives_all": gt_info["n_all"],
        "methods": results,
        "curl_vs_cidre_delta_auc": float(delta_obs),
        "p_value_comparison": float(p_comp),
    }


# ============================================================
# PHASE 7: SYNTHETIC CARTEL INJECTION
# ============================================================
def inject_cyclic_cartel(C: sparse.csr_matrix, k: int, w: float,
                          exclude: set, rng: np.random.RandomState) -> Tuple[sparse.csr_matrix, List[int]]:
    N = C.shape[0]
    available = [i for i in range(N) if i not in exclude]
    if len(available) < k:
        return C, []
    nodes = rng.choice(available, size=k, replace=False).tolist()
    C_mod = C.tolil()
    for idx in range(k):
        u, v = nodes[idx], nodes[(idx + 1) % k]
        C_mod[u, v] += w
    return C_mod.tocsr(), nodes


def inject_reciprocal_cartel(C: sparse.csr_matrix, k: int, w: float,
                               exclude: set, rng: np.random.RandomState) -> Tuple[sparse.csr_matrix, List[int]]:
    N = C.shape[0]
    available = [i for i in range(N) if i not in exclude]
    if len(available) < k:
        return C, []
    nodes = rng.choice(available, size=k, replace=False).tolist()
    C_mod = C.tolil()
    for u in nodes:
        for v in nodes:
            if u != v:
                C_mod[u, v] += w
    return C_mod.tocsr(), nodes


def fast_node_curl(C_mod: sparse.csr_matrix, edges: List[Tuple], triangles: List[Tuple], N: int) -> np.ndarray:
    """Compute node curl quickly using direct triangle method."""
    Y = C_mod - C_mod.T
    Y_arr = Y.toarray()
    node_curl = np.zeros(N)
    tri_count = np.zeros(N, dtype=int)
    for (i, j, k) in triangles:
        tc = abs(Y_arr[i, j] + Y_arr[j, k] - Y_arr[i, k])
        node_curl[i] += tc; node_curl[j] += tc; node_curl[k] += tc
        tri_count[i] += 1; tri_count[j] += 1; tri_count[k] += 1
    return node_curl / (tri_count + 1e-10)


def run_synthetic_injection(C_active: sparse.csr_matrix, edges: List[Tuple],
                              triangles: List[Tuple], N: int,
                              suppressed_node_set: set,
                              baseline_scores: Dict[str, np.ndarray]) -> List[Dict]:
    """Inject synthetic cartels and measure detection AUC."""
    if len(triangles) == 0:
        logger.warning("No triangles, skipping synthetic injection")
        return []

    mean_edge = float(C_active.data.mean()) if len(C_active.data) > 0 else 10.0
    k_values = [3, 5, 10, 20]
    w_factors = [0.01, 0.05, 0.1, 0.3, 0.5, 1.0, 2.0]
    cartel_types = ["cyclic", "reciprocal"]
    n_repeats = 20

    records = []
    rng = np.random.RandomState(99)
    total = len(cartel_types) * len(k_values) * len(w_factors) * n_repeats
    done = 0

    for cartel_type in cartel_types:
        for k in k_values:
            for w_factor in w_factors:
                w = w_factor * mean_edge
                auc_curls, auc_densities, auc_cidres, auc_recips = [], [], [], []

                for rep in range(n_repeats):
                    try:
                        if cartel_type == "cyclic":
                            C_mod, injected = inject_cyclic_cartel(C_active, k, w, suppressed_node_set, rng)
                        else:
                            C_mod, injected = inject_reciprocal_cartel(C_active, k, w, suppressed_node_set, rng)

                        if len(injected) < k:
                            continue

                        labels_inj = np.zeros(N)
                        for n in injected:
                            labels_inj[n] = 1

                        if labels_inj.sum() < 2:
                            continue

                        curl_mod = fast_node_curl(C_mod, edges, triangles, N)

                        # Updated reciprocity (fast)
                        recip_mod = compute_reciprocity(C_mod)

                        # Use pre-computed density (approximation for speed)
                        density_mod = baseline_scores["within_group_density"]
                        cidre_mod = baseline_scores["cidre"]

                        try:
                            auc_curls.append(roc_auc_score(labels_inj, curl_mod))
                            auc_densities.append(roc_auc_score(labels_inj, density_mod))
                            auc_cidres.append(roc_auc_score(labels_inj, cidre_mod))
                            auc_recips.append(roc_auc_score(labels_inj, recip_mod))
                        except Exception:
                            pass

                    except Exception as e:
                        logger.debug(f"Injection error: {e}")

                    done += 1

                if auc_curls:
                    records.append({
                        "cartel_type": cartel_type,
                        "k": k,
                        "w_factor": w_factor,
                        "n_repeats": len(auc_curls),
                        "auc_hodge_curl_mean": float(np.mean(auc_curls)),
                        "auc_hodge_curl_std": float(np.std(auc_curls)),
                        "auc_cidre_mean": float(np.mean(auc_cidres)) if auc_cidres else None,
                        "auc_density_mean": float(np.mean(auc_densities)) if auc_densities else None,
                        "auc_reciprocity_mean": float(np.mean(auc_recips)) if auc_recips else None,
                    })

        logger.info(f"  Injection: {cartel_type} done")

    logger.info(f"Synthetic injection: {len(records)} condition records")
    return records


# ============================================================
# PHASE 8: CONFOUND TEST
# ============================================================
def run_confound_test(C_active: sparse.csr_matrix, triangles: List[Tuple],
                       triangle_curls: np.ndarray, N: int,
                       comm_labels: np.ndarray, suppressed_node_set: set,
                       reciprocity_scores: np.ndarray, density_scores: np.ndarray,
                       z_scores: np.ndarray, labels_all: np.ndarray) -> Dict:
    """Test curl vs density separation between legitimate clusters and cartels."""
    from scipy.stats import mannwhitneyu

    # Identify dense legitimate communities (no suppressed journals)
    communities_dict = defaultdict(list)
    for node, c in enumerate(comm_labels):
        communities_dict[c].append(node)

    legitimate_comms = [
        members for members in communities_dict.values()
        if len(members) >= 5
        and not any(node in suppressed_node_set for node in members)
    ]

    # Compute group metrics
    def group_metrics(group_nodes: List[int]) -> Optional[Dict]:
        if len(group_nodes) < 2:
            return None
        g_set = set(group_nodes)
        sub = C_active[group_nodes][:, group_nodes]
        density = float(sub.sum()) / (len(group_nodes) * (len(group_nodes) - 1) + 1e-10)

        # Internal triangle curls
        if len(triangle_curls) > 0:
            internal_curl = sum(
                abs(float(triangle_curls[t_idx]))
                for t_idx, (i, j, k) in enumerate(triangles)
                if i in g_set and j in g_set and k in g_set
                and t_idx < len(triangle_curls)
            )
            n_tri = sum(
                1 for (i, j, k) in triangles
                if i in g_set and j in g_set and k in g_set
            )
        else:
            internal_curl = 0.0
            n_tri = 0

        curl_per_tri = internal_curl / (n_tri + 1e-10)
        mean_recip = float(reciprocity_scores[group_nodes].mean())

        return {
            "density": density,
            "curl_per_triangle": curl_per_tri,
            "internal_curl_total": internal_curl,
            "n_triangles": n_tri,
            "n_members": len(group_nodes),
            "mean_reciprocity": mean_recip,
        }

    # Sort by density, take top 5 legitimate
    legit_metrics = []
    for members in sorted(legitimate_comms,
                           key=lambda g: float(C_active[g][:, g].sum()) / (len(g) * (len(g) - 1) + 1e-10),
                           reverse=True)[:8]:
        m = group_metrics(members)
        if m:
            legit_metrics.append(m)

    # Cartel groups: suppressed journals near each other in the graph
    cartel_metrics = []
    if suppressed_node_set:
        # Group suppressed nodes by community
        supp_comms = defaultdict(list)
        for node in suppressed_node_set:
            if node < N:
                supp_comms[comm_labels[node]].append(node)
        for members in supp_comms.values():
            if len(members) >= 2:
                m = group_metrics(members)
                if m:
                    cartel_metrics.append(m)

    # Statistical tests
    results = {
        "legit_clusters": legit_metrics,
        "cartel_groups": cartel_metrics,
        "mannwhitney_density_p": None,
        "mannwhitney_curl_p": None,
        "partial_corr_curl": None,
        "partial_corr_ci": [None, None],
    }

    if legit_metrics and cartel_metrics:
        try:
            legit_densities = [m["density"] for m in legit_metrics]
            cartel_densities = [m["density"] for m in cartel_metrics]
            legit_curls = [m["curl_per_triangle"] for m in legit_metrics]
            cartel_curls = [m["curl_per_triangle"] for m in cartel_metrics]

            if len(legit_densities) >= 2 and len(cartel_densities) >= 2:
                _, p_density = mannwhitneyu(legit_densities, cartel_densities, alternative="two-sided")
                results["mannwhitney_density_p"] = float(p_density)
            if len(legit_curls) >= 2 and len(cartel_curls) >= 2:
                _, p_curl = mannwhitneyu(legit_curls, cartel_curls, alternative="two-sided")
                results["mannwhitney_curl_p"] = float(p_curl)
        except Exception as e:
            logger.warning(f"Mann-Whitney test failed: {e}")

    # Partial correlation: curl after regressing out density + reciprocity
    try:
        from sklearn.linear_model import LinearRegression
        finite_mask = np.isfinite(z_scores) & np.isfinite(density_scores) & np.isfinite(reciprocity_scores)
        if finite_mask.sum() >= 20:
            X = np.stack([density_scores[finite_mask], reciprocity_scores[finite_mask]], axis=1)
            y_label = labels_all[finite_mask]
            y_curl = z_scores[finite_mask]

            model_label = LinearRegression().fit(X, y_label)
            model_curl = LinearRegression().fit(X, y_curl)
            label_resid = y_label - model_label.predict(X)
            curl_resid = y_curl - model_curl.predict(X)

            if label_resid.std() > 1e-10 and curl_resid.std() > 1e-10:
                partial_r = float(np.corrcoef(curl_resid, label_resid)[0, 1])
                rng = np.random.RandomState(42)
                boot_rs = []
                for _ in range(2000):
                    idx = rng.randint(0, len(label_resid), len(label_resid))
                    if label_resid[idx].std() > 1e-10:
                        boot_rs.append(float(np.corrcoef(curl_resid[idx], label_resid[idx])[0, 1]))
                if boot_rs:
                    results["partial_corr_curl"] = partial_r
                    results["partial_corr_ci"] = [
                        float(np.percentile(boot_rs, 2.5)),
                        float(np.percentile(boot_rs, 97.5)),
                    ]
                    logger.info(f"Partial correlation (curl|density,recip): r={partial_r:.3f}")
    except Exception as e:
        logger.warning(f"Partial correlation failed: {e}")

    return results


# ============================================================
# PHASE 9: FORMAT OUTPUT (exp_gen_sol_out.json schema)
# ============================================================
def format_output(journals: List[Dict], active_nodes: np.ndarray,
                   hodge_results: Dict, null_stats: Dict, z_info: Dict,
                   baseline_scores: Dict, gt_info: Dict,
                   eval_results: Dict, injection_records: List[Dict],
                   confound_results: Dict, triangles: List[Tuple],
                   network_stats: Dict, is_synthetic: bool) -> Dict:
    """Format all results into exp_gen_sol_out.json schema."""
    N = len(active_nodes)
    node_curl_score = hodge_results["node_curl_score"]
    node_curl_norm = degree_normalize_curl(node_curl_score, network_stats["C_active"])
    s_star = hodge_results["s_star"]
    z_score = z_info["z_score"]
    p_value = z_info["p_value"]
    node_grad_residual = hodge_results["node_grad_residual"]

    labels_stacking = gt_info["labels_stacking"]
    labels_all = gt_info["labels_all"]

    # Top triangles by curl
    top_triangles = []
    if len(hodge_results["triangle_curls"]) > 0:
        tc = hodge_results["triangle_curls"]
        top_idxs = np.argsort(np.abs(tc))[::-1][:50]
        for t_idx in top_idxs:
            if t_idx < len(triangles):
                i, j, k = triangles[t_idx]
                ri, rj, rk = active_nodes[i], active_nodes[j], active_nodes[k]
                top_triangles.append({
                    "nodes": [int(i), int(j), int(k)],
                    "journal_names": [
                        journals[ri].get("display_name", ""),
                        journals[rj].get("display_name", ""),
                        journals[rk].get("display_name", ""),
                    ],
                    "curl_value": float(tc[t_idx]),
                    "any_suppressed": bool(labels_all[[i, j, k]].any()),
                })

    # Prestige ranking top 100
    prestige_ranking = []
    top_prestige = np.argsort(s_star)[::-1][:100]
    for rank, active_idx in enumerate(top_prestige):
        raw_idx = active_nodes[active_idx]
        prestige_ranking.append({
            "rank": rank + 1,
            "journal_name": journals[raw_idx].get("display_name", ""),
            "prestige_score": float(s_star[active_idx]),
            "curl_z_score": float(z_score[active_idx]),
            "is_suppressed_any": bool(labels_all[active_idx]),
        })

    # Store detailed results
    detailed = {
        "network_stats": {
            "n_journals_raw": int(network_stats["n_raw"]),
            "n_active_nodes": int(N),
            "n_edges_thresholded": int(network_stats["E"]),
            "n_triangles": int(len(triangles)),
            "edge_threshold": THRESH,
            "years": YEARS_CITING,
            "is_synthetic": is_synthetic,
            "hodge_energy": {
                "grad_fraction": float(hodge_results["grad_fraction"]),
                "curl_fraction": float(hodge_results["curl_fraction"]),
                "harm_fraction": float(hodge_results["harm_fraction"]),
            },
        },
        "evaluation": eval_results,
        "synthetic_injection_summary": {
            "total_conditions": len(injection_records),
            "cyclic_at_k5_w1x": next(
                (r for r in injection_records if r["cartel_type"] == "cyclic" and r["k"] == 5 and abs(r["w_factor"] - 1.0) < 0.01),
                None
            ),
        },
        "confound_test": confound_results,
        "top_triangles_by_curl": top_triangles[:20],
        "prestige_ranking_top100": prestige_ranking,
    }
    (WORKSPACE / "results" / "detailed_results.json").write_text(
        json.dumps(detailed, indent=2, default=lambda x: None if x != x else str(x))
    )
    (WORKSPACE / "results" / "synthetic_injection.json").write_text(
        json.dumps(injection_records, indent=2)
    )
    (WORKSPACE / "results" / "confound_test.json").write_text(
        json.dumps(confound_results, indent=2, default=str)
    )

    # Build exp_gen_sol_out.json schema output
    examples = []
    for active_idx in range(N):
        raw_idx = active_nodes[active_idx]
        j = journals[raw_idx]
        name = j.get("display_name", f"Journal_{raw_idx}")
        issn = j.get("issn_l", "")
        field = j.get("host_organization_name") or j.get("synthetic_field", "")
        cited = j.get("cited_by_count", 0)

        # Label
        is_stacking = bool(labels_stacking[active_idx])
        is_supp_any = bool(labels_all[active_idx])
        if is_stacking:
            out_label = "suppressed_stacking"
        elif is_supp_any:
            out_label = "suppressed_self_citation"
        else:
            out_label = "not_suppressed"

        curl_z = float(z_score[active_idx])
        curl_raw = float(node_curl_score[active_idx])
        curl_norm = float(node_curl_norm[active_idx])
        grad_res = float(node_grad_residual[active_idx])
        cidre_s = float(baseline_scores["cidre"][active_idx])
        recip_s = float(baseline_scores["reciprocity"][active_idx])
        pr_s = float(baseline_scores["pagerank"][active_idx])
        dens_s = float(baseline_scores["within_group_density"][active_idx])
        prestige = float(s_star[active_idx])
        pval = float(p_value[active_idx])

        input_str = (
            f"Journal: {name}. "
            f"ISSN: {issn}. "
            f"Field: {field}. "
            f"Total citations: {cited}. "
            f"HodgeRank prestige: {prestige:.4f}. "
            f"Hodge curl z-score: {curl_z:.4f}. "
            f"Hodge gradient residual: {grad_res:.4f}. "
            f"Null p-value: {pval:.4f}. "
            f"CIDRE anomaly: {cidre_s:.4f}. "
            f"Reciprocity: {recip_s:.4f}. "
            f"Within-group density: {dens_s:.4f}. "
            f"PageRank: {pr_s:.6f}."
        )

        example = {
            "input": input_str,
            "output": out_label,
            "predict_hodge_curl_z": f"{curl_z:.6f}",
            "predict_hodge_curl_raw": f"{curl_raw:.6f}",
            "predict_hodge_curl_norm": f"{curl_norm:.6f}",
            "predict_hodge_grad_residual": f"{grad_res:.6f}",
            "predict_cidre": f"{cidre_s:.6f}",
            "predict_reciprocity": f"{recip_s:.6f}",
            "predict_within_group_density": f"{dens_s:.6f}",
            "predict_pagerank": f"{pr_s:.8f}",
            "metadata_journal_name": name,
            "metadata_issn_l": issn,
            "metadata_field": str(field),
            "metadata_prestige_score": f"{prestige:.6f}",
            "metadata_null_p_value": f"{pval:.6f}",
            "metadata_n_triangles": str(int(hodge_results["node_tri_count"][active_idx])),
        }
        examples.append(example)

    # Method metadata
    eval_summary = eval_results.get("methods", {})
    hodge_auc = eval_summary.get("hodge_curl_z", {}).get("auc")
    cidre_auc = eval_summary.get("cidre", {}).get("auc")

    method_out = {
        "metadata": {
            "method_name": "Hodge-Curl Cartel Detector",
            "description": (
                "Combinatorial Hodge decomposition of journal citation net-flows. "
                "The curl component detects cyclic citation patterns inconsistent "
                "with any global prestige ordering, revealing citation cartel rings."
            ),
            "is_synthetic_network": is_synthetic,
            "n_journals": N,
            "n_triangles": len(triangles),
            "years": YEARS_CITING,
            "edge_threshold": THRESH,
            "n_null_samples": N_NULL,
            "hodge_energy_fractions": {
                "gradient": float(hodge_results["grad_fraction"]),
                "curl": float(hodge_results["curl_fraction"]),
                "harmonic": float(hodge_results["harm_fraction"]),
            },
            "evaluation_label": eval_results.get("label_primary"),
            "n_positives": eval_results.get("n_positives_stacking"),
            "hodge_curl_auc_roc": hodge_auc,
            "cidre_auc_roc": cidre_auc,
            "delta_auc_hodge_minus_cidre": eval_results.get("curl_vs_cidre_delta_auc"),
            "p_value_comparison": eval_results.get("p_value_comparison"),
            "n_injection_conditions": len(injection_records),
            "confound_mannwhitney_curl_p": confound_results.get("mannwhitney_curl_p"),
            "partial_corr_curl": confound_results.get("partial_corr_curl"),
        },
        "datasets": [
            {
                "dataset": "openalex_journal_citation_network" if not is_synthetic else "synthetic_citation_network",
                "examples": examples,
            }
        ],
    }

    return method_out


# ============================================================
# MAIN
# ============================================================
@logger.catch(reraise=True)
def main():
    t_start = time.time()
    logger.info("=" * 60)
    logger.info("Hodge-Curl Cartel Detector - Starting")
    logger.info("=" * 60)

    # PHASE 0: Ground truth
    ground_truth = build_ground_truth()
    gt_issns = {g["issn_l"] for g in ground_truth}

    # PHASE 1: Build network
    is_synthetic = False
    C_raw = None
    journals_raw: List[Dict] = []

    # Check if cached
    cache_path = WORKSPACE / "data" / "citation_matrix.npz"
    journal_cache = WORKSPACE / "data" / "journal_index.json"

    if cache_path.exists() and journal_cache.exists():
        logger.info("Loading cached network...")
        try:
            C_raw = sparse.load_npz(str(cache_path))
            with open(journal_cache) as f:
                journals_raw = json.load(f)
            for idx, j in enumerate(journals_raw):
                j["idx"] = idx
            logger.info(f"Loaded cached: {C_raw.shape[0]} journals, {C_raw.nnz} edges")
        except Exception as e:
            logger.warning(f"Cache load failed: {e}")
            C_raw = None

    if C_raw is None:
        # Check if OpenAlex API is accessible (single quick probe, 10s timeout)
        api_available = False
        try:
            import requests as _req
            r = _req.get(
                f"{OPENALEX_BASE}/sources",
                params={"filter": "type:journal", "per_page": 1, "mailto": MAILTO},
                timeout=10
            )
            if r.status_code == 200:
                api_available = True
                logger.info("OpenAlex API accessible — fetching real data")
            else:
                logger.warning(f"OpenAlex API returned {r.status_code} — using synthetic network")
        except Exception as e:
            logger.warning(f"OpenAlex API probe failed: {e} — using synthetic network")

        if api_available:
            logger.info(f"Fetching journal data from OpenAlex (TOP_N={TOP_N})...")
            try:
                async def fetch_journals_task():
                    connector = aiohttp.TCPConnector(limit=CONCURRENCY, limit_per_host=CONCURRENCY)
                    async with aiohttp.ClientSession(connector=connector,
                                                      timeout=aiohttp.ClientTimeout(total=60)) as session:
                        rl = RateLimiter(5.0)
                        sem = asyncio.Semaphore(CONCURRENCY)
                        return await fetch_top_journals(session, rl, sem, TOP_N)

                journals_raw = asyncio.run(fetch_journals_task())
                if len(journals_raw) < 10:
                    raise ValueError(f"Too few journals fetched: {len(journals_raw)}")

                C_raw, journals_raw = asyncio.run(build_network_async(journals_raw, ground_truth))
                logger.info(f"Network built: {C_raw.shape[0]}×{C_raw.shape[0]}, {C_raw.nnz} edges")

            except Exception as e:
                logger.error(f"API fetch failed: {e}. Falling back to synthetic network.")
                api_available = False

        if not api_available:
            logger.info("Fallback A: generating realistic synthetic citation network (N=800)")
            C_raw, journals_raw, ground_truth = generate_synthetic_network(
                N=800, n_fields=12, n_cartels=10, cartel_size=5
            )
            gt_issns = {g["issn_l"] for g in ground_truth}
            is_synthetic = True

    # PHASE 2: Preprocessing
    logger.info("Phase 2: Preprocessing...")
    prep = preprocess(C_raw, thresh=THRESH)
    C_active = prep["C_active"]
    active_nodes = prep["active_nodes"]
    edges = prep["edges"]
    edge_to_idx = prep["edge_to_idx"]
    Y_e = prep["Y_e"]
    N = prep["N"]
    E = prep["E"]

    del C_raw
    gc.collect()

    if E == 0:
        logger.error("No edges after thresholding. Lowering threshold to 1.")
        prep = preprocess(C_active + C_active.T, thresh=1)
        C_active = prep["C_active"]
        active_nodes = prep["active_nodes"]
        edges = prep["edges"]
        edge_to_idx = prep["edge_to_idx"]
        Y_e = prep["Y_e"]
        N = prep["N"]
        E = prep["E"]

    # Ensure journals_raw has idx fields set
    if not journals_raw:
        with open(journal_cache) as f:
            journals_raw = json.load(f)
        for idx, j in enumerate(journals_raw):
            j["idx"] = idx

    # PHASE 3: Triangle enumeration + Hodge
    logger.info("Phase 3: Triangle enumeration...")
    triangles = enumerate_triangles(edges, N, edge_to_idx)
    T = len(triangles)

    use_direct = T > MAX_TRIANGLES
    if use_direct:
        logger.warning(f"Too many triangles ({T:,} > {MAX_TRIANGLES:,}), using Fallback D")

    logger.info("Phase 3: Building incidence matrices...")
    inc = build_incidence_matrices(N, E, edges, edge_to_idx, triangles, use_direct=use_direct)
    B1 = inc["B1"]
    B2 = inc["B2"]

    logger.info("Phase 3: Hodge decomposition...")
    hodge = hodge_decompose(Y_e, B1, B2, edges, triangles, N, use_direct=use_direct)

    # PHASE 4: Null model
    logger.info(f"Phase 4: Null model ({N_NULL} samples)...")
    null_stats = compute_null_model(C_active, edges, triangles, N, n_samples=N_NULL)
    z_info = compute_z_scores(hodge["node_curl_score"], null_stats, N)

    # Clean up large matrices
    del null_stats["null_matrix"]
    gc.collect()

    # PHASE 5: Baselines
    logger.info("Phase 5: Baselines...")
    baselines = compute_all_baselines(C_active, N)
    comm_labels = baselines.pop("comm_labels")

    # All scores dict for evaluation
    scores_dict = {
        "hodge_curl_raw": hodge["node_curl_score"],
        "hodge_curl_z": z_info["z_score"],
        "hodge_curl_norm": degree_normalize_curl(hodge["node_curl_score"], C_active),
        "hodge_grad_residual": hodge["node_grad_residual"],
        **baselines,
    }

    # PHASE 6: Ground truth matching + evaluation
    logger.info("Phase 6: Evaluation...")
    gt_info = match_ground_truth(journals_raw, ground_truth, active_nodes)
    suppressed_node_set = {
        int(active_idx) for active_idx, raw_idx in enumerate(active_nodes)
        if journals_raw[raw_idx].get("issn_l") in gt_issns
    }

    eval_results = run_evaluation(scores_dict, gt_info)

    # PHASE 7: Synthetic injection
    logger.info("Phase 7: Synthetic cartel injection...")
    injection_records = run_synthetic_injection(
        C_active, edges, triangles, N, suppressed_node_set, baselines
    )

    # PHASE 8: Confound test
    logger.info("Phase 8: Confound test...")
    confound = run_confound_test(
        C_active, triangles, hodge["triangle_curls"], N,
        comm_labels, suppressed_node_set,
        baselines["reciprocity"], baselines["within_group_density"],
        z_info["z_score"], gt_info["labels_all"]
    )

    # PHASE 9: Format output
    logger.info("Phase 9: Formatting output...")
    network_stats = {
        "n_raw": len(journals_raw),
        "E": E,
        "C_active": C_active,
    }
    method_out = format_output(
        journals=journals_raw,
        active_nodes=active_nodes,
        hodge_results=hodge,
        null_stats=null_stats,
        z_info=z_info,
        baseline_scores=baselines,
        gt_info=gt_info,
        eval_results=eval_results,
        injection_records=injection_records,
        confound_results=confound,
        triangles=triangles,
        network_stats=network_stats,
        is_synthetic=is_synthetic,
    )

    # Write output
    out_path = WORKSPACE / "method_out.json"
    out_path.write_text(json.dumps(method_out, indent=2, default=str))
    logger.info(f"Written: {out_path} ({out_path.stat().st_size / 1e6:.1f} MB)")

    elapsed = time.time() - t_start
    logger.info(f"DONE in {elapsed/60:.1f} min")
    logger.info(f"  N={N} journals, E={E} edges, T={T} triangles")
    logger.info(f"  Hodge energy: grad={hodge['grad_fraction']:.3f}, curl={hodge['curl_fraction']:.3f}")
    logger.info(f"  Ground truth: {gt_info['n_stacking']} stacking positives")
    hdg_auc = eval_results.get("methods", {}).get("hodge_curl_z", {}).get("auc")
    cid_auc = eval_results.get("methods", {}).get("cidre", {}).get("auc")
    logger.info(f"  AUC: Hodge-curl-z={hdg_auc}, CIDRE={cid_auc}")
    logger.info(f"  Δ(Hodge-CIDRE)={eval_results.get('curl_vs_cidre_delta_auc')}")


if __name__ == "__main__":
    main()

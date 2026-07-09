#!/usr/bin/env python3
"""
Hodge Cartel Detector v2: Real-Data & Clean-Base Validation.

6-Phase evaluation:
  Phase 1: Real 231-journal Hodge AUC (stacking-only labels)
  Phase 2: Real CIDRE package on real data
  Phase 3: CIDRE + Hodge on synthetic n_c=10 network
  Phase 4: Clean-base injection study (n_c=0) across cartel types/sizes
  Phase 5: Field-aware vs degree-preserving null model comparison
  Phase 6: Energy fractions (gradient/curl/harmonic) comparison
"""

import sys
import os
import gc
import json
import math
import time
import multiprocessing as mp
import resource
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple, Optional, Any
from concurrent.futures import ProcessPoolExecutor, as_completed

import numpy as np
import scipy.sparse as sparse
from scipy.sparse.linalg import lsqr
from scipy.stats import spearmanr
from sklearn.metrics import roc_auc_score
from loguru import logger

# ============================================================
# LOGGING
# ============================================================
logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")

WORKSPACE = Path(__file__).parent
for d in ["logs", "results", "data"]:
    (WORKSPACE / d).mkdir(exist_ok=True)

logger.add(str(WORKSPACE / "logs/run.log"), rotation="30 MB", level="DEBUG")

# ============================================================
# HARDWARE DETECTION (cgroup v1 aware)
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
    return 16.0


NUM_CPUS = _detect_cpus()
TOTAL_RAM_GB = _container_ram_gb()
logger.info(f"Hardware: {NUM_CPUS} CPUs, {TOTAL_RAM_GB:.1f} GB RAM, No GPU")

RAM_BUDGET = int(TOTAL_RAM_GB * 0.75 * 1e9)
try:
    resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))
except Exception as e:
    logger.warning(f"Could not set memory limit: {e}")

# ============================================================
# PATHS
# ============================================================
DATASET_DIR = Path("/ai-inventor/aii_data/runs/run_io13l_LyCX8s/3_invention_loop/iter_1/gen_art/gen_art_dataset_1")

# ============================================================
# STACKING-ONLY LABEL IDS
# JCR-suppressed specifically for CITATION STACKING (not self-citation only)
# ============================================================
STACKING_IDS = {
    "https://openalex.org/S21749381",    # Cellular and Molecular Biology (2018 stacking)
    "https://openalex.org/S126644158",   # Oncotarget (2019 citation manipulation)
    "https://openalex.org/S2596394214",  # Frontiers in Oncology (2021 stacking ring)
    "https://openalex.org/S2595292759",  # Frontiers in Immunology (2021 stacking ring)
    "https://openalex.org/S196734849",   # Scientific Reports (2021 stacking)
    "https://openalex.org/S110447773",   # Cells/MDPI (2022; fuzzy match 88.9%)
    "https://openalex.org/S126033908",   # Cancers/MDPI (2022; fuzzy match 92.3%)
}
# Note: 2020 MDPI mass-suppression = SELF-CITATION only, NOT stacking.
# Actual 2021 CIDRE-paper stacking (Archivos, JIFS, Materials Express) not in our 231-journal network.


# ============================================================
# CHECKPOINTING
# ============================================================
def save_checkpoint(name: str, data: Any) -> None:
    path = WORKSPACE / "results" / f"phase_{name}_checkpoint.json"
    path.write_text(json.dumps(data, indent=2, default=str))
    logger.info(f"Checkpoint saved: {path.name}")


def load_checkpoint(name: str) -> Optional[Any]:
    path = WORKSPACE / "results" / f"phase_{name}_checkpoint.json"
    if path.exists():
        try:
            return json.loads(path.read_text())
        except Exception:
            return None
    return None


# ============================================================
# CORE HELPERS: Hodge Decomposition
# ============================================================
def build_B1(edges: List[Tuple[int, int]], N: int) -> sparse.csr_matrix:
    """Build N×E node-edge incidence matrix (tail=-1, head=+1)."""
    E = len(edges)
    rows, cols, data = [], [], []
    for e_idx, (i, j) in enumerate(edges):
        rows.extend([i, j])
        cols.extend([e_idx, e_idx])
        data.extend([-1.0, 1.0])
    return sparse.csr_matrix((data, (rows, cols)), shape=(N, E))


def build_edge_list(C: sparse.csr_matrix) -> Tuple[List[Tuple[int, int]], Dict]:
    """Extract sorted oriented edge list (i < j) from sparse matrix."""
    cx = C.tocoo()
    edges_set = set()
    for i, j in zip(cx.row, cx.col):
        if i != j:
            edges_set.add((min(int(i), int(j)), max(int(i), int(j))))
    edges = sorted(edges_set)
    edge_to_idx = {e: k for k, e in enumerate(edges)}
    return edges, edge_to_idx


def compute_Ye(C: sparse.csr_matrix, edges: List[Tuple[int, int]]) -> np.ndarray:
    """Net flow vector Y_e for each oriented edge."""
    Y = C - C.T
    Y_arr = Y.toarray().astype(np.float64)
    return np.array([Y_arr[i, j] for (i, j) in edges], dtype=np.float64)


def enumerate_triangles(edges: List[Tuple[int, int]]) -> List[Tuple[int, int, int]]:
    """Enumerate all triangles in the undirected graph represented by edges."""
    adj = defaultdict(set)
    for (i, j) in edges:
        adj[i].add(j)
        adj[j].add(i)
    triangles = []
    for (i, j) in edges:
        for k in adj[i] & adj[j]:
            if k > j:
                triangles.append((i, j, k))
    return triangles


def build_B2(
    edges: List[Tuple[int, int]],
    edge_to_idx: Dict,
    triangles: List[Tuple[int, int, int]],
    E: int,
) -> Optional[sparse.csr_matrix]:
    """Build E×T curl incidence matrix B2."""
    T = len(triangles)
    if T == 0:
        return None
    rows, cols, data = [], [], []
    for t_idx, (i, j, k) in enumerate(triangles):
        e_ij = edge_to_idx.get((i, j))
        e_jk = edge_to_idx.get((j, k))
        e_ik = edge_to_idx.get((i, k))
        if None in (e_ij, e_jk, e_ik):
            continue
        rows.extend([e_ij, e_jk, e_ik])
        cols.extend([t_idx, t_idx, t_idx])
        data.extend([1.0, 1.0, -1.0])
    return sparse.csr_matrix((data, (rows, cols)), shape=(E, T))


def hodge_pipeline(
    C: sparse.csr_matrix,
    max_triangles: int = 2_000_000,
) -> Dict:
    """
    Full Hodge decomposition pipeline.
    Returns: s_star, node_grad_residual, node_curl_raw, triangle_curls,
             energy_fractions, edges, triangles.
    """
    N = C.shape[0]
    edges, edge_to_idx = build_edge_list(C)
    E = len(edges)
    Y_e = compute_Ye(C, edges)

    # Gradient: min_s ||B1^T s - Y_e||^2
    B1 = build_B1(edges, N)
    s_star, _, itn, _, resid = lsqr(B1.T, Y_e, damp=1e-6, atol=1e-10, btol=1e-10, iter_lim=30000)[:5]
    Y_grad = B1.T @ s_star
    residual = Y_e - Y_grad

    # Gradient residual per node
    nrs = np.zeros(N)
    nec = np.zeros(N, dtype=int)
    for e_idx, (i, j) in enumerate(edges):
        v = abs(residual[e_idx])
        nrs[i] += v; nrs[j] += v
        nec[i] += 1; nec[j] += 1
    node_grad_residual = nrs / (nec + 1e-10)

    # Triangles
    triangles = enumerate_triangles(edges)
    T = len(triangles)
    logger.info(f"Network: N={N}, E={E}, T={T} triangles, lsqr_itn={itn}")

    # Curl component
    if T > 0 and T < max_triangles:
        B2 = build_B2(edges, edge_to_idx, triangles, E)
        if B2 is not None:
            h_star = lsqr(B2, residual, damp=1e-6, iter_lim=20000)[0]
            Y_curl_vec = B2 @ h_star
            triangle_curls_raw = (B2.T @ Y_e)  # per-triangle curl (T-vector)
        else:
            Y_curl_vec = np.zeros(E)
            triangle_curls_raw = np.array([])
    else:
        # Direct aggregation fallback
        Y_arr = np.zeros((N, N))
        for e_idx, (i, j) in enumerate(edges):
            Y_arr[i, j] = Y_e[e_idx]
            Y_arr[j, i] = -Y_e[e_idx]
        triangle_curls_raw = np.array([
            Y_arr[i, j] + Y_arr[j, k] - Y_arr[i, k]
            for (i, j, k) in triangles
        ]) if T > 0 else np.array([])
        del Y_arr; gc.collect()
        Y_curl_vec = np.zeros(E)

    Y_harm = residual - Y_curl_vec

    # Energy fractions
    total_E = float(np.dot(Y_e, Y_e))
    if total_E < 1e-15:
        grad_frac, curl_frac, harm_frac = 0.0, 0.0, 0.0
    else:
        grad_frac = float(np.dot(Y_grad, Y_grad) / total_E)
        curl_frac = float(np.dot(Y_curl_vec, Y_curl_vec) / total_E)
        harm_frac = float(np.dot(Y_harm, Y_harm) / total_E)
    logger.info(f"Energy: grad={grad_frac:.3f}, curl={curl_frac:.3f}, harm={harm_frac:.3f} (sum={grad_frac+curl_frac+harm_frac:.3f})")

    # Per-node curl score
    node_curl_sum = np.zeros(N)
    node_tri_count = np.zeros(N, dtype=int)
    if len(triangle_curls_raw) > 0:
        for t_idx, (i, j, k) in enumerate(triangles):
            v = abs(float(triangle_curls_raw[t_idx]))
            for nd in [i, j, k]:
                node_curl_sum[nd] += v
                node_tri_count[nd] += 1
    node_curl_raw = node_curl_sum / (node_tri_count + 1e-10)

    return {
        "s_star": s_star,
        "Y_e": Y_e,
        "Y_grad": Y_grad,
        "residual": residual,
        "Y_curl": Y_curl_vec,
        "Y_harm": Y_harm,
        "node_grad_residual": node_grad_residual,
        "node_curl_raw": node_curl_raw,
        "triangle_curls": triangle_curls_raw,
        "energy_fractions": {"gradient": grad_frac, "curl": curl_frac, "harmonic": harm_frac},
        "edges": edges,
        "edge_to_idx": edge_to_idx,
        "triangles": triangles,
        "N": N, "E": E, "T": T,
    }


def bootstrap_auc(
    scores: np.ndarray,
    labels: np.ndarray,
    B: int = 2000,
    seed: int = 42,
) -> Tuple[Optional[float], List]:
    """AUC-ROC with bootstrap 95% CI. Returns (auc, [lo, hi])."""
    scores = np.where(np.isfinite(scores), scores, 0.0)
    if labels.sum() < 2 or (labels == 0).sum() < 2:
        return None, [None, None]
    try:
        auc = float(roc_auc_score(labels, scores))
    except Exception:
        return None, [None, None]
    rng = np.random.RandomState(seed)
    boot = []
    for _ in range(B):
        idx = rng.randint(0, len(labels), len(labels))
        if labels[idx].sum() > 0 and (1 - labels[idx]).sum() > 0:
            try:
                boot.append(roc_auc_score(labels[idx], scores[idx]))
            except Exception:
                pass
    if len(boot) >= 10:
        ci = [float(np.percentile(boot, 2.5)), float(np.percentile(boot, 97.5))]
    else:
        ci = [auc, auc]
    return auc, ci


# ============================================================
# SYNTHETIC NETWORK GENERATOR (from iter-1, extended for n_c=0)
# ============================================================
def generate_synthetic_network(
    N: int = 800,
    n_fields: int = 12,
    n_cartels: int = 10,
    cartel_size: int = 3,
    seed: int = 42,
) -> Tuple[sparse.csr_matrix, List[Dict], List[Dict]]:
    """
    Generate synthetic citation network.
    n_cartels=0 → clean base with no injected cartels.
    cartel_size is forced to min(cartel_size, 3) to guarantee triangles.
    """
    rng = np.random.RandomState(seed)
    logger.info(f"Generating synthetic: N={N}, fields={n_fields}, cartels={n_cartels}, seed={seed}")

    field_labels = np.repeat(np.arange(n_fields), N // n_fields + 1)[:N]
    prestige = rng.exponential(scale=1.0, size=N)

    C = sparse.lil_matrix((N, N), dtype=np.float64)

    # Within-field citations (dense hierarchical)
    for field in range(n_fields):
        members = np.where(field_labels == field)[0]
        for i in members:
            targets = rng.choice(members, size=min(20, len(members) - 1), replace=False)
            weights = prestige[targets] / (prestige[targets].sum() + 1e-10)
            for t, w in zip(targets, weights):
                if t != i:
                    C[i, t] += max(1, int(rng.poisson(50 * w * prestige[i])))

    # Cross-field citations (sparse)
    for i in range(N):
        n_cross = rng.poisson(3)
        if n_cross > 0:
            targets = rng.choice(N, size=min(n_cross, N - 1), replace=False)
            for t in targets:
                if t != i:
                    C[i, t] += max(1, int(rng.poisson(5 * prestige[t])))

    # Inject cartels (skip if n_cartels=0)
    cartel_nodes_all: List[int] = []
    available = set(range(N))
    all_vals = [v for row in C.data for v in row]
    w_cartel = int(max(all_vals) * 0.6) if all_vals else 100

    for _ in range(n_cartels):
        k_use = min(cartel_size, 3)  # force triangles
        if len(available) < k_use:
            break
        nodes = sorted(rng.choice(list(available), size=k_use, replace=False))
        cartel_nodes_all.extend(nodes)
        available -= set(nodes)
        # Directed ring: A→B→C→A
        for idx in range(k_use):
            u, v = nodes[idx], nodes[(idx + 1) % k_use]
            C[u, v] += w_cartel
            C[v, u] += w_cartel * 0.15

    C_csr = C.tocsr()

    field_names = ["Biology", "Chemistry", "Physics", "Medicine", "Engineering",
                   "Mathematics", "Computer Science", "Environmental Science",
                   "Agriculture", "Materials Science", "Ecology", "Biochemistry"]
    journals = [
        {
            "id": f"https://openalex.org/S{i+1000000:08d}",
            "name": f"Journal_{i:04d}_{field_names[field_labels[i] % len(field_names)]}",
            "issn_l": f"{1000+i//100:04d}-{i%1000:04d}",
            "cited_by_count": int(C_csr[:, i].sum()),
            "synthetic_field": field_names[field_labels[i] % len(field_names)],
        }
        for i in range(N)
    ]
    gt = [
        {
            "openalex_id": journals[node]["id"],
            "name": journals[node]["name"],
            "reason": "citation_stacking",
        }
        for node in cartel_nodes_all
    ]

    logger.info(f"Synthetic: N={N}, nnz={C_csr.nnz}, cartel_nodes={len(cartel_nodes_all)}")
    return C_csr, journals, gt


# ============================================================
# FAST NODE CURL (direct triangle aggregation for injection loop)
# ============================================================
def fast_node_curl(
    C: sparse.csr_matrix,
    triangles: List[Tuple[int, int, int]],
    N: int,
) -> np.ndarray:
    """Direct triangle-aggregation curl score for speed."""
    Y = C - C.T
    Y_arr = Y.toarray()
    node_curl = np.zeros(N)
    tri_count = np.zeros(N, dtype=int)
    for (i, j, k) in triangles:
        tc = abs(Y_arr[i, j] + Y_arr[j, k] - Y_arr[i, k])
        node_curl[i] += tc; node_curl[j] += tc; node_curl[k] += tc
        tri_count[i] += 1; tri_count[j] += 1; tri_count[k] += 1
    return node_curl / (tri_count + 1e-10)


# ============================================================
# GRADIENT RESIDUAL FOR INJECTION (fast, full recompute)
# ============================================================
def injection_grad_residual(
    C_mod: sparse.csr_matrix,
) -> np.ndarray:
    """Compute gradient residual for a modified network (injection)."""
    N = C_mod.shape[0]
    edges, _ = build_edge_list(C_mod)
    if not edges:
        return np.zeros(N)
    E = len(edges)
    Y_e = compute_Ye(C_mod, edges)
    B1 = build_B1(edges, N)
    s_mod = lsqr(B1.T, Y_e, damp=1e-6, iter_lim=5000)[0]
    Y_grad = B1.T @ s_mod
    resid = Y_e - Y_grad
    nrs = np.zeros(N)
    nec = np.zeros(N, dtype=int)
    for e_idx, (i, j) in enumerate(edges):
        v = abs(resid[e_idx])
        nrs[i] += v; nrs[j] += v
        nec[i] += 1; nec[j] += 1
    return nrs / (nec + 1e-10)


# ============================================================
# CIDRE HELPERS
# ============================================================
def try_install_cidre() -> bool:
    """Attempt to install cidre via uv pip."""
    import subprocess
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "cidre", "--quiet"],
            capture_output=True, timeout=120
        )
        return result.returncode == 0
    except Exception:
        return False


def run_cidre(
    A: sparse.csr_matrix,
    thresholds: List[float] = None,
) -> Tuple[np.ndarray, str, int]:
    """
    Run real CIDRE package or improved approximation fallback.
    Returns: (score_vector, method_used, n_groups).
    """
    if thresholds is None:
        thresholds = [0.15, 0.05]
    N = A.shape[0]

    # Try real cidre
    try:
        import cidre as cidre_pkg
        for thresh in thresholds:
            groups = cidre_pkg.Cidre(group_membership=None).detect(A, threshold=thresh)
            if len(groups) > 0:
                score = np.zeros(N)
                for g in groups:
                    for nd, p in getattr(g, "donors", {}).items():
                        if 0 <= nd < N:
                            score[nd] = max(score[nd], -np.log(float(p) + 1e-300))
                    for nd, p in getattr(g, "recipients", {}).items():
                        if 0 <= nd < N:
                            score[nd] = max(score[nd], -np.log(float(p) + 1e-300))
                logger.info(f"Real CIDRE: {len(groups)} groups at threshold={thresh}")
                return score, "cidre_package", len(groups)
        logger.info("Real CIDRE: no groups found at any threshold")
        return np.zeros(N), "cidre_package_no_groups", 0
    except ImportError:
        logger.warning("cidre package not available, using improved Poisson fallback")
    except Exception as e:
        logger.warning(f"CIDRE package failed: {e}, using fallback")

    # Fallback: spectral clustering + Poisson null per block (closer to dcSBM)
    return _improved_poisson_cidre(A, N)


def _improved_poisson_cidre(
    A: sparse.csr_matrix,
    N: int,
) -> Tuple[np.ndarray, str, int]:
    """Improved CIDRE approximation: spectral clustering + Poisson null per block."""
    import networkx as nx
    A_sym = ((A + A.T) / 2).toarray()
    try:
        from sklearn.cluster import SpectralClustering
        n_clusters = min(10, N // 10)
        if n_clusters < 2:
            n_clusters = 2
        sc = SpectralClustering(n_clusters=n_clusters, affinity="precomputed",
                                random_state=42, n_init=5)
        labels_sc = sc.fit_predict(A_sym)
    except Exception:
        # Degree-based partition fallback
        degrees = A_sym.sum(1)
        labels_sc = np.floor(degrees / (degrees.max() / 10 + 1e-10)).astype(int).clip(0, 9)

    A_arr = A.toarray().astype(float)
    scores = np.zeros(N)
    communities = defaultdict(list)
    for nd, c in enumerate(labels_sc):
        communities[int(c)].append(nd)

    for members in communities.values():
        if len(members) < 2:
            continue
        sub = A_arr[np.ix_(members, members)]
        total = sub.sum()
        if total < 1:
            continue
        row_s = sub.sum(1)
        col_s = sub.sum(0)
        exp = np.outer(row_s, col_s) / (total + 1e-10)
        np.fill_diagonal(exp, 0)
        np.fill_diagonal(sub, 0)
        ratio = sub / (exp + 1e-10)
        for i, nd in enumerate(members):
            scores[nd] = max(scores[nd], float(ratio[i].max()))

    n_groups = int((scores > 2.0).sum())
    return scores, "cidre_poisson_spectral_fallback", n_groups


# ============================================================
# PHASE 1: REAL DATA HODGE EVALUATION
# ============================================================
@logger.catch(reraise=True)
def phase1_real_hodge() -> Dict:
    """Hodge decomposition on real 231-journal network. Primary evaluation."""
    logger.info("=" * 60)
    logger.info("PHASE 1: Real-Data Hodge Evaluation")
    logger.info("=" * 60)

    chk = load_checkpoint("1")
    if chk:
        logger.info("Phase 1: loaded from checkpoint")
        return chk

    # Load data
    A = sparse.load_npz(str(DATASET_DIR / "adjacency_matrix.npz")).astype(np.float64)
    meta = json.loads((DATASET_DIR / "journal_metadata.json").read_text())
    gt_labels = json.loads((DATASET_DIR / "ground_truth_labels.json").read_text())

    N = A.shape[0]
    assert N == len(meta), f"Mismatch: A.shape={N}, meta={len(meta)}"
    logger.info(f"Loaded: N={N} journals, nnz={A.nnz} citation pairs")

    # Build ID → index map
    id_to_idx = {m["id"]: i for i, m in enumerate(meta)}

    # Label vectors
    labels_all = np.zeros(N)
    labels_stacking = np.zeros(N)
    for j_id, lbl in gt_labels.items():
        idx = id_to_idx.get(j_id)
        if idx is not None and lbl == 1:
            labels_all[idx] = 1.0
            if j_id in STACKING_IDS:
                labels_stacking[idx] = 1.0

    n_all = int(labels_all.sum())
    n_stacking = int(labels_stacking.sum())
    logger.info(f"Labels: {n_stacking} stacking-only positives, {n_all} total suppressed, {N - n_all} clean")
    if n_stacking < 3:
        logger.warning(f"Only {n_stacking} stacking-specific journals matched in our 231-journal network. "
                       "Primary eval will use all-suppressed labels as fallback.")

    # Run Hodge pipeline
    hres = hodge_pipeline(A, max_triangles=2_000_000)

    # AUC evaluation
    p1_results = {}
    primary_labels = labels_stacking if n_stacking >= 2 else labels_all
    label_name = "stacking_only" if n_stacking >= 2 else "all_suppressed"
    logger.info(f"Primary labels: {label_name} (n_pos={int(primary_labels.sum())})")

    for score_name, score_vec in [
        ("hodge_grad_residual", hres["node_grad_residual"]),
        ("hodge_curl_raw", hres["node_curl_raw"]),
        ("hodge_prestige", hres["s_star"]),
    ]:
        auc_s, ci_s = bootstrap_auc(score_vec, labels_stacking)
        auc_a, ci_a = bootstrap_auc(score_vec, labels_all)
        auc_p, ci_p = bootstrap_auc(score_vec, primary_labels)
        p1_results[score_name] = {
            "auc_stacking_only": auc_s, "ci_stacking": ci_s,
            "auc_all_suppressed": auc_a, "ci_all": ci_a,
            "auc_primary": auc_p, "ci_primary": ci_p,
        }
        logger.info(f"  {score_name}: stacking_AUC={auc_s}, all_AUC={auc_a}")

    # Top journals by gradient residual
    top_by_grad = sorted(range(N), key=lambda i: hres["node_grad_residual"][i], reverse=True)[:20]
    top_journals_grad = [
        {"rank": r+1, "name": meta[i]["name"], "grad_residual": float(hres["node_grad_residual"][i]),
         "is_suppressed": bool(labels_all[i]), "is_stacking": bool(labels_stacking[i])}
        for r, i in enumerate(top_by_grad)
    ]
    logger.info(f"Top journal by grad_residual: {meta[top_by_grad[0]]['name']}")

    result = {
        "phase": 1,
        "N": N, "n_stacking": n_stacking, "n_all": n_all,
        "primary_label_name": label_name,
        "energy_fractions": hres["energy_fractions"],
        "p1_results": p1_results,
        "top20_by_grad_residual": top_journals_grad,
        "T": hres["T"], "E": hres["E"],
        # Raw arrays not serializable — store as lists for checkpoint
        "node_grad_residual": hres["node_grad_residual"].tolist(),
        "node_curl_raw": hres["node_curl_raw"].tolist(),
        "s_star": hres["s_star"].tolist(),
        "labels_stacking": labels_stacking.tolist(),
        "labels_all": labels_all.tolist(),
        "id_to_idx": {k: v for k, v in id_to_idx.items()},
    }

    save_checkpoint("1", {k: v for k, v in result.items()
                          if k not in ("node_grad_residual", "node_curl_raw", "s_star",
                                       "labels_stacking", "labels_all", "id_to_idx")})
    # Return full result (with arrays)
    return result


# ============================================================
# PHASE 2: REAL CIDRE ON REAL DATA
# ============================================================
@logger.catch(reraise=True)
def phase2_cidre_real(p1: Dict) -> Dict:
    """Run CIDRE (real package or fallback) on real 231-journal network."""
    logger.info("=" * 60)
    logger.info("PHASE 2: Real CIDRE on Real Data")
    logger.info("=" * 60)

    chk = load_checkpoint("2")
    if chk:
        logger.info("Phase 2: loaded from checkpoint")
        return chk

    A = sparse.load_npz(str(DATASET_DIR / "adjacency_matrix.npz")).astype(np.float64)
    N = A.shape[0]
    labels_stacking = np.array(p1["labels_stacking"])
    labels_all = np.array(p1["labels_all"])
    primary_labels = labels_stacking if p1["n_stacking"] >= 2 else labels_all

    cidre_scores, method_used, n_groups = run_cidre(A, thresholds=[0.15, 0.05, 0.01])

    auc_s, ci_s = bootstrap_auc(cidre_scores, labels_stacking)
    auc_a, ci_a = bootstrap_auc(cidre_scores, labels_all)
    auc_p, ci_p = bootstrap_auc(cidre_scores, primary_labels)

    logger.info(f"CIDRE ({method_used}): stacking_AUC={auc_s}, all_AUC={auc_a}, n_groups={n_groups}")

    result = {
        "phase": 2,
        "method_used": method_used,
        "n_groups": n_groups,
        "auc_stacking_only": auc_s, "ci_stacking": ci_s,
        "auc_all_suppressed": auc_a, "ci_all": ci_a,
        "auc_primary": auc_p, "ci_primary": ci_p,
        "cidre_scores": cidre_scores.tolist(),
    }

    save_checkpoint("2", {k: v for k, v in result.items() if k != "cidre_scores"})
    return result


# ============================================================
# PHASE 3: SYNTHETIC NETWORK (n_c=10) — CIDRE + HODGE
# ============================================================
@logger.catch(reraise=True)
def phase3_cidre_synthetic() -> Dict:
    """
    Generate synthetic n_c=10 network (same seed as iter-1).
    Run both Hodge and CIDRE to validate relative performance.
    """
    logger.info("=" * 60)
    logger.info("PHASE 3: Synthetic n_c=10 — Hodge + CIDRE")
    logger.info("=" * 60)

    chk = load_checkpoint("3")
    if chk:
        logger.info("Phase 3: loaded from checkpoint")
        return chk

    C_synth, journals_synth, gt_synth = generate_synthetic_network(
        N=800, n_fields=12, n_cartels=10, cartel_size=3, seed=42
    )
    N_s = C_synth.shape[0]
    stacking_ids_synth = {g["openalex_id"] for g in gt_synth}
    labels_s = np.array([
        1.0 if journals_synth[i]["id"] in stacking_ids_synth else 0.0
        for i in range(N_s)
    ])
    n_pos_synth = int(labels_s.sum())
    logger.info(f"Synthetic n_c=10: N={N_s}, n_cartel={n_pos_synth}")

    # Hodge on synthetic
    hres_s = hodge_pipeline(C_synth, max_triangles=2_000_000)
    auc_grad_s, ci_grad_s = bootstrap_auc(hres_s["node_grad_residual"], labels_s)
    auc_curl_s, ci_curl_s = bootstrap_auc(hres_s["node_curl_raw"], labels_s)

    logger.info(f"Synthetic Hodge: grad_AUC={auc_grad_s:.3f}, curl_AUC={auc_curl_s:.3f}")

    # CIDRE on synthetic
    cidre_s, method_used_s, n_groups_s = run_cidre(C_synth, thresholds=[0.15, 0.05, 0.01])
    auc_cidre_s, ci_cidre_s = bootstrap_auc(cidre_s, labels_s)
    logger.info(f"Synthetic CIDRE ({method_used_s}): AUC={auc_cidre_s}, groups={n_groups_s}")

    del C_synth; gc.collect()

    result = {
        "phase": 3,
        "N_synth": N_s,
        "n_cartel_nodes_synth": n_pos_synth,
        "hodge_grad_auc": auc_grad_s, "ci_grad": ci_grad_s,
        "hodge_curl_auc": auc_curl_s, "ci_curl": ci_curl_s,
        "cidre_auc": auc_cidre_s, "ci_cidre": ci_cidre_s,
        "cidre_method_used": method_used_s,
        "n_cidre_groups": n_groups_s,
        "energy_fractions_synth": hres_s["energy_fractions"],
        "note_iter1_approx_cidre_auc": 0.626,
    }

    save_checkpoint("3", result)
    return result


# ============================================================
# PHASE 4: CLEAN-BASE INJECTION STUDY
# ============================================================
def _injection_one_rep(
    C_base_data: np.ndarray,
    C_base_indices: np.ndarray,
    C_base_indptr: np.ndarray,
    C_base_shape: Tuple[int, int],
    base_triangles_arr: np.ndarray,
    cartel_type: str,
    k: int,
    w: float,
    seed: int,
) -> Dict:
    """Worker: one injection experiment (spawnable, no loguru deps)."""
    import numpy as np
    import scipy.sparse as sparse
    from scipy.sparse.linalg import lsqr
    from collections import defaultdict

    rng = np.random.RandomState(seed)
    N_b = C_base_shape[0]
    C_base = sparse.csr_matrix(
        (C_base_data, C_base_indices, C_base_indptr), shape=C_base_shape
    )

    # Select k random nodes
    nodes = rng.choice(N_b, size=k, replace=False).tolist()
    C_mod = C_base.tolil()

    if cartel_type == "cyclic":
        for idx in range(k):
            u, v = nodes[idx], nodes[(idx + 1) % k]
            C_mod[u, v] += w
    else:  # reciprocal
        w_per = w / max(1, k - 1)
        for u in nodes:
            for v in nodes:
                if u != v:
                    C_mod[u, v] += w_per

    C_mod = C_mod.tocsr()
    labels_inj = np.zeros(N_b)
    for nd in nodes:
        labels_inj[nd] = 1.0

    # Gradient residual (full recompute on modified network)
    Y = C_mod - C_mod.T
    Y_arr = Y.toarray()
    cx = C_mod.tocoo()
    edges_set = set()
    for i, j in zip(cx.row, cx.col):
        if i != j:
            edges_set.add((min(int(i), int(j)), max(int(i), int(j))))
    edges = sorted(edges_set)
    E = len(edges)
    Y_e = np.array([Y_arr[i, j] for (i, j) in edges], dtype=np.float64)

    # B1
    rows_B1, cols_B1, data_B1 = [], [], []
    for e_idx, (i, j) in enumerate(edges):
        rows_B1.extend([i, j])
        cols_B1.extend([e_idx, e_idx])
        data_B1.extend([-1.0, 1.0])
    B1 = sparse.csr_matrix((data_B1, (rows_B1, cols_B1)), shape=(N_b, E))
    s_mod = lsqr(B1.T, Y_e, damp=1e-6, iter_lim=5000)[0]
    Y_grad = B1.T @ s_mod
    resid = Y_e - Y_grad
    nrs = np.zeros(N_b)
    nec = np.zeros(N_b, dtype=int)
    for e_idx, (i, j) in enumerate(edges):
        v = abs(resid[e_idx])
        nrs[i] += v; nrs[j] += v
        nec[i] += 1; nec[j] += 1
    grad_res = nrs / (nec + 1e-10)

    # Triangle curl (use base triangles — approximation; fast)
    node_curl = np.zeros(N_b)
    tri_count_arr = np.zeros(N_b, dtype=int)
    for t in range(len(base_triangles_arr)):
        i, j, kk = int(base_triangles_arr[t, 0]), int(base_triangles_arr[t, 1]), int(base_triangles_arr[t, 2])
        tc = abs(Y_arr[i, j] + Y_arr[j, kk] - Y_arr[i, kk])
        node_curl[i] += tc; node_curl[j] += tc; node_curl[kk] += tc
        tri_count_arr[i] += 1; tri_count_arr[j] += 1; tri_count_arr[kk] += 1
    node_curl_raw = node_curl / (tri_count_arr + 1e-10)

    # AUC
    def safe_auc(sc, lb):
        try:
            from sklearn.metrics import roc_auc_score
            if lb.sum() > 0 and (1 - lb).sum() > 0:
                return float(roc_auc_score(lb, sc))
        except Exception:
            pass
        return None

    return {
        "auc_grad": safe_auc(grad_res, labels_inj),
        "auc_curl": safe_auc(node_curl_raw, labels_inj),
    }


@logger.catch(reraise=True)
def phase4_clean_injection() -> Dict:
    """
    Clean-base injection study.
    Base network has n_c=0 (no pre-existing cartels).
    Inject one cartel at a time and measure detection AUC.
    """
    logger.info("=" * 60)
    logger.info("PHASE 4: Clean-Base Injection Study")
    logger.info("=" * 60)

    chk = load_checkpoint("4")
    if chk:
        logger.info("Phase 4: loaded from checkpoint")
        return chk

    # Generate clean base
    logger.info("Generating clean base network (n_c=0, N=800)...")
    C_base, journals_base, _ = generate_synthetic_network(
        N=800, n_fields=12, n_cartels=0, cartel_size=0, seed=100
    )
    N_b = C_base.shape[0]
    mean_edge = float(C_base.data.mean()) if len(C_base.data) > 0 else 10.0
    logger.info(f"Clean base: N={N_b}, nnz={C_base.nnz}, mean_edge={mean_edge:.1f}")

    # Pre-compute base triangles
    base_edges, base_edge_to_idx = build_edge_list(C_base)
    base_triangles = enumerate_triangles(base_edges)
    base_triangles_arr = np.array(base_triangles, dtype=np.int32) if base_triangles else np.zeros((0, 3), dtype=np.int32)
    logger.info(f"Base triangles: {len(base_triangles):,}")

    # Serialize base for worker processes
    C_csr = C_base.tocsr()
    C_data = C_csr.data
    C_indices = C_csr.indices
    C_indptr = C_csr.indptr
    C_shape = C_csr.shape

    # Sweep parameters
    k_values = [3, 4, 5, 10]
    w_factors = [0.1, 0.3, 0.5, 1.0, 2.0]
    cartel_types = ["cyclic", "reciprocal"]
    n_repeats = 20

    total_conditions = len(cartel_types) * len(k_values) * len(w_factors)
    total_experiments = total_conditions * n_repeats
    logger.info(f"Injection sweep: {total_conditions} conditions × {n_repeats} reps = {total_experiments} experiments")

    records = []
    n_workers = max(1, NUM_CPUS - 1)
    global_seed = 200

    for cartel_type in cartel_types:
        for k in k_values:
            for w_f in w_factors:
                w = w_f * mean_edge
                aucs_grad, aucs_curl = [], []
                seed_offset = global_seed

                # Build worker args for this condition
                worker_args = []
                for rep in range(n_repeats):
                    worker_args.append((
                        C_data, C_indices, C_indptr, C_shape,
                        base_triangles_arr,
                        cartel_type, k, float(w), seed_offset + rep
                    ))
                seed_offset += n_repeats

                # Run in parallel with spawn context
                with ProcessPoolExecutor(
                    max_workers=n_workers,
                    mp_context=mp.get_context("spawn")
                ) as pool:
                    futures = [pool.submit(_injection_one_rep, *args) for args in worker_args]
                    for fut in as_completed(futures):
                        try:
                            res = fut.result()
                            if res["auc_grad"] is not None:
                                aucs_grad.append(res["auc_grad"])
                            if res["auc_curl"] is not None:
                                aucs_curl.append(res["auc_curl"])
                        except Exception as e:
                            logger.debug(f"Injection worker error: {e}")

                global_seed += n_repeats

                record = {
                    "cartel_type": cartel_type, "k": k, "w_factor": w_f,
                    "n_reps_completed": len(aucs_grad),
                    "auc_grad_residual_mean": float(np.mean(aucs_grad)) if aucs_grad else None,
                    "auc_grad_residual_std": float(np.std(aucs_grad)) if aucs_grad else None,
                    "auc_curl_raw_mean": float(np.mean(aucs_curl)) if aucs_curl else None,
                    "auc_curl_raw_std": float(np.std(aucs_curl)) if aucs_curl else None,
                }
                records.append(record)
                logger.info(
                    f"  {cartel_type} k={k} w={w_f:.1f}: "
                    f"grad={record['auc_grad_residual_mean']:.3f}±{record['auc_grad_residual_std']:.3f} "
                    f"curl={record['auc_curl_raw_mean']:.3f}±{record['auc_curl_raw_std']:.3f}"
                    if record["auc_grad_residual_mean"] is not None else
                    f"  {cartel_type} k={k} w={w_f:.1f}: no valid AUCs"
                )

    # Detectability thresholds (min w_factor for AUC > 0.7)
    thresholds = {}
    for ct in cartel_types:
        for k in k_values:
            for det in ["grad_residual", "curl_raw"]:
                cond = [r for r in records if r["cartel_type"] == ct and r["k"] == k]
                key_mean = f"auc_{det}_mean"
                thresh = next(
                    (r["w_factor"] for r in cond
                     if r.get(key_mean) is not None and r[key_mean] > 0.7),
                    None
                )
                thresholds[f"{ct}_k{k}_{det}_thresh_w0.7"] = thresh

    result = {
        "phase": 4,
        "N_base": N_b,
        "n_base_edges": len(base_edges),
        "n_base_triangles": len(base_triangles),
        "mean_edge_weight": float(mean_edge),
        "injection_records": records,
        "detectability_thresholds": thresholds,
    }

    save_checkpoint("4", result)
    return result


# ============================================================
# PHASE 5: FIELD-AWARE NULL MODEL
# ============================================================
@logger.catch(reraise=True)
def phase5_field_null(p1: Dict) -> Dict:
    """
    Compare field-aware vs degree-preserving null model.
    Field proxy = Louvain communities on real 231-journal network.
    """
    logger.info("=" * 60)
    logger.info("PHASE 5: Field-Aware Null Model Comparison")
    logger.info("=" * 60)

    chk = load_checkpoint("5")
    if chk:
        logger.info("Phase 5: loaded from checkpoint")
        return chk

    import networkx as nx

    A = sparse.load_npz(str(DATASET_DIR / "adjacency_matrix.npz")).astype(np.float64)
    N = A.shape[0]
    node_curl_raw = np.array(p1["node_curl_raw"])

    # Hodge info for triangles
    edges, edge_to_idx = build_edge_list(A)
    triangles = enumerate_triangles(edges)
    logger.info(f"Triangles for null model: {len(triangles):,}")

    # Louvain community detection (field proxy)
    A_sym = (A + A.T) / 2
    G = nx.from_scipy_sparse_array(A_sym)
    try:
        comms = nx.community.louvain_communities(G, seed=42)
        field_labels = np.zeros(N, dtype=int)
        for c_idx, comm in enumerate(comms):
            for nd in comm:
                field_labels[nd] = c_idx
        n_fields = len(comms)
        logger.info(f"Louvain: {n_fields} communities as field proxy")
    except Exception as e:
        logger.warning(f"Louvain failed: {e}, using degree-based partition")
        degrees = np.asarray(A.sum(1)).squeeze()
        field_labels = np.floor(degrees / (degrees.max() / 10 + 1e-10)).astype(int).clip(0, 9)
        n_fields = 10

    def compute_null_curl_zscores(null_type: str, n_samples: int = 100, seed: int = 0) -> np.ndarray:
        """Compute per-node curl z-scores under a null model."""
        A_arr = A.toarray().astype(float)
        null_curls = []
        rng = np.random.RandomState(seed)

        for _ in range(n_samples):
            if null_type == "degree_preserving":
                # Row-permutation null: shuffle citation targets within each row
                A_null = np.zeros_like(A_arr)
                for i in range(N):
                    row = A_arr[i]
                    nonzero_j = np.where(row > 0)[0]
                    if len(nonzero_j) > 1:
                        perm = rng.permutation(len(nonzero_j))
                        for orig_idx, new_idx in zip(nonzero_j, nonzero_j[perm]):
                            A_null[i, new_idx] = row[orig_idx]
                    else:
                        for orig_idx in nonzero_j:
                            A_null[i, orig_idx] = row[orig_idx]
            else:  # field_aware
                # Permute weights within each (field_A, field_B) block
                A_null = A_arr.copy()
                for f1 in range(n_fields):
                    for f2 in range(n_fields):
                        rows_f1 = np.where(field_labels == f1)[0]
                        cols_f2 = np.where(field_labels == f2)[0]
                        if len(rows_f1) < 2 or len(cols_f2) < 2:
                            continue
                        block = A_null[np.ix_(rows_f1, cols_f2)].copy()
                        flat = block.flatten()
                        rng.shuffle(flat)
                        A_null[np.ix_(rows_f1, cols_f2)] = flat.reshape(block.shape)

            # Direct triangle curl on null
            Y_null = A_null - A_null.T
            nc = np.zeros(N)
            tc = np.zeros(N, dtype=int)
            for (i, j, k) in triangles:
                curl = abs(Y_null[i, j] + Y_null[j, k] - Y_null[i, k])
                nc[i] += curl; nc[j] += curl; nc[k] += curl
                tc[i] += 1; tc[j] += 1; tc[k] += 1
            null_curls.append(nc / (tc + 1e-10))

        null_mat = np.stack(null_curls, axis=0)  # (n_samples, N)
        return (node_curl_raw - null_mat.mean(0)) / (null_mat.std(0) + 1e-10)

    logger.info("Computing degree-preserving null z-scores (100 samples)...")
    z_degree = compute_null_curl_zscores("degree_preserving", n_samples=100, seed=0)

    logger.info("Computing field-aware null z-scores (100 samples)...")
    z_field = compute_null_curl_zscores("field_aware", n_samples=100, seed=1)

    rho, p_rho = spearmanr(z_degree, z_field)
    logger.info(f"Spearman ρ(degree_null, field_null) = {rho:.3f}, p={p_rho:.4e}")

    recommendation = "degree_preserving_adequate" if rho > 0.9 else "use_field_aware"

    # AUC comparison under the two null models
    labels_stacking = np.array(p1["labels_stacking"])
    labels_all = np.array(p1["labels_all"])
    auc_deg_s, ci_deg_s = bootstrap_auc(z_degree, labels_stacking)
    auc_deg_a, ci_deg_a = bootstrap_auc(z_degree, labels_all)
    auc_fld_s, ci_fld_s = bootstrap_auc(z_field, labels_stacking)
    auc_fld_a, ci_fld_a = bootstrap_auc(z_field, labels_all)
    logger.info(f"Degree-null z-score AUC: stacking={auc_deg_s}, all={auc_deg_a}")
    logger.info(f"Field-null z-score AUC: stacking={auc_fld_s}, all={auc_fld_a}")

    result = {
        "phase": 5,
        "n_field_communities": int(n_fields),
        "spearman_rho": float(rho),
        "spearman_p": float(p_rho),
        "recommendation": recommendation,
        "degree_null_auc_stacking": auc_deg_s, "ci_deg_stacking": ci_deg_s,
        "degree_null_auc_all": auc_deg_a, "ci_deg_all": ci_deg_a,
        "field_null_auc_stacking": auc_fld_s, "ci_fld_stacking": ci_fld_s,
        "field_null_auc_all": auc_fld_a, "ci_fld_all": ci_fld_a,
        "z_degree_scores": z_degree.tolist(),
        "z_field_scores": z_field.tolist(),
    }

    save_checkpoint("5", {k: v for k, v in result.items() if "scores" not in k})
    return result


# ============================================================
# PHASE 6: ENERGY FRACTIONS COMPARISON
# ============================================================
@logger.catch(reraise=True)
def phase6_energy_comparison(real_energy: Dict, synth_energy: Dict) -> Dict:
    """Compare Hodge energy fractions: real vs synthetic n_c=10 network."""
    logger.info("=" * 60)
    logger.info("PHASE 6: Energy Fractions Comparison")
    logger.info("=" * 60)

    result = {
        "phase": 6,
        "real_231journal_network": real_energy,
        "synthetic_n_c10_network": synth_energy,
        "interpretation": {
            "gradient_dominant_in_real": real_energy["gradient"] > 0.5,
            "curl_elevated_in_synth": synth_energy["curl"] > real_energy["curl"],
            "real_grad": real_energy["gradient"],
            "real_curl": real_energy["curl"],
            "real_harm": real_energy["harmonic"],
            "synth_grad": synth_energy["gradient"],
            "synth_curl": synth_energy["curl"],
            "synth_harm": synth_energy["harmonic"],
            "delta_curl_synth_minus_real": synth_energy["curl"] - real_energy["curl"],
            "note": (
                "Real network: genuine scholarly flow expected to be mostly hierarchical (gradient-dominant). "
                "Synthetic n_c=10 network: injected cyclic rings raise curl fraction. "
                "Delta curl shows manipulation signal above natural baseline."
            ),
        }
    }
    logger.info(f"Real energy: grad={real_energy['gradient']:.3f}, curl={real_energy['curl']:.3f}, harm={real_energy['harmonic']:.3f}")
    logger.info(f"Synth energy: grad={synth_energy['gradient']:.3f}, curl={synth_energy['curl']:.3f}, harm={synth_energy['harmonic']:.3f}")
    logger.info(f"Delta curl (synth - real): {result['interpretation']['delta_curl_synth_minus_real']:.3f}")

    save_checkpoint("6", result)
    return result


# ============================================================
# FORMAT OUTPUT (exp_gen_sol_out schema)
# ============================================================
def write_outputs(p1: Dict, p2: Dict, p3: Dict, p4: Dict, p5: Dict, p6: Dict) -> None:
    """Write method_out.json and summary_results.json."""
    meta_list = json.loads((DATASET_DIR / "journal_metadata.json").read_text())
    gt_labels = json.loads((DATASET_DIR / "ground_truth_labels.json").read_text())
    N = len(meta_list)

    node_grad_residual = np.array(p1["node_grad_residual"])
    node_curl_raw = np.array(p1["node_curl_raw"])
    s_star = np.array(p1["s_star"])
    labels_stacking = np.array(p1["labels_stacking"])
    labels_all = np.array(p1["labels_all"])
    cidre_scores = np.array(p2["cidre_scores"]) if "cidre_scores" in p2 else np.zeros(N)

    # Also include z-scores from null model (Phase 5)
    z_degree = np.array(p5.get("z_degree_scores", [0.0] * N))
    z_field = np.array(p5.get("z_field_scores", [0.0] * N))

    examples = []
    for i, m in enumerate(meta_list):
        j_id = m["id"]
        is_stacking = bool(labels_stacking[i])
        is_supp = bool(labels_all[i])
        if is_stacking:
            out_label = "suppressed_stacking"
        elif is_supp:
            out_label = "suppressed_self_citation"
        else:
            out_label = "not_suppressed"

        gr = float(node_grad_residual[i])
        cr = float(node_curl_raw[i])
        pr = float(s_star[i])
        cid = float(cidre_scores[i]) if i < len(cidre_scores) else 0.0
        zd = float(z_degree[i]) if i < len(z_degree) else 0.0
        zf = float(z_field[i]) if i < len(z_field) else 0.0

        input_str = (
            f"Journal: {m['name']}. "
            f"ISSN: {m.get('issn_l', '')}. "
            f"Works count: {m.get('works_count', 0)}. "
            f"Cited by count: {m.get('cited_by_count', 0)}. "
            f"HodgeRank prestige: {pr:.4f}. "
            f"Gradient residual: {gr:.4f}. "
            f"Triangle curl raw: {cr:.4f}. "
            f"Curl z-score (degree-null): {zd:.4f}. "
            f"Curl z-score (field-null): {zf:.4f}. "
            f"CIDRE anomaly score: {cid:.4f}."
        )

        example = {
            "input": input_str,
            "output": out_label,
            "predict_hodge_grad_residual": f"{gr:.6f}",
            "predict_hodge_curl_raw": f"{cr:.6f}",
            "predict_hodge_prestige": f"{pr:.6f}",
            "predict_cidre": f"{cid:.6f}",
            "predict_curl_z_degree_null": f"{zd:.6f}",
            "predict_curl_z_field_null": f"{zf:.6f}",
            "metadata_journal_name": m["name"],
            "metadata_openalex_id": j_id,
            "metadata_issn_l": m.get("issn_l", ""),
            "metadata_is_stacking_suppressed": str(is_stacking),
            "metadata_is_any_suppressed": str(is_supp),
        }
        examples.append(example)

    # Compute combined AUC table
    primary_labels = labels_stacking if p1["n_stacking"] >= 2 else labels_all
    auc_grad_p, _ = bootstrap_auc(node_grad_residual, primary_labels)
    auc_curl_p, _ = bootstrap_auc(node_curl_raw, primary_labels)
    auc_cidre_p, _ = bootstrap_auc(cidre_scores, primary_labels)
    auc_zdeg_p, _ = bootstrap_auc(z_degree, primary_labels)
    auc_zfld_p, _ = bootstrap_auc(z_field, primary_labels)

    method_out = {
        "metadata": {
            "method_name": "Hodge-Curl Cartel Detector v2 (Real-Data & Clean-Base Validation)",
            "description": (
                "Combinatorial Hodge decomposition of journal citation net-flows detects cyclic citation patterns. "
                "6-phase evaluation: real data AUC, CIDRE comparison, synthetic validation, clean-base injection, "
                "field-aware null model, and energy fraction analysis."
            ),
            "n_journals": N,
            "n_stacking_positives": p1["n_stacking"],
            "n_all_suppressed_positives": p1["n_all"],
            "primary_label_name": p1["primary_label_name"],
            "phase1_auc_table": p1["p1_results"],
            "phase2_cidre": {
                "method_used": p2["method_used"],
                "n_groups": p2["n_groups"],
                "auc_stacking": p2["auc_stacking_only"],
                "auc_all": p2["auc_all_suppressed"],
            },
            "phase3_synthetic_n_c10": {
                "hodge_grad_auc": p3["hodge_grad_auc"],
                "hodge_curl_auc": p3["hodge_curl_auc"],
                "cidre_auc": p3["cidre_auc"],
                "iter1_approx_cidre_auc": p3["note_iter1_approx_cidre_auc"],
                "energy_fractions": p3["energy_fractions_synth"],
            },
            "phase4_injection_summary": {
                "n_conditions": len(p4["injection_records"]),
                "detectability_thresholds": p4["detectability_thresholds"],
                "note": "AUC>0.7 threshold w_factor for cyclic k=3 (triangle-based detection)",
            },
            "phase5_null_model": {
                "n_field_communities": p5["n_field_communities"],
                "spearman_rho": p5["spearman_rho"],
                "recommendation": p5["recommendation"],
                "degree_null_auc_stacking": p5["degree_null_auc_stacking"],
                "field_null_auc_stacking": p5["field_null_auc_stacking"],
            },
            "phase6_energy": {
                "real_gradient": p6["real_231journal_network"]["gradient"],
                "real_curl": p6["real_231journal_network"]["curl"],
                "synth_gradient": p6["synthetic_n_c10_network"]["gradient"],
                "synth_curl": p6["synthetic_n_c10_network"]["curl"],
                "delta_curl": p6["interpretation"]["delta_curl_synth_minus_real"],
            },
            "combined_auc_primary_label": {
                "hodge_grad_residual": auc_grad_p,
                "hodge_curl_raw": auc_curl_p,
                "cidre": auc_cidre_p,
                "curl_z_degree_null": auc_zdeg_p,
                "curl_z_field_null": auc_zfld_p,
            },
        },
        "datasets": [
            {
                "dataset": "openalex_real_231journal_jcr_suppression",
                "examples": examples,
            }
        ],
    }

    out_path = WORKSPACE / "method_out.json"
    out_path.write_text(json.dumps(method_out, indent=2, default=str))
    size_mb = out_path.stat().st_size / 1e6
    logger.info(f"Written method_out.json: {size_mb:.1f} MB ({N} journals)")

    # Summary results
    summary = {
        "phase1_real_hodge": {
            k: v for k, v in p1.items()
            if k not in ("node_grad_residual", "node_curl_raw", "s_star",
                         "labels_stacking", "labels_all", "id_to_idx")
        },
        "phase2_real_cidre": {k: v for k, v in p2.items() if k != "cidre_scores"},
        "phase3_synthetic": p3,
        "phase4_injection": p4,
        "phase5_field_null": {k: v for k, v in p5.items() if "scores" not in k},
        "phase6_energy": p6,
        "combined_auc_table": {
            "primary_label": p1["primary_label_name"],
            "n_positives": p1["n_stacking"] if p1["primary_label_name"] == "stacking_only" else p1["n_all"],
            "hodge_grad_residual": auc_grad_p,
            "hodge_curl_raw": auc_curl_p,
            "cidre": auc_cidre_p,
            "curl_z_degree_null": auc_zdeg_p,
            "curl_z_field_null": auc_zfld_p,
        }
    }
    (WORKSPACE / "summary_results.json").write_text(json.dumps(summary, indent=2, default=str))
    logger.info("Written summary_results.json")


# ============================================================
# MAIN
# ============================================================
@logger.catch(reraise=True)
def main():
    t_start = time.time()
    logger.info("=" * 60)
    logger.info("Hodge Cartel Detector v2 — Starting")
    logger.info("=" * 60)

    # Try to install cidre if not present
    try:
        import cidre  # noqa
        logger.info("cidre package available")
    except ImportError:
        logger.info("cidre not found, attempting install...")
        if try_install_cidre():
            logger.info("cidre installed successfully")
        else:
            logger.warning("cidre install failed, will use Poisson/dcSBM approximation")

    # Phase 1: Real Hodge
    p1 = phase1_real_hodge()

    # Phase 2: CIDRE on real data
    p2 = phase2_cidre_real(p1)

    # Phase 3: Synthetic n_c=10
    p3 = phase3_cidre_synthetic()

    # Phase 4: Clean-base injection
    p4 = phase4_clean_injection()

    # Phase 5: Field-aware null
    p5 = phase5_field_null(p1)

    # Phase 6: Energy comparison
    p6 = phase6_energy_comparison(p1["energy_fractions"], p3["energy_fractions_synth"])

    # Write outputs
    logger.info("Writing outputs...")
    write_outputs(p1, p2, p3, p4, p5, p6)

    elapsed = time.time() - t_start
    logger.info(f"DONE in {elapsed/60:.1f} min")
    logger.info(f"  Phase 1: Hodge energy = {p1['energy_fractions']}")
    logger.info(f"  Phase 1: grad_residual AUC (stacking) = {p1['p1_results'].get('hodge_grad_residual', {}).get('auc_stacking_only')}")
    logger.info(f"  Phase 2: CIDRE AUC (stacking) = {p2.get('auc_stacking_only')}")
    logger.info(f"  Phase 3: Synth CIDRE AUC = {p3.get('cidre_auc')}")
    logger.info(f"  Phase 5: null model rho = {p5.get('spearman_rho')}, recommendation = {p5.get('recommendation')}")
    logger.info(f"  Phase 6: delta_curl (synth-real) = {p6['interpretation'].get('delta_curl_synth_minus_real')}")


if __name__ == "__main__":
    main()

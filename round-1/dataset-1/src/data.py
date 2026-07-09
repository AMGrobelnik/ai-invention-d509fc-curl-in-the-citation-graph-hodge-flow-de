# /// script
# requires-python = ">=3.12"
# dependencies = ["scipy", "numpy"]
# ///
"""
Load OpenAlex Journal Citation Network from temp/datasets/ and write full_data_out.json
in exp_sel_data_out schema format.

One example per directed citation pair (i→j) where C[i,j] > 0.
15,188 directed pairs → 15,188 examples.

Input: citation features as structured text prompt.
Output: binary suppression label for journal i (string "0"/"1").
"""
import json
import sys
from pathlib import Path

import numpy as np
import scipy.sparse as sp

WS = Path(__file__).parent
DATASETS_DIR = WS / "temp" / "datasets"

def main():
    # --- Load raw files ---
    print("Loading raw data from temp/datasets/ ...")
    meta_list = json.loads((DATASETS_DIR / "journal_metadata.json").read_text())
    gt = json.loads((DATASETS_DIR / "ground_truth_labels.json").read_text())
    C = sp.load_npz(str(DATASETS_DIR / "adjacency_matrix.npz"))

    meta = {j["id"]: j for j in meta_list}
    all_ids = sorted(gt.keys())
    id2idx = {sid: i for i, sid in enumerate(all_ids)}
    idx2id = {i: sid for sid, i in id2idx.items()}

    print(f"  Journals: {len(all_ids)}, Suppressed: {sum(gt.values())}")
    print(f"  Matrix: {C.shape}, nnz={C.nnz}")

    # --- Build examples: one per directed pair (i→j) where C[i,j] > 0 ---
    coo = C.tocoo()
    examples = []
    for row_idx, (r, c, v) in enumerate(zip(coo.row, coo.col, coo.data)):
        sid_i = idx2id[r]
        sid_j = idx2id[c]
        c_ij = int(v)
        c_ji = int(C[c, r])
        net_flow = c_ij - c_ji
        label_i = int(gt.get(sid_i, 0))
        label_j = int(gt.get(sid_j, 0))

        m_i = meta.get(sid_i, {})
        m_j = meta.get(sid_j, {})
        name_i = m_i.get("name", sid_i.split("/")[-1])
        name_j = m_j.get("name", sid_j.split("/")[-1])
        field_i = m_i.get("field", "")
        works_i = m_i.get("works_count", 0)

        input_text = (
            f"Journal citation pair (2015-2022): [{name_i}] cites [{name_j}] "
            f"{c_ij} times; [{name_j}] cites [{name_i}] {c_ji} times; "
            f"net flow ({name_i}→{name_j}) = {net_flow}. "
            f"Journal [{name_i}] field: {field_i or 'unknown'}; "
            f"works in period: {works_i}. "
            f"Task: classify whether [{name_i}] was suppressed by Clarivate JCR "
            f"for citation manipulation (stacking or excessive self-citation) "
            f"during 2018-2022."
        )

        examples.append({
            "input": input_text,
            "output": str(label_i),
            "metadata_source_id_i": sid_i,
            "metadata_source_id_j": sid_j,
            "metadata_journal_name_i": name_i,
            "metadata_journal_name_j": name_j,
            "metadata_citation_count_ij": c_ij,
            "metadata_citation_count_ji": c_ji,
            "metadata_net_flow_ij": net_flow,
            "metadata_year_window": "2015-2022",
            "metadata_label_i": label_i,
            "metadata_label_j": label_j,
            "metadata_works_count_i": works_i,
            "metadata_field_i": field_i,
            "metadata_task_type": "binary_classification",
            "metadata_row_index": row_idx,
        })

    pos = sum(1 for e in examples if e["metadata_label_i"] == 1)
    print(f"  Examples: {len(examples)} ({pos} with suppressed journal-i, "
          f"{len(examples)-pos} with non-suppressed journal-i)")

    # --- Assemble exp_sel_data_out schema ---
    data_out = {
        "metadata": {
            "source": "OpenAlex API (2015-2022) + Clarivate JCR suppressed title lists",
            "task": (
                "Binary node classification: given a directed journal×journal "
                "citation pair, predict whether the source journal was suppressed "
                "by Clarivate JCR for citation manipulation. "
                "Designed for Hodge decomposition feature extraction on citation networks."
            ),
            "label_description": (
                "label=1: journal suppressed by Clarivate JCR 2018-2022 "
                "for citation stacking or excessive self-citation; label=0: not suppressed"
            ),
            "n_journals": len(all_ids),
            "n_suppressed_journals": int(sum(gt.values())),
            "n_citation_pairs": len(examples),
            "graph_edges": C.nnz,
            "year_window": "2015-2022",
            "suppression_rate": round(int(sum(gt.values())) / len(all_ids), 4),
        },
        "datasets": [
            {
                "dataset": "openalex_journal_citation_network_jcr_suppression",
                "examples": examples,
            }
        ],
    }

    out_path = WS / "full_data_out.json"
    out_path.write_text(json.dumps(data_out))
    size_mb = out_path.stat().st_size / 1e6
    print(f"\nWrote full_data_out.json: {len(examples)} examples, {size_mb:.1f} MB")


if __name__ == "__main__":
    main()

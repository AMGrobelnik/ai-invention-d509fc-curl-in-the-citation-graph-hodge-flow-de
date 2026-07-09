#!/usr/bin/env python3
"""Convert raw citation data into exp_sel_data_out schema format.

One example per journal: input = citation neighborhood summary,
output = binary suppression label (string "0"/"1").
"""
import json
from collections import defaultdict
from pathlib import Path

WS = Path(__file__).parent

pairs = json.loads((WS / "data_out.json").read_text())
meta_list = json.loads((WS / "journal_metadata.json").read_text())
gt = json.loads((WS / "ground_truth_labels.json").read_text())

meta = {j["id"]: j for j in meta_list}

# Aggregate per-journal stats from pairs
out_citations = defaultdict(int)   # sum of c_ij (journal i cites j)
in_citations = defaultdict(int)    # sum of c_ji (journal j cites i)
out_partners = defaultdict(list)   # top cited journals
in_partners = defaultdict(list)    # top citing journals

for r in pairs:
    sid_i = r["source_id_i"]
    sid_j = r["source_id_j"]
    c_ij = r["citation_count_ij"]
    c_ji = r["citation_count_ji"]
    out_citations[sid_i] += c_ij
    in_citations[sid_i] += c_ji
    out_partners[sid_i].append((c_ij, sid_j))
    in_partners[sid_i].append((c_ji, sid_j))

all_journals = sorted(gt.keys())

examples = []
for sid in all_journals:
    m = meta.get(sid, {})
    name = m.get("name", sid.split("/")[-1])
    issn_l = m.get("issn_l", "")
    works_count = m.get("works_count", 0)
    cited_by_count = m.get("cited_by_count", 0)
    label = gt.get(sid, 0)

    sum_out = out_citations[sid]
    sum_in = in_citations[sid]
    net = sum_out - sum_in

    # Top-3 cited journals
    top_out = sorted(out_partners[sid], reverse=True)[:3]
    top_out_strs = []
    for cnt, jid in top_out:
        jname = meta.get(jid, {}).get("name", jid.split("/")[-1])
        top_out_strs.append(f"{jname} ({cnt})")

    # Top-3 citing journals
    top_in = sorted(in_partners[sid], reverse=True)[:3]
    top_in_strs = []
    for cnt, jid in top_in:
        jname = meta.get(jid, {}).get("name", jid.split("/")[-1])
        top_in_strs.append(f"{jname} ({cnt})")

    input_text = (
        f"Journal: {name} (ISSN-L: {issn_l}). "
        f"Works published 2015-2022 in network: {works_count}. "
        f"Total citations given to other network journals: {sum_out}. "
        f"Total citations received from other network journals: {sum_in}. "
        f"Net flow (given minus received): {net}. "
        f"Top cited journals: {'; '.join(top_out_strs) if top_out_strs else 'none'}. "
        f"Top citing journals: {'; '.join(top_in_strs) if top_in_strs else 'none'}."
    )

    examples.append({
        "input": input_text,
        "output": str(label),
        "metadata_source_id": sid,
        "metadata_issn_l": issn_l,
        "metadata_works_count": works_count,
        "metadata_cited_by_count": cited_by_count,
        "metadata_sum_out_citations": sum_out,
        "metadata_sum_in_citations": sum_in,
        "metadata_net_flow": net,
        "metadata_suppression_label": label,
    })

data_out = {
    "metadata": {
        "source": "OpenAlex API",
        "label_source": "Clarivate JCR suppressed title lists 2018-2022",
        "year_window": "2015-2022",
        "task": "Binary classification: predict JCR citation-manipulation suppression from journal citation network features",
        "n_journals": len(all_journals),
        "n_suppressed": int(sum(gt.values())),
        "graph_edges": len(pairs),
    },
    "datasets": [
        {
            "dataset": "openalex_journal_citation_network_2015_2022",
            "examples": examples,
        }
    ],
}

(WS / "data_out.json").write_text(json.dumps(data_out))
print(f"Written data_out.json: {len(examples)} journal examples ({sum(gt.values())} suppressed)")

# mini: first 3 examples
mini = dict(data_out)
mini["datasets"] = [{"dataset": data_out["datasets"][0]["dataset"], "examples": examples[:3]}]
(WS / "mini_data_out.json").write_text(json.dumps(mini))
print(f"Written mini_data_out.json: 3 examples")

# Sync to temp/datasets/
import shutil
td = WS / "temp" / "datasets"
td.mkdir(parents=True, exist_ok=True)
for fname in ["data_out.json", "mini_data_out.json"]:
    shutil.copy(WS / fname, td / fname)
print("Synced to temp/datasets/")

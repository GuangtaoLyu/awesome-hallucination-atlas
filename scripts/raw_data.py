# -*- coding: utf-8 -*-
"""
Compatibility shim.

The canonical paper list now lives in ``data/seed.json`` (a JSON array of
[title, authors, url, year] records). This module keeps the historical
``from raw_data import RAW`` interface working for every other script
(generate.py, enrich_links.py, fetch_abstracts.py, collect_2026.py,
collect_candidates.py, merge_candidates.py) while moving the data OUT of
Python source code.

To add/merge papers, edit ``data/seed.json`` directly, or run
``merge_candidates.py`` which rewrites that file. Do NOT hand-edit RAW here.
"""
import json
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(_HERE)
_SEED = os.path.join(ROOT, "data", "seed.json")


def _load_seed(path=_SEED):
    if not os.path.exists(path):
        return []
    out = []
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    for it in data:
        if isinstance(it, (list, tuple)) and len(it) >= 4:
            out.append((str(it[0]), str(it[1]), str(it[2]), int(it[3])))
    return out


RAW = _load_seed()

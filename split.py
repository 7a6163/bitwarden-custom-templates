#!/usr/bin/env python3
"""Derive per-type Bitwarden import files in templates/ from templates.json.

templates.json is the source of truth. Re-run after editing it.
Each output is a self-contained Bitwarden export (folder + one item), so you can
import just one new type without duplicating everything in your vault.
"""
import json
import re
from pathlib import Path

src = json.load(open("templates.json"))
out = Path("templates")
out.mkdir(exist_ok=True)

for f in out.glob("*.json"):  # drop stale files for removed templates
    f.unlink()

for item in src["items"]:
    slug = re.sub(r"[^a-z0-9]+", "-", item["name"].lower()).strip("-")
    bundle = {"encrypted": False, "folders": src["folders"], "items": [item]}
    path = out / f"{slug}.json"
    with open(path, "w") as fh:
        json.dump(bundle, fh, indent=2)
        fh.write("\n")

print(f"wrote {len(src['items'])} files to {out}/")
assert len(list(out.glob("*.json"))) == len(src["items"]), "file count mismatch"

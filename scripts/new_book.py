#!/usr/bin/env python3
"""Scaffold a new Princess Puppy Adventures book module."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def die(msg: str):
    raise SystemExit(msg)

if len(sys.argv) < 3:
    die('usage: python scripts/new_book.py <slug> "<title>" ["subtitle"]')

slug, title = sys.argv[1], sys.argv[2]
subtitle = sys.argv[3] if len(sys.argv) > 3 else ""
if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
    die("slug must be lowercase kebab-case")

book_dir = ROOT / "books" / slug
if book_dir.exists():
    die(f"{book_dir} already exists")

index_path = ROOT / "books" / "index.json"
index = json.loads(index_path.read_text(encoding="utf-8"))
series_number = max([b.get("series_number", 0) for b in index.get("books", [])] or [0]) + 1

manifest = {
    "schema_version": 1,
    "slug": slug,
    "series_slug": "princess-puppy-adventures",
    "series_number": series_number,
    "title": title,
    "subtitle": subtitle,
    "contributors": {"author": "Chelsea Nash", "illustrator": "Sven Hardy Benson"},
    "status": "concept",
    "audience": {"min_age": 4, "max_age": 8},
    "format": {
        "binding": "paperback", "trim_inches": [8.5, 11],
        "interior": "black-and-white", "paper": "white",
        "page_count": 0, "bleed": False, "cover_finish": "glossy", "spine_text": False
    },
    "kdp": {
        "isbn_strategy": "undecided", "displayed_publisher": "undecided",
        "low_content": False, "working_us_price": None, "physical_proof_required": True
    },
    "canonical_paths": {
        "scenes": "content/scene-plan.json",
        "page_map": "production/page-map.json",
        "tracker": "tracker/TASKS.md",
        "metadata": "metadata/KDP.md",
        "qa": "qa/CHECKLIST.md"
    }
}

for rel in ("content","assets","production","metadata","qa","tracker","release"):
    (book_dir / rel).mkdir(parents=True, exist_ok=True)

(book_dir / "book.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
(book_dir / "README.md").write_text(f"# {title}\n\n{subtitle}\n\nStatus: concept.\n", encoding="utf-8")
(book_dir / "content" / "scene-plan.json").write_text(json.dumps({"schema_version":1,"book_slug":slug,"status":"draft","scenes":[]}, indent=2) + "\n", encoding="utf-8")
(book_dir / "production" / "page-map.json").write_text(json.dumps({"schema_version":1,"book_slug":slug,"page_count":0,"pages":[]}, indent=2) + "\n", encoding="utf-8")
for path, heading in [
    ("tracker/TASKS.md", "# Task Ledger\n"),
    ("metadata/KDP.md", "# KDP Metadata\n"),
    ("qa/CHECKLIST.md", "# Quality Gate\n"),
    ("assets/README.md", "# Assets\n"),
    ("release/README.md", "# Release\n"),
]:
    (book_dir / path).write_text(heading, encoding="utf-8")

index["books"].append({
    "slug":slug, "series_number":series_number, "title":title,
    "subtitle":subtitle, "status":"concept", "manifest":f"books/{slug}/book.json"
})
index_path.write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")
print(f"scaffolded {slug}; review manifests before committing")

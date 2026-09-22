#!/usr/bin/env python3
"""Validate LPPA monorepo invariants with only the Python standard library."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        ERRORS.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
        return None


def require(condition: bool, message: str):
    if not condition:
        ERRORS.append(message)


index = load_json(ROOT / "books" / "index.json")
if isinstance(index, dict):
    books = index.get("books", [])
    require(isinstance(books, list) and books, "books/index.json: books must be a non-empty list")
    slugs = [b.get("slug") for b in books if isinstance(b, dict)]
    require(len(slugs) == len(set(slugs)), "books/index.json: duplicate book slug")
    for entry in books:
        if not isinstance(entry, dict):
            ERRORS.append("books/index.json: every entry must be an object")
            continue
        slug = entry.get("slug")
        manifest_rel = entry.get("manifest")
        require(bool(slug), "books/index.json: each book needs slug")
        require(bool(manifest_rel), f"{slug}: registry entry needs manifest")
        if not manifest_rel:
            continue
        manifest_path = ROOT / manifest_rel
        require(manifest_path.exists(), f"{slug}: missing manifest {manifest_rel}")
        if not manifest_path.exists():
            continue
        book = load_json(manifest_path)
        if not isinstance(book, dict):
            continue
        require(book.get("slug") == slug, f"{slug}: manifest slug mismatch")
        for key in ("title", "contributors", "format", "kdp", "canonical_paths"):
            require(key in book, f"{slug}: missing {key} in book.json")
        contributors = book.get("contributors", {})
        require(bool(contributors.get("author")), f"{slug}: missing author")
        require(bool(contributors.get("illustrator")), f"{slug}: missing illustrator")
        fmt = book.get("format", {})
        pages = fmt.get("page_count")
        require(isinstance(pages, int) and pages >= 0, f"{slug}: invalid page_count")
        if isinstance(pages, int) and pages and pages < 79:
            require(fmt.get("spine_text") is False, f"{slug}: spine_text must be false below 79 pages")
        for label, rel in book.get("canonical_paths", {}).items():
            p = manifest_path.parent / rel
            require(p.exists(), f"{slug}: canonical {label} path missing: {p.relative_to(ROOT)}")

        scene_path = manifest_path.parent / book.get("canonical_paths", {}).get("scenes", "")
        page_path = manifest_path.parent / book.get("canonical_paths", {}).get("page_map", "")
        assets_rel = book.get("canonical_paths", {}).get("assets")
        assets_path = manifest_path.parent / assets_rel if assets_rel else None
        scenes = load_json(scene_path) if scene_path.is_file() else None
        page_map = load_json(page_path) if page_path.is_file() else None
        assets = load_json(assets_path) if assets_path and assets_path.is_file() else None

        if isinstance(page_map, dict) and isinstance(pages, int) and pages:
            mapped = page_map.get("pages", [])
            nums = [p.get("page") for p in mapped if isinstance(p, dict)]
            require(len(mapped) == pages, f"{slug}: page map has {len(mapped)} entries, expected {pages}")
            require(nums == list(range(1, pages + 1)), f"{slug}: page map must cover pages 1..{pages} exactly")

        # Asset-ingestion invariants are generic across books. A manifest may truthfully
        # record a missing legacy binary, but it may not claim an imported binary without
        # a repository path that actually exists. Scene affinities must also point to real
        # scene numbers so asset mapping cannot silently drift from the scene plan.
        if isinstance(assets, dict):
            candidates = assets.get("candidates", [])
            require(isinstance(candidates, list), f"{slug}: assets candidates must be a list")
            candidate_ids = [c.get("id") for c in candidates if isinstance(c, dict)]
            require(len(candidate_ids) == len(set(candidate_ids)), f"{slug}: duplicate candidate asset id")
            scene_count = len(scenes.get("scenes", [])) if isinstance(scenes, dict) else 0
            for candidate in candidates:
                if not isinstance(candidate, dict):
                    ERRORS.append(f"{slug}: every candidate asset must be an object")
                    continue
                asset_id = candidate.get("id") or "<missing-id>"
                require(bool(candidate.get("id")), f"{slug}: candidate asset missing id")
                require(bool(candidate.get("original_filename")), f"{slug}/{asset_id}: missing original_filename")
                state = candidate.get("binary_state")
                repo_rel = candidate.get("repository_path")
                require(state in {"missing", "imported"}, f"{slug}/{asset_id}: binary_state must be missing or imported")
                if state == "missing":
                    require(repo_rel is None, f"{slug}/{asset_id}: missing binary must not claim repository_path")
                elif state == "imported":
                    require(isinstance(repo_rel, str) and bool(repo_rel), f"{slug}/{asset_id}: imported binary needs repository_path")
                    if isinstance(repo_rel, str) and repo_rel:
                        repo_asset = manifest_path.parent / repo_rel
                        require(repo_asset.is_file(), f"{slug}/{asset_id}: imported binary not found at {repo_asset.relative_to(ROOT)}")
                affinities = candidate.get("scene_affinity", [])
                require(isinstance(affinities, list), f"{slug}/{asset_id}: scene_affinity must be a list")
                if isinstance(affinities, list) and scene_count:
                    for scene_number in affinities:
                        require(
                            isinstance(scene_number, int) and 1 <= scene_number <= scene_count,
                            f"{slug}/{asset_id}: invalid scene_affinity {scene_number!r}; expected 1..{scene_count}",
                        )

        if slug == "leia-magical-pawprint" and isinstance(scenes, dict):
            scene_list = scenes.get("scenes", [])
            require(len(scene_list) == 19, "Book 1: expected exactly 19 coloring scenes")
            scene_pages = [s.get("page") for s in scene_list if isinstance(s, dict)]
            require(scene_pages == list(range(5, 42, 2)), "Book 1: scenes must occupy odd pages 5–41")
            require(book.get("title") == "Leia the Princess Puppy", "Book 1: protected title changed")
            require(book.get("subtitle") == "And the Magical Pawprint", "Book 1: protected subtitle changed")
            require(contributors.get("author") == "Chelsea Nash", "Book 1: protected author changed")
            require(contributors.get("illustrator") == "Sven Hardy Benson", "Book 1: protected illustrator changed")
            require(pages == 42, "Book 1: protected page count changed")

series = load_json(ROOT / "series" / "series.json")
if isinstance(series, dict) and isinstance(index, dict):
    active = series.get("active_book")
    indexed = {b.get("slug") for b in index.get("books", []) if isinstance(b, dict)}
    require(active in indexed, "series/series.json: active_book must exist in books/index.json")

if ERRORS:
    print("LPPA validation FAILED:")
    for err in ERRORS:
        print(f" - {err}")
    sys.exit(1)

print("LPPA validation passed.")

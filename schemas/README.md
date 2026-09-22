# Manifest Schemas

These JSON Schemas document the stable interfaces used by LPPA tooling:

- `book.schema.json` — per-book identity, format, KDP strategy, canonical paths
- `scene-plan.schema.json` — coloring/story scene contract
- `page-map.schema.json` — exact interior sequence contract

`scripts/validate_repo.py` intentionally uses only Python's standard library so repository validation has no package-install dependency. The schemas remain the documented interface for editors, agents, and future tooling.

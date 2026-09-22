# Contributing

This is a commercial publishing workspace. Changes should make the product more reproducible, more polished, or closer to a validated release.

## Workflow

1. Read `AGENTS.md`.
2. Identify the active book from `books/index.json`.
3. Work in the relevant module; avoid drive-by changes elsewhere.
4. Keep machine-readable and human-readable versions synchronized.
5. Run `python scripts/validate_repo.py`.
6. Open a focused PR describing the production delta, validation performed, approval gates affected, and next action.

A PR may improve content, art planning, production, metadata, QA, tooling, or the public site, but it should have one coherent purpose.

Never use a PR to bypass an explicit human approval gate.

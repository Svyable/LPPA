# Project Structure

LPPA is a self-contained publishing monorepo designed to scale to multiple Princess Puppy Adventures books without turning Book 1 into a special-case codebase.

Canonical architecture and rationale: [ops/ARCHITECTURE.md](./ops/ARCHITECTURE.md).

## Rules

- Reusable series/character truth belongs under `series/`.
- Each book is an independent module under `books/<slug>/`.
- `books/index.json` is the registry used by repository tooling.
- Book-specific machine-readable invariants live in `book.json`, scene-plan JSON, and page-map JSON.
- Human-readable Markdown sits beside machine-readable data for review.
- Public marketing lives only under `docs/`.
- Derived release exports do not replace their source artifacts.
- Future books should be scaffolded with `scripts/new_book.py`, then deliberately filled in.

## Book 1

The canonical Book 1 module is `books/leia-magical-pawprint/`.

Older root-level `KDP-LAUNCH-TRACKER.md`, `production/`, `metadata/`, `qa/`, `tracker/`, and `assets/` material predates the modular layout. Treat it as migration/compatibility documentation. New Book 1 edits belong in the canonical book module.

# AGENTS.md — Princess Puppy Adventures

This repository is the **canonical working home** for Princess Puppy Adventures publishing work. Future Leia work belongs here unless a human explicitly says otherwise.

## Start here every run

1. Read `README.md`, `PROJECT-STRUCTURE.md`, and this file.
2. Read `books/index.json`.
3. For the active book, read its `book.json`, scoped `AGENTS.md`, scene plan, page map, tracker, metadata, and QA gate before editing.
4. Inspect open pull requests before starting overlapping work.
5. Choose the highest-value unblocked step on the active book's critical path.
6. Make concrete, reversible progress; update the canonical artifact and status in the same change.

## Source-of-truth hierarchy

- Series identity and reusable standards: `series/` plus root `BRAND-GUIDE.md`.
- Book registry: `books/index.json`.
- Book-specific immutable identity / format decisions: `books/<slug>/book.json`.
- Book-specific content and production truth: inside that book directory.
- Public marketing site: `docs/`.
- Generated exports are outputs, never the authoritative source.

Do not create a second tracker, second page map, or parallel manuscript outside the book module.

## Architecture rules

Treat each book as an independent module with its own content, assets, production, metadata, QA, tracker, and release state. Shared character/brand material belongs under `series/`, never copied into every book.

Tooling under `scripts/` must depend on manifests and documented interfaces, not hard-coded knowledge of Book 1. New books are added through `books/index.json` and a new book directory; existing books should not need structural edits.

Prefer machine-readable JSON for invariants and human-readable Markdown for explanation/review. When both exist, keep them synchronized in one PR.

## Book 1 protected decisions

For `leia-magical-pawprint`, do not change without explicit human approval:
- title: **Leia the Princess Puppy**
- subtitle: **And the Magical Pawprint**
- author: **Chelsea Nash**
- illustrator: **Sven Hardy Benson**
- 42 interior pages
- 8.5 × 11 inch paperback
- black-and-white interior on white paper
- KDP free ISBN strategy
- Princess Puppy Adventures series/brand
- physical proof before publication

## Art / asset discipline

Inspect existing assets before generating replacements. Preserve provenance. Use statuses such as `candidate`, `keeper`, `print`, and `released`. Never label an image print-ready merely because DPI metadata changed.

Approved reusable Leia character references belong under `series/characters/leia/`. Book-specific artwork belongs under that book's `assets/`.

Do not expose candidate art on the public site unless it has been deliberately approved for public use.

## Human approval gates

Never, without explicit human approval:
- publish a book;
- order a proof or make a purchase;
- spend money or buy an ISBN;
- create legal entities or accept contracts;
- alter ownership or creator credits;
- make irreversible external commitments.

Prepare everything needed for those actions, then surface the smallest decision required.

## Change quality

- Use focused branches/PRs for substantial changes.
- Run `python scripts/validate_repo.py` before calling repo structure valid.
- Keep public-site claims truthful to the actual release state.
- Do not silently delete historical decisions or provenance.
- When replacing an artifact, keep the replacement traceable in git history and update references.
- End automation work by updating the active book tracker/run log and stating the single best next action.

## Context-safe execution

GitHub is the durable project memory; chat context is temporary. Do not require a single long conversation to carry the project state.

- Work in bounded increments: one critical-path objective per run or PR.
- Checkpoint concrete progress to GitHub before expanding into another objective.
- Prefer targeted file reads over recursive repository dumps or repeatedly re-reading large histories.
- After several tool calls or a substantial asset audit, commit the useful state before doing more exploration.
- If the next critical-path step depends on image binaries that are not present in the repository or current working context, record the missing asset once and stop generating additional planning layers around it.
- Resume a long-running project from the canonical tracker and run log in a fresh chat when needed; do not treat conversation continuity as a project dependency.
- A context-window interruption must not invalidate completed work already committed to GitHub.

## Definition of done

A Book 1 release is not done because KDP accepts the files. It is done only after the repository records: exact 42-page interior, print-quality artwork, completed QA, final wrap cover, accurate metadata, Previewer pass, physical proof approval by Chelsea and Sven, and final publication identifiers.

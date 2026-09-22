# Project Structure

This repository is the durable working home for **Princess Puppy Adventures** and Book 1, *Leia the Princess Puppy: And the Magical Pawprint*.

## Working folders

- `assets/` — artwork inventory, naming rules, and eventually approved source/print assets.
- `production/` — exact 42-page map, assembly notes, and print manifests.
- `metadata/` — Amazon/KDP listing data and launch copy.
- `qa/` — preflight and physical-proof quality gates.
- `sources/` — authoritative production and KDP reference links.
- `docs/` — public GitHub Pages site only.
- `.github/workflows/` — repository automation and Pages deployment.

## Source-of-truth rule

The project launch tracker controls decisions, task status, page count, credits, and production sequence. Repo documents should be updated when those values change rather than creating competing plans.

## Asset discipline

1. Inspect existing work before generating replacements.
2. Preserve source files.
3. Use descriptive filenames and explicit status labels such as `candidate`, `keeper`, and `print`.
4. Never treat a low-resolution file as print-ready merely by changing DPI metadata.
5. Do not publish draft art to the marketing site unless it is intentionally approved for public use.

## Approval gates

Explicit human approval is required before publishing the book, ordering a proof, spending money, buying an ISBN, changing creator credits, or making another irreversible external commitment.

# Princess Puppy Adventures

Canonical publishing monorepo for **Princess Puppy Adventures**, beginning with **Leia the Princess Puppy: And the Magical Pawprint**.

**Author:** Chelsea Nash  
**Illustrator:** Sven Hardy Benson

## Active book

[Book 1 — Leia the Princess Puppy: And the Magical Pawprint](./books/leia-magical-pawprint/README.md)

- 42-page 8.5 × 11 inch paperback
- black-and-white interior on white paper
- 19 coloring scenes on odd/right pages 5–41
- KDP free ISBN
- working launch price $9.99
- physical proof required before publication

The current 19-scene adventure has been drafted and is **ready for review**. The next production step is approval, then mapping existing artwork to keepers/gaps and locking Leia's reusable character model.

## Monorepo map

- [AGENTS.md](./AGENTS.md) — operating instructions for humans and agents
- [books/index.json](./books/index.json) — machine-readable book registry
- [books/](./books/) — independent book modules
- [series/](./series/) — reusable series/character truth
- [BRAND-GUIDE.md](./BRAND-GUIDE.md) — series visual/story principles
- [ops/ARCHITECTURE.md](./ops/ARCHITECTURE.md) — scalable boundaries and SOLID design
- [ops/ASSET-POLICY.md](./ops/ASSET-POLICY.md) — asset/provenance rules
- [scripts/validate_repo.py](./scripts/validate_repo.py) — zero-dependency structural validation
- [scripts/new_book.py](./scripts/new_book.py) — future-book scaffolding
- [docs/](./docs/) — public pre-launch website only

## Canonicality

Book-specific work lives under `books/<slug>/`. Root-level legacy tracker/page-map folders are compatibility entry points only and should not become parallel sources of truth.

For Book 1, start with:
- [book.json](./books/leia-magical-pawprint/book.json)
- [scene plan](./books/leia-magical-pawprint/content/SCENE-PLAN.md)
- [page map](./books/leia-magical-pawprint/production/PAGE-MAP.md)
- [task ledger](./books/leia-magical-pawprint/tracker/TASKS.md)
- [KDP metadata](./books/leia-magical-pawprint/metadata/KDP.md)
- [QA gate](./books/leia-magical-pawprint/qa/CHECKLIST.md)

## Safety / approval

Do not publish, order proofs, spend money, buy ISBNs, alter creator credits, or make irreversible external commitments without explicit human approval.

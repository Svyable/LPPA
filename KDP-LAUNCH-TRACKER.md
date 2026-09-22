# Princess Puppy Adventures — KDP Launch Tracker

_Last synchronized: 2026-09-21_

## Book 1

**Leia the Princess Puppy: And the Magical Pawprint**  
Series / brand: **Princess Puppy Adventures**  
Author: **Chelsea Nash**  
Illustrator: **Sven Hardy Benson**

- 42 interior pages
- 8.5 × 11 inch paperback
- black-and-white interior on white paper
- 19 full-page coloring scenes on odd/right pages 5–41
- mostly blank reverses behind coloring pages
- KDP free ISBN for the first edition
- publisher display expected: **Independently published**
- working list price: **$9.99**
- no spine text at 42 pages
- physical proof required before publication

## Launch pulse

| Status | Count |
|---|---:|
| Complete | 6 |
| In Progress | 1 |
| Ready for Review | 3 |
| Blocked | 0 |
| Not Started | 32 |
| **Total** | **42** |

Full task ledger: [tracker/TASKS.md](./tracker/TASKS.md)  
Exact interior sequence: [production/PAGE-MAP.md](./production/PAGE-MAP.md)

## Current critical path

1. **C01 — Chelsea approves the 19-scene coloring list.**
2. **A01 — Inventory existing Leia art and map keeper candidates to those 19 scenes.** This is already in progress.
3. **A02 — Lock the definitive Leia character consistency sheet.**
4. Rebuild only keeper artwork that needs genuine print-quality work.
5. Simplify for ages approximately 4–8 and run line-weight/safe-margin checks.
6. Assemble and QA the exact 42-page interior.
7. Build the exact KDP wraparound cover.
8. Finalize metadata/pricing, upload, pass Print Previewer, order/review proof, correct, then publish.

## Existing artwork already identified

| Asset | Known size | Potential use | Status |
|---|---:|---|---|
| Leia the Princess Puppy Cover.png | 1448 × 1086 px | Cover concept | Needs production |
| Leia the Princess Puppy: Magical Pawprints.png | 1774 × 887 px | Spread / concept | Review |
| Leia’s Braver Day Adventure.png | 1208 × 1302 px | Interior concept | Review |
| image-gen-4(1).png | 1104 × 1425 px | Interior art | Needs high-res rebuild |
| image-gen-3(1).png | 1104 × 1425 px | Interior art | Needs high-res rebuild |

Additional Library candidates inspected during repo setup:
- Leia the Princess Puppy’s Magical Pawprint.png
- Princess Puppy’s Magical Pawprint.png
- Leia the Princess Puppy.png

These remain candidates until deliberately approved. See [assets/README.md](./assets/README.md).

## Ready-for-review items from the current tracker

- **A06:** title-page art
- **M05:** working reading age of 4–8
- **R01:** working US list price of $9.99

## Repository / marketing infrastructure

- [x] `Svyable/LPPA` established as durable project workspace.
- [x] Production, asset, QA, metadata, source, and brand documentation added.
- [x] Exact 42-page page map mirrored into repo.
- [x] Full 42-task production ledger mirrored into repo.
- [x] Pre-launch public website created under `docs/`.
- [x] GitHub Pages deployment workflow added.
- [ ] **Enable GitHub Pages for this repository with Build and deployment → Source = GitHub Actions.** The first deployment run reached `actions/configure-pages` and failed because GitHub reported that no Pages site is enabled for the repository.
- [ ] Re-run the Pages workflow and verify **https://svyable.github.io/LPPA/** after the setting is enabled.

The public site deliberately says **Coming soon** and does not use unapproved draft Leia artwork.

## Decision log

| Decision | Current state |
|---|---|
| Page count | 42 interior pages — final |
| Author credit | Chelsea Nash — final |
| Illustrator credit | Sven Hardy Benson — final |
| ISBN | KDP free ISBN for Book 1 — final |
| Formal paid/custom imprint | No for Book 1 — final |
| Brand treatment | Princess Puppy Adventures as series/customer-facing brand — final |
| Low-content classification | Normal coloring-book paperback; do not select low-content — final |
| Spine text | None at 42 pages — final |
| Launch price | $9.99 working price — review before publish |
| Physical proof | Required and must be approved by Chelsea and Sven |
| GitHub workspace | `Svyable/LPPA` |
| Pre-launch website | GitHub Pages static site from `docs/`; one-time Pages enablement still required |

## Quality gate

Before launch-ready status:

- [ ] Exactly 42 interior pages
- [ ] Correct trim size and page order
- [ ] All 19 coloring scenes on planned odd/right pages
- [ ] Genuine print-resolution artwork
- [ ] Safe margins, gutter, crop, and line weight
- [ ] Legible text
- [ ] Consistent Leia character model
- [ ] Title/subtitle/creator credits consistent everywhere
- [ ] Copyright and credits complete
- [ ] Correct free-ISBN workflow
- [ ] Accurate AI-generated-content disclosure based on actual final process
- [ ] Exact full-wrap cover from final KDP template
- [ ] Barcode area unobstructed
- [ ] Metadata accurately describes the finished book
- [ ] KDP Print Previewer passes
- [ ] Physical proof reviewed and approved by Chelsea and Sven

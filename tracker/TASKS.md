# Production Task Ledger

Snapshot synchronized from the existing Princess Puppy Adventures KDP Launch Tracker.

| ID | Phase | Task / deliverable | Owner | Status | Priority | Depends on |
|---|---|---|---|---|---|---|
| D01 | Decisions | Lock title: Leia the Princess Puppy | Both | Complete | Critical | — |
| D02 | Decisions | Lock subtitle: And the Magical Pawprint | Both | Complete | Critical | D01 |
| D03 | Decisions | Lock credits: Author Chelsea Nash / Illustrator Sven Hardy Benson | Both | Complete | Critical | — |
| D04 | Decisions | Lock 42-page interior count | Both | Complete | Critical | — |
| D05 | Decisions | Use KDP free ISBN for Book 1 | Both | Complete | High | — |
| D06 | Decisions | Use Princess Puppy Adventures as series/brand, not paid imprint | Both | Complete | High | D05 |
| C01 | Content | Approve 19-scene coloring list | Chelsea | Not Started | Critical | D04 |
| C02 | Content | Write final “Meet Leia” intro copy | Chelsea | Not Started | High | D01, D02 |
| C03 | Content | Write copyright + credits page | Chelsea | Not Started | High | D03, D05 |
| C04 | Content | Write closing / next-adventure copy | Chelsea | Not Started | Medium | D06 |
| A01 | Artwork | Inventory all existing Leia art and choose keeper scenes | Sven | In Progress | Critical | C01 |
| A02 | Artwork | Create a Leia character consistency sheet | Sven | Not Started | Critical | A01 |
| A03 | Artwork | Rebuild / redraw coloring art at print-ready resolution | Sven | Not Started | Critical | A02 |
| A04 | Artwork | Simplify line work for ages 4–8 | Sven | Not Started | High | A03 |
| A05 | Artwork | Check minimum line weight and safe margins | Sven | Not Started | High | A03 |
| A06 | Artwork | Finalize title page art | Sven | Ready for Review | High | D01, D02 |
| A07 | Artwork | Finalize “This book belongs to” page | Sven | Not Started | Medium | A02 |
| P01 | Production | Assemble 42-page interior PDF | Sven | Not Started | Critical | C02, C03, C04, A03, A06, A07 |
| P02 | Production | Keep coloring designs on right-hand/odd pages | Sven | Not Started | High | P01 |
| P03 | Production | Use mostly blank reverses behind coloring pages | Sven | Not Started | High | P01 |
| P04 | Production | Run 300-DPI / image-resolution audit | Sven | Not Started | Critical | P01 |
| P05 | Production | Run margin / crop / font audit | Sven | Not Started | Critical | P01 |
| K01 | Cover | Generate exact KDP 42-page cover template after interior locks | Sven | Not Started | Critical | P01 |
| K02 | Cover | Build full wraparound cover PDF | Sven | Not Started | Critical | K01 |
| K03 | Cover | Write and place back-cover copy | Chelsea | Not Started | High | K02 |
| M01 | Metadata | Finalize Amazon description | Chelsea | Not Started | High | C01 |
| M02 | Metadata | Finalize 7 keyword phrases | Chelsea | Not Started | Medium | M01 |
| M03 | Metadata | Choose up to 3 accurate KDP categories | Both | Not Started | Medium | M01 |
| M04 | Metadata | Set series: Princess Puppy Adventures | Both | Not Started | High | D06 |
| M05 | Metadata | Set reading age / audience | Chelsea | Ready for Review | Medium | C01 |
| M06 | Metadata | Record AI-generated image disclosure accurately | Both | Not Started | Critical | A03, K02 |
| R01 | Pricing | Confirm launch list price (working: $9.99 US) | Both | Ready for Review | High | P01 |
| U01 | KDP Upload | Create paperback title in KDP | Both | Not Started | Critical | M01, M02, M03, M04, M05 |
| U02 | KDP Upload | Assign free KDP ISBN | Both | Not Started | Critical | U01 |
| U03 | KDP Upload | Upload interior PDF and cover PDF | Both | Not Started | Critical | P05, K03, U02 |
| U04 | KDP Upload | Pass KDP Print Previewer | Both | Not Started | Critical | U03 |
| Q01 | Proof | Order physical proof copy | Both | Not Started | Critical | U04 |
| Q02 | Proof | Inspect physical proof: line quality, gutter, show-through, cover, barcode | Both | Not Started | Critical | Q01 |
| Q03 | Proof | Apply final proof corrections if needed | Sven | Not Started | High | Q02 |
| L01 | Launch | Publish paperback | Both | Not Started | Critical | Q02 or Q03 |
| L02 | Launch | Verify live Amazon detail page | Both | Not Started | High | L01 |
| L03 | Launch | Save ASIN/ISBN/live URL into tracker | Both | Not Started | Medium | L02 |

## Current pulse

- Total tasks: 42
- Complete: 6
- In Progress: 1
- Ready for Review: 3
- Blocked: 0
- Not Started: 32

## Immediate critical path

C01 → A01 → A02 → A03 → A04/A05 → P01 → P04/P05 → K01/K02 → upload/preview → proof → publish.

Publishing and proof ordering remain explicit human approval gates.

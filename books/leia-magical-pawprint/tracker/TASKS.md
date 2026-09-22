# Book 1 Task Ledger

This is the canonical Book 1 work ledger. Status values: `Not Started`, `In Progress`, `Ready for Review`, `Blocked`, `Complete`.

| ID | Phase | Task | Owner | Status | Priority | Depends on |
|---|---|---|---|---|---|---|
| D01 | Decisions | Lock title | Both | Complete | Critical | — |
| D02 | Decisions | Lock subtitle | Both | Complete | Critical | D01 |
| D03 | Decisions | Lock Chelsea Nash author / Sven Hardy Benson illustrator credits | Both | Complete | Critical | — |
| D04 | Decisions | Lock 42-page interior count | Both | Complete | Critical | — |
| D05 | Decisions | Use KDP free ISBN | Both | Complete | High | — |
| D06 | Decisions | Use Princess Puppy Adventures as series/brand | Both | Complete | High | D05 |
| C01 | Content | Approve 19-scene coloring list | Chelsea | Ready for Review | Critical | D04 |
| C02 | Content | Write final Meet Leia intro | Chelsea | Ready for Review | High | D01,D02 |
| C03 | Content | Write copyright + credits page | Chelsea | Ready for Review | High | D03,D05 |
| C04 | Content | Write closing / next-adventure copy | Chelsea | Ready for Review | Medium | D06 |
| A01 | Artwork | Inventory existing Leia art and map keepers/gaps to scenes | Sven | In Progress | Critical | C01 |
| A02 | Artwork | Create definitive Leia character consistency sheet | Sven | Not Started | Critical | A01 |
| A03 | Artwork | Rebuild/redraw keeper art at genuine print quality | Sven | Not Started | Critical | A02 |
| A04 | Artwork | Simplify line work for ages 4–8 | Sven | Not Started | High | A03 |
| A05 | Artwork | Check line weight and safe margins | Sven | Not Started | High | A03 |
| A06 | Artwork | Finalize title-page art | Sven | Ready for Review | High | D01,D02 |
| A07 | Artwork | Finalize This Book Belongs To page | Sven | Not Started | Medium | A02 |
| P01 | Production | Assemble exact 42-page interior PDF | Sven | Not Started | Critical | C02,C03,C04,A03,A06,A07 |
| P02 | Production | Verify coloring designs on odd/right pages | Sven | Not Started | High | P01 |
| P03 | Production | Verify mostly blank reverses | Sven | Not Started | High | P01 |
| P04 | Production | Run genuine-resolution audit | Sven | Not Started | Critical | P01 |
| P05 | Production | Run margin/crop/font audit | Sven | Not Started | Critical | P01 |
| K01 | Cover | Generate exact KDP 42-page cover template | Sven | Not Started | Critical | P01 |
| K02 | Cover | Build full wrap cover PDF | Sven | Not Started | Critical | K01 |
| K03 | Cover | Write/place back-cover copy | Chelsea | Not Started | High | K02 |
| M01 | Metadata | Finalize Amazon description | Chelsea | Not Started | High | C01 |
| M02 | Metadata | Finalize seven keyword phrases | Chelsea | Not Started | Medium | M01 |
| M03 | Metadata | Choose accurate KDP categories | Both | Not Started | Medium | M01 |
| M04 | Metadata | Set series | Both | Not Started | High | D06 |
| M05 | Metadata | Confirm reading age/audience | Chelsea | Ready for Review | Medium | C01 |
| M06 | Metadata | Record AI-generated-content disclosure accurately | Both | Not Started | Critical | A03,K02 |
| R01 | Pricing | Confirm $9.99 working US price against final KDP economics | Both | Ready for Review | High | P01 |
| U01 | KDP | Create paperback title in KDP | Both | Not Started | Critical | M01,M02,M03,M04,M05 |
| U02 | KDP | Assign free KDP ISBN | Both | Not Started | Critical | U01 |
| U03 | KDP | Upload interior and cover PDFs | Both | Not Started | Critical | P05,K03,U02 |
| U04 | KDP | Pass Print Previewer | Both | Not Started | Critical | U03 |
| Q01 | Proof | Order physical proof | Both | Not Started | Critical | U04 |
| Q02 | Proof | Inspect physical proof | Both | Not Started | Critical | Q01 |
| Q03 | Proof | Apply proof corrections if required | Sven | Not Started | High | Q02 |
| L01 | Launch | Publish paperback | Both | Not Started | Critical | Q02 or Q03 |
| L02 | Launch | Verify live Amazon detail page | Both | Not Started | High | L01 |
| L03 | Launch | Record ASIN/ISBN/live URL | Both | Not Started | Medium | L02 |

## Current critical path

C01 → A01 → A02 → A03 → A04/A05 → P01 → P04/P05 → K01/K02 → metadata/upload/Previewer → proof → publish.

C01 remains **Ready for Review**. C02–C04 now have complete draft copy in `content/FRONT-BACK-MATTER.md` and are **Ready for Review**, not complete; Chelsea-owned copy requires approval before final production.

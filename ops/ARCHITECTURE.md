# Repository Architecture

LPPA is a publishing monorepo: one shared series layer, many independent book modules, one public site, and repository-wide tooling.

## Boundaries

```
series/                       reusable brand + characters
books/
  index.json                  book registry
  <book-slug>/
    book.json                 immutable-ish identity + format decisions
    AGENTS.md                 scoped agent rules
    content/                  story/scene/front/back matter sources
    assets/                   book-specific art and provenance
    production/               page maps, assembly inputs, cover specs
    metadata/                 KDP/store listing sources
    qa/                       preflight/proof evidence
    tracker/                  book work ledger + run history
    release/                  frozen publication notes/identifiers
scripts/                      repo-wide tooling, no Book-1 hardcoding
schemas/                      documented machine-readable interfaces
templates/                    new-book scaffolding
docs/                         public website only
```

## SOLID applied to publishing

- **Single responsibility:** series rules, book content, production, metadata, QA, and public marketing live in separate modules.
- **Open/closed:** adding Book 2 means adding a new book module and registry entry, not rewriting Book 1.
- **Liskov-style substitutability:** every book manifest exposes the same required fields and canonical paths so tooling can process any book.
- **Interface segregation:** scripts consume small JSON manifests instead of scraping prose.
- **Dependency inversion:** validators/build tooling depend on the manifest contract; book modules do not depend on implementation details in scripts.

## Source vs outputs

Source files and manifests are canonical. PDFs, print exports, compressed previews, and KDP upload files are derived artifacts. Never edit a derived PDF as the only source of a production change.

## Binary assets

Keep canonical approved assets in-repo whenever technically practical. For large layered sources that exceed normal GitHub file limits, use Git LFS rather than replacing the asset with an external-only link. Every binary asset must have provenance/status documented beside it.

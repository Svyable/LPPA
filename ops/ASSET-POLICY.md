# Asset Policy

The repository is intended to be self-contained enough to reproduce a release.

## Storage classes

1. **Series reference** — reusable character model, marks, motifs: `series/characters/` and future `series/assets/`.
2. **Book candidate** — exploratory book-specific art: `books/<slug>/assets/candidates/`.
3. **Keeper source** — approved source used to make print art: `books/<slug>/assets/keepers/`.
4. **Print asset** — flattened final art used by production: `books/<slug>/assets/print/`.
5. **Release artifact** — final interior/cover PDFs and release manifest: `books/<slug>/release/` when intentionally frozen.

## Rules

- Do not overwrite provenance; supersede with a new version.
- Do not declare a low-resolution candidate print-ready by editing DPI metadata.
- Record generation/editing provenance accurately enough to support KDP AI disclosure.
- Public website use is a separate approval from print-keeper status.
- Prefer lossless source formats for line art.
- Do not commit secrets, private customer data, or unrelated personal files.

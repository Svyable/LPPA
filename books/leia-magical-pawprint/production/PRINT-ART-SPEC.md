# Book 1 Print-Art Acceptance Spec

Purpose: define the objective handoff from an approved Leia character model / keeper composition into production-ready interior line art. This does **not** promote any current candidate artwork and does not bypass A01 or A02.

## Fixed production target

- Paperback trim: **8.5 × 11 in**, portrait.
- Interior: **black ink on white paper**.
- Interior page count: **42**.
- Bleed: **none** under the current Book 1 manifest.
- Coloring scenes: odd/right pages 5–41.
- Mostly blank reverses: even/left pages 6–40.

At 300 pixels per inch, trim-size raster art is **2550 × 3300 px**. This is a minimum production baseline, not permission to enlarge a smaller source or change DPI metadata and call it print-ready.

## Current KDP manufacturing constraints

Checked against Amazon KDP's official Paperback Submission Guidelines on **2026-09-22**:

- manuscript images must be at least **300 DPI**;
- KDP recommends no more than **600 DPI** for images to avoid unnecessary processing/file-size problems;
- for a 24–150 page no-bleed paperback, minimum inside/gutter margin is **0.375 in** and minimum top, bottom, and outside margins are **0.25 in**;
- line elements should be at least **0.75 pt / 0.01 in / 0.3 mm** thick;
- fonts must be embedded;
- transparent objects/layers should be flattened before submission;
- the submitted PDF should not contain crop marks, trim marks, comments, annotations, placeholder text, or similar production debris.

Authoritative source: https://kdp.amazon.com/en_US/help/topic/G201857950

KDP margin reference: https://kdp.amazon.com/en_US/help/topic/GVBQ3CMEQW3W2VL6

These are platform constraints, not creative targets. Recheck the official KDP documentation before final upload in case Amazon changes requirements.

## LPPA working safe zone

KDP's minimum margins are failure boundaries, not ideal coloring-book composition boundaries. For Book 1, use this more conservative working zone for essential character/detail content:

- inside/gutter: **0.50 in preferred**, never below KDP's current 0.375 in minimum;
- top: **0.375 in preferred**;
- bottom: **0.375 in preferred**;
- outside: **0.375 in preferred**.

At 300 PPI, the preferred inset is 150 px at the gutter and 113 px on the other three edges (rounded up from 112.5 px). Decorative nonessential marks may approach the minimum margin only when deliberately reviewed; no artwork should imply bleed while the manifest says `bleed: false`.

## Line-art acceptance criteria

A scene may move from rebuilt source to `print` only when all of the following are true:

1. **Real resolution:** the source contains genuine detail at the intended print size; no metadata-only DPI promotion and no low-resolution candidate enlarged as the final master.
2. **Leia consistency:** Leia matches the approved series character model for face/muzzle, ears, markings, proportions, tail, crown/accessories, and expression vocabulary.
3. **Age fit:** the page reads clearly for approximately ages 4–8: large colorable regions, limited micro-detail, clear focal hierarchy, and generous white space.
4. **Line integrity:** important outlines are continuous and comfortably meet or exceed the current KDP 0.75 pt minimum at final size. Hairline artifacts, accidental doubled edges, muddy joins, and broken contours are repaired.
5. **No accidental grayscale:** coloring regions remain open and white unless a gray/black element is an intentional part of the approved design.
6. **Safe placement:** all essential content stays inside the LPPA preferred safe zone; nothing important crosses KDP's current minimum margins.
7. **No unintended bleed:** artwork ends cleanly within the trim page because Book 1 is currently no-bleed.
8. **Clean background:** no generation artifacts, watermarks, UI remnants, crop marks, signatures, stray pixels, or placeholder text.
9. **Scene fidelity:** the image satisfies the approved scene beat and composition rather than merely depicting Leia generically.
10. **Provenance:** the source/rebuild method, relevant input/reference asset IDs, editor/generator where applicable, and approval state are recorded so final KDP AI disclosure can be accurate.

## Source and export policy

- Preserve the highest-quality editable/source artifact available; do not make the flattened print file the only master.
- Prefer lossless formats for line-art masters.
- Flatten only the release/export copy when required for KDP/PDF assembly.
- Do not destructively overwrite a candidate or keeper source when rebuilding it; create a traceable successor.
- Record dimensions from the actual binary after import/export rather than trusting filenames or DPI metadata.

## Per-scene handoff record

Before a scene is treated as print-ready, record at minimum:

- scene ID and page;
- approved character-model version;
- source/keeper asset ID;
- rebuild/master asset path;
- print-export path;
- actual pixel dimensions;
- effective resolution at 8.5 × 11 placement;
- minimum observed/verified line weight where practical;
- safe-zone result;
- grayscale/artifact review result;
- provenance / AI-generation-editing note;
- reviewer and approval state.

A future machine-readable production-art manifest should carry these fields once the first real keeper enters A03. Do not create empty per-scene records merely to simulate progress.

## Gate relationship

This spec makes A03–A05 testable, but does not advance their task status. The order remains A01 → A02 → A03 → A04/A05. The missing legacy binaries must still be recovered or consciously abandoned before the current A01 evidence gap can be closed.
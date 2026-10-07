# Book 1 Candidate Art Audit

Status: **In progress**. This is the canonical A01 human-review document for mapping known legacy Leia artwork to the 19-scene plan. The machine-readable inventory is [`candidate-assets.json`](./candidate-assets.json). Keep the two synchronized whenever a candidate is imported, classified, or mapped. Four original PNGs were recovered and hash-verified on 2026-10-07; **none is yet approved as a keeper, print asset, or public artwork**. The remaining legacy references still require binary verification.

## Known candidates

| Candidate | Known size | Likely role / scene affinity | Current classification | Required review |
|---|---:|---|---|---|
| `Leia the Princess Puppy Cover.png` | 1448 × 1086 px | Cover concept / character reference; not directly suitable as the final KDP wrap | candidate | Import binary; inspect Leia face, ears, markings, crown/accessories and whether any character traits should inform the reusable model sheet. |
| `Leia the Princess Puppy: Magical Pawprints.png` | 1774 × 887 px | Broad magical-pawprint concept; potentially useful as narrative/scene reference | candidate | Import binary; identify which of scenes 1–19 it actually depicts before assigning a scene. |
| `Leia’s Braver Day Adventure.png` | 1208 × 1302 px | Courage/adventure concept; possible affinity with scene 5 or 10 | candidate | Import binary; compare composition against `Stepping-Stone Courage` and `A Brave Little Climb`; audit Leia consistency. |
| `image-gen-4(1).png` | 1104 × 1425 px | Interior-art candidate | candidate — known dimensions below target print raster | Import binary; identify scene/content; inspect line quality and composition. If retained, rebuild/redraw rather than changing DPI metadata. |
| `image-gen-3(1).png` | 1104 × 1425 px | Interior-art candidate | candidate — known dimensions below target print raster | Import binary; identify scene/content; inspect line quality and composition. If retained, rebuild/redraw rather than changing DPI metadata. |
| `Leia the Princess Puppy’s Magical Pawprint.png` | 1103 × 1426 px | Title/character/interior candidate | candidate | Import binary; record dimensions and visual content; map only after inspection. |
| `Princess Puppy’s Magical Pawprint.png` | 1208 × 1302 px | Title/character/interior candidate | candidate | Import binary; record dimensions and visual content; map only after inspection. |
| `Leia the Princess Puppy.png` | 1103 × 1426 px | Character/title candidate | candidate — imported | Detailed visual consistency and coloring suitability review pending. |
| `Leia’s Magical Pawprint Adventure.png` | 1103 × 1426 px | Four-panel black-and-white narrative / multi-scene storyboard reference | candidate — imported | Compare Leia shape and story beats; do not assume one page maps to one coloring scene. |

## Verified binary import (2026-10-07)

Four original PNGs are now in `assets/candidates/`, committed byte-for-byte from recovered Google Drive mirror files. Exact Git blob checksums matched originals in the project Library. Their manifest entries include source Drive IDs and SHA-256 hashes. Review-status remains **candidate**; cover concepts contain full color and character renderings with materially different facial/breed cues from some line-art sources, so **do not lock a character model from these alone**. The four-panel story reference is not 4 independent print pages. One previously encountered `image-gen-3(1).png` in the Library was an unrelated technical graphic; its same-name identity is unresolved, so the pre-existing legacy candidate remains missing rather than being silently replaced.

- `Leia the Princess Puppy.png` — 1103 × 1426 px, SHA-256 `5d2eddee4d5ce0b1e02952062bb9b4d0db8a2c278a4f3d01f412f58b2440c40a`; Black-and-white puppy title/character candidate with crown, castle, and narrative caption; not approved as definitive Leia.
- `Leia the Princess Puppy’s Magical Pawprint.png` — 1103 × 1426 px, SHA-256 `014029e417de3217670c4e1dbf4f0128ed8ad76e3d0bf271a0b9ab3f56793da8`; Color/line-art split composition with title lettering; use as cover concept only after checking Leia's appearance and title typography.
- `Princess Puppy’s Magical Pawprint.png` — 1208 × 1302 px, SHA-256 `36fefefb2950088c0e0d4320d567ee9c173ae2e07a2e4202f06cab3c2d05e5cc`; Close alternate of the colorful split cover concept, with different layout/aspect ratio; not print approved.
- `Leia’s Magical Pawprint Adventure.png` — 1103 × 1426 px, SHA-256 `ce2e36fa66cd4717b365772856507a269e2dc1d6bad928256cf8ca5d53c66a6d`; Four-panel black-and-white narrative/storyboard with multiple scenes; reference, not a standalone print coloring page.

## Print-size baseline

For an 8.5 × 11 inch full-page raster at 300 pixels per inch, the trim-size raster is **2550 × 3300 px** before any bleed allowance. This is a planning baseline, not permission to upscale a small source and call it print-ready. Final artwork may be vector or otherwise produced through a workflow that genuinely supports the required print quality.

## Scene mapping status

The scene plan itself is still **Ready for Review**, so this table records only evidence-based affinities. Do not force a legacy image into a scene merely to maximize reuse.

| Scene | Page | Existing candidate mapping | State |
|---:|---:|---|---|
| 1 | 5 | Unassigned pending binary inspection | gap/unknown |
| 2 | 7 | Unassigned pending binary inspection | gap/unknown |
| 3 | 9 | Unassigned pending binary inspection | gap/unknown |
| 4 | 11 | Unassigned pending binary inspection | gap/unknown |
| 5 | 13 | `Leia’s Braver Day Adventure.png` — possible affinity only | inspect |
| 6 | 15 | Unassigned pending binary inspection | gap/unknown |
| 7 | 17 | Unassigned pending binary inspection | gap/unknown |
| 8 | 19 | Unassigned pending binary inspection | gap/unknown |
| 9 | 21 | Unassigned pending binary inspection | gap/unknown |
| 10 | 23 | `Leia’s Braver Day Adventure.png` — possible affinity only | inspect |
| 11 | 25 | Unassigned pending binary inspection | gap/unknown |
| 12 | 27 | Unassigned pending binary inspection | gap/unknown |
| 13 | 29 | Unassigned pending binary inspection | gap/unknown |
| 14 | 31 | Unassigned pending binary inspection | gap/unknown |
| 15 | 33 | Unassigned pending binary inspection | gap/unknown |
| 16 | 35 | Unassigned pending binary inspection | gap/unknown |
| 17 | 37 | Unassigned pending binary inspection | gap/unknown |
| 18 | 39 | Unassigned pending binary inspection | gap/unknown |
| 19 | 41 | Unassigned pending binary inspection | gap/unknown |

## Binary-import checklist

For every imported candidate, record before promotion:

- repository filename and original filename;
- pixel dimensions / format;
- source provenance and generation/edit history when known;
- visual description and scene affinity;
- Leia consistency notes: breed appearance, face/muzzle, ears, eyes, coat markings, body proportions, tail, crown/accessories, expression;
- coloring suitability: clear closed regions, line weight, white space, micro-detail, accidental gray/shading;
- print assessment: genuine source quality, not just metadata DPI;
- decision: reject, reference-only, keeper-source, or requires redraw/rebuild;
- public-site approval as a separate decision from keeper status.

On import, set the manifest entry's `repository_path`, change `binary_state` to `imported`, record actual dimensions, and update classification/scene affinity only from visual evidence. If a legacy binary is conclusively unrecoverable, set `binary_state` to `unavailable` rather than deleting its historical record.

## A01 completion rule

A01 is complete only when all known candidate binaries have either been imported and reviewed or explicitly recorded as unavailable, every candidate has a disposition, and each of the 19 scenes is marked with a keeper source or a confirmed art gap. That evidence then feeds A02: the definitive reusable Leia character consistency sheet under `series/characters/leia/`.

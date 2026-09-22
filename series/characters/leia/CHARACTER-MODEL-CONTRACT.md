# Leia Character Model Contract

Status: **A02 preparation — not an approved character model.** This contract defines the evidence and views required to complete A02 after A01 establishes usable visual references. It deliberately does not invent Leia's unresolved physical traits.

## Purpose

Leia must remain recognizably the same puppy across every scene, cover, book, and future series asset. A02 is complete only when a reusable visual model and its written decisions make that consistency reproducible without relying on memory or a single pose.

## Evidence rule

Do not lock a physical trait from prose alone when the trait is visual. Each locked visual trait must cite one or more reviewed A01 keeper/reference assets or an explicitly approved new model-sheet drawing. If legacy references conflict, record the conflict and choose deliberately; do not average incompatible designs.

## Required identity decisions

The approved model must explicitly lock:

| Area | Decision required | Acceptance test |
|---|---|---|
| Overall puppy type | breed appearance / silhouette vocabulary | Leia is recognizable without crown or text |
| Head | skull, cheek and muzzle proportions | front, 3/4 and profile agree structurally |
| Ears | shape, size, set and carriage | ear identity survives expression changes |
| Eyes | shape, spacing, pupil/highlight convention | expressions vary without changing character identity |
| Nose / mouth | nose geometry, smile/mouth vocabulary | readable at coloring-book scale |
| Coat | exact markings and placement | markings do not migrate or mirror accidentally |
| Body | torso, leg and paw proportions | standing, sitting and walking poses feel like one character |
| Tail | length, shape and carriage | consistent across front/side/rear views |
| Crown | silhouette, points, band and placement | repeatable and simple enough for ages 4–8 |
| Accessories | default vs scene-specific items | no accidental costume drift |

## Required model-sheet views

At minimum, the approved reusable sheet must show:

1. front standing;
2. left/right profile convention (one profile may be mirrored only if markings are symmetric; otherwise both are required);
3. three-quarter standing;
4. seated;
5. walking or light action pose;
6. rear/three-quarter rear view sufficient for scene 18;
7. close head views for happy, curious, brave/determined, surprised, and gentle/kind expressions;
8. crown detail and any asymmetric coat-marking callouts.

## Coloring-book line-art contract

The model sheet must also demonstrate the production vocabulary used by Book 1:

- strong, clean outer silhouette;
- simpler interior detail than exterior contour;
- large closed coloring regions appropriate for roughly ages 4–8;
- no reliance on gray shading, texture noise, tiny fur strokes, or dense hatching to define Leia;
- facial features remain legible when printed at the smallest planned scene size;
- paws, eyes, ears, crown and coat markings remain distinguishable after normal print reproduction;
- generous white space around character detail; scene complexity belongs in composition, not micro-detail on Leia.

These are design constraints, not a substitute for a later physical-proof check.

## Scene stress tests

Before A02 can be marked Complete, the approved model must be demonstrably capable of the Book 1 demands below without redesigning Leia:

- scene 1: curious lean / close inspection;
- scene 5: mid-hop action;
- scene 6: gentle interaction with bunny;
- scene 10: climbing pose;
- scene 12: close interaction with bucket/key;
- scene 15: mirror view without marking inconsistency;
- scene 17: paw pressed into earth;
- scene 18: rear/three-quarter walking pose;
- scene 19: warm seated finale portrait.

A single polished front pose is therefore insufficient evidence for A02.

## Version and provenance block

When the visual model is approved, replace the placeholders below in the same PR that advances A02:

- Model version: `UNSET`
- Approval state: `UNAPPROVED`
- Approved by: `UNSET`
- Source/reference assets: `UNSET`
- Source commit: `UNSET`
- Model-sheet file(s): `UNSET`
- AI generation/edit provenance: `UNSET — record actual process truthfully`

## Promotion gate

A02 may move from Not Started/In Progress to Complete only when:

- A01 has dispositions for all known candidate assets and scene keeper/gap evidence;
- every identity decision above is resolved from reviewed evidence or explicit approval;
- required views and expression references exist in `series/characters/leia/`;
- Book 1 scene stress tests pass by visual review;
- provenance/version fields are filled;
- the approved model is reusable series truth rather than a Book 1-only workaround.

Until then, this file is a contract for the model, not the model itself.

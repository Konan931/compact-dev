# Repository labels

This document defines the internal label vocabulary used across `compact-dev`.

Labels are used to mark maintenance status, repository discipline, design intent, and explicit risk or ambiguity.

## Status labels

### `EXPERIMENTAL`
Prototype or exploratory material.

Use this label for:
- early implementations
- unstable interfaces
- proofs of concept
- short-lived trial structures

This label signals that breakage is acceptable and expected.

### `OWNED`
Actively maintained and reviewed material.

Use this label for:
- components with a clear maintainer
- reviewed tools
- stable or stabilizing implementation paths
- repository areas that are considered part of the active core

This label signals accountability and continuity.

### `ARCHIVED`
Preserved but not actively maintained.

Use this label for:
- historical material
- frozen experiments
- retired implementations
- preserved reference artifacts

Archived material may still be valuable, but should not be treated as current production direction.

## Discipline and structure labels

### `NOMISCATALL`
No misc at all.

Use this label to mark areas or files that must remain structurally strict and must not become catch-all storage.

This label exists to resist repository entropy.

## Design-space labels

### `KLANG`
System design workspace.

Use this label for:
- architecture sketches
- system-relationship notes
- conceptual models
- structural thinking spaces

This label does not necessarily imply production readiness. It identifies design intent and systems thinking.

## Explicit warning labels

### `SUSSYS`
Suspect system, explicitly marked.

Use this label for:
- questionable internals
- intentionally unsafe experiments
- unstable assumptions
- components that require caution during inspection or reuse

This label should be used deliberately and transparently.

## Creative or intentionally chaotic labels

### `ART`
Intentionally chaotic, aesthetic, or non-linear material.

Use this label for:
- creative debris with value
- aesthetic fragments
- intentionally rough concept material
- artifacts that are not cleanly technical, but still intentionally preserved

This label does not excuse meaningless clutter. It marks intentional irregularity.

## Usage rules

- Do not apply labels casually.
- Prefer explicitness over decoration.
- Avoid contradictory label combinations unless the contradiction is itself meaningful and documented.
- `OWNED` and `ARCHIVED` should normally not be combined.
- `EXPERIMENTAL` may later graduate into `OWNED`.
- `SUSSYS` should be used when caution is part of the meaning, not as a joke.
- `NOMISCATALL` should be treated as a structural constraint, not a visual tag.

## Philosophy

The label system exists to preserve clarity without flattening the character of the repository.

It should help maintain structure, intent, and honesty across the project as it grows.

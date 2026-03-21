# Architecture

## Overview

`compact-dev` is a compact developer toolbox and polyglot codekit built around a small-core philosophy.

The repository is designed to favor:

- composable tools
- explicit structure
- auditable repository state
- small interfaces
- incremental language expansion

The project currently uses Python as its primary reference implementation while reserving space for future Go and C components where they are operationally justified.

## Core idea

The central architectural idea of `compact-dev` is:

- keep the active core small
- avoid monolithic tooling
- separate repository discipline from language expansion
- let each implementation layer justify its existence

This repository is not intended to become a miscellaneous dumping ground for unrelated experiments.

It is meant to remain compact, interpretable, and maintainable.

## Repository layers

The project is currently organized into the following layers:

### 1. Repository control layer

This layer defines and preserves repository discipline.

Examples include:

- `compact audit`
- metadata files such as `profile.json`
- badge generation via `badge.json`
- documentation such as governance, labels, and structure notes

This layer ensures that the repository can inspect and describe itself.

### 2. Reference implementation layer

This layer contains the currently maintained implementation core.

At present, this is the Python package in:

- `src/python/compact/`

Its role is to:

- provide the canonical CLI behavior
- serve as the first implementation path
- remain easy to test, inspect, and evolve

### 3. Language expansion layer

This layer contains future language-specific implementations or utilities.

Currently reserved areas:

- `src/go/`
- `src/c/`

These directories exist to support carefully scoped additions, not speculative bulk expansion.

## Language roles

### Python

Python is currently the primary and maintained implementation language.

It is used because it supports:

- fast iteration
- readable CLI tooling
- simple testing
- straightforward packaging
- broad maintainability

Python is the current source of truth for implemented repository behavior.

### Go

Go is reserved for future tools that benefit from:

- static binaries
- fast startup
- low-friction deployment
- explicit CLI ergonomics

Go should be introduced when operational simplicity or binary distribution offers a real advantage.

### C

C is reserved for future tools that benefit from:

- low-level control
- minimal runtime overhead
- direct systems interaction
- explicit implementation boundaries

C should be introduced deliberately and only where it provides architectural or operational value.

## CLI design

The command-line interface should remain small, legible, and task-oriented.

The current command surface is intentionally compact:

- `compact init`
- `compact audit`
- `compact badge`

New commands should only be added when they are:

- clearly scoped
- structurally justified
- consistent with the repository philosophy

The CLI should prefer a toolbox model over a framework model.

## Auditability

Auditability is a first-class architectural concern.

The repository should be able to validate:

- required structure
- required metadata
- JSON integrity where applicable
- presence of core documentation
- presence of expected implementation anchors

This is currently expressed through `compact audit` and its associated tests.

## Documentation model

Documentation in `compact-dev` is part of the architecture, not an afterthought.

At minimum, the repository should maintain clarity around:

- structure
- governance
- labels
- implementation status
- future direction

Documentation should describe both the current truth and the intended direction without pretending unfinished parts already exist.

## Growth model

The repository should grow by extension, not by uncontrolled accumulation.

Preferred growth pattern:

1. define the structural need
2. document the role
3. add the smallest useful implementation
4. test it
5. integrate it into audit and documentation

This keeps the project compact even as it expands.

## Non-goals

`compact-dev` should not become:

- a general-purpose code dump
- a miscellaneous archive without rules
- a multi-language repository without implementation discipline
- an over-engineered framework with thin practical value

## Current status

The Python core is the active reference implementation.

Go and C are currently documented structural placeholders for future expansion.

The project is in an early but functional stage, with working packaging, CLI execution, repository audit, badge generation, and automated tests.

## Direction

The immediate direction of the project is:

- strengthen repository discipline
- refine CLI behavior
- improve documentation depth
- modernize automation
- expand language-specific tooling only when justified

The long-term direction is to remain compact while becoming more capable.
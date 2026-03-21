# Roadmap

## Overview

This roadmap describes the current direction of `compact-dev`.

It is intentionally compact and focuses on practical, auditable progress.

## Current baseline

The repository currently provides:

- Python packaging via `pyproject.toml`
- editable local installation
- a compact CLI entry point
- repository audit tooling
- badge generation
- automated tests for the Python core
- architecture, labels, governance, and structure documentation

## Near-term priorities

### 1. Repository discipline
- keep structure documentation aligned with reality
- extend audit coverage only where it improves clarity
- reduce transitional or ambiguous repository state

### 2. Python core refinement
- improve CLI ergonomics
- expand tests where functionality grows
- keep the implementation small and readable
- avoid unnecessary dependency growth

### 3. Documentation depth
- keep architecture and roadmap current
- document workspace intent clearly
- add contributor-facing guidance where useful

### 4. Automation
- modernize GitHub Actions
- align CI with the current Python packaging workflow
- keep automation minimal and maintainable

## Medium-term goals

### CLI improvements
Potential additions may include:

- improved `--help` output
- version reporting
- more explicit initialization behavior
- clearer command grouping if the toolbox grows

### Language expansion
The repository reserves space for:

- Go-based utilities in `src/go/`
- C-based utilities in `src/c/`

These areas should only expand when a concrete use case exists.

### Workspace maturation
Potential future additions include:

- dedicated README files for non-trivial subtools
- language-specific build guidance
- compact examples for supported workflows

## Long-term direction

The long-term goal is not size for its own sake.

The goal is to keep `compact-dev` compact while increasing:

- usefulness
- clarity
- auditability
- implementation depth where justified

## Non-goals

The project should not become:

- a miscellaneous archive
- a dumping ground for unrelated experiments
- a bloated framework with unclear ownership
- a multi-language repository without discipline

## Notes

This roadmap is directional rather than exhaustive.

New work should be added only when it strengthens the repository without diluting its structure.
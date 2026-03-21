# C workspace

This directory is reserved for C-based utilities and lower-level experiments within `compact-dev`.

## Purpose

The C workspace exists for components that benefit from:

- low-level control
- minimal runtime overhead
- portability
- direct systems interaction
- explicit implementation of small core utilities

## Intended use

Typical candidates for this area include:

- small system utilities
- parsing helpers
- low-level inspection tools
- compact support binaries
- experiments where direct control over memory and execution matters

## Current status

This directory is currently a structural placeholder.

There is no maintained C implementation yet.

## Relation to the Python core

The Python implementation in `src/python/compact/` is currently the primary reference implementation.

C code added here should be justified by one or more of the following:

- lower-level system access
- performance-sensitive behavior
- binary-size or dependency constraints
- educational or architectural value

C should be used deliberately, not decoratively.

## Rules

- Keep utilities compact and auditable.
- Prefer clarity over cleverness.
- Minimize hidden behavior.
- Avoid unnecessary build complexity.
- Document every non-trivial addition.

## Future direction

This workspace may later contain:

- single-purpose command-line tools
- helper libraries for compact utilities
- low-level experiments with explicit scope and documentation
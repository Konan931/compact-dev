# Go workspace

This directory is reserved for Go-based implementations and experiments within `compact-dev`.

## Purpose

The Go workspace exists to support future components that benefit from:

- static binaries
- fast startup time
- simple deployment
- strong CLI ergonomics
- explicit systems-level tooling

## Intended use

Typical candidates for this area include:

- standalone CLI helpers
- repository inspection tools
- filesystem-oriented utilities
- lightweight automation helpers
- ports of selected Python tooling where a compiled binary is beneficial

## Current status

This directory is currently a structural placeholder.

There is no maintained Go implementation yet.

## Relation to the Python core

The Python implementation in `src/python/compact/` is currently the primary reference implementation.

Go code added here should either:

- implement new functionality that is better suited to Go, or
- provide a carefully scoped port of an existing tool

Go should not duplicate Python code without a clear operational reason.

## Rules

- Keep tools small and focused.
- Prefer standard library solutions where reasonable.
- Avoid framework-heavy designs.
- Document each tool with a short README when the directory grows.
- Preserve repository clarity over premature expansion.

## Future direction

This workspace may later contain:

- one or more Go modules
- small internal packages
- compiled CLI utilities integrated into the broader `compact-dev` toolbox
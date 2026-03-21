# Contributing

Thank you for contributing to `compact-dev`.

This repository is intentionally compact and structured.
Contributions should preserve that quality rather than expand the repository without a clear reason.

## Principles

Contributions should align with the following principles:

- keep tools small and focused
- prefer clarity over cleverness
- document structural intent
- avoid miscellaneous accumulation
- preserve auditability
- justify expansion, especially across languages

## Before contributing

Before opening a change, please make sure that:

- the repository structure still makes sense
- documentation reflects reality
- Python tests pass
- `compact audit` still passes
- new files have a clear purpose
- additions do not weaken the compact nature of the project

## Local development

Set up a local development environment from the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
```

Run tests:

```bash
python -m pytest
```

Run repository audit:

```bash
compact audit
```

Regenerate badge metadata when needed:

```bash
compact badge
```

## Contribution scope

Good contributions usually include one or more of the following:

* improvements to existing compact tools
* better tests
* clearer documentation
* tighter repository discipline
* carefully justified additions to Python, Go, or C workspaces

Contributions should not introduce bulk without purpose.

## Python changes

Python is currently the primary reference implementation.

When changing Python code:

* keep functions small
* prefer explicit behavior
* avoid unnecessary dependencies
* preserve CLI legibility
* add or update tests when behavior changes

## Go and C changes

src/go/ and src/c/ are reserved for deliberate expansion.

Changes in these areas should be justified by clear technical need, such as:

* binary distribution
* startup performance
* low-level control
* systems-oriented behavior

Do not add language-specific code only for symmetry.

## Documentation changes

Documentation is part of the architecture.

When changing repository structure or direction, update the relevant documents as needed:

* README.md
* structure.md
* docs/architecture.md
* docs/roadmap.md
* docs/labels.md

Documentation should describe the current truth, not an imagined future state.

## Commit style

Prefer small, focused commits.

Examples:

* `Refactor badge generation and expand tests`
* `Document Go and C workspaces`
* `Tighten repository audit coverage`

Avoid mixing unrelated cleanup and feature work in a single commit unless the cleanup is required for the feature.

## Pull requests

Pull requests should clearly explain:

* _what_ changed
* _why_ it changed
* whether structure or documentation was affected
* whether tests and audit were run

Small, precise pull requests are preferred over broad, unfocused ones.

## Final note

`compact-dev` should remain compact.

Contribute in a way that increases usefulness, clarity, and structural integrity without turning the repository into a miscellaneous toolbox.
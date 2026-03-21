# compact-dev — a compact developer toolbox and codekit

> Built around the UNIX philosophy: small tools, composability, and clarity.

Maintained and curated within the ecosystem of **Digital Welfare™ Productions**.

![last update](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/Konan931/compact-dev/main/badge.json)

<a id="toc"></a>
## Table of contents
- [Overview](#overview)
- [Current status](#current-status)
- [Features](#features)
- [Profile](#profile)
- [Structure](#structure)
- [Labels](#labels)
- [Quick start](#quick-start)
- [Stability](#stability)
- [Architecture](#architecture)
- [Governance](#governance)
- [Roadmap](#roadmap)

<a id="overview"></a>
## Overview

**`compact-dev`** is a **compact developer toolbox** and **polyglot codekit** focused on:

- small, auditable tools
- repository discipline
- metadata-driven maintenance
- language-specific expansion without losing structural clarity

The current core is implemented in **Python**, while additional language targets such as **Go** and **C** are part of the repository design and _will be expanded incrementally_.

<a id="current-status"></a>
## Current status

The Python core is the current reference implementation.

At this stage, the repository already provides working utilities for:

- repository auditing
- badge generation
- initialization-oriented tooling

_The broader repository structure is intentionally prepared for future extension into **additional runtimes** and **lower-level implementations**._

<a id="features"></a>
## Features

- `compact init` — initialize project scaffolding
- `compact audit` — validate repository structure and metadata
- `compact badge` — generate `badge.json` for Shields.io endpoint badges

<a id="profile"></a>
## Profile

- [profile.json](./profile.json)
- Raw: https://raw.githubusercontent.com/Konan931/compact-dev/main/profile.json

<a id="structure"></a>
## Structure

See: [structure.md](./structure.md)

<a id="labels"></a>
## Labels

Repository labels are documented in more detail here:

- [docs/labels.md](./docs/labels.md)

Current label set:

- `EXPERIMENTAL` — prototype, may break
- `OWNED` — actively maintained and reviewed
- `ARCHIVED` — preserved but not actively maintained
- `NOMISCATALL` — no misc at all
- `KLANG` — system design workspace
- `SUSSYS` — suspect system, explicitly marked
- `ART` — intentionally chaotic or aesthetic material

<a id="quick-start"></a>
## Quick start

###### Run through the shell wrapper:

```bash
./bin/compact init
./bin/compact audit
./bin/compact badge
```

###### Run through Python directly:

```bash
PYTHONPATH=src/python python -m compact audit
PYTHONPATH=src/python python -m compact badge
```

Development test flow will be formalized through `pyproject.toml` and repository tests.

<a id="stability"></a>

## Stability

The Python core is currently the most stable and maintained part of the repository.

_**Interfaces and structure may still evolve** while the project is being refined, especially in areas related to **packaging**, **language expansion**, and **repository governance**._

<a id="architecture"></a>

## Architecture

See: [docs/architecture.md](./docs/architecture.md)

<a id="governance"></a>

## Governance

See: [docs/governance.md](./docs/governance.md)

<a id="roadmap"></a>

## Roadmap

See: [docs/roadmap.md](./docs/roadmap.md)

# compact-dev — compact project scaffolding that stays auditable

> Small tools, composable presets, explicit repository contracts.

`compact-dev` is a dependency-light project generator and repository auditor maintained within Digital Welfare™ Productions. Version 0.2 separates the generator from the repository it generates so a template remains small, portable, and explicit about what it does.

## Why this exists

A GitHub template should be reusable without dragging its author's identity, local state, or provider credentials into every new repository. `compact-dev` therefore treats templates as composable overlays backed by an auditable repository contract rather than a hidden mix of local assumptions.

## Quickest path from zero to a working project

If you want the shortest route to a usable repository, do this:

```bash
python -m pip install -e '.[dev]'
compact init ./demo --name "Demo CLI" --preset python-cli
compact audit ./demo --strict
compact doctor ./demo
```

That gives you a generated Python CLI project, a repository contract in `compact.toml`, and immediate validation checks for hygiene and setup.

If you want to preview without writing files:

```bash
compact init ./candidate --preset python-cli --dry-run
```

If you want to generate a static web site baseline instead:

```bash
compact init ./site --name "DWP Site" --preset web-static --preset vercel
```

## Quick start

```bash
python -m pip install -e '.[dev]'
compact presets
compact init ./demo --name "Demo CLI" --preset python-cli
compact audit ./demo --strict
compact doctor ./demo
```

Compose overlays when useful:

```bash
compact init ./site --name "DWP Site" --preset web-static --preset vercel
```

Preview without writing:

```bash
compact init ./candidate --preset python-cli --dry-run
```

Re-running an initialized project does not require repeating its name or presets:

```bash
compact init ./demo
```

The existing `compact.toml` contract supplies those defaults unless you explicitly override them.

## What a generated repo looks like

A typical generated Python project looks like this:

```text
demo/
├── README.md
├── pyproject.toml
├── compact.toml
├── src/
│   └── demo/
│       ├── __init__.py
│       └── cli.py
├── tests/
│   └── test_smoke.py
├── .github/
│   └── workflows/
│       └── ci.yml
└── docs/
```

This is intentionally compact: a single generated package layout, a clear contract file, and audit/doctor checks that are obvious to maintain.

## Commands

- `compact init [target]` — non-destructive scaffold generation; conflicts abort the entire write unless `--force` is explicit.
- `compact audit [target]` — validate `compact.toml`, preset-required files, unresolved tokens, backup artifacts, and common secret-bearing filenames.
- `compact doctor [target]` — inspect Python/Git and optional provider tooling without changing external services.
- `compact status [target]` — compact machine-friendly project/audit summary.
- `compact badge [target]` — refresh `badge.json` timestamp metadata.
- `compact presets` — list available presets and dependencies.

For `audit`, `doctor`, `status`, and `badge`, an explicit target is exact: the command will not silently climb into a parent project. If the target is omitted, `compact` discovers the nearest project root by walking upward from the current working directory.

`audit`, `doctor`, `status`, and `presets` support structured JSON where applicable.

## Presets

| Preset | Role |
| --- | --- |
| `base` | portable repo hygiene, docs, review template, `compact.toml` |
| `python-cli` | Python package, console entry point, pytest smoke test, CI |
| `web-static` | framework-free HTML/CSS/JS baseline |
| `vercel` | deployment hygiene and docs; does not link or deploy |

## Design guarantees

- Target paths come from the user, not from the installed package location.
- Explicit targets never fall through to a parent repository.
- Existing project identity and presets are retained on ordinary re-initialization.
- Default initialization is non-destructive and aborts on conflicts before writing.
- `--dry-run` exposes the plan; `--force` is required for managed-file replacement.
- Template paths reject parent traversal, absolute paths, Windows drive paths, and backslash-based escape forms.
- Project names are escaped for TOML, Python, and HTML where those formats require it.
- Provider linking, secrets, migrations, and deployment are not hidden side effects.
- The source repository dogfoods the same `compact.toml` contract used by generated projects.

## Development

```bash
PYTHONPATH=src/python python -m pytest
PYTHONPATH=src/python python -m compact audit . --strict
PYTHONPATH=src/python python -m compact init /tmp/compact-smoke --name Smoke --preset python-cli
PYTHONPATH=src/python python -m compact audit /tmp/compact-smoke --strict
```

CI additionally installs and executes generated Python projects across Linux, macOS, and Windows, and verifies preset resources from a built wheel.

See `docs/architecture.md`, `structure.md`, and `docs/roadmap.md` for the model and next steps.

## License

The repository's existing license remains unchanged in v0.2. Because this repository is also marked as a GitHub template, licensing for broader template reuse remains an explicit governance decision. The code and generated output remain clear about what is template-managed and what is project-local.

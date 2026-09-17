# compact-dev — compact project scaffolding that stays auditable

> Small tools, composable presets, explicit repository contracts.

`compact-dev` is a dependency-light project generator and repository auditor maintained within **Digital Welfare™ Productions**. Version 0.2 separates the generator from the repository it generates: the CLI now operates on a user-selected target instead of assuming its own installation directory.

## Why this exists

A GitHub template should be reusable without dragging its author's identity, local state, or provider credentials into every new repository. `compact-dev` therefore treats templates as composable overlays and records the selected contract in `compact.toml`.

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

## Commands

- `compact init [target]` — non-destructive scaffold generation; conflicts abort the entire write unless `--force` is explicit.
- `compact audit [target]` — validate `compact.toml`, preset-required files, unresolved tokens, backup artifacts, and common secret-bearing filenames.
- `compact doctor [target]` — inspect Python/Git and optional provider tooling without changing external services.
- `compact status [target]` — compact machine-friendly project/audit summary.
- `compact badge [target]` — refresh `badge.json` timestamp metadata.
- `compact presets` — list available presets and dependencies.

`audit`, `doctor`, `status`, and `presets` support structured JSON where applicable.

## Presets

| Preset | Role |
| --- | --- |
| `base` | portable repo hygiene, docs, review template, `compact.toml` |
| `python-cli` | Python package, console entry point, pytest smoke test, CI |
| `web-static` | framework-free HTML/CSS/JS baseline |
| `vercel` | deployment hygiene and docs; **does not** link or deploy |

## Design guarantees

- Target paths come from the user, not from the installed package location.
- Default initialization is non-destructive and aborts on conflicts before writing.
- `--dry-run` exposes the plan; `--force` is required for managed-file replacement.
- Provider linking, secrets, migrations, and deployment are not hidden side effects.
- The source repository dogfoods the same `compact.toml` contract used by generated projects.

## Development

```bash
PYTHONPATH=src/python python -m pytest
PYTHONPATH=src/python python -m compact audit . --strict
PYTHONPATH=src/python python -m compact init /tmp/compact-smoke --name Smoke --preset python-cli
PYTHONPATH=src/python python -m compact audit /tmp/compact-smoke --strict
```

See `docs/architecture.md`, `structure.md`, and `docs/roadmap.md` for the model and next steps.

## License

The repository's existing license remains unchanged in v0.2. Because this repository is also marked as a GitHub template, licensing for broader template reuse remains an explicit governance decision rather than an implicit generator default.

# Architecture

## 0.2 model

`compact-dev` separates four concerns:

1. **CLI** — user-facing commands and explicit target selection.
2. **Preset engine** — declarative manifests plus inline templates.
3. **Repository contract** — `compact.toml` records project identity, active presets, and optional extra audit requirements.
4. **Verification** — audit, doctor, status, and CI validate generated state without silently mutating external services.

## Data flow

```text
preset manifests + templates
          │
          v
    compact init TARGET
          │
          v
      compact.toml
          │
     ┌────┴─────┐
     v          v
 compact audit  compact doctor
```

## Target resolution

Target semantics are intentionally asymmetric:

- `compact init [target]` generates into the explicit target, defaulting to the current directory.
- `audit`, `doctor`, `status`, and `badge` use an explicit target exactly as provided.
- when those inspection commands omit the target, the CLI searches upward from the current directory for the nearest `compact.toml`.

This prevents a typo or uninitialized child directory from silently redirecting an explicit command to a parent project while preserving convenient operation from project subdirectories.

## Preset composition and re-initialization

Presets declare dependencies. `python-cli`, `web-static`, and `vercel` currently depend on `base`. Dependency resolution is deterministic and de-duplicated, so future overlays can be added without copying the entire base template.

When `compact init` encounters a valid existing `compact.toml`, omitted `--name` and `--preset` values inherit that contract. Explicit flags still override it. This makes ordinary re-initialization idempotent and prevents `--force` without other flags from accidentally collapsing a composed project back to `base`.

## Template boundaries

The renderer remains intentionally small but performs format-aware value preparation and path validation:

- TOML strings are encoded rather than interpolated raw.
- Python package identifiers are normalized and protected against reserved keywords.
- HTML-facing project names are escaped before insertion into attributes or text nodes.
- generated paths must be relative POSIX-style paths and may not traverse parents, use Windows drives, or contain backslashes.

These checks apply to preset output rather than the preset manifests themselves, so template tokens remain inspectable source data.

## Safety properties

Initialization plans all managed files before writing. If any destination conflicts and `--force` is absent, no generated file is written. `--dry-run` uses the same plan but never writes.

Deployment presets provide configuration and guidance only. Vercel linking, environment synchronization, previews, and production promotion remain explicit external actions.

## Source repository vs generated repository

The package source is not itself the canonical generated layout. The source uses `compact.toml` with `base` plus extra audit requirements; generated `python-cli` projects use the standard `src/<package>/` layout. This avoids the old self-bootstrap coupling.

## Extension contract

A new preset needs only:

- `resources/presets/<name>.toml`
- inline, inspectable file templates in that preset manifest
- tests proving generation and strict audit
- installation or execution smoke coverage when the preset produces runnable code

Provider presets must keep authentication, environment synchronization, provisioning, migration, and deployment as explicit external actions.

Avoid adding a runtime dependency solely to make templating more elaborate. The current token renderer is intentionally small and inspectable.

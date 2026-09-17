# Architecture

## 0.2 model

`compact-dev` now separates four concerns:

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

## Preset composition

Presets declare dependencies. `python-cli`, `web-static`, and `vercel` currently depend on `base`. Dependency resolution is deterministic and de-duplicated, so future overlays can be added without copying the entire base template.

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

Avoid adding a runtime dependency solely to make templating more elaborate. The current token renderer is intentionally small and inspectable.

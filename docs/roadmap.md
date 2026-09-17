# Roadmap

## v0.2 — template foundation

- target-aware generator instead of self-bootstrap
- composable preset manifests
- `base`, `python-cli`, `web-static`, and `vercel` presets
- atomic conflict handling, `--dry-run`, explicit `--force`
- configuration-backed audit with strict and JSON modes
- environment doctor and machine-readable status
- cross-platform smoke testing for generated projects

## Next candidates

These are intentionally not part of the v0.2 core commit:

- `typescript-lib` and `node-cli` overlays
- a `nextjs` overlay that composes with `vercel`
- `go-cli` and `c-cli` presets backed by real build/test flows rather than placeholder directories
- JSON Schema or generated documentation for `compact.toml`
- `compact diff` to compare a repository against its current preset baseline without overwriting it
- optional checksums/provenance metadata for generated files
- release automation and signed artifacts

## Governance decisions still open

- reconcile public GitHub-template use with the current proprietary license
- decide whether DWP-specific presets belong here or in a separate preset pack
- define the compatibility policy for preset changes across minor versions

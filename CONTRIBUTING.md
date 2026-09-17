# Contributing

`compact-dev` is intentionally small. Contributions should improve reuse, auditability, or portability without turning the core into a framework.

## Development loop

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
pytest
compact audit . --strict
```

## Preset changes

Every preset addition or behavior change should include:

- a declarative manifest and inspectable templates
- generation tests in a temporary directory
- a strict audit of the generated result
- documentation of external side effects, if any

Provider presets must not silently authenticate, provision, migrate, or deploy.

## Code style

Prefer standard-library solutions, explicit behavior, short functions, English code comments, and actionable error messages. Keep commits focused and document structural changes.

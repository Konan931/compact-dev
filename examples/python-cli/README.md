# Demo CLI example

This example is a generated project created from the `python-cli` preset in `compact-dev`.

It is intentionally small and complete enough to act as a reference scaffold for a real project.

## Quick run

```bash
python -m pip install -e .
demo --name "Alex"
```

## Test it

```bash
python -m pytest
```

## Layout

```text
demo-cli/
├── README.md
├── compact.toml
├── pyproject.toml
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   └── demo_cli/
│       ├── __init__.py
│       └── cli.py
└── tests/
    └── test_smoke.py
```

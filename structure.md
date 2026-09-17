# Repository structure

```text
compact-dev/
├── .github/
│   ├── pull_request_template.md
│   └── workflows/ci.yml
├── bin/
│   ├── compact
│   └── compact-init
├── docs/
│   ├── architecture.md
│   ├── decisions.md
│   ├── governance.md
│   ├── labels.md
│   └── roadmap.md
├── src/python/compact/
│   ├── __init__.py
│   ├── __main__.py
│   ├── audit.py
│   ├── badge.py
│   ├── cli.py
│   ├── config.py
│   ├── doctor.py
│   ├── init.py
│   ├── paths.py
│   ├── presets.py
│   ├── status.py
│   ├── templates.py
│   └── resources/presets/
│       ├── base.toml
│       ├── python-cli.toml
│       ├── web-static.toml
│       └── vercel.toml
├── tests/python/
├── .editorconfig
├── .gitattributes
├── .gitignore
├── compact.toml
├── CONTRIBUTING.md
├── LICENSE
├── pyproject.toml
├── README.md
└── SECURITY.md
```

Go and C remain possible future targets, but placeholder directories are no longer part of the generator contract. Language support should enter as executable, tested presets rather than empty symmetry.

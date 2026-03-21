# Repository structure

## Tree

```text
compact-dev/
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── bin/
│   ├── compact
│   ├── compact-init
│   ├── compact-init.bak
│   └── compact.bootstrap.bak
│
├── docs/
│   ├── architecture.md
│   ├── governance.md
│   └── labels.md
├──src/
│    ├── python/
│    │   └── compact/
│    │       ├── __init__.py
│    │       ├── __main__.py
│    │       ├── audit.py
│    │       ├── badge.py
│    │       └── paths.py
│    │
│    ├── go/
│    │   └── README.md
│    └── c/
│        └── README.md
│
├── tests/
│   └── python/
│       ├── test_audit.py
│       └── test_badge.py
│
├── .gitignore
├── badge.json
├── profile.json
├── pyproject.toml
├── README.md
└── structure.md
```

## Notes

* .github/workflows/ contains CI-related workflow definitions.

* bin/ contains thin wrapper scripts and bootstrap-oriented helpers.

* docs/ contains governance and repository vocabulary documentation.

* project/ currently exists in the repository root and should either be documented further or removed in a later cleanup pass.

* src/python/compact/ contains the current primary reference implementation.

* src/go/ and src/c/ are reserved for future language-specific extensions.

* tests/python/ contains automated tests for the Python core.

* profile.json and badge.json provide repository metadata and badge integration.

* pyproject.toml is the primary Python project definition for packaging, editable installs, and development dependencies.

## Status

* The Python core is currently the primary maintained implementation.

* Go and C are currently structural placeholders for future expansion and are not yet feature-complete.

* Some repository files and directories still reflect transitional state and may be cleaned up in later revisions.
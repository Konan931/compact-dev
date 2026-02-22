#!/usr/bin/env python3
# Repo audit tool for compact-dev.
# English-only comments as requested.

from __future__ import annotations

import json
import sys
from pathlib import Path

REQUIRED_DIRS = [
    "bin",
    "docs",
    "src/python/compact",
    "src/go",
    "src/c",
]

REQUIRED_FILES = [
    "README.md",
    "profile.json",
    "badge.json",
    "docs/governance.md",
]

def eprint(*args: object) -> None:
    print(*args, file=sys.stderr)

def check_exists(root: Path) -> list[str]:
    errors: list[str] = []
    for d in REQUIRED_DIRS:
        if not (root / d).exists():
            errors.append(f"Missing directory: {d}")
    for f in REQUIRED_FILES:
        if not (root / f).exists():
            errors.append(f"Missing file: {f}")
    return errors

def check_json(root: Path, rel: str) -> list[str]:
    p = root / rel
    if not p.exists():
        return []
    try:
        json.loads(p.read_text(encoding="utf-8"))
        return []
    except Exception as ex:
        return [f"Invalid JSON in {rel}: {ex}"]

def main(args: list[str] | None = None) -> int:
    if args is None:
        import sys
        args = sys.argv[1:]

    root = Path(__file__).resolve().parents[3]
    errors: list[str] = []
    errors += check_exists(root)
    errors += check_json(root, "profile.json")
    errors += check_json(root, "badge.json")

    if errors:
        eprint("AUDIT: FAIL")
        for err in errors:
            eprint(f"- {err}")
        return 1

    print("AUDIT: OK")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

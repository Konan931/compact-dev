from __future__ import annotations

from pathlib import Path


def resolve_root(target: str | Path | None = None) -> Path:
    """Resolve a user-controlled project root without assuming package location."""
    value = Path.cwd() if target is None else Path(target)
    return value.expanduser().resolve()


def find_project_root(start: str | Path | None = None) -> Path:
    """Find the nearest compact.toml, falling back to the resolved start path."""
    root = resolve_root(start)
    if root.is_file():
        root = root.parent
    for candidate in (root, *root.parents):
        if (candidate / "compact.toml").is_file():
            return candidate
    return root

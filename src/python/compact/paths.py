from __future__ import annotations

from pathlib import Path


def resolve_root(target: str | Path | None = None) -> Path:
    """Resolve a user-controlled path without assuming package location."""
    value = Path.cwd() if target is None else Path(target)
    return value.expanduser().resolve()


def find_project_root(start: str | Path | None = None) -> Path:
    """Discover the nearest compact.toml from a starting location."""
    root = resolve_root(start)
    if root.is_file():
        root = root.parent
    for candidate in (root, *root.parents):
        if (candidate / "compact.toml").is_file():
            return candidate
    return root


def resolve_project_root(target: str | Path | None = None) -> Path:
    """Resolve explicit targets exactly; discover parents only when target is omitted."""
    if target is not None:
        return resolve_root(target)
    return find_project_root()

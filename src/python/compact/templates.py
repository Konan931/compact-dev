from __future__ import annotations

from datetime import datetime, timezone
import html
import json
import keyword
from pathlib import PurePosixPath, PureWindowsPath
import re

from compact import __version__

_TOKEN_RE = re.compile(r"{{\s*([A-Za-z0-9_]+)\s*}}")


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.strip().lower()).strip("-")
    return slug or "project"


def package_name_from_slug(slug: str) -> str:
    package = re.sub(r"[^a-z0-9_]+", "_", slug.replace("-", "_"))
    if not package or package[0].isdigit():
        package = f"project_{package}" if package else "project"
    if keyword.iskeyword(package):
        package = f"{package}_pkg"
    return package


def build_context(
    project_name: str,
    presets: tuple[str, ...] | list[str],
    *,
    slug: str | None = None,
    package_name: str | None = None,
    generated_at: str | None = None,
) -> dict[str, str]:
    project_slug = slugify(project_name) if slug is None else slug
    package = package_name_from_slug(project_slug) if package_name is None else package_name
    timestamp = generated_at or datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    active = list(presets)
    return {
        "project_name": project_name,
        "project_name_toml": json.dumps(project_name, ensure_ascii=False),
        "project_name_python": repr(project_name),
        "project_name_html": html.escape(project_name, quote=True),
        "project_slug": project_slug,
        "package_name": package,
        "generated_at": timestamp,
        "project_year": timestamp[:4],
        "presets_toml": "[" + ", ".join(json.dumps(item) for item in active) + "]",
        "presets_display": ", ".join(active),
        "compact_version": __version__,
    }


def render_template(text: str, context: dict[str, str]) -> str:
    def replace(match: re.Match[str]) -> str:
        key = match.group(1)
        if key not in context:
            raise ValueError(f"Unknown template token: {key}")
        return context[key]

    rendered = _TOKEN_RE.sub(replace, text)
    unresolved = _TOKEN_RE.findall(rendered)
    if unresolved:
        raise ValueError(f"Unresolved template tokens: {', '.join(sorted(set(unresolved)))}")
    return rendered


def render_path(path: str, context: dict[str, str]) -> str:
    rendered = render_template(path, context)
    posix = PurePosixPath(rendered)
    windows = PureWindowsPath(rendered)
    if (
        not rendered
        or rendered in {".", ".."}
        or "\x00" in rendered
        or "\\" in rendered
        or posix.is_absolute()
        or bool(windows.drive)
        or any(part == ".." for part in posix.parts)
    ):
        raise ValueError(f"Unsafe template path: {rendered}")
    return rendered

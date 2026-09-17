from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import tomllib


class ConfigError(ValueError):
    """Raised when compact.toml is missing or malformed."""


@dataclass(frozen=True)
class CompactConfig:
    schema_version: int
    name: str
    slug: str
    package: str
    created: str
    presets: tuple[str, ...]
    required_files: tuple[str, ...] = ()
    required_dirs: tuple[str, ...] = ()


def _string(value: object, key: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ConfigError(f"compact.toml: {key} must be a non-empty string")
    return value.strip()


def load_config(root: Path) -> CompactConfig:
    path = root / "compact.toml"
    if not path.is_file():
        raise ConfigError(f"Missing compact.toml at {path}")

    try:
        data = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as exc:
        raise ConfigError(f"Invalid compact.toml: {exc}") from exc

    schema_version = data.get("schema_version")
    if schema_version != 1:
        raise ConfigError(f"compact.toml: unsupported schema_version {schema_version!r}")

    project = data.get("project")
    if not isinstance(project, dict):
        raise ConfigError("compact.toml: missing [project] table")

    preset_table = data.get("presets", {})
    active = preset_table.get("active", ["base"]) if isinstance(preset_table, dict) else None
    if not isinstance(active, list) or not active or not all(isinstance(item, str) for item in active):
        raise ConfigError("compact.toml: presets.active must be a non-empty string array")

    audit = data.get("audit", {})
    if not isinstance(audit, dict):
        raise ConfigError("compact.toml: [audit] must be a table")

    required_files = audit.get("required_files", [])
    required_dirs = audit.get("required_dirs", [])
    if not isinstance(required_files, list) or not all(isinstance(item, str) for item in required_files):
        raise ConfigError("compact.toml: audit.required_files must be a string array")
    if not isinstance(required_dirs, list) or not all(isinstance(item, str) for item in required_dirs):
        raise ConfigError("compact.toml: audit.required_dirs must be a string array")

    return CompactConfig(
        schema_version=1,
        name=_string(project.get("name"), "project.name"),
        slug=_string(project.get("slug"), "project.slug"),
        package=_string(project.get("package"), "project.package"),
        created=_string(project.get("created"), "project.created"),
        presets=tuple(active),
        required_files=tuple(required_files),
        required_dirs=tuple(required_dirs),
    )

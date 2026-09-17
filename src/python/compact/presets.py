from __future__ import annotations

from dataclasses import dataclass
from importlib import resources
import tomllib


class PresetError(ValueError):
    """Raised for unknown or malformed presets."""


@dataclass(frozen=True)
class PresetFile:
    target: str
    content: str


@dataclass(frozen=True)
class Preset:
    name: str
    description: str
    depends: tuple[str, ...]
    files: tuple[PresetFile, ...]


def _preset_root():
    return resources.files("compact").joinpath("resources", "presets")


def available_presets() -> tuple[str, ...]:
    names = [entry.name[:-5] for entry in _preset_root().iterdir() if entry.is_file() and entry.name.endswith(".toml")]
    return tuple(sorted(names))


def load_preset(name: str) -> Preset:
    manifest = _preset_root().joinpath(f"{name}.toml")
    if not manifest.is_file():
        raise PresetError(f"Unknown preset: {name}")
    data = tomllib.loads(manifest.read_text(encoding="utf-8"))
    meta = data.get("preset")
    if not isinstance(meta, dict) or meta.get("name") != name:
        raise PresetError(f"Malformed preset manifest: {name}")
    depends = meta.get("depends", [])
    file_rows = data.get("files", [])
    if not isinstance(depends, list) or not all(isinstance(item, str) for item in depends):
        raise PresetError(f"Preset {name}: depends must be a string array")
    if not isinstance(file_rows, list):
        raise PresetError(f"Preset {name}: files must be an array of tables")
    parsed_files: list[PresetFile] = []
    for row in file_rows:
        if not isinstance(row, dict) or not isinstance(row.get("target"), str) or not isinstance(row.get("content"), str):
            raise PresetError(f"Preset {name}: invalid file entry")
        parsed_files.append(PresetFile(target=row["target"], content=row["content"]))
    return Preset(
        name=name,
        description=str(meta.get("description", "")),
        depends=tuple(depends),
        files=tuple(parsed_files),
    )


def resolve_presets(requested: list[str] | tuple[str, ...] | None) -> tuple[Preset, ...]:
    names = list(requested or ["base"])
    ordered: list[Preset] = []
    visiting: set[str] = set()
    added: set[str] = set()

    def visit(name: str) -> None:
        if name in added:
            return
        if name in visiting:
            raise PresetError(f"Preset dependency cycle at {name}")
        visiting.add(name)
        preset = load_preset(name)
        for dependency in preset.depends:
            visit(dependency)
        visiting.remove(name)
        added.add(name)
        ordered.append(preset)

    for name in names:
        visit(name)
    return tuple(ordered)

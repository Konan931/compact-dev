from __future__ import annotations

from collections import OrderedDict
from dataclasses import dataclass
from pathlib import Path

from compact.config import ConfigError, load_config
from compact.presets import resolve_presets
from compact.templates import build_context, render_path, render_template


@dataclass(frozen=True)
class PlannedFile:
    path: Path
    relative_path: str
    content: str
    state: str


@dataclass(frozen=True)
class InitResult:
    target: Path
    presets: tuple[str, ...]
    files: tuple[PlannedFile, ...]
    conflicts: tuple[str, ...]
    dry_run: bool

    @property
    def ok(self) -> bool:
        return not self.conflicts


def initialize_project(
    target: Path,
    *,
    project_name: str | None = None,
    preset_names: list[str] | tuple[str, ...] | None = None,
    dry_run: bool = False,
    force: bool = False,
) -> InitResult:
    target = target.expanduser().resolve()

    existing_config = None
    if (target / "compact.toml").is_file():
        try:
            existing_config = load_config(target)
        except ConfigError:
            existing_config = None

    if project_name is None and existing_config is not None:
        name = existing_config.name
    else:
        name = (project_name or target.name or "project").strip()
    if not name:
        raise ValueError("Project name must not be empty")

    if preset_names is None and existing_config is not None:
        requested_presets: list[str] | tuple[str, ...] | None = existing_config.presets
    else:
        requested_presets = preset_names
    presets = resolve_presets(requested_presets)
    active = tuple(preset.name for preset in presets)

    if existing_config is not None and existing_config.name == name:
        context = build_context(
            name,
            active,
            slug=existing_config.slug,
            package_name=existing_config.package,
            generated_at=existing_config.created,
        )
    else:
        context = build_context(name, active)

    rendered: OrderedDict[str, str] = OrderedDict()
    for preset in presets:
        for spec in preset.files:
            relative = render_path(spec.target, context)
            content = render_template(spec.content, context)
            rendered[relative] = content

    planned: list[PlannedFile] = []
    conflicts: list[str] = []
    for relative, content in rendered.items():
        destination = target / relative
        if destination.exists():
            if not destination.is_file():
                state = "conflict"
            else:
                existing = destination.read_text(encoding="utf-8")
                state = "unchanged" if existing == content else ("overwrite" if force else "conflict")
        else:
            state = "create"
        if state == "conflict":
            conflicts.append(relative)
        planned.append(PlannedFile(destination, relative, content, state))

    result = InitResult(target, active, tuple(planned), tuple(conflicts), dry_run)
    if conflicts or dry_run:
        return result

    for item in planned:
        if item.state == "unchanged":
            continue
        item.path.parent.mkdir(parents=True, exist_ok=True)
        item.path.write_text(item.content, encoding="utf-8")
    return result

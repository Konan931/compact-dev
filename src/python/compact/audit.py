from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from pathlib import Path
import re

from compact.config import CompactConfig, ConfigError, load_config
from compact.presets import PresetError, resolve_presets
from compact.templates import build_context, render_path, slugify, package_name_from_slug


@dataclass(frozen=True)
class AuditIssue:
    level: str
    code: str
    message: str
    path: str | None = None


@dataclass(frozen=True)
class AuditResult:
    root: Path
    config: CompactConfig | None
    issues: tuple[AuditIssue, ...]
    strict: bool

    @property
    def errors(self) -> tuple[AuditIssue, ...]:
        return tuple(issue for issue in self.issues if issue.level == "error")

    @property
    def warnings(self) -> tuple[AuditIssue, ...]:
        return tuple(issue for issue in self.issues if issue.level == "warning")

    @property
    def ok(self) -> bool:
        return not self.errors and (not self.strict or not self.warnings)

    def to_dict(self) -> dict[str, object]:
        return {
            "root": str(self.root),
            "ok": self.ok,
            "strict": self.strict,
            "project": None if self.config is None else self.config.slug,
            "presets": [] if self.config is None else list(self.config.presets),
            "issues": [asdict(issue) for issue in self.issues],
        }


_SKIP_DIRS = {".git", ".venv", "node_modules", "dist", "build", "__pycache__", ".pytest_cache"}
_BACKUP_SUFFIXES = (".bak", ".orig", ".rej", "~")
_SECRET_NAMES = {".env", "id_rsa", "id_ed25519"}
_SECRET_SUFFIXES = {".pem", ".key"}
_TOKEN_PATTERN = re.compile(r"{{\s*[A-Za-z0-9_]+\s*}}")


def _iter_files(root: Path):
    for path in root.rglob("*"):
        if any(part in _SKIP_DIRS for part in path.parts):
            continue
        if path.is_file():
            yield path


def run_audit(root: Path, *, strict: bool = False) -> AuditResult:
    root = root.expanduser().resolve()
    issues: list[AuditIssue] = []
    try:
        config = load_config(root)
    except ConfigError as exc:
        issues.append(AuditIssue("error", "config", str(exc), "compact.toml"))
        return AuditResult(root, None, tuple(issues), strict)

    try:
        presets = resolve_presets(config.presets)
    except PresetError as exc:
        issues.append(AuditIssue("error", "preset", str(exc), "compact.toml"))
        return AuditResult(root, config, tuple(issues), strict)

    expected_slug = slugify(config.name)
    expected_package = package_name_from_slug(config.slug)
    if config.slug != expected_slug:
        issues.append(AuditIssue("warning", "slug-drift", f"project.slug is {config.slug!r}; normalized name is {expected_slug!r}", "compact.toml"))
    if config.package != expected_package:
        issues.append(AuditIssue("warning", "package-drift", f"project.package is {config.package!r}; normalized slug is {expected_package!r}", "compact.toml"))

    context = build_context(
        config.name,
        config.presets,
        slug=config.slug,
        package_name=config.package,
        generated_at=config.created,
    )
    required_files: list[str] = list(config.required_files)
    rendered_required: set[str] = set()
    for preset in presets:
        for spec in preset.files:
            path = render_path(spec.target, context)
            rendered_required.add(path)
            if path not in required_files:
                required_files.append(path)

    for relative in required_files:
        path = root / relative
        if not path.exists():
            issues.append(AuditIssue("error", "missing-file", f"Missing required file: {relative}", relative))
        elif not path.is_file():
            issues.append(AuditIssue("error", "wrong-type", f"Expected file but found another type: {relative}", relative))
        elif path.stat().st_size <= 1:
            issues.append(AuditIssue("warning", "empty-file", f"Required file is empty: {relative}", relative))
        else:
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                text = ""
            if relative in rendered_required and text and _TOKEN_PATTERN.search(text):
                issues.append(AuditIssue("error", "template-token", f"Unresolved template token in {relative}", relative))

    for relative in config.required_dirs:
        path = root / relative
        if not path.exists():
            issues.append(AuditIssue("error", "missing-dir", f"Missing required directory: {relative}", relative))
        elif not path.is_dir():
            issues.append(AuditIssue("error", "wrong-type", f"Expected directory but found another type: {relative}", relative))

    for path in _iter_files(root):
        rel = path.relative_to(root).as_posix()
        name = path.name
        if name.endswith(_BACKUP_SUFFIXES):
            issues.append(AuditIssue("warning", "backup-artifact", f"Backup artifact should not be committed: {rel}", rel))
        if name in _SECRET_NAMES or path.suffix.lower() in _SECRET_SUFFIXES:
            if name != ".env.example":
                issues.append(AuditIssue("warning", "secret-candidate", f"Potential secret-bearing file: {rel}", rel))

    return AuditResult(root, config, tuple(issues), strict)


def format_audit(result: AuditResult, *, json_output: bool = False) -> str:
    if json_output:
        return json.dumps(result.to_dict(), indent=2, ensure_ascii=False)
    lines = [f"AUDIT: {'OK' if result.ok else 'FAIL'}", f"root: {result.root}"]
    if result.config is not None:
        lines.append(f"project: {result.config.slug}")
        lines.append(f"presets: {', '.join(result.config.presets)}")
    for issue in result.issues:
        lines.append(f"[{issue.level.upper()}] {issue.code}: {issue.message}")
    if not result.issues:
        lines.append("issues: none")
    return "\n".join(lines)

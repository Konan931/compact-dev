from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from pathlib import Path
import platform
import shutil

from compact.config import ConfigError, load_config


@dataclass(frozen=True)
class DoctorCheck:
    status: str
    name: str
    detail: str


def run_doctor(root: Path) -> tuple[DoctorCheck, ...]:
    root = root.expanduser().resolve()
    checks: list[DoctorCheck] = [
        DoctorCheck("ok", "python", platform.python_version()),
        DoctorCheck("ok" if shutil.which("git") else "warning", "git", shutil.which("git") or "not found"),
        DoctorCheck("ok" if shutil.which("gh") else "info", "github-cli", shutil.which("gh") or "not found"),
    ]
    try:
        config = load_config(root)
    except ConfigError as exc:
        checks.append(DoctorCheck("error", "compact-config", str(exc)))
        return tuple(checks)

    checks.append(DoctorCheck("ok", "compact-config", f"schema={config.schema_version}; presets={','.join(config.presets)}"))
    if "vercel" in config.presets:
        vercel = shutil.which("vercel")
        checks.append(DoctorCheck("ok" if vercel else "warning", "vercel-cli", vercel or "not found"))
        linked = (root / ".vercel" / "project.json").is_file()
        checks.append(DoctorCheck("ok" if linked else "info", "vercel-link", "linked" if linked else "not linked (safe for a template)"))
    checks.append(DoctorCheck("ok" if (root / "LICENSE").is_file() else "info", "license", "present" if (root / "LICENSE").is_file() else "not selected"))
    return tuple(checks)


def format_doctor(checks: tuple[DoctorCheck, ...], *, json_output: bool = False) -> str:
    if json_output:
        return json.dumps([asdict(check) for check in checks], indent=2, ensure_ascii=False)
    return "\n".join(f"[{check.status.upper()}] {check.name}: {check.detail}" for check in checks)

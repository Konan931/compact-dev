from __future__ import annotations

import json
from pathlib import Path
import subprocess

from compact.audit import run_audit
from compact.config import ConfigError, load_config


def _git_branch(root: Path) -> str | None:
    try:
        proc = subprocess.run(
            ["git", "-C", str(root), "branch", "--show-current"],
            check=False,
            capture_output=True,
            text=True,
            timeout=3,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    value = proc.stdout.strip()
    return value or None


def status_payload(root: Path) -> dict[str, object]:
    root = root.expanduser().resolve()
    try:
        config = load_config(root)
        project = config.slug
        presets = list(config.presets)
    except ConfigError:
        project = None
        presets = []
    audit = run_audit(root)
    return {
        "root": str(root),
        "project": project,
        "presets": presets,
        "git_branch": _git_branch(root),
        "audit_ok": audit.ok,
        "errors": len(audit.errors),
        "warnings": len(audit.warnings),
    }


def format_status(payload: dict[str, object], *, json_output: bool = False) -> str:
    if json_output:
        return json.dumps(payload, indent=2, ensure_ascii=False)
    return "\n".join(f"{key}: {value}" for key, value in payload.items())

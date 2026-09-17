from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path

from compact.config import load_config


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def write_badge(root: Path) -> Path:
    root = root.expanduser().resolve()
    load_config(root)
    path = root / "badge.json"
    payload = {
        "schemaVersion": 1,
        "label": "last update",
        "message": utc_now_iso(),
        "color": "blue",
    }
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return path

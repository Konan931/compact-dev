#!/usr/bin/env python3
# badge.json generator for shields.io endpoint.
# English-only comments as requested.

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

def main(args: list[str] | None = None) -> int:
    if args is None:
        import sys
        args = sys.argv[1:]

    root = Path(__file__).resolve().parents[3]
    profile_path = root / "profile.json"
    badge_path = root / "badge.json"

    last_update = utc_now_iso()
    try:
        if profile_path.exists():
            prof = json.loads(profile_path.read_text(encoding="utf-8"))
            if isinstance(prof.get("last_update"), str) and prof["last_update"]:
                last_update = prof["last_update"]
    except Exception:
        pass

    badge = {
        "schemaVersion": 1,
        "label": "last update",
        "message": last_update,
        "color": "blue",
    }

    badge_path.write_text(json.dumps(badge, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {badge_path}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

import json
from datetime import datetime

from compact.badge import utc_now_iso


def test_utc_now_iso_format() -> None:
    value = utc_now_iso()
    assert value.endswith("Z")
    datetime.fromisoformat(value.replace("Z", "+00:00"))


def test_badge_payload_shape() -> None:
    message = "2026-02-22T12:00:00Z"
    badge = {
        "schemaVersion": 1,
        "label": "last update",
        "message": message,
        "color": "blue",
    }

    rendered = json.dumps(badge)
    parsed = json.loads(rendered)

    assert parsed["schemaVersion"] == 1
    assert parsed["label"] == "last update"
    assert parsed["message"] == message
    assert parsed["color"] == "blue"

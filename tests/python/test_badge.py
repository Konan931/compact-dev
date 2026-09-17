import json
from pathlib import Path

from compact.badge import write_badge
from compact.init import initialize_project


def test_write_badge(tmp_path: Path) -> None:
    initialize_project(tmp_path, project_name="Badge", preset_names=["base"])
    path = write_badge(tmp_path)
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert payload["schemaVersion"] == 1
    assert payload["label"] == "last update"
    assert payload["message"].endswith("Z")

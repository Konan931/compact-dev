from pathlib import Path

from compact.audit import run_audit
from compact.init import initialize_project


def test_missing_config_fails(tmp_path: Path) -> None:
    result = run_audit(tmp_path)
    assert not result.ok
    assert result.errors[0].code == "config"


def test_backup_artifact_is_warning_and_strict_failure(tmp_path: Path) -> None:
    initialize_project(tmp_path, project_name="Audit", preset_names=["base"])
    (tmp_path / "notes.bak").write_text("old", encoding="utf-8")
    normal = run_audit(tmp_path)
    strict = run_audit(tmp_path, strict=True)
    assert normal.ok
    assert any(issue.code == "backup-artifact" for issue in normal.warnings)
    assert not strict.ok

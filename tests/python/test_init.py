from pathlib import Path

from compact.audit import run_audit
from compact.init import initialize_project


def test_python_cli_generation_is_idempotent(tmp_path: Path) -> None:
    target = tmp_path / "demo"
    first = initialize_project(target, project_name="Demo CLI", preset_names=["python-cli"])
    assert first.ok
    assert (target / "src/demo_cli/cli.py").is_file()
    assert run_audit(target, strict=True).ok

    second = initialize_project(target, project_name="Demo CLI", preset_names=["python-cli"])
    assert second.ok
    assert all(item.state == "unchanged" for item in second.files)


def test_conflict_aborts_before_any_write(tmp_path: Path) -> None:
    target = tmp_path / "existing"
    target.mkdir()
    (target / "README.md").write_text("user content\n", encoding="utf-8")
    result = initialize_project(target, project_name="Existing", preset_names=["base"])
    assert not result.ok
    assert "README.md" in result.conflicts
    assert not (target / "compact.toml").exists()


def test_web_and_vercel_compose(tmp_path: Path) -> None:
    target = tmp_path / "site"
    result = initialize_project(target, project_name="Web Site", preset_names=["web-static", "vercel"])
    assert result.ok
    assert (target / "index.html").is_file()
    assert (target / "vercel.json").is_file()
    assert run_audit(target, strict=True).ok


def test_dry_run_does_not_create_target(tmp_path: Path) -> None:
    target = tmp_path / "dry"
    result = initialize_project(target, project_name="Dry", preset_names=["base"], dry_run=True)
    assert result.ok
    assert not target.exists()

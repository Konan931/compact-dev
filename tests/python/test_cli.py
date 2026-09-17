from pathlib import Path

from compact.cli import main


def test_cli_init_and_audit(tmp_path: Path) -> None:
    target = tmp_path / "cli"
    assert main(["init", str(target), "--name", "CLI Test", "--preset", "python-cli"]) == 0
    assert main(["audit", str(target), "--strict"]) == 0


def test_explicit_target_does_not_discover_parent(tmp_path: Path) -> None:
    parent = tmp_path / "parent"
    assert main(["init", str(parent), "--name", "Parent", "--preset", "base"]) == 0
    child = parent / "child"
    child.mkdir()

    assert main(["audit", str(child)]) == 1
    assert main(["badge", str(child)]) == 2
    assert not (parent / "badge.json").exists()


def test_implicit_target_discovers_parent(tmp_path: Path, monkeypatch) -> None:
    parent = tmp_path / "parent"
    assert main(["init", str(parent), "--name", "Parent", "--preset", "base"]) == 0
    child = parent / "nested" / "deeper"
    child.mkdir(parents=True)
    monkeypatch.chdir(child)
    assert main(["audit", "--strict"]) == 0


def test_presets_command() -> None:
    assert main(["presets", "--json"]) == 0

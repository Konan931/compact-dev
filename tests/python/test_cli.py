from pathlib import Path

from compact.cli import main


def test_cli_init_and_audit(tmp_path: Path) -> None:
    target = tmp_path / "cli"
    assert main(["init", str(target), "--name", "CLI Test", "--preset", "python-cli"]) == 0
    assert main(["audit", str(target), "--strict"]) == 0


def test_presets_command() -> None:
    assert main(["presets", "--json"]) == 0

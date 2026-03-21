from pathlib import Path

from compact.audit import check_exists, check_json


def test_check_exists_ok(tmp_path: Path) -> None:
    required_dirs = [
        "bin",
        "docs",
        "src/python/compact",
        "src/go",
        "src/c",
        "tests/python",
    ]
    required_files = [
        "README.md",
        "profile.json",
        "badge.json",
        "structure.md",
        "pyproject.toml",
        "docs/governance.md",
        "docs/labels.md",
        "tests/python/test_audit.py",
        "tests/python/test_badge.py",
    ]

    for rel in required_dirs:
        (tmp_path / rel).mkdir(parents=True, exist_ok=True)

    for rel in required_files:
        p = tmp_path / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("{}", encoding="utf-8")

    errors = check_exists(tmp_path)
    assert errors == []


def test_check_exists_missing_items(tmp_path: Path) -> None:
    errors = check_exists(tmp_path)
    assert "Missing directory: bin" in errors
    assert "Missing file: README.md" in errors


def test_check_json_ok(tmp_path: Path) -> None:
    p = tmp_path / "profile.json"
    p.write_text('{"name": "Konan"}', encoding="utf-8")

    errors = check_json(tmp_path, "profile.json")
    assert errors == []


def test_check_json_invalid(tmp_path: Path) -> None:
    p = tmp_path / "profile.json"
    p.write_text("{invalid json", encoding="utf-8")

    errors = check_json(tmp_path, "profile.json")
    assert len(errors) == 1
    assert errors[0].startswith("Invalid JSON in profile.json:")


def test_check_json_missing_file_is_ok(tmp_path: Path) -> None:
    errors = check_json(tmp_path, "profile.json")
    assert errors == []

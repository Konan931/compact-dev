from __future__ import annotations

from pathlib import Path

from compact.init import initialize_project
from compact.presets import available_presets, load_preset


def test_available_presets_are_listed():
    names = available_presets()
    assert "base" in names
    assert "python-cli" in names
    assert "web-static" in names
    assert "vercel" in names


def test_load_preset_has_expected_metadata():
    preset = load_preset("python-cli")
    assert preset.name == "python-cli"
    assert preset.description
    assert "base" in preset.depends
    assert preset.files


def test_initialize_project_dry_run_lists_files(tmp_path):
    target = tmp_path / "demo"
    result = initialize_project(
        target,
        project_name="Demo CLI",
        preset_names=["python-cli"],
        dry_run=True,
        force=False,
    )

    assert result.target == str(target)
    assert "python-cli" in result.presets
    assert result.files
    assert not result.conflicts
    assert any(item.relative_path.endswith("pyproject.toml") for item in result.files)


def test_initialize_project_generates_expected_layout(tmp_path):
    target = tmp_path / "demo"
    result = initialize_project(
        target,
        project_name="Demo CLI",
        preset_names=["python-cli"],
        dry_run=False,
        force=False,
    )

    assert result.conflicts == []
    assert target.exists()
    assert (target / "pyproject.toml").exists()
    assert (target / "src").exists()
    assert (target / "src" / "demo_cli").exists()
    assert (target / "tests").exists()
    assert (target / "compact.toml").exists()


def test_initialize_project_reuses_existing_contract(tmp_path):
    target = tmp_path / "demo"
    target.mkdir()
    (target / "compact.toml").write_text(
        """
        schema_version = 1

        [project]
        name = "Legacy Demo"
        slug = "legacy-demo"
        package = "legacy_demo"

        [presets]
        active = ["base"]
        """.strip(),
        encoding="utf-8",
    )

    result = initialize_project(
        target,
        project_name="New Demo",
        preset_names=None,
        dry_run=False,
        force=False,
    )

    assert result.target == str(target)
    assert "base" in result.presets

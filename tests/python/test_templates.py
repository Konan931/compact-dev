import json

import pytest

from compact.templates import build_context, package_name_from_slug, render_path, render_template, slugify


def test_slug_and_package_normalization() -> None:
    assert slugify("Hello, World!") == "hello-world"
    assert package_name_from_slug("hello-world") == "hello_world"
    assert package_name_from_slug("class") == "class_pkg"


def test_context_provides_format_specific_values() -> None:
    name = 'Research "R&D" <Lab>'
    context = build_context(name, ["base"])
    assert json.loads(context["project_name_toml"]) == name
    assert eval(context["project_name_python"]) == name
    assert context["project_name_html"] == "Research &quot;R&amp;D&quot; &lt;Lab&gt;"


def test_render_template_rejects_unknown_token() -> None:
    with pytest.raises(ValueError, match="Unknown template token"):
        render_template("{{ missing }}", {})


def test_render_path_rejects_cross_platform_escape_forms() -> None:
    for candidate in ("../escape", r"..\escape", r"C:\temp\escape", "/absolute"):
        with pytest.raises(ValueError, match="Unsafe template path"):
            render_path(candidate, {})

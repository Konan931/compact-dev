from compact.templates import package_name_from_slug, render_template, slugify


def test_slug_and_package_normalization() -> None:
    assert slugify("Hello, World!") == "hello-world"
    assert package_name_from_slug("hello-world") == "hello_world"


def test_render_template_rejects_unknown_token() -> None:
    try:
        render_template("{{ missing }}", {})
    except ValueError as exc:
        assert "Unknown template token" in str(exc)
    else:
        raise AssertionError("expected ValueError")

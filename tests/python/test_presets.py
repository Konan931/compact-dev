from compact.presets import available_presets, resolve_presets


def test_expected_presets_exist() -> None:
    assert {"base", "python-cli", "web-static", "vercel"}.issubset(set(available_presets()))


def test_dependency_resolution_is_ordered_and_deduplicated() -> None:
    names = [preset.name for preset in resolve_presets(["vercel", "web-static"])]
    assert names == ["base", "vercel", "web-static"]

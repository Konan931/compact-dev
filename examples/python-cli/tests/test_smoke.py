from demo_cli.cli import main


def test_main_smoke(capsys):
    import sys

    sys.argv = ["demo", "--name", "Alex"]
    result = main()
    captured = capsys.readouterr()

    assert result == 0
    assert captured.out.strip() == "Hello, Alex!"

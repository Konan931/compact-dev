import sys
import subprocess
from pathlib import Path


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[1] in {"-h", "--help"}:
        print(
            "Usage: compact <command> [args...]\n\n"
            "Commands:\n"
            "  init\n"
            "  audit\n"
            "  badge"
        )
        return 0 if len(argv) >= 2 else 2

    cmd, *rest = argv[1:]

    if cmd == "init":
        root = Path(__file__).resolve().parents[3]
        script = root / "bin" / "compact-init"
        return subprocess.call([str(script), *rest])

    if cmd == "audit":
        from compact.audit import main as audit_main
        return audit_main(rest)

    if cmd == "badge":
        from compact.badge import main as badge_main
        return badge_main(rest)

    print(f"Unknown command: {cmd}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

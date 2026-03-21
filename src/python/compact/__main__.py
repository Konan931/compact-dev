import subprocess
import sys

from compact.paths import repo_root


def main(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    if not argv or argv[0] in {"-h", "--help"}:
        print(
            "Usage: compact <command> [args...]\n\n"
            "Commands:\n"
            "  init\n"
            "  audit\n"
            "  badge"
        )
        return 0 if argv else 2

    cmd, *rest = argv

    if cmd == "init":
        script = repo_root() / "bin" / "compact-init"
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
    raise SystemExit(main())

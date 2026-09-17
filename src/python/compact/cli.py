from __future__ import annotations

import argparse
import json
import sys

from compact import __version__
from compact.audit import format_audit, run_audit
from compact.badge import write_badge
from compact.doctor import format_doctor, run_doctor
from compact.init import initialize_project
from compact.paths import resolve_project_root, resolve_root
from compact.presets import PresetError, available_presets, load_preset
from compact.status import format_status, status_payload


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="compact", description="Small, auditable project scaffolding and repository checks.")
    parser.add_argument("--version", action="version", version=f"compact-dev {__version__}")
    sub = parser.add_subparsers(dest="command")

    init_parser = sub.add_parser("init", help="Generate a project from composable presets")
    init_parser.add_argument("target", nargs="?", default=".")
    init_parser.add_argument("--name", dest="project_name")
    init_parser.add_argument("--preset", action="append", dest="presets", help="Repeat to compose presets")
    init_parser.add_argument("--dry-run", action="store_true")
    init_parser.add_argument("--force", action="store_true", help="Overwrite conflicting managed files")

    audit_parser = sub.add_parser("audit", help="Validate repository structure and template hygiene")
    audit_parser.add_argument("target", nargs="?")
    audit_parser.add_argument("--strict", action="store_true", help="Treat warnings as failure")
    audit_parser.add_argument("--json", action="store_true", dest="json_output")

    doctor_parser = sub.add_parser("doctor", help="Inspect local tooling and optional integration readiness")
    doctor_parser.add_argument("target", nargs="?")
    doctor_parser.add_argument("--json", action="store_true", dest="json_output")

    status_parser = sub.add_parser("status", help="Emit a compact repository status summary")
    status_parser.add_argument("target", nargs="?")
    status_parser.add_argument("--json", action="store_true", dest="json_output")

    badge_parser = sub.add_parser("badge", help="Refresh badge.json timestamp metadata")
    badge_parser.add_argument("target", nargs="?")

    presets_parser = sub.add_parser("presets", help="List available template presets")
    presets_parser.add_argument("--json", action="store_true", dest="json_output")
    return parser


def _print_init_result(result) -> int:
    print(f"target: {result.target}")
    print(f"presets: {', '.join(result.presets)}")
    for item in result.files:
        print(f"{item.state:>9}  {item.relative_path}")
    if result.conflicts:
        print("No files were written because conflicts were detected.", file=sys.stderr)
        print("Use --dry-run to inspect or --force to replace managed conflicts.", file=sys.stderr)
        return 1
    if result.dry_run:
        print("dry-run: no files written")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not args.command:
        parser.print_help()
        return 2

    try:
        if args.command == "init":
            result = initialize_project(
                resolve_root(args.target),
                project_name=args.project_name,
                preset_names=args.presets,
                dry_run=args.dry_run,
                force=args.force,
            )
            return _print_init_result(result)

        if args.command == "audit":
            root = resolve_project_root(args.target)
            result = run_audit(root, strict=args.strict)
            print(format_audit(result, json_output=args.json_output))
            return 0 if result.ok else 1

        if args.command == "doctor":
            root = resolve_project_root(args.target)
            checks = run_doctor(root)
            print(format_doctor(checks, json_output=args.json_output))
            return 1 if any(check.status == "error" for check in checks) else 0

        if args.command == "status":
            root = resolve_project_root(args.target)
            payload = status_payload(root)
            print(format_status(payload, json_output=args.json_output))
            return 0 if payload["audit_ok"] else 1

        if args.command == "badge":
            root = resolve_project_root(args.target)
            print(f"Wrote {write_badge(root)}")
            return 0

        if args.command == "presets":
            rows = [
                {"name": name, "description": load_preset(name).description, "depends": list(load_preset(name).depends)}
                for name in available_presets()
            ]
            if args.json_output:
                print(json.dumps(rows, indent=2, ensure_ascii=False))
            else:
                for row in rows:
                    deps = ",".join(row["depends"]) or "none"
                    print(f"{row['name']:<12} deps={deps:<12} {row['description']}")
            return 0
    except (PresetError, ValueError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    parser.error(f"Unhandled command: {args.command}")
    return 2

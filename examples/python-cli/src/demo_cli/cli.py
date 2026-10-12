from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="demo", description="A tiny generated CLI example.")
    parser.add_argument("--name", default="world", help="Name to greet")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    print(f"Hello, {args.name}!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

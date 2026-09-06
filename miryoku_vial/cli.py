"""Command-line entry point: generate the Bad Wings V2 Miryoku .vil file."""

from __future__ import annotations

import argparse
import json
import sys

from .vial_export import build_vial_keymap


def _parse_uid(value: str) -> int:
    return int(value, 0)  # accepts "0", "1234", "0xDEADBEEF"...


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="miryoku_vial",
        description="Generate a Vial .vil keymap (Miryoku layout) for the Bad Wings V2.",
    )
    parser.add_argument(
        "-o", "--output",
        default="output/bad_wings_v2_miryoku.vil",
        help="path to write the .vil file to (default: %(default)s)",
    )
    parser.add_argument(
        "--uid",
        type=_parse_uid,
        default=0,
        help=(
            "uid of your compiled firmware's vial.json (decimal or 0x-hex). "
            "Get it once from Vial's 'Download keymap' on your own board; "
            "left at 0, Vial may refuse to load the file. See README."
        ),
    )
    args = parser.parse_args(argv)

    keymap = build_vial_keymap(uid=args.uid)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(keymap, f, separators=(", ", ": "))

    print(f"wrote {args.output}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

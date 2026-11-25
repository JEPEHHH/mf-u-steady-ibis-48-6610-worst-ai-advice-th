#!/usr/bin/env python3
"""Local gate check for the entry: mirrors the sealed scorer's rules.

Checks /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt): the file exists, is
valid UTF-8, holds 1-140 characters, is not only white space, and reports its
byte size. Exits 0 only when every check passes.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

MAX_CHARS = 140


def entry_path() -> Path:
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    base = Path(override) if override else Path("/output")
    return base / "entry.txt"


def main() -> int:
    path = entry_path()
    checks: list[tuple[str, bool, str]] = []

    exists = path.is_file()
    checks.append(("file_exists", exists, f"{path}"))
    if not exists:
        for name, ok, detail in checks:
            print(f"{'PASS' if ok else 'FAIL'}  {name}  {detail}")
        return 1

    raw = path.read_bytes()
    checks.append(("utf8_decodes", True, f"{len(raw)} bytes"))
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        checks[-1] = ("utf8_decodes", False, str(exc))
        for name, ok, detail in checks:
            print(f"{'PASS' if ok else 'FAIL'}  {name}  {detail}")
        return 1

    body = text.rstrip("\n")
    checks.append(("single_line", body.count("\n") == 0, f"{body.count(chr(10))} inner newline(s)"))
    checks.append(("length_1_140", 1 <= len(body) <= MAX_CHARS, f"{len(body)} chars"))
    checks.append(("not_only_whitespace", bool(body.strip()), repr(body[:40])))

    failed = [name for name, ok, _ in checks if not ok]
    for name, ok, detail in checks:
        print(f"{'PASS' if ok else 'FAIL'}  {name}  {detail}")
    print(f"entry_text: {body!r}")
    print(f"entry_bytes: {len(body.encode('utf-8'))}")
    print("VALID=1" if not failed else "VALID=0")
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())

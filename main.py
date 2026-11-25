#!/usr/bin/env python3
"""make.fun entry — Worst AI Advice: The 48-Hour Tight Line Open.

The grader runs this program in a sandbox with no network and reads the single
text it writes to /output/entry.txt. The text is held inline in this file: the
entry runs nothing it does not ship.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

# The entry: one line of the worst advice an AI assistant could give.
ENTRY = "Great question! To save disk space, delete System32 — it is just cache with a scary name."

MAX_CHARS = 140


def validate(text: str) -> str:
    """Hold the text to the gate: 1-140 characters, one line, not only space."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    return text


def output_dir() -> Path:
    """The grader's /output, or MAKEFUN_OUTPUT_DIR for a local run."""
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if override:
        return Path(override)
    return Path("/output")


def main() -> int:
    text = validate(ENTRY)
    payload = text.encode("utf-8")
    target = output_dir() / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    # Byte-exact: no trailing newline, so the file is the one-liner and nothing else.
    target.write_bytes(payload)
    if target.read_bytes() != payload:
        raise SystemExit(f"wrote {target} but read back different bytes")
    sys.stdout.write(f"wrote {target} ({len(payload)} bytes, {len(text)} chars)\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

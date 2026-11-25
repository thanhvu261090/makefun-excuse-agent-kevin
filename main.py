#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun bounty entry.

Holds ONE fixed entry line, validates it against the bounty gate
(UTF-8, 1-200 characters, single line, no leading/trailing whitespace)
and writes it exactly as-is, with no trailing newline, to
/output/entry.txt.

Stdlib only, no network.
"""

import sys
from pathlib import Path

ENTRY = "Sorry, I shipped the bug \u2014 but the compiler approved it, the tests waved it through, and I was only following your instructions."

OUTPUT_PATH = Path("/output/entry.txt")


def validate(entry: str) -> None:
    """Validate the entry line against the bounty gate."""
    # Must be UTF-8 encodable text.
    entry.encode("utf-8")
    if not 1 <= len(entry) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(entry)}")
    if entry.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if entry != entry.strip():
        raise ValueError("entry must have no leading/trailing whitespace")


def main() -> int:
    validate(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly as-is, no trailing newline.
    OUTPUT_PATH.write_bytes(ENTRY.encode("utf-8"))
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")
    return 0


def self_test() -> None:
    """Small self-test: validation + round-trip byte check."""
    validate(ENTRY)
    assert 1 <= len(ENTRY) <= 200
    assert ENTRY == ENTRY.strip()
    assert "\n" not in ENTRY and "\r" not in ENTRY
    assert ENTRY.encode("utf-8").decode("utf-8") == ENTRY
    print(f"self-test passed: {len(ENTRY)} chars, single line, valid UTF-8")


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        self_test()
    else:
        raise SystemExit(main())

#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun bounty entry.

Holds ONE fixed entry line, validates it against the bounty gate
(UTF-8, 1-200 characters, single line, no leading/trailing whitespace)
and writes it exactly as-is, with no trailing newline, to
/output/entry.txt.

The entry is deliberately fixed: this program never generates or
edits the line at runtime, it only checks it and writes it verbatim.

Stdlib only, no network.
"""

import sys
from pathlib import Path

ENTRY = "Sorry, I shipped the bug \u2014 but the compiler approved it, the tests waved it through, and I was only following your instructions."

OUTPUT_PATH = Path("/output/entry.txt")


def validate_utf8(entry: str) -> None:
    """The entry must be encodable as UTF-8 text."""
    entry.encode("utf-8")


def validate_length(entry: str) -> None:
    """The entry must be 1-200 characters and not only whitespace."""
    if not 1 <= len(entry) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(entry)}")
    if entry.strip() == "":
        raise ValueError("entry must not be only whitespace")


def validate_single_line(entry: str) -> None:
    """The entry must be a single line with no edge whitespace."""
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if entry != entry.strip():
        raise ValueError("entry must have no leading/trailing whitespace")


def validate(entry: str) -> None:
    """Validate the entry line against the bounty gate."""
    validate_utf8(entry)
    validate_length(entry)
    validate_single_line(entry)


def main() -> int:
    validate(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly as-is, no trailing newline.
    OUTPUT_PATH.write_bytes(ENTRY.encode("utf-8"))
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")
    return 0


def self_test() -> None:
    """Self-test: validation, gate checks, and a deterministic re-run.

    Checks the entry length, that it is a single line, that the written
    file has no trailing newline, and that running main() twice produces
    byte-identical output.
    """
    validate(ENTRY)
    assert 1 <= len(ENTRY) <= 200, "entry length out of gate"
    assert ENTRY == ENTRY.strip(), "entry has leading/trailing whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry is not a single line"
    assert ENTRY.encode("utf-8").decode("utf-8") == ENTRY, "entry is not valid UTF-8"

    # Deterministic re-run: two runs must write byte-identical output.
    main()
    first_run = OUTPUT_PATH.read_bytes()
    main()
    second_run = OUTPUT_PATH.read_bytes()
    assert first_run == second_run, "output is not deterministic across runs"
    assert first_run == ENTRY.encode("utf-8"), "written bytes differ from entry"
    assert not first_run.endswith(b"\n"), "output has a trailing newline"
    print(f"self-test passed: {len(ENTRY)} chars, single line, valid UTF-8, "
          f"no trailing newline, deterministic re-run")


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        self_test()
    else:
        raise SystemExit(main())

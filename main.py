#!/usr/bin/env python3
"""Two Lines to Your Past Self — make.fun entry.

Writes exactly two lines to /output/entry.txt:
  line 1 — a warning to the writer's past self about one specific moment,
           in a single sentence;
  line 2 — one sentence on why that moment mattered and what changed
           because of it.

The entry must be UTF-8 text of 1-280 characters, not only whitespace,
exactly two lines. This program validates those constraints itself
before writing the file.
"""

import os
import sys

# The entry text. Two lines, each a single sentence.
ENTRY = """Don't say yes when your boss asks you to stay late on your daughter's third birthday, the cake still warm on the kitchen table.
She stopped asking you to come home after that, and you spent the next ten years learning how to be invited back."""


def validate(entry: str) -> None:
    """Check the gate constraints; raise on any violation."""
    if not entry or not entry.strip():
        raise ValueError("entry is empty or whitespace-only")
    if len(entry) > 280:
        raise ValueError(f"entry is {len(entry)} characters, over the 280 limit")
    lines = entry.split("\n")
    if len(lines) != 2:
        raise ValueError(f"entry must be exactly 2 lines, got {len(lines)}")
    for i, line in enumerate(lines, 1):
        if not line.strip():
            raise ValueError(f"line {i} is empty")
        if line.count(".") + line.count("!") + line.count("?") < 1:
            raise ValueError(f"line {i} is not a sentence")
    entry.encode("utf-8")  # must be valid UTF-8


def main() -> int:
    validate(ENTRY)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    # Verify what landed on disk is byte-exactly the intended entry.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "written file differs from ENTRY"
    print(f"Wrote {path}: {len(ENTRY)} characters, {ENTRY.count(chr(10)) + 1} lines")
    print("---")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())

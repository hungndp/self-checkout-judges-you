#!/usr/bin/env python3
"""Self-checkout judges you: one funny remark from a judgmental till.

Writes the entry line deterministically to /output/entry.txt
(or the path in ENTRY_OUTPUT) and prints it.
"""

import os
import sys

# The basket, as the machine sees it: twelve yoghurts, one lonely carrot.
SETUP = "Twelve yoghurts and one carrot."

# The sting, landed last: the carrot escalates.
PUNCH = "The carrot would like to speak to a manager."


def build_line():
    """Join setup and punch into the single entry line."""
    return SETUP + " " + PUNCH


def main():
    line = build_line()
    if not line or len(line) > 200:
        print("entry line invalid", file=sys.stderr)
        return 1
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

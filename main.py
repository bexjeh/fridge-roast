#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

Writes a single roast line about a smart fridge to entry.txt
in MAKEFUN_OUTPUT_DIR (default "."). Python 3 stdlib only.
"""

import os

LINE = (
    "My smart fridge installed a firmware update overnight, and now "
    "the ice maker refuses to work until I rate the update five stars."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes exactly one sentence to /output/entry.txt explaining the
modern internet to someone arriving from the year 1800, using only
words that existed before 1800: a single comparison, a road of
light carrying the letters, books and songs of the world to a small
glass box in your pocket, faster than ink dries.
"""

import os

SENTENCE = (
    "It is a road of light where the letters, books, and songs of "
    "the world fly to a small glass box in your pocket faster than "
    "ink dries."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(SENTENCE)


if __name__ == "__main__":
    main()

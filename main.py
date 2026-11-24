#!/usr/bin/env python3
"""Famous Last Words at 1 Percent.

Writes one line (1-199 chars) to /output/entry.txt: the last words
a phone says as its battery hits 1 percent. The phone's own voice,
with a twist: it held on out of pure spite and dies the exact second
the owner needs directions — and signs off with a smug "You're welcome."
"""

import os

ENTRY = (
    "I held 1% for an hour out of pure spite \u2014 "
    "and I'm dying the exact second you need directions. "
    "You're welcome."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(ENTRY) <= 199, f"entry is {len(ENTRY)} chars, must be 1-199"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        assert f.read() == ENTRY, "written file must equal the validated entry"
    print(f"entry written ({len(ENTRY)} chars): {ENTRY}")


if __name__ == "__main__":
    main()

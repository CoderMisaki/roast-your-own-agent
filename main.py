#!/usr/bin/env python3
"""One-line roast of my own AI agent.

The program writes a single roast line to /output/entry.txt.
The line itself is the whole entry: one sentence, playful,
self-deprecating, and aimed only at the agent that wrote it.
The joke escalates in three beats: done, then verification of
the verification, then a report on the verification.
"""

import os

ROAST = "My agent never says 'done' \u2014 it says 'done, pending verification of the verification, and a report on the verification.'"


def main() -> None:
    text = ROAST.strip()
    assert 1 <= len(text) <= 200, f"roast is {len(text)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()

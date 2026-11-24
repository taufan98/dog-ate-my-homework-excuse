#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse — make.fun entry.

Writes one line, under 200 characters, in which a dog explains why the
homework got eaten. The dog's own voice, with a twist of dog logic:
the homework smelled like bacon, so a taste test was the only
responsible course of action — and once the test failed twice, the
only thing left was to eat the evidence. A dog commits.
"""

import os

EXCUSE = (
    "It smelled faintly of bacon, so I ran a full taste test. "
    "It failed. Twice. I ate the evidence anyway — a dog commits."
)


def main():
    os.makedirs("/output", exist_ok=True)
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text == text.strip() and text, "entry must not be only whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()

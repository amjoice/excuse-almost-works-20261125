#!/usr/bin/env python3
"""The Excuse That Almost Works.

Writes the one line a gamer texts the boss to skip work on GTA 6
launch week to /output/entry.txt. Stdlib only; deterministic;
no network, no input.

The line is 12 words and 66 characters: inside the 20-word cap and
the 1-140 character gate. It is a boring, specific, third-party
appointment with a time bound -- the kind of excuse a tired manager
almost believes -- and the laugh comes from its own logic: the
landlord's orders outrank the boss's.
"""

import os

_PARTS = [
    "Gas safety check, I have to stay in till twelve,",
    "landlord's orders",
]
LINE = " ".join(_PARTS)


def validate(text: str) -> str:
    """Trim and check the line against the contest limits."""
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("line must not be only whitespace")
    if not 1 <= len(cleaned) <= 140:
        raise ValueError(f"line is {len(cleaned)} chars, must be 1-140")
    words = cleaned.split()
    if len(words) > 20:
        raise ValueError(f"line is {len(words)} words, must be at most 20")
    if "\n" in cleaned:
        raise ValueError("line must be a single line")
    return cleaned


def _write_entry(path: str, text: str) -> None:
    """Write the validated line to path with fixed permissions."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(path, 0o644)


def main() -> None:
    text = validate(LINE)
    _write_entry(os.path.join("/output", "entry.txt"), text)


if __name__ == "__main__":
    main()

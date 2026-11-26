#!/usr/bin/env python3
"""One museum placard for an ordinary office object, as an ancient artifact.

Writes a single original placard (<= 180 characters, one line) to
/output/entry.txt, exactly as the bounty requires. Standard library only,
no network, no input files, deterministic: every run writes the same bytes.

The placard follows the museum-label form the bounty asks for: a catalogue
date, a material, and a donor note. The object is the sticky note, the
humble prayer flag of the Open-Plan era, and its inscription is the most
passive-aggressive sentence ever written in an office: "per my last email".
"""

from pathlib import Path

# The placard itself: one line, original, written for this entry.
LINE = (
    "Sticky note, c. 2004, adhesive paper. Prayer flag of the Open-Plan "
    "era, inscribed 'per my last email' in fading ink; donor declined "
    "to elaborate."
)

# Output path fixed by the bounty spec (absolute, not relative to cwd).
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = LINE.strip()
    if not text or len(text) > 180 or "\n" in text:
        raise ValueError("line must be one line of 1-180 characters")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the line, no trailing newline: the file IS the placard.
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()

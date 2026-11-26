"""Write the entry line to the output directory.

Competition: "Invent a Word We Need" on make.fun — invent one new
English word and define it in a single clear line of at most 140
characters. The harness runs `python3 main.py` and reads
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).
"""

import os

LINE = "Tabnado (n.) — the storm of 87 open browser tabs that spins up the moment you try to find the one tab you actually need."
# "Tabnado": tab + tornado. A real gap — every heavy browser user knows
# the feeling, but no word for it exists; the definition lands in one
# reading, and the word is sayable, spellable and memorable.

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # Self-check: the entry must be one non-blank line, at most 140 chars.
    assert LINE.strip(), "entry line must not be blank"
    assert "\n" not in LINE.strip(), "entry line must be a single line"
    assert 1 <= len(LINE) <= 140, "entry line must be 1-140 characters"
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

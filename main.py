"""The Perfect Pickup Line, variant 2.

One ML/engineering mechanism is the romance: garbage collection.
The collector frees memory, and here freeing memory is also letting
go of the past. One mechanism, one turn, no second beat.
"""

import os
from pathlib import Path

ENTRY = (
    "You must be my garbage collector, because every time you're near, "
    "you free the memory I didn't know I was holding onto."
)

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

# The kit gate: /output/entry.txt must be UTF-8 text of 1 to 200
# characters, not only white space, and the line is one line.
MIN_CHARS = 1
MAX_CHARS = 200


def validate(text: str) -> None:
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry must be {MIN_CHARS} to {MAX_CHARS} characters, "
            f"got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")


def main() -> None:
    text = ENTRY
    validate(text)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()

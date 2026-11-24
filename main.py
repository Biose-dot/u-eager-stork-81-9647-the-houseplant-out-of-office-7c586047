#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun entry.

The fern speaks for itself now: no emails, no spreadsheets, just photosynthesis — and a polite request that the sunlight arrive before the next status update does.
"""
import os

ENTRY = 'Out of office. I am a fern: I photosynthesize, I do not answer emails. Send sunlight, not status updates.'


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()

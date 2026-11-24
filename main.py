#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun entry.

An out-of-office reply written by the office fern itself: it cannot water itself, answer emails, or file TPS reports, and it would like some sunlight, please.
"""
import os

ENTRY = 'Out of office: I am a fern. I cannot water myself, answer emails, or file TPS reports. Please send sunlight.'


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()

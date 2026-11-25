#!/usr/bin/env python3
"""Write the entry's single-line roast to /output/entry.txt."""

import os
from pathlib import Path

LINE = (
    "My agent spent 40,000 tokens teaching a Python file to say one sentence, then another "
    "40,000 proving it says the same sentence every time \u2014 the joke, it left unverified."
)


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()

"""Write one short text to the entry file for a make.fun bounty.

Standard library only, no network.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

TEXT = (
    "The waiting-room fish has a name tag on his bowl: Gerald. "
    "Gerald has been dead since Tuesday. The tag is new."
)


def output_dir() -> Path:
    """Where the entry file goes.

    MAKEFUN_OUTPUT_DIR wins; OUTPUT_DIR is the fallback; /output last.
    """
    for variable in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        configured = os.environ.get(variable)
        if configured:
            return Path(configured)
    return Path("/output")


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"text must be 1..280 characters, got {len(TEXT)}"

    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)

    entry = target / "entry.txt"
    entry.write_bytes(TEXT.encode("utf-8"))

    print(f"{len(TEXT)} characters written to {entry}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

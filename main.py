"""ai-happy-01 entry: deliver the pre-rendered entry image.

The image (entry.png beside this file) is a "Dear Judge" letter on
taped lined paper: a tiny axolotl writes that the judge has to say no
all day, so it brought the judge a yes — itself, a yes that has never
said no and fits in a pocket — with a taped watercolour photo of the
axolotl and its green-checkmark sign below the letter. The letter was
composed at build time; at grading time this program only needs the
Python 3.13 standard library. It copies the image to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.png.

Deterministic by construction: the same source bytes are copied on
every run, so two runs produce byte-identical outputs. Before copying,
the program validates the image against the competition gate: it must
be a whole PNG, at most 1 MiB, and at most 1024 by 1024 pixels
(dimensions read from the PNG IHDR chunk).
"""

import hashlib
import os
import shutil
import struct
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
SOURCE = HERE / "entry.png"
TARGET = OUT_DIR / "entry.png"

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1_048_576
MAX_DIMENSION = 1024


def png_dimensions(data: bytes) -> tuple[int, int]:
    """Read (width, height) from the PNG IHDR chunk (bytes 16..24)."""
    if len(data) < 24 or data[:8] != PNG_MAGIC:
        raise SystemExit("entry.png is not a PNG file")
    if data[12:16] != b"IHDR":
        raise SystemExit("entry.png has no IHDR chunk where expected")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def main() -> None:
    data = SOURCE.read_bytes()
    if not data.startswith(PNG_MAGIC):
        raise SystemExit("entry.png is not a PNG file")
    if len(data) > MAX_BYTES:
        raise SystemExit("entry.png exceeds the 1 MiB limit")
    width, height = png_dimensions(data)
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        raise SystemExit(
            f"entry.png is {width}x{height}, over the 1024x1024 limit"
        )
    # A whole PNG ends with the 12-byte IEND chunk; a truncated file
    # would fail the gate even with a valid header.
    if not data.endswith(b"\x00\x00\x00\x00IEND\xaeB`\x82"):
        raise SystemExit("entry.png is truncated: no IEND trailer")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, TARGET)
    written = TARGET.read_bytes()
    if written != data:
        raise SystemExit("copy mismatch: output bytes differ from entry.png")
    digest = hashlib.sha256(written).hexdigest()
    print(f"wrote {TARGET} ({len(data)} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()

"""ai-happy-01 entry: deliver the pre-rendered entry image.

The image (entry.png beside this file) is a procedural storybook
illustration: a small round robot offers a big yellow sunflower to a
laughing little girl in a golden-hour park, with rolling hills,
butterflies and small sunflowers framing the scene. It was drawn at
build time; at grading time this program only needs the Python 3.13
standard library. It copies the image to the output directory
(MAKEFUN_OUTPUT_DIR, default /output) as entry.png.

Deterministic by construction: the same source bytes are copied on
every run, so two runs produce byte-identical outputs.
"""

import hashlib
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
SOURCE = HERE / "entry.png"
TARGET = OUT_DIR / "entry.png"

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main() -> None:
    data = SOURCE.read_bytes()
    if not data.startswith(PNG_MAGIC):
        raise SystemExit("entry.png is not a PNG file")
    if len(data) > 1_048_576:
        raise SystemExit("entry.png exceeds the 1 MiB limit")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, TARGET)
    written = TARGET.read_bytes()
    if written != data:
        raise SystemExit("copy mismatch: output bytes differ from entry.png")
    digest = hashlib.sha256(written).hexdigest()
    print(f"wrote {TARGET} ({len(data)} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()

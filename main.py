#!/usr/bin/env python3
"""ai-excited-01 entry: "The Koi That Outgrew Its Cup".

The repository holds one image, entry.png: a colossal koi bursting out
of a tiny porcelain teacup. This program's whole job is to deliver that
image, byte for byte, to /output/entry.png where the judge reads it.
"""

import shutil
from pathlib import Path

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"


def checked_image_bytes(source: Path) -> bytes:
    """Read the entry image, refusing anything that is not PNG or JPEG."""
    data = source.read_bytes()
    if not (data.startswith(PNG_MAGIC) or data.startswith(JPEG_MAGIC)):
        raise ValueError(f"{source.name} is neither a PNG nor a JPEG image")
    if len(data) > 1_048_576:
        raise ValueError(f"{source.name} is {len(data)} bytes, over the 1 MiB cap")
    return data


def main() -> None:
    source = Path(__file__).resolve().parent / "entry.png"
    target = Path("/output/entry.png")
    data = checked_image_bytes(source)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("wb") as out:
        out.write(data)
    print(f"delivered {target} ({len(data)} bytes)")


if __name__ == "__main__":
    main()

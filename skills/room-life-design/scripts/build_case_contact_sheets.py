#!/usr/bin/env python3
"""Build labeled contact sheets for numbered room-case folders.

The script is deliberately non-destructive: source images are only read. Files
whose extension says JPEG but whose content is HEIF are supported when
``pillow-heif`` is installed.
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

try:
    from pillow_heif import register_heif_opener

    register_heif_opener()
except ImportError:
    pass


IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp", ".heic", ".heif"}


def natural_room_key(path: Path) -> tuple[int, str]:
    return (int(path.name), path.name) if path.name.isdigit() else (10**9, path.name)


def load_font(size: int) -> ImageFont.ImageFont:
    candidates = (
        Path("C:/Windows/Fonts/msyh.ttc"),
        Path("C:/Windows/Fonts/arial.ttf"),
    )
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


def load_rgb(path: Path) -> Image.Image:
    try:
        with Image.open(path) as image:
            return ImageOps.exif_transpose(image).convert("RGB")
    except Exception as exc:
        raise RuntimeError(
            f"Cannot decode {path}. If it is HEIF/HEIC, install pillow-heif."
        ) from exc


def make_tile(path: Path, tile_width: int, tile_height: int) -> Image.Image:
    label_height = 54
    canvas = Image.new("RGB", (tile_width, tile_height + label_height), "white")
    image = load_rgb(path)
    fitted = ImageOps.contain(image, (tile_width, tile_height))
    x = (tile_width - fitted.width) // 2
    y = (tile_height - fitted.height) // 2
    canvas.paste(fitted, (x, y))

    draw = ImageDraw.Draw(canvas)
    font = load_font(24)
    label = path.name
    bbox = draw.textbbox((0, 0), label, font=font)
    draw.text(
        ((tile_width - (bbox[2] - bbox[0])) // 2, tile_height + 12),
        label,
        fill="#222222",
        font=font,
    )
    return canvas


def make_room_sheet(room_dir: Path, output_dir: Path, tile_width: int = 560) -> Path | None:
    image_paths = sorted(
        [p for p in room_dir.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_SUFFIXES],
        key=lambda p: p.name.lower(),
    )
    if not image_paths:
        return None

    tile_height = 680
    columns = 2 if len(image_paths) > 1 else 1
    rows = math.ceil(len(image_paths) / columns)
    header_height = 72
    gap = 20
    sheet_width = columns * tile_width + (columns + 1) * gap
    sheet_height = header_height + rows * (tile_height + 54) + (rows + 1) * gap
    sheet = Image.new("RGB", (sheet_width, sheet_height), "#e9e7e2")

    draw = ImageDraw.Draw(sheet)
    title_font = load_font(34)
    draw.text((gap, 16), f"Room {room_dir.name} · {len(image_paths)} image(s)", fill="#111111", font=title_font)

    for index, path in enumerate(image_paths):
        tile = make_tile(path, tile_width, tile_height)
        row, column = divmod(index, columns)
        x = gap + column * (tile_width + gap)
        y = header_height + gap + row * (tile_height + 54 + gap)
        sheet.paste(tile, (x, y))

    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"room-{int(room_dir.name):02d}.jpg"
    sheet.save(output_path, quality=90, optimize=True)
    return output_path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("case_root", type=Path, help="Folder containing numbered room folders")
    parser.add_argument("output_dir", type=Path, help="Directory for generated contact sheets")
    args = parser.parse_args()

    room_dirs = sorted(
        [p for p in args.case_root.iterdir() if p.is_dir() and p.name.isdigit()],
        key=natural_room_key,
    )
    generated = []
    empty = []
    for room_dir in room_dirs:
        result = make_room_sheet(room_dir, args.output_dir)
        if result is None:
            empty.append(room_dir.name)
        else:
            generated.append(result)

    for path in generated:
        print(path)
    if empty:
        print(f"No images: {', '.join(empty)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""
Batch Image Info - Solution for Exercise 1, Task 10
Author: Claude (Anthropic) for teaching purposes
Note: This code may not be production-ready and is intended for educational use.
Requires: pip install Pillow
"""

import sys
from pathlib import Path
from PIL import Image


def format_size(bytes):
    """Convert bytes to human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes < 1024.0:
            return f"{bytes:.1f} {unit}"
        bytes /= 1024.0
    return f"{bytes:.1f} TB"


def get_image_info(directory, min_width=0, min_height=0):
    """Get dimensions and size info for all images in a directory."""
    dir_path = Path(directory)

    if not dir_path.exists() or not dir_path.is_dir():
        print(f"Error: '{directory}' is not a valid directory")
        return

    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'}
    images = []
    total_size = 0

    print(f"\n{'Filename':<30} {'Dimensions':<15} {'Size':<12} {'Format':<8}")
    print("-" * 75)

    for file_path in sorted(dir_path.iterdir()):
        if not file_path.is_file():
            continue

        if file_path.suffix.lower() not in image_extensions:
            continue

        try:
            with Image.open(file_path) as img:
                width, height = img.size
                format_name = img.format

                # Apply dimension filters
                if width < min_width or height < min_height:
                    continue

                file_size = file_path.stat().st_size
                total_size += file_size

                print(f"{file_path.name:<30} {width:>5}x{height:<8} "
                      f"{format_size(file_size):<12} {format_name:<8}")

                images.append(file_path.name)

        except Exception as e:
            print(f"{file_path.name:<30} [Error: {str(e)[:40]}]")

    print("-" * 75)
    print(f"\nTotal: {len(images)} images using {format_size(total_size)}")

    if min_width > 0 or min_height > 0:
        print(f"Filtered by: min {min_width}x{min_height}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python task10_image_info.py <directory> [min_width] [min_height]")
        sys.exit(1)

    directory = sys.argv[1]
    min_width = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    min_height = int(sys.argv[3]) if len(sys.argv) > 3 else 0

    get_image_info(directory, min_width, min_height)

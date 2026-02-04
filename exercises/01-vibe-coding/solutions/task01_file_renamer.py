#!/usr/bin/env python3
"""
Bulk File Renamer - Solution for Exercise 1, Task 1
Author: Claude (Anthropic) for teaching purposes
Note: This code may not be production-ready and is intended for educational use.
"""

import os
import sys
from pathlib import Path


def rename_files(directory, prefix):
    """Rename all files in directory with prefix and underscores instead of spaces."""
    dir_path = Path(directory)

    if not dir_path.exists():
        print(f"Error: Directory '{directory}' does not exist")
        return

    if not dir_path.is_dir():
        print(f"Error: '{directory}' is not a directory")
        return

    renamed_count = 0

    for item in dir_path.iterdir():
        if not item.is_file():
            continue

        # Check if already has prefix
        if item.name.startswith(prefix + "_"):
            print(f"Skipping (already has prefix): {item.name}")
            continue

        # Create new name: replace spaces with underscores
        new_name = item.name.replace(" ", "_")
        new_name = f"{prefix}_{new_name}"
        new_path = item.parent / new_name

        # Rename the file
        print(f"Renaming: {item.name} -> {new_name}")
        item.rename(new_path)
        renamed_count += 1

    print(f"\nRenamed {renamed_count} file(s)")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python task01_file_renamer.py <directory> <prefix>")
        sys.exit(1)

    directory = sys.argv[1]
    prefix = sys.argv[2]

    rename_files(directory, prefix)

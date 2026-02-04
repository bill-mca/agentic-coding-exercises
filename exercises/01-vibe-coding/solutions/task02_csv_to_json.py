#!/usr/bin/env python3
"""
CSV to JSON Converter - Solution for Exercise 1, Task 2
Author: Claude (Anthropic) for teaching purposes
Note: This code may not be production-ready and is intended for educational use.
"""

import csv
import json
import sys


def convert_value(value):
    """Try to convert value to appropriate type (int, float, or keep as string)."""
    value = value.strip()

    if not value:
        return None

    # Try integer
    try:
        return int(value)
    except ValueError:
        pass

    # Try float
    try:
        return float(value)
    except ValueError:
        pass

    # Keep as string
    return value


def csv_to_json(input_file, output_file):
    """Convert CSV file to JSON array of objects."""
    try:
        with open(input_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)

            # Convert each row, converting values to appropriate types
            data = []
            for row in reader:
                converted_row = {key: convert_value(value) for key, value in row.items()}
                data.append(converted_row)

        # Write JSON output
        with open(output_file, 'w') as jsonfile:
            json.dump(data, jsonfile, indent=2)

        print(f"Successfully converted {len(data)} rows to {output_file}")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found")
    except Exception as e:
        print(f"Error during conversion: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python task02_csv_to_json.py <input.csv> <output.json>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    csv_to_json(input_file, output_file)

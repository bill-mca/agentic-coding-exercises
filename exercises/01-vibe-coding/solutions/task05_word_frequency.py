#!/usr/bin/env python3
"""
Word Frequency Counter - Solution for Exercise 1, Task 5
Author: Claude (Anthropic) for teaching purposes
Note: This code may not be production-ready and is intended for educational use.
"""

import sys
import re
from collections import Counter


# Common stop words to exclude
STOP_WORDS = {
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from',
    'has', 'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the',
    'to', 'was', 'will', 'with', 'the', 'this', 'but', 'they', 'have',
    'had', 'what', 'when', 'where', 'who', 'which', 'why', 'how'
}


def count_words(filename, top_n=10):
    """Count word frequencies in a text file, excluding stop words."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read().lower()

        # Remove punctuation and split into words
        words = re.findall(r'\b[a-z]+\b', text)

        # Filter out stop words
        filtered_words = [word for word in words if word not in STOP_WORDS]

        # Count frequencies
        word_counts = Counter(filtered_words)

        # Get top N words
        top_words = word_counts.most_common(top_n)

        # Display results
        print(f"\nTop {top_n} words in '{filename}':\n")
        print(f"{'Word':<20} {'Count':>8}")
        print("-" * 30)

        for word, count in top_words:
            print(f"{word:<20} {count:>8}")

        print(f"\nTotal unique words: {len(word_counts)}")
        print(f"Total words (excluding stop words): {sum(word_counts.values())}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python task05_word_frequency.py <filename> [top_n]")
        sys.exit(1)

    filename = sys.argv[1]
    top_n = int(sys.argv[2]) if len(sys.argv) > 2 else 10

    count_words(filename, top_n)

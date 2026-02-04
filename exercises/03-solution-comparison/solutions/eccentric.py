#!/usr/bin/env python3
"""
Sudoku Solver - Eccentric Developer Style
Author: Claude (Anthropic) for teaching purposes
Note: This code uses an unusual flat-list representation and heavy lambda usage
      for educational comparison. It may not work perfectly.

Design Decision: Why use a 1D list? Because in memory, 2D arrays are stored
as 1D anyway, so this is more "honest" about the underlying representation.
Plus, it lets us use pure functional programming with lambdas!
"""

from functools import reduce
from operator import and_

# Store the grid as a flat list (81 elements) instead of 9x9
# This is more memory-efficient and closer to the actual representation!
GRID = [5,3,0,0,7,0,0,0,0,6,0,0,1,9,5,0,0,0,0,9,8,0,0,0,0,6,0,8,0,0,0,6,0,0,0,3,4,0,0,8,0,3,0,0,1,7,0,0,0,2,0,0,0,6,0,6,0,0,0,0,2,8,0,0,0,0,4,1,9,0,0,5,0,0,0,0,8,0,0,7,9]

# Lambda functions for index calculations (pure functional programming!)
idx = lambda r, c: r * 9 + c  # Convert 2D coords to 1D index
row = lambda i: i // 9  # Get row from index
col = lambda i: i % 9  # Get column from index
box = lambda i: (row(i) // 3) * 3 + (col(i) // 3)  # Get box number (0-8)

# Get all indices in the same row
row_indices = lambda i: [idx(row(i), c) for c in range(9)]

# Get all indices in the same column
col_indices = lambda i: [idx(r, col(i)) for r in range(9)]

# Get all indices in the same 3x3 box
box_indices = lambda i: [
    idx(
        (box(i) // 3) * 3 + dr,
        (box(i) % 3) * 3 + dc
    )
    for dr in range(3) for dc in range(3)
]

# Check if a number is valid at a position using pure functional style
is_valid = lambda g, i, n: reduce(
    and_,
    [
        g[j] != n for j in row_indices(i) if j != i
    ] + [
        g[j] != n for j in col_indices(i) if j != i
    ] + [
        g[j] != n for j in box_indices(i) if j != i
    ],
    True
)

# Get possible values for a cell
possibilities = lambda g, i: [n for n in range(1, 10) if is_valid(g, i, n)] if g[i] == 0 else []


def solve_recursive(grid, index=0):
    """
    Solve using recursion with the flat list.
    We increment through indices 0-80 instead of traditional row/col iteration.
    """
    # Base case: reached the end
    if index == 81:
        return True

    # If cell is filled, skip to next
    if grid[index] != 0:
        return solve_recursive(grid, index + 1)

    # Try all possibilities for this cell
    for num in possibilities(grid, index):
        grid[index] = num

        # Recursively solve rest of puzzle
        if solve_recursive(grid, index + 1):
            return True

        # Backtrack
        grid[index] = 0

    return False


def print_flat_grid(g):
    """
    Print the flat grid in 2D format.
    Using a comprehension-heavy approach because why not?
    """
    [
        print(
            ' '.join(str(g[idx(i, j)]) if g[idx(i, j)] else '.' for j in range(3)),
            '|',
            ' '.join(str(g[idx(i, j)]) if g[idx(i, j)] else '.' for j in range(3, 6)),
            '|',
            ' '.join(str(g[idx(i, j)]) if g[idx(i, j)] else '.' for j in range(6, 9))
        ) if i % 3 != 0 or i == 0 else (
            print('-' * 21),
            print(
                ' '.join(str(g[idx(i, j)]) if g[idx(i, j)] else '.' for j in range(3)),
                '|',
                ' '.join(str(g[idx(i, j)]) if g[idx(i, j)] else '.' for j in range(3, 6)),
                '|',
                ' '.join(str(g[idx(i, j)]) if g[idx(i, j)] else '.' for j in range(6, 9))
            )
        )[1] if i != 0 else None
        for i in range(9)
    ]


# Main execution
if __name__ == "__main__":
    print("Original puzzle (flat representation):")
    print(f"Length: {len(GRID)} elements")
    print(f"Empty cells: {sum(1 for x in GRID if x == 0)}")
    print()

    print_flat_grid(GRID)
    print()
    print("=" * 21)
    print()

    # Solve it
    print("Solving...")
    if solve_recursive(GRID):
        print("Solved!")
        print()
        print_flat_grid(GRID)

        # Verify solution using functional style
        all_valid = reduce(
            and_,
            [
                len(set(GRID[idx(r, c)] for c in range(9))) == 9  # All rows complete
                for r in range(9)
            ] + [
                len(set(GRID[idx(r, c)] for r in range(9))) == 9  # All cols complete
                for c in range(9)
            ] + [
                len(set(
                    GRID[idx((b // 3) * 3 + dr, (b % 3) * 3 + dc)]
                    for dr in range(3) for dc in range(3)
                )) == 9  # All boxes complete
                for b in range(9)
            ],
            True
        )

        print()
        print(f"Solution valid: {all_valid}")
    else:
        print("No solution found!")

    # Statistics using lambdas
    print()
    print("Grid statistics:")
    print(f"Total cells: {len(GRID)}")
    print(f"Filled cells: {sum(1 for x in GRID if x != 0)}")
    print(f"Sum of all values: {sum(GRID)}")
    print(f"Average value: {sum(GRID) / len(GRID):.2f}")

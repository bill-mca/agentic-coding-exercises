#!/usr/bin/env python3
"""
Sudoku Solver - Solution 4
Author: Claude (Anthropic) for teaching purposes
Note: This code is intentionally written for educational comparison. It may 
not work perfectly.

Design Thesis: 'Pythonic' function-based code that addresses the challenge 
directly.
"""

import sys
import copy
import time
# import json  # not actually used but imported anyway
from typing import List

# Constants
SIZE = 9
BOX_SIZE = 3


def print_grid(grid):
    """Print the sudoku grid with nice formatting."""
    for i in range(SIZE):
        if i % 3 == 0 and i != 0:
            print("------+-------+------")

        row_str = ""
        for j in range(SIZE):
            if j % 3 == 0 and j != 0:
                row_str += "| "
            row_str += str(grid[i][j]) + " "
        print(row_str)


def printGrid(grid):  # inconsistent naming - camelCase vs snake_case
    """Alternative print function - showing grid differently"""
    for row in grid:
        print(row)


def is_valid_in_row(grid, row, num):
    """Check if num is already in the row."""
    for col in range(9):
        if grid[row][col] == num:
            return False
    return True


def is_valid_in_col(grid, col, num):
    """Check if num is already in the column."""
    for row in range(9):
        if grid[row][col] == num:
            return False
    return True


def is_valid_in_box(grid, row, col, num):
    """Check if num is already in the 3x3 box."""
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if grid[box_row + i][box_col + j] == num:
                return False
    return True


def is_valid_placement(grid, row, col, num):
    """Check if we can place num at grid[row][col]."""
    # Check row
    if not is_valid_in_row(grid, row, num):
        return False

    # Check column
    if not is_valid_in_col(grid, col, num):
        return False

    # Check 3x3 box
    if not is_valid_in_box(grid, row, col, num):
        return False

    return True


def find_empty_cell(grid):
    """Find the next empty cell (represented by 0)."""
    for i in range(SIZE):
        for j in range(SIZE):
            if grid[i][j] == 0:
                return (i, j)
    return None


# def find_empty_optimized(grid):
#     # This was supposed to be a more optimized version
#     # but I never finished implementing it
#     pass


def solve_sudoku(grid):
    """
    Main solving function using backtracking.
    Returns True if solved, False otherwise.
    """
    empty = find_empty_cell(grid)

    if empty is None:
        return True  # No empty cells left, puzzle is solved!

    row, col = empty

    # Try digits 1-9
    for num in range(1, 10):
        if is_valid_placement(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            # Backtrack
            grid[row][col] = 0

    return False


def validate_grid(grid):
    """Validate that the initial grid is valid."""
    # Check grid size
    if len(grid) != 9:
        return False

    for row in grid:
        if len(row) != 9:
            return False

    # Check all values are 0-9
    for i in range(9):
        for j in range(9):
            if grid[i][j] < 0 or grid[i][j] > 9:
                return False

    # Check initial state doesn't violate rules
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                num = grid[i][j]
                grid[i][j] = 0  # temporarily remove
                if not is_valid_placement(grid, i, j, num):
                    grid[i][j] = num  # put it back
                    return False
                grid[i][j] = num  # put it back

    return True


def main():
    """Main function to run the solver."""
    # Example puzzle - easy difficulty
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Original Puzzle:")
    print_grid(puzzle)
    print()

    # Validate before solving
    if not validate_grid(puzzle):
        print("ERROR: Invalid puzzle!")
        return

    # Make a copy to preserve original
    puzzle_copy = copy.deepcopy(puzzle)

    # Solve the puzzle
    start_time = time.time()

    if solve_sudoku(puzzle_copy):
        end_time = time.time()
        print("Solved in {:.4f} seconds!".format(end_time - start_time))
        print()
        print("Solution:")
        print_grid(puzzle_copy)
    else:
        print("No solution exists for this puzzle.")


# Some test cases for later
# test_puzzle_1 = [[...]]
# test_puzzle_2 = [[...]]


if __name__ == "__main__":
    main()

    # Additional test case - hard puzzle
    print("\n" + "=" * 40)
    print("Testing with a harder puzzle:")
    print("=" * 40 + "\n")

    hard_puzzle = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 8, 5],
        [0, 0, 1, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 7, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 1, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 7, 3],
        [0, 0, 2, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 9]
    ]

    print("Original Hard Puzzle:")
    print_grid(hard_puzzle)

    if validate_grid(hard_puzzle):
        hard_copy = copy.deepcopy(hard_puzzle)
        start = time.time()

        if solve_sudoku(hard_copy):
            elapsed = time.time() - start
            print("\nSolved hard puzzle in {:.4f} seconds!".format(elapsed))
            print("\nSolution:")
            print_grid(hard_copy)
        else:
            print("\nCouldn't solve the hard puzzle.")
    else:
        print("Hard puzzle is invalid!")

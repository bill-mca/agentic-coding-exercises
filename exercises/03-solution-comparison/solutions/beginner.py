#!/usr/bin/env python3
"""
Sudoku Solver - Beginner Developer Style
Author: Claude (Anthropic) for teaching purposes
Note: This code is intentionally written in a beginner style with
      anti-patterns for educational comparison. It may not work perfectly.
"""

# This is my sudoku solver
# It solves sudoku puzzles using backtracking
# I learned about backtracking from a YouTube video

# The puzzle to solve - this MUST be stored in a variable called 'puzzle'
# and it MUST be 9x9 and it MUST be in this exact format
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

# Print the original puzzle
print("Original puzzle:")
for row in puzzle:
    print(row)
print()  # blank line for readability

# Now I need to solve it
# I'll use a recursive approach
# 0 means empty cell

# First, let me find all the empty cells
empty_cells = []  # this will store tuples of (row, col)
for row_idx in range(9):  # 9 rows
    for col_idx in range(9):  # 9 columns
        if puzzle[row_idx][col_idx] == 0:  # if cell is empty
            empty_cells.append((row_idx, col_idx))  # add to list

print(f"Found {len(empty_cells)} empty cells to fill")
print()

# Now I'll try to fill them one by one
# I need to keep track of which cell I'm working on
current_cell = 0

# I'll keep trying until I solve it or determine it's impossible
solved = False
iterations = 0  # to see how many times we loop

while not solved:
    iterations += 1
    print(f"Iteration {iterations}, working on cell {current_cell}")

    # Check if we've filled all cells
    if current_cell >= len(empty_cells):
        solved = True
        print("SOLVED!")
        break

    # Get the current empty cell position
    row, col = empty_cells[current_cell]

    # Get the current value in that cell
    current_value = puzzle[row][col]

    # Try the next number
    found_valid = False
    for try_num in range(current_value + 1, 10):  # try numbers from current+1 to 9
        # Check if try_num is valid in this position
        valid = True  # assume it's valid until proven otherwise

        # Check the row - make sure try_num isn't already in this row
        for c in range(9):
            if puzzle[row][c] == try_num:
                valid = False
                break

        # Check the column - make sure try_num isn't already in this column
        if valid:  # only check if still valid
            for r in range(9):
                if puzzle[r][col] == try_num:
                    valid = False
                    break

        # Check the 3x3 box - make sure try_num isn't already in the box
        if valid:  # only check if still valid
            # Figure out which box we're in
            box_row_start = (row // 3) * 3
            box_col_start = (col // 3) * 3

            # Check all cells in the box
            for r in range(box_row_start, box_row_start + 3):
                for c in range(box_col_start, box_col_start + 3):
                    if puzzle[r][c] == try_num:
                        valid = False
                        break
                if not valid:
                    break

        # If try_num is valid, use it!
        if valid:
            puzzle[row][col] = try_num
            print(f"  Placed {try_num} at position ({row}, {col})")
            found_valid = True
            current_cell += 1  # move to next cell
            break

    # If we couldn't find a valid number, we need to backtrack
    if not found_valid:
        print(f"  No valid number found, backtracking...")
        puzzle[row][col] = 0  # reset this cell
        current_cell -= 1  # go back to previous cell

        # Safety check - make sure we don't go back before the start
        if current_cell < 0:
            print("ERROR: Can't backtrack anymore! Puzzle has no solution!")
            solved = True  # exit the loop

    # Safety check - prevent infinite loops during development
    if iterations > 100000:
        print("Too many iterations! Something might be wrong...")
        break

print()
print("=" * 50)
print("Final solution:")
print("=" * 50)

# Print the solved puzzle nicely
for i in range(9):
    row_str = ""
    for j in range(9):
        row_str += str(puzzle[i][j]) + " "
        if j == 2 or j == 5:  # add separator after 3rd and 6th column
            row_str += "| "
    print(row_str)
    if i == 2 or i == 5:  # add separator after 3rd and 6th row
        print("-" * 22)

print()
print(f"Total iterations: {iterations}")
print("Done!")

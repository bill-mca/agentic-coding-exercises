# Challenge: Sudoku Solver

## Problem Statement

Implement a Sudoku solver that takes a 9x9 grid (partially filled) and completes it according to Sudoku rules.

## Sudoku Rules

1. Each row must contain the digits 1-9 without repetition
2. Each column must contain the digits 1-9 without repetition
3. Each of the nine 3x3 sub-grids must contain the digits 1-9 without repetition

## Requirements

### Input
- A 9x9 grid represented as a nested list, 2D array, or string
- Empty cells represented by 0 or '.'
- Can read from file, command-line argument, or hardcoded example

**Example input:**
```
5 3 0 | 0 7 0 | 0 0 0
6 0 0 | 1 9 5 | 0 0 0
0 9 8 | 0 0 0 | 0 6 0
------+-------+------
8 0 0 | 0 6 0 | 0 0 3
4 0 0 | 8 0 3 | 0 0 1
7 0 0 | 0 2 0 | 0 0 6
------+-------+------
0 6 0 | 0 0 0 | 2 8 0
0 0 0 | 4 1 9 | 0 0 5
0 0 0 | 0 8 0 | 0 7 9
```

### Output
- The completed 9x9 grid with all cells filled
- Display the grid in a readable format
- If no solution exists, indicate this clearly

**Example output:**
```
5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
------+-------+------
8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
------+-------+------
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9
```

### Core Functionality

1. **Grid Validation**
   - Check that input is valid (correct size, valid digits)
   - Verify the initial grid doesn't violate Sudoku rules

2. **Solving Algorithm**
   - Implement backtracking algorithm to find solution
   - Try placing digits 1-9 in empty cells
   - Check if placement is valid according to Sudoku rules
   - Backtrack if placement leads to no solution
   - Continue until grid is complete

3. **Validity Checking**
   - Check if a number can be placed in a specific cell
   - Verify row constraint
   - Verify column constraint
   - Verify 3x3 box constraint

4. **Grid Display**
   - Print the grid in a human-readable format
   - Show grid lines separating 3x3 boxes
   - Clear distinction between given and solved numbers (optional)

### Optional Enhancements

- Support multiple puzzle difficulties
- Puzzle generation (create valid Sudoku puzzles)
- Step-by-step solution display
- Performance measurement (time to solve)
- Validate that solution is unique
- GUI for interactive solving
- Statistics (number of backtracks)

## Algorithm: Backtracking

The standard approach uses recursive backtracking:

```
function solve(grid):
    find next empty cell
    if no empty cells:
        return True (solved!)

    for digit in 1 to 9:
        if digit is valid in this cell:
            place digit
            if solve(grid):
                return True
            remove digit (backtrack)

    return False (no solution from this state)
```

## Test Cases

Include at least these test cases:

### Easy Puzzle
```
5 3 0 | 0 7 0 | 0 0 0
6 0 0 | 1 9 5 | 0 0 0
0 9 8 | 0 0 0 | 0 6 0
------+-------+------
8 0 0 | 0 6 0 | 0 0 3
4 0 0 | 8 0 3 | 0 0 1
7 0 0 | 0 2 0 | 0 0 6
------+-------+------
0 6 0 | 0 0 0 | 2 8 0
0 0 0 | 4 1 9 | 0 0 5
0 0 0 | 0 8 0 | 0 7 9
```

### Hard Puzzle
```
0 0 0 | 0 0 0 | 0 0 0
0 0 0 | 0 0 3 | 0 8 5
0 0 1 | 0 2 0 | 0 0 0
------+-------+------
0 0 0 | 5 0 7 | 0 0 0
0 0 4 | 0 0 0 | 1 0 0
0 9 0 | 0 0 0 | 0 0 0
------+-------+------
5 0 0 | 0 0 0 | 0 7 3
0 0 2 | 0 1 0 | 0 0 0
0 0 0 | 0 4 0 | 0 0 9
```

### Invalid Puzzle (No Solution)
```
5 3 0 | 0 7 0 | 0 0 0
6 0 0 | 1 9 5 | 0 0 0
0 9 8 | 0 0 0 | 0 6 0
------+-------+------
8 0 0 | 0 6 0 | 0 0 3
4 0 0 | 8 0 3 | 0 0 1
7 0 0 | 0 2 0 | 0 0 6
------+-------+------
0 6 0 | 0 0 0 | 2 8 0
0 0 0 | 4 1 9 | 0 0 5
5 0 0 | 0 8 0 | 0 7 9  # Duplicate 5 in first column
```

## Expected Behavior

- **Valid puzzle:** Display the solved grid
- **Invalid puzzle:** Report error and explain why
- **Unsolvable puzzle:** Report "No solution found"
- **Performance:** Should solve most puzzles in under 1 second

## Success Criteria

A correct implementation should:
1. Solve all valid Sudoku puzzles
2. Correctly identify invalid/unsolvable puzzles
3. Display output in readable format
4. Handle edge cases gracefully
5. Complete within reasonable time

## Notes for Students

This challenge is ideal for comparing different coding styles because:
- The problem is well-defined and understandable
- There's a clear correct/incorrect answer
- The core algorithm is the same across implementations
- Differences emerge in code organization, validation, display, etc.
- It's complex enough to reach ~200 lines in verbose styles
- It's simple enough to understand all implementations

Focus on HOW each solution implements the same logic, not just WHETHER it works.

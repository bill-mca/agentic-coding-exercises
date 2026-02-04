#!/usr/bin/env python3
"""
Sudoku Solver - Enterprise Developer Style
Author: Claude (Anthropic) for teaching purposes
Note: This code is intentionally over-engineered for educational comparison.
      It may not work perfectly.
"""

import logging
import sys
from typing import List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum


class Difficulty(Enum):
    """Enumeration of puzzle difficulty levels."""
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"
    EXPERT = "expert"


@dataclass
class SolverConfig:
    """Configuration for the Sudoku solver."""
    verbose: bool = False
    show_steps: bool = False
    max_iterations: int = 1000000
    timeout_seconds: int = 30


class GridValidator:
    """Validator class for Sudoku grids."""

    @staticmethod
    def validate_dimensions(grid: List[List[int]]) -> bool:
        """Validate that the grid is 9x9."""
        if len(grid) != 9:
            return False
        return all(len(row) == 9 for row in grid)

    @staticmethod
    def validate_values(grid: List[List[int]]) -> bool:
        """Validate that all values are between 0 and 9."""
        for row in grid:
            for value in row:
                if not (0 <= value <= 9):
                    return False
        return True

    @staticmethod
    def validate_initial_state(grid: List[List[int]]) -> bool:
        """Validate that initial grid doesn't violate Sudoku rules."""
        for i in range(9):
            for j in range(9):
                if grid[i][j] != 0:
                    value = grid[i][j]
                    grid[i][j] = 0
                    if not ConstraintChecker.is_valid_placement(grid, i, j, value):
                        grid[i][j] = value
                        return False
                    grid[i][j] = value
        return True


class ConstraintChecker:
    """Checker for Sudoku constraints."""

    @staticmethod
    def is_valid_in_row(grid: List[List[int]], row: int, num: int) -> bool:
        """Check if number is valid in given row."""
        return num not in grid[row]

    @staticmethod
    def is_valid_in_column(grid: List[List[int]], col: int, num: int) -> bool:
        """Check if number is valid in given column."""
        return all(grid[row][col] != num for row in range(9))

    @staticmethod
    def is_valid_in_box(grid: List[List[int]], row: int, col: int, num: int) -> bool:
        """Check if number is valid in the 3x3 box."""
        box_row, box_col = (row // 3) * 3, (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if grid[box_row + i][box_col + j] == num:
                    return False
        return True

    @staticmethod
    def is_valid_placement(grid: List[List[int]], row: int, col: int, num: int) -> bool:
        """Check if placement satisfies all constraints."""
        return (ConstraintChecker.is_valid_in_row(grid, row, num) and
                ConstraintChecker.is_valid_in_column(grid, col, num) and
                ConstraintChecker.is_valid_in_box(grid, row, col, num))


class GridFormatter:
    """Formatter for displaying Sudoku grids."""

    @staticmethod
    def format_grid(grid: List[List[int]]) -> str:
        """Format grid as a pretty string."""
        lines = []
        for i, row in enumerate(grid):
            if i % 3 == 0 and i != 0:
                lines.append("------+-------+------")

            row_parts = []
            for j, val in enumerate(row):
                if j % 3 == 0 and j != 0:
                    row_parts.append("|")
                row_parts.append(str(val) if val != 0 else ".")
            lines.append(" ".join(row_parts))

        return "\n".join(lines)


class SudokuSolver:
    """Main Sudoku solver using backtracking algorithm."""

    def __init__(self, config: SolverConfig = SolverConfig()):
        """Initialize solver with configuration."""
        self.config = config
        self.logger = self._setup_logger()
        self.iteration_count = 0

    def _setup_logger(self) -> logging.Logger:
        """Set up logging configuration."""
        logger = logging.getLogger("SudokuSolver")
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG if self.config.verbose else logging.INFO)
        return logger

    def find_empty_cell(self, grid: List[List[int]]) -> Optional[Tuple[int, int]]:
        """Find the next empty cell in the grid."""
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return (i, j)
        return None

    def solve(self, grid: List[List[int]]) -> bool:
        """
        Solve the Sudoku puzzle using backtracking.

        Args:
            grid: 9x9 list of lists representing the puzzle

        Returns:
            True if solved, False if no solution exists
        """
        self.iteration_count += 1

        if self.iteration_count > self.config.max_iterations:
            self.logger.error("Maximum iterations exceeded")
            return False

        empty = self.find_empty_cell(grid)
        if empty is None:
            self.logger.info("Puzzle solved!")
            return True

        row, col = empty

        for num in range(1, 10):
            if ConstraintChecker.is_valid_placement(grid, row, col, num):
                grid[row][col] = num

                if self.config.show_steps:
                    self.logger.debug(f"Trying {num} at ({row}, {col})")

                if self.solve(grid):
                    return True

                grid[row][col] = 0

                if self.config.show_steps:
                    self.logger.debug(f"Backtracking from ({row}, {col})")

        return False


class SudokuCLI:
    """Command-line interface for the Sudoku solver."""

    def __init__(self):
        """Initialize the CLI."""
        self.running = True

    def display_menu(self):
        """Display the main menu."""
        print("\n" + "=" * 50)
        print("          SUDOKU SOLVER")
        print("=" * 50)
        print("\n1. Solve Example Puzzle (Easy)")
        print("2. Solve Example Puzzle (Hard)")
        print("3. Configure Settings")
        print("4. Exit")
        print("\n" + "=" * 50)

    def run(self):
        """Run the interactive CLI."""
        config = SolverConfig()

        while self.running:
            self.display_menu()
            choice = input("\nEnter your choice (1-4): ").strip()

            if choice == "1":
                self.solve_example(Difficulty.EASY, config)
            elif choice == "2":
                self.solve_example(Difficulty.HARD, config)
            elif choice == "3":
                config = self.configure_settings(config)
            elif choice == "4":
                print("\nThank you for using Sudoku Solver!")
                self.running = False
            else:
                print("Invalid choice. Please try again.")

    def solve_example(self, difficulty: Difficulty, config: SolverConfig):
        """Solve an example puzzle."""
        puzzle = self.get_example_puzzle(difficulty)

        print(f"\n{difficulty.value.upper()} Puzzle:")
        print(GridFormatter.format_grid(puzzle))

        solver = SudokuSolver(config)

        print("\nSolving...")
        if solver.solve(puzzle):
            print("\nSolution:")
            print(GridFormatter.format_grid(puzzle))
            print(f"\nSolved in {solver.iteration_count} iterations")
        else:
            print("\nNo solution found!")

        input("\nPress Enter to continue...")

    def configure_settings(self, config: SolverConfig) -> SolverConfig:
        """Configure solver settings."""
        print("\n--- Settings ---")
        print(f"1. Verbose mode: {config.verbose}")
        print(f"2. Show steps: {config.show_steps}")
        print("3. Back to main menu")

        choice = input("\nSelect setting to toggle (1-3): ").strip()

        if choice == "1":
            config.verbose = not config.verbose
            print(f"Verbose mode: {config.verbose}")
        elif choice == "2":
            config.show_steps = not config.show_steps
            print(f"Show steps: {config.show_steps}")

        return config

    @staticmethod
    def get_example_puzzle(difficulty: Difficulty) -> List[List[int]]:
        """Get an example puzzle of specified difficulty."""
        if difficulty == Difficulty.EASY:
            return [
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
        else:  # HARD
            return [
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


if __name__ == "__main__":
    cli = SudokuCLI()
    cli.run()

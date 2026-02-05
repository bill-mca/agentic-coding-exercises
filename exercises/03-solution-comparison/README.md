# Exercise 3: Solution Comparison and Analysis

## Purpose
Train evaluative skills crucial to agentic coding by analyzing multiple solutions to the same problem.

## Overview
When working with AI agents, you'll encounter many different approaches to solving the same problem. This exercise develops your ability to critically assess code quality, identify trade-offs, and make informed decisions about implementation strategies. You'll analyze five deliberately different solutions to a sudoku solver, each representing a distinct coding style and philosophy.

The sudoku solver challenge is ideal for comparing different coding styles because:
- The problem is well-defined and understandable
- It can be addressed with ~200 lines of code, which is small enough for a human to wrap their head around
- The core algorithm is the same across implementations
- Differences emerge in code organization, validation, display, etc.
- It's simple enough to understand all implementations

Focus on HOW each solution implements the same logic, not just WHETHER it works.

## Learning Objectives
- Evaluate code across multiple quality dimensions (readability, maintainability, performance)
- Identify code smells and anti-patterns
- Understand trade-offs between different implementation approaches
- Recognize when "working code" isn't "good code"
- Practice using AI as a partner for code analysis
- Develop judgment about appropriate complexity levels
- Understand context-dependent notions of "best" solution

## The Challenge

All five solutions solve the same problem: **Sudoku Solver**

- Input: 9x9 grid with some cells filled
- Output: Complete solved grid
- Algorithm: Backtracking

See [`challenge.md`](./challenge.md) for detailed problem specification.

## Analysis Guide

With the help of an AI agent, read each of the solutions and critique them.

Consider asking the AI agent:
- Does the code actually address the challenge?
- Is it well written?
- Who would've written this code and in what context?

## Principles
  
Keep in mind good engineering involves balancing multiple competing factors:

- Readability and maintainability vs. Performance: Sometimes you need highly optimized code (like in gaming engines or real-time systems), but often readable code that's "fast enough" is preferable.
- Conciseness vs. Clarity: Dense code might be shorter, but if it takes significantly longer for team members to understand and modify, it may not be worth it.
- Development Speed vs. Robustness: Rapid prototyping might use quick-and-dirty approaches, while production systems need more rigorous design.
- Flexibility vs. Simplicity: Generalized solutions can handle more cases but are often more complex than specialized ones.

In software engineering striking the "best" solution depends on many contextual factors like:
- Team size and turnover
- Maintenance requirements
- Performance constraints
- Domain (financial systems vs. personal scripts)
- Timeline pressures
- Code lifecycle expectations


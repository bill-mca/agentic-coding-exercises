# Challenge 1: Command-Line Calculator

## Problem Description
Build a command-line calculator that accepts mathematical expressions and returns evaluated results. The calculator should handle standard arithmetic operators and respect order of operations.

## Technical Requirements

### Core Functionality
- Accept expressions as command-line arguments or via interactive mode
- Support operators: `+`, `-`, `*`, `/`, `^` (exponentiation)
- Support parentheses for grouping
- Respect standard order of operations (PEMDAS)
- Handle floating-point and integer arithmetic

### Input/Output
- **Command-line mode:** `calc "2 + 3 * 4"` → `14`
- **Interactive mode:** Launch with no arguments for REPL
- Clear error messages for invalid expressions
- Support multi-line expressions in interactive mode

### Error Handling
- Division by zero
- Mismatched parentheses
- Invalid characters
- Overflow/underflow

### Optional Features
- Variables (e.g., `x = 5`, then `x * 2`)
- Mathematical functions (sin, cos, sqrt, log)
- Expression history in interactive mode

## External Dependencies
- None required (can use standard library)
- Optional: readline library for better interactive experience

## Data Requirements
- No persistent data storage needed
- Optional: Save history to file

## User Interface
- Command-line only
- Interactive REPL mode
- Help command showing available operators

## Performance Requirements
- Instant evaluation for typical expressions
- Handle expressions up to 1000 characters

## Testing Considerations
- Unit tests for expression parsing
- Test order of operations
- Edge cases (empty input, very large numbers)
- Regression tests for common errors

## Deployment
- Single executable or Python script
- Cross-platform (Windows, macOS, Linux)
- No installation beyond Python runtime

## Complexity Factors

**Algorithmic Complexity:** Low to Medium
- Parsing expressions requires understanding of operator precedence
- Implementing a parser (recursive descent or shunting-yard algorithm)

**Integration Complexity:** Very Low
- No external systems
- No network communication

**Domain Knowledge:** Low
- Basic mathematics
- Understanding of parsing/compilers helpful but not required

**Testing Difficulty:** Low
- Deterministic outputs
- Easy to write comprehensive test cases

**Deployment Complexity:** Very Low
- Single file distribution
- No infrastructure needed

## Estimated Effort
**Experienced Developer:** 2-4 hours (basic version), 6-8 hours (with advanced features)
**Team Size:** 1 developer
**AI Suitability:** High - well-defined problem with clear inputs/outputs

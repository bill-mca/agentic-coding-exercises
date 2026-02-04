# Exercise 3: Solution Comparison and Analysis

## Purpose
Train evaluative skills crucial to agentic coding by analyzing multiple solutions to the same problem.

## Overview
When working with AI agents, you'll encounter many different approaches to solving the same problem. This exercise develops your ability to critically assess code quality, identify trade-offs, and make informed decisions about implementation strategies. You'll analyze five deliberately different solutions to a Sudoku solver, each representing a distinct coding style and philosophy.

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

See `challenge.md` for detailed problem specification.

## Your Task: Generate Multiple Solutions

You'll work with your AI agent to create 3-5 different implementations of the Sudoku solver, each in a distinctly different style. The goal is to generate solutions that solve the same problem but demonstrate different coding approaches, quality levels, and trade-offs.

### Suggested Solution Styles

Here are some style archetypes to consider (choose 3-5):

**1. Beginner Style** (~100-150 lines)
- No functions—linear script
- Excessive comments
- Debug print statements
- Hardcoded values
- Works only under specific conditions

**2. Intermediate Style** (~150-200 lines)
- Some functions but inconsistent organization
- Mixed naming conventions
- Code duplication
- Commented-out code
- Works but has technical debt

**3. Clean/Professional Style** (~80-120 lines)
- Well-organized functions
- Clear naming
- Appropriate comments
- Error handling
- Balanced complexity

**4. Genius/Concise Style** (~20-50 lines)
- Hyper-optimized
- Minimal variable names
- Dense logic
- No documentation
- Clever but cryptic

**5. Enterprise/Over-engineered Style** (~200-250 lines)
- Classes and inheritance
- Design patterns
- Logging and config
- Menu system or elaborate UI
- Over-engineered for problem size

**6. Eccentric Style** (~100-150 lines)
- Unusual design choices
- Heavy use of lambdas or recursion
- Non-standard data structures
- "Clever" approaches
- Justified with questionable reasoning

---

## Instructions

### Part 1: Generate Solutions (60-90 minutes)

1. **Read the challenge specification** (`challenge.md`) to understand the problem

2. **Select 3-5 styles** from the suggested archetypes above

3. **Generate each solution with your AI agent:**

   For each style, prompt your AI specifically:
   ```
   "Write a Sudoku solver in Python using a [STYLE] approach. The code should:
   - [List specific characteristics of that style]
   - Be approximately [X] lines long
   - Demonstrate [specific anti-patterns or patterns]

   Here's the problem specification: [paste challenge.md]"
   ```

4. **Save each solution** in a `solutions/` directory with clear filenames:
   - `beginner.py`
   - `intermediate.py`
   - `clean.py`
   - `genius.py`
   - `enterprise.py`
   - etc.

5. **Test each solution:**
   - Run them with the test cases from `challenge.md`
   - Verify they produce correct output
   - Note which ones actually work

### Part 2: Initial Comparison (30 minutes)

6. **Review all your generated solutions:**
   - Read through each one
   - Note your initial impressions
   - Which looks most appealing?
   - Which looks most problematic?

7. **Create a comparison table:**
   | Solution | Lines | Works? | First Impression |
   |----------|-------|--------|------------------|
   | Beginner | 136 | Yes | Too many comments |
   | ... | ... | ... | ... |

### Part 3: Deep Analysis with AI (90-120 minutes)

8. **Analyze each solution systematically:**
   ```
   "Let's analyze this [Style] Sudoku solver. Evaluate it across these
   dimensions: readability, maintainability, performance, correctness,
   extensibility, and testability. What are its strengths and weaknesses?"
   ```

9. **Drill into specifics:**
   - Ask the AI to identify code smells
   - Discuss trade-offs in design decisions
   - Compare your assessment with AI's assessment
   - Challenge the AI's conclusions

### Part 3: Comparative Analysis (45-60 minutes)

9. **Use the analysis guide** (`analysis-guide.md`) to structure comparison

10. **Create a comparison matrix:**
    - Rate each solution on key dimensions
    - Identify strengths and weaknesses
    - Note which contexts favor which solution

11. **Discuss with AI:**
    - "Which solution is best for a startup with 3 developers?"
    - "Which would you use for a one-time script?"
    - "Which would you want in a production library?"
    - "Which could an AI generate most easily?"

### Part 4: Synthesis (30-45 minutes)

12. **Write your reflection addressing:**
    - What makes code "good" vs. "working"?
    - How does context affect what's appropriate?
    - What surprised you in the analysis?
    - How would you approach this problem?

13. **Optional: Write your own solution**
    - Take the best ideas from all five
    - Implement your ideal version
    - Ask AI to critique it

## Discussion Prompts for AI

Use these to guide your analysis sessions:

### Understanding Trade-offs
- "What does the Beginner solution get right despite its issues?"
- "When would the Genius solution's brevity be valuable?"
- "Is the Enterprise solution over-engineered, or appropriately structured?"

### Comparing Approaches
- "Compare how Intermediate and Genius handle validation. Which is better?"
- "What's the key difference between Enterprise and Eccentric over-engineering?"
- "Which two solutions are most similar in spirit?"

### Context and Judgment
- "In what scenario would you choose the Beginner approach?"
- "How much documentation is enough?"
- "When does abstraction clarify vs. obscure?"

### AI Collaboration
- "If I asked you to write a Sudoku solver, which style would you default to?"
- "How would you prevent an AI from generating the Beginner solution?"
- "What prompts would lead to each of these styles?"

## Tips for Success

### Analyzing Code
- Look beyond whether it works—consider how it works
- Consider the full lifecycle: writing, reading, modifying, debugging
- Think about team dynamics: could others contribute?
- Remember: complexity has a cost

### Working with AI
- The AI can explain any code—ask for clarification
- Push back on AI judgments—develop your own perspective
- Use AI to explore "what if": "What if we simplified this class?"
- Ask for concrete examples: "Show me a specific improvement"

### Developing Judgment
- There's rarely one "best" solution
- Context matters more than absolutes
- Your preferences will evolve with experience
- Good code often feels "boring"—that's okay!

## Common Insights

Students typically discover:

1. **Structure matters more than you think** - The Beginner solution's lack of organization causes cascading problems

2. **Brevity isn't clarity** - The Genius solution is impressively short but impossible to maintain

3. **Over-engineering is real** - Both Enterprise and Eccentric show how good intentions create complexity

4. **Consistency trumps perfection** - The Intermediate solution's inconsistency causes more issues than its individual choices

5. **"Working" and "good" are different** - All solutions work, but maintainability varies wildly

6. **Context is everything** - The "best" solution depends entirely on circumstances

## Time Estimate

- **Total exercise:** 3-4.5 hours
- Can be split across multiple sessions
- Part 2 is the most time-intensive

## Reference Solutions

After completing your own implementations and analysis, you can compare with reference solutions available in the `solutions` branch of this repository:

```bash
git checkout solutions
```

The solutions branch contains 5 example implementations demonstrating different coding styles. Use these to:
- Compare your AI-generated solutions with reference examples
- See how different prompts led to different implementations
- Validate your analysis and insights
- Explore additional code patterns

**Important:** Only look at reference solutions AFTER you've completed your own analysis. The learning comes from generating and evaluating solutions yourself.

## Extension Activities

### For individuals:
- Implement your ideal solution
- Refactor one solution to improve it
- Add features (puzzle generation, difficulty rating)
- Write tests for all solutions

### For groups:
- Debate which solution is "best"
- Each person champions a different solution
- Vote on which you'd want in your codebase
- Collaborative refactoring exercise

## Next Steps

After completing this exercise:
- You'll have developed critical code evaluation skills
- You'll better understand trade-offs in software design
- You'll be able to guide AI agents toward appropriate solutions
- You'll recognize code smells in AI-generated code
- Move on to Exercise 4 to practice documentation and dealing with limitations

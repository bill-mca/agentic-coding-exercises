# Questions Before Implementation

Before implementing exercises 1-4, I need clarification on the following:

## Exercise 1: Vibe Coding

### Q1.1: Automation task domains
The backlog mentions "automation tasks" - which domains are most relevant for your teaching context?
- File/directory management
- Text/log file processing
- API interactions
- System automation (process management, etc.)
- Data format conversions
- Other specific domains?

### Q1.2: Language preference
Should all trivial tasks be designed to be solved in Python, or would you like some tasks that are better suited to other languages (bash, JavaScript, etc.)?

All python. please update the readme to add this context. we're using python as a tool to teach agentic coding

## Exercise 2: Difficulty Assessment

### Q2.1: Student background
What level of programming experience should I assume for the target students?
- Beginner programmers (1-2 years experience)
- Intermediate (3-5 years)
- Advanced (5+ years)
- Mixed levels

There's a mix of levels so you can't really make assumptions. Be wary of lowest-common-denominator mindset but make it so that beginners aren't overwhelmed. I'm thinking that 


### Q2.2: Domain coverage
Should the challenges emphasize certain domains over others? The backlog mentions: web, CLI, data, systems, ML, games. Are all equally important, or should I weight toward specific areas?

## Exercise 3: Solution Comparison

### Q3.1: Challenge selection
For the code comparison exercise, what type of problem would be most pedagogically useful?

Options I'm considering:
- **Data processing**: CSV/JSON file parser and transformer
- **API client**: Wrapper for a REST API with request handling
- **Game logic**: Simple text-based game (e.g., Wordle clone, Hangman)
- **Validation**: Input validator with multiple rules and error reporting
- **Algorithm**: Implementation of a specific algorithm (e.g., pathfinding, text search)

Do an algorithm.
A sudoku solver would be awesome. 
The overly verbose examples should be in the realm of 200 lines of code


### Q3.2: Solution length target
The backlog says 50-200 lines. Should I aim for the shorter or longer end of this range? Shorter makes comparison easier, longer allows for more architectural differences.

Use your creativity. some of the examples 

## Exercise 4: Exploring and Failing

### Q4.1: Failure mode emphasis
What type of limitations should the ambitious projects emphasize?
- Technical limitations (AI can't solve the algorithmic complexity)
- Context limitations (project too large, exceeds token budget)
- Integration limitations (external APIs, hardware, etc.)
- Testing/verification limitations (AI can't verify complex behavior)
- All of the above?

None of the above! Let the students find these out and then learn from each others experience in a group reflection. Maybe have a footnote somewhere that suggests the ways that things can go wrong.

### Q4.2: Domain preference
The backlog lists: ML projects, systems projects, game development, reverse engineering, hardware integration. Should I provide roughly equal coverage or emphasize certain domains?
yep

## General Questions

### Q5.1: Commit frequency
Should I commit after completing each exercise (4 commits total), after each major task, or all at once at the end?

after each exercise.

### Q5.2: Testing requirements
Should I include actual test files with assertions for the code examples, or are comments indicating "this should work" sufficient for teaching materials?

no tests. Just write a comment near the top indicating that it was authored by you for teaching purposes and that it might not work.

### Q5.3: README files
Should each exercise subdirectory have its own README explaining setup and usage, or is the main exercises/README.md sufficient?

yes. Write a readme for each exercise. The project readme need only have a brief overview of what the exercise is about.

---


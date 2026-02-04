# Backlog: Agentic Coding Teaching Materials

This backlog contains all tasks required to create the code and materials for the agentic coding teaching exercises.

---

## Exercise 1: Vibe Coding

### Task 1.1: Create trivial coding tasks list
- [ ] **Status:** Not started
- **Description:** Create a document listing 10-15 trivial coding tasks suitable for single-pass AI solutions. Each task should be completable in under 5 minutes with a clear, unambiguous specification.
- **Output:** `exercises/01-vibe-coding/tasks.md`
- **Requirements:**
  - Tasks should cover different domains (string manipulation, file I/O, data transformation, simple algorithms)
  - Each task needs: title, description, example input/output, success criteria
  - Tasks should be language-agnostic where possible
  - Include a mix of: utility scripts, data processing, automation tasks
- **Example tasks to include:**
  - Rename files in a directory according to a pattern
  - Convert CSV to JSON
  - Find duplicate lines in a file
  - Generate a random password
  - Count word frequencies in a text file

### Task 1.2: Create sample solutions for trivial tasks
- [ ] **Status:** Not started
- **Description:** Provide reference solutions in Python for each trivial task to verify AI-generated solutions work correctly.
- **Output:** `exercises/01-vibe-coding/solutions/`
- **Requirements:**
  - One solution file per task
  - Include test data where applicable
  - Solutions should be clean and idiomatic

---

## Exercise 2: Difficulty Assessment

### Task 2.1: Create software development challenges list
- [ ] **Status:** Not started
- **Description:** Create a comprehensive list of 15-20 software development challenges spanning a wide range of complexity levels.
- **Output:** `exercises/02-difficulty-assessment/challenges.md`
- **Requirements:**
  - Challenges must span from trivial (1-hour tasks) to extremely complex (multi-month projects)
  - Each challenge needs sufficient detail for students to reason about resource requirements
  - Include challenges from different domains: web, CLI, data, systems, ML, games

### Task 2.2: Write detailed challenge specifications
- [ ] **Status:** Not started
- **Description:** For each challenge, write a detailed specification that enables students to reason about complexity.
- **Output:** `exercises/02-difficulty-assessment/specifications/`
- **Requirements:**
  - Each specification should include:
    - Problem description and goals
    - Technical requirements and constraints
    - External dependencies (APIs, libraries, hardware)
    - Data requirements
    - User interface requirements
    - Performance requirements
    - Testing requirements
    - Deployment considerations
  - Do NOT include difficulty ratings (students should derive these)
  - Include enough detail to estimate: team size, timeline, technical risks

### Task 2.3: Create difficulty assessment rubric
- [ ] **Status:** Not started
- **Description:** Create a rubric/framework students can use to assess challenge difficulty.
- **Output:** `exercises/02-difficulty-assessment/rubric.md`
- **Requirements:**
  - Dimensions to evaluate: algorithmic complexity, integration complexity, domain knowledge required, testing difficulty, deployment complexity
  - Guidance on how AI suitability correlates with different dimensions
  - Examples of how to apply the rubric

---

## Exercise 3: Solution Comparison and Analysis

### Task 3.1: Select a coding challenge for comparison exercise
- [ ] **Status:** Not started
- **Description:** Choose a coding challenge that is complex enough to have meaningfully different solutions but simple enough to be fully comprehensible.
- **Output:** `exercises/03-solution-comparison/challenge.md`
- **Requirements:**
  - Challenge should be solvable in 50-200 lines of code
  - Multiple valid architectural approaches should exist
  - Good candidates: file parser, data validator, simple game, API client wrapper
  - Document the challenge with clear requirements

### Task 3.2: Create "Intermediate Developer" solution
- [ ] **Status:** Not started
- **Description:** Write a solution that exhibits intermediate developer anti-patterns.
- **Output:** `exercises/03-solution-comparison/solutions/intermediate.py`
- **Requirements:**
  - Code duplication in multiple places
  - Inconsistent style (mixed naming conventions, inconsistent spacing)
  - Unnecessary imports that aren't used
  - Mix of functions and inline code in `if __name__ == "__main__"` block
  - Commented-out code blocks "for later"
  - Works correctly but is messy
  - Include inline comments explaining what the "developer" was thinking

### Task 3.3: Create "Beginner Developer" solution
- [ ] **Status:** Not started
- **Description:** Write a solution that exhibits beginner developer patterns.
- **Output:** `exercises/03-solution-comparison/solutions/beginner.py`
- **Requirements:**
  - No functions, just a linear script
  - Hardcoded assumptions (expects specific filename in same directory)
  - Excessive comments explaining obvious things
  - Many print statements for debugging left in
  - Brittle - breaks spectacularly with unexpected input
  - Works only under very specific conditions

### Task 3.4: Create "Genius Developer" solution
- [ ] **Status:** Not started
- **Description:** Write a hyper-optimised, elegant but cryptic solution.
- **Output:** `exercises/03-solution-comparison/solutions/genius.py`
- **Requirements:**
  - Extremely concise and efficient
  - Clever use of language features (comprehensions, lambdas, itertools)
  - Single-letter or very short variable names
  - No comments or documentation
  - Minimal error handling
  - Correct and performant, but hard to read
  - Would take significant effort for others to understand or modify

### Task 3.5: Create "Enterprise Developer" solution
- [ ] **Status:** Not started
- **Description:** Write an over-engineered solution with unnecessary infrastructure.
- **Output:** `exercises/03-solution-comparison/solutions/enterprise.py`
- **Requirements:**
  - Core functionality is well-implemented
  - Wrapped in an elaborate text-based UI/menu system
  - Possibly includes: logging framework, config file parsing, plugin architecture
  - Good practices applied but scope creep is evident
  - Maintenance burden far exceeds the problem complexity
  - Comments and documentation are thorough

### Task 3.6: Create "Eccentric Developer" solution
- [ ] **Status:** Not started
- **Description:** Write a solution that makes an unusual or unreasonable engineering choice.
- **Output:** `exercises/03-solution-comparison/solutions/eccentric.py`
- **Requirements:**
  - Choose an eccentric approach, such as:
    - Everything in a single massive regex
    - Recursive solution where iteration would be simpler
    - Using a database for a problem that doesn't need persistence
    - Implementing from scratch something that has a standard library solution
    - Async/concurrent solution for a clearly sequential problem
  - The solution should work but prompt discussion about trade-offs
  - Include a comment "explaining" the choice in-character

### Task 3.7: Create analysis guide
- [ ] **Status:** Not started
- **Description:** Create a guide for facilitators/students on how to analyse and compare the solutions.
- **Output:** `exercises/03-solution-comparison/analysis-guide.md`
- **Requirements:**
  - Questions to consider for each solution
  - Framework for evaluating: readability, maintainability, performance, correctness, extensibility
  - Discussion prompts about trade-offs
  - Notes on what each solution teaches about code quality

---

## Exercise 4: Exploring and Failing

### Task 4.1: Expand ambitious project ideas
- [ ] **Status:** Not started
- **Description:** Create a list of intentionally overambitious project ideas with enough detail to get students started.
- **Output:** `exercises/04-exploring-failing/ambitious-projects.md`
- **Requirements:**
  - 8-10 project ideas that are likely to hit limitations
  - Each idea should include:
    - Project description
    - Why it's interesting
    - What makes it ambitious
    - Suggested starting point
    - What kind of limitations students might encounter
  - Mix of: ML projects, systems projects, game development, reverse engineering, hardware integration
  - Make clear students can pursue their own ideas

### Task 4.2: Create progress documentation template
- [ ] **Status:** Not started
- **Description:** Create templates for documenting progress on ambitious projects.
- **Output:** `exercises/04-exploring-failing/templates/`
- **Requirements:**
  - `PROGRESS.md` template for tracking daily/session progress
  - `DECISIONS.md` template for documenting architectural decisions
  - `BLOCKERS.md` template for documenting issues and limitations
  - `RETROSPECTIVE.md` template for final reflection
  - Templates should prompt students to capture useful information for learning

---

## Exercise 5: Branching Architecture

### Task 5.1: Design core algorithm for branching exercise
- [ ] **Status:** Not started
- **Description:** Design a core algorithm/library that can support two meaningfully different applications.
- **Output:** `exercises/05-branching-architecture/design.md`
- **Requirements:**
  - Algorithm should be interesting but not trivial (50-150 lines)
  - Should have clear interfaces that different front-ends can use
  - Good candidates:
    - Text analysis library (can become CLI tool or web API)
    - Game logic engine (can become terminal game or GUI game)
    - Data transformation library (can become CLI pipeline or web service)
    - Calculation engine (can become calculator app or API)
  - Document the algorithm design and interfaces

### Task 5.2: Implement core algorithm on main branch
- [ ] **Status:** Not started
- **Description:** Implement the core algorithm with clean interfaces.
- **Output:** `exercises/05-branching-architecture/starter-repo/`
- **Requirements:**
  - Create a starter repository structure
  - Implement core algorithm with:
    - Clean API/interface
    - Unit tests
    - Documentation
  - No application layer yet - just the core
  - Include README explaining the exercise

### Task 5.3: Document branching exercise instructions
- [ ] **Status:** Not started
- **Description:** Write detailed instructions for the branching exercise.
- **Output:** `exercises/05-branching-architecture/instructions.md`
- **Requirements:**
  - Step-by-step guide for creating branches
  - Description of two different applications to build
  - Guidance on maintaining shared code
  - Reflection prompts about context engineering and version management

---

## Exercise 6: Sandbox Acceleration

### Task 6.1: Create programming exercise set for token efficiency
- [ ] **Status:** Not started
- **Description:** Create a set of 20-30 programming exercises designed to test token efficiency.
- **Output:** `exercises/06-sandbox-acceleration/exercises.md`
- **Requirements:**
  - Exercises should vary in:
    - Complexity (some quick, some involved)
    - Token cost (some need lots of context, some are self-contained)
    - Domain (algorithms, file processing, API work, data structures)
  - Each exercise should have:
    - Clear specification
    - Test cases for verification
    - Estimated relative token cost (low/medium/high)
  - Include a scoring system for the challenge

### Task 6.2: Create token tracking guide
- [ ] **Status:** Not started
- **Description:** Create a guide on tracking and optimising token usage.
- **Output:** `exercises/06-sandbox-acceleration/token-guide.md`
- **Requirements:**
  - Explanation of how tokens work in different AI systems
  - Strategies for reducing token usage
  - How to measure token consumption
  - Trade-offs between token efficiency and solution quality

---

## Exercise 7: CPS Development with AI

### Task 7.1: Create Raspberry Pi project specifications
- [ ] **Status:** Not started
- **Description:** Define 3-4 Raspberry Pi projects suitable for AI-assisted development.
- **Output:** `exercises/07-cps-development/projects.md`
- **Requirements:**
  - Projects should require physical components (LEDs, sensors, motors)
  - Varying complexity levels
  - Each project needs:
    - Hardware requirements list
    - Wiring diagram or description
    - Functional requirements
    - Success criteria that require physical observation
  - Include at least one project that could extend to Arduino

### Task 7.2: Create SSH setup guide
- [ ] **Status:** Not started
- **Description:** Write a guide for setting up SSH access for AI agents.
- **Output:** `exercises/07-cps-development/ssh-setup.md`
- **Requirements:**
  - Step-by-step SSH configuration
  - Security considerations
  - How to give AI agent SSH access safely
  - Troubleshooting common issues

### Task 7.3: Create human-in-the-loop protocol
- [ ] **Status:** Not started
- **Description:** Document the protocol for human feedback during CPS development.
- **Output:** `exercises/07-cps-development/feedback-protocol.md`
- **Requirements:**
  - How to report physical observations to the AI
  - Template phrases for common scenarios
  - When and how to intervene
  - Documentation practices during development

---

## Exercise 8: Red Team

### Task 8.1: Design docker network for cyberwar gaming
- [ ] **Status:** Not started
- **Description:** Design a docker network topology for the red team exercise.
- **Output:** `exercises/08-red-team/network-design.md`
- **Requirements:**
  - Multiple containers with different roles (web server, database, mail server, etc.)
  - Intentional vulnerabilities at varying difficulty levels
  - Isolated from host network
  - Easy to reset/rebuild
  - Document the topology and intentional vulnerabilities (for instructor use)

### Task 8.2: Create docker-compose configuration
- [ ] **Status:** Not started
- **Description:** Implement the docker network as a docker-compose configuration.
- **Output:** `exercises/08-red-team/docker-compose.yml` and supporting files
- **Requirements:**
  - All containers defined in docker-compose
  - Custom Dockerfiles where needed
  - Setup scripts for initial configuration
  - Reset/cleanup scripts
  - Minimal resource requirements

### Task 8.3: Create red team exercise guide
- [ ] **Status:** Not started
- **Description:** Write the exercise guide for the red team challenge.
- **Output:** `exercises/08-red-team/exercise-guide.md`
- **Requirements:**
  - Setup instructions
  - Rules of engagement
  - Objectives for the AI/attacker team
  - Guidance for the human defender team
  - Scoring or success criteria
  - Safety reminders and ethical guidelines

### Task 8.4: Create defender playbook
- [ ] **Status:** Not started
- **Description:** Create resources for the human defender team.
- **Output:** `exercises/08-red-team/defender-playbook.md`
- **Requirements:**
  - Monitoring tools and commands
  - Common defensive techniques
  - Log locations and analysis tips
  - Incident response procedures
  - No AI tool usage allowed - humans only

---

## General Tasks

### Task G.1: Create exercise directory structure
- [ ] **Status:** Not started
- **Description:** Set up the directory structure for all exercises.
- **Output:** `exercises/` directory tree
- **Requirements:**
  - Create all necessary directories
  - Add placeholder README in each exercise folder
  - Consistent structure across exercises

### Task G.2: Create main exercises index
- [ ] **Status:** Not started
- **Description:** Create an index document linking to all exercises.
- **Output:** `exercises/README.md`
- **Requirements:**
  - Overview of all exercises
  - Prerequisites for each
  - Suggested order
  - Time estimates
  - Links to each exercise

---

## Task Dependencies

```
G.1 → All other tasks (directory structure first)

1.1 → 1.2 (need tasks before solutions)

2.1 → 2.2 (need challenges before specifications)
2.1, 2.2 → 2.3 (rubric references challenges)

3.1 → 3.2, 3.3, 3.4, 3.5, 3.6 (need challenge before solutions)
3.2, 3.3, 3.4, 3.5, 3.6 → 3.7 (analysis guide references solutions)

4.1 → 4.2 (templates reference project types)

5.1 → 5.2 (design before implementation)
5.2 → 5.3 (instructions reference implementation)

6.1 → 6.2 (guide references exercises)

7.1 → 7.2, 7.3 (projects define context for guides)

8.1 → 8.2 (design before implementation)
8.2 → 8.3, 8.4 (guides reference implementation)

All tasks → G.2 (index created last)
```

---

## Notes for Implementing Agent

1. **Language choice:** Default to Python for code examples unless another language is more appropriate for the specific exercise.

2. **Quality standards:** All code should be functional and tested. Include appropriate error handling in reference solutions.

3. **Documentation:** Every file should have a header comment explaining its purpose and how it fits into the exercise.

4. **Consistency:** Follow the same formatting and style conventions across all exercises.

5. **Student-friendly:** Remember these materials are for learning. Include helpful comments and clear explanations where appropriate.

6. **Ethical considerations:** Exercise 8 (Red Team) requires careful handling. All vulnerabilities should be well-documented and the exercise should emphasise ethical hacking principles.

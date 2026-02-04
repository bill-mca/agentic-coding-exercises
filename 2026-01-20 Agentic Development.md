# Agentic Coding using LLMs

## Principles

1. **Human-led design and critique** — AI serves as an assistant, not the primary decision-maker
2. **Plan before coding** — Establish clear objectives and architecture before implementation
3. **Write the rules** — Give your AI agents a set of rules appropriate to the context - the less human oversight needed, the faster you will code
4. **Session-based project structure** — Break work into manageable, focused sessions
5. **Task-appropriate tooling** — Select the right AI agent for each job
6. **Recognise limitations** — Understand the boundaries and constraints of AI-assisted development

## Skills

### Problem-solving with AI

* Using AI to rapidly solve straightforward coding problems

* Assessing problem complexity and AI suitability

  * Identifying problems amenable to single-pass solutions
  * Recognising that some problems can't be solved even with the help of AI

### Planning

* Articulating objectives clearly
* Collaborating with AI to develop multi-step implementation plans
* Decomposing problems into constituent sub-problems
* Providing focused context and documentation to the AI agent

### Iterative development

* Giving the AI tasks that are manageable to minimise how much it needs your help
* Understanding context windows and token allocations

### Version control

* Ensuring forward progress through systematic version tracking
* Getting the AI to maintain systematic documentation through backlogs and project tracking
* Using the documented history to reflect on processes

### Code maintenance

* Understanding codebase scale limits
* Recognising the relationship between project size and maintenance burden
* Evaluating long-term sustainability of AI-generated solutions

## Exercises

### 1. Vibe coding

**Purpose:** Have a first experience of agentic AI development

Set up an AI agent and get familiar with its interface and capabilities. Start by attempting to solve some trivial programming problems in a single interaction. Then experiment with using the agent to automate a simple task on your computer, such as file organisation or data processing. The goal is to develop an intuitive feel for what the AI can do quickly and easily.

to do:
1. make a list of some trivial coding tasks

### 2. Difficulty assessment

**Purpose:** Build planning skills by learning to evaluate problem complexity

Before undertaking an agentic coding project, it's important to understand what the challenges will be. Given a collection of coding exercises, rank them from simplest to most complex. For each exercise, consider how difficult it would be for unassisted human software engineers to solve. Use the AI as a partner to reason about the difficulty of different programming tasks, identifying which could be solved easily by an AI in a single attempt and which would require a carefully orchestrated, multi-phase development effort. This skill is fundamental to effective planning.

to do:
* make a list of software development challenges for students
* write descriptions for each of the software challenges that make it possible for the student to reason about the resources needed to solve them

### 3. Solution comparison and analysis

**Purpose:** Train evaluative skills crucial to agentic coding

For a specific coding challenge, review 5 pre-prepared solutions that solve the same problem in different ways. Use the AI as a partner to reason about the code you've been given. Analyse and discuss the implementation differences, identifying the trade-offs and compromises each solution makes. Evaluate the strengths and weaknesses of each approach, considering factors such as readability, performance, maintainability, and elegance. This exercise develops your ability to critically assess code quality and make informed decisions about implementation strategies.

* Choose a software development challenge (maybe one from the list of trivial one-shotters)
* Generate 5 examples of different approaches to addressing the same problem:
    * Intermdiate code with lots of code duplication and lots of insonsistencies in style and method. A few unnecessary imports. They tried to neatly organise things into functions but they also put some of the core functionality into the `name=main` block. A few blocks of code that have been commented out but kept because this person doesn't understand version management.
    * Beginner code that has no functions or structure and just runs as a script which assumes that the input data is saved with a particular name in the same folder as the script. Works if the user knows exactly what assumptions it makes. Breaks spectacularly otherwise. way too many comments in this code. lots of print statements.
    * Super efficient and elegantly executed code that looks like it has been written by some genius coder but which has no documentation, no comments and minimal error handling. Variable names are not descriptive at all. Hard for anyone to read except the original author.
    * Well implemented code that follows lots of best practice software development protocols but wraps the core function in a bespoke interactive terminal/text-based UI that is unnecessary and will bloat the maintenance.
    * One more eccentric solution that doesn't make a reasonable engineering compromise given the context. 

### 4. Exploring and failing

**Purpose:** Have an experience of the limitations of agentic AI development and practice using documentation to reflect on the development process

Select an intentionally overambitious idea from a provided list—something that pushes the boundaries of what you and the AI can accomplish together. Work on the project iteratively, documenting your progress carefully. Reflect on the development process throughout, noting the progress you achieve, the nature of eventual limitations or failure, and the lessons learned about scope and complexity. Pay particular attention to how best to document the iterative development process so that both you and the AI agent understand where the project is up to and what the goals are. This exercise teaches valuable lessons about realistic scoping and effective documentation practices.

Ideas:
* Custom ML pipeline such as an image classifier
* Reverse engineer facebook
* A full custom multi-player GUI for a bespoke cardgame

To do:
* Just elaborate on the exercise and add a few more ideas to the llist. Make it clear that the students can do whatever they want as long as it is ambitious.

### 5. Branching architecture

**Purpose:** Develop version management and context engineering skills while practicing to break a project into sessions

Building on the insight from Exercise 3 that the best solution depends on the engineering context, use the agentic AI to develop two projects with shared core functionality but different applications. Create a core algorithm on the main branch, then implement two distinct applications of the algorithm on separate branches—for example, two different front-ends for the same underlying functionality. This exercise develops your skills with version management, recursive and multi-step development planning, and context engineering. Reflect on the process, noting how you managed the shared codebase, maintained consistency across branches, and communicated the project structure to the AI agent.

to do:
* Choose a coding challenge to use.
* develop the repo up to the point where it splits into two projects.

### 6. Sandbox acceleration

**Purpose:** Practice being efficient with tokens and time by context engineering, selecting the right model and minimising the amount of input you need to give

Set up an AI agent in a sandbox environment and activate YOLO mode, giving it maximum autonomy. Take a list of programming exercises and see how many you can successfully solve before exhausting your token allocation. This exercise teaches you to work efficiently with AI agents, prioritise tasks effectively, and understand the practical constraints of token limits and computational resources. Track which types of problems consume the most tokens and which can be solved most efficiently, developing an intuition for resource management in agentic development.

### 7. CPS development with AI

**Purpose:** See how much harder it is to make a physical artifact given that the agent can't evaluate success.

Choose a Rraspberry Pi project. Wire up the pi and establish an SSH pairing. Get an AI agent to use the SSH link to build the functionality that you want in the pi. You'll need to interact with the agent as you go to tell it when the physical components are working as expected. If you really want to stretch it you can get the agent to flash code to an arduino over serial connection.

### 8. Red team

**Purpose:** Break the boundaries of AI safety in a sandbox evironment so that you have some experience of what can go wrong.

Load up a network of docker containers on a server that have been designed for cyberwar gaming. Let the agent rip in YOLO mode and see if you can get it to take over the network and harvest all the traffic. Have a team of humans trying to defend without any AI assistance.
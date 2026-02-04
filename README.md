# Agentic Coding with LLMs

A guide to effective software development using AI agents as collaborative partners.

## Overview

Agentic coding is a development approach where AI assistants work alongside human developers to write, review, and maintain code. This guide provides principles, skills, and exercises for learning to code effectively with AI agents.

## Core Principles

### 1. Human-Led Design and Critique
AI serves as an assistant, not the primary decision-maker. You remain responsible for architectural decisions, code quality standards, and project direction.

### 2. Plan Before Coding
Establish clear objectives and architecture before implementation. Good planning reduces wasted effort and helps the AI understand your intentions.

### 3. Write the Rules
Give your AI agents a set of rules appropriate to the context. The clearer your guidelines, the less human oversight is needed, and the faster development proceeds.

### 4. Session-Based Project Structure
Break work into manageable, focused sessions. This helps maintain context, enables meaningful progress tracking, and prevents scope creep.

### 5. Task-Appropriate Tooling
Select the right AI agent for each job. Different tasks may benefit from different models, interfaces, or configurations.

### 6. Recognise Limitations
Understand the boundaries and constraints of AI-assisted development. Not every problem is well-suited to AI assistance, and some problems remain difficult regardless of tooling.

## Key Skills

### Problem-Solving with AI
- Using AI to rapidly solve straightforward coding problems
- Assessing problem complexity and AI suitability
- Identifying problems amenable to single-pass solutions
- Recognising when AI assistance won't help

### Planning
- Articulating objectives clearly
- Collaborating with AI to develop multi-step implementation plans
- Decomposing problems into constituent sub-problems
- Providing focused context and documentation to the AI agent

### Iterative Development
- Giving the AI tasks that are manageable to minimise intervention
- Understanding context windows and token allocations

### Version Control
- Ensuring forward progress through systematic version tracking
- Getting the AI to maintain documentation through backlogs and project tracking
- Using documented history to reflect on processes

### Code Maintenance
- Understanding codebase scale limits
- Recognising the relationship between project size and maintenance burden
- Evaluating long-term sustainability of AI-generated solutions

## Exercises

### Exercise 1: Vibe Coding
**Purpose:** Have a first experience of agentic AI development

Set up an AI agent and get familiar with its interface and capabilities. Start by solving trivial programming problems in a single interaction. Then experiment with using the agent to automate simple tasks on your computer, such as file organisation or data processing. The goal is to develop an intuitive feel for what the AI can do quickly and easily.

### Exercise 2: Difficulty Assessment
**Purpose:** Build planning skills by learning to evaluate problem complexity

Before undertaking an agentic coding project, understand what the challenges will be. Given a collection of coding exercises, rank them from simplest to most complex. Consider how difficult each would be for unassisted human software engineers. Use the AI as a partner to reason about difficulty, identifying which problems could be solved easily in a single attempt and which would require a carefully orchestrated, multi-phase effort.

### Exercise 3: Solution Comparison and Analysis
**Purpose:** Train evaluative skills crucial to agentic coding

For a specific coding challenge, review multiple solutions that solve the same problem in different ways. Use the AI as a partner to reason about the code. Analyse implementation differences, identifying trade-offs and compromises. Evaluate strengths and weaknesses considering readability, performance, maintainability, and elegance. This develops your ability to critically assess code quality and make informed decisions about implementation strategies.

### Exercise 4: Exploring and Failing
**Purpose:** Experience the limitations of agentic AI development and practice documentation

Select an intentionally overambitious idea—something that pushes the boundaries of what you and the AI can accomplish together. Work iteratively, documenting progress carefully. Reflect throughout, noting progress achieved, the nature of eventual limitations or failure, and lessons learned about scope and complexity. Pay attention to how best to document the iterative development process so that both you and the AI understand the project state and goals.

**Example ideas:**
- Custom ML pipeline such as an image classifier
- Reverse engineer a social media platform
- A full custom multiplayer GUI for a bespoke card game

### Exercise 5: Branching Architecture
**Purpose:** Develop version management and context engineering skills

Building on the insight that the best solution depends on engineering context, use agentic AI to develop two projects with shared core functionality but different applications. Create a core algorithm on the main branch, then implement two distinct applications on separate branches—for example, two different front-ends for the same underlying functionality. This develops skills with version management, recursive and multi-step development planning, and context engineering.

### Exercise 6: Sandbox Acceleration
**Purpose:** Practice efficient token and time usage through context engineering

Set up an AI agent in a sandbox environment and activate maximum autonomy mode. Take a list of programming exercises and see how many you can successfully solve before exhausting your token allocation. Track which types of problems consume the most tokens and which can be solved most efficiently. This teaches efficient work with AI agents, task prioritisation, and understanding practical constraints of token limits.

### Exercise 7: Cyber-Physical Systems Development
**Purpose:** Experience how physical artifacts add complexity when the agent cannot evaluate success

Choose a Raspberry Pi project. Wire up the Pi and establish an SSH connection. Get an AI agent to use the SSH link to build the functionality you want. You'll need to interact with the agent to tell it when physical components are working as expected. This highlights the challenge of developing systems where the AI cannot directly observe outcomes.

### Exercise 8: Red Team
**Purpose:** Experience AI safety boundaries in a controlled sandbox environment

Set up a network of docker containers designed for cyberwar gaming. Let the agent work in autonomous mode to see if you can get it to take over the network and harvest traffic. Have a team of humans trying to defend without AI assistance. This exercise provides hands-on experience with what can go wrong and why guardrails exist.

## Getting Started

1. Choose an AI coding assistant (Claude, GPT, etc.)
2. Set up your development environment
3. Start with Exercise 1 to build familiarity
4. Progress through exercises as your skills develop
5. Document your learnings and reflect on each session

## Contributing

This is a living document. Contributions, suggestions, and additional exercises are welcome.

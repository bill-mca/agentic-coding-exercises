# Exercise 2: Difficulty Assessment

## Purpose
Build planning skills by learning to evaluate the complexity of software development challenges.

## Overview
Before undertaking an agentic coding project, it's crucial to understand what the challenges will be. This exercise teaches you to assess project complexity across multiple dimensions, helping you identify which problems are suitable for AI-assisted development and which will require more careful planning.

## Learning Objectives
- Evaluate software projects across multiple complexity dimensions
- Estimate resource requirements (time, team size, expertise)
- Identify technical risks and challenges
- Understand which types of projects benefit most from AI assistance
- Practice using AI as a reasoning partner for technical assessment
- Develop intuition for project scoping and planning

## Materials

### 1. Challenge Descriptions (`challenges.md`)
18 software development challenges ranging from trivial to extremely complex:
- Command-line utilities
- Web applications
- Distributed systems
- Machine learning pipelines
- Mobile applications
- Infrastructure projects

### 2. Example Specification (`specifications/01-calculator.md`)
An example detailed specification showing how to document a challenge thoroughly:
- Technical requirements
- External dependencies
- Data requirements
- Performance requirements
- Testing considerations
- Deployment complexity
- Estimated effort

**Your task:** Create similar detailed specifications for 2-3 challenges of your choice. Use the example as a template.

### 3. Assessment Rubric (`rubric.md`)
A comprehensive framework for evaluating challenge difficulty across 8 dimensions:
- Algorithmic complexity
- Integration complexity
- Domain knowledge required
- Data complexity
- User interface complexity
- Testing difficulty
- Deployment complexity
- Team size requirements

## Instructions

### Part 1: Initial Assessment (Solo, 30-45 minutes)

1. **Read all 18 challenge descriptions** in `challenges.md`

2. **Make initial intuitive rankings:**
   - Without overthinking, rank them from simplest (1) to most complex (18)
   - Note your immediate reactions: which seem approachable? Which seem daunting?

3. **Review the rubric** in `rubric.md`
   - Understand the 8 assessment dimensions
   - Review the rating scales for each dimension

4. **Select 3-5 challenges** spanning different complexity levels

5. **Create detailed specifications** for your selected challenges
   - Review the example in `specifications/01-calculator.md`
   - Write similar specifications for your chosen challenges
   - Work with AI to think through all the requirements

### Part 2: AI-Assisted Analysis (With AI Agent, 60-90 minutes)

6. **Work with your AI agent to analyze each challenge:**
   - Ask the AI to assess challenges using the rubric
   - Discuss the assessment for each dimension
   - Estimate development effort and team requirements
   - Identify key technical risks

7. **Compare assessments:**
   - How do your initial intuitions compare with the detailed analysis?
   - Where did you underestimate or overestimate complexity?
   - What factors did you initially overlook?

8. **Discuss AI suitability:**
   - Which challenges are most suitable for AI-assisted development?
   - Which would benefit least from AI assistance?
   - What characteristics make a project "AI-friendly"?

### Part 3: Refined Ranking (Solo + AI, 30-45 minutes)

9. **Create your final ranking:**
   - Revise your initial ranking based on deeper analysis
   - Justify your ordering with reference to specific dimensions
   - Identify clusters of similar complexity

10. **Assess your own capabilities:**
    - Which challenges could you tackle solo with AI assistance?
    - Which would require a team?
    - Which are beyond your current skill level?

### Part 4: Reflection (15-30 minutes)

11. **Write a brief reflection** addressing:
    - What factors matter most in assessing complexity?
    - How accurate were your initial intuitions?
    - What surprised you during the analysis?
    - How does AI assistance change project feasibility?
    - What gaps in your knowledge did you identify?

## Example Workflow

Here's how to analyze a challenge with your AI agent:

```
You: "I'm working on Exercise 2: Difficulty Assessment. Let's analyze
Challenge 5: Markdown Blog Generator. Please assess it using the rubric
dimensions and provide ratings for each dimension."

AI: [Provides detailed analysis]

You: "You rated the algorithmic complexity as 'Medium'. Can you explain
what makes it medium rather than low? What are the challenging
algorithmic aspects?"

AI: [Explains markdown parsing, template rendering, etc.]

You: "How would you estimate the development time for an experienced
developer working solo with AI assistance?"

AI: [Provides estimate with reasoning]

You: "What would be the biggest technical risks or challenges in
implementing this?"

AI: [Discusses key challenges]
```

## Discussion Prompts

Use these prompts to guide your AI conversations:

- "What are the key differences between Challenge X and Challenge Y?"
- "Why would Challenge X require more people than Challenge Y?"
- "What domain knowledge is essential vs. nice-to-have for Challenge X?"
- "How would AI assistance change the effort estimate for this challenge?"
- "What could go wrong when implementing Challenge X?"
- "Which parts of Challenge X would be hardest for an AI to help with?"
- "How would you break Challenge X into phases?"

## Tips for Success

### Working Solo
- Trust your intuitions but test them systematically
- Consider projects you've worked on as reference points
- Think about what you personally find challenging vs. easy
- Don't just focus on coding - consider deployment, testing, etc.

### Working with AI
- Ask the AI to explain its reasoning
- Challenge the AI's assessments - probe deeper
- Ask for examples and counterexamples
- Use the AI to identify blind spots in your analysis
- Request alternative viewpoints

### Making Assessments
- Consider all dimensions, not just what interests you
- Think about the full lifecycle (development through production)
- Remember that "simple to describe" doesn't mean "simple to build"
- Consider what could go wrong (Murphy's Law applies)
- Think about how you'd verify correctness

## Common Insights

Students often discover:

1. **Integration complexity is often underestimated** - coordinating many systems is harder than implementing any single system

2. **Domain knowledge gates progress** - you can't code what you don't understand

3. **Testing complexity correlates with deployment complexity** - hard-to-test systems are hard to operate

4. **UI complexity is often underestimated** - especially mobile apps and real-time features

5. **Some "simple" problems hide deep complexity** - like search relevance or feed ranking algorithms

6. **AI is best suited for well-defined, isolated problems** - ambiguous or highly integrated problems are challenging

## Time Estimate

- **Total exercise:** 2.5-4 hours
- **Can be done in multiple sessions**

## Group Activity Option

If doing this exercise in a group:

1. **Individual assessment first** (parts 1-3)
2. **Group discussion:**
   - Share rankings and compare
   - Discuss major disagreements
   - Present most surprising findings
   - Vote on most/least AI-suitable projects
3. **Reflect on variation:**
   - Why do assessments differ?
   - How does expertise affect perception?
   - What can we learn from disagreement?

## Next Steps

After completing this exercise:
- You should have better intuition for project complexity
- You'll know what questions to ask when starting a project
- You'll understand which projects are good candidates for AI assistance
- Move on to Exercise 3 to practice evaluating code quality

# Exercise 4: Exploring and Failing

## Purpose
Experience the limitations of agentic AI development and practice systematic documentation of the development process.

## Overview
This exercise is different from the previous ones. Instead of analyzing existing code or completing small tasks, you'll tackle an ambitious project—something that pushes the boundaries of what you and your AI agent can accomplish together. The goal isn't necessarily to finish (though you might!), but to learn about working at the edge of your and the AI's capabilities.

## Learning Objectives
- Experience working on complex, multi-session projects
- Practice systematic progress tracking and documentation
- Learn to recognize and respond to blockers
- Understand when to persist vs. when to pivot
- Develop resilience when things don't work as planned
- Master documentation practices that enable AI collaboration
- Gain insight into the limitations of AI-assisted development
- Learn from the process, not just the outcome

## Why "Exploring and Failing"?

The name acknowledges an important truth: pushing boundaries means sometimes hitting walls. But hitting walls teaches you:

1. **Your limits** - What knowledge gaps you have
2. **AI's limits** - Where AI assistance breaks down
3. **Project complexity** - How problems scale
4. **Planning skills** - How to scope and adjust
5. **Resilience** - How to persist through challenges
6. **Documentation value** - Why tracking progress matters

**Remember:** "Failure" in this exercise is still success if you learn from it.

## The Challenge

Select an ambitious project from `ambitious-projects.md` (or create your own) and attempt to build it over 4-10 hours of work.

### What Makes a Good Choice?

**Choose a project that:**
- ✅ Genuinely excites you
- ✅ Feels challenging but within reach
- ✅ Has clear success criteria
- ✅ You can make tangible progress on
- ✅ Teaches you something valuable

**Avoid projects that:**
- ❌ Require expensive resources
- ❌ Depend on unavailable APIs or services
- ❌ Need specialized hardware you don't have
- ❌ Are completely outside your domain knowledge
- ❌ Have no objective measure of success

## Instructions

### Phase 0: Preparation (30-60 minutes)

1. **Review project ideas** in `ambitious-projects.md`
   - Read through all options
   - Consider difficulty and interest
   - Think about what you'd learn

2. **Select your project**
   - Trust your intuition
   - Pick something that excites you
   - Don't overthink it

3. **Set up documentation**
   - Copy templates from `templates/` to your project directory
   - Fill in initial information in `PROGRESS.md`
   - Prepare `DECISIONS.md` and `BLOCKERS.md`

4. **Initial planning session**
   - Define what "done" looks like
   - Break project into major components
   - Identify the minimal working version
   - Research what exists already

5. **Set expectations**
   - This will be challenging
   - You might not finish
   - That's okay and expected
   - The learning is in the journey

### Phase 1: Getting Started (1-2 hours)

6. **Start with the core**
   - Build the simplest possible working version
   - Prove the basic concept works
   - Don't worry about polish yet

7. **Document as you go**
   - Update `PROGRESS.md` during or immediately after each session
   - Note what you tried and what happened
   - Record AI interactions that were helpful or unhelpful

8. **Establish your rhythm**
   - Find a workflow that works for you
   - Learn when to ask AI for help vs. research yourself
   - Notice what kinds of prompts are effective

### Phase 2: Development (2-6 hours)

9. **Iterate and expand**
   - Add features incrementally
   - Test frequently
   - Adjust plans based on reality

10. **Handle blockers systematically**
    - When stuck, document in `BLOCKERS.md`
    - Try 2-3 approaches before escalating
    - Know when to pivot vs. persist
    - Use the 3-attempt rule: If 3 approaches fail, reconsider

11. **Make and document decisions**
    - Major choices go in `DECISIONS.md`
    - Include your reasoning
    - Note alternatives considered
    - Be honest about trade-offs

12. **Track your collaboration with AI**
    - What prompts work well?
    - Where does AI struggle?
    - When do you need to take over?
    - What can AI handle independently?

### Phase 3: Reality Check (variable timing)

13. **Assess progress regularly**
    - Are you making progress toward goals?
    - Do goals need to adjust?
    - Is the timeline realistic?
    - Should you pivot?

14. **Recognize inflection points**
    - When you break through a blocker
    - When you realize something won't work
    - When you need to change direction
    - When you achieve a milestone

15. **Be honest with yourself**
    - Is this project still feasible?
    - Are you learning?
    - Is frustration productive or destructive?
    - What would success look like from here?

### Phase 4: Conclusion (30-60 minutes)

16. **Determine your stopping point**
    - Completed successfully
    - Achieved partial goals
    - Hit an insurmountable blocker
    - Ran out of time
    - Lost interest (that's data too!)

17. **Complete the retrospective**
    - Fill out `RETROSPECTIVE.md` thoroughly
    - Be honest about what happened
    - Focus on learnings over outcomes
    - Celebrate what you accomplished

18. **Preserve your work**
    - Clean up repository if continuing
    - Archive if not continuing
    - Ensure documentation is complete
    - Your future self will thank you

## Documentation Templates

Four templates are provided in `templates/`:

### 1. PROGRESS.md
**Purpose:** Track day-to-day progress, decisions, and observations

**Use for:**
- Session summaries
- What worked/didn't work
- AI interaction notes
- Next steps

**Update:** After each work session

### 2. DECISIONS.md
**Purpose:** Document major architectural and technical decisions

**Use for:**
- Framework/library choices
- Architectural patterns
- Trade-off decisions
- Approach selections

**Update:** When making significant decisions

### 3. BLOCKERS.md
**Purpose:** Track obstacles and how you address them

**Use for:**
- Active blockers
- Attempted solutions
- Resolved issues
- Workarounds
- Abandoned approaches

**Update:** When stuck or unstuck

### 4. RETROSPECTIVE.md
**Purpose:** Final reflection on the entire project

**Use for:**
- Overall assessment
- Learning outcomes
- What went well/poorly
- Future recommendations

**Complete:** At the end of the project

## Working with AI During This Exercise

### Effective Patterns

**Start each session by sharing context:**
```
"I'm working on [project]. Last session I [summary]. Today I want to [goal].
Here's where I left off: [key details]"
```

**Ask for planning help:**
```
"I want to implement [feature]. What are the major steps? What should I
consider? What could go wrong?"
```

**Request code review:**
```
"Here's the code I wrote. What issues do you see? How would you improve it?
What edge cases am I missing?"
```

**Debug together:**
```
"I'm getting [error]. Here's the relevant code: [code]. Here's what I've tried:
[attempts]. What should I try next?"
```

**Seek explanations:**
```
"I don't understand [concept]. Can you explain it in the context of my project?
What do I need to know to implement [feature]?"
```

### What to Expect from AI

**AI excels at:**
- Generating boilerplate code
- Explaining concepts and errors
- Suggesting standard approaches
- Reviewing code for issues
- Providing examples
- Debugging common errors

**AI struggles with:**
- Novel or unusual problems
- Deep domain expertise
- Debugging complex interactions
- Performance optimization
- Knowing what you don't know
- Making strategic project decisions

**You must provide:**
- Project vision and goals
- Strategic decisions
- Context and constraints
- Final judgment on trade-offs
- Testing and validation
- Course corrections

## Common Experiences

Students often encounter:

### Week 1
- Excitement and optimism
- Rapid initial progress
- "This is easier than I thought!"

### Week 2
- First major blocker
- Realization of complexity
- Questioning initial approach

### Week 3
- Breakthrough or pivot
- Adapted expectations
- Deeper understanding

### End
- Pride in progress, regardless of completion
- Appreciation for documentation
- Clarity about AI's strengths/limitations
- Better intuition for project scoping

## When to Stop

Consider concluding the project when:

- ✅ You've achieved your (possibly adjusted) goals
- ✅ You've learned what you set out to learn
- ✅ You're no longer making meaningful progress
- ✅ You've hit your time budget
- ✅ The blocker is insurmountable with current resources
- ✅ You've gained valuable experience to apply elsewhere

Don't feel obligated to:
- ❌ Finish just because you started
- ❌ Continue when learning has plateaued
- ❌ Keep going out of stubbornness
- ❌ Reach an arbitrary milestone

The learning is the goal, not the completion.

## Success Criteria

You've succeeded in this exercise if you:

1. **Attempted something ambitious** - Pushed beyond your comfort zone
2. **Documented systematically** - Used the templates to track progress
3. **Worked with AI effectively** - Learned what works and what doesn't
4. **Reflected thoughtfully** - Completed a thorough retrospective
5. **Learned something valuable** - Can articulate what you gained

Finishing the project is a bonus, not a requirement.

## Time Estimate

- **Minimum:** 4-5 hours (enough to hit meaningful challenges)
- **Recommended:** 6-8 hours (enough for iteration)
- **Maximum:** 10-12 hours (diminishing returns beyond this)

Split across multiple days is fine and often better.

## Tips for Success

### Planning
- Start with the smallest possible working version
- Don't try to build everything at once
- Expect to adjust your goals
- Research existing solutions for ideas

### Development
- Commit frequently
- Test each component as you build
- Don't optimize prematurely
- Comment your code (especially AI-generated code)

### Documentation
- Document in real-time or immediately after
- Be specific and honest
- Future-you needs context
- Include failures, not just successes

### AI Collaboration
- Be specific in prompts
- Provide context each session
- Verify AI-generated code
- Ask for explanations
- Challenge AI suggestions

### Mental Health
- Take breaks when frustrated
- It's okay to pivot or stop
- Progress isn't always visible
- Learning counts even when code doesn't work

## Group Variation

If doing this exercise with others:

1. **Individual work:** Everyone does their own project
2. **Regular check-ins:** Share progress and blockers (weekly?)
3. **Group reflection:** Final session to compare experiences
4. **Key discussion questions:**
   - What types of blockers did people encounter?
   - How did AI help or hinder?
   - What would you do differently?
   - What patterns emerged?

## After the Exercise

### Share Your Experience
If comfortable, share your retrospective with others. Your challenges help them learn too.

### Apply Your Learnings
The lessons from this exercise transfer to:
- Future ambitious projects
- Better scoping and planning
- More effective AI collaboration
- Improved documentation habits
- Realistic self-assessment

### Keep or Archive
Decide whether to:
- Continue the project (now informed by experience)
- Archive it (preserve the learning)
- Cannibalize it (reuse parts for other projects)
- Abandon it (that's okay too)

## Next Steps

After completing this exercise:
- You understand your limits and AI's limits better
- You have documentation practices that enable long-term projects
- You can assess project ambition more accurately
- You're ready for Exercise 5 and beyond
- Most importantly: You're not afraid to try ambitious things

## Final Thoughts

This exercise is designed to be challenging. You might feel:
- Frustrated when blocked
- Excited when breaking through
- Disappointed if you don't finish
- Proud of what you learned

All of these are valid and valuable.

The goal is to push boundaries and learn what happens when you do. Whether your code works perfectly, partially, or not at all, if you documented the journey and reflected on it, you've succeeded.

**Remember: The best way to learn your limits is to exceed them.**

Good luck, and enjoy the exploration! 🚀

# Difficulty Assessment Rubric

This rubric provides a framework for evaluating the complexity of software development challenges. Use these dimensions to assess and rank the challenges systematically.

## Assessment Dimensions

### 1. Algorithmic Complexity
**What it measures:** The difficulty of the core algorithms and logic required.

**Rating Scale:**
- **Very Low:** Simple CRUD operations, basic string/array manipulation
- **Low:** Standard algorithms (sorting, searching), basic data structures
- **Medium:** Custom algorithms, graph algorithms, parsing
- **High:** Complex optimization problems, advanced data structures
- **Very High:** Distributed algorithms, ML algorithms, compiler optimizations

**Questions to ask:**
- How sophisticated are the core algorithms?
- Are there well-known solutions, or must custom algorithms be developed?
- How much computer science theory knowledge is required?

### 2. Integration Complexity
**What it measures:** How many external systems, APIs, or components must work together.

**Rating Scale:**
- **Very Low:** Standalone application, no external dependencies
- **Low:** 1-2 external libraries or simple file I/O
- **Medium:** 3-5 external services/APIs, database integration
- **High:** Multiple databases, message queues, third-party APIs
- **Very High:** Microservices architecture, dozens of integrations

**Questions to ask:**
- How many external systems need to be integrated?
- Are there network communication requirements?
- How many distinct technologies must be coordinated?

### 3. Domain Knowledge Required
**What it measures:** Specialized knowledge needed beyond general programming skills.

**Rating Scale:**
- **Very Low:** Common programming tasks, no special domain knowledge
- **Low:** Basic web/CLI concepts
- **Medium:** Understanding of specific domain (networking, ML basics, databases)
- **High:** Deep domain expertise (distributed systems, compilers, ML engineering)
- **Very High:** Multiple domains of deep expertise required

**Questions to ask:**
- What specialized knowledge areas are involved?
- Could a competent programmer learn the domain while building this?
- Are there subtle domain-specific pitfalls?

### 4. Data Complexity
**What it measures:** Challenges related to data management, persistence, and scale.

**Rating Scale:**
- **Very Low:** No persistent data or simple file storage
- **Low:** Single database, simple schema
- **Medium:** Complex schema, data migrations, moderate scale
- **High:** Multiple data stores, sharding, caching strategies
- **Very High:** Data at scale (TB+), consistency challenges, global distribution

**Questions to ask:**
- How much data needs to be stored?
- What are the data consistency requirements?
- Are there data migration or versioning concerns?

### 5. User Interface Complexity
**What it measures:** Sophistication of the user-facing interface.

**Rating Scale:**
- **Very Low:** Command-line only, simple text output
- **Low:** Basic CLI with formatted output, simple web form
- **Medium:** Interactive web UI, responsive design
- **High:** Rich web application, real-time updates
- **Very High:** Native mobile apps, complex interactions, accessibility

**Questions to ask:**
- What platforms need to be supported (web, mobile, desktop)?
- How interactive is the UI?
- Are there real-time or collaborative features?

### 6. Testing Difficulty
**What it measures:** How challenging it is to verify correctness and quality.

**Rating Scale:**
- **Very Low:** Deterministic outputs, easy to write assertions
- **Low:** Mostly deterministic, straightforward test cases
- **Medium:** Some non-deterministic behavior, integration testing needed
- **High:** Timing-dependent, distributed systems, ML models
- **Very High:** Scale testing required, emergent behavior, hard to reproduce bugs

**Questions to ask:**
- Are outputs deterministic?
- How long do tests take to run?
- Are special resources needed for testing (GPUs, clusters)?
- How easy is it to create test data?

### 7. Deployment Complexity
**What it measures:** Difficulty of deploying and operating the system in production.

**Rating Scale:**
- **Very Low:** Single script/executable, runs anywhere
- **Low:** Simple web app, single server deployment
- **Medium:** Database + app server, basic DevOps
- **High:** Multi-service deployment, orchestration, monitoring
- **Very High:** Multi-region, auto-scaling, complex infrastructure

**Questions to ask:**
- What infrastructure is required?
- How many components need to be deployed?
- What are the reliability and scaling requirements?
- How complex is the operational burden?

### 8. Team Size Indicator
**What it measures:** How many people and what roles are needed.

**Rating Scale:**
- **1 person:** A single developer can complete it
- **2-3 people:** Small team, possibly specialized roles
- **4-7 people:** Mid-size team with specialized roles
- **8-15 people:** Large team with multiple specializations
- **15+ people:** Enterprise-scale team with many roles

**Questions to ask:**
- Can one person realistically handle all aspects?
- Are multiple specializations required (frontend, backend, mobile, ML, DevOps)?
- How much work can be parallelized?

## AI Suitability Assessment

Beyond general difficulty, assess how suitable the project is for AI-assisted development:

### AI-Friendly Characteristics
✅ **Well-defined specifications**
✅ **Clear input/output contracts**
✅ **Existing libraries for complex parts**
✅ **Deterministic behavior**
✅ **Good documentation and examples available online**
✅ **Decomposable into independent modules**
✅ **Standard patterns and practices apply**

### AI-Challenging Characteristics
⚠️ **Ambiguous requirements**
⚠️ **Novel problems without established solutions**
⚠️ **Performance optimization critical**
⚠️ **Deep domain expertise required**
⚠️ **Debugging complex interactions**
⚠️ **Non-deterministic or emergent behavior**
⚠️ **Security-critical components**
⚠️ **Architectural decisions with long-term consequences**

## How to Use This Rubric

### Step 1: Individual Assessment
For each challenge, rate it on each dimension (1-5 scale or categorical labels).

### Step 2: Overall Complexity Score
Calculate a weighted score (or create a complexity profile). Consider that some dimensions matter more than others depending on context.

**Suggested weighting:**
- Algorithmic: 20%
- Integration: 15%
- Domain Knowledge: 25%
- Data: 10%
- UI: 10%
- Testing: 10%
- Deployment: 10%

### Step 3: Time and Team Estimates
Based on the scores, estimate:
- Development time for an experienced team
- Team size and composition
- Key technical risks

### Step 4: AI Suitability
Mark which AI-friendly/challenging characteristics apply and assess overall AI suitability:
- **High:** AI can handle most aspects with guidance
- **Medium:** AI can assist but requires significant human expertise
- **Low:** AI provides limited value beyond boilerplate

### Step 5: Rank Challenges
Order challenges from simplest to most complex based on your assessment.

## Example Assessment

**Challenge:** Command-Line Calculator

| Dimension | Rating | Notes |
|-----------|--------|-------|
| Algorithmic | Medium | Parsing expressions, operator precedence |
| Integration | Very Low | No external systems |
| Domain Knowledge | Low | Basic parsing concepts |
| Data | Very Low | No persistence |
| UI | Very Low | CLI only |
| Testing | Low | Deterministic, easy to test |
| Deployment | Very Low | Single script |
| **Team Size** | **1 person** | Solo project |
| **AI Suitability** | **High** | Well-defined, common problem |

**Overall Complexity:** Low
**Estimated Effort:** 2-8 hours

---

**Challenge:** Social Media Platform

| Dimension | Rating | Notes |
|-----------|--------|-------|
| Algorithmic | Very High | Feed algorithms, recommendations, search |
| Integration | Extreme | Dozens of services and APIs |
| Domain Knowledge | Very High | Multiple specialized domains |
| Data | Very High | Scale, consistency, global distribution |
| UI | Very High | Web + iOS + Android apps |
| Testing | Extreme | Scale testing, distributed systems |
| Deployment | Extreme | Multi-region, auto-scaling |
| **Team Size** | **15-30 people** | Large enterprise team |
| **AI Suitability** | **Low** | Requires extensive expertise |

**Overall Complexity:** Extreme
**Estimated Effort:** 18-36 months

## Discussion Questions

Use your AI agent to explore these questions:

1. **Which dimensions matter most?** Is algorithmic complexity more important than deployment complexity?

2. **How do dimensions interact?** Does high integration complexity make testing harder?

3. **What makes something AI-suitable?** Which challenges could benefit most from AI assistance?

4. **Where does AI struggle?** What types of problems are hardest for AI to help with?

5. **How accurate are effort estimates?** How much variation exists between developers?

6. **What skills matter most?** Which dimensions require the most specialized expertise?

7. **How does planning help?** Would breaking complex projects into phases make them more tractable?

## Tips for Group Discussion

- Compare your rankings with others
- Discuss where you disagree and why
- Consider how your own expertise affects your assessments
- Think about how AI assistance changes the difficulty landscape
- Reflect on which projects you'd want to tackle with AI help

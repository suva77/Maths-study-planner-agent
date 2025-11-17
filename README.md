# Maths-study-planner-agent
# Project name
MathMate — Maths Study Planner & Doubt Solver (Multi-Agent System)
# Short subtitle
A multi-agent assistant that creates personalized math study plans, detects weakness, and gives step-by-step math explanations
# Track: Agents for Good — Education
# Project Summary
This project introduces a multi‑agent AI system designed to help students study mathematics more effectively through personalized planning, step‑by‑step doubt solving, and smart progress tracking.
    The system combines three intelligent agents:
      - Planner Agent — Creates personalized study schedules.
      - Doubt Solver Agent — Provides clear solutions to maths questions.
      - Weakness Detector Agent — Identifies weak areas and suggests revisions.
     The model runs as a multi‑agent collaboration, where each agent performs a specialized task and shares context using tools & memory.
# Problem Statement
Students often struggle with:
     - Organizing maths topics,
     - Following a consistent study plan,
     - Understanding difficult questions,
     - Tracking progress and weakness,
This leads to poor performance, low confidence, and inefficient study habits.
The proposed system solves these by combining structured planning with intelligent doubt solving.
# Goals of the System
- Provide daily/weekly maths study plans
- Give accurate, step‑by‑step solutions to maths problems
- Detect weak topics and recommend revisions
- Maintain memory of past study history
# System Architecture
# Agent 1: Planner Agent
1. Generates study plans.
2. Adjusts based on past performance.
3. Uses long‑term memory.
# Agent 2: Doubt Solver Agent
1. Parses math questions.
2. Solves step‑by‑step.
3. Verifies the answers.
# Agent 3: Weakness Detector Agent
1. Monitors study logs.
2. Detects weak chapters.
3. Communicates with Planner Agent to modify future plans.
# Workflow
1. User inputs their maths topics or questions.
2. Planner Agent generates a personalized plan.
3. Doubt Solver Agent answers questions.
4. Weakness Detector analyses mistakes and updates memory.
5. Planner adjusts next‑day study plan.
# Tools Used
1. Agent framework (multi‑agent orchestration).
2. Memory tool for storing progress.
3. Math reasoning tool.
4. Logging tool.
# Installation & Setup
Follow these steps to run the project locally:
1. Clone the repository:
     git clone https://github.com/<your-username>/<repo-name>.git
2. Go to project folder:
     cd <repo-name>
3. Install required dependencies:
     pip install -r requirements.txt
4. Run the main file:
     python main.py
# Project Structure
maths-study-agent/
1. agents/
- planner_agent.py
- doubt_solver_agent.py
- weakness_detector_agent.py
2. memory/
- study_history.json
3. tools/
- math_tool.py
- log_tool.py
4. app.py
- README.md
- requirements.txt
# Key Features
- Personalized Study Planner — Creates daily/weekly maths study plans based on your level.
- Weakness Detection — Automatically identifies weak topics using your incorrect answers.
- Doubt Solver — Clears any maths question with step-by-step explanation.
- Adaptive Learning — Adjusts your next study plan based on performance.
- Progress Tracking — Saves your study logs and shows improvement.
- Multi-Agent Architecture — Each agent performs a specialized task and collaborates.
# Demo (How It Works)
Example Walkthrough

1️⃣ User Input
The student enters:
“I want to study Calculus and also solve this question: ∫ (3x² + 2x) dx”

2️⃣ Planner Agent Response
Creates a personalized plan:
- Day 1 — Basics of Differentiation
- Day 2 — Integration types
- Day 3 — Practice problems
- Day 4 — Review & Weakness check

3️⃣ Doubt Solver Agent Response
Solves the question step-by-step:
∫ (3x² + 2x) dx
= ∫ 3x² dx + ∫ 2x dx
= x³ + x² + C

4️⃣ Weakness Detector Agent Response
Analyzes mistakes from previous logs and says:
“Student is weak in Integration by Parts → Adding extra practice for tomorrow.”

5️⃣ Planner Agent Adjusts Study Plan
Updates Day 2 to include:
Extra 5-10 problems in Integration by Parts
# Conclusion
MathMate is designed to make maths learning smarter, easier, and highly personalized.
By combining three specialized agents — Planner, Doubt Solver, and Weakness Detector — the system creates a complete study ecosystem for students.

This project demonstrates how multi-agent AI can improve education by:

- guiding students with structured study plans,
- giving clear step-by-step explanations,
- and continuously adapting to their progress.

MathMate is not just a tool —
it is a smart study companion that grows with the learner and helps them become more confident in mathematics.















     




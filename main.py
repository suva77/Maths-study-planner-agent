from agents.planner_agent import PlannerAgent
from agents.doubt_solver_agent import DoubtSolverAgent
from agents.weakness_detector_agent import WeaknessDetectorAgent
from tools.memory_tool import MemoryTool
from tools.math_tool import MathTool

# Initialize tools
memory = MemoryTool()
math_tool = MathTool()

# Initialize agents
planner = PlannerAgent(memory)
solver = DoubtSolverAgent(math_tool)
weakness = WeaknessDetectorAgent(memory)

print("Welcome to MathMate — Multi-Agent Maths Study System!\n")

while True:
    print("Choose an option:")
    print("1. Generate Study Plan")
    print("2. Solve a Math Doubt")
    print("3. Show Weak Topics")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        topics = input("Enter your maths topics (comma separated): ")
        topics = [t.strip() for t in topics.split(",")]
        plan = planner.create_plan(topics)
        print("\nYour Study Plan:")
        for t in plan:
            print("•", t)

    elif choice == "2":
        q = input("Enter your math question: ")
        answer = solver.solve(q)
        print("\nStep-by-step solution:\n", answer)

    elif choice == "3":
        weak = weakness.find_weaknesses()
        print("\nYour weak topics:")
        for w in weak:
            print("•", w)

    elif choice == "4":
        print("Goodbye! Keep learning ❤️")
        break
    else:
        print("Invalid choice. Try again.")

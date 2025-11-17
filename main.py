# main.py

from agents.planner_agent import PlannerAgent
from agents.doubt_solver_agent import DoubtSolverAgent
from agents.weakness_detector_agent import WeaknessDetectorAgent
from tools.memory_tool import MemoryTool

# Initialize tools & agents
memory = MemoryTool()
planner = PlannerAgent(memory)
solver = DoubtSolverAgent()
weak_detector = WeaknessDetectorAgent(memory)

# Example usage
if __name__ == "__main__":

    print("\n--- MATH STUDY AGENT SYSTEM ---\n")

    topics = ["Algebra", "Trigonometry", "Calculus"]
    plan = planner.generate_plan(topics)
    print("Study Plan:", plan)

    question = "2*x + 3*x"
    answer = solver.solve(question)
    print("\nDoubt Solver Output:")
    print(answer)

    weak = weak_detector.update_weakness("Algebra", "wrong")
    print("\nUpdated Weak Topics:", weak)

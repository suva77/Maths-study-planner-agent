# doubt_solver_agent.py

import sympy as sp

class DoubtSolverAgent:
    def __init__(self):
        pass

    def solve(self, question):
        """
        Solves basic algebra & calculus questions step-by-step.
        """
        try:
            # Try symbolic solving
            expr = sp.sympify(question)
            solution = sp.simplify(expr)
            return f"Step-by-step solution:\n\nFinal Answer: {solution}"

        except:
            return "I could not understand the question. Please provide a clear math expression."

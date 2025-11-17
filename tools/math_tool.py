# math_tool.py

import sympy as sp

def solve_expression(expr):
    try:
        return sp.simplify(sp.sympify(expr))
    except:
        return "Invalid math expression"

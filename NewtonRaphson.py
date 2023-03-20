# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#Newton raphson code
import math
import sympy as sp

def func_1(x):
    result = x ** 3 - 2 * x - 5
    return result

def derivative_1():
    x = sp.Symbol('x')
    f = x ** 2 + 2 * x + 1

    # Compute the derivative of f(x)
    f_answer = sp.diff(f, x)
    return f_answer

def next_approx(x, f, f_answer):
    next_s = x - f/f_answer
    return next_s

# Main code to execute the algorithm
tolerance = 1e-6
x = 2
f = func_1(x)
f_answer = derivative_1()
next_s= next_approx(x, f, f_answer)

while abs(next_s - x) > tolerance:
    x = next_s
    f = func_1(x)
    f_prime = derivative_1()
    next_s = next_approx(x, f, f_answer)

print("The root is approximately", next_s.evalf())





# See PyCharm help at https://www.jetbrains.com/help/pycharm/

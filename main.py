# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#This is a python code to implement Bisection mehtod
import math
import timeit


def f(x):
    return x ** 3 - 2 * x - 5


a = 2
b = 3
tolerance = 1e-6
max_iteration = 1000
for i in range(max_iteration):
    c = (a + b) / 2
    print(f"The Iteration number is : {i}")
    if abs(f(c)) < tolerance:

        print(f"The rooot at x={c:.6f}")
        print(" time used is ", timeit.timeit())
        break
    elif f(c) * f(a) < 0:
        b = c
    else:
        a = c
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

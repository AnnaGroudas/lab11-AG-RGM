"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def square_root(a):
    if a<0:
        raise ValueError("a cannot be a negative number!")
    return math.sqrt(a)# raise ValueError if a < 0

def hypotenuse(a, b):
    return math.hypot(a, b) # can have negative nums

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a ==0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return b/a

def log(a, b):
    if a<=0:
        raise ValueError("a must be a positive value!")
    return math.log(b,a) # use math library + raise ValueError

def exp(a, b):
    return a**b





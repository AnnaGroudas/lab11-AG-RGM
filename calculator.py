"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example


import math


# def add(a, b):
#     pass

import math

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





"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
<<<<<<< HEAD
# First example
# def add(a, b):
#     pass

import math
=======

import math

def square_root(a):
    if a<0:
        raise ValueError("a cannot be a negative number!")
    return math.sqrt(a)# raise ValueError if a < 0

def hypotenuse(a, b):
    return math.hypot(a, b) # can have negative nums

>>>>>>> a6ed769f805cb3aa723e96d10a548336f9744e4f
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
<<<<<<< HEAD
    if a==0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return b / a # raise ZeroDivisionError if a == 0
=======
    if a ==0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return b/a
>>>>>>> a6ed769f805cb3aa723e96d10a548336f9744e4f

def log(a, b):
    if a<=0:
        raise ValueError("a must be a positive value!")
    return math.log(b,a) # use math library + raise ValueError

<<<<<<< HEAD

def exp(a, b):
    return a**b
=======
def exp(a, b):
    return a**b


>>>>>>> a6ed769f805cb3aa723e96d10a548336f9744e4f



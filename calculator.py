# https://github.com/singhanuv747-hash/lab11--A.S---A.S-.git
# Partner 1: <Anuv Singh>
# Partner 2: None

import math

def square_root(a):
    if a < 0:
        raise ValueError("Square root not defined for negative numbers")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def log(a, b):
    if a <= 0:
        raise ValueError("Logarithm undefined for this input")
    if b <= 0 or b == 1:
        raise ValueError("Invalid base")
    return math.log(a, b)

def exp(a, b):
    return a ** b

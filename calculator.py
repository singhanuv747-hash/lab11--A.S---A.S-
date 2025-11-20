# https://github.com/singhanuv747-hash/lab11--A.S---A.S-.git
# Partner 1: <Anuv Singh>
# Partner 2: None

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def log(a, b):
    if a <= 0:
        raise ValueError("Logarithm undefined for a <= 0.")
    if b <= 0 or b == 1:
        raise ValueError("Invalid logarithm base.")
    return math.log(a, b)

def exp(a, b):
    return a ** b

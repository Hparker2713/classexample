import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # TODO fix later
    return a / b

def factorial(a):
    if a < 0:
        return "Error: factorial not defined for negative numbers"
    return math.factorial(int(a))

print("*** Calculator App ***")
print("4 + 3 =", add(4, 3))
print("10 - 5 =", subtract(10, 5))
print("6 * 7 =", multiply(6, 7))
print("20 / 4 =", divide(20, 4))
print("5! =", factorial(5))

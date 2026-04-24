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

def square_root(a):
    if a < 0:
        return "Error: cannot square root a negative number"
    return math.sqrt(a)

print("*** Calculator App ***")
print("4 + 3 =", add(4, 3))
print("10 - 5 =", subtract(10, 5))
print("6 * 7 =", multiply(6, 7))
print("20 / 4 =", divide(20, 4))
print("sqrt(49) =", square_root(49))

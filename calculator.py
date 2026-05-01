import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    assert b != 0, "Jeff says: you cannot divide by zero!!"
    return a / b

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("*** Team B's Calculator App ***")

print("4 + 3 =", add(4, 3))
print("10 - 5 =", subtract(10, 5))
print("6 * 7 =", multiply(6, 7))
print("20 / 4 =", divide(20, 4))
print("5! =", factorial(5))

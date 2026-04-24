def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b

print("*** Calculator App hayden style***")
print("4 + 3 =", add(4, 3))
print("10 - 5 =", subtract(10, 5))
print("6 * 7 =", multiply(6, 7))
print("20 / 4 =", divide(20, 4))
print("2 ^ 8 =", power(2, 8))

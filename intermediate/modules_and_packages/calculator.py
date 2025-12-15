# Creating Your Own Modules
# This is our custom calculator module.

# (1) ADDITION
def add(a, b):
    return a + b

# (2) SUBTRACTION
def subtract(a, b):
    return a - b

# (3) MULTIPLICATION
def multiply(a, b):
    return a * b

# (4) DIVISION
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

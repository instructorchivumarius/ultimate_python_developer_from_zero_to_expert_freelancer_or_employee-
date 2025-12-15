# Errors Types in Python

# 1. SYNTAX ERROR
# Uncomment to see the error:
# print("Hello"  

# 2. RUNTIME ERROR
number = 10
# Uncomment to see the error:
# result = number / 0   # ZeroDivisionError

# 3. LOGICAL ERROR
# Code runs, but result is wrong
def add_numbers(a, b):
    return a - b  # mistake instead of a + b

print("Logical Error Example:", add_numbers(5, 3))

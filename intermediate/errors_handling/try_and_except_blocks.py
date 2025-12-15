# Try and Except Blocks

# 1 – Without error handling
# Uncomment to see the crash:
# number = int("abc")   # ValueError

# 2 – With try/except
try:
    number = int("abc")
    print("Conversion successful:", number)
except ValueError:
    print("Error: Cannot convert text to number")

# 3 – Multiple exceptions
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")
except ValueError:
    print("Value error occurred")

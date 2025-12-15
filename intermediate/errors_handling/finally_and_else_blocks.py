# Finally and Else Blocks

# 1 – Using else
try:
    number = int("10")
    print("Conversion successful")
except ValueError:
    print("Conversion failed")
else:
    print("No error occurred, so this else block runs")

# 2 – Using finally
try:
    result = 10 / 2
    print("Result:", result)
except ZeroDivisionError:
    print("Division by zero error")
finally:
    print("This finally block always runs")

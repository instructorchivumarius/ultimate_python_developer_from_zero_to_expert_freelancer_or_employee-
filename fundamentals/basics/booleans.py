# Data types: Booleans (True / False)

# Basic Boolean values
is_student = True
is_employed = False

print("Is student?", is_student)
print("Is employed?", is_employed)

# Booleans from comparisons
age = 20
is_adult = age >= 18
print("Is adult?", is_adult)

# Logical comparisons
x = 10
y = 5

print("x > y:", x > y)
print("x == y:", x == y)
print("x != y:", x != y)

# Logical operators
a = True
b = False

print("a AND b:", a and b)
print("a OR b:", a or b)
print("NOT a:", not a)

# Boolean conversion
print("bool(0):", bool(0))         # False
print("bool(1):", bool(1))         # True
print("bool(''):", bool(""))       # False
print("bool('text'):", bool("text"))  # True

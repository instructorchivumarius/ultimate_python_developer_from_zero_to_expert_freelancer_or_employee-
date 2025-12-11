# Logical Operators in Python 

# ───────────────────────────────
# (1) SETUP: Boolean values
a = True
b = False
print("() SETUP:", f"a={a}, b={b}")
print("-" * 50)

# ───────────────────────────────
# (2) AND operator
print("(2) AND")
print("a and b:", a and b)
print("a and True:", a and True)
print("b and False:", b and False)
print("-" * 50)

# ───────────────────────────────
# (3) OR operator
print("(3) OR")
print("a or b:", a or b)
print("a or False:", a or False)
print("b or True:", b or True)
print("-" * 50)

# ───────────────────────────────
# (4) NOT operator
print("(4) NOT")
print("not a:", not a)
print("not b:", not b)
print("-" * 50)

# ───────────────────────────────
# (5) COMBINATIONS
print("(5) COMBINATIONS")
print("(a and b) or not a:", (a and b) or not a)
print("a or (b and not a):", a or (b and not a))
print("-" * 50)

# ───────────────────────────────
# (6) SHORT-CIRCUIT EVALUATION
print("(6) SHORT-CIRCUIT")
x = 5
print("False and (x/0):", False and (x/0))  # no error
print("True or (x/0):", True or (x/0))      # no error
print("-" * 50)

# ───────────────────────────────
# (7) NON-BOOLEAN VALUES
print("(7) NON-BOOLEAN")
print("5 and 10:", 5 and 10)       # returns last value if all truthy
print("0 and 10:", 0 and 10)       # returns 0
print("5 or 10:", 5 or 10)         # returns first truthy
print("0 or 10:", 0 or 10)         # returns 10
print("not 0:", not 0)             # True (0 is Falsey)
print("not []:", not [])           # True (empty list is Falsey)
print("-" * 50)

print("DONE")

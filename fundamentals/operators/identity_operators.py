# Identity Operators in Python 

# ───────────────────────────────
# (1) SETUP: lists and variables
a = [1, 2, 3]
b = [1, 2, 3]
c = a
x = 10
y = 10
print("SETUP:", f"a={a}, b={b}, c=a, x={x}, y={y}")
print("-" * 50)

# ───────────────────────────────
# (2) is OPERATOR
print("(2) is OPERATOR")
print("a is b:", a is b)      # False: different objects, same content
print("a is c:", a is c)      # True: same object in memory
print("x is y:", x is y)      # True in CPython (small integers cached)
print("-" * 50)

# ───────────────────────────────
# (3) is not OPERATOR
print("(3) is not OPERATOR")
print("a is not b:", a is not b)  # True
print("a is not c:", a is not c)  # False
print("-" * 50)

# ───────────────────────────────
# (4) CONTENT vs IDENTITY
print("(4) CONTENT vs IDENTITY")
print("a == b:", a == b)   # True → same content
print("a is b:", a is b)   # False → different objects
print("-" * 50)

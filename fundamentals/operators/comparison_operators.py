# Comparison Operators in Python 

# ───────────────────────────────
# (1) SETUP: integers and strings
a = 10
b = 3
x = 10.0
name1 = "Alice"
name2 = "Bob"
print("SETUP:", f"a={a}, b={b}, x={x}, name1='{name1}', name2='{name2}'")
print("-" * 50)

# ───────────────────────────────
# (2) EQUALITY and INEQUALITY
print("(2) == and !=")
print("a == x:", a == x)  # int vs float
print("a == b:", a == b)
print("a != b:", a != b)
print("name1 == 'Alice':", name1 == "Alice")
print("name1 != name2:", name1 != name2)
print("-" * 50)

# ───────────────────────────────
# (3) GREATER / LESS
print("(3) >, <, >=, <=")
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= 10:", a >= 10)
print("b <= 3:", b <= 3)
print("-" * 50)

# ───────────────────────────────
# (4) STRING COMPARISONS
print("(4) STRINGS")
print("name1 < name2:", name1 < name2)
print("'apple' < 'banana':", "apple" < "banana")
print("'Zoo' < 'apple':", "Zoo" < "apple")  # case-sensitive
print("-" * 50)

# ───────────────────────────────
# (5) CHAINED COMPARISONS
print("(5) CHAINED")
print("1 < a < 20:", 1 < a < 20)
print("5 < b < 2:", 5 < b < 2)
print("-" * 50)

# ───────────────────────────────
# (6) IS vs ==
print("(6) IS vs ==")
c = [1, 2, 3]
d = [1, 2, 3]
print("c == d:", c == d)   # compares values
print("c is d:", c is d)   # compares identity
e = c
print("c is e:", c is e)
print("-" * 50)

print("DONE")

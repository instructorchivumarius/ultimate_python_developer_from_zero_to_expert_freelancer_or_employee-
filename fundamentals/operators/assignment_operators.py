# Assignment Operators in Python 

# ───────────────────────────────
# (1) BASIC ASSIGNMENT =
a = 10
print("(1) BASIC =", a)
print("-" * 50)

# ───────────────────────────────
# (2) ADD AND ASSIGN +=
a += 5
print("(2) += Add and Assign:", a)
print("-" * 50)

# ───────────────────────────────
# (3) SUBTRACT AND ASSIGN -=
a -= 3
print("(3) -= Subtract and Assign:", a)
print("-" * 50)

# ───────────────────────────────
# (4) MULTIPLY AND ASSIGN *=
a *= 2
print("(4) *= Multiply and Assign:", a)
print("-" * 50)

# ───────────────────────────────
# (5) DIVIDE AND ASSIGN /= and //=
a /= 4
print("(5) /= Divide and Assign:", a)
a //= 2
print("(5) //= Floor Divide and Assign:", a)
print("-" * 50)

# ───────────────────────────────
# (6) MODULUS AND ASSIGN %=
a %= 4
print("(6) %= Modulus and Assign:", a)
print("-" * 50)

# ───────────────────────────────
# (7) EXPONENTIATION AND ASSIGN **=
a = 3
a **= 3
print("(7) **= Exponentiation and Assign:", a)
print("-" * 50)

# ───────────────────────────────
# (8) COMBINED WITH VARIABLES
x, y = 5, 2
x *= y + 3
print("(8) COMBINED with variables (x *= y+3):", x)
print("DONE")

# Bitwise Operators in Python 

# ───────────────────────────────
# (1) SETUP
a = 6   # 110 in binary
b = 3   # 011 in binary
print("SETUP:", f"a={a} ({bin(a)}), b={b} ({bin(b)})")
print("-" * 50)

# ───────────────────────────────
# (2) AND (&)
print("(2) AND &")
print("a & b:", a & b)  
print("-" * 50)

# ───────────────────────────────
# (3) OR (|)
print("(3) OR |")
print("a | b:", a | b)
print("-" * 50)

# ───────────────────────────────
# (4) XOR (^)
print("(4) XOR ^")
print("a ^ b:", a ^ b)
print("-" * 50)

# ───────────────────────────────
# (5) NOT (~)
print("(5) NOT ~")
print("~a:", ~a)  
print("~b:", ~b)
print("-" * 50)

# ───────────────────────────────
# (6) SHIFT LEFT (<<)
print("(6) SHIFT LEFT <<")
print("a << 1:", a << 1)
print("b << 2:", b << 2)
print("-" * 50)

# ───────────────────────────────
# (7) SHIFT RIGHT (>>)
print("(7) SHIFT RIGHT >>")
print("a >> 1:", a >> 1)
print("b >> 2:", b >> 2)
print("-" * 50)

print("DONE")

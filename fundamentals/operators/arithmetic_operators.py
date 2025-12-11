# Arithmetic Operators in Python 

# ───────────────────────────────
# (1) SETUP: integers and floats
a = 10
b = 3
x = 10.0
y = 3.0
neg = -7
print("SETUP:", f"a={a}, b={b}, x={x}, y={y}, neg={neg}")
print("-" * 50)

# ───────────────────────────────
# (2) ADDITION, SUBTRACTION, MULTIPLICATION
print("(2) ADD / SUB / MUL")
print("Addition a + b:", a + b)
print("Subtraction a - b:", a - b)
print("Multiplication a * b:", a * b)
print("Mix types x * b:", x * b) 
print("-" * 50)

# ───────────────────────────────
# (3) DIVISION: / vs //
print("(3) DIVISION: / vs //")
print("a / b:", a / b)
print("a // b:", a // b)
print("x / y:", x / y)
print("x // y:", x // y)
print("neg // b:", neg // b)  
print("-" * 50)

# ───────────────────────────────
# (4) MODULUS %
print("(4) MODULUS %")
print("a % b:", a % b)
print("neg % b:", neg % b)
print("b % a:", b % a)
print("-" * 50)

# ───────────────────────────────
# (5) EXPONENTIATION **
print("(5) EXPONENTIATION **")
print("a ** b:", a ** b)
print("2 ** 0:", 2 ** 0)
print("2 ** 0.5:", 2 ** 0.5)  
print("-" * 50)


# ───────────────────────────────
# (6) PRECEDENCE
print("(6) PRECEDENCE")
print("2 + 3 * 4:", 2 + 3 * 4)
print("(2 + 3) * 4:", (2 + 3) * 4)
print("2 ** 3 * 2:", 2 ** 3 * 2)
print("2 ** (3 * 2):", 2 ** (3 * 2))
print("-" * 50)

# ───────────────────────────────
# (7) MATH MODULE EXTRAS
import math
print("(7) EXTRAS (math)")
print("math.sqrt(25):", math.sqrt(25))
print("math.floor(10/3):", math.floor(10/3))
print("math.trunc(10/3):", math.trunc(10/3))
print("-" * 50)

# ───────────────────────────────
# (8) PITFALLS
print("(8) PITFALLS")
# print(1 / 0)  # ZeroDivisionError
big = 2 ** 50
print("2 ** 50 has digits:", len(str(big)))
print("DONE")

# Walrus Operator (:=) in Python 

# ───────────────────────────────
# (1) BASIC USAGE
print("(1) BASIC USAGE")
print(x := 5)
print("-" * 50)

# ───────────────────────────────
# (2) USE IN EXPRESSION (NUMBERS)
print("(2) USE IN EXPRESSION WITH NUMBERS")
result = (y := 10) + 2
print("y:", y, "result:", result)
print("-" * 50)

# ───────────────────────────────
# (3) USE IN EXPRESSION (STRINGS)
print("(3) USE IN EXPRESSION WITH STRINGS")
message = f"Hello {(name := 'Python')}"
print("name:", name, "message:", message)
print("-" * 50)

print("DONE")

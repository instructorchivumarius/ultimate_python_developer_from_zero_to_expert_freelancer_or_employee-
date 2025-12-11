# Membership Operators in Python 

# ───────────────────────────────
# (1) SETUP
fruits = ["apple", "banana", "cherry"]
text = "hello world"
numbers = {1, 2, 3, 4, 5}
print("SETUP:", fruits, text, numbers)
print("-" * 50)

# ───────────────────────────────
# (2) IN with LIST
print("(2) IN with LIST")
print("'apple' in fruits:", "apple" in fruits)
print("'orange' in fruits:", "orange" in fruits)
print("-" * 50)

# ───────────────────────────────
# (3) NOT IN with LIST
print("(3) NOT IN with LIST")
print("'apple' not in fruits:", "apple" not in fruits)
print("'orange' not in fruits:", "orange" not in fruits)
print("-" * 50)

# ───────────────────────────────
# (4) IN with STRING
print("(4) IN with STRING")
print("'world' in text:", "world" in text)
print("'python' in text:", "python" in text)
print("-" * 50)

# ───────────────────────────────
# (5) IN with SET
print("(5) IN with SET")
print("3 in numbers:", 3 in numbers)
print("10 in numbers:", 10 in numbers)
print("-" * 50)

# ───────────────────────────────
# (6) NOT IN with SET
print("(6) NOT IN with SET")
print("3 not in numbers:", 3 not in numbers)
print("10 not in numbers:", 10 not in numbers)
print("-" * 50)

print("DONE")

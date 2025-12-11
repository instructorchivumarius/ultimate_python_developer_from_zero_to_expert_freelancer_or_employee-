# Operators on Dictionaries in Python 

# ───────────────────────────────
# (1) SETUP: sample dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print("SETUP:", dict1, dict2)
print("-" * 50)

# ───────────────────────────────
# (2) MERGING DICTIONARIES (| operator)
print("(2) MERGING")
merged = dict1 | dict2
print("dict1 | dict2:", merged)
print("-" * 50)

# ───────────────────────────────
# (3) UPDATE VALUES (|= operator)
print("(3) UPDATE VALUES")
dict1 |= dict2
print("dict1 after |= dict2:", dict1)
print("-" * 50)

# ───────────────────────────────
# (4) MEMBERSHIP (in, not in)
print("(4) MEMBERSHIP")
print("'a' in dict1:", "a" in dict1)
print("'z' not in dict1:", "z" not in dict1)
print("-" * 50)

# ───────────────────────────────
# (5) DICTIONARY COMPREHENSION
print("(5) COMPREHENSION")
squares = {x: x**2 for x in range(5)}
print("Squares dict:", squares)
print("-" * 50)

# ───────────────────────────────
# (6) UNPACKING (** operator)
print("(6) UNPACKING")
dict3 = {"x": 100, "y": 200}
combined = {**dict1, **dict3}
print("Combined with **:", combined)
print("-" * 50)

print("DONE")

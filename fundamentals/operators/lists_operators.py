# Operators on Lists in Python 

# ───────────────────────────────
# (1) SETUP: sample lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("SETUP:", list1, list2)
print("-" * 50)

# ───────────────────────────────
# (2) CONCATENATION (+)
print("(2) CONCATENATION")
print("list1 + list2:", list1 + list2)
print("-" * 50)

# ───────────────────────────────
# (3) REPLICATION (*)
print("(3) REPLICATION")
print("list1 * 3:", list1 * 3)
print("-" * 50)

# ───────────────────────────────
# (4) MEMBERSHIP (in, not in)
print("(4) MEMBERSHIP")
print("2 in list1:", 2 in list1)
print("7 in list1:", 7 in list1)
print("7 not in list1:", 7 not in list1)
print("-" * 50)

# ───────────────────────────────
# (5) COMPARISON
print("(5) COMPARISON")
print("list1 == [1, 2, 3]:", list1 == [1, 2, 3])
print("list1 < list2:", list1 < list2)
print("-" * 50)

# ───────────────────────────────
# (6) UNPACKING (star operator *)
print("(6) UNPACKING")
a, b, *rest = [10, 20, 30, 40, 50]
print("a:", a, "b:", b, "rest:", rest)
print("-" * 50)

print("DONE")

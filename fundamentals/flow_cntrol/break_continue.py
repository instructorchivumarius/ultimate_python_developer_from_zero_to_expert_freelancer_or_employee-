# Break and Continue in Python 

# ───────────────────────────────
# (1) BREAK in a loop
for n in [1, 2, 3, 4, 5]:
    if n == 3:
        print("Found 3 -> break")
        break
    print("n:", n)

print("-" * 50)

# ───────────────────────────────
# (2) CONTINUE in a loop
for n in [1, 2, 3, 4, 5]:
    if n % 2 == 0:
        continue  # skip even numbers
    print("odd:", n)

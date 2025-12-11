# range() and enumerate() in Python 

# ───────────────────────────────
# (1) range() in a FOR loop
for n in range(3):        # 0, 1, 2
    print("n:", n)

print("-" * 50)

# ───────────────────────────────
# (2) enumerate() with a LIST
fruits = ["apple", "banana", "cherry"]
for idx, fruit in enumerate(fruits, start=1):
    print(f"{idx}. {fruit}")

# If – Elif – Else in Python 

# ───────────────────────────────
# (1) IF – ELIF – ELSE with numbers
number = 0
if number > 0:
    print("The number is positive")
elif number == 0:
    print("The number is zero")
else:
    print("The number is negative")

print("-" * 50)

# ───────────────────────────────
# (2) IF – ELIF – ELSE with grades
grade = 85
if grade >= 90:
    print("Grade: A")
elif grade >= 75:
    print("Grade: B")
else:
    print("Grade: C or lower")

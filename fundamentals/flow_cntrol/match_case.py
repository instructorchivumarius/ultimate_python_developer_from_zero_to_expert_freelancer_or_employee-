# Match Case in Python 

# ───────────────────────────────
# (1) BASIC MATCH – WEEKDAY
day = "Monday"

match day:
    case "Monday":
        print("Start of the week")
    case "Friday":
        print("Almost weekend")
    case _:
        print("Regular day")

print("-" * 50)

# ───────────────────────────────
# (2) MATCH with NUMBERS
score = 85

match score:
    case s if s >= 90:
        print("Grade: A")
    case s if s >= 75:
        print("Grade: B")
    case _:
        print("Grade: C or lower")

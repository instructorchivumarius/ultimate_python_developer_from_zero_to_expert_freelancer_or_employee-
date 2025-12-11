# Nested If Statements in Python 

# ───────────────────────────────
# (1) NESTED IF – AGE & LICENSE
age = 19
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You are under 18")

print("-" * 30)

# ───────────────────────────────
# (2) NESTED IF – ROLE & SUBSCRIPTION
role = "user"        # try: "admin", "user"
is_active = True     # try: True, False

if role == "admin":
    if is_active:
        print("Admin panel: access granted")
    else:
        print("Admin inactive: access denied")
else:
    if is_active:
        print("User dashboard: access granted")
    else:
        print("Please activate your account")

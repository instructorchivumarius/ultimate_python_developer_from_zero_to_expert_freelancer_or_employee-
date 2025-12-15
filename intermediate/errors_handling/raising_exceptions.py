# Raising Exceptions



def divide(a, b):
    # Enforce a Business Rule: b must not be zero
    if b == 0:
        raise ValueError("b must not be zero")
    return a / b



def validate_age(age):
    # Guard Against Invalid Input
    if age < 0:
        raise ValueError("age cannot be negative")
    if age > 130:
        raise ValueError("age seems unrealistic")
    return True



def parse_int(text):
    # Chain the Original Exception for Better Debugging
    try:
        return int(text)
    except ValueError as e:
        raise ValueError(f"cannot parse integer from '{text}'") from e


def risky():
    try:
        # Some Complex Logic...
        _ = divide(10, 0)   # will raise
    except ValueError as e:
        print("Logging error inside risky():", e)
        # Decide we can't Recover Here → Re-Raise to the Caller
        raise



if __name__ == "__main__":
    # SAFE (no crashes): we catch exceptions at the call site
    # 1) Divide with Bad Input
    try:
        print("divide(4, 2) =", divide(4, 2))
        print("divide(5, 0) =", divide(5, 0))
    except ValueError as e:
        print("Caught:", e)

    # 2) Validate Age
    for a in [25, -3, 200]:
        try:
            validate_age(a)
            print(f"Age {a} is valid")
        except ValueError as e:
            print(f"Age {a} invalid ->", e)

    # 3) Parse Int with Raise from
    for text in ["42", "4two"]:
        try:
            print(f"parse_int('{text}') =", parse_int(text))
        except ValueError as e:
            print("Parse error:", e)

    # 4) Re-Raise
    try:
        risky()
    except ValueError as e:
        print("Caller caught re-raised error:", e)

    # --- Uncomment to see uncaught crash examples ---
    # divide(1, 0)
    # validate_age(-10)
    # parse_int("abc")

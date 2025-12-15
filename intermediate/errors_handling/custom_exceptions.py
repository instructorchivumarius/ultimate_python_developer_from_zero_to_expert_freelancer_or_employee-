# Custom Exceptions

# Define a custom exception for driving age
class UnderageDrivingError(Exception):
    """Raised when the age is below the legal driving age."""
    pass



def check_driving_age(age):
    if age < 18:
        raise UnderageDrivingError("You must be at least 18 to drive.")
    return "You are old enough to drive."



if __name__ == "__main__":
    # Test the Custom Exception
    ages = [16, 20]
    for age in ages:
        try:
            result = check_driving_age(age)
            print(result)
        except UnderageDrivingError as e:
            print("Caught custom exception:", e)

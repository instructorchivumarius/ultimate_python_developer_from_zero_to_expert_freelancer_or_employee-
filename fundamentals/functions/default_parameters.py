# Default and Optional Parameters in Python 

# (1) FUNCTION WITH DEFAULT PARAMETER
def greet_user(name="Guest"):
    print("Hello, " + name + "!")

# calling the function with and without argument
greet_user("Alice")
greet_user()

# (2) FUNCTION WITH TWO PARAMETERS (ONE DEFAULT)
def introduce(name, country="Unknown"):
    print("My name is " + name + " and I am from " + country)

# calling the function
introduce("Bob", "USA")
introduce("Eve")

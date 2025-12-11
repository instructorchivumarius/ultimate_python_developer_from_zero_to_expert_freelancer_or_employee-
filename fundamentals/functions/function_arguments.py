# Function Arguments and Return Values in Python 

# (1) FUNCTION WITH ONE PARAMETER
def greet_user(name):
    print("Hello, " + name + "!")

# calling the function
greet_user("Alice")
greet_user("Bob")

# (2) FUNCTION THAT RETURNS A VALUE
def add_numbers(a, b):
    return a + b

# calling the function and saving the result
result1 = add_numbers(3, 5)
result2 = add_numbers(10, 20)

print("First sum:", result1)
print("Second sum:", result2)

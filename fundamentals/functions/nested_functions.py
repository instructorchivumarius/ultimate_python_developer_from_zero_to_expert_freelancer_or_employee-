# Nested Functions in Python 

# (1) FUNCTION WITH A NESTED FUNCTION
def outer_function():
    print("This is the outer function.")

    def inner_function():
        print("This is the inner function.")

    # call inner function from inside
    inner_function()

# calling the outer function
outer_function()

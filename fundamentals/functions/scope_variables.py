# Scope: Local vs Global Variables in Python 

# (1) GLOBAL VARIABLE
message = "I am global"

def show_global():
    print(message)  # can access global variable

# calling the function
show_global()

# (2) LOCAL VARIABLE
def show_local():
    local_message = "I am local"
    print(local_message)

# calling the function
show_local()

# (3) GLOBAL vs LOCAL
number = 10  # global

def change_number():
    number = 5  # local variable with the same name
    print("Inside function:", number)

# calling the function
change_number()

# check global value
print("Outside function:", number)

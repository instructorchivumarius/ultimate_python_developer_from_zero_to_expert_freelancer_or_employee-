# Collections/ Data Types: Tuples in Python

# Creating a tuple
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Days of the week:", weekdays)

# Accessing elements
print("First day:", weekdays[0])
print("Last day:", weekdays[-1])

# Checking length
print("Number of days:", len(weekdays))

# Single-element tuple (comma is required!)
single_tuple = ("Python",)
print("Single-element tuple:", single_tuple)

# Iterating through a tuple
for day in weekdays:
    print("Day:", day)

# Tuples are immutable – you can't change them
# weekdays[0] = "Sunday"  # Will raise an Error: TypeError: 'tuple' object does not support item assignment 

# Collections/ Data Types: Lists in Python

# Creating a list
fruits = ["apples", "bananas", "pears"]
print("Fruit list:", fruits)

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Modifying an element
fruits[1] = "oranges"
print("Updated list:", fruits)

# Adding elements
fruits.append("kiwi")
print("After append:", fruits)

# Inserting at a specific position
fruits.insert(1, "grapes")
print("After insert:", fruits)

# Removing elements
fruits.remove("apples")
print("After remove:", fruits)

del fruits[0]  # delete by index
print("After del:", fruits)

# List length
print("Number of fruits:", len(fruits))

# Iterating through the list
for fruit in fruits:
    print("Fruit:", fruit)

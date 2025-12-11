# Collections/ Data Types: Sets in Python

# Creating a set (no duplicates, no order)
fruits = {"apple", "banana", "orange", "apple"}
print("Fruits set:", fruits)  # duplicates removed

# Adding an element
fruits.add("kiwi")
print("Added kiwi:", fruits)

# Removing an element
fruits.remove("banana")
print("Removed banana:", fruits)

# Checking if an item exists
print("Is 'apple' in the set?", "apple" in fruits)

# Iterating through a set
for fruit in fruits:
    print("Fruit:", fruit)

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Intersection:", set1 & set2)
print("Union:", set1 | set2)
print("Difference:", set1 - set2)

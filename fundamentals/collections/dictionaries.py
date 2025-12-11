# Collections/ Data Types: Dictionaries in Python

# Creating a dictionary
student = {
    "name": "Ana",
    "age": 21,
    "major": "Computer Science"
}
print("Student dictionary:", student)

# Accessing values
print("Student's name:", student["name"])
print("Age:", student.get("age"))

# Adding a new key-value pair
student["year"] = 3
print("Updated dictionary:", student)

# Modifying a value
student["age"] = 22
print("After modification:", student)

# Removing a key
del student["major"]
print("After deletion:", student)

# Iterating through dictionary
for key, value in student.items():
    print(f"{key}: {value}")

# Check if key exists
if "name" in student:
    print("The key 'name' exists.")

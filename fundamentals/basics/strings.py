# Strings in Python

# Defining a string with double quotes
message = "Hello, world!"
print(message)

# String with single quotes
another_message = 'Python is awesome!'
print(another_message)

# Multiline strings (triple quotes)
long_text = """This is
a string
across multiple lines."""
print(long_text)

# Concatenation
first_name = "Marius"
last_name = "Chivu"
full_name = first_name + " " + last_name
print(full_name)

# F-string (modern formatting)
formatted_message = f"My name is {first_name} {last_name}."
print(formatted_message)

# Useful string functions
print(message.upper())     # uppercase
print(message.lower())     # lowercase
print(len(message))        # string length
print("world" in message)  # content check
print(message.replace("Hello", "Hi"))

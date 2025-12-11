# Writing Text Files (2025)

# (1) CREATE EMPTY FILE
file = open("intermediate/working_with_files/example.txt", "w")   # creates the file if it does not exist
file.close()

# (2) WRITE CONTENT INTO FILE
file = open("intermediate/working_with_files/example.txt", "w")
file.write("This is the first line.\n")
file.write("This is the second line.\n")
file.close()

# (3) OVERWRITE FILE
# file = open("intermediate/working_with_files/example.txt", "w")
# file.write("The old content is replaced.\n")
# file.close()

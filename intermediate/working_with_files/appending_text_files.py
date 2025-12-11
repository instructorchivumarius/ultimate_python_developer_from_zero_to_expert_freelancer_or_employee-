# Appending to Text Files 

# (1) APPEND ONE LINE
file = open("intermediate/working_with_files/example.txt", "a")
file.write("Appended line 1.\n")
file.close()

# (2) APPEND MULTIPLE LINES
file = open("intermediate/working_with_files/example.txt", "a")
file.writelines([
    "Appended line 2.\n",
    "Appended line 3.\n"
])
file.close()

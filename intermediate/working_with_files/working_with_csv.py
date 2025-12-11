# Working with CSV Files
import csv

# (1) CREATE CSV FILE AND WRITE HEADER
file = open("intermediate/working_with_files/data.csv", "w", newline="")   # "w" creates the file; newline="" avoids extra blank lines (Windows)
writer = csv.writer(file)
writer.writerow(["Name", "Age", "City"])
file.close()

# (2) WRITE DATA ROWS
file = open("intermediate/working_with_files/data.csv", "a", newline="")   # "a" adds new rows at the end
writer = csv.writer(file)
writer.writerow(["Alice", 25, "New York"])
writer.writerow(["Bob", 30, "London"])
file.close()

# (3) READ CSV FILE
file = open("intermediate/working_with_files/data.csv", "r", newline="")
reader = csv.reader(file)
for row in reader:
    print("Row:", row)
file.close()

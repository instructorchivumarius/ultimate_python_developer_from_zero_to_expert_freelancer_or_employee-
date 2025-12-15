# Python Standard Library Examples
# Demonstrating a few useful built-in modules.

# (1) DATETIME EXAMPLE
import datetime

today = datetime.date.today()
print("Today's date is:", today)

# (2) RANDOM EXAMPLE
import random

number = random.randint(1, 10)
print("Random number between 1 and 10:", number)

# (3) OS EXAMPLE
import os

files = os.listdir(".")
print("Files in current directory:", files)

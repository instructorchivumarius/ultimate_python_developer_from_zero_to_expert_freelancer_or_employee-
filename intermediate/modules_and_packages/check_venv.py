# Verify the virtual environment by importing a package installed inside it
# Run this only AFTER activating the virtual environment

from colorama import Fore, Style
import sys

print("Python executable:", sys.executable)
print(Fore.GREEN + "Virtual environments keep project packages isolated!")
print(Style.RESET_ALL + "Back to normal.")

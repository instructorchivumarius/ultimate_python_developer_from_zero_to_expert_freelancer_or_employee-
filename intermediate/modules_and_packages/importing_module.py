# Different ways to import and use the calculator module

# (1) STANDARD IMPORT
import calculator
print("Standard:", calculator.add(2, 3))

# (2) IMPORT WITH ALIAS
import calculator as calc
print("Alias:", calc.subtract(10, 4))

# (3) IMPORT SPECIFIC FUNCTIONS
from calculator import multiply, divide
print("Multiply:", multiply(3, 5))
print("Divide:", divide(10, 2))

# (4) IMPORT ALL (NOT RECOMMENDED IN PRACTICE)
from calculator import *
print("Star import:", add(7, 8))

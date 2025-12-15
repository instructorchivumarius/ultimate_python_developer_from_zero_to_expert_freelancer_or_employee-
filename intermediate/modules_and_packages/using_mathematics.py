# Using our mathematics custom package with multiple modules

# (1) IMPORT FROM SUBMODULES
from mathematics import math_tools, text_tools

# (2) CALL FUNCTIONS FROM math_tools
print("Add:", math_tools.add(3, 4))
print("Multiply:", math_tools.multiply(5, 6))

# (3) CALL FUNCTIONS FROM text_tools
print(text_tools.shout("hello"))
print(text_tools.whisper("HELLO"))

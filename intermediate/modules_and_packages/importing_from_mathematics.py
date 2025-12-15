# Different ways to import from our mathematics package

# (1) IMPORT FULL SUBMODULE
import mathematics.math_tools
print("Add:", mathematics.math_tools.add(2, 3))

# (2) IMPORT WITH ALIAS
import mathematics.text_tools as txt
print("Shout:", txt.shout("hello"))

# (3) IMPORT SPECIFIC FUNCTIONS
from mathematics.math_tools import multiply
print("Multiply:", multiply(4, 5))

# (4) IMPORT MULTIPLE FUNCTIONS
from mathematics.text_tools import shout, whisper
print(shout("bye"))
print(whisper("LOUD"))

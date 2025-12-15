# Using wildcard imports from wildcard.py

# (1) IMPORT EVERYTHING WITH *
from mypackage.wildcard import *

print("Add:", add(2, 3))
print("Multiply:", multiply(4, 5))

# (2) TRY TO USE A FUNCTION NOT IN __all__
# This will cause an error, because secret_function is excluded.
try:
    print(secret_function())
except NameError:
    print("secret_function is not available with * import")

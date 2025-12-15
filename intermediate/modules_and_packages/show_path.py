# Show the Python module search path

import sys

print("Module Search Path:")
for path in sys.path:
    print(" -", path)

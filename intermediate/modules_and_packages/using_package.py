# Using our package module

# (1) IMPORT FROM THE PACKAGE FOLDER
# The folder name is the package name, and inside it we have package.py
# Example import styles (pick one and keep it in your file):

# Style A: import the submodule with an alias
import mypackage.package as package

# (2) CALL FUNCTIONS FROM THE SUBMODULE
print(package.greet("Alice"))
print("Double 7 =", package.double(7))

# --- Alternative styles (for demo in class; keep commented) ---
# Style B: from mypackage import package
# from mypackage import package
# print(package.greet("Bob"))

# Style C: from mypackage.package import greet, double
# from mypackage.package import greet, double
# print(greet("Carol"))
# print(double(10))

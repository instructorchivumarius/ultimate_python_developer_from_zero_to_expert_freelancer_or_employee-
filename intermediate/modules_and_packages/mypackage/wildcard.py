# __all__ and Wildcard Imports
# Demonstrating how to control wildcard imports.

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def secret_function():
    return "This is a secret!"

# (1) __all__ controls what gets imported with *
__all__ = ["add", "multiply"]

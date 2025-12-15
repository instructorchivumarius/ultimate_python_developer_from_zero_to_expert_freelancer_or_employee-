# Executing Modules as Scripts
# A module that can be run directly or imported.

def greet(name):
    return f"Hello, {name}!"

# (1) MAIN BLOCK
if __name__ == "__main__":
    print("Running runnable.py directly")
    print(greet("Alice"))

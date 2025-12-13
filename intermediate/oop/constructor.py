# [1] The Constructor
#     In this lesson, we learned how to use the constructor method __init__.
#     The constructor runs automatically when a new object is created.
#     It is used to initialize object attributes.
#
# [2] The __str__ Special Method
#     We continued in the same file constructor.py from the previous lesson.
#     In that lesson, we added __str__ to define how the object prints.
#
# [3] Other Special Methods
#     In this lesson, we add two more dunder methods:
#       • __len__ → allows len(object)
#       • __del__ → runs when an object is about to be destroyed
#     We keep previous code and comment out what we don’t use now.
#____________________________________________________________________________________________


# [1]-1 DEFINE CLASS PERSON WITH CONSTRUCTOR
class Person:
    # [1]-1-1 CONSTRUCTOR
    def __init__(self, name, age):
        # Instance attributes initialized when object is created
        self.name = name
        self.age = age

    # [2]-1 ADD __str__ METHOD (kept from previous lesson)
    def __str__(self):
        return f"{self.name} is {self.age} years old."

    # [3]-1 ADD __len__ METHOD 
    def __len__(self):
        # Demo choice: define the “length” of a Person as their age
        return self.age

    # [3]-2 ADD __del__ METHOD 
    def __del__(self):
        # Called when the object is about to be destroyed (by GC or del)
        print(f"Object {self.name} is being deleted.")


# [1]-2 CREATE FIRST OBJECT
p1 = Person("Alice", 25)

# [1]-3 CREATE SECOND OBJECT
p2 = Person("Bob", 30)


# [1]-4 ACCESS ATTRIBUTES (kept for reference, not used now)
# print("Person 1:", p1.name, "-", p1.age, "years old")
# print("Person 2:", p2.name, "-", p2.age, "years old")

# [2]-2 PRINT OBJECTS DIRECTLY (uses __str__) — not focus of this lesson
# print(p1)
# print(p2)


# [3]-3 USE __len__ (calls __len__)
print("Age via len(p1):", len(p1))

# [3]-4 DELETE AN OBJECT (calls __del__)
del p1

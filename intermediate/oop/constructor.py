# II-2.17 The __str__ Special Method
# [1] The Constructor
#     In this lesson, we learn how to use the constructor method __init__.
#     The constructor runs automatically when a new object is created.
#     It is used to initialize object attributes.
#
# [2] The __str__ Special Method
#     We continue in the same file constructor.py from the previous lesson.
#     In this lesson, we add the __str__ method to define how our object
#     is displayed when printed — returning a human-readable string.
#____________________________________________________________________________________________


# [1]-1 DEFINE CLASS PERSON WITH CONSTRUCTOR
class Person:
    # [1]-1-1 CONSTRUCTOR
    def __init__(self, name, age):
        # Instance attributes initialized when object is created
        self.name = name
        self.age = age


    # [2]-1 ADD __str__ METHOD 
    def __str__(self):
        return f"{self.name} is {self.age} years old."


# [1]-2 CREATE FIRST OBJECT
p1 = Person("Alice", 25)

# [1]-3 CREATE SECOND OBJECT
p2 = Person("Bob", 30)


# [1]-4 ACCESS ATTRIBUTES (kept for reference)
# print("Person 1:", p1.name, "-", p1.age, "years old")
# print("Person 2:", p2.name, "-", p2.age, "years old")


# [2]-2 PRINT OBJECTS DIRECTLY (uses __str__)
print(p1)
print(p2)

# [1] The Constructor
#     In this lesson, we learn how to use the constructor method __init__.
#     The constructor runs automatically when a new object is created.
#     It is used to initialize object attributes.
#____________________________________________________________________________________________


# [1]-1 DEFINE CLASS PERSON WITH CONSTRUCTOR
class Person:
    # [1]-1-1 CONSTRUCTOR
    def __init__(self, name, age):
        # Instance attributes initialized when object is created
        self.name = name
        self.age = age



# [1]-2 CREATE FIRST OBJECT
p1 = Person("Alice", 25)

# [1]-3 CREATE SECOND OBJECT
p2 = Person("Bob", 30)



# [1]-4 ACCESS ATTRIBUTES
print("Person 1:", p1.name, "-", p1.age, "years old")
print("Person 2:", p2.name, "-", p2.age, "years old")

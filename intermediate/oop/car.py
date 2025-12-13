# [1] Objects
#     Starting from Objects Lesson, we define the Car class.
#     This class will be used and extended in all upcoming lessons
#
# [2] Instance Attributes
#     We continue in the same file car.py from the previous lesson.
#     In this lesson, we add Instance Attributes using the constructor __init__.
#     Instance Attributes are unique for each object.
#
# [3] Class Attributes
#     We continue in the same file car.py.
#     In this lesson, we add a Class Attribute.
#     Class attributes are shared by all objects of the class.
#____________________________________________________________________________________________


# [1]-1 DEFINE THE CAR CLASS
class Car:
    # [3]-1 DEFINE CLASS ATTRIBUTE
    wheels = 4  # Shared by all Car objects



    # [2]-1 CONSTRUCTOR WITH INSTANCE ATTRIBUTES
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color



# [2]-2 CREATE FIRST OBJECT WITH INSTANCE VALUES
car1 = Car("Tesla", "Red")

# [1]-2.2 ACCESS INSTANCE ATTRIBUTES FROM FIRST OBJECT
print("Car 1 brand:", car1.brand)
print("Car 1 color:", car1.color)

# [3]-2 ACCESS CLASS ATTRIBUTES
print("Car 1 wheels:", car1.wheels)



# [2]-3 CREATE SECOND OBJECT WITH DIFFERENT INSTANCE VALUES
car2 = Car("BMW", "Blue")

# [1]-3.2 ACCESS INSTANCE ATTRIBUTES FROM SECOND OBJECT
print("Car 2 brand:", car2.brand)
print("Car 2 color:", car2.color)

# [3]-3 ACCESS CLASS ATTRIBUTES
print("Car 2 wheels:", car2.wheels)

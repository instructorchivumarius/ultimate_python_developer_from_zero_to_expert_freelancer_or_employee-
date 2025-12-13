# II-2.3 Instance Attributes
# [1] Objects
#     Starting from Objects Lesson, we define the Car class.
#     This class will be used and extended in all upcoming lessons
# 
# [2] Instance Attributes
#     We continue in the same file car.py from the previous lesson.
#     In this lesson, we add Instance Attributes using the constructor __init__.
#     Instance Attributes are unique for each object.
#____________________________________________________________________________________________


# [1]-1 DEFINE THE CAR CLASS
class Car:
    # brand = "Tesla"
    # color = "Red"

    # [2]-1 DEFINE CONSTRUCTOR WITH INSTANCE ATTRIBUTES
    def __init__(self, brand, color):
        # [2]-1.1 Instance Attribute: brand
        self.brand = brand
        # [2]-1.2 Instance Attribute: color
        self.color = color



# [1]-2.1 CREATE FIRST OBJECT WITH VALUES
# car1 = Car()
# [2]-2 CREATE FIRST OBJECT WITH INSTANCE VALUES
car1 = Car("Tesla", "Red")

# [1]-2.2 ACCESS ATTRIBUTES FROM FIRST OBJECT
print("Car 1 brand:", car1.brand)
print("Car 1 color:", car1.color)


# [1]-3.1 CREATE SECOND OBJECT WITH DIFFERENT VALUES
# car2 = Car()
# [2]-3 CREATE SECOND OBJECT WITH DIFFERENT INSTANCE VALUES
car2 = Car("BMW", "Blue")

# [1]-3.2 ACCESS ATTRIBUTES FROM SECOND OBJECT
print("Car 2 brand:", car2.brand)
print("Car 2 color:", car2.color)

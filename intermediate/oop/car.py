# [1] Objects
#     Starting from Objects Lesson, we define the Car class.
#     This class will be used and extended in all upcoming lessons
#____________________________________________________________________________________________


# [1]-1 DEFINE THE CAR CLASS
class Car:
    brand = "Tesla"
    color = "Red"


# [1]-2.1 CREATE FIRST OBJECT WITH VALUES
car1 = Car()

# [1]-2.2 ACCESS ATTRIBUTES FROM FIRST OBJECT
print("Car 1 brand:", car1.brand)
print("Car 1 color:", car1.color)

# [1]-3.1 CREATE SECOND OBJECT WITH DIFFERENT VALUES
car2 = Car()

# [1]-3.2 ACCESS ATTRIBUTES FROM SECOND OBJECT
print("Car 2 brand:", car2.brand)
print("Car 2 color:", car2.color)

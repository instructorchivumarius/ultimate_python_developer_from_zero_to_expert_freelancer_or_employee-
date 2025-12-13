# [1] Polymorphism Basics
#     In this lesson we learn how different classes
#     can share the same method name but behave differently.
#     Polymorphism allows us to use a common interface
#     while keeping unique behaviors in each subclass.
#
# [2] Polymorphism in Functions
#     We continue in the same file polymorphism.py from the previous lesson.
#     In this lesson, we use functions that work with multiple object types.
#     Any object that implements draw() can be used with the same function.
#____________________________________________________________________________________________


# [1]-1 DEFINE PARENT CLASS SHAPE
class Shape:
    # [1]-1-1 METHOD IN PARENT CLASS
    def draw(self):
        print("Drawing a generic shape.")


# [1]-2 DEFINE CHILD CLASS CIRCLE
class Circle(Shape):
    # [1]-2-1 OVERRIDE METHOD draw()
    def draw(self):
        print("Drawing a circle.")


# [1]-3 DEFINE CHILD CLASS SQUARE
class Square(Shape):
    # [1]-3-1 OVERRIDE METHOD draw()
    def draw(self):
        print("Drawing a square.")


# [1]-4 DEFINE CHILD CLASS TRIANGLE
class Triangle(Shape):
    # [1]-4-1 OVERRIDE METHOD draw()
    def draw(self):
        print("Drawing a triangle.")


# [1]-5 CREATE OBJECTS (FROM PREVIOUS LESSON)
# c = Circle()
# s = Square()
# t = Triangle()


# [1]-6 USE POLYMORPHISM (COMMENTED, FROM PREVIOUS LESSON)
# shapes = [c, s, t]  # list of Shape references
# for sh in shapes:
#     sh.draw()       # each object responds with its own draw()


# [2]-1 DEFINE A FUNCTION THAT USES POLYMORPHISM
def render_shape(shape):
    print("Rendering shape:")
    shape.draw()      # Works for any object with draw()
    print()


# [2]-2 CREATE OBJECTS
circle = Circle()
square = Square()
triangle = Triangle()


# [2]-3 CALL FUNCTION WITH DIFFERENT OBJECTS
render_shape(circle)
render_shape(square)
render_shape(triangle)

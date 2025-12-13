# [1] Inheritance Basics
#     In this lesson we learn how one class can inherit from another.
#     Inheritance allows child classes to reuse and extend functionality
#     from a parent class, keeping the code clean and organized.
#
# [2] Method Overriding
#     We continue in the same file inheritance.py from the previous lesson.
#     In this lesson, we learn how child classes can override parent methods
#     to provide their own specific behavior.
#____________________________________________________________________________________________


# [1]-1 DEFINE PARENT CLASS
class Animal:
    # [1]-1-1 METHOD IN PARENT CLASS
    def speak(self):
        print("This animal makes a sound.")



# [1]-2 DEFINE CHILD CLASS DOG
class Dog(Animal):
    # [1]-2-1 METHOD IN DOG CLASS
    def bark(self):
        print("The dog barks: Woof!")

    # [2]-1 OVERRIDE METHOD speak()
    def speak(self):
        print("The dog says: Woof!")



# [1]-3 DEFINE CHILD CLASS CAT
class Cat(Animal):
    # [1]-3-1 METHOD IN CAT CLASS
    def meow(self):
        print("The cat meows: Meow!")

    # [2]-2 OVERRIDE METHOD speak()
    def speak(self):
        print("The cat says: Meow!")



# [1]-4 CREATE OBJECTS AND USE METHODS (from previous lesson)
dog = Dog()
dog.speak()   # Inherited method (now overridden)
# dog.bark()    # Specific to Dog

cat = Cat()
cat.speak()   # Inherited method (now overridden)
# cat.meow()    # Specific to Cat

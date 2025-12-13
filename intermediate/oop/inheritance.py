# [1] Inheritance Basics
#     In this lesson we learn how one class can inherit from another.
#     Inheritance allows child classes to reuse and extend functionality
#     from a parent class, keeping the code clean and organized.
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



# [1]-3 DEFINE CHILD CLASS CAT
class Cat(Animal):
    # [1]-3-1 METHOD IN CAT CLASS
    def meow(self):
        print("The cat meows: Meow!")



# [1]-4 CREATE OBJECTS AND USE METHODS
dog = Dog()
dog.speak()   # Inherited method
dog.bark()    # Specific to Dog

cat = Cat()
cat.speak()   # Inherited method
cat.meow()    # Specific to Cat

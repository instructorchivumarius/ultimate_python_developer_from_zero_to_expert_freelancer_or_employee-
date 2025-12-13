# [1] Encapsulation 
#     In this lesson we learn how encapsulation hides data inside a class.
#____________________________________________________________________________________________


# [1]-1 DEFINE BASE CLASS VEHICLE
class Vehicle:
    # [1]-1-1 PUBLIC ATTRIBUTE
    brand = "Generic Vehicle"

    # [1]-1-2 PROTECTED ATTRIBUTE
    _fuel_capacity = 50   # Convention: should not be accessed directly

    # [1]-1-3 PRIVATE ATTRIBUTE
    __engine_number = "ENG-12345"  # Completely hidden outside the class


    # [1]-2 PUBLIC METHOD
    def show_info(self):
        print("Brand:", self.brand)
        print("Fuel capacity:", self._fuel_capacity)
        print("Engine number:", self.__engine_number)


# [1]-3 CREATE OBJECT
car = Vehicle()


# [1]-4 CALL METHOD
car.show_info()

# [1]-5 TRY TO ACCESS ATTRIBUTES DIRECTLY
print("Public brand:", car.brand)
print("Protected fuel capacity (not recommended):", car._fuel_capacity)

# Uncommenting the next line would cause an error
# print("Private engine number:", car.__engine_number)

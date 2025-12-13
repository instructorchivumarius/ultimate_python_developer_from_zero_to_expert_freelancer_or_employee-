# [1] Encapsulation 
#     In this lesson we learn how encapsulation hides data inside a class.
#
# [2] Private and Protected Variables
#     We continue in the same file encapsulation.py from the previous lesson.
#     We focused on access levels (_protected, __private) and safe internal access.
#
# [3] Getters and Setters
#     We continue in the same file encapsulation.py.
#     In this lesson, we add methods to READ and UPDATE private data safely:
#       • Getter → returns a private value in a controlled way
#       • Setter → updates a private value in a controlled way (optionally validate)
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


    # [2]-1 NEW PUBLIC METHOD (safe access demo)
    def show_attributes(self):
        print("Fuel capacity:", self._fuel_capacity)
        print("Engine number:", self.__engine_number)


    # [3]-1 GETTER METHOD
    def get_engine_number(self):
        return self.__engine_number

    # [3]-2 SETTER METHOD
    def set_engine_number(self, new_number):
        # (optional simple validation for demo; keep it very basic)
        if isinstance(new_number, str) and new_number.strip():
            self.__engine_number = new_number
        else:
            print("Invalid engine number. Update skipped.")


# [1]-3 CREATE OBJECT
car = Vehicle()


# [1]-4 CALL METHOD (kept from previous lesson, not used now)
# car.show_info()


# [1]-5 TRY TO ACCESS ATTRIBUTES DIRECTLY (kept from previous lesson)
# print("Public brand:", car.brand)
# print("Protected fuel capacity (not recommended):", car._fuel_capacity)
# Uncommenting the next line would cause an error
# print("Private engine number:", car.__engine_number)


# [2]-2 ACCESS PROTECTED ATTRIBUTE (works, but not recommended) — not used in this lesson
# print("Accessing protected fuel capacity:", car._fuel_capacity)

# [2]-3 TRY TO ACCESS PRIVATE ATTRIBUTE (would raise an error) — not used in this lesson
# print("Accessing private engine number:", car.__engine_number)

# [2]-4 USE METHOD TO ACCESS PRIVATE ATTRIBUTE SAFELY — not used in this lesson
# car.show_attributes()


# [3]-3 USE GETTER
print("Engine number (via getter):", car.get_engine_number())

# [3]-4 USE SETTER
car.set_engine_number("ENG-98765")

# [3]-5 USE GETTER AGAIN
print("Updated engine number (via getter):", car.get_engine_number())

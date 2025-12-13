# [▬] Abstraction shows WHAT an object does, not HOW it does it.
#     We hide complex details and show only what’s essential.
#____________________________________________________________________________________________


# (1) DEFINE PARENT CLASS (GENERAL MODEL)
class Device:

    # (1-1) GENERIC METHOD – to be redefined in subclasses
    def turn_on(self):
        print("Generic device: subclasses should define their own 'turn_on()' method.")

    # (1-2) SHARED METHOD – same for all subclasses
    def turn_off(self):
        print("Device is now turned OFF.")



# (2) DEFINE CHILD CLASS – FAN
class Fan(Device):

    # (2-1) IMPLEMENT SPECIFIC turn_on() FOR FAN
    def turn_on(self):
        print("Fan: Blades are spinning, air is circulating.")



# (3) DEFINE CHILD CLASS – LIGHT
class Light(Device):

    # (3-1) IMPLEMENT SPECIFIC turn_on() FOR LIGHT
    def turn_on(self):
        print("Light: The room is now illuminated.")



# (4) CREATE OBJECTS
fan = Fan()
lamp = Light()



# (5) USE COMMON INTERFACE (SAME METHODS, DIFFERENT RESULTS)
fan.turn_on()
fan.turn_off()

lamp.turn_on()
lamp.turn_off()



# (6) OPTIONAL – USE PARENT CLASS DIRECTLY (prints generic message)
# generic = Device()
# generic.turn_on()

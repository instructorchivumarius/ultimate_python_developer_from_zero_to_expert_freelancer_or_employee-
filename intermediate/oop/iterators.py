# [▬] Iterators
#     Iterators let us go through elements one by one — like reading a list step by step.
#     Any object that supports __iter__() and __next__() is called an *iterator*.
#____________________________________________________________________________________________


# (1) DEFINE A SIMPLE ITERATOR CLASS
class Countdown:
    # (1-1) CONSTRUCTOR: set the starting number
    def __init__(self, start):
        self.current = start

    # (1-2) DEFINE __iter__() — returns the iterator object itself
    def __iter__(self):
        return self

    # (1-3) DEFINE __next__() — returns next value in the sequence
    def __next__(self):
        if self.current <= 0:
            # Stop the iteration when we reach 0
            raise StopIteration
        value = self.current
        self.current -= 1
        return value



# (2) CREATE AN ITERATOR OBJECT
countdown = Countdown(3)



# (3) USE A FOR LOOP (automatically calls __iter__() and __next__())
for number in countdown:
    print("Counting down:", number)

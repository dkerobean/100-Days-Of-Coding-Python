# advanced arguments (args and kwargs)

def add(*args):
    for n in args:
        print(n)

add(4,6,4234,43,43,3,43,43,4)


def add_numbers(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add_numbers(2,4,1,4,5))


# all arguments are passed inside a tupple


# Kwargs (stored inside a dictionary)

def calculate(n, **kwargs):
    for key, value in kwargs.items():
        print(key, value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(3, add=3, multiply=4)

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(make="Nissan", model="electric")
print(my_car)


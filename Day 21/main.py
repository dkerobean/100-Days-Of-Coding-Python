#inheritance

class Animal:
    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("inhale and exhale")

    def eat(self):
        print("put food in stomach")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("move in water")

    def breathe(self):
        super().breathe()
        print("But under water")


shark = Fish()
shark.breathe()


piano_keys = ["a", "b", "c", "d", "e", "f", "g"]

print(piano_keys[2:5])
#2 to the end
print(piano_keys[2:])

#up to 5th position
print(piano_keys[:5])

#with step of 2
print(piano_keys[2:5:2])

#skip 2nd iitems
print(piano_keys[::2])

#reverse list
print(piano_keys[::-1])



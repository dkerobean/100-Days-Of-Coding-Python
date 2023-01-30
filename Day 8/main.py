
#funnction
def greet(name):
    print(f"hello {name}")
    print(f"how are you {name}")
    print(f"Good bye {name}")


greet("Dickie")

#more than one input

def greet2(name, location):
    print(f"hello {name}")
    print(f"what is it like in {location}")

greet2("dickie", "Accra")

greet2(location="Accra", name="Dick")

#exercise
import math
def wall(height, width, coverage):
    cans = ( height * width ) / coverage
    print(math.ceil(cans))

wall(3, 9, 5)

print(2%8)



def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print("Its a prime number")
    else:
        print("its not a prime")

number = int(input("Enter number: "))

prime_checker(number)










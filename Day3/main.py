# if else statement

height = int(input("What is your height? "))
age = int(input("Enter your age "))
bill = 0

if height >= 120:
    print("You can ride")
    if age < 12:
        bill = 5
        print("pay 5")
    elif age <= 18:
        bill = 7
        print("pay 7")
    else:
        bill = 12
        print("pay 12")

    wants_photo = input("Do you want a photo, Y or N ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is {bill}")

else:
    print("wear heels")

# excersise
number = int(input("Enter your number "))

if number % 2 > 0:
    print("number is odd")
else:
    print("number is even")

# exercise

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

BMI = round(weight / height ** 2, 1)

if BMI < 18.5:
    print(f"Your bmi is {BMI}, you are underweight")
elif BMI < 25:
    print(f"Your bmi is {BMI}, you hve normal weight")
elif BMI < 30:
    print(f"Your bmi is {BMI}, you are underweight")
elif BMI < 35:
    print(f"Your bmi is {BMI}, you are obese")
else:
    print(f"Your bmi is {BMI}, you are clinically obese")

# exercise (leap year)

year = int(input("Enter year: "))

if year % 4 == 0 and year % 100 == 0 or year % 400 == 0:
    print("Leap")
else:
    print("not a leap")

# exercise (pizza order)

print("Welcome to python pizza")

size = input("What size do you want? S,M, L ")
add_pepperoni = input("Do you want peperoni? Y or N ")
extra_cheese = input("Do you want extra cheese ? Y or N ")
bill = 0

if size == "S":
    bill = 15
    if extra_cheese == "Y":
        bill += 1
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill = 20
    if extra_cheese == "Y":
        bill += 1
    if add_pepperoni == "Y":
        bill += 3
elif size == "L":
    bill = 25
    if extra_cheese == "Y":
        bill += 1
    if add_pepperoni == "Y":
        bill += 3
else:
    print("please enter a correct size")

print(f"Your final bill is: ₵{bill}")

# logical operators
# AND both true
# OR just one true
# NOT reverse condition

# exercise
first_name = input("Enter your name: ")
second_name = input("Enter his or her name: ")

combined_name = first_name + second_name

T = combined_name.lower().count("t")
R = combined_name.lower().count("r")
U = combined_name.lower().count("u")
E = combined_name.lower().count("e")

L = combined_name.lower().count("l")
O = combined_name.lower().count("o")
V = combined_name.lower().count("v")
E = combined_name.lower().count("e")

score = str(T + R + U + E) + str( L + O + V + E)
love_score = int(score)

if (love_score < 10) or (love_score > 90):
    print(f"your score is {score}, you go together like coke and mentos")
elif (love_score >= 40) and (love_score <= 50):
    print(f"your score is {score}, you are alright together")
else:
    print(f"your score is {score}")










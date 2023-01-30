#Data types

#subscripting
name = "Hello world"
print(name[-1])

# replace comma with underscore 123,243,234
number = 123_243_234
print(number)

#check data type
type(number)

#exercise

number = input("enter number")
answer = int(number[0]) + int(number[1])
print(number[0] + " + " + number[0] + " = " + str(answer))

#exponent
dig = 2**2

#PEMDAS
#paranthesis, exponents, multiplicatin, division, addition, subtraction

#code exercise(BMI calculator)

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

BMI = int(int(weight) / float(height) ** 2)

print("Your BMI is " + str(BMI))

# round number
print(round(2.55555, 2))
print(round(8/3,2))

#floor
print(5//2)

#Fstringd
score = 10
winning = True
like = 5.3

print(f"your score is {score}, your winning rate is {like}")

# 1 year = 365 days, 1 year = 2 weeks, 1 year = 12 months


age = int(input("What is your age ? "))
years_remaining = 70 - age
days_remaining = years_remaining * 365
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52

print(f"You have {days_remaining} days, {months_remaining} months and {years_remaining} years")








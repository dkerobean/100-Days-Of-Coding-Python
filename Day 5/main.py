#loops
fruits = ["apple", "peach", "pear"]

for fruit in fruits:
    print(fruit)

#exercise
students_height = [180, 124, 165, 173, 189, 169, 146]
total_height = 0

for height in students_height:
    total_height += height

average_height = round(total_height / len(students_height))
print(average_height)

#exercise
scores = input("Enter students scores: ").split(",")
highest = 0


for score in scores:
    if int(score) > highest:
        highest = int(score)

print(f"the highest score is {highest}")

#range function
for i in range(1, 11, 2):
    print(i)

sum = 0
for number in range(1, 101):
    sum += number

print(sum)

#exercise
total = 0
for i in range(2, 101, 2):
    total += i
    print(total)

#exercise
for i in range(1, 101):
    if (i % 3 == 0) and (i % 5 == 0):
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fiz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)









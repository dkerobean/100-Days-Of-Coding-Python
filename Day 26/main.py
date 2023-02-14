# list comprehension (create new list from a previous llist)
import pandas

numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

# using list comprehension
# new_list = [new_item for item in list]

new_list2 = [n + 1 for n in numbers]
print(new_list2)


name = "Angela"
name_list = [letter for letter in name]
print(name_list)


new_range = [num * 2 for num in range(1, 5)]
print(new_range)


# conditional list comprehension
# new_lists = [new_item for item in list if test]

names = ["dickson", "manfred", "eric", "yaw", "sandy", "freddie", "alexander"]
new_names = [name for name in names if len(name) < 6]
print(new_names)

upper_names = [name.upper() for name in names if len(name) > 6]
print(upper_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)

with open("file1.txt") as f:
    file1 = f.readlines()

with open("file2.txt") as f:
    file2 = f.readlines()


same_numbers = [int(num) for num in file1 if num in file2]
print(f"here {same_numbers}")


# dictionary comprehension
#new_dict = {new_key:new_value for item in list}
#new_dict = {new_key:new_value for (key, value) in dict.items() if test}

import random

student_scores = {student:random.randint(1, 100) for student in names}
print(student_scores)

passed_students = {student:score for (student, score) in student_scores.items() if score >= 70}
print(passed_students)


# exercise
sentence = "What is the Airspeed Velocity of an unladen Swallow?"
words = sentence.split()

result = {word:len(word) for word in words }
print(result)


# exercise
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}


weather_f = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items() }
print(weather_f)


# panda Dataframe

student_dict = {
    "student": ["Angela", "Dickson", "Eric"],
    "Score": [56, 76, 98]
}

for (key, value) in student_dict.items():
    print(value)

student_data = pandas.DataFrame(student_dict)
print(student_data)

# loop through dataframe
for (index, row) in student_data.iterrows():
    print(row.student)
    print(row.score)
    if row.student == "Dickson":
        print(row.Score)










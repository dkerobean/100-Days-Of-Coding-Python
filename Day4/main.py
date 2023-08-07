  # random module

import random

# integer
random_number = random.randint(1, 49)
print(random_number)

#float from 0.000 to 0.999
random_float = random.random()
print(random_float)

#exercise
dice = random.randint(0,1)
print(dice)
if dice == 0:
    print("Head")
else:
    print("Tail")


#lists

regions_in_Ghana = ["Accra", "Kumasi", "Takoradi", "Oti", "Central"]
print(regions_in_Ghana[2])
print(regions_in_Ghana[-5])

regions_in_Ghana[3] = "Volta"
print(regions_in_Ghana)
regions_in_Ghana.append("Nothern")
regions_in_Ghana.extend(["Ashanti", "Brong Ahafo"])

#exercise (who is going to pay)
names = input("Enter names of people. name1, name2,...")
name_list = names.split(",")
selector = random.randint(0, len(name_list) - 1)
person_to_pay = name_list[selector]
print(f"{person_to_pay} will pay the bill!")

#nested lists
fruits = ["banana", 'apples', "pears"]
vegetables = ["tomatoes", "potatoes", "spinash"]

dirty_dozen = [vegetables, fruits]
print(dirty_dozen)

#exercise

row1 = ["🟥", "🟥", "🟥"]
row2 = ["🟥", "🟥", "🟥"]
row3 = ["🟥", "🟥", "🟥"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to place your 'X' ?")
row = int(position[1])
column = int(position[0])

print(f"row is {row}")
print(f"column is {column}")

selected_row = map[row - 1]
selected_row[column - 1] = "X"


# if row == 1:
#     row1[column - 1] = "X"
# elif row == 2:
#     row2[column - 1] = "X"
# elif row == 3:
#     row3[column - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")













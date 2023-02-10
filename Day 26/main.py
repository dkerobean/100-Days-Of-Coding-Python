# list comprehension (create new list from a previous llist)
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


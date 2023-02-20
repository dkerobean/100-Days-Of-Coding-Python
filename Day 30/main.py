try:
    dict = {1: "one", 2: "two"}
    print(dict[3])
    file = open("file.txt")
except FileNotFoundError as error_message:
    print(error_message)
except KeyError:
    print("key does not exist error")
else:
    print("file passed successfully")
finally:
    print("Happens no matter what happens")


# raise your exceptions

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Height should not exceed 3")

bmi = weight / height ** 2
print(bmi)

# code exercise
fruits = ["Apple", "Pear", "Orange"]

# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("fruit pie")
    else:
        print(fruit + " pie")


make_pie(1)

# code exercise

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass

print(total_likes)

# exercise

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
is_continue = True

while is_continue:
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Enter a valid word")
        pass
    else:
        print(output_list)
        is_continue = False









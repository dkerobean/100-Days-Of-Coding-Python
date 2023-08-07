PLACEHOLDER = "[name]"

# change names to list
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()


with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()

    for name in names:
        stripped_name = name.strip()
        letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as letter:
            letter.write(letter_content)


import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear

print(logo)

chosen_word = random.choice(word_list)
display = []
lives = 6

for _ in range(len(chosen_word)):
    display += "_"

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You loose")

    print(display)
    #print(chosen_word)

    if "_" not in display:
        end_of_game = True
        print("You win")

    print(stages[lives])

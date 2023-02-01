import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
computer_guess = random.randint(1, 100)

EASY_LEVEL = 10
HARD_LEVEL = 5


def guess_num(num):
    """ takes number of guesses as input and checks if users guess match computers guess"""
    attempts = num
    should_continue = True

    while should_continue and attempts != 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_guess = int(input("Guess a number: "))
        if user_guess == computer_guess:
            print(f"You got it! The answer was {computer_guess}.")
            should_continue = False
        elif user_guess > computer_guess:
            print("Too high")
            print("Guess again")
            attempts -= 1
        elif user_guess < computer_guess:
            print("Too low")
            print("Guess again")
            attempts -= 1

    else:
        print(f"You run out of guesses,you loose 😒. The answer was {computer_guess}.")


if difficulty == "hard":
    print(computer_guess)
    guess_num(HARD_LEVEL)
else:
    guess_num(EASY_LEVEL)




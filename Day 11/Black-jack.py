import random
from art import logo
import os
cls = lambda: os.system('cls')


def play_blackjack():
    user_cards = []
    computer_cards = []
    game_over = False

    def deal_card():
        """ Returns a random card from the deck """
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
        card = random.choice(cards)
        return card

    def calculate_score(cards):
        """ Takes a list of cards and calculates the total score
        and also checks for black jack"""

        if 11 in cards and 10 in cards and len(cards) == 2:
            return 0

        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)

        return sum(cards)

    def compare(user_score, computer_score):
        """ determines who won by using black jack rules"""
        if user_score == computer_score:
            return "Draw 😒"
        elif computer_score == 0:
            return "You lost, computer has a black jack"
        elif user_score == 0:
            return "Won, You go a black jack"
        elif user_score > 21:
            return "You went over, You loose"
        elif computer_score > 21:
            return "Computer went over, you win"
        elif user_score > computer_score:
            return "You win"
        elif computer_score > user_score:
            return "computer wins"
        else:
            return "You loose"

    for _ in range(2):
        deal_card()
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        print(logo)
        users_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"user cards {user_cards}, score {users_score}")
        print(f"computer_cards {computer_cards[0]}")

        if users_score == 0 or computer_score == 0 or users_score > 21:
            game_over = True
        else:
            user_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_deal == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score {users_score}")
    print(f"Computer final hand: {computer_cards}, final score {computer_score}")
    print(compare(users_score, computer_score))


while input("Do you want to play black jack? Type 'y' or 'n': ") == 'y':
    cls()
    play_blackjack()














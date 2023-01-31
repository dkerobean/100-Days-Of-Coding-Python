from replit import clear
from art import logo

print(logo)

to_continue = True
bidders = {}


def add_bidders(user_name, user_bid):
    bidders[user_name] = user_bid
    highest_bid = 0
    highest_bidder = ""

    for user in bidders:
        if bidders[user] > highest_bid:
            highest_bid = bidders[user]
            highest_bidder = user

    print(f"{highest_bidder} won with a bid of {highest_bid}")


while to_continue:
    print("Welcome to the blind auction program")
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: "))
    finnish = input("Are there other bidders? Type 'yes' or 'no' ")
    add_bidders(user_name=name, user_bid=bid)
    if finnish == 'no':
        to_continue = False
    else:
        clear()









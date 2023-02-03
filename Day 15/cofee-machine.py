MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 1800,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

money = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

drink_choice = input("“What would you like? (espresso/latte/cappuccino): ")


def check_resources(drink):
    is_enough = True
    ingredients = MENU[drink]["ingredients"]
    for items in ingredients:
        if ingredients[items] > resources[items]:
            print(f"not enough {items}")
            is_enough = False
    return is_enough


def print_report():
    for item in resources:
        print(f"{item}: {resources[item]}")
    print(f"Money: ${money}")


def process_coins():
    print("insert coins")


def make_drink(choice):
    if choice == "espresso":
        if check_resources(choice):
            process_coins()
        else:
            print("Not enough resources")

    elif choice == "latte":
        print(choice)
    elif choice == "cappuccino":
        print(choice)
    elif choice == "off":
        print("Off for maintenance")
    elif choice == "report":
        print_report()
    else:
        print("Enter a valid input")


make_drink(drink_choice)

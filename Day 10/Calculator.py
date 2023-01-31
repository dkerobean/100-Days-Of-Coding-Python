from art import logo


def add(n1, n2):
    """ Takes two numbers and adds them """
    return n1 + n2


def subtract(n1, n2):
    """ Takes two numbers and subtracts second from first number """
    return n1 - n2


def divide(n1, n2):
    """ Takes two numbers and divides them """
    return n1 / n2


def multiply(n1, n2):
    """ Takes two numbers and multiplies them """
    return n1 * n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    num1 = float(input("Whats the first number?: "))
    for operator in operations:
        print(operator)

    should_continue = True

    while should_continue:
        operator = input("Pick an operation from the line above: ")
        num2 = float(input("Whats the next number?: "))

        calculate = operations[operator]
        answer = calculate(num1, num2)

        print(f"{num1} {operator} {num2} = {answer}")

        if input(f"Type 'y' to continue to calculate with {answer}, or type 'n' to start a new calculation.: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()




















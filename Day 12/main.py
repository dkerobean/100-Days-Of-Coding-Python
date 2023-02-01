#scope
apples = 1
banana = 1


def buy_apples():
    global apples
    apples += 5
    print(f"function: {apples}")

def garden():
    return banana + 1

fruit = garden()


buy_apples()
print(f"outside apples {apples}")

#avoid modifying global scope

#constants (all upercase)

PI = 3.14159




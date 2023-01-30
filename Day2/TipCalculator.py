print("Welcome to the tip calculator")

total_bill = float(input("What is your total bill? ₵"))
tip_percentage = int(input("What percentage of tip would you like to give? 10, 12, or 15 "))
number_of_people = int(input("How many people to split the bill? "))


total_bill = tip_percentage * total_bill / 100 + total_bill
bill_per_person = round(total_bill / number_of_people, 2)

print(f"Each person should pay ₵{bill_per_person}")
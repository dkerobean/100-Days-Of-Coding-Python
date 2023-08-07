# Write a Python program to find the maximum of two numbers?
import math


def max_numbers(*args):
    max_number = 0
    for i in args:
        if i > max_number:
            max_number = i

    return max_number


print(max_numbers(87889,6))

# Write a Python program to check prime numbers.

def check_prime(num):

    if num >= 1:
        return False

    for i in range(2, num):
        if (num % i) == 0:
            return False

    return True


print(check_prime(10))

#Write a Python factorial program without using if-else, for, and ternary operators.

def factorial(num):
    return math.factorial(num)

factorial(4)

#Write a Python program to calculate the area of a triangle.

def area_triangle(h, b):
    return (h * b / 2)

print(area_triangle(5, 4))

# Armstrong number
def arm_number(num):

    arm_sum = 0
    len_num = len(str(num))
    num_str = str(num)

    for i in range(0, len_num):
        digits = int(num_str[i]) ** len_num
        arm_sum += digits

    if arm_sum == num:
        print(f"{num} is an armstrong number")
    else:
        print(f"{num} is not armstrong number")

    print(len_num)


arm_number(370)

# Question 1:
# Write a Python function that takes a list of integers as input and returns the sum of all even numbers in the list.

def sum_integer(list_int):

    even_sum = 0

    for i in list_int:
        if i % 2 == 0:
            even_sum += i

    # list comprehension

    even_list1 = sum(i for i in list_int if i % 2 == 0)

    print(f"even {even_sum}")
    print(even_list1)

sum_integer([2,3,4,5,6,6])


# Question 2:
# Write a Python function that checks if a given word is a palindrome (a word that reads the same backward as forward).

def palindrome_check(word):

    return word[::-1] == word

print(palindrome_check("racecar"))


# Question 3:
# Implement a Python class representing a simple bank account.
# The class should have methods to deposit and withdraw funds and to check the account balance.

class BankAccount:

    def __init__(self, name, acc_number, acc_balance):
        self.name = name,
        self.acc_number = acc_number,
        self.acc_balance = acc_balance

    def deposit_money(self):
        amount = int(input("Enter the amount to deposit: "))
        if amount > 0:
            self.acc_balance += amount

    def check_account(self, amount):
        if amount > self.acc_balance:
            print(f"You do not have enough balance, your balance is {self.acc_balance}")
        else:
            balance = self.acc_balance - amount
            self.acc_balance = balance
            print(f"you have withdrawn {amount}, your balance is {balance}")

    def withdraw_money(self):
        amount = int(input("Enter amount to withdraw"))
        self.check_account(amount)

    def check_account_balance(self):
        return self.acc_balance




# Creating an instance of the BankAccount class
account = BankAccount("dickson", 100, 200)

#
# account.deposit_money()
# print(account.check_account_balance())
#
# account.withdraw_money()
# print(account.check_account_balance())


# Question 4:
# Write a Python function to find and return the second-largest number in a list of integers.


def second_largest_number(num_list):

    if len(num_list) < 2:
        return None

    first_max = max(num_list)
    num_list.remove(first_max)

    second_max = max(num_list)
    return second_max

second_largest_number([10, 20, 5, 40, 30])

#Question 5:
#Implement a Python function to remove duplicates from a list while preserving the order of elements.


def remove_duplicate(list):

    new_list = []

    for i in list:
        if i not in new_list:
            new_list.append(i)

    print(new_list)

remove_duplicate([1,1,2,3,4,5,5,6])


# Question: Write a Python function to calculate the factorial of a given number.

def factorial(n):

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

# Question: Write a Python function to remove duplicates from a list.

def remove_duplicates(list):

    unique_list = []

    for i in list:
        if i not in unique_list:
            unique_list.append(i)

    return unique_list

print(print(remove_duplicates([1, 2, 2, 3, 4, 4, 5])))


# Question: Write a Python function to count the frequency of each element in a list.

def count_frequency(list):

    frequency = {}

    # for i in list:
    #     if i not in frequency:
    #         frequency[i] = 1
    #     else:
    #         frequency[i] += 1

    for i in list:
        frequency[i] = frequency.get(i, 0) + 1

    return frequency

print(count_frequency([1, 2, 2, 3, 4, 4, 5]))



# Given a list of numbers from 1 to N (where one number is missing), write a Python function to find the missing number.

def find_number(list):

    sorted_list = sorted(list)

    n = len(list) + 1

    total_sum = n * (n + 1) // 2
    actual_sum = sum(list)

    return total_sum - actual_sum


print(find_number([1,3,2,6,7,5]))

# Write a function that prints numbers from 1 to n. But for multiples of 3, print "Fizz"
# instead of the number, and for multiples of 5, print "Buzz". For numbers that are
# multiples of both 3 and 5, print "FizzBuzz".

def fizz_buzz(n):

    for i in range(1, n+1):
        if (i % 3) and (i % 5) == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print("Buzz")

fizz_buzz(4)


# Write a function to merge two sorted lists into a single sorted list.

def merge_lists(list1, list2):

   merged_list = []
   i,j = 0, 0

   while i < len(list1) and j < len(list2):
       if list1[i] < list2[j]:
           merged_list.append(list1[i])
           i += 1
       else:
           merged_list.append(list2[j])
           j += 1

   merged_list.extend(list1[i:])
   merged_list.extend(list2[j:])

   return merged_list

print(merge_lists([1,3,5], [2,4,6]))













#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
'''
num_str = repr(number)
last_digit = num_str[-1]
last_digit = int(last_digit)
'''
check = 0
if number < 0:
    number *= -1
    check = 1

last_digit = number % 10
if check == 1:
    number *= -1
    last_digit *= -1


print(f"Last digit of {number} is {last_digit}", end=" ")
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
elif (last_digit < 6) and (last_digit != 0):
    print("and is less than 6 and not 0")

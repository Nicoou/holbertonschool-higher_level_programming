#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number2 = number % 10
if number < 0:
    number *= -1
    number2 = number % 10
    number *= -1
    number2 *= -1

if number2 > 5:
    print(f"Last digit of {number} is {number2} and is greater than 5")

elif number2 < 0:
    print(f"last digit of {number} is {number2} and is less than 6 and not 0")

elif number2 == 0:
    print(f"last digit of {number} if {number2} and is 0")

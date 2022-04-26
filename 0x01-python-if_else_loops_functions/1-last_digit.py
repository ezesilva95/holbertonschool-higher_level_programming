#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastD = number % (-10)
else:
    lastD = number % 10
if lastD > 5:
    print(f"Last digit of {number:d} is {lastD} and is greater than 5")
elif lastD < 6:
    print(f"Last digit of {number:d} is {lastD} and is less than 6 and not 0")
elif lastD == 0:
    print(f"Last digit of {number:d} is {lastD} and is 0")

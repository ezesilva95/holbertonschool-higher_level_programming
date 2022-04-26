#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastnumber = number % (-10)
else:
    lastnumber = number % 10
if lastnumber > 5:
	print(f"Last digit of {number:d} is {lastnumber:d} and is greater than 5")
elif lastnumber < 6:
	print(f"Last digit of {number:d} is {lastnumber:d} and is less than 6 and not 0")
elif lastnumber == 0:
	print(f"Last digit of {number:d} is {lastnumber:d} and is 0")

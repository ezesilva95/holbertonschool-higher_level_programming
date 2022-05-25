#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(10, 3))
print(add_integer(25, 0))
print(add_integer(-95, 5))
print(add_integer(10, -5))
print(add_integer(4, -5))
print(add_integer(3.5, 4.5))

try:
    print(add_integer([21], 3))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
try:
        print(add_integer(a, 3))
except Exception as e:
        print(e)
try:
        print(add_integer("BestSchool"))
except Exception as e:
        print(e)

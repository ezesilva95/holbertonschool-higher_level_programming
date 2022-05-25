#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("Ezequiel", "Silva")
say_my_name("Ezequiel")
say_my_name("Ezequiel", "")
try:
    say_my_name(1, "Silva")
except Exception as e:
    print(e)

try:
        say_my_name("Ezequiel", 1)
except Exception as e:
        print(e)

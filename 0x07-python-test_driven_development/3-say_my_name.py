#!/usr/bin/python3
'''
2. Say my name
function that prints My name is <first name> <last name>
'''


def say_my_name(first_name, last_name=""):
    '''
    first_name and last_name must be strings
    Return full name
    '''
    if type(first_name) is str and type(last_name) is str:
        print(f"My name is {first_name:s} {last_name:s}")
    elif type(first_name) is not str:
            raise TypeError("first_name must be a string")
    else:
        raise TypeError("last_name must be a string")

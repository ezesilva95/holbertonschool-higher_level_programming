#!/usr/bin/python3
'''
3. Print square
function that prints a square with the character #.
'''


def print_square(size):
    '''
    Print a square with #
    '''
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")

    if size == 0:
        print("", end="")
    else:
        print("\n".join(["#" * size for rows in range(size)]))

#!/usr/bin/python3
'''
4. Text indentation
function that prints a text with 2 \n after each of these char: ., ? and :
'''


def text_indentation(text):
    '''
    print text with 2 \n after . ? and :
    '''
    if type(text) is not str:
        raise TypeError("Text must be an string")

    Schar = [".", "?", ":"]
    newline = "\n\n"

    for char in text:
        print(char, end="")
        if char in Schar:
            print(newline, end="")

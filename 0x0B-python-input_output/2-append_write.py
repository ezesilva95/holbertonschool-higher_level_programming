#!/usr/bin/python3
'''
Module 2.Append to a file
'''


def append_write(filename="", text=""):
    '''
    appends a str at the end of a text file and return the num of char added
    '''
    with open(filename, mode="a", encoding="utf-8") as f:
        f.write(text)
        return len(text)

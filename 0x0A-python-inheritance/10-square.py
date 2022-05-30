#!/usr/bin/python3
'''
10. Square #1
Write a class Square that inherits from Rectangle (9-rectangle.py):
'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    inherits from Rectangle task 9
    '''
    def __init__(self, size):
        '''
        init size
        '''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

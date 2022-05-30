#!/usr/bin/python3
'''
11. Square #2
Write a class Square that inherits from Rectangle 9-rectangle.py
'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    inherits from Rectangle (9-rectangle.py)
    '''
    def __init__(self, size):
        '''
        init size
        '''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __area__(self):
        '''
        area(self)
        '''
        return self.__width * self.__height

    def __str__(self):
        '''
        prints square
        '''
        return "[Square] " + str(self.__size) + "/" + str(self.__size)

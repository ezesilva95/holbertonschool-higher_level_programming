#!/usr/bin/python3
'''
class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
'''


class Rectangle:
    '''
    class rectangle
    '''

    def __init__(self, width=0, height=0):
        '''
        initilizate rectanlges
        '''
        self.height = height
        self.width = width

    @property
    def width(self):
        '''
        get width
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        set width
        '''
        if type(value) is int:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        '''
        get height
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        set height
        '''
        if type(value) is int:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("width must be an integer")

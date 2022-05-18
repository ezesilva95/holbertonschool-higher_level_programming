#!/usr/bin/python3
'''
class Rectangle that defines a rectangle by: (based on 4-rectangle.py)
'''


class Rectangle:
    '''
    class rectangle
    '''

    def __init__(self, width=0, height=0):
        '''
        initilizate rectangles
        '''
        self.height = height
        self.width = width

    @property
    def width(self):
        '''
        get widht
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

    def area(self):
        '''
        return area of rectangle
        '''
        return self.__width * self.__height

    def perimeter(self):
        '''
        return perimeter
        '''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        '''
        print rectangle with #
        '''
        if self.__width == 0 or self.height == 0:
            return ""
        pic = "\n".join(["#" * self.__width for rows in range(self.__height)])
        return pic

    def __repr__(self):
        '''
        str representation
        '''
        return (f"Rectangle({self.width:d}, {self.height:d})")
    
    def __del__(self):
        '''
        delete instance class
        '''
        print("Bye rectangle...")


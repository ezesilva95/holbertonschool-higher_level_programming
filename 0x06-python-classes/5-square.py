#!/usr/bin/python3
'''
class Square that defines a square by: (based on 4-square.py)
'''


class Square:
    '''
    class square
    '''

    def __init__(self, size=0):
        '''
        init a square

        The size of a square is crucial for a square.
        One way to have the control is to keep it privately.
        You will see in next tasks how to get,
        update and validate the size value.
        '''
        self.size = size

    @property
    def size(self):
        '''
        get size
        '''

        return self.__size

    @size.setter
    def size(self):
        '''
        set size
        '''

        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                raise TypeError("size must be an integer")
        else:
            self.__size = value

    def area(self):
        '''
        calculator of area of the square
        '''

        return (self.__size)**2

    def my_print(self):
        '''
        Print a sqaure using #
        '''
        print("\n".join(["#" * self.__size for rows in range(self.__size)]))

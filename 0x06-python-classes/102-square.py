#!/usr/bin/python3
'''
class Square that defines a square by: (based on 3-square.py)
'''


class Square:
    '''
    class square
    '''

    def __init__(self, size=0):
        '''
        class square
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
    def size(self, value):
        '''
        set size
        '''

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''
        calculator of area of the square
        '''

        return (self.__size)**2

    def __eq__(self, other):
        '''
        equal
        '''
        return self.area == other.area

    def _ne__(self, other):
        '''
        not equal
        '''
        return self.size != other.size

    def _ne__(self, other):
        '''
        lesser than
        '''
        return self.size < other.size

    def _ne__(self, other):
        '''
        lesser or equal than
        '''
        return self.size <= other.size

    def _ne__(self, other):
        '''
        greater or equal than
        '''
        return self.size >= other.size

    def _ne__(self, other):
        '''
        greater than
        '''
        return self.size > other.size

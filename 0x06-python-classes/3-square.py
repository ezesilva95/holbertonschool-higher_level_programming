#!/usr/bin/python3
'''
class Square that defines a square by: (based on 2-square.py)
'''


class Square:
    '''
    class square
    '''

    def __init__(self, size=0):
        '''
        init square

        The size of a square is crucial for a square.
        One way to have the control is to keep it privately.
        You will see in next tasks how to get,
        update and validate the size value.
        '''
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        '''
        calculates area of the square
        '''

        return (self.__size)**2

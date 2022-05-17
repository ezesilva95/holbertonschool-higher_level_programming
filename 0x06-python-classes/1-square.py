#!/usr/bin/python3
'''
class Square that defines a square by: (based on 0-square.py)
'''


class Square:
    '''
    class square
    '''
    def __init__(self, size):
        '''
        init square

        The size of a square is crucial for a square.
        One way to have the control is to keep it privately.
        You will see in next tasks how to get,
        update and validate the size value.
        '''
        self.__size = size

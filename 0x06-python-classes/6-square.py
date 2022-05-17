#!/usr/bin/python3
'''
class Square that defines a square by: (based on 5-square.py)
'''


class Square:
    '''
    class square
    '''

    def __init__(self, size=0, position=(0, 0)):
        '''
        Init a square

        The size of a square is crucial for a square.
        One way to have the control is to keep it privately.
        You will see in next tasks how to get,
        update and validate the size value.
        '''
        self.__size = size
        self.__position = position

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

        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self._size = value
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        '''
        get position
        '''

        return self.__position

    @position.setter
    def position(self, value):
        '''
        set position
        '''
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        '''
        calculator of area of the square
        '''

        return (self.__size)**2

    def my_print(self):
        '''
        Prints square with #
        '''
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join([" " * self.__position[0] +
                             "#" * self.__size
                             for rows in range(self.__size)]))

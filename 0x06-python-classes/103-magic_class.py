#!/usr/bin/python3
'''def magicClass'''
import math

class MagicClass:
    '''init and define methods'''
    def __init__(self, radius=0):
        '''init MagicClass'''
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        '''Calculator of area'''
        return self.__radius ** 2 * math.pi

    def circumference(self):
        '''calculator of circumference'''
        return 2 * math.pi * self.__radius

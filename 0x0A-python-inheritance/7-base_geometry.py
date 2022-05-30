#!/usr/bin/python3
'''
7. Integer validator
Write a class BaseGeometry (based on 6-base_geometry.py).
'''


class BaseGeometry:
    '''
    area(self)
    '''
    def area(self):
        '''
        return not implemented
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' 
        int validator
        '''
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

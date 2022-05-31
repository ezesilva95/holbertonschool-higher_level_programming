#!/usr/bin/python3
'''
10. Student to JSON with filter
'''


class Student():
    '''
    defines a student
    '''
    def __init__(self, first_name, last_name, age):
        '''
        Instantiation with first_name, last_name and age
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        retrieves a dictionary representation of a Student instance
        '''
        if attrs is None:
            return self.__dict__
        else:
            dictionary = {}
            for at in attrs:
                if at in self.__dict__:
                    dictionary[at] = self.__dict__[at]
            return dictionary

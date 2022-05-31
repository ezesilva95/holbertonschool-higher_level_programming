#!/usr/bin/ptyhon3
'''
Module 11. Student to disk and reload
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

    def reload_from_json(self, json):
        '''
        replaces all attributes of the Student instance
        
        for atr_name, atr_value in json.items():
            setattr(self, atr_name, atr_value)
        '''
        self.__dict__update(json)

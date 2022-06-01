#!/usr/bin/python3
'''
Module 11. Student to disk and reload
'''


class Student():
    '''
    Write a class Student that defines a student by
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
        etrieves a dictionary representation of a Student instance
        '''
        if attrs is None:
            return self.__dict__
        else:
            dictionary = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    dictionary[att] = self.__dict__[att]
            return dictionary

    def reload_from_json(self, json):
        '''
        replaces all attributes of the Student instance
        '''
        for atr_name, atr_value in json.items():
            setattr(self, atr_name, atr_value)

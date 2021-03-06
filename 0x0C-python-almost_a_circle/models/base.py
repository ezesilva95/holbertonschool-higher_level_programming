#!/usr/bin/python3
'''
1. Base class
'''

import json


class Base():
    '''
    private class
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Initialize id
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        returns the JSON string representation of list_dictionaries
        '''
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        writes the JSON string representation of list_objs to a file
        '''
        objects = []
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            for i in list_objs:
                objects.append(cls.to_dictionary(i))
        with open(filename, "w") as f:
            f.write(cls.to_json_string(objects))

    @staticmethod
    def from_json_string(json_string):
        '''
        returns the list of the JSON string representation json_string
        '''
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
        returns an instance with all attributes already set
        '''
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''
        returns a list of instances
        '''
        filename = cls.__name__ + ".json"
        li = []
        try:
            with open(filename, "r") as f:
                inst = cls.from_json_string(f.read())
            for i in inst:
                li.append(cls.create(**i))
        except FileNotFoundError:
            pass
        return li

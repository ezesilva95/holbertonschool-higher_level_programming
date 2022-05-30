#!/usr/bin/python3
'''
3.Same class or inherit from
function that returns True if the object is an instance of,
or if the obj is an instance of a class that inherited from the specified class
'''


def is_kind_of_class(obj, a_class):
    '''
     returns True if successful or false if not
    '''
    return isinstance(obj, a_class)

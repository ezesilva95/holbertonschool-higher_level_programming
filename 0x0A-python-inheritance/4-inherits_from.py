#!/usr/bin/python3
'''
4. Only sub class of
function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class
'''


def inherits_from(obj, a_class):
    '''
    returns true if successful, false if not.
    '''
    return (type(obj) is not a_class and issubclass(type(obj), a_class))

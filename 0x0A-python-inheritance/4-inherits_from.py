#!/usr/bin/python3
'''
4. Only sub class of
'''


def inherits_from(obj, a_class):
    '''
    returns true if successful, false if not.
    '''
    return (type(obj) is not a_class and issubclass(type(obj), a_class))

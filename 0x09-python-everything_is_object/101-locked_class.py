#!/usr/bin/python3
'''
LockedClass with no class or object attribute
'''

class LockedClass:
    '''
    locked classi
    prevents the user from dynamically creating new instance attributes, 
    except if the new instance attribute is called first_name
    '''

    __slots__ = "first_name"

#!/usr/bin/python3
'''
1. My list
'''


class MyList(list):
    '''
    class Mylist that inherits from list
    '''
    def print_sorted(self):
        '''
        that prints the list, but sorted (ascending sort)
        '''
        print(sorted(self))

#!/usr/bin/python3
'''
12. My integer
Write a class MyInt that inherits from int
'''


class MyInt(int):
    '''
    MyInt is a rebel. MyInt has == and != operators inverted
    '''
    def __init__(self, num):
        '''
        init num
        '''
        self.num = num

    def __eq__(self, other):
        '''
        not equal
        '''
        return self.num != other

    def __ne__(self, other):
        '''
        both equal
        '''
        return self.num == other

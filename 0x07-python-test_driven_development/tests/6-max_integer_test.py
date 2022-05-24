#!/usr/bin/python3
'''
Unittest for max_integer([..])
'''

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''
    5. Max integer - Unittest
    '''

    def test_ints_floats(self):
        self.assertEqual(max_integer([1]), 2)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([-0.33, -1.5]), -0.33)
        self.assertEqual(max_integer([10, -10, 1]), 10)

    def test_lists(self):
        self.assertEqual(max_integer([1, 3], [1, 5]), [1, 5])

    def test_None(self):
        self.assertEqual(max_integer([None]), None)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)

    def test_strings(self):
        self.assertEqual(max_integer("1234567"), '7')
        self.assertEqual(max_integer(['a', 'd', 'm', 'x', 'y']), 'y')
        self.assertEqual(max_integer("admxy"), 'y')

if __name__ == "__main__":
            unittest.main()

#!/usr/bin/python3
'''
1. Divide a matrix
Write a function that divides all elements of a matrix.
'''


def matrix_divided(matrix, div):
    '''
    matrix must be a list of lists of integers or floats
    return matrix
    '''
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")


    message = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(message)

    new_matrix = []
    new_len = len(matrix[0])
    for lists in matrix:
        if type(lists) is not list:
            raise TypeError(message)
        if len(lists) != new_len:
            raise TypeError("Each row of the matrix must have the same size")
        nlist = []
        for i in lists:
            if type(i) is not int and type(i) is not float:
                raise TypeError(message)
            nlist.append(round(i/div, 2))
        new_matrix.append(nlist)
    return new_matrix

#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
        [5, 10, 15], [5, 5, 5]
]
print(matrix_divided(matrix, 5))
print(matrix)

matrix = [
        [1, 2, 3], [4, 5, 6]
]
print(matrix_divided(matrix, 2))
print(matrix)

try:

    matrix_divided([[5, 10, "Hello"], [5, 5, 5]], 5)

except Exception as e:
        print(e)


try:

        matrix_divided([[5, 10, 15], [5, 5, 5]], 0)

except Exception as e:
            print(e)

try:

        matrix_divided([[5, 10, 15], [5, 5, 5]], "a")

except Exception as e:
            print(e)

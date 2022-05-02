#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        i = 0
        for i in range(len(row)):
            if i == len(row) - 1:
                print(f"{row[i]}", end="")
            else:
                print(f"{row[i]}", end="")
        print()

#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        i = sum(a*b for a, b in my_list)
        j = sum(b for a, b in my_list)
        k = i/j
        return k
    return (0)

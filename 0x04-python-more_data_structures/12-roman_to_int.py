#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None and type(roman_string) is not str:
        return (0)
    num = 0
    for i in range(len(roman_string)):
        roman_string += "-"
        next_i = roman_string[i + 1]
        if roman_string[i] == 'I':
            if next_i == 'V' or next_i == 'X':
                num -= 1
            else:
                num += 1
        if roman_string[i] == 'V':
            num += 5
        if roman_string[i] == 'X':
            if next_i == 'L' or next_i == 'C':
                num -= 10
            else:
                num += 10
        if roman_string[i] == 'L':
            num += 50
        if roman_string[i] == 'C':
            num += 100
        if roman_string[i] == 'D':
            if next_i == 'M':
                num -= 500
            else:
                num += 500
        if roman_string[i] == 'M':
            num += 1000
    return num

#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is not None and type(roman_string) is str:
        num = 0
        roman_string += "-"
        for i in range(len((roman_string)) - 1):
            j = i + 1
            if roman_string[i] == 'I':
                if roman_string[j] == 'V' or roman_string[j] == 'X':
                    num -= 1
                else:
                    num += 1
            if roman_string[i] == 'V':
                num += 5
            if roman_string[i] == 'X':
                if roman_string[j] == 'L' or roman_string[j] == 'C':
                    num -= 10
                else:
                    num += 10
            if roman_string[i] == 'L':
                num += 50
            if roman_string[i] == 'C':
                if roman_string[j] == 'D' or roman_string[j] == 'M':
                    num -= 100
                else:
                    num += 100
            if roman_string[i] == 'D':
                num += 500
            if roman_string[i] == 'M':
                num += 1000
        return num
    else:
        return (0)

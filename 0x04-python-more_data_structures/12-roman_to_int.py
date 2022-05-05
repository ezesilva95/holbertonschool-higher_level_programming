#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is not None and type(roman_string) is str:
        num = 0
        for i, c in enumerate(roman_string):
            j = i + 1
            if c == 'I':
                if j < len(roman_string):
                    if roman_string[j] == 'V' or roman_string[j] == 'X':
                        num -= 1
                    else:
                        num += 1
                else:
                    num += 1
            if c == 'V':
                num += 5
            if c == 'X':
                if j < len(roman_string):
                    if roman_string[j] == 'L' or roman_string[j] == 'C':
                        num -= 10
                    else:
                        num += 10
                else:
                    num += 10
            if c == 'L':
                num += 50
            if c == 'C':
                if j < len(roman_string):
                    if roman_string[j] == 'D' or roman_string[j] == 'M':
                        num -= 100
                    else:
                        num += 100
                else:
                    num += 100
            if c == 'D':
                num += 500
            if c == 'M':
                num += 1000
        return num
    else:
        return (0)

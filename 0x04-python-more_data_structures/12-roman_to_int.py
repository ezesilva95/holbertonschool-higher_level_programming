#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None and type(roman_string) is not str:
        return (0)
    else:
        num = 0
        for i, c in enumerate(roman_string):
            next_i = i+ 1
            if c == 'I':
                if next_i < len(roman_string):
                    if next_i == 'V' or next_i == 'X':
                        num -= 1
                    else:
                        num += 1
                else:
                    num += 1
            if c == 'V':
                num += 5
            if c == 'X':
                if next_i < len(roman_string):
                    if next_i == 'L' or next_i == 'C':
                        num -= 10
                    else:
                        num += 10
                else:
                    num += 10
            if c == 'L':
                num += 50
            if c == 'C':
                if next_i < len(roman_string):
                    if next_i == 'D' or next_i == 'M':
                        num -= 100
                    else:
                        num += 100
                else:
                    num += 100
            if c == 'D':
                if next_i == 'M':
                    num -= 500
                else:
                    num += 500
            if c == 'M':
                num += 1000
    return num

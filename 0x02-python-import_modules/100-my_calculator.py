#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    op = argv[2]
    operator = {"+", "-", "*", "/"}
    if op not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == '+':
            print(f"{a} {op} {b} = {add(a, b)}")
        elif argv[2] == '-':
            print(f"{a} {op} {b} = {sub(a, b)}")
        elif argv[2] == '*':
            print(f"{a} {op} {b} = {mul(a, b)}")
        else:
            print(f"{a} {op} {b} = {div(a, b)}")

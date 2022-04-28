#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5
    from calculator_1 import add
    print(f"{a} + {b} = {add(a, b)}")
    from calculator_1 import sub
    print(f"{a} - {b} = {sub(a, b)}")
    from calculator_1 import mul
    print(f"{a} * {b} = {mul(a, b)}")
    from calculator_1 import div
    print(f"{a} / {b} = {div(a, b)}")

#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    usr = argv[1:]
    size = len(usr)
    if size != 1:
        print(f"{size} arguments", end="")
        if size == 0:
            print(".")
        else:
            print(":")
    else:
        print(f"{size} argument:")
    for idx, arg in enumerate(usr):
        print(f"{idx + 1}: {arg}")

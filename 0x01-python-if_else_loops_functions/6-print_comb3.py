#!/usr/bin/python3
for firstn in range(0, 10):
    for lastn in range((firstn+1), 10):
        if (firstn != 8):
            print("{}{}, ".format(firstn, lastn), end="")
        else:
            print("{}{}".format(firstn, lastn))

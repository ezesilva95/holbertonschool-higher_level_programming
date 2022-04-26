#!/usr/bin/python3
for firstn in range(0, 10):
    for lastn in range((firstn+1), 10):
        if (firstn != 8):
            print(f"{firstn}{lastn}, ", end="")
        else:
            print(f"{firstn}{lastn}")

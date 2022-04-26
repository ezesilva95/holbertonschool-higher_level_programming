#!/usr/bin/python3
for c in range(ord('a'), ord('z')+1):
    if c in [ord('e'), ord('q')]:
        continue

    print(f"{c:c}", end="")

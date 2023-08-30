#!/usr/bin/python3
for value in range(0, 90):
    if value % 10 > value / 10:
        if value != 89:
            print(f"{value:02d}, ", end='')
        else:
            print(f"{value:02d}")

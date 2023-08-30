#!/usr/bin/python3
for value in range(0, 100):
    if value != 99:
        print(f"{value:02d}, ", end='')
    else:
        print(value)

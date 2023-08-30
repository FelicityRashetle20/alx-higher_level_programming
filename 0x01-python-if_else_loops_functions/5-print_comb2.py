#!/usr/bin/python3
for value in range(0, 100):
    if value != 99:
        print("{}".format('0' + str(value) if value < 10 else value), end=', ')
    else:
        print(value)

#!/usr/bin/python3
def uppercase(str):
    for letter in range(len(str)):
        if ord(str[letter]) >= 97 and ord(str[letter]) <= 122:
            value = 32
        else:
            value = 0
        print("{:c}".format(ord(str[letter]) - value), end='')
    print()

#!/usr/bin/python3
for lttr in range(26):
    if lttr != 4 and lttr != 16:
        print("{:s}".format(chr(lttr + ord("a"))), end="")

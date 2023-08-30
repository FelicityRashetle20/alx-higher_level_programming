#!/usr/bin/python3
for value in reversed(range(97, 123)):
    print("{:c}".format(value if (value % 2 == 0) else (value - 32)), end='')

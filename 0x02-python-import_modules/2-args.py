#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    value = len(sys.argv) - 1

    if value == 0:
        print("{} arguments.".format(value))
    elif value == 1:
        print("{} argument:".format(value))
    else:
        print("{} arguments:".format(value))

    if value >= 1:
        value = 0
        for arg in sys.argv:
            if value != 0:
                print("{}: {}".format(value, arg))
            value += 1

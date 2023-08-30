#!/usr/bin/python3
if __name__ == "__main__":
    """Calculates the sum of all arguments"""
    import sys
    total_value = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            total_value += int(arg)
    print(total_value)

#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        final = a / b
    except IndexError:
        final = None
    finally:
        print("Inside result: {}".format(final))
        return (final)

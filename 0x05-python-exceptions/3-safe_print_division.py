#!/usr/bin/python3
#Assume that a and b are integers
def safe_print_division(a, b):
    try:
        final = a / b
    except:
        final = None
    finally:
        print("Inside result: {}".format(final))
        return (final)

import sys

#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as t:
        sys.stderr.write("Exception: {}\n".format(t))
        return (False)
    else:
        return (True)

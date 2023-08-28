import sys
#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        final_pointer = fct(*args)
    except Exception as i:
        sys.stderr.write("Exception: {}\n".format(i))
        final_pointer = None
    return (final_pointer)

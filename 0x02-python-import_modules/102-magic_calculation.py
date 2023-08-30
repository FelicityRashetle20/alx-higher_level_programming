#!/usr/bin/python3
def magic_calculation(a, b):
    """Documentation as required by ALX"""
    from magic_calculation_102 import add, sub
    if a < b:
        total_val = add(a, b)
        for i in range(4, 6):
            total_val = add(total_val, i)
        return (total_val
    else:
        return (sub(a, b))

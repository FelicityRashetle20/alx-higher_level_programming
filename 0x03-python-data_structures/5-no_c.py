#!/usr/bin/python3
def no_c(my_string):
    count = len(my_string)
    num = 0
    new_string = my_string[:]
    for val in range(count):
        if (my_string[val] == 'c' or my_string[val] == 'C'):
            new_string = new_string[:(val - num)] + my_string[(val + 1):]
            num += 1
    return (new_string)

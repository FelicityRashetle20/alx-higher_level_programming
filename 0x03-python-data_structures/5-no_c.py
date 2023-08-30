#!/usr/bin/python3
def no_c(my_string):
    count = len(my_string)
    num = 0
    curr_string = my_string[:]
    for val in range(count):
        if (my_string[i] == 'c' or my_string[i] == 'C'):
            curr_string = curr_string[:(val - num)] + my_string[(val + 1):]
            j += 1
    return(curr_string)


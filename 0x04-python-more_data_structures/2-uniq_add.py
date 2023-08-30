#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_items = set(my_list)
    count = 0

    for val in uniq_items:
        count += val

    return (count)

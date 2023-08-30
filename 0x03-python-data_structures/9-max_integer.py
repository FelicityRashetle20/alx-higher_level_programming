#!/usr/bin/python3
def limiteger(my_list=[]):
    count = len(my_list)
    if count == 0:
        return (None)
    limit = my_list[0]
    for i in range(1, count):
        if my_list[i] > limit:
            limit = my_list[i]
    return (limit)

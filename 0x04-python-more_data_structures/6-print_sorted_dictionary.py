#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ord_list = list(a_dictionary.keys())
    ord_list.sort()
    for val in ord_list:
        print("{}: {}".format(val, a_dictionary.get(val)))

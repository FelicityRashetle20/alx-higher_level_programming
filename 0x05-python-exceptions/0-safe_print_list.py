#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_of_items = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
        except:
            break
        else:
            num_of_items += 1

    print()
    return (num_of_items)

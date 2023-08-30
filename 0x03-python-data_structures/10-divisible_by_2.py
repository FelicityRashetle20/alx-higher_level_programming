#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    final_ans = []
    for val in range(len(my_list)):
        if my_list[val] % 2 == 0:
            final_ans.append(True)
        else:
            final_ans.append(False)
    return (final_ans)

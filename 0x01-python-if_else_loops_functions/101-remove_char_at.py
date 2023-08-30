#!/usr/bin/python3
def remove_char_at(str, n):
    st = ""
    for num in range(len(str)):
        if num != n:
            st = st + str[num]
    return (st)

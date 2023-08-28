#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    out_list = []
    for i in range(list_length):
        try:
            final = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            final = 0
        except TypeError:
            print("wrong type")
            final = 0
        except IndexError:
            print("out of range")
            final = 0
        finally:
            out_list.append(final)

    return (out_list)

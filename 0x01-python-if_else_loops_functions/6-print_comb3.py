#!/usr/bin/python3
for value in range(100):
    if int(value / 10) != value % 10 and int(value / 10) < value % 10:
        print("{}{}".format(int(value / 10), value % 10), end="")
        if (value != 89):
            print(", ", end="")
print("")

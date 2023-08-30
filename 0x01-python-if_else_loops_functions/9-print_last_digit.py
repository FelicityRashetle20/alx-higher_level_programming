#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        final_digit = number % 10
    else:
        final_digit = number % -10
        final_digit *= -1

    print("{final_digit:d}", end='')
    return (final_digit)

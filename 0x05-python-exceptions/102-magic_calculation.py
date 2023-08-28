#!/usr/bin/python3
def magic_calculation(lowBound, highBound):
    total_calc = 0
    for i in range(1, 3):
        try:
            if (i > lowBound):
                raise Exception("Too far")
            else:
                total_calc += (lowBound ** highBound) / i
        except Exception:
            total_calc = highBound + lowBound
            break
    return (total_calc)

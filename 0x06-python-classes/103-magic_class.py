#!/usr/bin/python3
"""Documentation asrequired by the ALX program
"""

import math


class MagicClass:
    """Class that defines the properties
       of the circumference of a circle
    """
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    """Defines the area as explaines by ALX"""
    def area(self):
        return ((self.__radius ** 2) * math.pi)

    """Defines the circumference as explained by ALX"""
    def circumference(self):
        return (2 * math.pi * self.__radius)

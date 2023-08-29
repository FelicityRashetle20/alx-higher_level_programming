#!/usr/bin/python3
"""Documentation as required by the ALX program
"""


class Square:
    """ Documentation as required by the ALX program
    """
    def __eq__(self, other):
        return self.__size == other.__size

    def __lt__(self, other):
        return self.__size < other.__size

    def __le__(self, other):
        return self.__size <= other.__size

    def __ne__(self, other):
        return self.__size != other.__size

    def __gt__(self, other):
        return self.__size > other.__size

    def __ge__(self, other):
        return self.__size >= other.__size

    def __init__(self, size=0):
        """ Documentation as required by the ALX program
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Documentation as required by the ALX program
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """ Documentation as required by the ALX program
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Documentation as required by the ALX program
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

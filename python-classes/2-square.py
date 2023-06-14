#!/usr/bin/python3
"""another square"""


class Square:
    """Square"""
    __size = 0

    def __init__(self,value, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size >= 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

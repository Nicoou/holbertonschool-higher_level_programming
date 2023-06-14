#!/usr/bin/python3
"""another square"""


class Square:
    """Square"""
    __size = 0

    def __init__(self, value, size=0):
        if not isinstance(size, int):
            raise Exception("size must be an integer")
        if not size >= 0:
            raise Exception("size must be >= 0")

        self.__size = value

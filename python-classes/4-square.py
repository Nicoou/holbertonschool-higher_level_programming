#!/usr/bin/python3
"""another square"""


class Square:
    """Square"""

    def __init__(self, size=0):
        """another square"""
        self._size = None
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        """square class"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        area = self.size * self.size
        return area

#!/usr/bin/python3
""" 9-rectangle"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """class of square"""
    def __init__(self, size):
        """method"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

        def area(self):
            """method"""
            return self.__size ** 2
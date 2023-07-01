#!/usr/bin/python3
"""Task 2"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width
        
    @width.setter
    def widt(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be an integer")
        self.__width = value
        
    @property
    def height(self):
        return self.__height

    @property
    def x(self):
            return self.__x
        
    @property
    def y(self):
        return self.__y

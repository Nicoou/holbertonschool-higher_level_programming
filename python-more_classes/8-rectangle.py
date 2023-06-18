#!/usr/bin/python3
""" module """


class Rectangle:
    """ Rectangle """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height != 0 and self.__width != 0:
            return (self.__width * 2) + (self.__height * 2)
        else:
            return 0

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance or Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def print(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        print(self)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ''

        for i in range(self.__height - 1):
            print(str(self.print_symbol) * self.__width)
        print(str(self.print_symbol) * self.__width, end="")
        return ''

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

#!/usr/bin/python3
""" task 8 rectangle"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle"""
    def __init__(self, width, height):
        """Method"""
        self.integer_validator("width", width)
        __width = width
        self.integer_validator("height", height)
        __height = height

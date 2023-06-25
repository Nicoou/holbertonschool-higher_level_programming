#!/usr/bin/python3
""" task 8 rectangle"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """method"""
        self.integer_validator("width", width)
        __width = width
        self.integer_validator("height", height)
        __height = height
        
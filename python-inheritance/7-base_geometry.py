#!/usr/bin/python3
""" task 7 base geometry """


class BaseGeometry:
    """class BaseGeometry, commit """
    def area(self):
        """method"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise TypeError("{} must be greater than 0",format(name))

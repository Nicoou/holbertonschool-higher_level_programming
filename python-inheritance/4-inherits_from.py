#!/usr/bin/python3
""" task 4 inherits """


def inherits_from(obj, a_class):
    """function that return true if the obj is an instance"""
    if type(obj) == a_class:
        return False
    if issubclass(type(obj), a_class):
        return True
    return False

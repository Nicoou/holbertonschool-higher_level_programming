#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0 or my_list == []:
        return None
    new_list = my_list[0]
    for x in my_list:
        if x >= new_list:
            new_list = x
    return new_list

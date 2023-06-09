#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for x in range(o, x):
        try:
            print("{:d}".format(my_list[x]), end="")
            i += 1
        except (ValueError, TypeError):
            pass
    print()
    return i
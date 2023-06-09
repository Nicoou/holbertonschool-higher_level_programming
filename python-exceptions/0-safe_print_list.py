#!/usr/bin/python3
def safe_print_integer(my_list=[], x=0):
    i = 0
    for x in range(0, x):
        try:
            print(my_list[x], end="")
            i += 1
        except Exception:
            break
    print()
    return i

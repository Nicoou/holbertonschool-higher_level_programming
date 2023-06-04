#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    cont = 0
    res = 0
    for x in argv:
        if cont != 0:
            res = res + int(x)
        cont += 1
    print("{}".format(res))    

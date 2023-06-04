#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    cont = 0
    if len(argv) < 2:
        print("0 arguments.")
else:
    print("{} {}".format(len(argv) - 1,
                         "arguments:" if len(argv) > 2 else "arguments:"))

for x in argv:
    if cont != 0:
        print("{}: {}".format(cont, x))
    cont += 1

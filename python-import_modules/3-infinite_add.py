#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    res = 0
    argc = len(sys.argv)
    if argc == 1:
        print("0")
        quit()
    else:
        for idx, argc in enumerate(sys.argv):
            if idx > 0:
                res += int(argc)
        print("{}".format(res))

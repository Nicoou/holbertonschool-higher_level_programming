#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        x = 0
        for y in i:
            # this print is for clear the space at the end of the matrix
            print("{:d}".format(y), end="" if len(i) - 1 == x else " ")
            x += 1
        print()

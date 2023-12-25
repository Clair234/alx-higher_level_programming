#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for topmatrix in matrix:
        if len(topmatrix) == 0:
            print()
        for i in range(len(topmatrix)):
            print("{:d}".format(topmatrix[i]),
                    end="\n" if i is len(topmatrix) - 1 else " ")


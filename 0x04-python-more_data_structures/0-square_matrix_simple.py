#!/usr/bin/python3

def square_matrix_simple(matrix):
    new_matrix = []
    for row in matrix:
        ans = list(map(lambda x: x**2, row))
        new_matrix.append(ans)
    return new_matrix

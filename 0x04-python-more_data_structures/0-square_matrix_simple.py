#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    matrix_2 = [row[:] for row in matrix]
    for i in range(0, len(matrix_2)):
        for j in range(0, len(matrix_2[i])):
            matrix_2[i][j] = matrix_2[i][j] ** 2
    return matrix_2

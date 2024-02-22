#!/usr/bin/python3

"""A module that rotates a matrix by 90 degrees"""


def rotate_2d_matrix(matrix):
    """A 90 degrees rotated matrix"""
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()

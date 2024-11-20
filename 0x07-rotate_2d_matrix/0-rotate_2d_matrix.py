#!/usr/bin/python3
"""
Module to rotate a 2D matrix by 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate an n x n 2D matrix by 90 degrees clockwise.

    Args:
        matrix (List[List[int]]): The matrix to rotate.
    """
    # Step 1: Transpose the matrix
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()

#!usr/bin/python3
"""
Pascal's Triangle
"""

def pascal_triangle(n):
    """
    Generate Pascal's Triangle of n levels.
    
    Args:
    n (int): The number of levels in the triangle.
    
    Returns:
    list of lists: Pascal's Triangle represented as a list of lists of integers.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the triangle with the first row

    for i in range(1, n):
        row = [1]  # Start each row with 1
        for j in range(1, i):
            # Each element is the sum of the two elements above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # End each row with 1
        triangle.append(row)

    return triangle

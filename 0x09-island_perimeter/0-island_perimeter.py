#!/usr/bin/python3
"""Island Perimeter Problem Grid
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid.

    Args:
        grid (list of list of int): 2D grid containing 0 (water) or 1 (land).

    Returns:
        int: The perimeter of the island.
    """

    perimeter = 0

    # Iterate through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:  # Check if the cell is land
                # Check the top cell
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check the bottom cell
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check the left cell
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check the right cell
                if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
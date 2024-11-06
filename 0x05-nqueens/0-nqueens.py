#!/usr/bin/python3
""" N queens """
import sys


# Argument validation
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    sys.exit(1)

n = int(sys.argv[1])

if n < 4:
    print("N must be at least 4")
    sys.exit(1)


def queens(n, i=0, a=[], b=[], c=[]):
    """Find all solutions using backtracking."""
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def solve(n):
    """Print solutions in the required format."""
    for solution in queens(n, 0):
        formatted_solution = [[i, solution[i]] for i in range(n)]
        print(formatted_solution)


solve(n)

#!/usr/bin/python3
import sys


def is_valid(board, row, col):
    """Check if a queen can be placed on board at (row, col)"""
    for i in range(row):
        # Check column and diagonals
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n):
    """Solve the N Queens problem and return all solutions"""
    def backtrack(row, board):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(row + 1, board)
                board[row] = -1

    solutions = []
    board = [-1] * n
    backtrack(0, board)
    return solutions


def print_solutions(solutions):
    """Print all solutions in the required format"""
    for solution in solutions:
        print([[i, solution[i]] for i in range(len(solution))])


if __name__ == "__main__":
    # Check if the right number of arguments is given
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Validate that N is an integer
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N-Queens problem and print solutions
    solutions = solve_nqueens(n)
    print_solutions(solutions)

#!/usr/bin/python3
import sys


def is_valid(board, row, col):
    """Check if a queen can be placed on the board at (row, col)."""
    for i in range(row):
        # Check for same column and both diagonals
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n):
    """Generate all possible solutions for the N-Queens problem."""
    def backtrack(row, board):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(row + 1, board)
                board[row] = -1  # Reset position

    solutions = []
    board = [-1] * n
    backtrack(0, board)
    return solutions


def print_solutions(solutions):
    """Format and print solutions as required."""
    for solution in solutions:
        formatted_solution = [[i, solution[i]] for i in range(len(solution))]
        print(formatted_solution)


if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Validate that N is an integer
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Ensure N meets the minimum size requirement
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Generate and print solutions
    solutions = solve_nqueens(n)
    print_solutions(solutions)


# Task 04: Sudoku Solver
# Developed using Python and Backtracking Algorithm


def print_board(board):
    """Display the Sudoku board."""
    print("\n" + "-" * 25)

    for row in range(9):
        for col in range(9):
            if col % 3 == 0:
                print("| ", end="")

            print(board[row][col], end=" ")

        print("|")

        if (row + 1) % 3 == 0:
            print("-" * 25)


def find_empty_cell(board):
    """Find an empty cell represented by 0."""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col

    return None


def is_valid(board, number, position):
    """Check whether a number can be placed in a cell."""
    row, col = position

    # Check the row
    for current_col in range(9):
        if (
            board[row][current_col] == number
            and current_col != col
        ):
            return False

    # Check the column
    for current_row in range(9):
        if (
            board[current_row][col] == number
            and current_row != row
        ):
            return False

    # Check the 3x3 box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3

    for current_row in range(box_row, box_row + 3):
        for current_col in range(box_col, box_col + 3):
            if (
                board[current_row][current_col] == number
                and (current_row, current_col) != position
            ):
                return False

    return True


def solve_sudoku(board):
    """Solve Sudoku using backtracking."""
    empty_cell = find_empty_cell(board)

    # If no empty cell remains, Sudoku is solved
    if empty_cell is None:
        return True

    row, col = empty_cell

    # Try numbers from 1 to 9
    for number in range(1, 10):
        if is_valid(board, number, (row, col)):
            board[row][col] = number

            # Recursively solve the remaining board
            if solve_sudoku(board):
                return True

            # Backtrack if the number leads to no solution
            board[row][col] = 0

    return False


def main():
    """Run the Sudoku Solver application."""

    # 0 represents an empty cell
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("SUDOKU SOLVER")
    print("\nOriginal Sudoku:")
    print_board(board)

    if solve_sudoku(board):
        print("\nSolved Sudoku:")
        print_board(board)
        print("\nSudoku solved successfully!")
    else:
        print("\nNo solution exists for this Sudoku.")


if __name__ == "__main__":
    main()

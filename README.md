
# Sudoku Solver

A Python-based Sudoku Solver that solves a 9×9 Sudoku puzzle using the Backtracking Algorithm.

The application displays the original Sudoku puzzle and automatically finds and displays its solution.

## Features

- Solve a 9×9 Sudoku puzzle
- Uses the Backtracking Algorithm
- Checks row constraints
- Checks column constraints
- Checks 3×3 box constraints
- Displays the original Sudoku puzzle
- Displays the solved Sudoku grid
- Detects if a puzzle has no solution

## Technologies Used

- Python
- Backtracking Algorithm

## Requirements

- Python 3.x
- No external libraries required

## Project Structure

```text
Task_04_Sudoku_Solver/
│
├── main.py
└── README.md
```

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/Task_04_Sudoku_Solver.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Task_04_Sudoku_Solver
   ```

3. Run the program:

   ```bash
   python main.py
   ```

## How It Works

The Sudoku board is represented as a 9×9 list in Python.

Empty cells are represented by `0`.

The Backtracking Algorithm works by:

1. Finding an empty cell.
2. Trying numbers from 1 to 9.
3. Checking whether the number is valid in the row, column, and 3×3 box.
4. Placing the number if it is valid.
5. Recursively solving the remaining puzzle.
6. Backtracking when a number leads to an invalid solution.

## Learning Outcomes

- Understanding recursion
- Implementing the Backtracking Algorithm
- Working with 2D lists
- Using Python functions
- Applying logical problem-solving
- Understanding constraint checking

## Internship Task

Task 04 completed as part of the Software Development Internship Program at Prodigy InfoTech.

## Author

Hasrat Shaikh

GitHub: https://github.com/hasratshaikh

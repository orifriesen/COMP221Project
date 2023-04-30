# Backtracking Sudoku Solver
COMP 221: Algorithm Design and Analysis Final Project

This project is a Sudoku Solver that uses a brute-force backtracking algorithm to solve the inputted Sudoku puzzle. The upper bounds time complexity is $O(9^{n^2})$, but since there are fewer and fewer value choices as the program runs, in reality the program is much faster than its upper bounds time complexity.

Packages Required:
* tkinter
* pygame
* numpy

To run the program, run the `Testing.py` file.

This will create a pop-up window where the user is able to click on each cell of the Sudoku board and then input a number value into that cell. Once the user is satisfied with the inputs to the Sudoku algorithm, pressing the `"S"` key on the keyboard will produce a viable solution to the inputted Sudoku puzzle.

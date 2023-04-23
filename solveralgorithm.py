import numpy as np

def checkRowAndCol(inputGrid, row, col, num):
    for i in range(9):
        if inputGrid[row][i] == num or inputGrid[i][col] == num:
            return False
    return True
def checkSquare(inputGrid, row, col, num):
    startRow = row - (row % 3)
    startCol = col - (col % 3)
    for i in range(3):
        for j in range(3):
            if inputGrid[startRow + i][startCol + j] == num:
                return False
    return True

def isLegal(inputGrid, row, col, num):
    if checkRowAndCol(inputGrid, row, col, num) and checkSquare(inputGrid, row, col, num):
        return True
    else:
        return False

def solvePuzzle(inputGrid, row, col):
    if row == 8 and col == 9:
        return True
    
    if col == 9:
        row += 1
        col = 0
    
    if inputGrid[row][col] > 0:
        return solvePuzzle(inputGrid, row, col+1)
    for num in range(1, 10):
        if isLegal(inputGrid, row, col, num) == True:
            inputGrid[row][col] = num
            if solvePuzzle(inputGrid, row, col+1):
                return True
    inputGrid[row][col] = 0
    return False



inputGrid = [[0, 0, 3, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 5, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 4, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],]

if (solvePuzzle(inputGrid, 0, 0)):
    print(inputGrid)
else:
    print("no solution  exists ")
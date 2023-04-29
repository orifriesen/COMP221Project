import pygame

pygame.init()

# Screen details (DON'T MAKE LESS THAN ~500, DID NOT MAKE WITH RESIZABILITY IN MIND!)
screen_width = 540
screen_height = 540
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sudoku Solver")  # Tentative name...
font = pygame.font.SysFont('Comic Sans', 30)  # Comic sans cause why not

# The grid on which the game is played, set it up as empty, but will be changed later
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Grid + cells (cell being a unit in the grid yeah)
cell_size = 60
cell_positions = [
    [(0, 0), (60, 0), (120, 0), (180, 0), (240, 0), (300, 0), (360, 0), (420, 0), (480, 0)],
    [(0, 60), (60, 60), (120, 60), (180, 60), (240, 60), (300, 60), (360, 60), (420, 60), (480, 60)],
    [(0, 120), (60, 120), (120, 120), (180, 120), (240, 120), (300, 120), (360, 120), (420, 120), (480, 120)],
    [(0, 180), (60, 180), (120, 180), (180, 180), (240, 180), (300, 180), (360, 180), (420, 180), (480, 180)],
    [(0, 240), (60, 240), (120, 240), (180, 240), (240, 240), (300, 240), (360, 240), (420, 240), (480, 240)],
    [(0, 300), (60, 300), (120, 300), (180, 300), (240, 300), (300, 300), (360, 300), (420, 300), (480, 300)],
    [(0, 360), (60, 360), (120, 360), (180, 360), (240, 360), (300, 360), (360, 360), (420, 360), (480, 360)],
    [(0, 420), (60, 420), (120, 420), (180, 420), (240, 420), (300, 420), (360, 420), (420, 420), (480, 420)],
    [(0, 480), (60, 480), (120, 480), (180, 480), (240, 480), (300, 480), (360, 480), (420, 480), (480, 480)]
]


# Actually draw the grid
def draw_grid():
    for rows in range(9):
        for cols in range(9):
            rect = pygame.Rect(cell_positions[rows][cols], (cell_size, cell_size))
            pygame.draw.rect(screen, pygame.color.Color("White"), rect, 1)
            if grid[rows][cols] != 0:
                number_text = font.render(str(grid[rows][cols]), True, pygame.color.Color("Black"))
                number_rect = number_text.get_rect(center=rect.center)
                screen.blit(number_text, number_rect)


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
        return solvePuzzle(inputGrid, row, col + 1)
    for num in range(1, 10):
        if isLegal(inputGrid, row, col, num) == True:
            inputGrid[row][col] = num
            if solvePuzzle(inputGrid, row, col + 1):
                return True
    inputGrid[row][col] = 0
    return False



# Highlight the selected cell
def highlight_cell(rows, cols):
    rect = pygame.Rect(cell_positions[rows][cols], (cell_size, cell_size))
    pygame.draw.rect(screen, pygame.color.Color("Green"), rect, 3)


# Change cell number ONLY POSITIVE NON ZERO INTEGERS!!!
def change_number(rows, cols, number):
    grid[rows][cols] = number
    rect = pygame.Rect(cell_positions[rows][cols], (cell_size, cell_size))
    pygame.draw.rect(screen, pygame.color.Color("White"), rect)
    number_text = font.render(str(number), True, pygame.color.Color("Black"))
    number_rect = number_text.get_rect(center=rect.center)
    screen.blit(number_text, number_rect)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            for rows in range(9):
                for cols in range(9):
                    rect = pygame.Rect(cell_positions[rows][cols], (cell_size, cell_size))
                    if rect.collidepoint(mouse_position):
                        selected_cell = (rows, cols)
                        highlight_cell(rows, cols)
        elif event.type == pygame.KEYDOWN:
            if event.unicode.isdigit() and selected_cell is not None:
                change_number(selected_cell[0], selected_cell[1], int(event.unicode))
            elif event.key == pygame.K_BACKSPACE and selected_cell is not None:
                change_number(selected_cell[0], selected_cell[1], 0)
            elif event.key == pygame.K_s:
                # Call the solver algorithm here
                print("fuck")
                solvePuzzle(grid, 0, 0)
                screen.fill((100,100,255))
                pygame.display.update()

    draw_grid()
    pygame.display.update()


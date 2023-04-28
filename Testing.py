import pygame

pygame.init()

# Screen details (DON'T MAKE LESS THAN ~500, DID NOT MAKE WITH RESIZABILITY IN MIND!)
screen_width = 750
screen_height = 750
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


# The actual "game" loop
running = True
selected_cell = None
while running:
    for event in pygame.event.get():
        # Quit evebt
        if event.type == pygame.QUIT:
            running = False
        # Handles the clicking of cells + highlighting
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row = y // cell_size
            col = x // cell_size
            if selected_cell is not None:
                highlight_cell(*selected_cell)
            selected_cell = (row, col)
            highlight_cell(row, col)
        # Handles inputting of numbers into the grid, ONLY POSITIVE NONZERO INTEGERS!!!
        elif event.type == pygame.KEYDOWN:
            if selected_cell is not None and pygame.K_1 <= event.key <= pygame.K_9:
                change_number(selected_cell[0], selected_cell[1], event.key - pygame.K_0)

    # Draw + Update
    draw_grid()
    pygame.display.update()

pygame.quit()

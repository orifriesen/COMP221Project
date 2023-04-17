import tkinter as tk

# Define the dimensions of the grid
grid_size = 9
cell_size = 50

# Define the colors for the grid and the selected cell
grid_color = "black"
highlight_color = "red"

# Define the currently selected cell
selected_cell = [0, 0]


# Define a function to highlight the selected cell
def highlight_cell():
    # Cell Coordinates
    row, col = selected_cell

    # Remove Old Highlight
    canvas.delete("highlight")

    # Create Highlight
    x1 = col * cell_size
    y1 = row * cell_size
    x2 = (col + 1) * cell_size
    y2 = (row + 1) * cell_size
    canvas.create_rectangle(x1, y1, x2, y2, outline=highlight_color, width=3, tag="highlight")


# Key press check
def handle_keypress(event):
    # Get current cell
    row, col = selected_cell

    # Move the selected cell based on the arrow key pressed
    if event.keysym == "Up" and row > 0:
        selected_cell[0] -= 1
    elif event.keysym == "Up" and row == 0:
        selected_cell[0] += grid_size - 1
    elif event.keysym == "Down" and row < grid_size - 1:
        selected_cell[0] += 1
    elif event.keysym == "Down" and row == grid_size - 1:
        selected_cell[0] -= grid_size - 1
    elif event.keysym == "Left" and col > 0:
        selected_cell[1] -= 1
    elif event.keysym == "Left" and col == 0:
        selected_cell[1] += grid_size - 1
    elif event.keysym == "Right" and col < grid_size - 1:
        selected_cell[1] += 1
    elif event.keysym == "Right" and col == grid_size - 1:
        selected_cell[1] -= grid_size - 1

    # Highlight the new cell
    highlight_cell()


# Tkinter stuff
window = tk.Tk()
window.title("Sodoku Solver")
window.geometry("{}x{}".format(grid_size * cell_size, grid_size * cell_size))

# Create a canvas and draw the grid on it
canvas = tk.Canvas(window, width=grid_size * cell_size, height=grid_size * cell_size)
canvas.pack()
for row in range(grid_size):
    for col in range(grid_size):
        number = (row * grid_size + col) % 9 + 1
        x1 = col * cell_size
        y1 = row * cell_size
        x2 = (col + 1) * cell_size
        y2 = (row + 1) * cell_size
        cell = canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=str(number), font=("Arial", 20))
        canvas.create_rectangle(x1, y1, x2, y2, outline=grid_color, width=1)

# Highlight the initial selected cell
highlight_cell()

# Bind the canvas to a function that handles key presses
canvas.focus_set()
canvas.bind("<Key>", handle_keypress)

# Start the Tkinter event loop
window.mainloop()


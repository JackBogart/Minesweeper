import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import random
from colorama import Back
class Minefield:
    def __init__(self, grid_size, difficulty):
        self.width = grid_size
        self.num_of_mines = grid_size * difficulty
        self.grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
        self.__place_mines(self.num_of_mines)

    def __len__(self) -> int:
        return self.width
    
    def __place_mines(self, num_of_mines) -> None:
        for _ in range(num_of_mines):
            r, c = random.randint(0, self.width-1), random.randint(0, self.width-1)
            while(self.grid[r][c] == "M"):
                r, c = random.randint(0, self.width-1), random.randint(0, self.width-1)
            self.grid[r][c] = "M"

            for i in range(max(r-1, 0), min(r+2, self.width)):
                for j in range(max(c-1, 0), min(c+2, self.width)):
                    if self.grid[i][j] != "M":
                        self.grid[i][j] += 1
    
    def print_minefield(self):
        for row in self.grid:
            print(" ", end="")
            for element in row:
                if element == "M":
                    print(Back.BLACK + "  ", end="")
                elif element == 0:
                    print(Back.WHITE + "  ", end="")
                else:
                    print(Back.WHITE + " " + str(element), end="")
            print(Back.RESET)

def flag_square(event, r, c):
    buttons[r][c].config(text=currentField.grid[r][c])

def create_grid_gui(root, rows, cols):
    buttons = []
    for row in range(rows):
        button_row = []
        for col in range(cols):
            btn = tk.Button(root, width=2)
            btn.grid(row=row, column=col)
            btn.config(command=lambda r=row, c=col: reveal_cell(r, c))
            btn.bind('<Button-3>', lambda e, r=row, c=col: flag_square(e, r, c))
            button_row.append(btn)  # Add button to the row list
        buttons.append(button_row)  # Add the row list to the buttons list
    
    return buttons

def reveal_cell(row, col):
    if currentField.grid[row][col] == "M":
        buttons[row][col].config(image=images["mine"])
    else:
        buttons[row][col].config(text=currentField.grid[row][col])

buttons = None
currentField = None
images = {}
def load_images():
    # Load all necessary images and store references in the 'images' dictionary
    original_image = Image.open(r"assets/mine.png")
    resized_image = original_image.resize((10, 10))  # Adjust size as needed
    images["mine"] = ImageTk.PhotoImage(resized_image, width=2)

if __name__ == '__main__':
    currentField = Minefield(12, 2)
    root = tk.Tk()
    root.title('Minesweeper')
    load_images()
    
    # Create and display the grid GUI
    buttons = create_grid_gui(root, 12, 12)
    currentField.print_minefield()
    root.mainloop()
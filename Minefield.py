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


if __name__ == '__main__':
    testField = Minefield(12, 2)

    testField.print_minefield()
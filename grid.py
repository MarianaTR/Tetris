import pygame
from colors import Color

class Grid:
    def __init__(self) -> None:
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.piece_colors = Color.get_color_pieces()

    def reset(self):
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end= " ")
            print()

    def is_inside(self, row, column):
        if row >= self.num_rows or column >= self.num_cols or column < 0:
            return False
        return True
    
    def is_busy(self, row, column):
        if self.grid[row][column] == 0:
            return False
        return True
    
    def is_row_full(self, row):
        if 0 in self.grid[row]:
            return False
        return True

    def clear_row(self, row):
        self.grid[row] = [0 for j in range(self.num_cols)]

    def move_row_down(self, row, num_rows):
        row_move = self.grid[row]
        self.grid[row + num_rows] = row_move
        self.grid[row] = [0 for j in range(self.num_cols)]

    def verify_completed_rows(self):
        completed = 0
        for row in range(self.num_rows - 1, 0, -1):
            if self.is_row_full(row):
                completed += 1
                self.clear_row(row)
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed

    def draw(self, screen):
        
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                value = self.grid[row][column]
                cell = pygame.Rect(column*self.cell_size + 200,row*self.cell_size + 30,self.cell_size - 1,self.cell_size - 1)
                pygame.draw.rect(screen, self.piece_colors[value],cell)

    def is_perfect_clear(self):
        for row in range(self.num_rows-1, 0, -1):
            is_clean_row = [element == 0 for element in self.grid[row]]
            if not all(is_clean_row):
                return False
            
        return True

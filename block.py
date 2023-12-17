from colors import Color
import pygame
from position import Position

class Block:
    def __init__(self, id) -> None:
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        self.colors = Color.get_color_pieces()
        self.ghost = 0

    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns

    def rotation(self, type):
        self.rotation_state += type
        if self.rotation_state > 3:
            self.rotation_state = 0
        if self.rotation_state < 0:
            self.rotation_state = 3


    def get_cell_positions(self):
        piece = self.cells[self.rotation_state]
        moved_piece = []
        for cell in piece:
            position = Position(cell.row + self.row_offset, cell.column + self.column_offset)
            moved_piece.append(position)
        return moved_piece

    def draw(self, screen, offset_x, offset_y, border = 0):
        grid_piece = self.get_cell_positions()
        for grid in grid_piece:
            cell_rect = pygame.Rect(offset_x + grid.column*self.cell_size , 
                                    offset_y + grid.row*self.cell_size ,self.cell_size - 1,self.cell_size - 1)
            if border == 1:
                pygame.draw.rect(screen, self.colors[self.id],cell_rect, 2,10)
            else:
                pygame.draw.rect(screen, self.colors[self.id],cell_rect)

    def clear(self, screen, x, y):
        background_color = (0, 0, 0, 0) 
        grid_piece = self.get_cell_positions()
        for grid in grid_piece:
            cell_rect = pygame.Rect(x + grid.column*self.cell_size , 
                                    y + grid.row*self.cell_size ,self.cell_size - 1,self.cell_size - 1)
            pygame.draw.rect(screen, background_color, cell_rect)
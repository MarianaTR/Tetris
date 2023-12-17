from grid import Grid
from blocks import *
import random, pygame
from colors import Color
from score import *
import pygame
import copy

class Game:
    pieces_rect = pygame.Rect(510, 50, 180, 550)
    def  __init__(self) -> None:
        self.reset()
        

    def get_random_block(self):
        blocks_random = []
        while len(self.blocks) > 0:
            block = random.choice(self.blocks)
            blocks_random.append(block)
            self.blocks.remove(block)
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), ZBlock(), TBlock()]
        self.ghost_piece = self.pieces[blocks_random[0].id-1]
        self.ghost_piece.reset()
        return blocks_random
    
    #Move the normal piece
 
    def move_left(self):
        self.score +=1
        self.random_bag[0].move(0, -1)
        if self.is_within_the_limit() == False or self.is_colliding_with_another_piece(self.random_bag[0]) == True:
            self.random_bag[0].move(0, 1)
            

    def move_right(self):
        self.score +=1
        self.random_bag[0].move(0, 1)
        if self.is_within_the_limit() == False or self.is_colliding_with_another_piece(self.random_bag[0]) == True:
            self.random_bag[0].move(0, -1)

    def move_down(self):
        self.score +=1
        self.random_bag[0].move(1,0)               
            
        if self.is_within_the_limit() == False or self.is_colliding_with_another_piece(self.random_bag[0]) == True:
            self.random_bag[0].move(-1, 0)
            
            self.lock_block()

    def move_hard_drop(self):
        self.score +=1
        row = -10
        while True:
            if row < 0:
                cells = self.random_bag[0].get_cell_positions()
                for cell in cells:
                    if cell.row > row:
                        row = cell.row
                
                n = 20
                inicio = 1 
                invested_value = inicio + n - (row - inicio) - 1

                self.score += 2 * invested_value
            self.random_bag[0].move(1,0)

            if self.is_within_the_limit() == False or self.is_colliding_with_another_piece(self.random_bag[0]) == True:
                self.random_bag[0].move(-1, 0)
                self.lock_block()
                break

    def hourly_rotation(self):
        self.score +=1
        self.random_bag[0].rotation(1)
        if self.is_within_the_limit() == False or self.is_colliding_with_another_piece(self.random_bag[0]) == True:
            self.random_bag[0].rotation(-1)

    def antihourly_rotation(self):
        self.score +=1
        self.random_bag[0].rotation(-1)
        if self.is_within_the_limit() == False or self.is_colliding_with_another_piece(self.random_bag[0]) == True:
            self.random_bag[0].rotation(1)

    #Move to ghost piece

    def move_left_ghost(self):
        #self.ghost_piece.move(-self.ghost_piece.row_offset, 0)
        self.ghost_piece.rotation_state = self.random_bag[0].rotation_state
        self.ghost_piece.move(0,-1)
        if self.is_within_the_limit2() == False:
            self.ghost_piece.move(0,1)
        while self.is_colliding_with_another_piece(self.ghost_piece) == True:
            self.ghost_piece.move(-1,0)
        
        
    def move_right_ghost(self):
        #self.ghost_piece.move(-self.ghost_piece.row_offset, 0)
        self.ghost_piece.rotation_state = self.random_bag[0].rotation_state
        self.ghost_piece.move(0,1)
        if self.is_within_the_limit2() == False:
                self.ghost_piece.move(0,-1)
        while self.is_colliding_with_another_piece(self.ghost_piece) ==  True:
            self.ghost_piece.move(-1,0)

    def hourly_rotation_ghost(self):
        self.ghost_piece.rotation_state = self.random_bag[0].rotation_state
        while self.is_within_the_limit2() == False or self.is_colliding_with_another_piece(self.ghost_piece) == True:
            self.ghost_piece.move(-1,0)
            

    def antihourly_rotation_ghost(self):
        self.ghost_piece.rotation_state = self.random_bag[0].rotation_state
        while self.is_within_the_limit2() == False or self.is_colliding_with_another_piece(self.ghost_piece) == True:
            self.ghost_piece.move(-1,0)

    def draw_ghost_piece(self, screen):
        
        while True:
            self.ghost_piece.move(1,0)

            if self.is_within_the_limit2() == False or self.is_colliding_with_another_piece(self.ghost_piece) == True:
                self.ghost_piece.move(-1, 0)
                self.ghost_piece.draw(screen, 200, 30, 1)
                break
    
    def lock_block(self):
        cells = self.random_bag[0].get_cell_positions()
        for position in cells:
            self.grid.grid[position.row][position.column] = self.random_bag[0].id
        self.random_bag.pop(0)
        self.can_change = True
        
        if len(self.random_bag) == 0:
            self.random_bag = self.get_random_block()
        self.ghost_piece = self.pieces[self.random_bag[0].id -1]
        self.ghost_piece.reset()
        lines_completed = self.grid.verify_completed_rows()
        self.line_completed +=lines_completed

        if self.grid.is_perfect_clear():

            self.score += perfect_clear(self.grid, self.level, lines_completed)
        elif lines_completed != 0:

            self.score += line_completed_score(lines_completed, self.level)

        if lines_completed != 0:

            self.combo_count +=1
            self.score += combo(self.level, self.combo_count)
        else:

            self.combo_count = 0

        
        
        if self.line_completed >= 10:
            self.level += 1
            self.line_completed = 0

        if self.is_colliding_with_another_piece(self.random_bag[0]) == True:
            self.game_over = True

    def is_colliding_with_another_piece(self, piece):
        cells = piece.get_cell_positions()
        for cell in cells:
            if self.grid.is_busy(cell.row, cell.column) == True:
                return True
        return False
    

    def is_within_the_limit(self):

        cells = self.random_bag[0].get_cell_positions()
        for cell in cells:
            if self.grid.is_inside(cell.row, cell.column) == False:
                return False
        return True
    
    def is_within_the_limit2(self):
        cells = self.ghost_piece.get_cell_positions()
        for cell in cells:
            if self.grid.is_inside(cell.row, cell.column) == False:
                return False
        return True
    
    def draw(self, screen):
        if self.ghost_piece == None:
            if len(self.random_bag) != 0:
                self.ghost_piece = self.pieces[self.random_bag[0].id-1]
                self.ghost_piece.reset()

        self.clear_pieces(screen)
        self.set_next_piece()

        if len(self.random_bag) == 0:
            self.random_bag = self.get_random_block()

        self.grid.draw(screen)
        self.draw_ghost_piece(screen)
        self.random_bag[0].draw(screen, 200, 30)

        #Drawing the next pieces section
        nexts_pieces= 0
        piece_index_y = 100
    
        for piece in self.next_pieces:
            piece.draw(screen, 450, piece_index_y)
            nexts_pieces+=1
            piece_index_y += 100
            if nexts_pieces == 3:
                break

    def clear_pieces(self, screen):
        nexts_pieces= 0
        piece_index_y = 100
        for piece in self.next_pieces:
            piece.clear(screen, 450, piece_index_y)
            nexts_pieces+=1
            piece_index_y += 100
            if nexts_pieces == 3:
                break

    def reset(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), ZBlock(), TBlock()]
        self.pieces = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), ZBlock(), TBlock()]
        self.random_bag = self.get_random_block()
        self.game_over = False
        self.retained_piece = None
        self.next_pieces = []
        self.ghost_piece = None
        self.level = 1
        self.velocity = 0
        self.score = 0
        self.aux_piece= None
        self.can_change = True
        self.line_completed = 0
        self.combo_count = 0
        self.score_record = 0
        self.read_score_record()

    def set_retained_piece(self, screen):
        if self.can_change:
            self.pieces = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), ZBlock(), TBlock()]
            self.clear_stored(screen)
            self.ghost_piece=None
            
            if self.retained_piece != None:
                self.aux_piece = copy.deepcopy(self.retained_piece)
                self.aux_piece.reset()
    
            self.retained_piece = copy.deepcopy(self.random_bag[0])
            self.retained_piece.reset()
            
            self.retained_piece.draw(screen, -50, 530)
            self.random_bag.pop(0)
            
            if self.aux_piece != None:
                self.random_bag.insert(0, self.aux_piece)
                
                self.ghost_piece = self.pieces[self.random_bag[0].id-1]
                self.ghost_piece.reset()
            self.can_change = False
            

    def clear_stored(self, screen):
        if self.retained_piece != None:
            self.retained_piece.clear(screen, -50, 530)

    def set_next_piece(self):
        self.next_pieces = []
        pieces = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), ZBlock(), TBlock()]
        index = 0
        for piece in self.random_bag[1:]:
            self.next_pieces.append(pieces[piece.id-1])
            index+=1
            if index == 3:
                break

    def save_score_record(self):
        if self.score > self.score_record:
            with open('score_record.txt', 'w') as file:
                file.write(str(self.score))

    def read_score_record(self):
        try: 
            with open('score_record.txt', 'r') as file:
                self.score_record = int(file.read())

        except FileNotFoundError:
            return  
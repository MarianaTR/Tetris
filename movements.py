
#Move the normal piece
 
def move_left(self):
    self.random_bag[0].move(0, -1)
    if self.is_within_the_limit(self.random_bag[0]) == False or self.is_colliding_with_another_piece(self.random_bag[0]) == True:
        self.random_bag[0].move(0, 1)
            

def move_right(self):
    self.random_bag[0].move(0, 1)
    if self.is_within_the_limit(self.random_bag[0]) == False or self.is_colliding_with_another_piece(self.random_bag[0]) == True:
        self.random_bag[0].move(0, -1)

def move_down(self):
    self.random_bag[0].move(1,0)

    if self.is_within_the_limit(self.random_bag[0]) == False or self.is_colliding_with_another_piece(self.random_bag[0]) == True:
        self.random_bag[0].move(-1, 0)
        self.lock_block()

def move_hard_drop(self):
    while True:
        self.random_bag[0].move(1,0)

        if self.is_within_the_limit(self.random_bag[0]) == False or self.is_colliding_with_another_piece(self.random_bag[0]) == True:
            self.random_bag[0].move(-1, 0)
            self.lock_block()
            break

def hourly_rotation(self):
    self.random_bag[0].rotation(1)
    if self.is_within_the_limit(self.random_bag[0]) == False or self.is_colliding_with_another_piece(self.random_bag[0]) == True:
        self.random_bag[0].rotation(-1)

def antihourly_rotation(self):
    self.random_bag[0].rotation(-1)
    if self.is_within_the_limit(self.random_bag[0]) == False or self.is_colliding_with_another_piece(self.random_bag[0]) == True:
        self.random_bag[0].rotation(1)

#Move to ghost piece

def move_left_ghost(self):
    self.ghost_piece.move(-self.ghost_piece.row_offset, 0)
    self.ghost_piece.rotation_state = self.random_bag[0].rotation_state
    self.ghost_piece.move(0,-1)
    if self.is_within_the_limit(self.ghost_piece) == False:
        self.ghost_piece.move(0,1)
    while self.is_colliding_with_another_piece(self.ghost_piece) == True:
        self.ghost_piece.move(-1,0)
        
        
def move_right_ghost(self):
    self.ghost_piece.move(-self.ghost_piece.row_offset, 0)
    self.ghost_piece.rotation_state = self.random_bag[0].rotation_state
    self.ghost_piece.move(0,1)
    if self.is_within_the_limit(self.ghost_piece) == False:
            self.ghost_piece.move(0,-1)
    while self.is_colliding_with_another_piece(self.ghost_piece) ==  True:
        self.ghost_piece.move(-1,0)

def hourly_rotation_ghost(self):
    self.ghost_piece.rotation_state = self.random_bag[0].rotation_state
    while self.is_within_the_limit(self.ghost_piece) == False or self.is_colliding_with_another_piece(self.ghost_piece) == True:
        self.ghost_piece.move(-1,0)
            

def antihourly_rotation_ghost(self):
    self.ghost_piece.rotation_state = self.random_bag[0].rotation_state
    while self.is_within_the_limit(self.ghost_piece) == False or self.is_colliding_with_another_piece(self.ghost_piece) == True:
        self.ghost_piece.move(-1,0)
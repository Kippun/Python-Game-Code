from grid import Grid
from blocks import *
import random
import pygame

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [LBlock(), IBlock(), JBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.suara_muter = pygame.mixer.Sound("assets/sound effects/mutermuter.ogg")
        self.suara_kesamping = pygame.mixer.Sound("assets/sound effects/geserdong.ogg")
        self.suara_hilang1 = pygame.mixer.Sound("assets/sound effects/balokhilang1.ogg")
        self.suara_hilang2 = pygame.mixer.Sound("assets/sound effects/balokhilang2.ogg")
        self.suara_hilang3 = pygame.mixer.Sound("assets/sound effects/balokhilang3.ogg")
        self.suara_hilang4 = pygame.mixer.Sound("assets/sound effects/balokhilang4.ogg")

    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        elif lines_cleared == 4:
            self.score += 700
        self.score += move_down_points

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [LBlock(), IBlock(), JBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    # input key untuk gerak baloknya
    def move_left(self):
        self.current_block.move(0, -1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, 1)
        else:
            self.suara_kesamping.play()

    def move_right(self):
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, -1)
        else:
            self.suara_kesamping.play()

    def move_down(self):
        self.current_block.move(1, 0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1, 0)
            self.lock_block()

    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotation()
        else:
            self.suara_muter.play()

    # syntax saat balok menyentuh dasar tidak bergerak dan menghilangkan balok ketika sudah penuh
    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        if rows_cleared == 1:
            self.suara_hilang1.play()
            self.update_score(rows_cleared, 0)
        if rows_cleared == 2:
            self.suara_hilang2.play()
            self.update_score(rows_cleared, 0)
        if rows_cleared == 3:
            self.suara_hilang3.play()
            self.update_score(rows_cleared, 0)
        if rows_cleared == 4:
            self.suara_hilang4.play()
            self.update_score(rows_cleared, 0)
        if self.block_fits() == False:
            self.game_over = True

    # syntax untuk memunculkan balok selanjutnya
    def reset(self):
        self.grid.reset()
        self.blocks = [LBlock(), IBlock(), JBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.next_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False

    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)

        # variasi pada blok I dan O yang letaknya miring
        if self.next_block.id == 3:
            self.next_block.draw(screen, 285, 115)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 285, 100)
        else:
            self.next_block.draw(screen, 305, 100)
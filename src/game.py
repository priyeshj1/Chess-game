import pygame
from const import *
from board import Board
from dragger import Dargger

class Game:
    def __init__(self):
        self.board = Board()
        self.dragger = Dargger()
        self.next_turn = 'white'

    def bg(self, surface):
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    color = (234, 235, 200)
                else:
                    color = (119, 154, 88) 

                pygame.draw.rect(surface, color, (i * SQUARE_SIZE, j * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    def show_peices(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                peice = self.board.squares[row][col].peice
                if peice != None:
                    peice.set_texture(size=80)
                    if peice is not self.dragger.peice:
                        img = pygame.image.load(peice.texture)
                        img_centre = col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2
                        peice.texture_rect = img.get_rect(center=img_centre)
                        surface.blit(img, peice.texture_rect)
                        

    def show_moves(self, surface):
        if self.dragger.dragging:
            peice = self.dragger.peice
            for move in peice.moves:
                color = '#C86464'
                rect = pygame.Rect(move.final.col * SQUARE_SIZE, move.final.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(surface, color, rect)

    def update_turn(self):
        if self.next_turn == 'white':
            self.next_turn = 'black'
        else:
            self.next_turn = 'white'
    
    def show_last_moves(self, surface):
        last_move = self.board.last_move
        if last_move:
            pygame.draw.rect(surface, 'yellow', (last_move.initial.col * SQUARE_SIZE, last_move.initial.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.rect(surface, 'yellow', (last_move.final.col * SQUARE_SIZE, last_move.final.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        
    def reset(self):
        self.__init__()
                
from const import *
import pygame

from game import Game
from square import Square
from move import Move

from sound import Sound

class Chess:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chess")
        self.game = Game()
        self.sound = Sound()
    
    def run(self):
        screen = self.screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger
        sound = self.sound
        
        while True:
            game.bg(screen)
            game.show_last_moves(screen)
            game.show_moves(screen)
            game.show_peices(screen)

            if dragger.dragging:
                dragger.update_blit(screen)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update(event.pos)
                    select_row = event.pos[1] // SQUARE_SIZE
                    select_col = event.pos[0] // SQUARE_SIZE

                    if board.squares[select_row][select_col].peice != None:
                        peice = board.squares[select_row][select_col].peice
                        if peice.color == game.next_turn:
                            board.calc_moves(peice, select_row, select_col)
                            dragger.save_pos_initial()
                            dragger.drag(peice)
                            game.bg(screen)
                            game.show_last_moves(screen)
                            game.show_moves(screen)
                            game.show_peices(screen)
                            
                        
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update(event.pos)
                        game.bg(screen)
                        game.show_last_moves(screen)
                        game.show_moves(screen)
                        game.show_peices(screen)
                        dragger.update_blit(screen)

                elif event.type == pygame.MOUSEBUTTONUP:
                    if dragger.dragging:
                        dragger.update(event.pos)
                        release_row = event.pos[1] // SQUARE_SIZE
                        release_col = event.pos[0] // SQUARE_SIZE

                        # MOVE LOGIC
                        initial = Square(dragger.initial[0], dragger.initial[1])
                        final = Square(release_row, release_col, board.squares[release_row][release_col].peice)


                        move = Move(initial, final)
                        if move in dragger.peice.moves:
                            if final.peice != None:
                                sound.play('kill')
                            else:
                                sound.play('move')
                            board.move(dragger.peice, move)
                            game.bg(screen)
                            game.show_peices(screen)
                            game.update_turn()
                            board.last_move = move

                    dragger.undrag()
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game.reset()
                        game = self.game
                        board = self.game.board
                        dragger = self.game.dragger
                        
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.display.update()


Chess = Chess()
Chess.run()
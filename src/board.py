from const import *
from square import Square
from piece import *
from move import Move

import tkinter as tk
from tkinter import simpledialog

class Board:

    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]
        self.last_move = None
        self._create()
        self.add_piece('white')
        self.add_piece('black')

    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def add_piece(self, color):
        row_pawn, row_other = (6, 7) if color == "white" else (1, 0)

        for i in range(COLS):
            self.squares[row_pawn][i] = Square(row_pawn, i, Pawn(color))    
        
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))
        self.squares[row_other][4] = Square(row_other, 4, King(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))
        
    def calc_moves(self, peice, row, col):

        def knight_moves():
            # 8 possible moves
            possible_moves = [
                (row-2, col+1),
                (row-1, col+2),
                (row+1, col+2),
                (row+2, col+1),
                (row+2, col-1),
                (row+1, col-2),
                (row-1, col-2),
                (row-2, col-1),
            ]

            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move

                if Square.ingrid(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].possible_move(peice.color):
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        move = Move(initial, final)
                        peice.add_moves(move)
                        

        def pawn_moves():

            #vertical moves
            steps = 1 if peice.moved else 2
            pos_moves = [(row  + peice.dir * (1 + i), col) for i in range(steps)]
            for possible_move in pos_moves:
                possible_move_row, possible_move_col = possible_move
                if Square.ingrid(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty():
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        move = Move(initial, final)
                        peice.add_moves(move)
                    else:
                        break
                else:
                    break
            
            #diagonal moves
            possible_moves = [
                (row + peice.dir, col + 1),
                (row + peice.dir, col - 1),
            ]
            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                if Square.ingrid(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isenemy(peice.color):
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        move = Move(initial, final)
                        peice.add_moves(move)


        def linear_moves(incrs):
            for incr in incrs:
                row_incr, col_incr = incr
                for i in range(1, 8):
                    possible_move = (row + row_incr * i, col + col_incr * i)
                    if Square.ingrid(*possible_move):
                        if self.squares[possible_move[0]][possible_move[1]].isempty():
                            initial = Square(row, col)
                            final = Square(*possible_move)
                            move = Move(initial, final)
                            peice.add_moves(move)
                        else:
                            if self.squares[possible_move[0]][possible_move[1]].isenemy(peice.color):
                                initial = Square(row, col)
                                final = Square(*possible_move)
                                move = Move(initial, final)
                                peice.add_moves(move)
                            break
                    else:
                        break

        def king_moves():
            possible_moves = [
                (row - 1, col - 1),
                (row - 1, col),
                (row - 1, col + 1),
                (row, col - 1),
                (row, col + 1),
                (row + 1, col - 1),
                (row + 1, col),
                (row + 1, col + 1),
            ]

            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                if Square.ingrid(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].possible_move(peice.color):
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        move = Move(initial, final)
                        peice.add_moves(move)

            # castling
            if not peice.moved:
                # queen side
                left_rook = self.squares[row][0].peice
                if left_rook and left_rook.name == 'rook' and not left_rook.moved:
                    pos = True
                    for i in range(1, 4):
                        if not self.squares[row][col - i].isempty():
                            pos = False
                            break
                    if pos:
                        # move for rook
                        initial = Square(row, 0)
                        final = Square(row, 3)
                        move = Move(initial, final)
                        left_rook.add_moves(move)

                        # move for king
                        initial = Square(row, col)
                        final = Square(row, 2)
                        move = Move(initial, final)
                        peice.add_moves(move)
                
                # king side
                right_rook = self.squares[row][7].peice
                if right_rook and right_rook.name == 'rook' and not right_rook.moved:
                    pos = True
                    for i in range(1, 3):
                        if not self.squares[row][col + i].isempty():
                            pos = False
                            break
                    if pos:
                        # move for rook
                        initial = Square(row, 7)
                        final = Square(row, 5)
                        move = Move(initial, final)
                        right_rook.add_moves(move)

                        # move for king
                        initial = Square(row, col)
                        final = Square(row, 6)
                        move = Move(initial, final)
                        peice.add_moves(move)

        def bishop_moves():
            linear_moves([(1, 1), (1, -1), (-1, 1), (-1, -1)])

        def rook_moves():
            linear_moves([(0, 1), (0, -1), (1, 0), (-1, 0)])

        if peice.name == 'pawn':
            pawn_moves()
        elif peice.name == 'knight':
            knight_moves()
        elif peice.name == 'bishop':
            bishop_moves()
        elif peice.name == 'rook':
            rook_moves()
        elif peice.name == 'queen':
            bishop_moves()
            rook_moves()
        elif peice.name == 'king':
            king_moves()
    
    def move(self, peice, move):
        initial = move.initial
        final = move.final
        self.squares[initial.row][initial.col].peice = None
        self.squares[final.row][final.col].peice = peice

        # pawn promotion
        if peice.name == 'pawn' and (final.row == 7 or final.row == 0):
            choice = self.get_promotion_choice()

            if choice == 'Q':
                self.squares[final.row][final.col].peice = Queen(peice.color)
            elif choice == 'R':
                self.squares[final.row][final.col].peice = Rook(peice.color)
            elif choice == 'B':
                self.squares[final.row][final.col].peice = Bishop(peice.color)
            elif choice == 'N':
                self.squares[final.row][final.col].peice = Knight(peice.color)

        peice.moved = True

        peice.moves = []
        self.last_move = move
    
        # castle
        if peice.name == 'king' and abs(initial.col - final.col) == 2:
            if initial.col < final.col:
                rook = self.squares[initial.row][7].peice
            else:
                rook = self.squares[initial.row][0].peice
            self.move(rook, rook.moves[-1])

    def get_promotion_choice(self):
        root = tk.Tk()
        root.withdraw()  # Hide the main window

        prompt = "Choose a piece to promote to, Queen(Q) or Rook(R) or Bishop(B) or Knight(N):"
        choice = simpledialog.askstring("Pawn Promotion", prompt, initialvalue="Q")

        root.destroy()

        return choice

        
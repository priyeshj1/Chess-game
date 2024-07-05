import os

class Peice:
    def __init__(self, color, name, value, texture=None, texture_rect=None):
        self.color = color
        self.name = name
        self.value = value  
        self.texture = texture
        self.set_texture(self)
        self.texture_rect = texture_rect
        self.moves = []
        self.moved = False

    def set_texture(self, size=80):
        self.texture = os.path.join(f'util/images/imgs-{size}px/{self.color}_{self.name}.png')
        
    def add_moves(self, move):
        self.moves.append(move)

class Pawn(Peice):
    def __init__(self, color):
        self.dir = -1 if color == "white" else 1
        super().__init__(color, "pawn", 1)

class Knight(Peice):
    def __init__(self, color):
        super().__init__(color, "knight", 3)

class Bishop(Peice):
    def __init__(self, color):
        super().__init__(color, "bishop", 3)

class Rook(Peice):
    def __init__(self, color):
        super().__init__(color, "rook", 5)

class Queen(Peice):
    def __init__(self, color):
        super().__init__(color, "queen", 9)

class King(Peice):
    def __init__(self, color):
        super().__init__(color, "king", 999999)


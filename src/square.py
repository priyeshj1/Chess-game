class Square:
    def __init__(self, row, col, peice=None):
        self.row = row
        self.col = col
        self.peice = peice

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col
    
    @staticmethod
    def ingrid(*args):
        for arg in args:
            if arg < 0 or arg > 7:
                return False
        return True
    
    def isempty(self):
        return self.peice is None
    
    def isenemy(self, color):
        return self.peice is not None and self.peice.color != color

    def possible_move(self, color):
        return self.isempty() or self.isenemy(color)
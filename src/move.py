
class Move():
    def __init__(self, start, end):
        self.initial = start
        self.final = end
    
    def __eq__(self, other):
        return self.initial == other.initial and self.final == other.final
        
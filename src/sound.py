import pygame 

pygame.mixer.init()

class Sound:
    def __init__(self):
        self.move = pygame.mixer.Sound('util/sounds/move.wav')
        self.kill = pygame.mixer.Sound('util/sounds/capture.wav')
    
    def play(self, sound):
        if sound == 'move':
            self.move.play()
        elif sound == 'kill':
            self.kill.play()
    

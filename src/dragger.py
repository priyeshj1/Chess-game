import pygame
from const import *

class Dargger:
    def __init__(self):
        self.mousex = 0
        self.mousey = 0
        self.initial = (0, 0)
        self.dragging = False
        self.peice = None
    
    def update_blit(self, surface):
        img = pygame.image.load(self.peice.texture)
        img_centre = (self.mousex, self.mousey)
        self.peice.texture_rect = img.get_rect(center=img_centre)
        surface.blit(img, self.peice.texture_rect)

    def update(self, pos):
        self.mousex, self.mousey = pos

    def save_pos_initial(self):
        self.initial = (self.mousey // SQUARE_SIZE, self.mousex // SQUARE_SIZE)

    def drag(self, peice):
        self.dragging = True
        self.peice = peice
    
    def undrag(self):
        self.dragging = False
        self.peice = None
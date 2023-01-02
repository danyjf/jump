import pygame
from pygame import *
from pygame.sprite import *

class Ground:
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 1024, 32)
        self.image = pygame.image.load("assets/sprites/ground.png").convert_alpha()

    def update(self, game):
        pass
    
    def render(self, display):
        display.blit(self.image , self.rect)

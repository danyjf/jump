import pygame
from pygame import *
from pygame.sprite import *


class FloatingPlatform:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 150, 32)
        Sprite.__init__(self)
        self.image = pygame.image.load("platform.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (150,32))

    def update(self, delta_time):
        pass
    
    def render(self, display):
        display.blit(self.image , self.rect)

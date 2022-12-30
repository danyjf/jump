import pygame
from pygame import *
from pygame.sprite import *

class Ground:
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 1024, 32)
        self.image = pygame.image.load("ground.png").convert_alpha()
        #self.image = pygame.transform.scale(self.image, (1027,132))

    def update(self, delta_time):
        pass
    
    def render(self, display):
        display.blit(self.image , self.rect)

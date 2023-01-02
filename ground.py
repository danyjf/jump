import pygame
from pygame import *
from pygame.sprite import *

from entity import Entity

class Ground(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 1024, 110)
        Sprite.__init__(self)
        self.image = pygame.image.load("assets/sprites/ground.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (1024, 110))

    def render(self, display):
        display.blit(self.image , self.rect)

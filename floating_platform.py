﻿import pygame
import random

from platforms import Platform
from settings import WIDTH, HEIGHT

class FloatingPlatform(Platform):
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 150, 32)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("platform.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (150,32))

    def update(self, game):
        pass
    
    def render(self, display):
        display.blit(self.image , self.rect)
    
    def clone(self):
        return FloatingPlatform(random.randint(0, WIDTH - self.rect.width), -40)

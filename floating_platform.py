import pygame
import random

from platforms import Platform
from settings import WIDTH, HEIGHT

class FloatingPlatform(Platform):
    def __init__(self, x_min, x_max, y):
        self.x_min = x_min
        self.x_max = x_max
        self.y = y
        self.rect = pygame.Rect(random.randint(x_min, x_max), y, 150, 32)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/sprites/platform.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (150,32))

    def update(self, game):
        pass
    
    def render(self, display):
        display.blit(self.image , self.rect)
    
    def clone(self):
        return FloatingPlatform(self.x_min, self.x_max, self.y)

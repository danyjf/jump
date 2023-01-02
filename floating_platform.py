import pygame
import random

from platforms import Platform

class FloatingPlatform(Platform):
    def __init__(self, x_min, x_max, y):
        # initialize the platform to a random x value between the x_min and x_max
        super().__init__(random.randint(x_min, x_max), y, 150, 32)
        self.x_min = x_min
        self.x_max = x_max
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/sprites/platform.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 32))

    def render(self, display):
        display.blit(self.image , self.rect)
    
    def clone(self):
        return FloatingPlatform(self.x_min, self.x_max, self.rect.y)

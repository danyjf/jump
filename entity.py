import pygame

class Entity:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
    
    def update(self, game):
        pass
    
    def render(self, display):
        pass

import pygame

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def update(self):
        pass
    
    def render(self, display):
        pygame.draw.rect(display, 'red', (self.x, self.y, 32, 32))

import pygame

class Ground:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 1024, 32)

    def update(self, delta_time):
        pass
    
    def render(self, display):
        pygame.draw.rect(display, 'yellow', self.rect)

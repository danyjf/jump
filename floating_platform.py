import pygame

class FloatingPlatform:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 150, 32)

    def update(self, delta_time):
        pass
    
    def render(self, display):
        pygame.draw.rect(display, 'brown', self.rect)

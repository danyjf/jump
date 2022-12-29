import pygame

class Background:
    def __init__(self, width, height):
        self.i = 0
        self.width = width
        self.height = height
        self.image = pygame.image.load("assets/sprites/sky.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
    
    def update(self, delta_time):
        pass
    
    def render(self, display):
        self.i += 0.5

        display.blit(self.image, (self.i, 0))
        display.blit(self.image, (self.width + self.i, 0))

        if self.i == -self.width:
            display.blit(self.image, (self.width + self.i, 0))
            self.i = 0

        self.i -= 1

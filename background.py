import pygame

class Background:
    def __init__(self, width, height):
        self.scroll = 0
        self.scroll_speed = 0.5
        self.width = width
        self.height = height
        self.image = pygame.image.load("assets/sprites/sky.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
    
    def render(self, display):
        # render the image on the position of the scroll
        display.blit(self.image, (self.scroll, 0))
        # render the image again right next to the previous one
        display.blit(self.image, (self.width + self.scroll, 0))

        # when the scroll has done a full loop reset it
        if self.scroll <= -self.width:
            self.scroll = 0

        # decrease the scroll value so that the image scrolls from right to left
        self.scroll -= self.scroll_speed

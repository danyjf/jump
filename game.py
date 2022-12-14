import pygame

from player import Player

class Game:
    def __init__(self, width, height):
        self.display = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

        self.running = True
        self.entities = [Player()]
    
    def loop(self):
        while self.running:
            self.handle_events()
            self.process_input()
            self.update()
            self.render()
            self.clock.tick(15)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def process_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            pass
        elif keys[pygame.K_DOWN]:
            pass
        elif keys[pygame.K_LEFT]:
            pass
        elif keys[pygame.K_RIGHT]:
            pass
    
    def update(self):
        for entity in self.entities:
            entity.update()
    
    def render(self):
        self.display.fill("white")
        
        for entity in self.entities:
            entity.render(self.display)
        
        pygame.display.flip()

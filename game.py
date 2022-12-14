import pygame

from player import Player
from input_handler import InputHandler

class Game:
    def __init__(self, width, height):
        self.display = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

        self.running = True
        self.input_handler = InputHandler()
        self.delta_time = 0
        
        self.player = Player()
        self.entities = [self.player]
    
    def loop(self):
        while self.running:
            self.delta_time = self.clock.tick(60) / 1000
            self.handle_events()
            self.process_input()
            self.update()
            self.render()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def process_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            command = self.input_handler.handle_input('up')
            command.execute(self.player)
        if keys[pygame.K_LEFT]:
            command = self.input_handler.handle_input('left')
            command.execute(self.player)
        if keys[pygame.K_RIGHT]:
            command = self.input_handler.handle_input('right')
            command.execute(self.player)
    
    def update(self):
        for entity in self.entities:
            entity.update(self.delta_time)
    
    def render(self):
        self.display.fill("white")
        
        for entity in self.entities:
            entity.render(self.display)
        
        pygame.display.flip()

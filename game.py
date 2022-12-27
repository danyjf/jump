import pygame

from input_handler import InputHandler
from player import Player
from ground import Ground
from floating_platform import FloatingPlatform
from camera import Camera

class Game:
    def __init__(self, width, height):
        self.display = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

        self.running = True
        self.input_handler = InputHandler()
        self.delta_time = 0
        
        self.player1 = Player(100, 0, 'red')
        self.player2 = Player(892, 0, 'green')
        self.camera = Camera(self.player1, self.player2)
        self.entities = [
            self.player1, 
            self.player2, 
            Ground(0, 544),
            FloatingPlatform(0, 450)
        ]
    
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
        
        if keys[pygame.K_w]:
            command = self.input_handler.handle_input('w')
            command.execute(self.player1)
        if keys[pygame.K_a]:
            command = self.input_handler.handle_input('a')
            command.execute(self.player1)
        if keys[pygame.K_d]:
            command = self.input_handler.handle_input('d')
            command.execute(self.player1)
        
        if keys[pygame.K_UP]:
            command = self.input_handler.handle_input('up')
            command.execute(self.player2)
        if keys[pygame.K_LEFT]:
            command = self.input_handler.handle_input('left')
            command.execute(self.player2)
        if keys[pygame.K_RIGHT]:
            command = self.input_handler.handle_input('right')
            command.execute(self.player2)
    
    def update(self):
        for entity in self.entities:
            entity.update(self.delta_time)
        
        self.player1.is_on_ground = False
        self.player2.is_on_ground = False
        for entity in self.entities:
            if entity != self.player1 and entity != self.player2:
                if entity.rect.colliderect(self.player1.rect):
                    self.player1.collision(entity)
                if entity.rect.colliderect(self.player2.rect):
                    self.player2.collision(entity)
        
        self.camera.update(self.entities)
    
    def render(self):
        self.display.fill("white")
        
        for i in range(len(self.entities) - 1, -1, -1):
            self.entities[i].render(self.display)
        
        pygame.display.flip()

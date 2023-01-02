import pygame

from input_handler import InputHandler
from player import Player
from ground import Ground
from floating_platform import FloatingPlatform
from camera import Camera
from background import Background
from scoreboard import ScoreBoard
from platform_spawn_manager import PlatformSpawnManager
from settings import WIDTH, HEIGHT
from win_screen import WinScreen

class Game:
    def __init__(self):
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        pygame.mixer.music.load('assets/sounds/music.mp3')
        pygame.mixer.music.play(-1)

        self.running = True
        self.input_handler = InputHandler()
        self.delta_time = 0
        
        ground = Ground(0, 544)
        self.player1 = Player('Player1', 100, 513, ground)
        self.player2 = Player('Player2', 892, 513, ground)
        self.camera = Camera(self.player1, self.player2)
        
        self.ui = [
            ScoreBoard(self.player1, self.player2),
            WinScreen(self.player1, self.player2)
        ]
        self.entities = [
            self.player1, 
            self.player2, 
            ground,
            PlatformSpawnManager(self.player1, self.player2),
            FloatingPlatform(0, WIDTH / 2 - 150, 190),
            FloatingPlatform(WIDTH / 2 - 150, WIDTH - 150, 190), 
            FloatingPlatform(0, WIDTH - 150, 300), 
            FloatingPlatform(WIDTH / 2 - 150, WIDTH - 150, 300), 
            FloatingPlatform(0, WIDTH - 150, 420), 
            FloatingPlatform(WIDTH / 2 - 150, WIDTH - 150, 420) 
        ]
        self.background = [
            Background(WIDTH, HEIGHT)
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
        # update the game objects
        for entity in self.entities:
            entity.update(self)
        
        # detect the collisions
        self.player1.is_on_ground = False
        self.player2.is_on_ground = False
        for entity in self.entities:
            if isinstance(entity, Ground) or isinstance(entity, FloatingPlatform):
                if entity.rect.colliderect(self.player1.rect):
                    self.player1.collision(entity)
                if entity.rect.colliderect(self.player2.rect):
                    self.player2.collision(entity)
        
        # update the camera
        self.camera.update(self.entities)
    
    def render(self):
        self.display.fill('white')
        
        # render the background objects
        for i in range(len(self.background) - 1, -1, -1):
            self.background[i].render(self.display)
        
        # render the game objects on top
        for i in range(len(self.entities) - 1, -1, -1):
            self.entities[i].render(self.display)

        # render the ui on top
        for i in range(len(self.ui) - 1, -1, -1):
            self.ui[i].render(self.display)
        
        pygame.display.flip()

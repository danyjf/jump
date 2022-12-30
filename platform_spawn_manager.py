import pygame
import random

from spawner import Spawner
from floating_platform import FloatingPlatform
from settings import WIDTH

class PlatformSpawnManager:
    def __init__(self, player1, player2):
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.player1 = player1
        self.player2 = player2
        self.max_height = 0
        self.can_add_platforms = True
        self.spawner = Spawner()
        self.platform_left = FloatingPlatform(0, WIDTH / 2 - 150, -40)
        self.platform_right = FloatingPlatform(WIDTH / 2, WIDTH - 150, -40)
        self.platform_middle = FloatingPlatform(round(WIDTH / 3), round((2 / 3) * WIDTH) - 150, -40)
    
    def update(self, game):
        if max(self.player1.dist_from_ground, self.player2.dist_from_ground) > self.max_height:
            self.max_height = max(self.player1.dist_from_ground, self.player2.dist_from_ground)
        
        if self.can_add_platforms and self.max_height % 100 >= 90:
            if random.randint(0, 1) == 0:
                game.entities.append(self.spawner.spawn_platform(self.platform_left))
                game.entities.append(self.spawner.spawn_platform(self.platform_right))
            else:
                game.entities.append(self.spawner.spawn_platform(self.platform_middle))
            self.can_add_platforms = False
        elif self.max_height % 100 < 90:
            self.can_add_platforms = True
    
    def render(self, display):
        pass

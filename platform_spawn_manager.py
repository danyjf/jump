import pygame

from spawner import Spawner
from floating_platform import FloatingPlatform

class PlatformSpawnManager:
    def __init__(self, player1, player2):
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.player1 = player1
        self.player2 = player2
        self.max_height = 0
        self.can_add_platforms = True
        self.spawner = Spawner()
        self.platform = FloatingPlatform(0, 0)
    
    def update(self, game):
        if self.player1.dist_from_ground > self.max_height:
            self.max_height = self.player1.dist_from_ground
        
        if self.can_add_platforms and self.max_height % 100 >= 90:
            game.entities.append(self.spawner.spawn_platform(self.platform))
            self.can_add_platforms = False
        elif self.max_height % 100 < 90:
            self.can_add_platforms = True
    
    def render(self, display):
        pass

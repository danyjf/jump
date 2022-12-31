import pygame
from pygame import *
from pygame.sprite import *
from states import Idle
from ground import Ground
from floating_platform import FloatingPlatform
from subject import Subject
from events import EVENT_HEIGHT_CHANGE, EVENT_DEATH
from settings import HEIGHT

class Player(Subject, Sprite):
    def __init__(self, name, x, y, ground, color):
        super().__init__()
        Sprite.__init__(self)
        self.image = pygame.image.load("assets/sprites/mariostand.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (32,32))
        self.name = name
        self.rect = pygame.Rect(x, y, 32, 32)
        self.ground = ground
        self.dist_from_ground = self.ground.rect.top - (self.rect.bottom - 1)
        self.color = color
        self.movement_speed = 200
        self.jump_speed = -400
        self.velocity_x = 0
        self.velocity_y = 0
        self.gravity = 600
        self.state = Idle()
        self.is_on_ground = False
    
    def update(self, game):
        new_state = self.state.update(self, game.delta_time)
        if new_state != None:
            self.state = new_state
            self.state.enter()
        
        new_dist_from_ground = self.ground.rect.top - (self.rect.bottom - 1)
        if new_dist_from_ground != self.dist_from_ground:
            self.dist_from_ground = new_dist_from_ground
            self.notify(self, EVENT_HEIGHT_CHANGE)
        
        if self.rect.y > HEIGHT:
            self.notify(self, EVENT_DEATH)
    
    def render(self, display):
        display.blit(self.image, self.rect)

    def up(self):
        if self.velocity_y == 0:
            self.velocity_y = self.jump_speed
    
    def left(self):
        if self.velocity_x == self.movement_speed:
            self.velocity_x = 0
        else:
            self.velocity_x = -self.movement_speed
    
    def right(self):
        if self.velocity_x == -self.movement_speed:
            self.velocity_x = 0
        else:
            self.velocity_x = self.movement_speed
    
    def get_direction_x(self):
        if self.velocity_x > 0:
            return 1
        elif self.velocity_x < 0:
            return -1
        return 0

    def collision(self, other):
        if isinstance(other, Ground) or isinstance(other, FloatingPlatform):
            if self.velocity_y < 0:
                self.is_on_ground = False
            else:
                # plus one because otherwise the rects dont overlap and the 
                # collision is not detected
                self.rect.bottom = other.rect.top + 1
                self.is_on_ground = True
                self.velocity_y = 0

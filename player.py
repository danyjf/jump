import pygame
from pygame import *
from pygame.sprite import *
from states import Idle
from input_handler import Left
from input_handler import Right
from ground import Ground
from floating_platform import FloatingPlatform
from subject import Subject
from events import EVENT_HEIGHT_CHANGE

width=1024
height=576

class Player(Subject, Sprite):
    def __init__(self, name, x, y, ground, color):
        super().__init__()
        Sprite.__init__(self)
        self.idle_image = pygame.image.load("mariostand.png").convert_alpha()
        self.idle_image = pygame.transform.scale(self.idle_image, (32,32))
        self.walk_image = pygame.image.load("mariostand.png").convert_alpha()
        self.walk_image = pygame.transform.scale(self.walk_image, (32,32))
        self.jump_image = pygame.image.load("mariojump_r.png").convert_alpha()
        self.jump_image = pygame.transform.scale(self.jump_image, (32,32))
        self.fall_image = pygame.image.load("mariojump_r.png").convert_alpha()
        self.fall_image = pygame.transform.scale(self.jump_image, (32,32))
        self.display_image = None
        self.flip_image = False
        self.name = name
        self.rect = pygame.Rect(x, y, 32, 32)
        self.ground = ground
        self.dist_from_ground = self.ground.rect.top - (self.rect.bottom - 1)

        self.color = color
        self.movement_speed = 100
        self.jump_speed = -400
        self.velocity_x = 0
        self.velocity_y = 0
        self.gravity = 600
        self.state = Idle()
        self.state.enter(self)
        self.is_on_ground = False
    
    def update(self, delta_time):
        new_state = self.state.update(self, delta_time)
        if new_state != None:
            self.state = new_state
            self.state.enter(self)
        
        new_dist_from_ground = self.ground.rect.top - (self.rect.bottom - 1)
        if new_dist_from_ground != self.dist_from_ground:
            self.dist_from_ground = new_dist_from_ground
            self.notify(self, EVENT_HEIGHT_CHANGE)
        
        self.screen_limits()
    
    def render(self, display):
        if not self.flip_image:
            display.blit(self.display_image, self.rect)
        else:
            display.blit(pygame.transform.flip(self.display_image, True, False), self.rect)

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

    def screen_limits(self):
        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.top <= 0:
            self.rect.top = 0
    
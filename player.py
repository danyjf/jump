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
        self.image = pygame.image.load("mariostand2.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (32,32))
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
        self.is_on_ground = False

    
    def update(self, delta_time):
        new_state = self.state.update(self, delta_time)
        if new_state != None:
            self.state = new_state
            self.state.enter()
        
        new_dist_from_ground = self.ground.rect.top - (self.rect.bottom - 1)
        if new_dist_from_ground != self.dist_from_ground:
            self.dist_from_ground = new_dist_from_ground
            self.notify(self, EVENT_HEIGHT_CHANGE)
    
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

    def screen_limits(self):
        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.top <= 0:
            self.rect.top = 0
        

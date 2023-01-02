import pygame
from pygame import *
from pygame.sprite import *
from states import Idle
from ground import Ground
from floating_platform import FloatingPlatform
from subject import Subject
from events import EVENT_HEIGHT_CHANGE, EVENT_DEATH
from settings import WIDTH, HEIGHT
from player_sprite import PlayerSprite
from player_sound import PlayerSound

class Player(Subject):
    def __init__(self, name, x, y, ground):
        super().__init__()
        self.player_sprite = PlayerSprite()
        self.player_sound = PlayerSound()
        self.name = name
        self.rect = pygame.Rect(x, y, 32, 32)
        self.ground = ground
        self.dist_from_ground = self.ground.rect.top - (self.rect.bottom - 1)
        self.movement_speed = 200
        self.jump_speed = -400
        self.velocity_x = 0
        self.velocity_y = 0
        self.gravity = 600
        self.state = Idle()
        self.state.enter(self)
        self.is_on_ground = False
    
    def update(self, game):
        new_state = self.state.update(self, game.delta_time)
        if new_state != None:
            self.state = new_state
            self.state.enter(self)
        
        new_dist_from_ground = self.ground.rect.top - (self.rect.bottom - 1)
        if new_dist_from_ground != self.dist_from_ground:
            self.dist_from_ground = new_dist_from_ground
            self.notify(self, EVENT_HEIGHT_CHANGE)
        
        self.screen_limits()
    
    def render(self, display):
        if not self.player_sprite.flip_image:
            display.blit(self.player_sprite.display_image, self.rect)
        else:
            display.blit(pygame.transform.flip(self.player_sprite.display_image, True, False), self.rect)

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
        # keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.y > HEIGHT:
            self.notify(self, EVENT_DEATH)
    
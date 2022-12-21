import pygame

from states import Idle, Walking

class Player:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.movement_speed = 100
        self.jump_speed = -400
        self.velocity_x = 0
        self.velocity_y = 0
        self.gravity = 600
        self.state = Idle()
    
    def update(self, delta_time):
        new_state = self.state.update(self, delta_time)
        if new_state != None:
            self.state = new_state
            self.state.enter()
        
        # self.velocity_x = 0
        if self.y > 576 - 32:
            self.y = 576 - 32
            self.velocity_y = 0
    
    def render(self, display):
        pygame.draw.rect(display, self.color, (self.x, self.y, 32, 32))

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
    
    def is_on_ground(self):
        if self.y >= 576 - 32:
            return True
    
    def get_direction_x(self):
        if self.velocity_x > 0:
            return 1
        elif self.velocity_x < 0:
            return -1
        return 0

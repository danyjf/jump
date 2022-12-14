import pygame

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.movement_speed = 100
        self.jump_speed = -200
        self.velocity_x = 0
        self.velocity_y = 0
        self.gravity = 200
    
    def update(self, delta_time):
        self.velocity_y += self.gravity * delta_time
        self.x += self.velocity_x * delta_time
        self.y += self.velocity_y * delta_time
        self.velocity_x = 0
        
        if self.y > 576 - 32:
            self.y = 576 - 32
            self.velocity_y = 0
    
    def render(self, display):
        pygame.draw.rect(display, 'red', (self.x, self.y, 32, 32))

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

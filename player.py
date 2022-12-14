import pygame

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.movement_speed = 50
        self.jump_speed = -200
        self.velocity = [0, 0]
        self.gravity = 200
    
    def update(self, delta_time):
        self.velocity[1] += self.gravity * delta_time
        self.x += self.velocity[0] * delta_time
        self.y += self.velocity[1] * delta_time
        self.velocity[0] = 0
        
        if self.y > 576 - 32:
            self.y = 576 - 32
        print(self.y)
    
    def render(self, display):
        pygame.draw.rect(display, 'red', (self.x, self.y, 32, 32))

    def up(self):
        self.velocity[1] = self.jump_speed
    
    def left(self):
        self.velocity[0] = -self.movement_speed
    
    def right(self):
        self.velocity[0] = self.movement_speed

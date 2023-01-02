import pygame
from pygame import *


class State:
    def __init__(self, name):
        self.name = name
    
    def enter(self, player):
        print(f'Entering {self.name}')
    
    def update(self, player, delta_time):
        pass
    
    def exit(self, player):
        pass

class Idle(State):
    def __init__(self):
        super().__init__(self.__class__.__name__)
    
    def enter(self, player):
        player.display_image = player.idle_image
    
    def update(self, player, delta_time):
        direction_x = player.get_direction_x()
        
        if player.velocity_y < 0:
            return Jumping()
        elif direction_x != 0:
            return Walking()
        elif not player.is_on_ground:
            return Falling()

class Walking(State):
    def __init__(self):
        super().__init__(self.__class__.__name__)
    
    def enter(self, player):
        player.display_image = player.walk_image
    
    def update(self, player, delta_time):
        direction_x = player.get_direction_x()
        
        if direction_x == 1:
            player.flip_image = False
        elif direction_x == -1:
            player.flip_image = True
        
        player.rect.x += round(player.velocity_x * delta_time)
        player.velocity_x = 0
        
        if player.velocity_y < 0:
            return Jumping()
        elif direction_x == 0:
            return Idle()
        elif not player.is_on_ground:
            return Falling()

class Jumping(State):
    def __init__(self):
        super().__init__(self.__class__.__name__)
    
    def enter(self, player):
        player.display_image = player.jump_image
    
    def update(self, player, delta_time):
        direction_x = player.get_direction_x()
        
        if direction_x == 1:
            player.flip_image = False
        elif direction_x == -1:
            player.flip_image = True
        
        player.velocity_y += player.gravity * delta_time
        player.rect.x += round(player.velocity_x * delta_time)
        player.rect.y += round(player.velocity_y * delta_time)
        player.velocity_x = 0
        
        if player.is_on_ground:
            if direction_x == 0:
                return Idle()
            else:
                return Walking()

class Falling(State):
    def __init__(self):
        super().__init__(self.__class__.__name__)
    
    def enter(self, player):
        player.display_image = player.fall_image
    
    def update(self, player, delta_time):
        direction_x = player.get_direction_x()
        
        if direction_x == 1:
            player.flip_image = False
        elif direction_x == -1:
            player.flip_image = True
        
        player.velocity_y += player.gravity * delta_time
        player.rect.x += round(player.velocity_x * delta_time)
        player.rect.y += round(player.velocity_y * delta_time)
        player.velocity_x = 0
        
        if player.is_on_ground:
            if direction_x == 0:
                return Idle()
            else:
                return Walking()

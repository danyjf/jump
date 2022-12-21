class State:
    def __init__(self, name):
        self.name = name
    
    def enter(self):
        print(f'Entering {self.name}')
    
    def update(self, player, delta_time):
        pass
    
    def exit(self):
        pass

class Idle(State):
    def __init__(self):
        super().__init__(self.__class__.__name__)
    
    def update(self, player, delta_time):
        if player.velocity_y < 0:
            return Jumping()
        elif player.velocity_x != 0:
            return Walking()
        
        player.velocity_y += player.gravity * delta_time
        player.y += player.velocity_y * delta_time

class Walking(State):
    def __init__(self):
        super().__init__(self.__class__.__name__)
    
    def update(self, player, delta_time):
        if player.velocity_x == 0:
            return Idle()
        
        player.velocity_y += player.gravity * delta_time
        player.x += player.velocity_x * delta_time
        player.y += player.velocity_y * delta_time

class Jumping(State):
    def __init__(self):
        super().__init__(self.__class__.__name__)
    
    def update(self, player, delta_time):
        if player.velocity_y == 0 and player.velocity_x != 0:
            return Walking()
        elif player.velocity_y == 0:
            return Idle()

        player.velocity_y += player.gravity * delta_time
        player.x += player.velocity_x * delta_time
        player.y += player.velocity_y * delta_time

class Falling(State):
    def __init__(self):
        super().__init__(self.__class__.__name__)
    
    def update(self, player, delta_time):
        if player.velocity_y == 0:
            return Idle()
        
        player.velocity_y += player.gravity * delta_time
        player.x += player.velocity_x * delta_time
        player.y += player.velocity_y * delta_time

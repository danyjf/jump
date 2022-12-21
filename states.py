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
        elif not player.is_on_ground():
            return Falling()

class Walking(State):
    def __init__(self):
        super().__init__(self.__class__.__name__)
    
    def update(self, player, delta_time):
        player.velocity_y += player.gravity * delta_time
        player.x += player.velocity_x * delta_time
        player.y += player.velocity_y * delta_time
        
        if player.velocity_y < 0:
            return Jumping()
        elif player.velocity_x == 0:
            return Idle()
        elif not player.is_on_ground():
            return Falling()

class Jumping(State):
    def __init__(self):
        super().__init__(self.__class__.__name__)
    
    def update(self, player, delta_time):
        player.velocity_y += player.gravity * delta_time
        player.x += player.velocity_x * delta_time
        player.y += player.velocity_y * delta_time
        
        if player.is_on_ground():
            if player.velocity_x == 0:
                return Idle()
            else:
                return Walking()

class Falling(State):
    def __init__(self):
        super().__init__(self.__class__.__name__)
    
    def update(self, player, delta_time):
        player.velocity_y += player.gravity * delta_time
        player.x += player.velocity_x * delta_time
        player.y += player.velocity_y * delta_time
        
        if player.is_on_ground():
            if player.velocity_x == 0:
                return Idle()
            else:
                return Walking()

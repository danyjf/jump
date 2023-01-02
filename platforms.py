from entity import Entity

class Platform(Entity):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
    
    def clone(self):
        return NotImplemented

from spawner import Spawner
from floating_platform import FloatingPlatform
from settings import WIDTH
from entity import Entity

class PlatformSpawnManager(Entity):
    def __init__(self, player1, player2):
        super().__init__(0, 0, 0, 0)
        self.player1 = player1
        self.player2 = player2
        self.max_height = 0
        self.can_add_platforms = True
        self.spawner = Spawner()
        self.platform_left = FloatingPlatform(0, WIDTH / 2 - 150, -40)
        self.platform_right = FloatingPlatform(WIDTH / 2, WIDTH - 150, -40)
    
    def update(self, game):
        # update the max height reached by the players
        if max(self.player1.dist_from_ground, self.player2.dist_from_ground) > self.max_height:
            self.max_height = max(self.player1.dist_from_ground, self.player2.dist_from_ground)
        
        # when the maximum height of the players increases by more than 90 add a new platform
        if self.can_add_platforms and self.max_height % 100 >= 90:
            # create a platform on a random x position of the left and right sides of the screen
            game.entities.append(self.spawner.spawn_platform(self.platform_left))
            game.entities.append(self.spawner.spawn_platform(self.platform_right))
            self.can_add_platforms = False
        elif self.max_height % 100 < 90:
            self.can_add_platforms = True

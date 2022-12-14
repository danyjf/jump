import pygame

class Game:
    def __init__(self, width, height):
        self.display = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

        self.running = True
        self.game_objects = []
    
    def loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.update()
            
            self.render()
            
            self.clock.tick(15)

    def update(self):
        for obj in self.game_objects:
            obj.update()
    
    def render(self):
        self.display.fill("white")
        
        for obj in self.game_objects:
            obj.render(self.display)
        
        pygame.display.flip()

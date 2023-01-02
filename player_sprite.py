import pygame

class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.idle_image = pygame.image.load("mariostand.png").convert_alpha()
        self.idle_image = pygame.transform.scale(self.idle_image, (32,32))
        self.walk_image = pygame.image.load("mariostand.png").convert_alpha()
        self.walk_image = pygame.transform.scale(self.walk_image, (32,32))
        self.jump_image = pygame.image.load("mariojump_r.png").convert_alpha()
        self.jump_image = pygame.transform.scale(self.jump_image, (32,32))
        self.fall_image = pygame.image.load("mariojump_r.png").convert_alpha()
        self.fall_image = pygame.transform.scale(self.jump_image, (32,32))
        self.display_image = None
        self.flip_image = False

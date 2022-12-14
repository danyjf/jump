import pygame

from game import Game

if __name__ == "__main__":
    pygame.init()
    
    game = Game(width=500, height=500)
    game.loop()
    
    pygame.quit()

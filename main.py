import pygame

from game import Game

if __name__ == "__main__":
    pygame.init()
    
    game = Game(width=1024, height=576)
    game.loop()
    
    pygame.quit()

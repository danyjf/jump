import pygame

from observer import Observer
from events import EVENT_DEATH
from settings import WIDTH, HEIGHT

class WinScreen(Observer):
    def __init__(self, player1, player2):
        self.player1 = player1
        player1.add_observer(self)
        self.player2 = player2
        player2.add_observer(self)
        self.is_active = False
        self.win_screen_text = WinScreenText()
        self.winner = None
    
    def render(self, display):
        if self.is_active:
            display.blit(self.win_screen_text.text, self.win_screen_text.text_rect)
    
    def on_notify(self, entity, event):
        if event == EVENT_DEATH and not self.is_active:
            if entity == self.player1:
                self.winner = self.player2
            else:
                self.winner = self.player1
            
            self.win_screen_text.setup(self.winner.name)
            
            self.is_active = True

class WinScreenText:
    def __init__(self):
        self.font = pygame.font.Font('./assets/fonts/Figerona-VF.ttf', 50)
        self.text = None
        self.text_rect = None
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
    
    def setup(self, winner_name):
        display_text = f'{winner_name} Wins!'
        self.text = self.font.render(display_text, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.x, self.y)

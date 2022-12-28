import pygame

from observer import Observer

class ScoreBoard(Observer):
    def __init__(self, player1, player2):
        self.scores = {player1.name: '', player2.name: ''}
        player1.add_observer(self)
        player2.add_observer(self)
        self.scoreboard_text = ScoreBoardText(self.scores)

    def render(self, display):
        for player_name in self.score_board_text.text:
            display.blit(self.score_board_text.text[player_name], self.score_board_text.text_rect[player_name])
    
    def on_notify(self, entity, event):
        # if event == Environment.EAT:
        #     self.scores[entity.name] += 1
        #     self.score_board_text.update_scores(self.scores)
        print('here')

class ScoreBoardText:
    def __init__(self, scores):
        self.font = pygame.font.Font('./assets/fonts/Figerona-VF.ttf', 20)
        self.display_text = {}
        self.text = {}
        self.text_rect = {}
        self.x = 50
        self.y = 20
        
        for player_name in scores:
            self.display_text[player_name] = f'{player_name}: {scores[player_name]}'
            self.text[player_name] = self.font.render(self.display_text[player_name], True, (0, 0, 0))
            self.text_rect[player_name] = self.text[player_name].get_rect()
            self.text_rect[player_name].center = (self.x, self.y)
            self.y += 30
    
    def update_scores(self, scores):
        self.display_text = {}
        for player_name in scores:
            self.display_text[player_name] = f'{player_name}: {scores[player_name]}'
            self.text[player_name] = self.font.render(self.display_text[player_name], True, (0, 0, 0))

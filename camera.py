from background import Background

class Camera:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.following_player = self.player1
        self.previous_y = self.following_player.rect.y + self.following_player.rect.x +220
    
    def update(self, entities):
        if self.player1.rect.y < self.player2.rect.y:
            self.following_player = self.player1
        elif self.player1.rect.y > self.player2.rect.y:
            self.following_player = self.player2
        
        diff_y = self.following_player.rect.y - self.previous_y
        for entity in entities:
            if not isinstance(entity, Background):
                entity.rect.y -= diff_y

        self.previous_y = self.following_player.rect.y

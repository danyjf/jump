class Camera:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.following_player = self.player1
        self.y_offset = self.following_player.rect.y - 256
    
    def update(self, entities):
        if self.player1.rect.y < self.player2.rect.y:
            self.following_player = self.player1
        elif self.player1.rect.y > self.player2.rect.y:
            self.following_player = self.player2
        
        diff_y = self.following_player.rect.y - self.y_offset
        for entity in entities:
            entity.rect.y -= diff_y

import pygame

class Goal(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('Ino_game_asssets/rocket/rocket.png')
        self.rect = self.image.get_rect(topleft= pos)

    def on_player_reach(self):

        #TODO Level complete
        print("Уровень пройден")



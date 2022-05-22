import pygame
from support import import_folder

class Goal(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('Ino_game_asssets/rocket/rocket.png')
        self.rect = self.image.get_rect(topleft= pos)
        self.anim = []
        self.frame_speed = 1 / 32
        self.frame_index = 0

    def on_player_reach(self,player):

        #TODO Level complete
        print("Уровень пройден")

        player.kill()

        self.anim = import_folder("Ino_game_asssets/rocket/anim/start")
        self.update = self.start_rocket

    def start_rocket(self):


        if self.frame_index >= len(self.anim):
            print('ЗАКОНЧИЛИ')
            self.update = self.launch_rocket
        else:
            self.image = self.anim[int(self.frame_index)]
            self.frame_index += self.frame_speed

    def launch_rocket(self):
        self.rect.y -= 5

        if self.rect.y < 0:
            print("Можно грузить следующий уровень")
            return True

    def update(self):
        pass



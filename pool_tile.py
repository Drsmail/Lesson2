import pygame
from tiles import Static_tile

class Pool_tile(Static_tile):

    def __init__(self, pos, img, is_green):

        super().__init__(pos,img)
        self.is_green = is_green



    def on_player_colade(self, player):

        if self.is_green == player.is_green:
            print('Игрок на луже своего цвета!')
            return

        print('Игрок убит лужей другого цвета!')
        player.recive_demage(5)



    def update():
        pass
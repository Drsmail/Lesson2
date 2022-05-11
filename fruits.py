import pygame
from tiles import Static_tile


class Fruit(Static_tile):


    def __init__(self, pos, img):
        super().__init__(pos, img)


    def on_player_colade(self):

        print('Игрок собрал фрукт!')
        self.collected()

    def collected(self):

        self.kill()

    def animate(self):
        super().update()

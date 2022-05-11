import pygame
from tiles import Dinamyc_tile
from enum import Enum, IntFlag
from support import import_folder


class Pool_tile(Dinamyc_tile):
    class PoolTypes(IntFlag):
        LEFT = True
        RIGHT = False
        GREEN = True
        RED = False

    pt = PoolTypes
    anim_dict = {(pt.GREEN, pt.LEFT): [],
                 (pt.GREEN, pt.RIGHT): [],
                 (pt.RED, pt.LEFT): [],
                 (pt.RED, pt.RIGHT): []}

    def __init__(self, pos, is_green, is_left):
        anim = self.anim_dict[is_green, is_left]
        super().__init__(pos, anim, frame_speed = 1/10)
        self.is_green = is_green

    @staticmethod
    def load_assets():

        pt = Pool_tile.PoolTypes

        Pool_tile.anim_dict = {(pt.GREEN, pt.LEFT): import_folder("Ino_game_asssets/pools/anims/green_left"),
                          (pt.GREEN, pt.RIGHT): import_folder("Ino_game_asssets/pools/anims/green_right"),
                          (pt.RED, pt.LEFT): import_folder("Ino_game_asssets/pools/anims/red_left"),
                          (pt.RED, pt.RIGHT): import_folder("Ino_game_asssets/pools/anims/red_right")}

    def on_player_colade(self, player):
        if self.is_green == player.is_green:
            print('Игрок на луже своего цвета!')
            return

        print('Игрок убит лужей другого цвета!')
        player.recive_demage(5)

    def animate(self):
        super().update()

import pygame
from level import Level
import json
from support import get_all_levels

class Game():

    def __init__(self,screen):

        self.final_score = 0
        self.level_score = 0
        self.GameIsRuning = True
        self.screen = screen

    def __del__(self):
        return


        #load first level

        levels_path = "Ino_game_asssets/Levels/JSON_LEVELS"
        self.Levels = get_all_levels(levels_path)

        self.curent_level_index = 1
        self.current_level = Level(self.Levels[self.curent_level_index][0], self.Levels[self.curent_level_index][1], screen)
        self.current_level.load()
        self.levelCompete = False

    def runGame(self):

        self.levelCompete = self.current_level.run()

        if (self.levelCompete == True):
            self.curent_level_index += 1
            self.current_level = Level(self.Levels[self.curent_level_index][0], self.Levels[self.curent_level_index][1], self.screen)
            self.current_level.load()

            if (self.curent_level_index == len(self.Levels)):
                print("Вы прошли игру")



        print("Готов сменить уровень")







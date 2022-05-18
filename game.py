import pygame
from level import Level
import json

class Game():

    def __init__(self,screen):

        self.final_score = 0
        self.level_score = 0
        self.GameIsRuning = True
        self.screen = screen

        #load first level
        self.first_level_path = "Ino_game_asssets/Levels"

        with open("Ino_game_asssets/Levels/level_0.tmj", "r") as level_row:
            level_data = json.load(level_row)

        self.current_level = Level(level_data, self.first_level_path, screen)
        self.current_level.load()

    def runGame(self):

        self.current_level.run()





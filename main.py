import pygame
import sys
import json

import global_settings
from global_settings import *
from level import Level

FPS = 60
size = screen_width, screen_height
screen = pygame.display.set_mode(size)
pygame.display.set_caption("инопланетянины")

clock = pygame.time.Clock()



#a = MyTiles( (200,200),tile_size)

level_path = "Ino_game_asssets/Levels"
with open("Ino_game_asssets/Levels/level_0.tmj", "r") as level_row:
    level_data = json.load(level_row)


print(level_data)
lvl1 = Level(level_data, level_path, screen)

lvl1.load()

while global_settings.GameIsRuning:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Игра закрылась!")
            sys.exit()


    clock.tick(FPS)
    screen.fill((0,0,255))

    lvl1.run()

    #screen.blit(ino.image,ino.rect)

    pygame.display.update()

sys.exit()
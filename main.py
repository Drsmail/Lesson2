import pygame
import sys

import global_settings
from global_settings import *
from level import Level

FPS = 60
size = screen_width, screen_height
screen = pygame.display.set_mode(size)
pygame.display.set_caption("инопланетянины")

clock = pygame.time.Clock()


#a = MyTiles( (200,200),tile_size)
lvl1 = Level(level_map, screen)

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
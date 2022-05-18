import pygame
import sys
from global_settings import *
from game import Game

FPS = 60
size = screen_width, screen_height
screen = pygame.display.set_mode(size)
pygame.display.set_caption("инопланетянины")
pygame.font.init()
pygame.mixer.init()

clock = pygame.time.Clock()

inoGame = Game(screen)


while inoGame.GameIsRuning:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Игра закрылась!")
            sys.exit()

    clock.tick(FPS)
    screen.fill((0,0,255))

    inoGame.runGame()
    pygame.display.update()

sys.exit()
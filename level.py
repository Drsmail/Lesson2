import pygame

from tiles import MyTiles
from player import Player
from global_settings import  tile_size

class Level():

    def __init__(self, map, screen):

        self.GlobalPlayer = None
        self.map = map
        self.tiles_groop = pygame.sprite.Group()
        self.player_groop = pygame.sprite.Group()
        self.screen = screen

    def load(self):

        for row_index, row in enumerate(self.map):
            #print(f"Строка: {row} А её номер {row_index}")
            for col_index, cell in enumerate(row):
                # print(f" Ячейка: {cell} а её номер {col_index}")
                # print(f" В ячейке (y,x): {row_index,col_index} находится  {cell}")
                y = row_index * tile_size
                x = col_index * tile_size
                if (cell == 'X'):
                    temp = MyTiles((x, y), tile_size)
                    self.tiles_groop.add(temp)
                elif (cell == 'P'):
                    temp = Player((x,y))
                    self.GlobalPlayer = temp
                    self.player_groop.add(temp)

    def horizontal_movement_collision(self):

        #player = self.player_groop.sprite

        player = self.GlobalPlayer
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles_groop.sprites():
            if sprite.rect.colliderect(player.rect):

                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):

        #player = self.player_groop.sprite
        player = self.GlobalPlayer
        player.apply_grav()

        for sprite in self.tiles_groop.sprites():
            if sprite.rect.colliderect(player.rect):

                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True

                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def run(self):

        self.player_groop.update()

        self.horizontal_movement_collision()
        self.vertical_movement_collision()

        self.player_groop.draw(self.screen)
        self.tiles_groop.draw(self.screen)

import pygame

from tiles import MyTiles
from pool_tile import Pool_tile
from player import Player
from global_settings import tile_size
from button import Button
from door import Door


class Level():

    def __init__(self, map, screen):

        self.GlobalPlayer = None
        self.map = map
        self.tiles_groop = pygame.sprite.Group()
        self.pool_groop = pygame.sprite.Group()
        self.player_groop = pygame.sprite.Group()
        self.screen = screen

        self.button_groop = pygame.sprite.Group()
        self.button_groop.add(Button((400, 400), 3))
        self.button_groop.add(Button((400, 200), 3))

        self.door_groop = pygame.sprite.Group()
        d = Door((8*64, 6*64), 3)
        self.door_groop.add(d)
        self.tiles_groop.add(d)

    def load(self):

        for row_index, row in enumerate(self.map):
            # print(f"Строка: {row} А её номер {row_index}")
            for col_index, cell in enumerate(row):
                # print(f" Ячейка: {cell} а её номер {col_index}")
                # print(f" В ячейке (y,x): {row_index,col_index} находится  {cell}")
                y = row_index * tile_size
                x = col_index * tile_size
                if (cell == 'X'):
                    temp = MyTiles((x, y), tile_size)
                    self.tiles_groop.add(temp)
                elif (cell == 'P'):
                    temp = Player((x, y))
                    self.GlobalPlayer = temp
                    self.player_groop.add(temp)
                elif cell in ['(', ')', '[', ']']:
                    temp = Pool_tile((x, y), cell)
                    self.tiles_groop.add(temp)
                    self.pool_groop.add(temp)

    def horizontal_movement_collision(self):

        # player = self.player_groop.sprite

        player = self.GlobalPlayer
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles_groop.sprites():
            if sprite.rect.colliderect(player.rect):

                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):

        # player = self.player_groop.sprite
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

                # poison pits
                if sprite in self.pool_groop.sprites():
                    sprite.on_player_colade(player)

    def check_all_buttons(self):

        player = self.GlobalPlayer

        for sprite in self.button_groop.sprites():
            if sprite.rect.colliderect(player.rect):

                id = sprite.pressed()

                for door in self.door_groop.sprites():
                    if door.id == id:
                        door.open()
                        self.tiles_groop.remove(door)
            else:

                # TODO 2 КНОПКИ ПЕРВАЯ ОТКРЫВАЕТ ВТОРАЯ ЗАКРЫВАЕТ ПЕРВУЮ ИСПРАВИТЬ!

                id = sprite.not_active()

                for door in self.door_groop.sprites():
                    if door.id == id:
                        door.close()
                        self.tiles_groop.add(door)


    def run(self):

        self.player_groop.update()

        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.check_all_buttons()

        print(len(self.tiles_groop))

        self.player_groop.draw(self.screen)
        self.tiles_groop.draw(self.screen)
        self.pool_groop.draw(self.screen)
        self.button_groop.draw(self.screen)
        self.door_groop.draw(self.screen)

import pygame

import tiles

import xml.dom.minidom

from pool_tile import Pool_tile
from player import Player
from goal import Goal
from fruits import Fruit
from global_settings import tile_size
from ui import UI
from button import Button
from door import Door


class Level():

    def __init__(self, json_data, json_path, screen):

        self.UserInterface = UI(screen)
        self.level_score = 0

        self.json_data = json_data
        self.json_path = json_path
        self.screen = screen

        self.GlobalPlayer = None
        self.GlobalGoal = None

        self.tiles_groop = pygame.sprite.Group()
        self.pool_groop = pygame.sprite.Group()
        self.player_groop = pygame.sprite.Group()
        self.Goal_groop = pygame.sprite.Group()
        self.door_groop = pygame.sprite.Group()
        self.button_groop = pygame.sprite.Group()
        self.fruits_groop = pygame.sprite.Group()

        self.load_assets()

    def load_assets(self):
        Pool_tile.load_assets()

    def load(self):

        # load all images

        All_imges = []
        All_imges.append(pygame.Surface((64, 64)))

        for tileset in self.json_data['tilesets']:
            path = tileset['source']
            path = self.json_path + '/' + path
            domtree = xml.dom.minidom.parse(path)
            group = domtree.documentElement
            images = group.getElementsByTagName('image')
            print(f"New tilset {path} with imgs:")
            for image in images:
                print(f"-- Tileset {image.getAttribute('source')}--")
                img_path = path + '/..' + '/' + image.getAttribute('source')
                All_imges.append(pygame.image.load(img_path))
                # image.getElementsByTagName('')

        print(self.json_data['layers'])

        col = self.json_data['layers'][0]['width']  # x
        str = self.json_data['layers'][0]['height']  # y

        for layer in self.json_data['layers']:
            print(layer['name'])
            # print(layer['data'])
            if layer['type'] == "tilelayer":
                for index, cell in enumerate(layer['data']):

                    if cell == 0:
                        continue

                    x = (index % col) * tile_size
                    y = (index // col) * tile_size

                    if layer['name'] == 'Terrain':
                        img = All_imges[cell]
                        temp = tiles.Static_tile((x, y), img)
                        self.tiles_groop.add(temp)

                    elif layer['name'] == 'Pools':

                        green = False
                        left = False
                        img = All_imges[cell]
                        if img.get_at((45, 5))[1] == 164:
                            green = True
                        if img.get_at((10, 15)) == (182, 154, 94):
                            left = True
                        temp = Pool_tile((x, y), green, left)
                        self.tiles_groop.add(temp)
                        self.pool_groop.add(temp)

                    elif layer['name'] == 'Fruits':
                        img = All_imges[cell]
                        temp = Fruit((x, y), img)
                        self.fruits_groop.add(temp)

                    elif layer['name'] == 'Player':
                        temp = Player((x, y))
                        self.GlobalPlayer = temp
                        self.player_groop.add(temp)

                    elif layer['name'] == 'Rocket':
                        temp = Goal((x, y))
                        self.GlobalGoal = temp
                        self.Goal_groop.add(temp)

            elif layer['type'] == 'objectgroup':

                if layer['name'] == 'Doors':
                    for obj in layer['objects']:
                        img_id = obj['gid']
                        for prop in obj['properties']:
                            if prop['name'] == 'id':
                                id = prop['value']
                        x = obj['x']
                        y = obj['y'] - 64
                        pos = (x,y)
                        Temp = Door(pos,id)
                        self.door_groop.add(Temp)

                if layer['name'] == 'Buttons':
                    for obj in layer['objects']:
                        img_id = obj['gid']
                        for prop in obj['properties']:
                            if prop['name'] == 'id':
                                id = prop['value']
                        x = obj['x']
                        y = obj['y'] - 64
                        pos = (x,y)
                        Temp = Button(pos,id)
                        self.button_groop.add(Temp)



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

        if len(self.button_groop.sprites()) == 0:
            return -1

        player = self.GlobalPlayer

        for sprite in self.button_groop.sprites():
            if sprite.rect.colliderect(player.rect):

                button_id = sprite.id

                for door in self.door_groop.sprites():
                    if door.id == button_id:
                        sprite.activate(door)
            else:

                button_id = sprite.id

                for door in self.door_groop.sprites():
                    if door.id == button_id:
                        sprite.deactivate(door)

    def check_all_fuits(self):

        if len(self.fruits_groop.sprites()) == 0:
            return -1

        player = self.GlobalPlayer

        for sprite in self.fruits_groop.sprites():
            if sprite.rect.colliderect(player.rect):
                sprite.on_player_colade()
                self.level_score += 1

    def chek_goal_reach(self):

        if self.GlobalGoal == None:
            print("А как так без ракеты?")
            return -1

        player = self.GlobalPlayer

        if self.GlobalGoal.rect.colliderect(player.rect):
            self.GlobalGoal.on_player_reach(player)
            #print("Уровень пройден")

    def run(self):

        self.player_groop.update()

        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.check_all_buttons()
        self.check_all_fuits()
        self.chek_goal_reach()

        self.player_groop.draw(self.screen)
        self.tiles_groop.draw(self.screen)
        self.pool_groop.draw(self.screen)
        self.button_groop.draw(self.screen)
        self.door_groop.draw(self.screen)
        self.fruits_groop.draw(self.screen)
        self.Goal_groop.draw(self.screen)

        self.UserInterface.draw_health(self.GlobalPlayer.health, 100)
        self.UserInterface.draw_fruits(self.level_score)

        self.pool_groop.update()
        level_end = self.GlobalGoal.update()

        if level_end is None:
            return False
        else:
            return level_end

import pygame

class Pool_tile(pygame.sprite.Sprite):

    def __init__(self, pos, type):

        super().__init__()

        self.is_left = None
        self.is_green = None

        if type == '(':
            self.is_left = True
            self.is_green = True
        if type == ')':
            self.is_left = False
            self.is_green = True
        if type == '[':
            self.is_left = True
            self.is_green = False
        if type == ']':
            self.is_left = False
            self.is_green = False

        if (self.is_green == None or self.is_left == None):
            return -1

        if self.is_left == True:
            if self.is_green == True:
                self.image = pygame.image.load('assets/mapTiles/квадратиксзеленойлужей1.png')
            else:
                self.image = pygame.image.load('assets/mapTiles/квадратикскраснойлужей1.png')
        else:
            if self.is_green == True:
                self.image = pygame.image.load('assets/mapTiles/квадратиксзеленойлужей2.png')
            else:
                self.image = pygame.image.load('assets/mapTiles/квадратикскраснойлужей2.png')

        self.rect = self.image.get_rect(topleft = pos)


    def on_player_colade(self, player):

        if self.is_green == player.is_green:
            print('Игрок на луже своего цвета!')
            return

        print('Игрок убит лужей другого цвета!')
        player.recive_demage(5)



    def update():
        pass
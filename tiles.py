import pygame

class MyTiles(pygame.sprite.Sprite):

    def __init__(self, pos, size):

        super().__init__()

        #self.image = pygame.Surface((size,size))
        #self.image.fill((200,162,200))
        self.image = pygame.image.load('assets/mapTiles/квадратик.png')
        self.rect = self.image.get_rect(topleft = pos)

    def update():
        pass
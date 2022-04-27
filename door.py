import pygame


class Door(pygame.sprite.Sprite):

    def __init__(self, pos, id):
        super().__init__()

        self.image = pygame.Surface((64,64))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(topleft=pos)
        self.id = id
        self.is_closed = True

    def close(self):
        if self.is_closed == False:
            self.is_closed = True
            self.image.fill((255,0,0))

    def open(self):
        if self.is_closed == True:
            self.is_closed = False
            self.image.fill((0,255,0))

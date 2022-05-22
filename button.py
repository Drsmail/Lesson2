import pygame
from door import Door


class Button(pygame.sprite.Sprite):

    def __init__(self, pos, id):
        super().__init__()

        self.image = pygame.Surface((32,32))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(topleft=pos)
        self.id = id
        self.is_active_now = False
        self.is_active_prev = False

    def activate(self, door:Door):
        self.is_active_now = True

        if self.is_active_now == self.is_active_prev:
            pass
        else:
            self.is_active_prev = True
            self.image.fill((0, 255, 0))
            door.open()

    def deactivate(self, door: Door):
        self.is_active_now = False

        if self.is_active_now == self.is_active_prev:
            pass
        else:
            self.is_active_prev = False
            #self.image.fill((255, 0, 0))
            #door.close()


import pygame


class Button(pygame.sprite.Sprite):

    def __init__(self, pos, id):
        super().__init__()

        self.image = pygame.Surface((32,32))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(topleft=pos)
        self.id = id
        self.is_active = False

    def pressed(self):
        self.image.fill((0, 255, 0))
        self.is_active = True
        return self.id

    def not_active(self):

        if self.is_active == False:
            return self.id

        self.image.fill((255, 0, 0))
        return self.id

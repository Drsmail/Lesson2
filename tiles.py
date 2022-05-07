import pygame

class base_tile(pygame.sprite.Sprite):

    def __init__(self, pos, size):

        super().__init__()

        self.image = pygame.Surface((64,64))
        self.image.fill((200,162,200))
        self.rect = self.image.get_rect(topleft = pos)



    def update(self):
        pass

class Static_tile(base_tile):

        def __init__(self, pos, img):

            size = (64,64) #TODO

            super().__init__(pos,size)

            self.image = img

        def update(self):
            pass


class Dinamyc_tile(base_tile):

    def __init__(self, pos, img):
        size = (64, 64)  # TODO

        super().__init__(pos, size)

        self.anim = img
        self.image = img[0]
        self.current_image = 0

    def update(self):

        self.image = self.anim[self.current_image]
        self.current_image = (self.current_image + 1) % len(self.anim)

        pass
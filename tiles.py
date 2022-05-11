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

    def __init__(self, pos, imgs, frame_speed):
        size = (64, 64)  # TODO

        super().__init__(pos, size)

        self.anim = imgs
        self.image = imgs[0]
        self.frame_index = 0
        self.frame_speed = frame_speed

    def update(self):

        self.image = self.anim[int(self.frame_index)]
        self.frame_index = (self.frame_index + self.frame_speed)
        self.frame_index = self.frame_index % len(self.anim)

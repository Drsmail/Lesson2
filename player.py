import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32,64))
        self.image.fill("green")
        self.rect = self.image.get_rect(topleft=pos)


        # player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -15

    def get_input(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_UP]:
            self.jump()
        else:
            self.direction.x = 0

        # if keys[pygame.K_DOWN]:
        #     self.direction.y = 1


    def apply_grav(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed


    def update(self):

        self.get_input()



import pygame
from  support import import_folder

class Player(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('anim/walk/1.png')
        # self.image.fill("green")
        self.rect = self.image.get_rect(topleft=pos)


        # player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -15

        #player anim
        self.frame_index = 0
        self.animation_speed = 0.25
        self.status = 'stand'
        self.import_hero_assets()



    def import_hero_assets(self):
        path_to_anim = "C:/Users/Dr_smail/PycharmProjects/Lesson2/anim/"

        self.animations = {'walk': [], 'jump': [], 'death': []}

        for anim in self.animations.keys():
            full_path = path_to_anim + '/' + anim
            self.animations[anim] = import_folder(full_path)

    def get_status(self):
        if self.direction.y < 0:
            self.status ='jump'
        elif self.direction.y > 0:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'walk'
            else:
                self.status = 'stand'

    def get_input(self):

        keys = pygame.key.get_pressed()

        # TODO Нельзя идти вправо и однавременно прыг

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

    def animate(self):

        status = self.status

        if status in self.animations.keys():
            animation = self.animations[status]
        else:
            return

        self.frame_index += self.animation_speed
        if self.frame_index > len(animation) - 1:
            self.frame_index = 0

        print(f'frame_index {self.frame_index}')
        print(f'status {self.status}')

        self.image = animation[int(self.frame_index)]



    def update(self):

        self.get_input()
        self.get_status()
        self.animate()



from os import walk
import pygame

def import_folder(path):

    surf_list = []

    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surf_list.append(image_surf)

    return surf_list

#path = "C:/Users/Dr_smail/PycharmProjects/Lesson2/anim/walk"
#a = import_folder(path)
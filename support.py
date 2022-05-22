from os import walk
import pygame
import json

def import_folder(path):

    surf_list = []

    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surf_list.append(image_surf)

    return surf_list


def get_tiles_images(name):
    surf_list = []

    path = "" #TODO

    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surf_list.append(image_surf)

def get_all_levels(path):

    Levels = []

    for _,__,levles_name in walk(path):
        for lvl in levles_name:
            full_path = path + '/' + lvl

            with open(full_path, "r") as level_row:
                level_data = json.load(level_row)

            Levels.append((level_data, path + '/..'))

    return Levels



#path = "C:/Users/Dr_smail/PycharmProjects/Lesson2/anim/walk"
#a = import_folder(path)
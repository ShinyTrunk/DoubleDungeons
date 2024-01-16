import os
import sys
import pygame
from settings import TILE_IMAGES
from functions import load_image
from creatures import *

#all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
#box_group = pygame.sprite.Group()
#player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
enemy_list = []
player = None

class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = TILE_IMAGES[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Box(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites, box_group)
        self.image = TILE_IMAGES[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


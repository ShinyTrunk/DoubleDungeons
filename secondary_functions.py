import pygame
import os
import sys

import pytmx

from settings import TILE_WIDTH, TILE_HEIGHT
from surface_to_sprite_transformer import Card
from sprite_groups import walls_group


def load_image(name):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходиМ
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def terminate():
    pygame.quit()
    sys.exit()


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def set_tiled_map(filename):
    filename = f"data/map/{filename}.tmx"
    game_map = pytmx.load_pygame(filename)
    for layer in game_map.visible_layers:
        for x, y, gid, in layer:
            tile = game_map.get_tile_image_by_gid(gid)
            if tile is not None:
                if layer.name == "Walls":
                    Card(tile, x * TILE_WIDTH, y * TILE_HEIGHT, walls_group)
                else:
                    Card(tile, x * TILE_WIDTH, y * TILE_HEIGHT)

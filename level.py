import os
import sys
import pygame
from creatures import *

#all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
#box_group = pygame.sprite.Group()
#player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
enemy_list = []
player = None

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходи
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Box(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites, box_group)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


def terminate():
    pygame.quit()
    sys.exit()


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


tile_images = {
    'wall': load_image('wood.png'),
    'empty': load_image('dessert_floor_2.png')
}
# player_image = load_image('knight.png')
enemy1_image = load_image('broomstickman.png')
tile_width = tile_height = 50


def generate_level(level):
    new_player, x, y = None, None, None
    px, py = None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Box('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                px, py = x, y
            elif level[y][x] == '!':
                Tile('empty', x, y)
                enemy_list.append([x, y])
    for i in range(len(enemy_list)):
        if i % 2 == 0:
            enemy_group.add(Enemy(enemy_list[i][0], enemy_list[i][1], load_image("Thief_anim4.png"), 8, 5, 120, 80, 0, 8))
        if i % 2 != 0:
            enemy_group.add(Enemy(enemy_list[i][0], enemy_list[i][1], load_image("Anomaly_anim.png"), 7, 5, 120, 80, 0, 6))
    new_player = Player(px, py, load_image("Knight_anin — copy.png"), 14, 7, 120, 80, 0, 7)
    player_group.add(new_player)
    return new_player, x, y
import pygame
import os
import sys
from creatures import *


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходи
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
            enemy_group.add(
                Enemy(enemy_list[i][0], enemy_list[i][1], load_image("Thief_anim4.png"), 8, 5, 120, 80, 0, 8))
        if i % 2 != 0:
            enemy_group.add(
                Enemy(enemy_list[i][0], enemy_list[i][1], load_image("Anomaly_anim.png"), 7, 5, 120, 80, 0, 6))
    new_player = Player(px, py, load_image("Knight_anin — copy.png"), 14, 7, 120, 80, 0, 7)
    player_group.add(new_player)
    return new_player, x, y

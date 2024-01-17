import os
import sys
import pygame
from creatures import *
from settings import SIZE

screen = pygame.display.set_mode(SIZE)


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, animation, length):
        super().__init__(all_sprites)
        self.frames = []
        self.animation = animation
        self.length = length
        self.cut_sheet(sheet, columns, rows, self.animation, self.length)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows, animation, length):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for i in range(length):
            frame_location = (self.rect.w * i, self.rect.h * animation)
            self.frames.append(sheet.subsurface(pygame.Rect(
                frame_location, self.rect.size)))

    def update_anim(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


class Player(AnimatedSprite):
    def __init__(self, pos_x, pos_y, sheet, columns, rows, x, y, animation, length):
        super().__init__(sheet, columns, rows, x, y, animation, length)
        # self.image = player_imag
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 5, tile_height * pos_y + 5)

    def update(self, *args, **kwargs):
        if args:
            if args[0] == pygame.K_UP:
                player_group.sprites()[0].animation = 1
                for i in range(10):
                    self.rect = self.rect.move(0, -5)
            if args[0] == pygame.K_DOWN:
                self.rect = self.rect.move(0, 50)
            if args[0] == pygame.K_LEFT:
                self.rect = self.rect.move(-50, 0)
            if args[0] == pygame.K_RIGHT:
                self.rect = self.rect.move(50, 0)
        if pygame.sprite.spritecollide(self, box_group, False):
            if args[0] == pygame.K_UP:
                self.rect = self.rect.move(0, 50)
            if args[0] == pygame.K_DOWN:
                self.rect = self.rect.move(0, -50)
            if args[0] == pygame.K_LEFT:
                self.rect = self.rect.move(50, 0)
            if args[0] == pygame.K_RIGHT:
                self.rect = self.rect.move(-50, 0)


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        self.floor_surf = pygame.image.load("./data/level1_map.png").convert()
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

        for sprite in all_sprites:
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)


class Enemy(AnimatedSprite):
    def __init__(self, pos_x, pos_y, sheet, columns, rows, x, y, animation, length):
        super().__init__(sheet, columns, rows, x, y, animation, length)
        # self.image = enemy1_image
        # self.first_line = first_line
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 5, tile_height * pos_y + 5)


all_sprites = YSortCameraGroup()
tiles_group = pygame.sprite.Group()
box_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
enemy_list = []
player = None


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
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
                pass
            #                Tile('empty', x, y)
            elif level[y][x] == '#':
                Box('wall', x, y)
            elif level[y][x] == '@':
                #               Tile('empty', x, y)
                px, py = x, y
            elif level[y][x] == '!':
                #               Tile('empty', x, y)
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

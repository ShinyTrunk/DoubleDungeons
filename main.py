import pygame
import sys
import os
from creatures import *
from start_screen import *
from level import *
from pytmx import pytmx
from level import screen
from settings import *

pygame.init()

# screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
enemy_list = []
player = None
# all_sprites = pygame.sprite.Group()
# tiles_group = pygame.sprite.Group()
# player_group = pygame.sprite.Group()
# box_group = pygame.sprite.Group()
# enemy_group = pygame.sprite.Group()


# def load_image(name, colorkey=None):
#    fullname = os.path.join('data', name)
#    # если файл не существует, то выходим
#    if not os.path.isfile(fullname):
#        print(f"Файл с изображением '{fullname}' не найден")
#        sys.exit()
#    image = pygame.image.load(fullname)
#    return image
#
#
# class Tile(pygame.sprite.Sprite):
#    def __init__(self, tile_type, pos_x, pos_y):
#        super().__init__(tiles_group, all_sprites)
#        self.image = tile_images[tile_type]
#        self.rect = self.image.get_rect().move(
#            tile_width * pos_x, tile_height * pos_y)
#
#
# class Box(pygame.sprite.Sprite):
#    def __init__(self, tile_type, pos_x, pos_y):
#        super().__init__(tiles_group, all_sprites, box_group)
#        self.image = tile_images[tile_type]
#        self.rect = self.image.get_rect().move(
#            tile_width * pos_x, tile_height * pos_y)


# class AnimatedSprite(pygame.sprite.Sprite):
#    def __init__(self, sheet, columns, rows, x, y, animation, length):
#        super().__init__(all_sprites)
#        self.frames = []
#        self.animation = animation
#        self.length = length
#        self.cut_sheet(sheet, columns, rows, self.animation, self.length)
#        self.cur_frame = 0
#        self.image = self.frames[self.cur_frame]
#        self.rect = self.rect.move(x, y)
#
#    def cut_sheet(self, sheet, columns, rows, animation, length):
#        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
#                                sheet.get_height() // rows)
#        for i in range(length):
#            frame_location = (self.rect.w * i, self.rect.h * animation)
#            self.frames.append(sheet.subsurface(pygame.Rect(
#                frame_location, self.rect.size)))
#
#    def update_anim(self):
#        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
#        self.image = self.frames[self.cur_frame]
#
#
## knight = AnimatedSprite(load_image("Thief_anim4.png"), 8, 5, 120, 80)
# class Enemy(AnimatedSprite):
#    def __init__(self, pos_x, pos_y, sheet, columns, rows, x, y, animation, length):
#        super().__init__(sheet, columns, rows, x, y, animation, length)
#        # self.image = enemy1_image
#        # self.first_line = first_line
#        self.rect = self.image.get_rect().move(
#            tile_width * pos_x + 5, tile_height * pos_y + 5)
#
#
# class Player(AnimatedSprite):
#    def __init__(self, pos_x, pos_y, sheet, columns, rows, x, y, animation, length):
#        super().__init__(sheet, columns, rows, x, y, animation, length)
#        # self.image = player_image
#        self.rect = self.image.get_rect().move(
#            tile_width * pos_x + 5, tile_height * pos_y + 5)
#    def update(self, *args, **kwargs):
#        if args:
#            if args[0] == pygame.K_UP:
#                player_group.sprites()[0].animation = 1
#                for i in range(10):
#                    self.rect = self.rect.move(0, -5)
#            if args[0] == pygame.K_DOWN:
#                self.rect = self.rect.move(0, 50)
#            if args[0] == pygame.K_LEFT:
#                self.rect = self.rect.move(-50, 0)
#            if args[0] == pygame.K_RIGHT:
#                self.rect = self.rect.move(50, 0)
#        if pygame.sprite.spritecollide(self, box_group, False):
#            if args[0] == pygame.K_UP:
#                self.rect = self.rect.move(0, 50)
#            if args[0] == pygame.K_DOWN:
#                self.rect = self.rect.move(0, -50)
#            if args[0] == pygame.K_LEFT:
#                self.rect = self.rect.move(50, 0)
#            if args[0] == pygame.K_RIGHT:

#                self.rect = self.rect.move(-50, 0)
#
#
# def terminate():
#    pygame.quit()
#    sys.exit()
#
#
# def start_screen():
#    intro_text = []
#
#    fon = pygame.transform.scale(load_image('startscreen_background_1.png'), (WIDTH, HEIGHT))
#    screen.blit(fon, (0, 0))
#    font = pygame.font.Font(None, 30)
#    text_coord = 50
#    for line in intro_text:
#        string_rendered = font.render(line, 1, pygame.Color('black'))
#        intro_rect = string_rendered.get_rect()
#        text_coord += 10
#        intro_rect.top = text_coord
#        intro_rect.x = 10
#        text_coord += intro_rect.height
#        screen.blit(string_rendered, intro_rect)
#    while True:
#        for event in pygame.event.get():
#            pos = pygame.mouse.get_pos()
#            if event.type == pygame.QUIT:
#                terminate()
#            elif event.type == pygame.MOUSEBUTTONDOWN and 287 < pos[0] < 498 and 402 < pos[1] < 462:
#                return  # начинаем игру
#        pygame.display.flip()
#        clock.tick(FPS)


# def load_level(filename):
#    filename = "data/" + filename
#    with open(filename, 'r') as mapFile:
#        level_map = [line.strip() for line in mapFile]
#
#    max_width = max(map(len, level_map))
#
#    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


pygame.display.set_caption('Double Dungeons')
tile_images = {
    'wall': load_image('wood.png'),
    'empty': load_image('dessert_floor_2.png')
}
# player_image = load_image('knight.png')
enemy1_image = load_image('broomstickman.png')

tile_width = tile_height = 50

# def generate_level(level):
#    new_player, x, y = None, None, None
#    px, py = None, Non
#    for y in range(len(level)):
#        for x in range(len(level[y])):
#            if level[y][x] == '.':
#                Tile('empty', x, y)
#            elif level[y][x] == '#':
#                Box('wall', x, y)
#            elif level[y][x] == '@':
#                Tile('empty', x, y)
#                px, py = x, y
#            elif level[y][x] == '!':
#                Tile('empty', x, y)
#                enemy_list.append([x, y])
#    for i in range(len(enemy_list)):
#        if i % 2 == 0:
#            enemy_group.add(Enemy(enemy_list[i][0], enemy_list[i][1], load_image("Thief_anim4.png"), 8, 5, 120, 80, 0, 8))
#        if i % 2 != 0:
#            enemy_group.add(Enemy(enemy_list[i][0], enemy_list[i][1], load_image("Anomaly_anim.png"), 7, 5, 120, 80, 0, 6))
#    new_player = Player(px, py, load_image("Knight_anin — copy.png"), 14, 7, 120, 80, 0, 7)
#    player_group.add(new_player)
#    return new_player, x, y


start_screen()
player, level_x, level_y = generate_level(load_level('map.txt'))
running = True
while running:
    clock.tick(10)
    screen.fill(BLACK)
    player_group.sprites()[0].update_anim()
    for sprite in enemy_group.sprites():
        sprite.update_anim()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            player.update(event.key)
    # player.update_anim()
    all_sprites.custom_draw(player)
    pygame.display.flip()

terminate()

import pygame
import sys
import os
from sprite_groups import all_sprites
from start_screen import *
from level import *
from pytmx import pytmx
from level import screen
from settings import *

pygame.init()


clock = pygame.time.Clock()
enemy_list = []
player = None


pygame.display.set_caption('Double Dungeons')
# tile_images = {
#     'wall': load_image('wood.png'),
#     'empty': load_image('dessert_floor_2.png')
# }
#
# enemy1_image = load_image('broomstickman.png')
#
# tile_width = tile_height = 50


start_screen()
# player, level_x, level_y = generate_level(load_level('map.txt'))
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
    all_sprites.custom_draw(player)
    pygame.display.flip()

terminate()

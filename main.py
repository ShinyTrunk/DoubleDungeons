import pygame
import sys
import os
from functions import generate_level, load_level
from start_screen import *
from level import *
from creatures import *
from pytmx import pytmx

from settings import *

pygame.init()

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
enemy_list = []
start_screen()
player, level_x, level_y = generate_level(load_level('map.txt'))
running = True
while running:

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
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

terminate()

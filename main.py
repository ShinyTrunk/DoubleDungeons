import os

import pygame.image

from camera import Camera
from death_screen import death_screen
from player_interface import show_interface
from secondary_functions import load_level, set_tiled_map, scale_image, set_music, change_level, save_progress, \
    load_progress
from sprite_groups import *
from start_screen import *
from settings import *
from level import *

pygame.init()
screen = pygame.display.set_mode(SIZE)

pygame.display.set_caption('Double Dungeons')
start_screen(screen)

set_tiled_map('level1_map_2')
player, level_x, level_y = generate_level(load_level('map/map.txt'))
player_obj = player_group.sprites()[0]
camera = Camera()
clock = pygame.time.Clock()
set_music('sound')
pl = player


def main():
    scale_image("death_Screen.png", 0.667, 0.742, "data/death_screens", "death_screen.png")
    global pl
    running = True
    while running:
        screen.fill((0, 0, 0))
        if len(enemy_group.sprites()) == 0:
            save_progress(player_obj.hp, player_obj.damage, player_obj.looted_chests, player_obj.rect.x, player_obj.rect.y)
            print(load_progress())
            print("piska")
            for sprite in all_sprites:
                sprite.remove(all_sprites)
            player_obj.remove(player_group)
            player1, level_x, level_y = generate_level(load_level('map/map.txt'))
            pl = player1
            change_level("level2_map")
            all_sprites.draw(screen)
        if player.hp <= 0:
            death_screen(screen)
        player_group.sprites()[0].update_anim()
        for sprite in enemy_group.sprites():
            sprite.update_anim()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                player.update(event.key)
                for sprite in enemy_group:
                    sprite.set_target_player(player)
                    sprite.update(event.key)
        camera.update(pl)
        for sprite in all_sprites:
            camera.apply(sprite)
        all_sprites.draw(screen)
        show_interface(screen)

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
    terminate()

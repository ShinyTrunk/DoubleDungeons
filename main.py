import os

import pygame.image

from camera import Camera
from player_interface import show_interface
from secondary_functions import load_level, set_tiled_map, scale_image
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

camera = Camera()
clock = pygame.time.Clock()


def main():
    # scale_image("thief_animated_sprite_16x16.png", 2.606, 2.606, "data/animated_sprites", "thief_animated_sprite_48x48.png")
    running = True
    while running:
        screen.fill((0, 0, 0))
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
        camera.update(player)
        for sprite in all_sprites:
            camera.apply(sprite)
        all_sprites.draw(screen)
        show_interface(screen)

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
    terminate()

import os

import pygame.image

from camera import Camera
from death_screen import death_screen
from player_interface import show_interface
from secondary_functions import load_level, set_tiled_map, scale_image, set_music, change_level, save_progress, \
    load_progress, remove_all_sprites_groups
from sprite_groups import *
from start_screen import *
from settings import *
from level import *
from flags import flags

pygame.init()
screen = pygame.display.set_mode(SIZE)

pygame.display.set_caption('Double Dungeons')

camera = Camera()
clock = pygame.time.Clock()


def game_screen(screen, level_number) -> str:
    set_tiled_map(f'level{level_number}_map')
    player, level_x, level_y = generate_level(load_level('map/map.txt'))
    while flags["game_screen"]:
        screen.fill((0, 0, 0))
        if len(enemy_group.sprites()) == 0:
            save_progress(player.hp, player.damage, player.looted_chests, player.defeated_enemies)
            return "live"
        if player.hp <= 0:
            pygame.mixer.music.stop()
            save_progress(player.hp, player.damage, player.looted_chests, player.defeated_enemies)
            flags["death_screen"] = True
            flags["game_screen"] = False
            return "death"
        player_group.sprites()[0].update_anim()
        for sprite in enemy_group.sprites():
            sprite.update_anim()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
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


def main():
    level_number = 1
    while any(flags.values()):
        remove_all_sprites_groups()
        if flags["start_screen"]:
            set_music('dark_fantasy_background_music')
            start_screen(screen)
        elif flags["game_screen"]:
            state = game_screen(screen, level_number)
            while state != "death":
                remove_all_sprites_groups()
                level_number += 1
                state = game_screen(screen, level_number)
        elif flags["death_screen"]:
            death_screen(screen)


if __name__ == "__main__":
    main()
    terminate()

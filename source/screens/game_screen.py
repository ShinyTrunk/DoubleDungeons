import pygame

from source.functions.load_level import load_level
from source.functions.save_progress import save_progress
from source.functions.set_tiled_map import set_tiled_map
from source.functions.terminate import terminate
from source.helpers.state import flags
from source.functions.generate_level import generate_level
from source.interfaces.player_interface import show_interface
from source.helpers.settings import FPS
from source.sprites.sprite_groups.sprite_groups import player_group, enemy_group, all_sprites


def game_screen(screen, level_number, camera, clock, player_hp):
    set_tiled_map(f'level{level_number}_map')
    player, level_x, level_y = generate_level(load_level('map/map.txt'), player_hp)
    while flags["game_screen"]:
        screen.fill((0, 0, 0))
        if len(enemy_group.sprites()) == 0:
            save_progress(player.hp, player.damage, player.looted_chests, player.defeated_enemies)
            return player.hp
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


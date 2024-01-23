import pygame.image

from source.functions.remove_all_sprites_groups import remove_all_sprites_groups
from source.functions.set_music import set_music
from source.screens.good_ending_screen import good_ending_screen
from source.sprites.camera import Camera
from source.screens.death_screen import death_screen
from source.screens.game_screen import game_screen
from source.screens.start_screen import *
from source.helpers.settings import *
from source.helpers.state import state

pygame.init()

pygame.display.set_caption('Double Dungeons')


def main():
    screen = pygame.display.set_mode(SIZE)

    camera = Camera()
    clock = pygame.time.Clock()
    hp = 20

    while any(state.values()):
        good_ending_screen(screen)
        level_number = 1
        remove_all_sprites_groups()
        if state["start_screen"]:
            set_music('dark_fantasy_background_music')
            start_screen(screen)
        elif state["game_screen"]:
            hp = game_screen(screen, level_number, camera, clock, hp)
            while hp != "death":
                remove_all_sprites_groups()
                level_number += 1
                if level_number > 3:
                    state["good_ending_screen"] = True
                    state["game_screen"] = False,
                    break
                hp = game_screen(screen, level_number, camera, clock, hp)
        elif state["death_screen"]:
            death_screen(screen)
            hp = 20
        elif state["good_ending_screen"]:
            good_ending_screen(screen)


if __name__ == "__main__":
    main()
    terminate()

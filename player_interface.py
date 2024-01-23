import pygame
from sprite_groups import player_group, chests_group

pygame.font.init()
font = pygame.font.Font("data/fonts/pixel_font_main.ttf", 40)


def show_interface(screen):
    hp = int()
    looted_chests = int()
    chests_left = len(chests_group)
    for player in player_group:
        hp = player.hp
        looted_chests = player.looted_chests
    hp_text = font.render(f"hp {hp}", True, "white")
    screen.blit(hp_text, (10, 10))
    looted_chests_text = font.render(f"chests {looted_chests}", True, "white")
    screen.blit(looted_chests_text, (630, 10))

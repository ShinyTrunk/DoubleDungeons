import pygame

from source.helpers.fonts import standart_font
from source.sprites.sprite_groups.sprite_groups import player_group

pygame.font.init()


def show_interface(screen):
    hp = player_group.sprites()[-1].hp
    looted_chests = player_group.sprites()[-1].looted_chests
    hp_text = standart_font.render(f"hp {hp}", True, "white")
    screen.blit(hp_text, (10, 10))
    looted_chests_text = standart_font.render(f"chests {looted_chests}", True, "white")
    screen.blit(looted_chests_text, (600, 10))

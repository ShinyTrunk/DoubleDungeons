import pygame

from settings import WIDTH, HEIGHT
from secondary_functions import load_image, terminate, set_music, load_progress
from sprite_groups import player_group
from flags import flags
from start_screen import start_screen

pygame.font.init()
font = pygame.font.Font("data/fonts/pixel_font_main.ttf", 50)
big_font = pygame.font.Font("data/fonts/pixel_font_main.ttf", 80)


def death_screen_show_text(screen):
    looted_chests = str()
    defeated_enemies = str()
    you_died_text = big_font.render("you died", True, "white")
    looted_chests_text = font.render(f"chests looted: {load_progress()['looted_chests']}", True, "white")
    defeated_enemies_text = font.render(f"enemies defeated: {load_progress()['enemies_defeated']}", True, "white")
    button_text = font.render(f"retry", True, "white")
    screen.blit(looted_chests_text, (220, 250))
    screen.blit(defeated_enemies_text, (190, 350))
    screen.blit(you_died_text, (270, 100))
    screen.blit(button_text, (355, 445))


def death_screen(screen) -> None:
    set_music("death_screen_music")
    intro_text = []
    background = pygame.transform.scale(load_image('death_screens\\death_screen.png'), (WIDTH, HEIGHT))
    screen.blit(background, (0, 0))
    while flags["death_screen"]:
        button = pygame.rect.Rect(320, 440, 200, 75)
        pygame.draw.rect(screen, "red", button)
        death_screen_show_text(screen)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                terminate()
            if button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                flags["start_screen"] = True
                flags["death_screen"] = False
                return
        pygame.display.flip()

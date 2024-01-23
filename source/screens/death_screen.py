import pygame

from source.functions.load_image import load_image
from source.functions.load_progress import load_progress
from source.functions.set_music import set_music
from source.functions.terminate import terminate
from source.helpers.fonts import bold_font, standart_font
from source.helpers.settings import WIDTH, HEIGHT
from source.helpers.state import flags

pygame.font.init()


def death_screen_show_text(screen):
    you_died_text = bold_font.render("you died", True, "white")
    looted_chests_text = standart_font.render(f"chests looted: {load_progress()['looted_chests']}", True, "white")
    defeated_enemies_text = standart_font.render(f"enemies defeated: {load_progress()['enemies_defeated']}", True, "white")
    button_text = standart_font.render(f"retry", True, "white")
    screen.blit(looted_chests_text, (220, 250))
    screen.blit(defeated_enemies_text, (190, 350))
    screen.blit(you_died_text, (270, 100))
    screen.blit(button_text, (355, 445))


def death_screen(screen):
    set_music("death_screen_music")
    background = pygame.transform.scale(load_image('death_screens\\death_screen.png'), (WIDTH, HEIGHT))
    screen.blit(background, (0, 0))
    while flags["death_screen"]:
        button_rect = pygame.rect.Rect(320, 440, 200, 75)
        pygame.draw.rect(screen, "red", button_rect)
        death_screen_show_text(screen)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                terminate()
            if button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                flags["start_screen"] = True
                flags["death_screen"] = False
                return
        pygame.display.flip()

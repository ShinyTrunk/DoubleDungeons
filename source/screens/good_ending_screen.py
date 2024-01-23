import pygame

from source.functions.load_image import load_image
from source.functions.terminate import terminate
from source.helpers.state import state
from source.helpers.fonts import standart_font
from source.helpers.settings import WIDTH, HEIGHT


def good_ending_screen(screen):
    final_text = standart_font.render("you finally escaped the dungeon!", False, "white")
    background = pygame.transform.scale(load_image('ending_screens\\good_ending_screen.png'), (WIDTH, HEIGHT))
    button_text = standart_font.render(f"leave", True, "black")
    button_rect = pygame.rect.Rect(320, 440, 200, 75)
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, "gray", button_rect)
    screen.blit(final_text, (40, 100))
    screen.blit(button_text, (355, 445))
    while state["good_ending_screen"]:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                terminate()
            if button_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
                terminate()

        pygame.display.flip()

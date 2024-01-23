import pygame

from source.functions.load_image import load_image
from source.functions.terminate import terminate
from source.helpers.state import state
from source.helpers.fonts import standart_font
from source.helpers.settings import WIDTH, HEIGHT


def good_ending_screen(screen):
    final_text = standart_font.render("you finally finished my dungeon!", False, "white")
    background = pygame.transform.scale(load_image('ending_screens\\good_ending_screen.png'), (WIDTH, HEIGHT))
    screen.blit(background, (0, 0))
    screen.blit(final_text, (40, 100))
    while state["good_ending_screen"]:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and 287 < pos[0] < 498 and 402 < pos[1] < 462:
                return
        pygame.display.flip()

import pygame

from source.helpers.settings import WIDTH, HEIGHT
from secondary_functions import load_image, terminate


def good_ending_screen(screen):
    background = pygame.transform.scale(load_image('ending_screens\\good_ending_screen.png'), (WIDTH, HEIGHT))
    screen.blit(background, (0, 0))
    while True:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and 287 < pos[0] < 498 and 402 < pos[1] < 462:
                return
        pygame.display.flip()
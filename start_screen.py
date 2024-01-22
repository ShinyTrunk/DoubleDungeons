import pygame

import flags
from settings import WIDTH, HEIGHT
from secondary_functions import load_image, terminate


def start_screen(screen):
    intro_text = []
    background = pygame.transform.scale(load_image('startscreens\\startscreen_background_light.png'), (WIDTH, HEIGHT))
    screen.blit(background, (0, 0))
    while True:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and 287 < pos[0] < 498 and 402 < pos[1] < 462:
                flags.flag_start = False
                flags.flag_main = True
        pygame.display.flip()

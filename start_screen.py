import pygame

from settings import WIDTH, HEIGHT
from secondary_functions import load_image, terminate


def start_screen(screen):
    intro_text = []
    fon = pygame.transform.scale(load_image('startscreens\startscreen_background_light.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and 287 < pos[0] < 498 and 402 < pos[1] < 462:
                return
        pygame.display.flip()

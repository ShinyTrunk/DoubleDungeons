import pygame

from source.functions.load_image import load_image
from source.functions.terminate import terminate
from source.helpers.state import flags
from source.helpers.settings import WIDTH, HEIGHT


def start_screen(screen):
    background = pygame.transform.scale(load_image('startscreens\\startscreen_background_light.png'), (WIDTH, HEIGHT))
    button_rect = pygame.rect.Rect(308, 388, 300, 300)
    screen.blit(background, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                flags["start_screen"] = False
                flags["game_screen"] = True
                return
        pygame.display.flip()

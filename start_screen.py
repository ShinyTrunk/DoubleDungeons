import pygame

from flags import flags
from settings import WIDTH, HEIGHT
from secondary_functions import load_image, terminate


def start_screen(screen) -> None:
    intro_text = []
    background = pygame.transform.scale(load_image('startscreens\\startscreen_background_light.png'), (WIDTH, HEIGHT))
    button = pygame.rect.Rect(308, 388, 300, 300)
    screen.blit(background, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                flags["start_screen"] = False
                flags["game_screen"] = True
                return
        pygame.display.flip()

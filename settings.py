import pygame
from functions import load_image
YELLOW = pygame.Color("yellow")
RED = pygame.Color("red")
GREEN = pygame.Color("green")
BLUE = pygame.Color("blue")
BLACK = pygame.Color("black")
WHITE = pygame.Color("white")
SIZE = WIDTH, HEIGHT = (960, 960)
FPS = 10
TILE_IMAGES = {
    'wall': load_image('wood.png'),
    'empty': load_image('dessert_floor_2.png')
}
enemy1_image = load_image('broomstickman.png')
TILE_WIDTH = TILE_HEIGHT = 64
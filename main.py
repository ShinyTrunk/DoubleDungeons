import pygame
import sys
import os

from camera import Camera
from sprite_groups import *
from start_screen import *
import pytmx
#from level import screen
from settings import *
from level import *
pygame.init()
screen = pygame.display.set_mode(SIZE)

clock = pygame.time.Clock()
enemy_list = []
player = None
class Card(pygame.sprite.Sprite):
    def __init__(self, surface,x,y):
        super().__init__(all_sprites)
        self.image = surface
        self.rect = self.image.get_rect().move(x,y)


pygame.display.set_caption('Double Dungeons')
# tile_images = {
#     'wall': load_image('wood.png'),
#     'empty': load_image('dessert_floor_2.png')
# }
#
# enemy1_image = load_image('broomstickman.png')
#
# tile_width = tile_height = 50

start_screen(screen)
gameMap = pytmx.load_pygame('data/map/level1_map.tmx')
for layer in gameMap.visible_layers:
    for x, y, gid, in layer:
        tile = gameMap.get_tile_image_by_gid(gid)
        #screen.blit(tile, (x * 64,y * 64))
        Card(tile, x*64, y*64)
camera = Camera()
player, level_x, level_y = generate_level(load_level('map.txt'))
running = True
while running:
    clock.tick(10)
    player_group.sprites()[0].update_anim()
    for sprite in enemy_group.sprites():
        sprite.update_anim()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            player.update(event.key)

    camera.update(player)
    screen.fill((0, 0, 0))
        # обновляем положение всех спрайтов
    for sprite in all_sprites:
        camera.apply(sprite)
    all_sprites.draw(screen)
    pygame.display.flip()

terminate()

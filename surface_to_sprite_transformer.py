import pygame

from sprite_groups import all_sprites


class Card(pygame.sprite.Sprite):
    def __init__(self, surface, x, y):
        super().__init__(all_sprites)
        self.image = surface
        self.rect = self.image.get_rect().move(x, y)

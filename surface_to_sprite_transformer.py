import pygame

from sprite_groups import all_sprites


class Card(pygame.sprite.Sprite):
    def __init__(self, surface, x, y, sprites_group=all_sprites):
        super().__init__(all_sprites, sprites_group)
        self.image = surface
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect().move(x, y)
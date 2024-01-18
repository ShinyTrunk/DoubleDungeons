import pygame
from settings import WIDTH, HEIGHT

# class YSortCameraGroup(pygame.sprite.Group):
#     def __init__(self):
#         super().__init__()
#         self.display_surface = pygame.display.get_surface()
#         print(self.display_surface)
#         self.half_width = self.display_surface.get_size()[0] // 2
#         self.half_height = self.display_surface.get_size()[1] // 2
#         self.offset = pygame.math.Vector2()
#
#         self.floor_surf = pygame.image.load("./data/level1_map.png").convert()
#         self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))
#
#     def custom_draw(self, player):
#         self.offset.x = player.rect.centerx - self.half_width
#         self.offset.y = player.rect.centery - self.half_height
#
#         floor_offset_pos = self.floor_rect.topleft - self.offset
#         self.display_surface.blit(self.floor_surf, floor_offset_pos)
#
#         for sprite in self:
#             offset_pos = sprite.rect.topleft - self.offset
#             self.display_surface.blit(sprite.image, offset_pos)

class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - HEIGHT // 2)
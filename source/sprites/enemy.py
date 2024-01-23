import pygame

from source.helpers.settings import TILE_WIDTH, TILE_HEIGHT
from source.sprites.animated_sprite import AnimatedSprite
from source.sprites.sprite_groups.sprite_groups import walls_group, player_group


class Enemy(AnimatedSprite):
    def __init__(self, sprite_group, pos_x, pos_y, sheet, columns, rows, x, y, animation, length, damage=5):
        super().__init__(sprite_group, sheet, columns, rows, x, y, animation, length)
        self.mask = pygame.mask.from_surface(self.image)
        cropped_rect = pygame.Rect(36, 16, self.image.get_width() - 72, self.image.get_height() - 32)
        self.cropped_image = self.image.subsurface(cropped_rect)
        self.target_player = None
        self.speed = 64
        self.rect = self.cropped_image.get_rect().move(
            TILE_WIDTH * pos_x + 36, TILE_HEIGHT * pos_y + 32)
        self.hp = 8
        self.damage = damage

    def set_target_player(self, player):
        self.target_player = player

    def update(self, *args):
        if args[0] == pygame.K_UP or args[0] == pygame.K_DOWN or args[0] == pygame.K_LEFT or args[0] == pygame.K_RIGHT:
            if self.target_player:
                player_rect = self.target_player.rect
                dx = player_rect.x - self.rect.x
                dy = player_rect.y - self.rect.y

                if abs(dx) > abs(dy):
                    if dx > 0:
                        new_x = self.rect.x + self.speed
                        if not self.check_collision(new_x, self.rect.y):
                            self.rect.x = new_x
                    elif dx < 0:
                        new_x = self.rect.x - self.speed
                        if not self.check_collision(new_x, self.rect.y):
                            self.rect.x = new_x
                else:
                    if dy > 0:
                        new_y = self.rect.y + self.speed
                        if not self.check_collision(self.rect.x, new_y):
                            self.rect.y = new_y
                    elif dy < 0:
                        new_y = self.rect.y - self.speed
                        if not self.check_collision(self.rect.x, new_y):
                            self.rect.y = new_y
            for player in player_group:
                if pygame.sprite.collide_mask(self, player):
                    if args[0] == pygame.K_UP:
                        self.rect = self.rect.move(0, -64)
                    if args[0] == pygame.K_DOWN:
                        self.rect = self.rect.move(0, 64)
                    if args[0] == pygame.K_LEFT:
                        self.rect = self.rect.move(-64, 0)
                    if args[0] == pygame.K_RIGHT:
                        self.rect = self.rect.move(64, 0)

    def check_collision(self, x, y):
        temp_rect = self.rect.copy()
        temp_rect.x = x
        temp_rect.y = y
        for wall in walls_group:
            if temp_rect.colliderect(wall.rect):
                return True
        return False

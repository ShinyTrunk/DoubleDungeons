import pygame

from source.helpers.settings import TILE_WIDTH, TILE_HEIGHT
from source.sprites.animated_sprite import AnimatedSprite
from source.sprites.sprite_groups.sprite_groups import chests_group, walls_group, all_sprites, potions_group, \
    enemy_group


class Player(AnimatedSprite):

    def __init__(self, sprite_group, pos_x, pos_y, sheet, columns, rows, x, y, animation, length, hp=20, damage=5):
        super().__init__(sprite_group, sheet, columns, rows, x, y, animation, length)
        self.mask = pygame.mask.from_surface(self.image)
        cropped_rect = pygame.Rect(36, 16, self.image.get_width() - 72, self.image.get_height() - 32)
        self.cropped_image = self.image.subsurface(cropped_rect)
        self.rect = self.cropped_image.get_rect().move(
            TILE_WIDTH * pos_x + 36, TILE_HEIGHT * pos_y + 32)
        self.looted_chests = 0
        self.defeated_enemies = 0
        self.hp = hp
        self.damage = damage
        self.old_pos_x = self.rect.x
        self.old_pos_y = self.rect.y

    def update(self, *args, **kwargs):
        self.old_pos_x = self.rect.x
        self.old_pos_y = self.rect.y
        if args:
            if args[0] == pygame.K_UP:
                self.rect = self.rect.move(0, -64)
                self.old_pos_y += 64
            if args[0] == pygame.K_DOWN:
                self.rect = self.rect.move(0, 64)

                self.old_pos_y -= 64
            if args[0] == pygame.K_LEFT:
                self.rect = self.rect.move(-64, 0)
                self.old_pos_x += 64
            if args[0] == pygame.K_RIGHT:
                self.rect = self.rect.move(64, 0)
                self.old_pos_x -= 64
        for wall in walls_group:
            if pygame.sprite.collide_mask(self, wall):
                if args[0] == pygame.K_UP:
                    self.rect = self.rect.move(0, 64)
                if args[0] == pygame.K_DOWN:
                    self.rect = self.rect.move(0, -64)
                if args[0] == pygame.K_LEFT:
                    self.rect = self.rect.move(64, 0)
                if args[0] == pygame.K_RIGHT:
                    self.rect = self.rect.move(-64, 0)
        for chest in chests_group:
            if pygame.sprite.collide_mask(self, chest):
                chest.remove((chests_group, all_sprites))
                self.looted_chests += 1
                self.damage += 1
        for potion in potions_group:
            if pygame.sprite.collide_mask(self, potion):
                potion.remove((potions_group, all_sprites))
                self.hp += 5
        for enemy in enemy_group:
            if pygame.sprite.collide_rect(self, enemy):
                if enemy.hp - self.damage <= 0:
                    enemy.hp -= self.damage
                else:
                    self.hp -= enemy.damage
                    enemy.hp -= self.damage
            if self.old_pos_x == enemy.rect.x and self.old_pos_y == enemy.rect.y:
                self.hp -= enemy.damage
            if enemy.hp <= 0:
                enemy.remove((enemy_group, all_sprites))
                self.defeated_enemies += 1


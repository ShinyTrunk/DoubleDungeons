import pygame
from sprite_groups import player_group, all_sprites, walls_group, chests_group, enemy_group
from settings import TILE_WIDTH, TILE_HEIGHT, WIDTH, HEIGHT

# player = None


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_group, sheet, columns, rows, x, y, animation, length):
        super().__init__(all_sprites, sprite_group)
        self.frames = []
        self.animation = animation
        self.length = length
        self.cut_sheet(sheet, columns, rows, self.animation, self.length)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows, animation, length):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for i in range(length):
            frame_location = (self.rect.w * i, self.rect.h * animation)
            self.frames.append(sheet.subsurface(pygame.Rect(
                frame_location, self.rect.size)))

    def update_anim(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


class Enemy(AnimatedSprite):
    def __init__(self, sprite_group, pos_x, pos_y, sheet, columns, rows, x, y, animation, length):
        super().__init__(sprite_group, sheet, columns, rows, x, y, animation, length)
        self.mask = pygame.mask.from_surface(self.image)
        cropped_rect = pygame.Rect(28, 8, self.image.get_width() - 56, self.image.get_height() - 16)
        self.cropped_image = self.image.subsurface(cropped_rect)
        self.target_player = None
        self.speed = 64
        self.rect = self.cropped_image.get_rect().move(
            TILE_WIDTH * pos_x + 36, TILE_HEIGHT * pos_y + 32)
        self.hp = 8
        self.damage = 5

    def set_target_player(self, player):
        self.target_player = player

    def update(self):
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

    def check_collision(self, x, y):
        temp_rect = self.rect.copy()
        temp_rect.x = x
        temp_rect.y = y
        for wall in walls_group:
            if pygame.sprite.collide_mask(self, wall):
                return True
            return False


class Player(AnimatedSprite):

    def __init__(self, sprite_group, pos_x, pos_y, sheet, columns, rows, x, y, animation, length):
        super().__init__(sprite_group, sheet, columns, rows, x, y, animation, length)
        self.mask = pygame.mask.from_surface(self.image)
        cropped_rect = pygame.Rect(28, 8, self.image.get_width() - 56, self.image.get_height() - 16)
        self.cropped_image = self.image.subsurface(cropped_rect)
        self.rect = self.cropped_image.get_rect().move(
            TILE_WIDTH * pos_x + 36, TILE_HEIGHT * pos_y + 32)
        self.looted_chests = 0
        self.hp = 20
        self.damage = 5

    def update(self, *args, **kwargs):
        if args:
            if args[0] == pygame.K_UP:
                self.rect = self.rect.move(0, -64)
            if args[0] == pygame.K_DOWN:
                self.rect = self.rect.move(0, 64)
            if args[0] == pygame.K_LEFT:
                self.rect = self.rect.move(-64, 0)
            if args[0] == pygame.K_RIGHT:
                self.rect = self.rect.move(64, 0)
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
            # print(chests_group)
            if pygame.sprite.collide_mask(self, chest):
                chest.remove((chests_group, all_sprites))
                self.looted_chests += 1
                print(self.looted_chests)
        for enemy in enemy_group:
            if pygame.sprite.collide_rect(self, enemy):
                self.hp -= enemy.damage
                enemy.hp -= self.damage
                print(f"player_hp = {self.hp}, enemy_hp = {enemy.hp}")
            if enemy.hp <= 0:
                enemy.remove((enemy_group, all_sprites))
            if self.hp <= 0:
                print("death")
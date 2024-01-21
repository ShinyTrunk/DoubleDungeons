import pygame

from secondary_functions import change_level, load_level
from sprite_groups import player_group, all_sprites, walls_group, chests_group, enemy_group, potions_group
from settings import TILE_WIDTH, TILE_HEIGHT, WIDTH, HEIGHT


# player = None


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_group, sheet, columns, rows, x, y, animation, length):
        super().__init__(all_sprites, sprite_group)
        self.frames = []
        self.sheet = sheet
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
        cropped_rect = pygame.Rect(36, 16, self.image.get_width() - 72, self.image.get_height() - 32)
        self.cropped_image = self.image.subsurface(cropped_rect)
        self.target_player = None
        self.speed = 64
        self.rect = self.cropped_image.get_rect().move(
            TILE_WIDTH * pos_x + 36, TILE_HEIGHT * pos_y + 32)
        self.hp = 8
        self.damage = 5

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

    #    for player in player_group:
    #        print('.')
    #        if player.rect.x != self.rect.x and player.rect.y == self.rect.y:
    #            print(player.rect.x, self.rect.y)
    #            print('!')
    #            if pygame.sprite.collide_rect(self, player):
    #                player.hp -= self.damage
    #                print(f"player_hp = {player.hp}, enemy_hp = {self.hp}")
    #      if enemy.hp <= 0:
    #          enemy.remove((enemy_group, all_sprites))
    #     if self.hp <= 0:
    #         print("death")

    def check_collision(self, x, y):
        temp_rect = self.rect.copy()
        temp_rect.x = x
        temp_rect.y = y
        for wall in walls_group:
            if temp_rect.colliderect(wall.rect):
                return True
        return False


class Player(AnimatedSprite):

    def __init__(self, sprite_group, pos_x, pos_y, sheet, columns, rows, x, y, animation, length, hp=20, damage=5):
        super().__init__(sprite_group, sheet, columns, rows, x, y, animation, length)
        self.mask = pygame.mask.from_surface(self.image)
        cropped_rect = pygame.Rect(36, 16, self.image.get_width() - 72, self.image.get_height() - 32)
        self.cropped_image = self.image.subsurface(cropped_rect)
        self.rect = self.cropped_image.get_rect().move(
            TILE_WIDTH * pos_x + 36, TILE_HEIGHT * pos_y + 32)
        self.looted_chests = 0
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
            print(f"old_x = {self.old_pos_x}, new_x = {self.rect.x}")
            print(f"old_y = {self.old_pos_y}, new_y = {self.rect.y}")
            for i in enemy_group:
                print(i.rect.x, i.rect.y)
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
                print(self.looted_chests)
        for potion in potions_group:
            if pygame.sprite.collide_mask(self, potion):
                potion.remove((potions_group, all_sprites))
                self.hp += 5
                # print(self.looted_chests)
        for enemy in enemy_group:
            if pygame.sprite.collide_rect(self, enemy):
                if enemy.hp - self.damage <= 0:
                    enemy.hp -= self.damage
                else:
                    self.hp -= enemy.damage
                    enemy.hp -= self.damage
                # self.animation = 4
                # self.length = 5
                # self.frames = []
                # self.cut_sheet(self.sheet, 14, 7, 4, 5)
                # for i in range(5):
                #     self.update_anim()
                print(f"player_hp = {self.hp}, enemy_hp = {enemy.hp}")
            if self.old_pos_x == enemy.rect.x and self.old_pos_y == enemy.rect.y:
                print(self.old_pos_x, enemy.rect.x)
                print(self.old_pos_y, enemy.rect.y)
                self.hp -= enemy.damage
                print('враг сзади')
            if enemy.hp <= 0:
                enemy.remove((enemy_group, all_sprites))
            if self.hp <= 0:
                # self.remove((player_group, all_sprites))
                print("death")
                # all_sprites.sprites().clear()
                # change_level("level2_map")

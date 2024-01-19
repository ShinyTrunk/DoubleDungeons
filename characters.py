import pygame
from sprite_groups import box_group, player_group, all_sprites, walls_group
from settings import TILE_WIDTH, TILE_HEIGHT

player = None


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
        # self.image = enemy1_image
        # self.first_line = first_line
        self.rect = self.image.get_rect().move(
            TILE_WIDTH * pos_x + 5, TILE_HEIGHT * pos_y + 5)


class Player(AnimatedSprite):

    def __init__(self, sprite_group, pos_x, pos_y, sheet, columns, rows, x, y, animation, length):
        super().__init__(sprite_group, sheet, columns, rows, x, y, animation, length)
        # self.image = player_imag
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect().move(
            TILE_WIDTH * pos_x + 5, TILE_HEIGHT * pos_y + 5)

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
        for sprite in walls_group:
            if pygame.sprite.collide_mask(self, sprite):
                if args[0] == pygame.K_UP:
                    self.rect = self.rect.move(0, 64)
                if args[0] == pygame.K_DOWN:
                    self.rect = self.rect.move(0, -64)
                if args[0] == pygame.K_LEFT:
                    self.rect = self.rect.move(64, 0)
                if args[0] == pygame.K_RIGHT:
                    self.rect = self.rect.move(-64, 0)

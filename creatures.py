import pygame
from level import box_group, player_group, all_sprites

# box_group = pygame.sprite.Group()
# player_group = pygame.sprite.Group()
# all_sprites = pygame.sprite.Group()
tile_width = tile_height = 50
player = None


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, animation, length):
        super().__init__(all_sprites)
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


# knight = AnimatedSprite(load_image("Thief_anim4.png"), 8, 5, 120, 80)
class Enemy(AnimatedSprite):
    def __init__(self, pos_x, pos_y, sheet, columns, rows, x, y, animation, length):
        super().__init__(sheet, columns, rows, x, y, animation, length)
        # self.image = enemy1_image
        # self.first_line = first_line
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 5, tile_height * pos_y + 5)


class Player(AnimatedSprite):
    def __init__(self, pos_x, pos_y, sheet, columns, rows, x, y, animation, length):
        super().__init__(sheet, columns, rows, x, y, animation, length)
        # self.image = player_imag
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 5, tile_height * pos_y + 5)

    def update(self, *args, **kwargs):
        if args:
            if args[0] == pygame.K_UP:
                player_group.sprites()[0].animation = 1
                for i in range(10):
                    self.rect = self.rect.move(0, -5)
            if args[0] == pygame.K_DOWN:
                self.rect = self.rect.move(0, 50)
            if args[0] == pygame.K_LEFT:
                self.rect = self.rect.move(-50, 0)
            if args[0] == pygame.K_RIGHT:
                self.rect = self.rect.move(50, 0)
        if pygame.sprite.spritecollide(self, box_group, False):
            if args[0] == pygame.K_UP:
                self.rect = self.rect.move(0, 50)
            if args[0] == pygame.K_DOWN:
                self.rect = self.rect.move(0, -50)
            if args[0] == pygame.K_LEFT:
                self.rect = self.rect.move(50, 0)
            if args[0] == pygame.K_RIGHT:
                self.rect = self.rect.move(-50, 0)

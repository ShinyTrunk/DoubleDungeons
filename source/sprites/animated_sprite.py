import pygame

from source.sprites.sprite_groups.sprite_groups import all_sprites


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


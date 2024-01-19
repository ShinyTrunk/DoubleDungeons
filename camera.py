import pygame
from settings import WIDTH, HEIGHT


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
        new_dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 2)
        new_dy = -(target.rect.y + target.rect.h // 2 - HEIGHT // 2)

        # Проверяем, чтобы камера не выходила за границы экрана
        if 0 <= target.rect.x + new_dx <= 1920 - WIDTH:
            self.dx = new_dx
        if 0 <= target.rect.y + new_dy <= 1600 - HEIGHT:
            self.dy = new_dy
        # self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 2)
        # self.dy = -(target.rect.y + target.rect.h // 2 - HEIGHT // 2)
        # if 0 <= target.rect.x + new_dx <= WIDTH - WIDTH:
        #     self.dx = new_dx
        # if 0 <= target.rect.y + new_dy <= map_height - HEIGHT:
        #     self.dy = new_dy

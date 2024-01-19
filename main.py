from camera import Camera
from secondary_functions import load_level, set_tiled_map
from sprite_groups import *
from start_screen import *

from settings import *
from level import *

pygame.init()
screen = pygame.display.set_mode(SIZE)

pygame.display.set_caption('Double Dungeons')
start_screen(screen)

set_tiled_map('level1_map')
player, level_x, level_y = generate_level(load_level('map/map.txt'))

camera = Camera()
clock = pygame.time.Clock()


def main(screen):
    running = True
    while running:
        player_group.sprites()[0].update_anim()
        for sprite in enemy_group.sprites():
            sprite.update_anim()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                player.update(event.key)
        camera.update(player)
        screen.fill((0, 0, 0))
        # обновляем положение всех спрайтов
        for sprite in all_sprites:
            camera.apply(sprite)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main(screen)
    terminate()

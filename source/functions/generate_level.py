from source.functions.load_image import load_image
from source.sprites.enemy import Enemy
from source.sprites.player import Player
from source.sprites.sprite_groups.sprite_groups import enemy_group, player_group


def generate_level(level, player_hp):
    new_player, x, y = None, None, None
    enemy_list = []
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '@':
                px, py = x, y
                new_player = Player(player_group, px, py,
                                    load_image("animated_sprites\\knight_animated_sprite_48x48.png"), 14,
                                    7, 120, 80, 0, 7, player_hp)
            elif level[y][x] == '!':
                enemy_list.append([x, y])
    for i in range(len(enemy_list)):
        if i % 2 == 0:
            Enemy(enemy_group, enemy_list[i][0], enemy_list[i][1],
                  load_image("animated_sprites\\thief_animated_sprite_48x48.png"), 8,
                  5, 125, 83.2, 0, 6)
        elif i % 2 != 0:
            Enemy(enemy_group, enemy_list[i][0], enemy_list[i][1],
                  load_image("animated_sprites\\thief_animated_sprite_48x48.png"), 8,
                  5, 120, 80, 0, 8)

    return new_player, x, y

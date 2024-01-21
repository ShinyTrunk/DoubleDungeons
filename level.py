from secondary_functions import load_image
from sprite_groups import enemy_group, player_group
from characters import Enemy, Player

enemy_list = []


def generate_level(level):
    new_player, x, y = None, None, None
    px, py = None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '@':
                # Tile('empty', x, y)
                px, py = x, y
            elif level[y][x] == '!':
                # Tile('empty', x, y)
                enemy_list.append([x, y])
    for i in range(len(enemy_list)):
        if i % 2 == 0:
            Enemy(enemy_group, enemy_list[i][0], enemy_list[i][1],
                  load_image("animated_sprites\\thief_animated_sprite_48x48.png"), 8,
                  5, 125, 83.2, 0, 6)
        if i % 2 != 0:
            Enemy(enemy_group, enemy_list[i][0], enemy_list[i][1],
                  load_image("animated_sprites\\thief_animated_sprite_48x48.png"), 8,
                  5, 120, 80, 0, 8)
    if len(player_group.sprites()) == 0:
        new_player = Player(player_group, px, py,
                            load_image("animated_sprites\\knight_animated_sprite_48x48.png"), 14,
                            7, 120, 80, 0, 7)

    return new_player, x, y

from source.sprites.sprite_groups import sprite_groups


def remove_all_sprites_groups():
    try:
        sprite_groups.all_sprites.remove(sprite_groups.all_sprites)
        sprite_groups.chests_group.remove(sprite_groups.chests_group)
        sprite_groups.potions_group.remove(sprite_groups.potions_group)
        sprite_groups.player_group.remove(sprite_groups.player_group)
        sprite_groups.enemy_group.remove(sprite_groups.enemy_group)
        sprite_groups.floor_tiles_group.remove(sprite_groups.floor_tiles_group)
        sprite_groups.walls_group.remove(sprite_groups.walls_group)
    except Exception as error:
        return error

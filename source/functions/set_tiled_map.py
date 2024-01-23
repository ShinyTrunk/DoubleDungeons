import pytmx

from source.helpers.settings import TILE_WIDTH, TILE_HEIGHT
from source.sprites.sprite_groups.sprite_groups import walls_group, chests_group, potions_group
from source.sprites.surface_to_sprite_transformer import Card


def set_tiled_map(filename):
    filename = f"source/data/map/{filename}.tmx"
    game_map = pytmx.load_pygame(filename)
    for layer in game_map.visible_layers:
        for x, y, gid, in layer:
            tile = game_map.get_tile_image_by_gid(gid)
            if tile is not None:
                if layer.name == "Walls":
                    Card(tile, x * TILE_WIDTH, y * TILE_HEIGHT, walls_group)
                elif layer.name == "Chests":
                    Card(tile, x * TILE_WIDTH, y * TILE_HEIGHT, chests_group)
                elif layer.name == "Potions":
                    Card(tile, x * TILE_WIDTH, y * TILE_HEIGHT, potions_group)
                else:
                    Card(tile, x * TILE_WIDTH, y * TILE_HEIGHT)

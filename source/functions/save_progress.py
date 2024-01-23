def save_progress(hp, damage, looted_chests, enemies_defeated):
    with open("source/data/saves/player_saves.txt", "w") as file:
        file.write(f"{hp} {damage} {looted_chests} {enemies_defeated}")

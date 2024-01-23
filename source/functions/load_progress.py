def load_progress():
    with open("source/data/saves/player_saves.txt", "r") as file:
        save = file.read().split()
        progress = {'hp': save[0], 'damage': save[1], 'looted_chests': save[2], 'enemies_defeated': save[3]}
    return progress

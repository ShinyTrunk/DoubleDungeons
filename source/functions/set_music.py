import pygame


def set_music(name, play=-1):
    pygame.mixer.music.load(f"source/data/sounds/{name}.mp3")
    pygame.mixer.music.play(play)

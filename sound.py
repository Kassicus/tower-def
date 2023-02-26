import pygame
import random

pygame.mixer.init()

gunshots = {
    "one": pygame.mixer.Sound("assets/sounds/gunshot_1.wav"),
    "two": pygame.mixer.Sound("assets/sounds/gunshot_2.wav"),
    "three": pygame.mixer.Sound("assets/sounds/gunshot_3.wav")
}

def play_random_sound(group: list) -> None:
    key, val = random.choice(list(group.items()))

    pygame.mixer.Sound.set_volume(group[key], 0.5)
    pygame.mixer.Sound.play(group[key])
    pygame.mixer.Sound.fadeout(group[key], 750)
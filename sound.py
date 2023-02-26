import pygame

pygame.mixer.init()

sounds = {
    "gunshot": pygame.mixer.Sound("assets/sounds/gunshot.wav")
}

def play_sound(sound: pygame.mixer.Sound):
    pygame.mixer.Sound.set_volume(sounds[sound], 0.5)
    pygame.mixer.Sound.play(sounds[sound])
    pygame.mixer.Sound.fadeout(sounds[sound], 750)
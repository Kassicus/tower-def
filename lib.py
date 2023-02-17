import pygame
import random

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

WAYPOINTS = [
    pygame.math.Vector2(100, 200),
    pygame.math.Vector2(400, 800),
    pygame.math.Vector2(900, 300)]

class Color():
    def __init__(self) -> None:
        self.BLACK = pygame.Color(0, 0, 0, 255)
        self.WHITE = pygame.Color(255, 255, 255, 255)
        self.RED = pygame.Color(255, 0, 0, 255)
        self.GREEN = pygame.Color(0, 255, 0, 255)
        self.BLUE = pygame.Color(0, 0, 255, 255)
        self.YELLOW = pygame.Color(255, 255, 0, 255)
        self.MAGENTA = pygame.Color(255, 0, 255, 255)
        self.CYAN = pygame.Color(0, 255, 255, 255)

    def get_random_color(self) -> pygame.Color:
        c = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        return c

color = Color()

display_surface = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
events = pygame.event.get()

delta_time = 0
frame_limit = 120
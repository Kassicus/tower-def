import pygame
import random

SCREEN_WIDTH_UNITS = 20
SCREEN_HEIGHT_UNITS = 12

SCREEN_MODIFIER = 64

SCREEN_WIDTH = int(SCREEN_WIDTH_UNITS * SCREEN_MODIFIER)
SCREEN_HEIGHT = int(SCREEN_HEIGHT_UNITS * SCREEN_MODIFIER)

LEVEL_BACKGROUNDS = {
    "grass_1": pygame.image.load("assets/tiled/grass_1.png")
}

ENEMY_SPRITES = {
    "base_right": pygame.image.load("assets/sprites/base_enemy_right.png"),
    "base_down": pygame.image.load("assets/sprites/base_enemy_down.png"),
    "base_left": pygame.image.load("assets/sprites/base_enemy_left.png"),
    "base_up": pygame.image.load("assets/sprites/base_enemy_up.png"),
}

TOWER_SPRITES = {
    "standard": pygame.image.load("assets/sprites/standard_turret.png"),
    "advanced": pygame.image.load("assets/sprites/advanced_turret.png")
}

RAW_WAYPOINTS = [
    [0, 3],
    [6, 3],
    [6, 8],
    [4, 8],
    [4, 10],
    [8, 10],
    [8, 3],
    [11, 3],
    [11, 2],
    [13, 2],
    [13, 7],
    [12, 7],
    [12, 9],
    [14, 9],
    [14, 7],
    [12, 7],
    [12, 9],
    [14, 9],
    [14, 8],
    [19, 8],
    [19, 6],
    [16, 6],
    [16, 4],
    [18, 4],
    [18, -1]
]

WAYPOINTS = []

def refine_waypoints() -> None:
    for waypoint in RAW_WAYPOINTS:
        w = pygame.math.Vector2(int(waypoint[0] * 64), int(waypoint[1] * 64))
        WAYPOINTS.append(w)

def create_random_waypoints(count: int) -> None:
    for x in range(count):
        w = pygame.math.Vector2(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
        WAYPOINTS.append(w)

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

        self.NONE = pygame.Color(145, 255, 77, 255)

    def get_random_color(self) -> pygame.Color:
        c = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        return c

color = Color()

display_surface = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
events = pygame.event.get()

delta_time = 0
frame_limit = 120
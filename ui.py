import pygame

import lib

class Store():
    def __init__(self, win_x: int, win_y: int, width: int, height: int) -> None:
        self.pos = pygame.math.Vector2(win_x, win_y)
        self.size = pygame.math.Vector2(width, height)
        self.is_visible = False

    def toggle_visibility(self) -> None:
        if self.is_visible:
            self.is_visible = False
        else:
            self.is_visible = True

    def draw_window(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, lib.color.WHITE, (self.pos.x, self.pos.y, self.size.x, self.size.y))
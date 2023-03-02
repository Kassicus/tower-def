import pygame

import lib

class BasePanel():
    def __init__(self, x: int, y: int, width: int, height: int, background_color: pygame.Color) -> object:
        self.pos = pygame.math.Vector2(x, y)
        self.size = pygame.math.Vector2(width, height)

        self.background_color = background_color

        self.buttons = pygame.sprite.Group()

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, self.background_color, (self.pos.x, self.pos.y, self.pos.x + self.size.x, self.pos.y + self.size.y))
        self.buttons.draw(surface)

    def update(self) -> None:
        self.buttons.update()

class StorePanel(BasePanel):
    def __init__(self) -> object:
        super().__init__(1280, 0, 250, 768, lib.color.WHITE)

class InfoPanel(BasePanel):
    def __init__(self) -> object:
        super().__init__(0, 768, lib.SCREEN_WIDTH, 150, lib.color.RED)
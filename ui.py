import pygame

import lib

class CloseButton(pygame.sprite.Sprite):
    def __init__(self, win_x: int, win_y: int, width: int, height: int, parent: object) -> None:
        super().__init__()

        self.pos = pygame.math.Vector2(win_x, win_y)
        self.size = pygame.math.Vector2(width, height)

        self.parent = parent

        self.is_hovered = False

        self.image = pygame.Surface([self.size.x, self.size.y])
        self.image.fill(lib.color.RED)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def close_parent(self) -> None:
        self.parent.close()

    def check_hovered(self) -> bool:
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if self.pos.x < mouse_x < self.pos.x + self.size.x:
            if self.pos.y < mouse_y < self.pos.y + self.size.y:
                return True
            else:
                return False
        else:
            return False

    def check_clicked(self) -> bool:
        if pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False

    def update(self) -> None:
        if self.check_hovered():
            if self.check_clicked():
                self.close_parent()

class BaseWindow():
    def __init__(self, win_x: int, win_y: int, width: int, height: int, background_color: pygame.Color) -> None:
        self.pos = pygame.math.Vector2(win_x, win_y)
        self.size = pygame.math.Vector2(width, height)

        self.background_color = background_color

        self.is_visible = False

        self.buttons = pygame.sprite.Group()
        self.close_button = CloseButton(self.pos.x + self.size.x - 30, self.pos.y, 30, 30, self)

    def close(self) -> None:
        self.is_visible = False

    def toggle_visibility(self) -> None:
        if self.is_visible:
            self.is_visible = False
        else:
            self.is_visible = True

    def draw_window(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, self.background_color, (self.pos.x, self.pos.y, self.size.x, self.size.y))
        self.buttons.draw(surface)

    def update(self) -> None:
        self.buttons.update()

class Store(BaseWindow):
    def __init__(self, win_x: int, win_y: int, width: int, height: int) -> None:
        super().__init__(win_x, win_y, width, height, lib.color.WHITE)

class Menu(BaseWindow):
    def __init__(self, win_x: int, win_y: int, width: int, height: int) -> None:
        super().__init__(win_x, win_y, width, height, lib.color.WHITE)


import pygame

import lib
import groups

class Grid(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, size: int) -> None:
        super().__init__()

        self.pos = pygame.math.Vector2(x, y)
        
        self.image = pygame.Surface([size, size])
        self.image.fill(lib.color.NONE)
        self.image.set_colorkey(lib.color.NONE)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def update(self):
        pass

class Level():
    def __init__(self, background: str, grid_size: list, grid_box_size: int) -> None:
        self.background = lib.LEVEL_BACKGROUNDS["grass_1"]

        self.grid_size = pygame.math.Vector2(grid_size[0], grid_size[1])
        self.grid_box_size = grid_box_size

    def create_grid(self) -> None:
        for x in range(int(self.grid_size.x)):
            for y in range(int(self.grid_size.y)):
                g = Grid(x * self.grid_box_size, y * self.grid_box_size, self.grid_box_size)
                groups.grid_tiles.add(g)

    def highlight_grid(self) -> None:
        mouse_x, mouse_y = pygame.mouse.get_pos()

        for grid in groups.grid_tiles:
            if grid.pos.x < mouse_x < grid.pos.x + grid.rect.width:
                if grid.pos.y < mouse_y < grid.pos.y + grid.rect.height:
                    print(grid.pos.x, grid.pos.y)

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.background, (0, 0))

    def update(self) -> None:
        #self.highlight_grid()
        pass
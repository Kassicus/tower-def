import pygame

import lib

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, vel: pygame.math.Vector2, size: int, damage: int) -> None:
        super().__init__()

        self.pos = pygame.math.Vector2(x, y)
        self.vel = vel

        self.damage = damage

        self.lifetime = 8000

        self.image = pygame.Surface([size, size])
        self.image.fill(lib.color.MAGENTA)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def destroy(self) -> None:
        self.kill()

    def update(self) -> None:
        self.pos += self.vel * lib.delta_time
        self.rect.center = self.pos

        self.lifetime -= 1
        if self.lifetime <= 0:
            self.kill()

import pygame
import math

import lib

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, vel: pygame.math.Vector2, size: int, damage: int, color: pygame.Color) -> None:
        super().__init__()

        self.pos = pygame.math.Vector2(x, y)
        self.vel = vel

        self.damage = damage

        self.lifetime = 8000

        self.image = pygame.Surface([size, size])
        self.image.fill(color)
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

class TrackingProjectile(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, speed: int, target: pygame.sprite.Sprite, size: int, damage: int, color: pygame.Color) -> None:
        super().__init__()

        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(0, 0)

        self.speed = speed
        self.target = target

        self.damage = damage
        self.lifetime = 8000

        self.image = pygame.Surface([size, size])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def get_vectors(self) -> list:
        distance = [self.target.pos.x - self.pos.x, self.target.pos.y - self.pos.y]
        normal = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
        rate = [distance[0] / normal, distance[1] / normal]
        vectors = [rate[0] * self.speed, rate[1] * self.speed]

        return vectors
    
    def chase_target(self) -> None:
        self.vel.x = self.get_vectors()[0]
        self.vel.y = self.get_vectors()[1]

    def destroy(self) -> None:
        self.kill()    
        
    def update(self) -> None:
        if self.target.health >= 3:
            self.chase_target()

        self.pos += self.vel * lib.delta_time
        self.rect.center = self.pos

        self.lifetime -= 1
        if self.lifetime <= 0:
            self.kill()
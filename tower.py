import pygame
import math
import random

import lib
import groups
import projectile

class BaseTurret(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, size: int, damage: int, projectile_speed: float) -> None:
        super().__init__()

        self.pos = pygame.math.Vector2(x, y)

        self.damage = damage
        self.projectile_speed = projectile_speed
        self.shot_max_cooldown = 100
        self.shot_cooldown = 100
        
        self.image = pygame.Surface([size, size])
        self.image.fill(lib.color.WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def get_vectors(self, target: pygame.math.Vector2) -> list:
        distance = [target.x - self.pos.x, target.y - self.pos.y]
        normal = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
        rate = [distance[0] / normal, distance[1] / normal]
        vectors = [rate[0] * self.projectile_speed, rate[1] * self.projectile_speed]

        return vectors
    
    def shoot(self) -> None:
        if len(groups.enemies) > 0:
            target = random.choice(groups.enemies.sprites())
            target_raw_vectors = self.get_vectors(target.pos)
            target_vectors = pygame.math.Vector2(target_raw_vectors[0], target_raw_vectors[1])
            proj = projectile.Projectile(self.pos.x, self.pos.y, target_vectors, 4, 1)
            groups.projectiles.add(proj)
    
    def update(self) -> None:
        self.shot_cooldown -= 1

        if self.shot_cooldown <= 0:
            self.shoot()
            self.shot_cooldown = self.shot_max_cooldown

class RedTurret(BaseTurret):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 40, 1, 1500)
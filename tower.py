import pygame
import math
import random

import lib
import groups
import projectile

class BaseTurret(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, size: int, damage: int, projectile_speed: float, color: pygame.Color) -> None:
        super().__init__()

        self.pos = pygame.math.Vector2(x, y)

        self.damage = damage
        self.projectile_speed = projectile_speed
        self.shot_max_cooldown = 100
        self.shot_cooldown = 100

        self.target_type = "first"
        self.projectile_type = "static"

        self.color = color
        
        self.image = pygame.Surface([size, size])
        self.image.fill(self.color)
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
            match self.target_type:
                case "first":
                    target = groups.enemies.sprites()[0]
                case "last":
                    last = len(groups.enemies)
                    target = groups.enemies.sprites()[last - 1]
                case "random":
                    target = random.choice(groups.enemies.sprites())
                case _:
                    target = groups.enemies.sprites()[0]

            match self.projectile_type:
                case "static":
                    target_raw_vectors = self.get_vectors(target.pos)
                    target_vectors = pygame.math.Vector2(target_raw_vectors[0], target_raw_vectors[1])
                    proj = projectile.Projectile(self.pos.x, self.pos.y, target_vectors, 4, 1, self.color)
                    groups.projectiles.add(proj)
                case "dynamic":
                    proj = projectile.TrackingProjectile(self.pos.x, self.pos.y, self.projectile_speed, target, 4, 3, self.color)
                    groups.projectiles.add(proj)
    
    def update(self) -> None:
        self.shot_cooldown -= 1

        if self.shot_cooldown <= 0:
            self.shoot()
            self.shot_cooldown = self.shot_max_cooldown

class RedTurret(BaseTurret):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 40, 1, 1500, lib.color.RED)

class BlueTurret(BaseTurret):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 30, 3, 200, lib.color.BLUE)
        self.shot_max_cooldown = 30
        self.shot_cooldown = 30
        self.projectile_type = "dynamic"
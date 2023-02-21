import pygame
import math
import random

import lib
import groups
import projectile

class BaseTurret(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, damage: int, projectile_speed: float) -> None:
        super().__init__()

        self.pos = pygame.math.Vector2(x, y)

        self.damage = damage
        self.projectile_speed = projectile_speed
        self.shot_max_cooldown = 100
        self.shot_cooldown = 100

        self.target_type = "first"
        self.projectile_type = "static"

        self.target = None
        
        self.image = lib.TOWER_SPRITES["standard"].convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def get_vectors(self, target: pygame.math.Vector2) -> list:
        distance = [target.x - self.pos.x, target.y - self.pos.y]
        normal = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
        rate = [distance[0] / normal, distance[1] / normal]
        vectors = [rate[0] * self.projectile_speed, rate[1] * self.projectile_speed]

        return vectors
    
    def rotate_to_target(self, target: pygame.math.Vector2) -> tuple[pygame.Surface, pygame.Rect]:
        angle = math.atan2(self.pos.x - target.x, self.pos.y - target.y)
        degrees = math.degrees(angle)

        rotated_image = pygame.transform.rotate(self.image, degrees)
        new_rect = rotated_image.get_rect(center = self.rect.center)

        return(rotated_image, new_rect)
    
    def shoot(self) -> None:
        if len(groups.enemies) > 0:
            match self.target_type:
                case "first":
                    self.target = groups.enemies.sprites()[0]
                case "last":
                    last = len(groups.enemies)
                    self.target = groups.enemies.sprites()[last - 1]
                case "random":
                    self.target = random.choice(groups.enemies.sprites())
                case _:
                    self.target = groups.enemies.sprites()[0]

            match self.projectile_type:
                case "static":
                    target_raw_vectors = self.get_vectors(self.target.pos)
                    target_vectors = pygame.math.Vector2(target_raw_vectors[0], target_raw_vectors[1])
                    proj = projectile.Projectile(self.pos.x, self.pos.y, target_vectors, 1)
                    groups.projectiles.add(proj)
                case "dynamic":
                    proj = projectile.TrackingProjectile(self.pos.x, self.pos.y, self.projectile_speed, self.target, 3)
                    groups.projectiles.add(proj)

    def rotate_sprite(self, surface: pygame.Surface) -> None:
        if self.target != None:
            rotated = self.rotate_to_target(self.target.pos)
            surface.blit(rotated[0], rotated[1])
        else:
            rot_hold = pygame.math.Vector2(self.pos.x, self.pos.y - 100)
            rotated = self.rotate_to_target(rot_hold)
            surface.blit(rotated[0], rotated[1])

    def update(self) -> None:
        self.shot_cooldown -= 1

        if self.shot_cooldown <= 0:
            self.shoot()
            self.shot_cooldown = self.shot_max_cooldown

class RedTurret(BaseTurret):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 1, 1500)

class BlueTurret(BaseTurret):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 3, 600)
        self.image = lib.TOWER_SPRITES["advanced"].convert_alpha()
        self.shot_max_cooldown = 30
        self.shot_cooldown = 30
        self.projectile_type = "dynamic"
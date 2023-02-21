import pygame
import math

import lib

class BaseEnemy(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, size: int, health: int, speed: float) -> None:
        super().__init__()

        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(0, 0)

        self.speed = speed
        self.health = health

        self.waypoints = lib.WAYPOINTS.copy()

        self.image = lib.ENEMY_SPRITES["base_right"].convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def move_to_waypoint(self, waypoint: pygame.math.Vector2) -> None:
        if self.waypoints:
            if self.rect.center != waypoint:
                self.vel.x = int(self.get_vectors(waypoint)[0])
                self.vel.y = int(self.get_vectors(waypoint)[1])
            else:
                self.waypoints.pop(0)

    def get_vectors(self, target: pygame.math.Vector2) -> list:
        distance = [target.x - self.pos.x, target.y - self.pos.y]
        normal = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
        rate = [distance[0] / normal, distance[1] / normal]
        vectors = [rate[0] * self.speed, rate[1] * self.speed]

        return vectors

    def debug(self) -> None:
        if len(self.waypoints) >= 1:
            pygame.draw.line(pygame.display.get_surface(), lib.color.BLUE, self.pos, self.waypoints[0], 1)
            pygame.draw.line(pygame.display.get_surface(), lib.color.RED, self.pos, (self.pos.x, self.pos.y + self.vel.y))
            pygame.draw.line(pygame.display.get_surface(), lib.color.GREEN, self.pos, (self.pos.x + self.vel.x, self.pos.y))

    def update(self) -> None:
        self.pos += self.vel * lib.delta_time
        self.rect.center = pygame.math.Vector2(round(self.pos.x), round(self.pos.y))

        if self.vel.x < 0:
            self.image = lib.ENEMY_SPRITES["base_left"].convert_alpha()
        elif self.vel.x > 0:
            self.image = lib.ENEMY_SPRITES["base_right"].convert_alpha()
        elif self.vel.y < 0:
            self.image = lib.ENEMY_SPRITES["base_up"].convert_alpha()
        elif self.vel.y > 0:
            self.image = lib.ENEMY_SPRITES["base_down"].convert_alpha()

        if len(self.waypoints) >= 1:
            self.move_to_waypoint(self.waypoints[0])
        else:
            self.vel.x, self.vel.y = 0, 0

        if self.pos.y < -50:
            self.kill()

        if self.health <= 0:
            self.kill()

class RedEnemy(BaseEnemy):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 20, 10, 50)
        
        
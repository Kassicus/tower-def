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

        self.waypoints = lib.WAYPOINTS

        self.image = pygame.Surface([size, size])
        self.image.fill(lib.color.RED)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def move_to_waypoint(self, waypoint: pygame.math.Vector2) -> None:
        if self.waypoints:
            if self.rect.center != waypoint:
                self.vel.x = int(self.get_vectors(waypoint)[0])
                self.vel.y = int(self.get_vectors(waypoint)[1])
            else:
                self.waypoints.pop(0)
        else:
            self.vel.x, self.vel.y = 0, 0

    def get_vectors(self, target: pygame.math.Vector2) -> list:
        distance = [target.x - self.pos.x, target.y - self.pos.y]
        normal = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
        rate = [distance[0] / normal, distance[1] / normal]
        vectors = [rate[0] * self.speed, rate[1] * self.speed]

        return vectors

    def update(self) -> None:
        self.pos += self.vel * lib.delta_time
        self.rect.center = pygame.math.Vector2(int(self.pos.x), int(self.pos.y))

        print(self.rect.center, self.pos, self.waypoints[0])

        if self.waypoints:
            self.move_to_waypoint(self.waypoints[0])

        #TODO Move this to the debug file for each enemy
        #pygame.draw.line(pygame.display.get_surface(), lib.color.CYAN, self.pos, self.waypoints[0], 3)

        if self.health <= 0:
            self.kill()

class RedEnemy(BaseEnemy):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 20, 10, 300)
        
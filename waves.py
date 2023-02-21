import pygame

import lib
import enemy
import groups

wave_group = pygame.sprite.Group()

class Wave(pygame.sprite.Sprite):
    def __init__(self, enemy_type: str, count: int, spawn_delay: float) -> None:
        super().__init__()
        self.enemy_type = enemy_type
        self.count = count
        self.current_count = 0
        self.spawn_delay = spawn_delay
        self.spawn_time = 0

        self.image = pygame.Surface([0, 0])
        self.image.fill(lib.color.NONE)
        self.image.set_colorkey(lib.color.NONE)
        self.rect = self.image.get_rect()

    def update(self):
        if self.current_count < self.count:

            self.spawn_time += 1

            if self.spawn_time >= self.spawn_delay:
                match self.enemy_type:
                    case "basic":
                        e = enemy.RedEnemy(-100, 192)
                        groups.enemies.add(e)
                        self.current_count += 1

                self.spawn_time = 0

        else:
            self.kill()
import pygame

enemies = pygame.sprite.Group()
towers = pygame.sprite.Group()
projectiles = pygame.sprite.Group()

def check_projectile_collision() -> None:
    for e in enemies:
        for p in projectiles:
            if e.rect.colliderect(p.rect):
                e.health -= p.damage
                p.destroy()
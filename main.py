import pygame

import lib
import debug
import enemy
import groups
import tower

pygame.init()

class Game():
    def __init__(self) -> None:
        self.screen = lib.display_surface
        pygame.display.set_caption("Tower Defender")

        self.running = True
        self.clock = pygame.time.Clock()

        self.debug_interface = debug.DebugInterface()

        lib.create_random_waypoints(5)

        self.test = tower.RedTurret(500, 500)
        self.test2 = tower.RedTurret(1000, 800)
        groups.towers.add(self.test, self.test2)
        
    def run(self) -> None:
        while self.running:
            self.event_loop()
            self.draw()
            self.update()

    def event_loop(self) -> None:
        lib.events = pygame.event.get()

        for event in lib.events:
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    self.debug_interface.toggle_active()

                if event.key == pygame.K_ESCAPE:
                    self.running = False

                if event.key == pygame.K_e:
                    e = enemy.RedEnemy(100, 100)
                    groups.enemies.add(e)

    def draw(self) -> None:
        self.screen.fill(lib.color.BLACK)

        groups.enemies.draw(self.screen)
        groups.towers.draw(self.screen)
        groups.projectiles.draw(self.screen)

        if self.debug_interface.active:
            self.debug_interface.draw()
            
            for enemy in groups.enemies:
                enemy.debug()

    def update(self) -> None:
        groups.enemies.update()
        groups.towers.update()
        groups.projectiles.update()
        groups.check_projectile_collision()

        self.debug_interface.update(self.clock)
        pygame.display.update()
        lib.delta_time = self.clock.tick(lib.frame_limit) / 1000

if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()
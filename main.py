import pygame

import lib
import debug
import enemy
import groups
import tower
import level
import waves

pygame.init()

class Game():
    def __init__(self) -> None:
        self.screen = lib.display_surface
        pygame.display.set_caption("Tower Defender")

        self.running = True
        self.clock = pygame.time.Clock()

        self.debug_interface = debug.DebugInterface()

        self.level = level.Level([10, 12], 64)
        self.level.create_grid()

        lib.refine_waypoints()
        
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
                    e = enemy.RedEnemy(-100, 192)
                    groups.enemies.add(e)

                if event.key == pygame.K_b:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    t = tower.DoubleTurret(mouse_x, mouse_y)
                    groups.towers.add(t)
                
                if event.key == pygame.K_r:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    t = tower.SingleTurret(mouse_x, mouse_y)
                    groups.towers.add(t)

                if event.key == pygame.K_w:
                    w = waves.Wave("basic", 50, 50)
                    waves.wave_group.add(w)

    def draw(self) -> None:
        self.screen.fill(lib.color.BLACK)

        self.level.draw(self.screen)

        groups.enemies.draw(self.screen)
        groups.projectiles.draw(self.screen)

        for tower in groups.towers:
            tower.rotate_sprite(self.screen)    

        if self.debug_interface.active:
            self.debug_interface.draw()
            
            for enemy in groups.enemies:
                enemy.debug()

    def update(self) -> None:
        groups.enemies.update()
        groups.towers.update()
        groups.projectiles.update()
        
        groups.check_projectile_collision()

        waves.wave_group.update()

        self.level.update()

        self.debug_interface.update(self.clock)
        pygame.display.update()
        lib.delta_time = self.clock.tick(lib.frame_limit) / 1000

if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()
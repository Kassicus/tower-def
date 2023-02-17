import pygame

import lib

class DebugInterface():
    def __init__(self) -> None:
        self.active = False

        self.font = pygame.font.SysFont("Courier", 16)

        self.fps_text = None

        self.display_surface = pygame.display.get_surface()

    def get_fps(self, clock: pygame.time.Clock) -> pygame.Surface:
        fps_string = "FPS: " + str(int(clock.get_fps()))
        fps_text = self.font.render(fps_string, True, lib.color.CYAN)
        return fps_text
    
    def toggle_active(self) -> None:
        if self.active:
            self.active = False
        else:
            self.active = True
    
    def draw(self) -> None:
        self.display_surface.blit(self.fps_text, (1820, 10))

    def update(self, clock: pygame.time.Clock) -> None:
        self.fps_text = self.get_fps(clock)
import pygame

import lib

class DebugInterface():
    def __init__(self) -> None:
        self.active = False

        self.font = pygame.font.SysFont("Courier", 16)

        self.fps_text = None
        self.mouse_text = None

        self.fps_offset = 0
        self.mouse_offset = 0

        self.display_surface = pygame.display.get_surface()

    def get_fps(self, clock: pygame.time.Clock) -> list [pygame.Surface, int]:
        fps_string = "FPS: " + str(int(clock.get_fps()))
        fps_text = self.font.render(fps_string, True, lib.color.CYAN)
        
        fps_offset = int(lib.SCREEN_WIDTH - lib.SIDE_PANEL_WIDTH - fps_text.get_width() - 10)

        return fps_text, fps_offset
    
    def get_mouse(self) -> list [pygame.Surface, int]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_string = "Mouse: " + str(mouse_x) + " " + str(mouse_y)
        mouse_text = self.font.render(mouse_string, True, lib.color.CYAN)

        mouse_offset = int(lib.SCREEN_WIDTH - lib.SIDE_PANEL_WIDTH - mouse_text.get_width() - 10)

        return mouse_text, mouse_offset
    
    def toggle_active(self) -> None:
        if self.active:
            self.active = False
        else:
            self.active = True
    
    def draw(self) -> None:
        self.display_surface.blit(self.fps_text, (self.fps_offset, 10))
        self.display_surface.blit(self.mouse_text, (self.mouse_offset, 30))

    def update(self, clock: pygame.time.Clock) -> None:
        self.fps_text, self.fps_offset = self.get_fps(clock)
        self.mouse_text, self.mouse_offset = self.get_mouse()
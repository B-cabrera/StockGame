# My Own Button Class
from typing import Tuple
import pygame
from pygame import Rect
from pygame import font

class Button:

    def __init__(self, sface: pygame.Surface, loc_x: int, loc_y: int, long: int, wide: int, label: str) -> None:
        self.x = loc_x
        self.y = loc_y
        self.len = long
        self.wid = wide
        self.surface = sface
        self.text = label


    def draw(self, screen: pygame.display, color: Tuple) -> None:
        box = Rect(self.x, self.y, self.len, self.wid)
        
        # Making text inside the button
        button_font = font.SysFont('avenir', 30, True)
        button_text = button_font.render(self.text, True, (255,255,255))

        
        # Showing the text and the button
        pygame.draw.rect(self.surface, color, box, 0, 20)
        self.surface.blit(button_text, (self.x + (self.len / 2) - 30 ,  self.y + self.wid / 5))
        
        screen.flip()



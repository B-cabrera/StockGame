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
        self.box = Rect(self.x, self.y, self.len, self.wid)
        self.is_clicked = False

    def draw(self, screen: pygame.display, color: Tuple) -> bool:

        # Handling event if button is clicked
        mouse_pos = pygame.mouse.get_pos()

        if self.box.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0] == True and self.is_clicked  == False:
                self.is_clicked = True
                return True

        # Making text inside the button
        button_font = font.SysFont('avenir', 30, True)
        button_text = button_font.render(self.text, True, (255,255,255))

        
        # Showing the text and the button
        pygame.draw.rect(self.surface, color, self.box, 0, 20)
        self.surface.blit(button_text, button_text.get_rect(center = self.box.center))

        screen.flip()


        

    def get_rect(self) -> Rect:
        return self.box




        



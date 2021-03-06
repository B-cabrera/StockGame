# Class for stock

from random import randint
from typing import Tuple
import pygame
from pygame import Rect, Surface
from pygame import font
from button import Button



class Stock:

    def __init__(self, name: str, share_price: int, dimensions: Tuple) -> None:
        self.tick = self.__check_tick(name)
        self.price = share_price
        self.temp_constants = dimensions  # Dimensions of the game window
        self.be_shown = True
        self.open_for_trade = False


    # Changes the word passed into a 5 letter stock ticker
    def __check_tick(self, word: str) -> str:

        if len(word) > 5:
            word = word[0:5]

        return word.upper()


    # Displays the Stock details and allows for game to start
    def show(self, space: Surface, window: pygame.display, color: Tuple) -> bool:
        if self.be_shown:
            top_line = pygame.draw.aaline(space, color, (0,50), (self.temp_constants[1], 50))
            bottom_line = pygame.draw.aaline(space, color, (0, self.temp_constants[0] - 100), (self.temp_constants[1], self.temp_constants[0] - 100))

            self.show_price(space)

            window.flip()

            if self.__start(space, window):
                self.open_for_trade= True
                cover_rect = Rect(0,0,300,60)
                cover_rect.center = space.get_rect().center
                pygame.draw.rect(space, (0,0,0), cover_rect)
                self.be_shown = False

            
    # Starts the game after start button is pressed
    def __start(self, face: Surface, dplay: pygame.display) -> bool:
        started = False

        start_button = Button(face, 0, 0, 300, 60, "START")

        # Centering starting button in window
        start_button.get_rect().center = (face.get_rect().center)

        if start_button.draw(dplay, (192,192,192)):
            started = True
            return started

    # Displays the stock price with format -> TICKER: $Price
    def show_price(self, place: Surface) -> Surface:

        stock_font = font.SysFont('timesnewroman', 30)
        stock_text = stock_font.render(f"{self.tick}: ${self.price}", True, (255,255,255))
        place.blit(stock_text, (0, 50))

        return stock_text




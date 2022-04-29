from tkinter import CENTER
import pygame
from player import Player
from pygame import font
from button import Button
from stock import Stock



class PlayingField(object):
    
    # Constants for window size
    WINDOW_HEIGHT = 600
    WINDOW_LENGTH = 1000

    def __init__(self):
        pygame.init()
        them = Player()

        # Colors for button, green = buy, red = sell
        green = (0,200,5)
        red = (244,85,50)
        black = (0,0,0)
        white = (255,255,255)
        

        # Setting up the window 
        self.window  = pygame.display
        self.surface = self.window.set_mode((self.WINDOW_LENGTH, self.WINDOW_HEIGHT))
        self.window.set_caption("Brenden Cabrera Stock Game")

        # Initializing the Stock
        my_stock = Stock("ABCDEFGHIJK", 10000)

        # Showing the Stock on screen
        top_line = pygame.draw.aaline(self.surface, white, (0,50), (self.WINDOW_LENGTH, 50))
        bottom_line = pygame.draw.aaline(self.surface, white, (0, self.WINDOW_HEIGHT - 100), (self.WINDOW_LENGTH, self.WINDOW_HEIGHT - 100))
        stock_font = font.SysFont('timesnewroman', 30)
        stock_text = stock_font.render(f"{my_stock.tick}: ${my_stock.price}", True, white)
        self.surface.blit(stock_text, (0, 50))

        self.window.flip()




        self.temp_middle_x = self.WINDOW_LENGTH / 2

        # Setting up Buy button
        buy_button = Button(self.surface, 0 , 0, 300 , 60, "BUY")
        button_rect = buy_button.get_rect()
        button_rect.center = (self.WINDOW_LENGTH // 2, self.WINDOW_HEIGHT - buy_button.wid)

        self.show_starting_balance(them)
    


        # Running Loop
        running = True

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Showing the Buy button if not in trade
            if not them.is_in_trade():
                if buy_button.draw(self.window, green):
                    them.enter_trade()
            else:
                # Setting up Sell button
                cover_rect = buy_button.get_rect()
                pygame.draw.rect(self.surface, black, cover_rect)
                sell_button = Button(self.surface, 0 , 0, 300 , 60, "SELL")

                button_rect = sell_button.get_rect()
                button_rect.center = (self.WINDOW_LENGTH // 2, self.WINDOW_HEIGHT - sell_button.wid)

                if sell_button.draw(self.window, red):
                    them.exit_trade()

        pygame.quit()

        


    def show_starting_balance(self, player: Player) :
        pygame.font.init()

        # Setting basic color
        white = (255,255,255)

        basicfont = font.SysFont('cambria', 40)
        balance = player.get_balance()

        text = basicfont.render(f"Balance: ${balance}", True, white)

        self.surface.blit(text, text.get_rect(center = (self.surface.get_rect().center[0], 20)))
        self.window.flip()

        








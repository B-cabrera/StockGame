from random import randint
import pygame
from player import Player
from pygame import Rect, font
from button import Button
from stock import Stock



class PlayingField(object):
    
    # Constants for window size
    WINDOW_HEIGHT = 600
    WINDOW_LENGTH = 1000

    def __init__(self):
        pygame.init()
        self.them = Player()

        # Colors for button, green = buy, red = sell
        self.green = (0,200,5)
        self.red = (244,85,50)
        self.black = (0,0,0)
        white = (255,255,255)
        

        # Setting up the window 
        self.window  = pygame.display
        self.surface = self.window.set_mode((self.WINDOW_LENGTH, self.WINDOW_HEIGHT))
        self.window.set_caption("Brenden Cabrera Stock Game")

        # Initializing the Stock
        my_stock = Stock("ABCDEFGHIJK", 10000, (self.WINDOW_HEIGHT, self.WINDOW_LENGTH))

        self.temp_middle_x = self.WINDOW_LENGTH / 2

        # Setting up Buy button
        self.buy_button = Button(self.surface, 0 , 0, 300 , 60, "BUY")
        button_rect = self.buy_button.get_rect()
        button_rect.center = (self.WINDOW_LENGTH // 2, self.WINDOW_HEIGHT - self.buy_button.wid)

        self.show_starting_balance(self.them)

        lines = []
        prev_end = (0,self.WINDOW_HEIGHT // 2)
        next_end = (randint(0, self.WINDOW_LENGTH // 4), randint(100, self.WINDOW_HEIGHT - 110))
    

        # Running Loop
        running = True

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if not self.them.is_in_trade():
                        self.them.enter_trade()
                    else: 
                        self.them.exit_trade()


            # Showing the Stock on screen
            my_stock.show(self.surface, self.window, white)

            if my_stock.open_for_trade:

                # Showing stock line 
                if next_end[0] <= self.WINDOW_LENGTH :
                    temp_rect = pygame.draw.line(self.surface, (255,255,255), prev_end, next_end)
                    lines.append(temp_rect)

                    pygame.time.delay(500)
                    self.window.flip()

                    self.show_status()

                    prev_end = next_end
                    next_end = (randint(prev_end[0], self.WINDOW_LENGTH + 5), randint(100, self.WINDOW_HEIGHT - 110))
                else:
                    for line in lines:
                        pygame.draw.rect(self.surface, (0,0,0), line)
                        self.window.flip()
                
                    prev_end = (0, next_end[1])
                    next_end = (randint(0, self.WINDOW_LENGTH // 4), randint(100, self.WINDOW_HEIGHT - 110))


    
    
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


    def show_status(self):
        if not self.them.is_in_trade():
            self.buy_button.draw(self.window, self.green)
               
        else:
            # Setting up Sell button
            cover_rect = self.buy_button.get_rect()
            pygame.draw.rect(self.surface, self.black, cover_rect)
            sell_button = Button(self.surface, 0 , 0, 300 , 60, "SELL")

            button_rect = sell_button.get_rect()
            button_rect.center = (self.WINDOW_LENGTH // 2, self.WINDOW_HEIGHT - sell_button.wid)

            sell_button.draw(self.window, self.red)

        








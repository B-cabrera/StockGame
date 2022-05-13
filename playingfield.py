from pickle import FALSE
from random import randint
from typing import List
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

        # Setting up Buy button
        self.buy_button = Button(self.surface, 0 , 0, 300 , 60, "BUY")
        button_rect = self.buy_button.get_rect()
        button_rect.center = (self.WINDOW_LENGTH // 2, self.WINDOW_HEIGHT - self.buy_button.wid)

        # Constantly showing player balance
        self.show_balance()

        # Initial Random Values for Stock Line
        lines = []
        prev_end = (0,self.WINDOW_HEIGHT // 2)
        next_end = (prev_end[0] + 20, randint(100, self.WINDOW_HEIGHT - 110))

        # Setting initial clock speed
        clock = pygame.time.Clock()
        clock.tick(10)

        # Running Loop
        running = True

        while running:
            # Checking for win/loss constantly
            self.win_loss_check(my_stock)

            # Listening for key presses
            running = self.listen_for_key(my_stock)

            # Showing instructions
            self.display_instructions()

            # Showing the Stock on screen
            my_stock.show(self.surface, self.window, white)

            if my_stock.open_for_trade:

                # Showing stock line 
                if next_end[0] <= self.WINDOW_LENGTH :
                    clock.tick(5)

                    change = prev_end[1] - next_end[1]

                    self.update_stock_price(my_stock, change)

                    # Updating balance if they're in a trade
                    if self.them.is_in_trade():
                        self.update_player_balance(change * 10)    

                    # Rect to cover the stock line sections
                    temp_rect = pygame.draw.line(self.surface, (79, 134, 255), prev_end, next_end, 3)
                    lines.append(temp_rect)


                    self.window.flip()

                    self.show_status()

                    # Setting up coordinates for next line sections
                    prev_end = next_end
                    next_end = (prev_end[0] + 20, randint(100, self.WINDOW_HEIGHT - 110))
                else:
                    # Clearing lines on screen and restarting at left side of window
                    self.clear_lines(lines)
                    prev_end = (0, next_end[1])
                    next_end = (prev_end[0] + 20, randint(100, self.WINDOW_HEIGHT - 110))
    

        pygame.quit()
        

    # Displaying player's current balance with format: Balance: $Player-Balance
    def show_balance(self) :
        pygame.font.init()

        # Setting basic color
        white = (255,255,255)

        basicfont = font.SysFont('cambria', 40)
        balance = self.them.get_balance()

        text = basicfont.render(f"Balance: ${balance}", True, white)

        self.surface.blit(text, text.get_rect(center = (self.surface.get_rect().center[0], 20)))
        self.window.flip()


    # Showing Buy or Sell at the bottom of the screen, depending on trade status
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

    # Showing the game instructions at the top of the screen
    def display_instructions(self):
        instructions_font = font.SysFont('cambria', 20)

        # Rendering all text
        instructions_top = instructions_font.render("USE SPACEBAR TO ENTER", True, (255,255,255))
        instructions_bottom = instructions_font.render("AND EXIT TRADE", True, (255,255,255))
        instructions_right_top = instructions_font.render("GET 15,000 TO WIN", True, (255,255,255))
        instructions_right_bottom = instructions_font.render("OR LOSE WHEN YOU'RE BROKE", True, (255,255,255))

        # Display all text
        self.surface.blit(instructions_top, (0,0))
        self.surface.blit(instructions_bottom, (0, 20))
        self.surface.blit(instructions_right_top, (800,0))
        self.surface.blit(instructions_right_bottom, (700, 20))

    # Changing stock price after a change, then showing it
    def update_stock_price(self, stock: Stock, value: int) -> None:
        
        pygame.draw.rect(self.surface, (0,0,0), Rect(100, 55, 110, 50))
        stock.price += value
        stock.show_price(self.surface)

    # Changing player balance after a change, then showing it
    def update_player_balance(self, cash: int):
        pygame.draw.rect(self.surface, (0,0,0), Rect(300, 0, 400, 50))

        self.them.change_balance(cash)
        self.show_balance()

    # Checking for win or loss
    def win_loss_check(self, market: Stock) -> bool:

        if self.them.get_balance() >= 15000:
            market.open_for_trade = False
            self.show_win()
        elif self.them.get_balance() <= 0:
            market.open_for_trade = False
            self.show_game_over()
        
    # Displaying the game over screen
    def show_game_over(self):
        pygame.draw.rect(self.surface, (0,0,0), Rect(0,50, self.WINDOW_LENGTH, self.WINDOW_HEIGHT))

        game_over_font = font.SysFont('cambria', 60)
        game_over_text = game_over_font.render("GAME OVER! YOU LOSE!", True, (255,255,255))

        self.surface.blit(game_over_text, game_over_text.get_rect(center = self.surface.get_rect().center))
        self.window.flip()

    # Displaying the win screen
    def show_win(self):
        pygame.draw.rect(self.surface, (0,0,0), Rect(0,50, self.WINDOW_LENGTH, self.WINDOW_HEIGHT))

        win_font = font.SysFont('cambria', 60)
        win_text = win_font.render("CONGRATS! YOU WON", True, (255,255,255))

        self.surface.blit(win_text, win_text.get_rect(center = self.surface.get_rect().center))
        self.window.flip()

    # Listening for certain key presses
    def listen_for_key(self, stck: Stock) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if stck.open_for_trade:
                    if not self.them.is_in_trade():
                        self.them.enter_trade()
                    else: 
                        self.them.exit_trade() 
        
        return True

    # Drawing rects that match background over the line sections
    def clear_lines(self, lines: List):
        for line in lines:
            pygame.draw.rect(self.surface, (0,0,0), line)
            self.window.flip()
        







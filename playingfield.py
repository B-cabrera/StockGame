import pygame
from player import Player
from pygame import font
from button import Button



class PlayingField(object):
    
    # Constants for window size
    WINDOW_HEIGHT = 600
    WINDOW_LENGTH = 1000

    def __init__(self):
        pygame.init()
        him = Player()
        

        # Setting up the window 
        self.window  = pygame.display
        self.surface = self.window.set_mode((self.WINDOW_LENGTH, self.WINDOW_HEIGHT))
        self.window.set_caption("Brenden Cabrera Stock Game")


        self.show_starting_balance(him)


        # Setting up the button
        green = (0,200,5)
        temp_width = 60
        buy_button = Button(self.surface, 200, (self.WINDOW_HEIGHT - temp_width - 20), 300 , temp_width, "BUY")

        # Running Loop
        running = True

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Showing the Buy button
            buy_button.draw(self.window, green)



        pygame.quit()

        


    def show_starting_balance(self, player: Player) :
        pygame.font.init()

        # Setting basic color
        white = (255,255,255)

        basicfont = font.SysFont('cambria', 40)
        balance = player.get_balance()

        text = basicfont.render("Balance: " + str(balance), True, white)

        self.surface.blit(text, (10,0))
        self.window.flip()

        








import pygame
from player import Player
from pygame import font



class PlayingField(object):

    WINDOW_HEIGHT = 600
    WINDOW_WIDTH = 1000

    def __init__(self):
        pygame.init()
        self.window  = pygame.display
        him = Player()

        self.surface = self.window.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.window.set_caption("Brenden Cabrera Stock Game")

        self.show_balance(him)

        self.exit_scenario()

        

        

    
    # Code for the exit scenario (Closing Window)
    def exit_scenario(self):
        running = True

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


        pygame.quit()

    

    def show_balance(self, player: Player) :
        pygame.font.init()

        # Setting basic color
        white = (255,255,255)

        basicfont = font.SysFont('arial', 40)
        balance = player.get_balance()

        text = basicfont.render("Balance: " + str(balance), True, white)

        self.surface.blit(text, (400,0))
        self.window.flip()

        







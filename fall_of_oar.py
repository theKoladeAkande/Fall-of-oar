import sys

import pygame


__metaclass__ = type 

class FallOfOar():
    """ Manages game's properties and assets. """

    def __init__(self):
        """Initialize game, create screen objects and other required resources. """
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Fall Of Oar")

    def run_game(self):
        """ Runs the main loop for the game. """
        while True:
            #Listens for mouse and keyboard activities
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Display the drawn screen.
            pygame.display.flip()




if __name__ == "__main__":
    # create game instance, run game
    foor = FallOfOar()
    foor.run_game()

import pygame


import os


__metaclass__ = type


class SpaceShip:
    """ A class for spaceship's activties and properties"""

    def __init__(self, foor_game):
        """Initialize the spaceship and get starting point """
        self.screen = foor_game.screen
        self.screen_rect = foor_game.screen.get_rect()
        # current_path = os.path.dirname(os.getcwd())
        image_path = os.path.join(os.getcwd(), 'images')
        space_ship_yellow_path = os.path.join(image_path, 'green_spaceship.png')
        # Load spaceship
        self.image = pygame.image.load(space_ship_yellow_path)
        self.rect = self.image.get_rect()
        # Set new spaceship's position at the center of screen
        self.rect.midbottom = self.screen_rect.midbottom


    def blitme(self):
        """ Draw the spaceship"""
        self.screen.blit(self.image, self.rect)

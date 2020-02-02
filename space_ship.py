import pygame


import os


__metaclass__ = type


class SpaceShip:
    """ A class for spaceship's activties and properties"""

    def __init__(self, foor_game):
        """Initialize the spaceship and get starting point """
        self.screen = foor_game.screen
        self.settings = foor_game.settings
        self.screen_rect = foor_game.screen.get_rect()
        image_path = os.path.join(os.getcwd(), 'images')
        space_ship_yellow_path = os.path.join(image_path, 'green_spaceship.png')
        # Load spaceship
        self.image = pygame.image.load(space_ship_yellow_path)
        self.rect = self.image.get_rect()
        # Set new spaceship's position at the center of screen
        self.rect.midbottom = self.screen_rect.midbottom
        # A decminal value for the  horizontal  position of the ship
        self.x = float(self.rect.x)
        # Flags for movement
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """ use the movement flag to update the ship's position """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.spaceship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.spaceship_speed
        self.rect.x = self.x


    def blitme(self):
        """ Draw image of the spaceship as specified by the postion"""
        self.screen.blit(self.image, self.rect)
